from ..modules import TMCLModule

# features
from ..features import MotorControlModule, DriveSettingModule, LinearRampModule
from ..features import StallGuard2Module, CoolStepModule


class TMCM1160(TMCLModule):
    """
    The TMCM-1160 is a single axis stepper motor controller/driver module for sensorless load dependent current control.
            * Supply voltage: 9 - 51V
    """
    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)
        self.name = "TMCM-1160"
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
            referenceSwitchStatus          = 9
            RightEndstop                   = 10
            LeftEndstop                    = 11
            rightLimitSwitchDisable        = 12
            leftLimitSwitchDisable         = 13
            minimumSpeed                   = 130
            actualAcceleration             = 135
            RampMode                       = 138
            MicrostepResolution            = 140
            Ref_SwitchTolerance            = 141
            softStopFlag                   = 149
            EndSwitchPowerDown             = 150
            rampDivisor                    = 153
            PulseDivisor                   = 154
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
            smartEnergyHysteresis          = 170
            SECUS                          = 171
            smartEnergyHysteresisStart     = 172
            SG2FilterEnable                = 173
            SG2Threshold                   = 174
            slopeControlHighSide           = 175
            slopeControlLowSide            = 176
            ShortToGroundProtection        = 177
            ShortDetectionTime             = 178
            VSense                         = 179
            smartEnergyActualCurrent       = 180
            smartEnergyStallVelocity       = 181
            smartEnergyThresholdSpeed      = 182
            smartEnergySlowRunCurrent      = 183
            RandomTOffMode                 = 184
            ReferenceSearchMode            = 193
            ReferenceSearchSpeed           = 194
            referenceSwitchSpeed           = 195
            referenceSwitchDistance        = 196
            lastReferenceSwitchPosition    = 197
            BoostCurrent                   = 200
            freewheelingDelay              = 204
            LoadValue                      = 206
            extendedErrorFlags             = 207
            DrvStatusFlags                 = 208
            EncoderPosition                = 209
            encoderPrescaler               = 210
            max_EncoderDeviation           = 212
            PowerDownDelay                 = 214
            absoluteResolverValue          = 215
            externalEncoderPosition        = 216
            externalEncoderPrescaler       = 217
            ExternalEncoderMax_Deviation   = 218
            Step_DirectionMode             = 254
    
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
        ASCIIMode                      = 67
        serialHeartbeat                = 68
        CANBitrate                     = 69
        CANSendId                      = 70
        CANReceiveId                   = 71
        telegramPauseTime              = 75
        serialHostAddress              = 76
        autoStartMode                  = 77
        limitSwitchPolarity            = 79
        protectionMode                 = 81
        CANHeartbeat                   = 82
        CANSecondaryAddress            = 83
        eepromCoordinateStore          = 84
        zeroUserVariables              = 85
        serialSecondaryAddress         = 87
        reverseShaftDirection          = 90
        applicationStatus              = 128
        downloadMode                   = 129
        programCounter                 = 130
        lastTmclError                  = 131
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
        OUT1 = 1
        IN0  = 0
        IN1  = 1
