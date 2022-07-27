from ..modules import TMCLModule

# features
from ..features import MotorControlModule, DriveSettingModule, LinearRampModule
from ..features import StallGuard2Module, CoolStepModule


class TMCM1140(TMCLModule):
    """
    The TMCM-1140 is a single axis stepper motor controller/driver module for sensorless load dependent current control.
            * Supply voltage: 9 - 28V
    """
    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)
        self.name = "TMCM-1140"
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
            TargetPosition              = 0
            ActualPosition              = 1
            TargetVelocity              = 2
            ActualVelocity              = 3
            MaxVelocity                 = 4
            MaxAcceleration             = 5
            MaxCurrent                  = 6
            StandbyCurrent              = 7
            PositionReachedFlag         = 8
            ReferenceSwitchStatus       = 9
            RightEndstop                = 10
            LeftEndstop                 = 11
            RightLimitSwitchDisable     = 12
            LeftLimitSwitchDisable      = 13
            MinimumSpeed                = 130
            ActualAcceleration          = 135
            RampType                    = 138
            MicrostepResolution         = 140
            ReferenceSwitchTolerance    = 141
            SoftStopFlag                = 149
            EndSwitchPowerDown          = 150
            RampDivisor                 = 153
            PulseDivisor                = 154
            Intpol                      = 160
            DoubleEdgeSteps             = 161
            ChopperBlankTime            = 162
            ConstantTOffMode            = 163
            DisableFastDecayComparator  = 164
            ChopperHysteresisEnd        = 165
            ChopperHysteresisStart      = 166
            Toff                        = 167
            SEIMIN                      = 168
            SECDS                       = 169
            SmartEnergyHysteresis       = 170
            SECUS                       = 171
            SmartEnergyHysteresisStart  = 172
            SG2FilterEnable             = 173
            SG2Threshold                = 174
            SlopeControlHighSide        = 175
            SlopeControlLowSide         = 176
            ShortToGroundProtection     = 177
            ShortDetectionTime          = 178
            VSense                      = 179
            SmartEnergyActualCurrent    = 180
            SmartEnergyStallVelocity    = 181
            SmartEnergyThresholdSpeed   = 182
            SmartEnergySlowRunCurrent   = 183
            RandomTOffMode              = 184
            ReferenceSearchMode         = 193
            ReferenceSearchSpeed        = 194
            ReferenceSwitchSpeed        = 195
            ReferenceSwitchDistance     = 196
            LastReferenceSwitchPosition = 197
            BoostCurrent                = 200
            FreewheelingDelay           = 204
            LoadValue                   = 206
            ExtendedErrorFlags          = 207
            DrvStatusFlags              = 208
            EncoderPosition             = 209
            EncoderPrescaler            = 210
            MaxEncoderDeviation         = 212
            PowerDownDelay              = 214
            AbsoluteResolverValue       = 215
            ExternalEncoderPosition     = 216
            ExternalEncoderPrescaler    = 217
            ExternalEncoderMaxDeviation = 218

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
        SerialBaudRate    = 65
        SerialAddress     = 66
        SerialHeartbeat   = 68
        CANBitRate        = 69
        CANsendID         = 70
        CANreceiveID      = 71
        TelegramPauseTime = 75
        SerialHostAddress = 76
        AutoStartMode     = 77
        EndSwitchPolarity = 79
        TMCLCodeProtection = 81
        CANHeartbeat      = 82
        CANSecondaryAddress  = 83
        eepromCoordinateStore          = 84
        zeroUserVariables              = 85
        serialSecondaryAddress         = 87
        reverseShaftDirection          = 90
        ApplicationStatus = 128
        ProgramCounter    = 130
        TickTimer         = 132
        randomNumber      = 133
        SuppressReply       = 255

    class GP3:
        timer_0                        = 0
        timer_1                        = 1
        timer_2                        = 2
        stopLeft_0                     = 27
        stopRight_0                    = 28
        input_0                        = 39
        input_1                        = 40
        input_2                        = 41
        input_3                        = 42

    class IO:
        OUT0 = 0
        OUT1 = 1
        IN0  = 0
        IN1  = 1
        IN2  = 2
        IN3  = 3
