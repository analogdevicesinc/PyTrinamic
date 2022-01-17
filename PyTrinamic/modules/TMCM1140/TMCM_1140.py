# interfaces
from PyTrinamic.modules import TMCLModule, Motor

# features
from PyTrinamic.features.StallGuard2Module import StallGuard2Module
from PyTrinamic.features.CoolStepModule import CoolStepModule
from PyTrinamic.features.DriveSettingModule import DriveSettingModule
from PyTrinamic.features.LinearRampModule import LinearRampModule
from PyTrinamic.features.MotorControlModule import MotorControlModule


class TMCM_1140(TMCLModule):
    """
    The TMCM-1140 is a single axis stepper motor controller/driver module for sensorless load dependent current control.
            * Supply Voltage: 9 - 28V
    """
    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)
        self.name = "TMCM-1140"
        self.desc = self.__doc__
        self.motors = [self.Motor0(self, 0)]

    def rotate(self, axis, velocity):
        self.connection.rotate(axis, velocity, self.module_id)

    def stop(self, axis):
        self.connection.stop(axis, self.module_id)

    def move_to(self, axis, position, velocity=None):
        if velocity:
            self.motors[0].LinearRamp.max_velocity = velocity
        self.connection.moveTo(axis, position, self.module_id)

    def move_by(self, axis, difference, velocity=None):
        if velocity:
            self.motors[0].LinearRamp.max_velocity = velocity
        self.connection.moveBy(axis, difference, self.module_id)

    class Motor0(Motor, DriveSettingModule, LinearRampModule, MotorControlModule, StallGuard2Module, CoolStepModule):

        def __init__(self, module, axis):
            Motor.__init__(self, module, axis)
            DriveSettingModule.__init__(self)
            LinearRampModule.__init__(self)
            StallGuard2Module.__init__(self)
            CoolStepModule.__init__(self)

        def get_position_reached(self):
            return self.get_axis_parameter(self.AP.PositionReachedFlag)

        class AP:
            TargetPosition              =  0
            ActualPosition              =  1
            TargetVelocity              =  2
            ActualVelocity              =  3
            MaxVelocity                 =  4
            MaxAcceleration             =  5
            MaxCurrent                  =  6
            StandbyCurrent              =  7
            PositionReachedFlag         =  8
            ReferenceSwitchStatus       =  9
            RightEndstop                =  10
            LeftEndstop                 =  11
            RightLimitSwitchDisable     =  12
            LeftLimitSwitchDisable      =  13
            MinimumSpeed                =  130
            ActualAcceleration          =  135
            RampType                    =  138
            MicrostepResolution         =  140
            ReferenceSwitchTolerance    =  141
            SoftStopFlag                =  149
            EndSwitchPowerDown          =  150
            RampDivisor                 =  153
            PulseDivisor                =  154
            Intpol                      =  160
            DoubleEdgeSteps             =  161
            ChopperBlankTime            =  162
            ConstantTOffMode            =  163
            DisableFastDecayComparator  =  164
            ChopperHysteresisEnd        =  165
            ChopperHysteresisStart      =  166
            Toff                        =  167
            SEIMIN                      =  168
            SECDS                       =  169
            SmartEnergyHysteresis       =  170
            SECUS                       =  171
            SmartEnergyHysteresisStart  =  172
            SG2FilterEnable             =  173
            SG2Threshold                =  174
            SlopeControlHighSide        =  175
            SlopeControlLowSide         =  176
            ShortToGroundProtection     =  177
            ShortDetectionTime          =  178
            VSense                      =  179
            SmartEnergyActualCurrent    =  180
            SmartEnergyStallVelocity    =  181
            SmartEnergyThresholdSpeed   =  182
            SmartEnergySlowRunCurrent   =  183
            RandomTOffMode              =  184
            ReferenceSearchMode         =  193
            ReferenceSearchSpeed        =  194
            ReferenceSwitchSpeed        =  195
            ReferenceSwitchDistance     =  196
            LastReferenceSwitchPosition =  197
            BoostCurrent                =  200
            FreewheelingDelay           =  204
            LoadValue                   =  206
            ExtendedErrorFlags          =  207
            DrvStatusFlags              =  208
            EncoderPosition             =  209
            EncoderPrescaler            =  210
            MaxEncoderDeviation         =  212
            PowerDownDelay              =  214
            AbsoluteResolverValue       =  215
            ExternalEncoderPosition     =  216
            ExternalEncoderPrescaler    =  217
            ExternalEncoderMaxDeviation =  218

        class ENUMs:
            MicrostepResolutionFullstep      = 0
            MicrostepResolutionHalfstep      = 1
            MicrostepResolution4Microsteps   = 2
            MicrostepResolution8Microsteps   = 3
            MicrostepResolution16Microsteps  = 4
            MicrostepResolution32Microsteps  = 5
            MicrostepResolution64Microsteps  = 6
            MicrostepResolution128Microsteps = 7
            MicrostepResolution256Microsteps = 8

    class GPs:
        SerialBaudRate    = 65
        SerialAddress     = 66
        CANBitRate        = 69
        CANsendID         = 70
        CANreceiveID      = 71
        TelegramPauseTime = 75
        SerialHostAddress = 76
        AutoStartMode     = 77
        ApplicationStatus = 128
        ProgramCounter    = 130
        TickTimer         = 132

    class IOs:
        OUT0 = 0
        OUT1 = 1
