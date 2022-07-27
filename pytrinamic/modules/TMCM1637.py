from ..modules import TMCLModule

# features
from ..features import MotorControlModule, DriveSettingModule, LinearRampModule, ABNEncoderModule
from ..features import DigitalHallModule, PIDModule


class TMCM1637(TMCLModule):
    """
    The TMCM-1637 is a single axis servo drive module for three phase BLDC motors, two phase stepper motors and DC motors.
        * Supply Voltage: 8 - 24V
    """
    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)

        self.name = "TMCM-1637"
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
            self.abn_encoder = ABNEncoderModule(module, axis, self.AP)
            self.digital_hall = DigitalHallModule(module, axis, self.AP)
            self.pid = PIDModule(module, axis, self.AP)

        def get_position_reached(self):
            return self.get_axis_parameter(self.AP.PositionReachedFlag)

        class AP:
            AdcPhaseA                       = 0
            AdcPhaseB                       = 1
            CurrentPhaseA                   = 2
            CurrentPhaseB                   = 3
            CurrentPhaseC                   = 4
            AdcOffsetPhaseA                 = 5
            AdcOffsetPhaseB                 = 6
            MotorPolePairs                  = 10
            MaxCurrent                      = 11
            OpenLoopCurrent                 = 12
            MotorDirection                  = 13
            MotorType                       = 14
            CommutationMode                 = 15
            ActualOpenLoopAngle             = 16
            ActualEncoderAngle              = 17
            ActualHallAngle                 = 18
            ActualAbsoluteEncoderAngle      = 19
            PositionSensorSelection         = 25
            TargetTorque                    = 30
            ActualTorque                    = 31
            TargetFlux                      = 32
            ActualFlux                      = 33
            TargetVelocity                  = 40
            RampVelocity                    = 41
            ActualVelocity                  = 42
            MaxVelocity                     = 43
            MaxAcceleration                 = 44
            EnableRamp                      = 45
            TargetPosition                  = 50
            RampPosition                    = 51
            ActualPosition                  = 52
            TargetReachedDistance           = 53
            TargetReachedVelocity           = 54
            PositionReachedFlag             = 55
            PositionScaler                  = 56
            TorqueP                         = 70
            TorqueI                         = 71
            VelocityP                       = 72
            VelocityI                       = 73
            PositionP                       = 74
            CurrentPIDErrorSum              = 75
            FluxPIDErrorSum                 = 76
            VelocityPIDErrorSum             = 77
            TorquePIDError                  = 78
            FluxPIDError                    = 79
            VelocityPIDError                = 80
            PositionPIDError                = 81
            HallSensorPolarity              = 90
            HallSensorDirection             = 91
            HallSensorInterpolation         = 92
            HallSensorOffset                = 93
            HallSensorInputs                = 94
            EncoderSteps                    = 100
            EncoderDirection                = 101
            EncoderInitMode                 = 102
            EncoderInitState                = 103
            EncoderInitDelay                = 104
            EncoderInitVelocity             = 105
            EncoderOffset                   = 106
            ClearOnNull                     = 107
            ClearOnce                       = 108
            EncoderInputs                   = 109
            PWMFrequency                    = 110
            StatusFlags                     = 156
            ReferenceSwitchEnable           = 209
            ReferenceSwitchPolarity         = 210
            RightStopSwitch                 = 211
            LeftStopSwitch                  = 212
            HomeStopSwitch                  = 213
            SupplyVoltage                   = 220
            DriverTemperature               = 221
            MainLoopsPerSecond              = 230
            TorqueLoopsPerSecond            = 231
            VelocityLoopsPerSecond          = 232
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
            COMM_MODE_DIGITAL_HALL          = 2
            COMM_MODE_ABN_ENCODER           = 3
 
            ENCODER_INIT_MODE_0             = 0
            ENCODER_INIT_MODE_1             = 1
            ENCODER_INIT_MODE_2             = 2

            POS_SELECTION_SAME              = 0
            POS_SELECTION_ABN               = 1
            POS_SELECTION_ABS               = 2

            VEL_SELECTION_SAME              = 0
            VEL_SELECTION_ABN               = 1
            VEL_SELECTION_ABS               = 2

            FLAG_POSITION_END               = 0x00004000

            MOTOR_TYPE_NO_MOTOR             = 0
            MOTOR_TYPE_SINGLE_PHASE_DC      = 1
            MOTOR_TYPE_TWO_PHASE_STEPPER    = 2
            MOTOR_TYPE_THREE_PHASE_BLDC     = 3

    class GP:
        SerialBaudRate      = 65
        SerialAddress       = 66
        CANBitRate          = 69
        CANsendID           = 70
        CANreceiveID        = 71
        TelegramPauseTime   = 75
        SerialHostAddress   = 76
        AutoStartMode       = 77
        ApplicationStatus   = 128
        ProgramCounter      = 130
        TickTimer           = 132

    class IO:
        ADIN_0 = 0
        GPI_0 = 2
        GPI_1 = 3
        GPO_0 = 0
