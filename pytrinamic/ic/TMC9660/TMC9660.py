################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from ...ic import TMCIc
from ...modules import ParameterApiDevice

from .TMC9660_ap import Ap
from .TMC9660_bank0 import Bank0
from .TMC9660_bank2 import Bank2
from .TMC9660_bank3 import Bank3


class TMC9660(TMCIc, ParameterApiDevice):
    """TMC9660 IC class.

    The TMC9660 class provides a simple interface for communication with a TMC9660 IC.

    :cvar ap: The TMC9660's axis parameters. These are only available if parameter app is running.
    :cvar gp_bank0: The TMC9660's global parameters bank 0. These are only available if parameter app is running.
    :cvar gp_bank2: The TMC9660's global parameters bank 2. These are only available if parameter app is running.
    :cvar gp_bank3: The TMC9660's global parameters bank 3. These are only available if parameter app is running.
    """
    ap = Ap()
    
    gp_bank0 = Bank0()
    gp_bank2 = Bank2()
    gp_bank3 = Bank3()
    
    def __init__(self, connection=None, module_id=0):
        """You only need a module ID if you have multiple TMC9660 ICs on a shared RS485 bus."""

        super().__init__("TMC9660", self.__doc__)
        self._connection = connection
        self._ap_index_bit_width = 12
        self._module_id = module_id

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
