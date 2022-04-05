from pytrinamic.tmcl import TMCLCommand
from enum import IntEnum

class RAMDebug_Command(IntEnum):
    INIT                        =  0
    SET_SAMPLE_COUNT            =  1
    SET_SAMPLING_SOURCE         =  2 # Placeholder
    SET_PRESCALER               =  3
    SET_CHANNEL                 =  4
    SET_TRIGGER_CHANNEL         =  5
    SET_SHIFT_MASK              =  6
    ENABLE_TRIGGER              =  7
    GET_STATE                   =  8
    GET_SAMPLE                  =  9
    GET_INFO                    = 10
    GET_CHANNEL_TYPE            = 11
    GET_CHANNEL_ADDRESS         = 12
    SET_PRETRIGGER_SAMPLE_COUNT = 13
    GET_PRETRIGGER_SAMPLE_COUNT = 14
    SET_PROCESS_FREQUENCY       = 15
    SET_TYPE                    = 16
    SET_EVAL_CHANNEL            = 17
    SET_ADDRESS                 = 18
    SET_TRIGGER_TYPE            = 19
    SET_TRIGGER_EVAL_CHANNEL    = 20
    SET_TRIGGER_ADDRESS         = 21

class RAMDebug_Channel(IntEnum):
    CHANNEL_CAPTURE_DISABLED = 0
    CHANNEL_AXIS_PARAMETER   = 1
    CHANNEL_REGISTER         = 2
    CHANNEL_STACKED_REGISTER = 3
    CHANNEL_SYSTICK          = 4
    CHANNEL_MEMORY_ADDRESS   = 5
    CHANNEL_ANALOG_INPUT     = 6

class RAMDebug_Info(IntEnum):
    INFO_MAX_CHANNELS       = 0
    INFO_BUFFER_ELEMENTS    = 1
    INFO_SAMPLING_FREQUENCY = 2
    INFO_CAPTURED_SAMPLES   = 3

class RAMDebug_Trigger(IntEnum):
    TRIGGER_UNCONDITIONAL         = 0
    TRIGGER_RISING_EDGE_SIGNED    = 1
    TRIGGER_FALLING_EDGE_SIGNED   = 2
    TRIGGER_DUAL_EDGE_SIGNED      = 3
    TRIGGER_RISING_EDGE_UNSIGNED  = 4
    TRIGGER_FALLING_EDGE_UNSIGNED = 5
    TRIGGER_DUAL_EDGE_UNSIGNED    = 6

class RAMDebug_State(IntEnum):
    IDLE           = 0
    TRIGGER        = 1
    CAPTURE        = 2
    COMPLETE       = 3
    PRETRIGGER     = 4

class Channel():
    def __init__(self, channel_type, value, address = 0, signed = False, mask = 0xFFFF_FFFF, shift = 0, eval_channel = 0): #TODO: add signed
        self.value = value
        self.type = channel_type
        self.shift = shift
        self.mask = mask
        self.address = address
        self.signed = signed
        self.eval_channel = eval_channel

    @classmethod
    def axis_parameter(cls, motor, parameter_nr, eval_channel=0):
        channel_type = RAMDebug_Channel.CHANNEL_AXIS_PARAMETER
        value = ((motor << 24) & 0xFF00_0000) | (parameter_nr & 0x0000_00FF)
        # Error if value is bigger than 8 bits
        return cls(channel_type, value, eval_channel=eval_channel)

    @classmethod
    def register(cls, motor, address, signed=False, eval_channel=0):
        channel_type = RAMDebug_Channel.CHANNEL_REGISTER
        value = ((motor << 24) & 0xFF00_0000) | (address & 0x0000_FFFF)

        # Error if value is bigger than 8 bits
        return cls(channel_type, value, address, signed, eval_channel=eval_channel)

    @classmethod
    def stacked_register(cls, motor, data_address, selector_address, value, eval_channel=0):
        channel_type = RAMDebug_Channel.CHANNEL_STACKED_REGISTER
        value = ((motor << 24) & 0xFF00_0000) | (value << 16 & 0x00FF_0000) | (selector_address << 8 & 0x0000_FF00) | (data_address & 0x0000_00FF)
        # Error if value is bigger than 8 bits
        return cls(channel_type, value, eval_channel=eval_channel)

    @classmethod
    def field(cls, motor, field, signed=False, eval_channel=0):
        channel_type = RAMDebug_Channel.CHANNEL_REGISTER

        address = field[0]
        mask    = field[1]
        shift   = field[2]

        value = ((motor << 24) & 0xFF00_0000) | (address & 0x0000_FFFF)

        return cls(channel_type, value, address, signed, mask, shift, eval_channel=eval_channel)

    @classmethod
    def memory_address(cls, address):
        channel_type = RAMDebug_Channel.CHANNEL_MEMORY_ADDRESS
        value = address
        return cls(channel_type, value, address)

    @classmethod
    def analog_input(cls, number):
        channel_type = RAMDebug_Channel.CHANNEL_ANALOG_INPUT
        value = number

        # Error if value is bigger than 8 bits
        return cls(channel_type, number)

