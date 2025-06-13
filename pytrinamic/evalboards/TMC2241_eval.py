################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Implementation of TMC2241-EVAL"""


from pytrinamic.evalboards import TMCLEval
from pytrinamic.ic import TMC2241
from pytrinamic.ic import RegisterApiDevice
from pytrinamic.tmcl import TMCLCommand
from pytrinamic.features import MotorControlModule


class TMC2241_eval(TMCLEval, RegisterApiDevice):
    """Generic class for TMC2241 eval boards."""

    def __init__(self, connection, module_id=1):
        TMCLEval.__init__(self, connection, module_id)
        self._connection = connection
        self._module_id = module_id
        self.ics = [TMC2241()]
        self.motors = [self._MotorTypeA(self, 0)]

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
    
    class _MotorTypeA(MotorControlModule):
        def __init__(self, eval_board, axis):
            MotorControlModule.__init__(self, eval_board, axis, self.AP)

        class AP:
            TargetPosition = 0
            ActualPosition = 1
            TargetVelocity = 2
            ActualVelocity = 3
            MaxVelocity = 4
            MaxAcceleration = 5
            MaxCurrent = 6