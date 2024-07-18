################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from ..modules import TMCLModule

# features
from ..features import MotorControlModule, DriveSettingModule, LinearRampModule
from ..features import StallGuard2Module, CoolStepModule


class TMCM1311(TMCLModule):
    """
    The TMCM-1311 is a single axis stepper motor controller/driver module with closed loop regulation.
            * Supply voltage: 12 - 48V
    """
    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)
        self.name = "TMCM-1311"
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
            RightLimitSwitchDiable         = 12
            LeftLimitSwitchDisable         = 13
            CLTorqueModeTargetCurrent      = 14
            MaximumPossibleCurrent         = 15
            CLVelocityReached              = 16
            CLVelocityReachedWindow        = 17
            StatusWord                     = 18
            CLTorqueModeActualCurrent      = 19
            CLTorqueModeSlope              = 20
            ThermalWindingTimeConstant     = 25
            IITLimit                       = 26
            IITSum                         = 27
            IITExceedCounter               = 28
            ClearIITExceededFlag           = 29
            CLFieldWeakeningMinimumVelocity= 108
            CLFieldWeakeningMaximimVelocity= 109
            CLEncoderOffset                = 112
            CLCurrentScaleMinimum          = 113
            CLCurrentScaleMaximum          = 114
            CLCurrentScaleInputSelect      = 115
            CLCurrentScaleLowerErrorLimit  = 116
            CLCurrentScaleUpperErrorLimit  = 117
            CLCurrentScaleIncrementValue   = 118
            CLCurrentScaleDecrementValue   = 119
            CLCurrentScaleIncrementTimeout = 120
            CLCurrentScaleDecrementTimeout = 121
            CLCurrentScaleEnable           = 122
            CLActualCurrentScaleFactor     = 123
            CLCorrectionVelocityP          = 124
            CLMaxFollowingError            = 125
            CLMaxCorrectionVelocity        = 126
            RelativePositioningOption      = 127
            RampMode                       = 128
            ClosedLoopMode                 = 129
            StartStopVelocity              = 130
            MeasuredSpeed                  = 131
            EncoderInitialization          = 132
            CLInitFlag                     = 133
            CLPositionReachedWindow        = 134
            EncoderDeviation               = 134
            CLPositionReachedTime          = 135
            CLStandstillPositionErrorGain  = 136
            CLStandstillPosErrDampening    = 137
            CLStandtstillPositionErrorLimit= 138
            MicrostepResolution            = 140
            CLTorqueModeStartStopCurrent   = 141
            CurrentPhaseA                  = 151
            CurrentPhaseB                  = 152
            SupplyVoltage                  = 153
            ActualDCCurrent                = 154
            ModuleTemperature              = 155
            ChopperBlankTime               = 162
            ChopperMode                    = 163
            ChopperHysteresisDecrement     = 164
            ChopperHysteresisEnd           = 165
            ChopperHysteresisStart         = 166
            TOff                           = 167
            SmartEnergyCurrentMinimum      = 168
            SmartEnergyCurrentDownStep     = 169
            SmartEnergyHysteresis          = 170
            SmartEnergyCurrentUpStep       = 171
            SmartEnergyHysteresisStart     = 172
            StallGuard2FilterEnable        = 173
            StallGuard2Threshold           = 174
            SlopeControlHighSide           = 175
            SlopeControlLowSide            = 176
            ShortToGroundProtection        = 177
            ShortDetectionTime             = 178
            VSense                         = 179
            SmartEnergyActualCurrent       = 180
            SmartEnergyStallVelocity       = 181
            SmartEnergyThresholdSpeed      = 182
            SmartEnergySlowRunCurrent      = 183
            ReferenceSearchMode            = 193
            ReferenceSearchSpeed           = 194
            ReferenceSwitchSpeed           = 195
            EndSwitchDistance              = 196
            BoostCurrent                   = 200
            EncoderMode                    = 201
            FullstepResolution             = 202
            Freewheeling                   = 204
            LoadValue                      = 206
            ExtendedErrorFlags             = 207
            DriverErrorFlags               = 208
            EncoderPosition                = 209
            EncoderResolution              = 210
            MaxPositionEncoderDeviation    = 212
            SettingDelay                   = 214
            CLGamma                        = 230
            CLVirtualActualPosition        = 233
            CLActualTargetCurrentScaleFactor = 236
            CLPositionError                = 237
            StepDirMode                    = 254
    
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
        CANBitrate                     = 69
        CANReplyID                     = 70
        CANModuleID                    = 71
        telegramPauseTime              = 75
        serialHostAddress              = 76
        autoStartMode                  = 77
        endSwitchPolarity              = 79
        protectionMode                 = 81
        CANSecondaryAddress            = 83
        eepromCoordinateStore          = 84
        zeroUserVariables              = 85
        serialSecondaryAddress         = 87
        interfaceSelection             = 88
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
        input_2                        = 41
        input_3                        = 42
        input_4                        = 43
        input_5                        = 44
        input_6                        = 45
        input_7                        = 46

    class IO:
        OUT0 = 0
        OUT1 = 1
        OUT2 = 2
        OUT3 = 3
        OUT4 = 4
        OUT5 = 5
        OUT6 = 6
        OUT7 = 7
        IN0 = 0
        IN1 = 1
        IN2 = 2
        IN3 = 3
        IN4 = 4
        IN5 = 5
        IN6 = 6
        IN7 = 7
        Home = 0
