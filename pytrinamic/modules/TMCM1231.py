from ..modules import TMCLModule

# features
from ..features import MotorControlModule, DriveSettingModule, LinearRampModule
from ..features import StallGuard2Module, CoolStepModule


class TMCM1231(TMCLModule):
    """
    The TMCM-1231 is a  single axis controller/driver module for 2-phase bipolar stepper motors.
    """
    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)
        self.name = "TMCM-1231"
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
            RunCurrent                     = MaxCurrent
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
            RelativePositioningOption      = 127
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
            EndSwitchDistance              = 196
            LastReferencePosition          = 197
            LatchedActualPosition          = 198
            LatchedEncoderPosition         = 199
            BoostCurrent                   = 200
            EncoderMode                    = 201
            MotorFullStepResolution        = 202
            FreewheelingMode               = 204
            LoadValue                      = 206
            ExtendedErrorFlags             = 207
            DriverErrorFlags               = 208
            EncoderPosition                = 209
            EncoderResolution              = 210
            MaxPositionEncoderDeviation    = 212
            MaxVelocityEncoderDeviation    = 213
            PowerDownDelay                 = 214
            ReverseShaft                   = 251
            StepDirectionMode              = 254

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
        SerialBaudRate                 = 65
        SerialAddress                  = 66
        SerialHearbeat                 = 68
        CANBitRate                     = 69
        CANsendID                      = 70
        CANreceiveID                   = 71
        TelegramPauseTime              = 75
        SerialHostAddress              = 76
        AutoStartMode                  = 77
        TMCLCodeProtection             = 81
        CANHeartbeat                   = 82
        CANSecondaryAddress            = 83
        eepromCoordinateStore          = 84
        zeroUserVariables              = 85
        serialSecondaryAddress         = 87
        ApplicationStatus              = 128
        DownloadMode                   = 129
        ProgramCounter                 = 130
        TickTimer                      = 132
        RandomNumber                   = 133
        SuppressReply                  = 255

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
        GPO0    = 0
        AIN0    = 0
        GPI0    = 2
        GPI1    = 3

