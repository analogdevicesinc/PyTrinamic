
# interfaces
from PyTrinamic.modules.tmcl_module import tmcl_module

# features
from PyTrinamic.features.LinearRampModule import LinearRampModule
from PyTrinamic.features.ABNEncoderModule import ABNEncoderModule
from PyTrinamic.features.DigitalHallModule import DigitalHallModule
from PyTrinamic.features.DriveSettingModule import DriveSettingModule
from PyTrinamic.features.PIDModule import PIDModule
from PyTrinamic.features.MotorControlModule import MotorControlModule


class TMCM_1617(tmcl_module):
    """
    The TMCM-1617 is a single axis servo drive platform for 3-phase BLDC motors and DC motors.
        * Supply Voltage: 8 - 28V
    """
    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)

        self.name = "TMCM-1617"
        self.desc = self.__doc__
        self.motors = [self.Motor0(self, 0)]

    def rotate(self, axis, velocity):
        self.connection.rotate(axis, velocity, self.module_id)

    def stop(self, axis):
        self.connection.stop(axis, self.module_id)

    def move_to(self, axis, position, velocity=None):
        if velocity:
            self.max_velocity = velocity
        self.connection.moveTo(axis, position, self.module_id)

    def move_by(self, axis, difference, velocity=None):
        if velocity:
            self.max_velocity = velocity
        self.connection.moveBy(axis, difference, self.module_id)

    class Motor0(tmcl_module.Motor, LinearRampModule, ABNEncoderModule, DigitalHallModule, DriveSettingModule,
                  PIDModule, MotorControlModule):
        def __init__(self, module, axis):
            tmcl_module.Motor.__init__(self, module, axis)
            LinearRampModule.__init__(self)
            ABNEncoderModule.__init__(self)
            DigitalHallModule.__init__(self)
            DriveSettingModule.__init__(self)
            PIDModule.__init__(self)

        def get_position_reached(self):
            return self.get_axis_parameter(self.APs.PositionReachedFlag)

        class APs:
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
            MotorType                       = 14
            CommutationMode                 = 15
            ActualOpenLoopAngle             = 16
            ActualEncoderAngle              = 17
            ActualHallAngle                 = 18
            PositionSensorSelection         = 25
            VelocitySensorSelection         = 26
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
            EncoderSteps                    = 100
            EncoderDirection                = 101
            EncoderInitMode                 = 102
            EncoderInitState                = 103
            EncoderInitDelay                = 104
            EncoderInitVelocity             = 105
            EncoderOffset                   = 106
            ClearOnNull                     = 107
            ClearOnce                       = 108
            StatusFlags                     = 156
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

        class ENUMs:
            COMM_MODE_DISABLED              = 0
            COMM_MODE_OPENLOOP              = 1
            COMM_MODE_DIGITAL_HALL          = 2
            COMM_MODE_ABN_ENCODER           = 3
            COMM_MODE_ABS_ENCODER           = 4

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
            MOTOR_TYPE_THREE_PHASE_BLDC     = 3

    class GPs:
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

    class IOs:
        GPI_0 = 0
        GPI_1 = 1
        GPI_2 = 2
        GPI_3 = 3
        GPI_4 = 3
        GPI_5 = 3
