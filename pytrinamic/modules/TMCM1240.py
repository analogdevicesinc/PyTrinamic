from pytrinamic.modules import TMCLModule

# features
from pytrinamic.features import MotorControlModule, DriveSettingModule, LinearRampModule


class TMCM1240(TMCLModule):
    """
    The TMCM-1240 is a single axis controller/driver module. Supply voltage is 24V.
    """
    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)
        self.name = "TMCM-1240"
        self.desc = self.__doc__
        self.motors = [self.Motor0(self, 0)]

    def rotate(self, axis, velocity):
        self.connection.rotate(axis, velocity, self.module_id)

    def stop(self, axis):
        self.connection.stop(axis, self.module_id)

    def move_to(self, axis, position, velocity=None):
        if velocity:
            self.motors[0].linear_ramp.max_velocity = velocity
        self.connection.move_to(axis, position, self.module_id)

    def move_by(self, axis, difference, velocity=None):
        if velocity:
            self.motors[0].linear_ramp.max_velocity = velocity
        return self.connection.move_by(axis, difference, self.module_id)

    class Motor0(MotorControlModule):

        def __init__(self, module, axis):
            MotorControlModule.__init__(self, module, axis, self.AP)
            self.drive_settings = DriveSettingModule(module, axis, self.AP)
            self.linear_ramp = LinearRampModule(module, axis, self.AP)

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
            RightLimitSwitchDisable        = 12
            LeftLimitSwitchDisable         = 13
            SwapLimitSwitches              = 14
            A1                             = 15
            V1                             = 16
            MaxDeceleration                = 17
            D1                             = 18
            StartVelocity                  = 19
            StopVelocity                   = 20
            RampWaitTime                   = 21
            THIGH                          = 22
            MinDcStepSpeed                 = 23
            RightLimitSwitchPolarity       = 24
            LeftLimitSwitchPolarity        = 25
            SoftStop                       = 26
            HighSpeedChopperMode           = 27
            HighSpeedFullstepMode          = 28
            MeasuredSpeed                  = 29
            PowerDownRamp                  = 31
            DcStepTime                     = 32
            DcStepStallGuard               = 33
            RelativePositioningOption      = 127
            MicrostepResolution            = 140
            Intpol                         = 160
            DoubleEdgeSteps                = 161
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
            smartEnergyHysteresisStart     = 172
            SG2FilterEnable                = 173
            SG2Threshold                   = 174
            GlobalCurrentScaler            = 178
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
            ReferenceSwitchSpeed           = 195
            ReferenceSwitchDistance        = 196
            LastReferenceSwitchPosition    = 197
            FullstepResolution             = 202
            FreewheelingMode               = 204
            LoadValue                      = 206
            ErrorFlags                     = 207  # ExtendedErrorFlags
            StatusFlags                    = 208  # DrvStatusFlags
            EncoderPosition                = 209
            EncoderCleat                   = 210
            MaxEncoderDeviation            = 212
            PowerDownDelay                 = 214
            AbsoluteResolverValue          = 215
            ExternalEncoderPosition        = 216
            ExternalEncoderResolution      = 217
            ExternalEncoderMaxDeviation    = 218
            ReverseShaft                   = 251
            StepDirectionMode              = 254
            UnitMoode                      = 255

        class ENUM:
            FLAG_POSITION_END = 0x00004000

    class GP:
        Timer_0                        = 0
        Timer_1                        = 1
        Timer_2                        = 2
        StopLeft_0                     = 27
        StopRight_0                    = 28
        input_0                        = 39
        Input_1                        = 40
        Input_2                        = 41
        Input_3                        = 42
        SerialBaudRate                 = 65
        SerialAddress                  = 66
        ASCIIMode                      = 67
        SerialHeartbeat                = 68
        TelegramPauseTime              = 75
        SerialHostAddress              = 76
        AutoStartMode                  = 77
        LimitSwitchPolarity            = 79
        ProtectionMode                 = 81
        EepromCoordinateStore          = 84
        ZeroUserVariables              = 85
        SerialSecondaryAddress         = 87
        ReverseShaftDirection          = 90
        ApplicationStatus              = 128
        DownloadMode                   = 129
        ProgramCounter                 = 130
        LastTmclError                  = 131
        TickTimer                      = 132
        RandomNumber                   = 133
        Intpol                         = 255


#    " StallGuard2 functions "
#    def setStallguard2Filter(self, axis, enableFilter):
#        self.setAxisParameter(self.APs.SG2FilterEnable, axis, enableFilter)

#    def setStallguard2Threshold(self, axis, threshold):
#        self.setAxisParameter(self.APs.SG2Threshold, axis, threshold)

#    def setStopOnStallVelocity(self, axis, velocity):
#        self.setAxisParameter(self.APs.smartEnergyStallVelocity, axis, velocity)
