'''
Created on 09.01.2019

@author: LK, ED, LH
'''

from PyTrinamic.evalboards.TMC_EvalBoard import TMC_EvalBoard
from PyTrinamic.modules.tmcl_module import TMCLModule
from PyTrinamic.ic.TMC5072.TMC5072 import TMC5072
from PyTrinamic.features.LinearRampModule import LinearRampModule
from PyTrinamic.features.StallGuard2Module import StallGuard2Module
from PyTrinamic.features.CurrentModule import CurrentModule
from PyTrinamic.features.MotorControlModule import MotorControlModule

class TMC5072_eval(TMC_EvalBoard):
    """
    This class represents a TMC5072 Evaluation board
    """

    def __init__(self, connection, module_id=1):
        """
        Constructor for the TMC5130 evalboard instance.

        Parameters:
        connection: TMCL connection interface instance.
        module_id: Module ID to identify the evalboard module. This is used to differentiate
        between different modules on shared busses. Default is set to 1, different
        values have to be configured with the module first.
        """
        super().__init__(connection, module_id, TMC5072(self, 0), self.EVAL_TYPES.MOTION_CONTROLLER)
        self.MOTORS = [ self.MOTOR(self, 0), self.MOTOR(self, 1) ]

    class MOTOR(TMCLModule.Motor, LinearRampModule, StallGuard2Module, CurrentModule, MotorControlModule):
        "Motor class for the generic motor."

        def __init__(self, module, axis):
            TMCLModule.Motor.__init__(self, module, axis)
            LinearRampModule.__init__(self)
            StallGuard2Module.__init__(self)
            CurrentModule.__init__(self)

        class APs:
            TargetPosition                 = 0
            ActualPosition                 = 1
            TargetVelocity                 = 2
            ActualVelocity                 = 3
            MaxVelocity                    = 4
            MaxAcceleration                = 5
            MaxCurrent                     = 6
            StandbyCurrent                 = 7
            PositionReachedFlag            = 8
            RightEndstop                   = 10
            LeftEndstop                    = 11
            AutomaticRightStop             = 12
            AutomaticLeftStop              = 13
            SW_MODE                        = 14
            A1                             = 15
            V1                             = 16
            MaxDeceleration                = 17
            D1                             = 18
            StartVelocity                  = 19
            StopVelocity                   = 20
            RampWaitTime                   = 21
            smartEnergyThresholdSpeed      = 22
            THIGH                          = 23
            VDCMIN                         = 24
            HighSpeedFullstepMode          = 28
            MicrostepResolution            = 140
            ChopperBlankTime               = 162
            ConstantTOffMode               = 163
            DisableFastDecayComparator     = 164
            ChopperHysteresisEnd           = 165
            ChopperHysteresisStart         = 166
            TOff                           = 167
            SEIMIN                         = 168
            SECDS                          = 169
            smartEnergyHysteresis          = 170
            SECUS                          = 171
            smartEnergyHysteresisStart     = 172
            SG2FilterEnable                = 173
            SG2Threshold                   = 174
            VSense                         = 179
            smartEnergyActualCurrent       = 180
            smartEnergyStallVelocity       = 181
            RandomTOffMode                 = 184
            ChopperSynchronization         = 185
            LoadValue                      = 206
            EncoderPosition                = 209
            EncoderResolution              = 210
