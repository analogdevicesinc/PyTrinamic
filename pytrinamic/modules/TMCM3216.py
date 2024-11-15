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


class TMCM3216(TMCLModule):
    """
    The TMCM-3216 is a three axis controller/driver module. Supply voltage is 24V.
    """
    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)
        self.name = "TMCM-3216"
        self.desc = self.__doc__
        self.motors = [self._MotorTypeA(self, 0), self._MotorTypeA(self, 1), self._MotorTypeA(self, 2),
                       self._MotorTypeA(self, 3), self._MotorTypeA(self, 4), self._MotorTypeA(self, 5)]

    def rotate(self, axis, velocity):
        """
        Rotates the motor on the given axis with the given velocity.

        Parameters:
        axis: Axis index.
        velocity: Target velocity to rotate the motor with. Units are module specific.

        Returns: None
        """
        self.connection.rotate(axis, velocity, self.module_id)

    def stop(self, axis):
        """
        Stops the motor on the given axis.

        Parameters:
        axis: Axis index.

        Returns: None
        """
        self.connection.stop(axis, self.module_id)

    def move_to(self, axis, position, velocity=None):
        """
        Moves the motor on the given axis to the given target position.

        Parameters:
        axis: Axis index.
        position: Target position to move the motor to. Units are module specific.
        velocity: Maximum position velocity to position the motor. Units are module specific.
        If no velocity is given, the previously configured maximum positioning velocity (AP 4)
        will be used.

        Returns: None
        """
        if velocity:
            self.motors[axis].linear_ramp.max_velocity = velocity
        self.connection.move_to(axis, position, self.module_id)

    def move_by(self, axis, difference, velocity=None):
        """
        Moves the motor on the given axis by the given position difference.

        Parameters:
        axis: Axis index.
        difference: Position difference to move the motor by. Units are module specific.
        velocity: Maximum position velocity to position the motor. Units are module specific.
        If no velocity is given, the previously configured maximum positioning velocity (AP 4)
        will be used.

        Returns: None
        """
        if velocity:
            self.motors[axis].linear_ramp.max_velocity = velocity
        self.connection.move_by(axis, difference, self.module_id)

    class _MotorTypeA(MotorControlModule):
        """
        Motor class for the motor on axis 0.
        """
        def __init__(self, module, axis):
            MotorControlModule.__init__(self, module, axis, self.AP)
            self.drive_settings = DriveSettingModule(module, axis, self.AP)
            self.linear_ramp = LinearRampModule(module, axis, self.AP)
            self.stallguard2 = StallGuard2Module(module, axis, self.AP)
            self.coolstep = CoolStepModule(module, axis, self.AP, self.stallguard2)

        def get_position_reached(self):
            """
            Indicates whether a positioning task has been completed.

            Returns:
            1, if target position has been reached.
            0, if target position has not been reached.
            """
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
            HighSpeedTheshold              = 22
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
            A2                             = 34
            V2                             = 35
            D2                             = 36
            VMaxMiniumTime                 = 37
            VirtualStopLeft                = 38
            VirtualStopRight               = 39
            VirtualStopFlags               = 40
            VirtualStopEnable              = 41
            VirtualStopEncoderMode         = 42
            PosCompPosition                = 43
            PosCompRepeat                  = 44
            PosCompOutputMask              = 45
            PosCompPulseLength             = 46
            TargetReachedOutputMask        = 47
            MotionStartInputMask           = 48
            RelativePositioningOption      = 127
            MicrostepResolution            = 140
            StepInterpolationEnable        = 160
            ChopperBlankTime               = 162
            ConstantTOffMode               = 163
            DisableFastDecayComparator     = 164
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
            GlobalCurrentScaler            = 178
            FullScaleCurrentRange          = 179
            SmartEnergyActualCurrent       = 180
            StopOnStallVelocity            = 181
            SmartEnergyThresholdSpeed      = 182
            PassiveFastDecayTime           = 185
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
            EncoderMode                    = 201
            FullstepResolution             = 202
            FreewheelingMode               = 204
            LoadValue                      = 206
            ErrorFlags                     = 207  # ExtendedErrorFlags
            StatusFlags                    = 208  # DrvStatusFlags
            EncoderPosition                = 209
            EncoderResolution              = 210
            MaxEncoderDeviation            = 212
            PowerDownDelay                 = 214
            StallGuard4Result              = 220
            StallGuard4Threshold           = 221
            StallGuard4FilterEnable        = 222
            StallGuard4AngleOffset         = 223
            ReverseShaft                   = 251

        class ENUM:
            """
            Constant enums for parameters of this module.
            """
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
        """
        Global parameter map for this module.
        """
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
        CANSecondaryAddress           = 83
        EepromCoordinateStore         = 84
        ZeroUserVariables             = 85
        SerialSecondaryAddress        = 86
        ApplicationStatus             = 128
        DownloadMode                  = 129
        ProgramCounter                = 130
        TickTimer                     = 132
        RandomNumber                  = 133
        SuppressReply                 = 255

    class GP3:
        Timer_0                        = 0
        Timer_1                        = 1
        Timer_2                        = 2
        StopLeft_0                     = 27
        StopRight_0                    = 28
        StopLeft_1                     = 29
        StopRight_1                    = 30
        StopLeft_2                     = 31
        StopRight_2                    = 32
        Input_0                        = 39
        Input_1                        = 40
        Input_2                        = 41
        Input_3                        = 42


    class IO:
        OUT0   = 0
        OUT1   = 1
        OUT2   = 2
        OUT3   = 3
        AIN0   = 0
        AIN1   = 1
        IN0    = 2
        IN1    = 3
        IN2    = 4
        IN3    = 5
