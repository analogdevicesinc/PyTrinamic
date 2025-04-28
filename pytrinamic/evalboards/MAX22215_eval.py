################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Implementation of MAX22215-EVAL"""
 
 
from pytrinamic.ic import MAX22215
from pytrinamic.ic import RegisterApiDevice
from pytrinamic.tmcl import TMCLCommand
 
 
class MAX22215_eval(RegisterApiDevice):
    """Generic class for MAX22215 eval boards."""
 
    def __init__(self, connection, module_id=1):
        self._connection = connection
        self._module_id = module_id
        self.ics = [MAX22215()]
 
    def write_register(self, register_address, block, value):
        """Implementation of the RegisterApiDevice::write_register() function."""
        return self._connection.write_register(
            register_address,
            TMCLCommand.WRITE_DRV,
            block,
            value,
            module_id=self._module_id
        )
 
    def read_register(self, register_address, block, signed=False):
        """Implementation of the RegisterApiDevice::read_register() function."""
        return self._connection.read_register(
            register_address,
            TMCLCommand.READ_DRV,
            block,
            module_id=self._module_id,
            signed=signed,
        )