'''
Created on 03.12.2019

@author: JM
'''

from PyTrinamic.modules.tmcl_module import TMCLModule
from PyTrinamic.features.linear_ramp_module import LinearRampModule
from PyTrinamic.features.StallGuard2Module import StallGuard2Module
from PyTrinamic.features.CurrentModule import CurrentModule
from PyTrinamic.features.motor_control_module import MotorControlModule
from PyTrinamic.features.SRampModule import SRampModule
from PyTrinamic.features.SixPointRampModule import SixPointRampModule
class TMCM_3312(TMCLModule):

    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)

        self.MOTORS = [self.MOTOR_0(self, 0),self.MOTOR_0(self, 1),self.MOTOR_0(self, 2)]


    def showChipInfo(self):
        print("The TMCM-3312 is a triple axis stepper motor controller/driver module for sensorless load dependent current control. ")

    def rotate(self, axis, velocity):
        self.connection.rotate(axis, velocity, self.module_id)

    def stop(self, axis):
        self.connection.stop(axis, self.module_id)

    def move_to(self, axis, position, velocity=None):
        if velocity:
            self.max_velocity = velocity
        self.connection.moveTo(axis, position, self.module_id)

    def move_by(self, axis, difference, velocity=None):
        if velocity:
            self.max_velocity = velocity
        self.connection.moveBy(axis, difference, self.module_id)

    class MOTOR_0(TMCLModule.Motor, LinearRampModule, StallGuard2Module, SRampModule, SixPointRampModule, CurrentModule, MotorControlModule):

        def __init__(self, module, axis):
            TMCLModule.Motor.__init__(self, module, axis)
            LinearRampModule.__init__(self)
            StallGuard2Module.__init__(self)
            SRampModule.__init__(self)
            CurrentModule.__init__(self)
            SixPointRampModule.__init__(self)

        def get_position_reached(self):
            return self.get_axis_parameter(self.APs.PositionReachedFlag)

        class AP:
            TargetPosition                 = 0
            ActualPosition                 = 1
            TargetVelocity                 = 2
            ActualVelocity                 = 3
            MaxVelocity                    = 4
            MaxAcceleration                = 5
            RunCurrent                     = 6
            StandbyCurrent                 = 7
            PositionReachedFlag            = 8
            HomeSwitch                     = 9
            RightEndstop                   = 10
            LeftEndstop                    = 11
            RightLimit                     = 12
            LeftLimit                      = 13
            RampType                       = 14
            StartVelocity                  = 15
            StartAcceleration              = 16
            MaxDeceleration                = 17
            BreakVelocity                  = 18
            FinalDeceleration              = 19 
            StopVelocity                   = 20
            StopDeceleration               = 21 
            Bow1                           = 22
            Bow2                           = 23
            Bow3                           = 24
            Bow4                           = 25
            VirtualStopLeft                = 26
            VirtualStopRight               = 27
            VirtualStopEnable              = 28
            VirtualStopMode                = 29
            SwapStopSwitches               = 33
            EnableSoftStop                 = 34
            BowScalingFactor               = 35
            TorqueMode                     = 50
            CLgammaVmin                    = 108
            CLgammaVmax                    = 109
            CLmaximumGamma                 = 110
            CLbeta                         = 111
            CLoffset                       = 112
            CLcurrentMin                   = 113
            CLcurrentMax                   = 114
            CLcorrectionVelocityP          = 115
            CLcorrectionVelocityI          = 116
            CLcorrectionVelocityIClipping  = 117
            CLcorrectionVelocityDVClock    = 118
            CLcorrectionVelocityDVClipping = 119
            CLupscaleDelay                 = 120
            CLdownscaleDelay               = 121
            ActualScalerValue              = 123
            CLcorrectionPositionP          = 124
            CLmaxCorrectionTolerance       = 125
            CLstartUp                      = 126
            RelativePositioningOption      = 127
            ClosedLoopMode                 = 129
            MeasuredSpeed                  = 131
            CurrentMeasuredSpeed           = 132
            ClosedLoopInitFlag             = 133
            PositioningWindow              = 134
            EncMeanWait                    = 136
            EncMeanFilter                  = 137
            EncMeanInt                     = 138
            MicrostepResolution            = 140
            EncoderInputSampleRate         = 150
            EncoderInputFilterLength       = 151            
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
            ShortToGroundProtection        = 177
            VSense                         = 179
            SmartEnergyActualCurrent       = 180
            SmartEnergyStallVelocity       = 181
            SmartEnergyThresholdSpeed      = 182
            RandomTOffMode                 = 184
            ChopperSynchronization         = 185
            PWMThresholdSpeed              = 186
            PWMGrad                        = 187
            PWMAmplitude                   = 188
            PWMScale                       = 189
            PWMMode                        = 190
            PWMFrequency                   = 191
            PWMAutoscale                   = 192
            ReferenceSearchMode            = 193
            ReferenceSearchSpeed           = 194
            RefSwitchSpeed                 = 195
            RightLimitSwitchPosition       = 196
            LastReferencePosition          = 197
            EncoderMode                    = 201
            MotorFullStepResolution        = 202
            PWMSymmetric                   = 203
            FreewheelingMode               = 204
            LoadValue                      = 206
            ErrorFlags                     = 207
            StatusFlags                    = 208
            EncoderPosition                = 209
            EncoderResolution              = 210
            EncoderDeviationMax            = 212
            PowerDownDelay                 = 214
            GroupIndex                     = 219
            ReverseShaft                   = 251
        

    class ENUM():
        pass

    class GP():
        RS485Baudrate                 = 65
        SerialAddress                 = 66
        SerialHeartbeat               = 68
        CANBitrate                    = 69
        CANSendId                     = 70
        CANReceiveId                  = 71
        TelegramPauseTime             = 75
        SerialHostAddress             = 76
        AutoStartMode                 = 77
        ProtectionMode                = 81
        CANHeartbeat                  = 82
        CANSecondaryId                = 83
        EepromCoordinateStore         = 84
        ZeroUserVariables             = 85
        ApplicationStatus             = 128
        DownloadMode                  = 129
        ProgramCounter                = 130
        LastTmclError                 = 131
        TickTimer                     = 132
        RandomNumber                  = 133
        SuppressReply                 = 255