class RAMDebug():
    def __init__(self, connection):
        self._connection = connection

        # Read out the constant RAMDEBUG parameters
        self.MAX_CHANNELS  = self._command(RAMDebug_Command.GET_INFO.value, 0, RAMDebug_Info.INFO_MAX_CHANNELS.value).value
        self.MAX_ELEMENTS  = self._command(RAMDebug_Command.GET_INFO.value, 0, RAMDebug_Info.INFO_BUFFER_ELEMENTS.value).value
        self.MAX_FREQUENCY = self._command(RAMDebug_Command.GET_INFO.value, 0, RAMDebug_Info.INFO_SAMPLING_FREQUENCY.value).value

        self._prescaler = 0
        self._process_frequency = 1000
        self._sample_count = self.MAX_ELEMENTS
        self._pretrigger_samples = 0
        self._trigger_channel = Channel(RAMDebug_Channel.CHANNEL_CAPTURE_DISABLED, 0, 0, 0, 0)
        self._trigger_type = RAMDebug_Trigger.TRIGGER_UNCONDITIONAL
        self._trigger_threshold = 0
        self._trigger_mask = 0x0000_0000
        self._trigger_shift = 0x0000_0000
        self.channels = []
        self.samples = []

    def get_sample_count(self):
        return self._sample_count

    def set_sample_count(self, sample_count):
        self._sample_count = sample_count

    def get_process_frequency(self):
        return self._process_frequency

    def set_process_frequency(self, process_frequency):
        self._process_frequency = process_frequency

    def set_prescaler(self, prescaler):
        self._prescaler = prescaler

    def set_trigger_type(self, trigger_type):
        if isinstance(trigger_type, RAMDebug_Trigger):
            self._trigger_type = trigger_type

    def set_trigger_threshold(self, trigger_threshold):
        self._trigger_threshold = trigger_threshold

    def set_trigger_channel(self, channel):
        if isinstance(channel, Channel):
            self._trigger_channel = channel
            self._trigger_mask = channel._mask
            self._trigger_shift = channel._shift


    def set_pretrigger_samples(self, pretrigger_samples):
        self._pretrigger_samples = pretrigger_samples

    def set_channel(self, channel):
        if self.channel_count() >= self.MAX_CHANNELS:
            raise RuntimeError("Out of channels!")

        self.channels.append(channel)

    def get_channels(self):
        return self.channels

    def start_measurement_module(self):
        self._command(RAMDebug_Command.INIT.value, 0, 0)
        self._command(RAMDebug_Command.SET_SAMPLE_COUNT.value, 0, self.get_total_samples())
        self._command(RAMDebug_Command.SET_PRESCALER.value, 0, self._prescaler)
        for channel in self.channels:
            self._command(RAMDebug_Command.SET_CHANNEL.value, channel.type.value, channel.value)

        self._command(RAMDebug_Command.SET_SHIFT_MASK.value, self._trigger_shift, self._trigger_mask)
        self._command(RAMDebug_Command.SET_PRETRIGGER_SAMPLE_COUNT.value, 0, self._pretrigger_samples * self.channel_count())
        self._command(RAMDebug_Command.SET_TRIGGER_CHANNEL.value, self._trigger_channel.type.value, self._trigger_channel.value)
        self._command(RAMDebug_Command.ENABLE_TRIGGER.value, self._trigger_type.value, self._trigger_threshold)

    def start_measurement_eval(self):
        self._command(RAMDebug_Command.INIT.value, 0, 0)
        self._command(RAMDebug_Command.SET_SAMPLE_COUNT.value, 0, self.get_total_samples())
        self._command(RAMDebug_Command.SET_PROCESS_FREQUENCY, 0, self._process_frequency)
        self._command(RAMDebug_Command.SET_PRESCALER.value, 0, self._prescaler)
        for channel in self.channels:
            self._command(RAMDebug_Command.SET_EVAL_CHANNEL.value, 0, channel.eval_channel)
            self._command(RAMDebug_Command.SET_ADDRESS.value, 0, channel.value)
            self._command(RAMDebug_Command.SET_TYPE.value, 0, channel.type.value)

        self._command(RAMDebug_Command.SET_SHIFT_MASK.value, self._trigger_shift, self._trigger_mask)
        self._command(RAMDebug_Command.SET_PRETRIGGER_SAMPLE_COUNT.value, 0, self._pretrigger_samples * self.channel_count())
        self._command(RAMDebug_Command.SET_TRIGGER_TYPE.value, 0, self._trigger_channel.type.value)
        self._command(RAMDebug_Command.SET_TRIGGER_EVAL_CHANNEL.value, 0, self._trigger_channel.eval_channel)
        self._command(RAMDebug_Command.SET_TRIGGER_ADDRESS.value, 0, self._trigger_channel.value)
        self._command(RAMDebug_Command.ENABLE_TRIGGER.value, self._trigger_type.value, self._trigger_threshold)

    def start_measurement(self, is_eval=False):
        if(is_eval):
            self.start_measurement_eval()
        else:
            self.start_measurement_module()

    def is_measurement_done(self):
        return self.get_state() == RAMDebug_State.COMPLETE.value

    def get_samples(self):
        i = 0
        data = []

        while i < self.get_total_samples():
            reply = self._command(RAMDebug_Command.GET_SAMPLE.value, 0, i)
            done = reply.status != 0x64
            if done:
                break
            data.append(reply.value)

            i += 1

        # Split data into list for each channel and apply mask/shift to samples on each channel
        self.samples = []
        for i in range(self.channel_count()):
            # Extract the channel data out of the raw buffer
            values = data[i::self.channel_count()]

            # Apply mask/shift
            mask  = self.channels[i].mask
            shift = self.channels[i].shift
            values = [(x & mask) >> shift for x in values]

            # Apply signedness
            if self.channels[i].signed:
                bits = bin(mask).count("1")
                values = [self.__to_signed(x, bits) for x in values]

            self.samples.append(values)

        return self.samples

    @staticmethod
    def __to_signed(value, bits):
        mask = 1<<(bits-1)
        return (value ^ mask) - mask

    # Calculates total number of samples across all channels
    def get_total_samples(self):
        if (self._sample_count * self.channel_count() > self.MAX_ELEMENTS) | self._sample_count == 0:
            return self.MAX_ELEMENTS
        else:
            return self._sample_count * self.channel_count()


    def channel_count(self):
        return len(self.channels)

    def get_state(self):
        return self._command(RAMDebug_Command.GET_STATE.value, 0, 0).value

    def __str__(self):
        text  = f"RAMDebug handler for connection {self._connection}\n"
        text += f"\tMaximum channels:      {self.MAX_CHANNELS}\n"
        text += f"\tMaximum samples:       {self.MAX_ELEMENTS}\n"
        text += f"\tMaximum sampling rate: {self.MAX_FREQUENCY}"

        return text

    def _command(self, cmd_type, motor, value):
        """
        Helper wrapper for sending RAMDebug TMCL opcodes
        """
        return self._connection.send(TMCLCommand.RAMDEBUG, cmd_type, motor, value)
