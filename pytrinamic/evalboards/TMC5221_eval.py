################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################
"""Implementation of TMC5221-EVAL"""
 
 
from pytrinamic.ic import TMC5221
from pytrinamic.ic import RegisterApiDevice
from pytrinamic.tmcl import TMCLCommand
 
 
class TMC5221_eval(RegisterApiDevice):
    """Generic class for TMC5221 eval boards."""
 
    def __init__(self, connection, module_id=1):
        self._connection = connection
        self._module_id = module_id
        self.ics = [TMC5221()]
 
    def write_register(self, register_address, block, value):
        """Implementation of the RegisterApiDevice::write_register() function."""
        return self._connection.write_register(
            register_address,
            TMCLCommand.WRITE_MC,
            block,
            value,
            module_id=self._module_id
        )
 
    def read_register(self, register_address, block, signed=False):
        """Implementation of the RegisterApiDevice::read_register() function."""
        return self._connection.read_register(
            register_address,
            TMCLCommand.READ_MC,
            block,
            module_id=self._module_id,
            signed=signed,
        )