from pytrinamic.evalboards import TMCLEval
from pytrinamic.ic import TMC6300
from pytrinamic.features import MotorControlModule
from pytrinamic.helpers import TMC_helpers


class TMC6300_eval(TMCLEval):
    def __init__(self, connection, module_id=1):
        TMCLEval.__init__(self, connection, module_id)
        self.motors = [self._MotorTypeA(self, 0)]
        self.ics = [TMC6300()]

    # Motion control functions

    def rotate(self, motor, value):
        self._connection.rotate(motor, value)

    def stop(self, motor):
        self._connection.stop(motor)

    class _MotorTypeA(MotorControlModule):
        def __init__(self, eval_board, axis):
            MotorControlModule.__init__(self, eval_board, axis, self.AP)

        def set_target_pwm(self, value):
            self.set_axis_parameter(self.AP.TargetPWM, value)

        def set_commutation_mode(self, value):
            self.set_axis_parameter(self.AP.CommutationMode, value)

        def set_standby_current(self, value):
            self.set_axis_parameter(self.AP.ICStandby, value)

        def set_hall_direction(self, value):
            self.set_axis_parameter(self.AP.HallDirection, value)

        def set_hall_order(self, value):
            self.set_axis_parameter(self.AP.HallOrder, value)

        class AP:
            ActualControlledAngle          = 1
            ActualHallAngle                = 2
            ActualPWM                      = 3
            TargetPWM                      = 4
            CommutationMode                = 5
            OpenLoopStepTime               = 6
            Current                        = 7
            HallDirection                  = 8
            HallOrder                      = 9
            ICStandby                      = 10
            VMMeasurement                  = 11
