################################################################################
# Copyright © 2026 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from pytrinamic.evalboards import TMCLEval
from pytrinamic.ic import RegisterApiDevice
from pytrinamic.ic import TMC6460
from pytrinamic.tmcl import TMCLCommand
from pytrinamic.datalogger import DataLogger


class TMC6460_eval(RegisterApiDevice):
    """TMC6460-EVAL class.
    """
    def __init__(self, connection, module_id=1):
        self._connection = connection
        self._module_id = module_id
        self.ics = [TMC6460()]
        self.datalogger = DataLogger(connection, module_id)

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