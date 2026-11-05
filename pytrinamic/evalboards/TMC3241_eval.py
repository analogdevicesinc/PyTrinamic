################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################
"""Implementation of TMC3241-EVAL"""

from pytrinamic.evalboards import TMCLEval
from pytrinamic.ic import TMC3241
from pytrinamic.ic import RegisterApiDevice
from pytrinamic.tmcl import TMCLCommand


class TMC3241_eval(TMCLEval, RegisterApiDevice):
    """Generic class for TMC3241 eval boards."""

    def __init__(self, connection, module_id=1):
        TMCLEval.__init__(self, connection, module_id)
        self._connection = connection
        self._module_id = module_id
        self.ics = [TMC3241()]

    def write_register(self, register_address, block, value):
        """Implementation of the RegisterApiDevice::write_register() function."""
        return self._connection.write_register(
            register_address, TMCLCommand.WRITE_DRV, block, value, module_id=self._module_id
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
