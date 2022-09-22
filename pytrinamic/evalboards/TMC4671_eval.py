from pytrinamic.evalboards import TMCLEval
from pytrinamic.ic import TMC4671
from pytrinamic.features import MotorControlModule
from pytrinamic.helpers import TMC_helpers


class TMC4671_eval(TMCLEval):
    """
    Use TMC4671-EVAL with Landungsbrücke/Startrampe at MC spi channel to access the TMC4671.
    """
    def __init__(self, connection, module_id=1):
        TMCLEval.__init__(self, connection, module_id)
        self.motors = [self._MotorTypeA(self, 0)]
        self.ics = [TMC4671(connection)]

    # Use the motion controller channel for register access

    def write_register(self, register_address, value):
        return self._connection.write_mc(register_address, value, self._module_id)

    def read_register(self, register_address, signed=False):
        return self._connection.read_mc(register_address, self._module_id, signed)

    class _MotorTypeA(MotorControlModule):
        def __init__(self, eval_board, axis):
            MotorControlModule.__init__(self, eval_board, axis, self.AP)

        class AP:
            MaxVelocity                    = 4
            Acceleration                   = 11
            EnableRamp                     = 12
            RampVelocity                   = 13
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
