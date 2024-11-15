################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Implementation of TMC9660 eval boards.

The following eval boards are implemented:

* TMC9660-3PH-EVAL
* TMC9660-STEPPER-EVAL

"""
from typing import Union

from pytrinamic.modules import Parameter
from pytrinamic.ic import TMC9660
from pytrinamic.ic.tmc_ic import UblApiDevice
from pytrinamic.tmcl import TMCLCommand


class TMC9660_eval(UblApiDevice):
    """Generic class for TMC9660 eval boards."""
    def __init__(self, connection, default_module_id=3):
        self._connection = connection
        self._ap_index_bit_width = 12
        self._module_id = default_module_id
        self.ics = [TMC9660()]

    def write_register(self, register_address, block, value):
        """Implementation of the UblApiDevice::write_register() function."""
        return self._connection.write_register(
            register_address,
            TMCLCommand.WRITE_MC,
            block,
            value,
            module_id=self._module_id
        )

    def read_register(self, register_address, block, signed=False):
        """Implementation of the UblApiDevice::read_register() function."""
        return self._connection.read_register(
            register_address,
            TMCLCommand.READ_MC,
            block,
            module_id=self._module_id,
            signed=signed,
        )
        
    def get_axis_parameter(self, ap: Parameter):
        signed = True if ap.datatype == Parameter.Datatype.SIGNED else False
        return self._connection.get_axis_parameter(
            ap.index,
            0,
            signed,
            module_id=self._module_id,
            index_bit_width=self._ap_index_bit_width,
        )

    def set_axis_parameter(self, ap: Parameter, value):
        return self._connection.set_axis_parameter(
            ap.index,
            0,
            value,
            module_id=self._module_id,
            index_bit_width=self._ap_index_bit_width,
        )

    def get_global_parameter(self, gp: Parameter, bank):
        signed = True if gp.datatype == Parameter.Datatype.SIGNED else False
        return self._connection.get_global_parameter(
            gp.index,
            bank,
            signed,
            module_id=self._module_id,
        )

    def set_global_parameter(self, gp: Parameter, bank, value):
        return self._connection.set_global_parameter(
            gp.index,
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