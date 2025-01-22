################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Implementation of TMC5241-EVAL"""


from pytrinamic.ic import TMC5241
from pytrinamic.ic import RegisterApiDevice
from pytrinamic.tmcl import TMCLCommand


class TMC5241_eval(RegisterApiDevice):
    """Generic class for TMC5241 eval boards."""

    def __init__(self, connection, module_id=1):
        self._connection = connection
        self._module_id = module_id
        self.ics = [TMC5241()]

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