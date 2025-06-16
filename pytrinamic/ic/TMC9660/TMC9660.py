################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from ...ic import TMCIc, RegisterApiDevice
from ...modules import ParameterApiDevice
from ...tmcl import TMCLCommand
from ...datalogger import DataLogger

from .TMC9660_ap import Ap
from .TMC9660_gpbank0 import GpBank0
from .TMC9660_gpbank2 import GpBank2
from .TMC9660_gpbank3 import GpBank3
from .MCCmap import _ALL_REGISTERS as MccRegisterGroup
from .ADCmap import _ALL_REGISTERS as AdcRegisterGroup
from .SYS_CTRLmap import _ALL_REGISTERS as SysCtrlRegisterGroup


class TMC9660(TMCIc, RegisterApiDevice, ParameterApiDevice):
    """TMC9660 IC class.

    The TMC9660 class provides a simple interface for communication with a TMC9660 IC.

    :cvar ap: The TMC9660's axis parameters. These are only available if parameter app is running.
    :cvar gp_bank0: The TMC9660's global parameters bank 0. These are only available if parameter app is running.
    :cvar gp_bank2: The TMC9660's global parameters bank 2. These are only available if parameter app is running.
    :cvar gp_bank3: The TMC9660's global parameters bank 3. These are only available if parameter app is running.
    :cvar MCC: The TMC9660's motion controller core registers. These are only available if register app is running.
    :cvar ADC: The TMC9660's ADC registers. These are only available if register app is running.
    :cvar SYS_CTRL: The TMC9660's system control registers. These are only available if register app is running.
    :cvar IO: The TMC9660's IOs
    """

    class _Io:
        class Gpio:
            def __init__(self, index):
                self.index = index

            @property
            def name(self):
                return f"GPIO{self.index}"

        def __init__(self):
            self.GPIO0  = self.Gpio(0)
            self.GPIO1  = self.Gpio(1)
            self.GPIO2  = self.Gpio(2)
            self.GPIO3  = self.Gpio(3)
            self.GPIO4  = self.Gpio(4)
            self.GPIO5  = self.Gpio(5)
            self.GPIO6  = self.Gpio(6)
            self.GPIO7  = self.Gpio(7)
            self.GPIO8  = self.Gpio(8)
            self.GPIO9  = self.Gpio(9)
            self.GPIO10 = self.Gpio(10)
            self.GPIO11 = self.Gpio(11)
            self.GPIO12 = self.Gpio(12)
            self.GPIO13 = self.Gpio(13)
            self.GPIO14 = self.Gpio(14)
            self.GPIO15 = self.Gpio(15)
            self.GPIO16 = self.Gpio(16)
            self.GPIO17 = self.Gpio(17)
            self.GPIO18 = self.Gpio(18)

    ap = Ap()
    
    gp_bank0 = GpBank0()
    gp_bank2 = GpBank2()
    gp_bank3 = GpBank3()

    MCC = MccRegisterGroup(channel=0, block=0, width=None)
    ADC = AdcRegisterGroup(channel=0, block=1, width=None)
    SYS_CTRL = SysCtrlRegisterGroup(channel=0, block=2, width=None)

    IO = _Io()
    
    def __init__(self, connection=None, module_id=0):
        """You only need a module ID if you have multiple TMC9660 ICs on a shared RS485 bus."""

        super().__init__("TMC9660", self.__doc__)

        self._connection = connection
        self._ap_index_bit_width = 12
        self._module_id = module_id
        self.datalogger = DataLogger(connection, module_id=module_id)

    def write_register(self, register_address, block, value):
        """Implementation of the RegisterApiDevice::write_register() function."""
        return self._connection.write_register(register_address, TMCLCommand.WRITE_MC, block, value, self._module_id, address_bit_width=11)

    def read_register(self, register_address, block, signed=False):
        """Implementation of the RegisterApiDevice::read_register() function."""
        return self._connection.read_register(register_address, TMCLCommand.READ_MC, block, self._module_id, signed, address_bit_width=11)
    
    def _get_axis_parameter(self, index: int, signed: bool):
        """Implementation of the ParameterApiDevice::_get_axis_parameter() function."""
        return self._connection.get_axis_parameter(
            index,
            0,
            module_id=self._module_id,
            signed=signed,
            index_bit_width=self._ap_index_bit_width,
        )

    def _set_axis_parameter(self, index: int, value: int):
        """Implementation of the ParameterApiDevice::_set_axis_parameter() function."""
        return self._connection.set_axis_parameter(
            index,
            0,
            value,
            module_id=self._module_id,
            index_bit_width=self._ap_index_bit_width,
        )

    def _get_global_parameter(self, index: int, bank: int, signed: bool):
        """Implementation of the ParameterApiDevice::_get_global_parameter() function."""
        return self._connection.get_global_parameter(
            index,
            bank,
            module_id=self._module_id,
            signed=signed,
        )

    def _set_global_parameter(self, index, bank, value):
        """Implementation of the ParameterApiDevice::_set_global_parameter() function."""
        return self._connection.set_global_parameter(
            index,
            bank,
            value,
            module_id=self._module_id,
        )
