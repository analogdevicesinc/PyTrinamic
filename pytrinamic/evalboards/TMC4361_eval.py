from pytrinamic.evalboards import TMCLEval
from pytrinamic.ic import TMC4361
from pytrinamic.features import MotorControlModule
from pytrinamic.helpers import TMC_helpers


class TMC4361_eval(TMCLEval):
    """
    This class represents a TMC4361 Evaluation board

    Communication is done over the TMCL commands writeMC and readMC. An
    implementation without TMCL may still use this class if these two functions
    are provided properly.
    """
    def __init__(self, connection, module_id=1):
        TMCLEval.__init__(self, connection, module_id)
        self.motors = [self._MotorTypeA(self, 0)]
        self.ics = [TMC4361()]

    # Use the motion controller channel for register access

    def write_register(self, register_address, value):
        return self._connection.write_mc(register_address, value, self._module_id)

    def read_register(self, register_address, signed=False):
        return self._connection.read_mc(register_address, self._module_id, signed)

    # Motion control functions

    def rotate(self, motor, value):
        self._connection.rotate(motor, value)

    def stop(self, motor):
        self._connection.stop(motor)

    def move_to(self, motor, position, velocity=None):
        if velocity and velocity != 0:
            # Set maximum positioning velocity
            self.motors[motor].set_axis_parameter(self.motors[motor].AP.MaxVelocity, velocity)
        self._connection.move_to(motor, position, self._module_id)

    class _MotorTypeA(MotorControlModule):
        def __init__(self, eval_board, axis):
            MotorControlModule.__init__(self, eval_board, axis, self.AP)

        class AP:
            TargetPosition                 = 0
            ActualPosition                 = 1
            TargetVelocity                 = 2
            ActualVelocity                 = 3
            MaxVelocity                    = 4
            MaxAcceleration                = 5
            PositionReachedFlag            = 8
            RampType                       = 14
            StartVelocity                  = 15
            AStart                         = 16
            MaxDeceleration                = 17
            VBreak                         = 18
            DFinal                         = 19
            StopVelocity                   = 20
            DSTOP                          = 21
            BOW1                           = 22
            BOW2                           = 23
            BOW3                           = 24
            BOW4                           = 25
            VirtualStopLeft                = 26
            VirtualStopRight               = 27
            PowerDownDelay                 = 214
