################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

from pytrinamic.evalboards import TMCLEval
from pytrinamic.ic import TMC4671
from pytrinamic.features import MotorControlModule, LinearRampModule


class TMC4671_eval(TMCLEval):
    """
    Use TMC4671-EVAL with Landungsbrücke/Startrampe at MC spi channel to access the TMC4671.
    """
    def __init__(self, connection, module_id=1):
        TMCLEval.__init__(self, connection, module_id)
        self.motors = [self._MotorTypeA(self, 0)]
        self.ics = [TMC4671(connection)]

    # Use the motion controller channel for register access
    def move_to(self, axis, position, velocity=None):
        if velocity:
            self.motors[axis].linear_ramp.max_velocity = velocity
        self.connection.move_to(axis, position, self.module_id)

    def move_by(self, axis, difference, velocity=None):
        if velocity:
            self.motors[axis].linear_ramp.max_velocity = velocity
        self.connection.move_by(axis, difference, self.module_id)

    def write_register(self, register_address, value):
        return self._connection.write_mc(register_address, value, self._module_id)

    def read_register(self, register_address, signed=False):
        return self._connection.read_mc(register_address, self._module_id, signed)

    class _MotorTypeA(MotorControlModule):
        def __init__(self, eval_board, axis):
            MotorControlModule.__init__(self, eval_board, axis, self.AP)
            self.linear_ramp = LinearRampModule(eval_board, axis, self.AP)


        class AP:
            MaxVelocity                    = 4
            MaxAcceleration                = 11
            EnableRamp                     = 12
            RampVelocity                   = 13
            LinearTargetPosition           = 25
            TargetTorque                   = 171
            PID_FLUX_TARGET                = 172
            PID_VELOCITY_TARGET            = 173
            TargetPosition                 = 174
            ActualTorque                   = 176
            ActualVelocity                 = 178
            ActualPosition                 = 179
            TargetTorqueRaw                = 189
            PIDIN_TARGET_FLUX              = 191
            TargetVelocity                 = 192
            torqueMeasurementFactor        = 251
            StartEncoderInitialization     = 252
            EncoderInitState               = 253
            ActualEncoderWaitTime          = 254
