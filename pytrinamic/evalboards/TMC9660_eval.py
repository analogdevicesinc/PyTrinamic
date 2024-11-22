################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Implementation of TMC9660 eval boards.

The following eval boards are implemented:

* TMC9660-3PH-EVAL
* TMC9660-STEPPER-EVAL

"""

from pytrinamic.modules import ParameterApiDevice
from pytrinamic.ic import TMC9660


class TMC9660_eval(ParameterApiDevice):
    """Generic class for TMC9660 eval boards."""
    def __init__(self, connection, default_module_id=3):
        self._connection = connection
        self._ap_index_bit_width = 12
        self._module_id = default_module_id
        self.ics = [TMC9660()]
    
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


class TMC9660_3PH_eval(TMC9660_eval):
    """Representation of the TMC9660-3PH-EVAL."""
    pass


class TMC9660_STEPPER_eval(TMC9660_eval):
    """Representation of the TMC9660-STEPPER-EVAL."""
    pass