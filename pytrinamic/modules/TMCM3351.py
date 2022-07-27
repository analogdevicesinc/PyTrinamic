from ..modules import TMCLModule

# features
from ..features import MotorControlModule, DriveSettingModule, LinearRampModule
from ..features import StallGuard2Module, CoolStepModule


class TMCM3351(TMCLModule):
    """
    The TMCM-3351 is a three axis stepper motor controller/driver module for sensorless load dependent current control.
    """
    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)
        self.name = "TMCM-3351"
        self.desc = self.__doc__
        self.motors = [self._MotorTypeA(self, 0), self._MotorTypeA(self, 1), self._MotorTypeA(self, 2)]

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
            BoostCurrent                   = 200
            EncoderMode                    = 201
            MotorFullStepResolution        = 202
            FreewheelingMode               = 204
            LoadValue                      = 206
            ErrorFlags                     = 207
            StatusFlags                    = 208
            EncoderPosition                = 209
            EncoderResolution              = 210
            MaxPositionEncoderDeviation    = 212
            MaxVelocityEncoderDeviation    = 213
            PowerDownDelay                 = 214
            GroupIndex                     = 249
            ReverseShaft                   = 251

        class ENUM:
            microstep_resolution_fullstep = 0
            microstep_resolution_halfstep = 1
            microstep_resolution_4_microsteps = 2
            microstep_resolution_8_microsteps = 3
            microstep_resolution_16_microsteps = 4
            microstep_resolution_32_microsteps = 5
            microstep_resolution_64_microsteps = 6
            microstep_resolution_128_microsteps = 7
            microstep_resolution_256_microsteps = 8

    class GP0:
        SerialBaudRate      = 65
        SerialAddress       = 66
        SerialHearbeat      = 68
        CANBitRate          = 69
        CANsendID           = 70
        CANreceiveID        = 71
        TelegramPauseTime   = 75
        SerialHostAddress   = 76
        AutoStartMode       = 77
        TMCLCodeProtection  = 81
        CANHeartbeat        = 82
        CANSecondaryAddress = 83
        eepromCoordinateStore          = 84
        zeroUserVariables              = 85
        serialSecondaryAddress         = 87
        ApplicationStatus   = 128
        ProgramCounter      = 130
        TickTimer           = 132
        RandomNumber        = 133
        SuppressReply       = 255

    class GP3:
        timer_0                        = 0
        timer_1                        = 1
        timer_2                        = 2
        stopLeft_0                     = 27
        stopRight_0                    = 28
        stopLeft_1                     = 29
        stopRight_1                    = 30
        stopLeft_2                     = 31
        stopRight_2                    = 32
        input_0                        = 39
        input_1                        = 40
        input_2                        = 41
        input_3                        = 42
        input_4                        = 43
        input_5                        = 44
        input_6                        = 45
        input_7                        = 46

    class IO:
        OUT0   = 0
        OUT1   = 1
        OUT2   = 2
        OUT3   = 3
        OUT4   = 4
        OUT5   = 5
        OUT6   = 6
        OUT7   = 7
        IN0    = 0
        IN1    = 1
        IN2    = 2
        IN3    = 3
        IN4    = 4
        IN5    = 5
        IN6    = 6
        IN7    = 7
