'''
Created on 09.01.2019

@author: LK, ED, LH
'''

from PyTrinamic.evalboards.TMC_EvalBoard import TMC_EvalBoard
from PyTrinamic.modules.tmcl_module import TMCLModule
from PyTrinamic.ic.TMC5130.TMC5130 import TMC5130
from PyTrinamic.features.LinearRampModule import LinearRampModule
from PyTrinamic.features.StallGuard2Module import StallGuard2Module
from PyTrinamic.features.CurrentModule import CurrentModule
from PyTrinamic.features.MotorControlModule import MotorControlModule

class TMC5130_eval(TMC_EvalBoard):
    """
    This class represents a TMC5130 Evaluation board.

    This can be used directly with the Landungsbruecke evaluation platform.
    """

    __PIN_MAP = [
        # (pin_ic, pin_board)
        (2, 15),
        (3, 22),
        (4, 23),
        (5, 24),
        (7, 25),
        (8, 9),
        (9, 10),
        (23, 4),
        (24, 6),
        (25, 5),
        (26, 30),
        (27, 29),
        (28, 28)
    ]

    def __init__(self, connection, module_id=1):
        """
        Constructor for the TMC5130 evalboard instance.

        Parameters:
        connection: TMCL connection interface instance.
        module_id: Module ID to identify the evalboard module. This is used to differentiate
        between different modules on shared busses. Default is set to 1, different
        values have to be configured with the module first.
        """
        super().__init__(connection, module_id, TMC5130(self, 0), self.EVAL_TYPES.MOTION_CONTROLLER)
        self.MOTORS = [self.MOTOR_0(self, 0)]

    class MOTOR_0(TMCLModule.Motor, LinearRampModule, StallGuard2Module, CurrentModule, MotorControlModule):
        "Motor class for the motor on axis 0."

        def __init__(self, module, axis):
            TMCLModule.Motor.__init__(self, module, axis)
            LinearRampModule.__init__(self)
            StallGuard2Module.__init__(self)
            CurrentModule.__init__(self)

        class APs():
            "Axis parameter map for this axis."
            TargetPosition                 = 0
            ActualPosition                 = 1
            TargetVelocity                 = 2
            ActualVelocity                 = 3
            MaxVelocity                    = 4
            MaxAcceleration                = 5
            RunCurrent                     = 6
            StandbyCurrent                 = 7
            PositionReachedFlag            = 8
            VREF                           = 9
            RightEndstop                   = 10
            LeftEndstop                    = 11
            AutomaticRightStop             = 12
            AutomaticLeftStop              = 13
            SWMode                         = 14
            A1                             = 15
            V1                             = 16
            MaxDeceleration                = 17
            D1                             = 18
            StartVelocity                  = 19
            StopVelocity                   = 20
            RampWaitTime                   = 21
            THIGH                          = 23
            VDCMIN                         = 24
            HighSpeedChopperMode           = 27
            HighSpeedFullstepMode          = 28
            MeasuredSpeed                  = 29
            RampMode                       = 30
            IScaleAnalog                   = 33
            InternalRSense                 = 34
            MicrostepResolution            = 140
            ChopperBlankTime               = 162
            ConstantTOffMode               = 163
            DisableFastDecayComparator     = 164
            ChopperHysteresisEnd           = 165
            ChopperHysteresisStart         = 166
            TOff                           = 167
            SEIMIN                         = 168
            SECDS                          = 169
            SmartEnergyHysteresis          = 170
            SECUS                          = 171
            SmartEnergyHysteresisStart     = 172
            SG2FilterEnable                = 173
            SG2Threshold                   = 174
            VSense                         = 179
            SmartEnergyActualCurrent       = 180
            SmartEnergyStallVelocity       = 181
            SmartEnergyThresholdSpeed      = 182
            RandomTOffMode                 = 184
            ChopperSynchronization         = 185
            PWMThresholdSpeed              = 186
            PWMGrad                        = 187
            PWMAmplitude                   = 188
            PWMFrequency                   = 191
            PWMAutoscale                   = 192
            FreewheelingMode               = 204
            LoadValue                      = 206
            EncoderPosition                = 209
            EncoderResolution              = 210
