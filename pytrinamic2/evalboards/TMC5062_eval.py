from pytrinamic2.evalboards.tmcl_eval import TMCLEval
from pytrinamic2.ic.TMC5062.TMC5062 import TMC5062
from pytrinamic2.features import MotorControlModule
from pytrinamic2.helpers import TMC_helpers


class TMC5062_eval(TMCLEval, TMC5062):
    """
    This class represents a TMC5062 Evaluation board
    """
    def __init__(self, connection, module_id=1):
        TMCLEval.__init__(self, connection, module_id)
        TMC5062.__init__(self)
        self.motors = [self.Motor0(self, 0), self.Motor0(self, 1)]

    # Use the motion controller channel for register access

    def write_register(self, register_address, value):
        return self._connection.write_mc(register_address, value)

    def read_register(self, register_address, signed=False):
        return self._connection.read_mc(register_address, signed)

    def write_register_field(self, field, value):
        return self.write_register(field[0], TMC_helpers.field_set(self.read_register(field[0]),
                                   field[1], field[2], value))

    def read_register_field(self, field):
        return TMC_helpers.field_get(self.read_register(field[0]), field[1], field[2])

    # Motion control functions

    def rotate(self, axis, value):
        self._connection.rotate(axis, value)

    def stop(self, axis):
        self._connection.stop(axis)

    def move_to(self, axis, position, velocity=None):
        if velocity and velocity != 0:
            # Set maximum positioning velocity
            self.motors[axis].set_axis_parameter(self.motors[axis].AP.MaxVelocity, velocity)
        self._connection.move_to(axis, position, self._module_id)

    class Motor0(MotorControlModule):
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
            StandbyCurrent = 7
            PositionReachedFlag = 8
            RightEndstop = 10
            LeftEndstop = 11
            AutomaticRightStop = 12
            AutomaticLeftStop = 13
            SW_MODE = 14
            A1 = 15
            V1 = 16
            MaxDeceleration = 17
            D1 = 18
            StartVelocity = 19
            StopVelocity = 20
            RampWaitTime = 21
            smartEnergyThresholdSpeed = 22
            THIGH = 23
            VDCMIN = 24
            HighSpeedFullstepMode = 28
            MicrostepResolution = 140
            ChopperBlankTime = 162
            ConstantTOffMode = 163
            DisableFastDecayComparator = 164
            ChopperHysteresisEnd = 165
            ChopperHysteresisStart = 166
            TOff = 167
            SEIMIN = 168
            SECDS = 169
            smartEnergyHysteresis = 170
            SECUS = 171
            smartEnergyHysteresisStart = 172
            SG2FilterEnable = 173
            SG2Threshold = 174
            VSense = 179
            smartEnergyActualCurrent = 180
            resetStall = 181
            RandomTOffMode = 184
            ChopperSynchronization = 185
            LoadValue = 206
            EncoderPosition = 209
            EncoderResolution = 210
