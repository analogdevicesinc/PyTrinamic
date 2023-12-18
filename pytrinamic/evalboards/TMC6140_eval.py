################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

from pytrinamic.evalboards import TMCLEval
from pytrinamic.ic import TMC6140
from pytrinamic.features import MotorControlModule


class TMC6140_eval(TMCLEval):
    def __init__(self, connection, module_id=1):
        TMCLEval.__init__(self, connection, module_id)
        self.motors = [self._MotorTypeA(self, 0)]
        self.ics = [TMC6140()]

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

        def set_hall_direction(self, value):
            self.set_axis_parameter(self.AP.InvertHallDirection, value)

        def set_hall_order(self, value):
            self.set_axis_parameter(self.AP.HallOrder, value)

        class AP:
            TargetAngle                    = 1
            HallAngle                      = 2
            TargetPWM                      = 3
            ActualPWM                      = 4
            CommutationMode                = 5
            Current                        = 6
            InvertHallDirection            = 7
            HallOrder                      = 8
            StandbyOnDriverDisable         = 10
            ActualHallVelocity             = 16
            MotorPolePairs                 = 19

