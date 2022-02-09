from pytrinamic.modules import TMCLModule

# features
from pytrinamic.features import MotorControlModule, DriveSettingModule, LinearRampModule, DigitalHallModule, PIDModule


class TMC4671_LEV_REF(TMCLModule):
    """
    The TMC4671-LEV-REF is a highly compact controller/driver module for brushless DC (BLDC) motors with up to 30A
    coil current and hall sensor feedback. Supply voltage is 24-48V.
    """
    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)
        self.name = "TMC4671-LEV-REF"
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
            self.digital_hall = DigitalHallModule(module, axis, self.AP)
            self.pid = PIDModule(module, axis, self.AP)

        class AP:
            AdcPhaseA                       = 3
            AdcPhaseB                       = 4
            AdcOffsetPhaseA                 = 5
            AdcOffsetPhaseB                 = 6
            CurrentPhaseA                   = 7
            CurrentPhaseB                   = 8
            CurrentPhaseC                   = 9
            DualShuntFactor                 = 10
            OpenLoopCurrent                 = 12
            MotorType                       = 14
            CommutationMode                 = 15
            ActualOpenLoopAngle             = 16
            ActualHallAngle                 = 18
            TorqueP                         = 20
            TorqueI                         = 21
            VelocityP                       = 22
            VelocityI                       = 23
            TargetTorque                    = 30
            ActualTorque                    = 31
            TargetVelocity                  = 40
            RampVelocity                    = 41
            ActualVelocity                  = 42
            MaxVelocity                     = 43
            Acceleration                    = 44
            EnableRamp                      = 45
            PedalPulsesPerRotation          = 50
            PedalSenseDelay                 = 52
            TorqueSensorGain                = 53
            TorqueSensorOffset              = 54
            TorqueDeadband                  = 55
            AssistCutOutDistance            = 56
            InitialRightTorque              = 57
            InitialRightTorqueSpeed         = 58
            LeftRightRatio                  = 60
            AverageSportMode                = 61
            PedalDirection                  = 65
            PedalMotorEnable                = 66
            AverageTorque                   = 67
            PositiveMotoringRampTime        = 70
            NegativeMotoringRampTime        = 71
            Speed_0                         = 73
            Speed_1                         = 74
            Speed_2                         = 75
            Speed_3                         = 76
            Speed_4                         = 77
            Speed_5                         = 78
            Speed_6                         = 79
            Speed_7                         = 80
            Speed_8                         = 81
            Torque_0                        = 82
            Torque_1                        = 83
            Torque_2                        = 84
            Torque_3                        = 85
            Torque_4                        = 86
            Torque_5                        = 87
            Torque_6                        = 88
            Torque_7                        = 89
            Torque_8                        = 90
            MaximumSpeed                    = 91
            ActualMapSpeedTorque            = 92
            ActualGain                      = 93
            ActualTorqueLimit               = 94
            MaxTorque                       = 100
            MotorPolePairs                  = 101
            GearRatio                       = 102
            WheelDiameter                   = 103
            WheelPulsesPerRotation          = 104
            HallSensorOffset                = 105
            HallSensorPolarity              = 106
            HallSensorInterpolation         = 107
            HallSensorDirection             = 108
            CurrentRegulatorBandwidth       = 110
            MinimumMotorCurrent             = 111
            SwapMotorAAndCPhase             = 114
            MotorTestModes                  = 115
            ActualSpeedRPM                  = 116
            ActualSpeedMS                   = 117
            ActualSpeedKMH                  = 118
            MinBatteryVoltage               = 130
            MaxBatteryVoltage               = 131
            CutOffVoltage                   = 132
            BatterySavingTimer              = 133
            SupplyVoltage                   = 220
            DriverTemperature               = 221
            StatusFlags                     = 222
            Supply12V                       = 223
            Supply6V                        = 224
            Supply5V                        = 225
            PedalTorqueActual               = 226
            LeftPedalTorque                 = 227
            RightPedalTorque                = 228
            TargetPedalTorque               = 229
            MainLoopsPerSecond              = 230
            TorqueLoopsPerSecond            = 231
            VelocityLoopsPerSecond          = 232
            PedalCounter                    = 233
            PedalPosition                   = 234
            PedalCountsPerSecond            = 235
            PedalVelocity                   = 236
            FilteredPedalVelocity           = 237
            FilteredPedalVelocityFast       = 238
            DebugValue0                     = 240
            DebugValue1                     = 241
            DebugValue2                     = 242
            DebugValue3                     = 243
            DebugValue4                     = 244
            DebugValue5                     = 245
            DebugValue6                     = 246
            DebugValue7                     = 247
            DebugValue8                     = 248
            DebugValue9                     = 249
            EnableDriver                    = 255

        class ENUM:
            COMM_MODE_DISABLED              = 0
            COMM_MODE_OPENLOOP              = 1
            COMM_MODE_HALL                  = 2
            COMM_MODE_HALL_PEDAL_CONTROLLED = 3

    class GP:
        SerialBaudRate      = 65
        SerialAddress       = 66
        CANBitRate          = 69
        CANsendID           = 70
        CANreceiveID        = 71
        SerialHostAddress   = 76
