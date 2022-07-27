from ..modules import TMCLModule

# features
from ..features import MotorControlModule, DriveSettingModule, LinearRampModule
from ..features import StallGuard2Module, CoolStepModule


class TMCM1370(TMCLModule):
    """
    The TMCM-1370 is a single axis stepper motor controller/driver module for sensorless load dependent current control.
            * Supply voltage: 9 - 28V
    """
    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)
        self.name = "TMCM-1370"
        self.desc = self.__doc__
        self.motors = [self._MotorTypeA(self, 0)]

    def rotate(self, axis, velocity):
        self.connection.rotate(axis, velocity, self.module_id)

    def stop(self, axis):
        self.connection.stop(axis, self.module_id)

    def move_to(self, axis, position, velocity=None):
        if velocity:
            self.motors[axis].linear_ramp.max_velocity = velocity
        self.connection.move_to(axis, position, self.module_id)

    def move_by(self, axis, difference, velocity=None):
        if velocity:
            self.motors[axis].linear_ramp.max_velocity = velocity
        self.connection.move_by(axis, difference, self.module_id)

    class _MotorTypeA(MotorControlModule):

        def __init__(self, module, axis):
            MotorControlModule.__init__(self, module, axis, self.AP)
            self.drive_settings = DriveSettingModule(module, axis, self.AP)
            self.linear_ramp = LinearRampModule(module, axis, self.AP)
            self.stallguard2 = StallGuard2Module(module, axis, self.AP)
            self.coolstep = CoolStepModule(module, axis, self.AP, self.stallguard2)

        def get_position_reached(self):
            return self.get_axis_parameter(self.AP.PositionReachedFlag)

        class AP:
            TargetPosition                 = 0
            ActualPosition                 = 1
            TargetVelocity                 = 2
            ActualVelocity                 = 3
            MaxVelocity                    = 4
            MaxAcceleration                = 5
            MaxCurrent                     = 6
            StandbyCurrent                 = 7
            PositionReachedFlag            = 8
            HomeSwitch                     = 9
            RightEndstop                   = 10
            LeftEndstop                    = 11
            RightLimitSwitchEnablePolarity = 12
            LeftLimitSwitchEnablePolarity  = 13
            RampType                       = 14
            StartVelocity                  = 15
            StartAcceleration              = 16
            MaxDeceleration                = 17
            breakVelocity                  = 18
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
            SwapLimitSwitches              = 33
            LimitSwitchSoftStop            = 34
            BowScaler                      = 35
            PositionCompareValue           = 40
            PositionComparePulseLength     = 41
            PositionCompareOutput          = 42
            PositionCompareRepeat          = 43
            Torque                         = 50
            CLGammaVMin                    = 108
            CLGammaVMax                    = 109
            CLMaxGamma                     = 110
            CLBeta                         = 111
            CLOffset                       = 112
            CLCurrentMin                   = 113
            CLCurrentMax                   = 114
            CLCorrectionVelocityP          = 115
            CLCorrectionVelocityI          = 116
            CLCorrectionVelIClip           = 117
            CLCorrectionVelDVClock         = 118
            CLCorrectionVelDVClip          = 119
            CLUpscaleDelay                 = 120
            CLDownscaleDelay               = 121
            ActualScalerValue              = 123
            CLCorrectionPositionP          = 124
            CLMaxCorrectionTolerance       = 125
            CLStartUp                      = 126
            RelativePositioningOption      = 127
            ClosedLoop                     = 129
            InitMode                       = 130
            MeasuredSpeed                  = 131
            CurrentMeasuredSpeed           = 132
            CL_init_flag                   = 133
            EncoderDeviation               = 134
            enc_vmean_wait                 = 136
            enc_vmean_filter               = 137
            enc_vmean_int                  = 138
            ChopperBlankTime               = 162
            ConstantTOffMode               = 163
            ChopperHysteresisDecrement     = 164
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
            SlopeControlHighSide           = 175
            ShortToGroundProtection        = 177
            ShortDetectionTime             = 178
            VSense                         = 179
            SmartEnergyActualCurrent       = 180
            SmartEnergyStallVelocity       = 181
            SmartEnergyThresholdSpeed      = 182
            SmartEnergySlowRunCurrent      = 183
            RandomTOffMode                 = 184
            ReferenceSearchMode            = 193
            ReferenceSearchSpeed           = 194
            ReferenceSwitchSpeed           = 195
            ReferenceSwitchDistance        = 196
            LastReferenceSwitchPosition    = 196
            BoostCurrent                   = 200
            FullstepResolution             = 202
            FreewheelingMode               = 204
            LoadValue                      = 206
            ExtendedErrorFlags             = 207
            DriverErrorFlags               = 208
            EncoderPosition                = 209
            EncoderResolution              = 210
            StopOnErrorMode                = 211
            MaxPositionEncoderDeviation    = 212
            MaxVelocityEncoderDeviation    = 213
            SettingDelay                   = 214
            AbsoluteEncoder                = 215
            EncoderErrorBits               = 219
            AllStatusBits                  = 250
            ReverseShaft                   = 251
            ClearAlarmOutputs              = 252
    
        class ENUM:
            MicrostepResolutionFullstep      = 0
            MicrostepResolutionHalfstep      = 1
            MicrostepResolution4Microsteps   = 2
            MicrostepResolution8Microsteps   = 3
            MicrostepResolution16Microsteps  = 4
            MicrostepResolution32Microsteps  = 5
            MicrostepResolution64Microsteps  = 6
            MicrostepResolution128Microsteps = 7
            MicrostepResolution256Microsteps = 8

    class GP0:
        serialBaudRate                 = 65
        serialAddress                  = 66
        serialHeartbeat                = 68
        telegramPauseTime              = 75
        serialHostAddress              = 76
        autoStartMode                  = 77
        protectionMode                 = 81
        eepromCoordinateStore          = 84
        zeroUserVariables              = 85
        serialSecondaryAddress         = 87
        reverseShaftDirection          = 90
        applicationStatus              = 128
        downloadMode                   = 129
        programCounter                 = 130
        tickTimer                      = 132
        randomNumber                   = 133
        SuppressReply                  = 255

    class GP3:
        timer_0                        = 0
        timer_1                        = 1
        timer_2                        = 2
        stopLeft_0                     = 27
        stopRight_0                    = 28
        input_0                        = 39
        input_1                        = 40

    class IO:
        OUT0 = 0
        Home = 0
        Enable = 1
