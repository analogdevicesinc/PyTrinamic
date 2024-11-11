################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from typing import Union

from ...ic.tmc_ic import TMCIc, UblApiDevice
from ...modules import Parameter
from ...tmcl import TMCLCommand

from .TMC9660_ap import Ap
from .TMC9660_bank0 import Bank0
from .TMC9660_bank2 import Bank2
from .TMC9660_bank3 import Bank3
from .MCCmap import MCCMap
from .ADCmap import ADCMap
from .SYS_CTRLmap import SYS_CTRLMap
from .GPIOmap import GPIOMap
from .SPI0map import SPI0Map
from .SPI1map import SPI1Map
from .I2Cmap import I2CMap
from .TIM_ADVmap import TIM_ADVMap


class TMC9660(TMCIc, UblApiDevice):
    """TMC9660 IC class.

    The TMC9660 class provides a simple interface for communication with a TMC9660 IC.

    :cvar ap: The TMC9660's axis parameters. These are only available if parameter app is running.
    :cvar gp_bank0: The TMC9660's global parameters bank 0. These are only available if parameter app is running.
    :cvar gp_bank2: The TMC9660's global parameters bank 2. These are only available if parameter app is running.
    :cvar gp_bank3: The TMC9660's global parameters bank 3. These are only available if parameter app is running.
    :cvar MCC: The TMC9660's motion controller core registers. These are only available if register app is running.
    :cvar ADC: The TMC9660's ADC registers. These are only available if register app is running.
    :cvar SYS_CTRL: The TMC9660's system control registers. These are only available if register app is running.
    :cvar GPIO: The TMC9660's GPIO registers. These are only available if register app is running.
    :cvar SPI0: The TMC9660's SPI0 registers. These are only available if register app is running.
    :cvar SPI1: The TMC9660's SPI1 registers. These are only available if register app is running.
    :cvar I2C: The TMC9660's I2C registers. These are only available if register app is running.
    :cvar TIM_ADV: The TMC9660's advanced timer registers. These are only available if register app is running.
    """
    ap = Ap()
    
    gp_bank0 = Bank0()
    gp_bank2 = Bank2()
    gp_bank3 = Bank3()

    MCC = MCCMap(block=0).ALL_REGISTERS
    ADC = ADCMap(block=1).ALL_REGISTERS
    SYS_CTRL = SYS_CTRLMap(block=2).ALL_REGISTERS
    GPIO = GPIOMap(block=4).ALL_REGISTERS
    SPI0 = SPI0Map(block=7).ALL_REGISTERS
    SPI1 = SPI1Map(block=8).ALL_REGISTERS
    I2C = I2CMap(block=10).ALL_REGISTERS
    TIM_ADV = TIM_ADVMap(block=14).ALL_REGISTERS
    
    def __init__(self, connection=None, module_id=0):
        """You only need a module ID if you have multiple TMC9660 ICs on a shared RS485 bus."""

        super().__init__("TMC9660", self.__doc__)
        self._connection = connection
        self.ap_index_bit_width = 12
        self.module_id = module_id

    def write_register(self, register_address, block, value):
        """Implementation of the UblApiDevice::write_register() function."""
        return self._connection.write_register(register_address, TMCLCommand.WRITE_MC, block, value, self.module_id)

    def read_register(self, register_address, block, signed=False):
        """Implementation of the UblApiDevice::read_register() function."""
        return self._connection.read_register(register_address, TMCLCommand.READ_MC, block, self.module_id, signed)

    def get_axis_parameter(self, ap: Union[Parameter, int]):
        return self._connection.get_axis_parameter(ap, 0, self.module_id, index_bit_width=self.ap_index_bit_width)

    def set_axis_parameter(self, ap: Union[Parameter, int], value: int):
        return self._connection.set_axis_parameter(ap, 0, value, self.module_id, self.ap_index_bit_width)

    def get_global_parameter(self, gp: Union[Parameter, int], bank: int):
        return self._connection.get_global_parameter(gp, bank, self.module_id)

    def set_global_parameter(self, gp: Union[Parameter, int], bank:int, value: int):
        return self._connection.set_global_parameter(gp, bank, value, self.module_id)