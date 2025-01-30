"""Draft of a new shiny RAMDebug implementation

TODO:
* Add pre-trigger and its config parameters
* Field merge and extraction
* Write more tests against TMCM-1617 -> use latest firmware on the master branch of TMCL-Weasel
* Add the option to use a list of Parameter/Register/Filed objects for log_data
"""

from __future__ import annotations
from dataclasses import dataclass
from enum import IntEnum

from pytrinamic.rd import Rd
from pytrinamic.modules.tmcl_module import Parameter
from pytrinamic.ic.tmc_ic import Register, Field
from pytrinamic.helpers import to_signed_32


class DataLoggerConfigError(Exception):
    pass


class DataLogger:

    @dataclass
    class Info:
        base_frequency_hz: int
        sample_buffer_length: int
        number_of_channels: int

    class DataType:
        pass

    class DataTypeAp(DataType):
        def __init__(self, index, axis=0, signed=False):
            self.index = index
            self.axis = axis
            self.signed = signed

        @classmethod
        def from_parameter(cls, parameter: Parameter, axis: int = 0) -> DataLogger.DataTypeAp:
            return cls(
                index=parameter.index,
                axis=axis,
                signed=(parameter.datatype==Parameter.Datatype.SIGNED),
            )

    class DataTypeGp(DataType):
        def __init__(self, index, bank=0, signed=False):
            self.index = index
            self.bank = bank
            self.signed = signed

        @classmethod
        def from_parameter(cls, parameter: Parameter) -> DataLogger.DataTypeGp:
            return cls(
                index=parameter.index,
                bank=parameter.block,
                signed=(parameter.datatype==Parameter.Datatype.SIGNED),
            )
    
    class DataTypeRegister(DataType):
        def __init__(self, block, channel, address, signed=False):
            self.block = block
            self.channel = channel
            self.address = address
            self.signed = signed

        @classmethod
        def from_register(cls, register: Register, channel) -> DataLogger.DataTypeRegister:
            return cls(
                block=register.block,
                channel=channel,
                address=register.address,
                signed=register.signed,
            )
        
    class DataTypeField(DataType):
        def __init__(self, block, field, channel, signed=False):
            self.block = block
            self.channel = channel
            self.address = field[0]
            self.mask = field[1]
            self.shift = field[2]
            self.signed = signed

        @classmethod
        def from_field(cls, field: Field, channel) -> DataLogger.DataTypeField:
            return cls(
                block=field.parent.block,
                channel=channel,
                address=field.parent.address,
                mask=field.mask,
                shift=field.shift
            )

        def get(self, register_value) -> int:
            value = (register_value & self.mask) >> self.shift
            if self.signed:
                base_mask = self.mask >> self.shift
                sign_mask = base_mask & (~base_mask >> 1)
                value = (value ^ sign_mask) - sign_mask
            return value

    @dataclass
    class Log:
        rate_hz: float
        samples: list

    class TriggerType(IntEnum):
        UNCONDITIONAL         = 0
        RISING_EDGE_SIGNED    = 1
        FALLING_EDGE_SIGNED   = 2
        DUAL_EDGE_SIGNED      = 3
        RISING_EDGE_UNSIGNED  = 4
        FALLING_EDGE_UNSIGNED = 5
        DUAL_EDGE_UNSIGNED    = 6

    @dataclass
    class Config:
        down_sampling_factor: int
        samples_per_channel: int
        log_data: dict
        trigger_type: None
        trigger_on: None
        trigger_threshold: int

    def __init__(self, connection, module_id):
        self.rd = Rd(connection, module_id)
        self.config = DataLogger.Config(
            down_sampling_factor=1,
            samples_per_channel=0,
            log_data={},
            trigger_type=self.TriggerType.UNCONDITIONAL,
            trigger_on=None,
            trigger_threshold=None,
        )
        self.logs = {}
        self._info = None
        self._channels_used_count = 0
        self._total_number_of_samples = 0
        self._download_is_done = True
        self._download_offset = 0
        self._downloaded_raw_data = []

    def get_info(self) -> DataLogger.Info:
        return DataLogger.Info(
            base_frequency_hz=self.rd.get_info(Rd.Info.SAMPLING_FREQUENCY),
            sample_buffer_length=self.rd.get_info(Rd.Info.BUFFER_ELEMENTS),
            number_of_channels=self.rd.get_info(Rd.Info.MAX_CHANNELS),
        )

    def activate_trigger(self) -> None:
        if self.config.samples_per_channel == 0:
            raise DataLoggerConfigError("No samples per channel specified!")
        self._info = self.get_info()
        self._channels_used_count = len(self.config.log_data)
        self._total_number_of_samples = self.config.samples_per_channel*self._channels_used_count
        if self._channels_used_count > self._info.number_of_channels:
            raise DataLoggerConfigError("Exceeding number of channels!")
        if self._total_number_of_samples > self._info.sample_buffer_length:
            raise DataLoggerConfigError("Samples per channel exceeds sample buffer length!")
        self.rd.init()
        self.rd.set_sample_count(self.config.samples_per_channel*self._channels_used_count)
        self.rd.set_prescaler(self.config.down_sampling_factor)
        if self.config.trigger_type != self.TriggerType.UNCONDITIONAL:
            if self.config.trigger_on is None:
                raise DataLoggerConfigError("Trigger type specified but no trigger data given in `config.trigger_on`!")
            channel_type, select = self._get_channel_type_and_select(datatype=self.config.trigger_on)
            self.rd.set_trigger_channel(channel_type=channel_type, select=select)
        
        for datatype in self.config.log_data.values():
            channel_type, select = self._get_channel_type_and_select(datatype=datatype)
            self.rd.set_channel(
                channel_type=channel_type,
                select=select
            )

        if self.config.trigger_type == self.TriggerType.UNCONDITIONAL:
            self.rd.enable_trigger(self.config.trigger_type, 0)
        else:
            if self.config.trigger_threshold is None:
                raise DataLoggerConfigError("Trigger type specified is conditional but no threshold given in `config.trigger_threshold!")
            self.rd.enable_trigger(self.config.trigger_type, self.config.trigger_threshold)


    def got_triggered(self) -> bool:
        return self.rd.get_state() >= Rd.State.CAPTURE

    def is_done(self) -> bool:
        return self.rd.get_state() == Rd.State.COMPLETE

    def download_logs_step(self) -> bool:
        self._download_is_done = False
        self._downloaded_raw_data.append(self.rd.get_sample(self._download_offset))
        self._download_offset += 1
        if self._download_offset < self._total_number_of_samples:
            return True

        self.logs = {}
        for i in range(len(self.config.log_data)):
            name, datatype = list(self.config.log_data.items())[i]
            samples = self._downloaded_raw_data[i::self._channels_used_count]
            if isinstance(datatype, DataLogger.DataTypeField):
                samples = [datatype.get(sample) for sample in samples]
            else:
                if datatype.signed:
                    samples = [to_signed_32(sample) for sample in samples]
            self.logs[name] = DataLogger.Log(
                rate_hz=self._info.base_frequency_hz/self.config.down_sampling_factor,
                samples=samples
            )
        self._downloaded_raw_data = []
        self._download_offset = 0
        self._download_is_done = True
        return False
    
    def download_logs(self) -> None:
        while self.download_logs_step():
            pass

    def _get_channel_type_and_select(self, datatype):
        if isinstance(datatype, DataLogger.DataTypeAp):
            select = ((datatype.axis << 24) & 0xFF00_0000) | ((datatype.index << 0) & 0x00FF_FFFF)
            return self.rd.Channel.AXIS_PARAMETER, select
        elif isinstance(datatype, DataLogger.DataTypeGp):
            select = ((datatype.bank << 24) & 0xFF00_0000) | ((datatype.index << 0) & 0x00FF_FFFF)
            return self.rd.Channel.GLOBAL_PARAMETER, select
        elif isinstance(datatype, DataLogger.DataTypeRegister) or isinstance(datatype, DataLogger.DataTypeField):
            select = ((datatype.block << 24) & 0xFF00_0000) | (datatype.address & 0x00FF_FFFF)
            return self.rd.Channel.REGISTER, select
        else:
            raise ValueError("Unknown DataType")
        
    @property
    def download_progress(self) -> float:
        if self._download_is_done:
            return 100.0
        else:
            return 100*self._download_offset/self._total_number_of_samples