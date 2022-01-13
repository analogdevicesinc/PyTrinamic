
# interfaces
from PyTrinamic.modules.tmcl_module import tmcl_module

# features
from PyTrinamic.features.DriveSettingModule import DriveSettingModule
from PyTrinamic.features.LinearRampModule import LinearRampModule
from PyTrinamic.features.ABNEncoderModule import ABNEncoderModule
from PyTrinamic.features.DigitalHallModule import DigitalHallModule
from PyTrinamic.features.PIDModule import PIDModule
from PyTrinamic.features.MotorControlModule import MotorControlModule


class TMCC_160(tmcl_module):
    """
    The TMCC160 is designed for evaluating all features of the TMCC160-LC motionCookie. Supply voltage is 7-24V.
    """
    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)

        self.name = "TMCC-160"
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

    class Motor0(tmcl_module.Motor, DriveSettingModule, LinearRampModule, ABNEncoderModule, DigitalHallModule,
                 PIDModule, MotorControlModule):

        def __init__(self, module, axis):
            tmcl_module.Motor.__init__(self, module, axis)
            DriveSettingModule.__init__(self)
            LinearRampModule.__init__(self)
            ABNEncoderModule.__init__(self)
            DigitalHallModule.__init__(self)
            PIDModule.__init__(self)

        def get_position_reached(self):
            return self.get_axis_parameter(self.APs.StatusFlags) & self.ENUMs.FLAG_POSITION_END

        class APs:
            TargetPosition                 = 0
            ActualPosition                 = 1
            TargetVelocity                 = 2
            ActualVelocity                 = 3
            MaxVelocity                    = 4
            MaxCurrent                     = 6      # MaxTorque
            TargetReachedVelocity          = 7
            MotorHaltedVelocity            = 9
            TargetReachedDistance          = 10
            MaxAcceleration                = 11
            SwitchVelocity                 = 12
            RampVelocity                   = 13
            ThermalWindingTimeConstant     = 25
            IItlimit                       = 26
            IItSum                         = 27
            IItExceededCounter             = 28
            ClearIItExceededFlag           = 29
            ReinitBldcRegulation           = 31
            PIDRegulationLoopDelay         = 133
            CurrentRegulationLoopDelay     = 134
            EnableRamp                     = 146
            ActualTorque                   = 150
            SupplyVoltage                  = 151
            DriverTemperature              = 152
            TargetTorque                   = 155
            StatusFlags                    = 156
            CommutationMode                = 159
            ClearOnNull                    = 161
            ClearOnce                      = 163
            HallOffset                     = 164
            EncoderOffset                  = 165
            TorqueP                        = 172
            TorqueI                        = 173
            SingleShuntOffset              = 175
            SingleShuntVref                = 176
            OpenLoopCurrent                = 177    # StartCurrent
            DebugValue0                    = 190
            DebugValue1                    = 191
            DebugValue2                    = 192
            DebugValue3                    = 193
            DebugValue4                    = 194
            DebugValue5                    = 195
            DebugValue6                    = 196
            DebugValue7                    = 197
            DebugValue8                    = 198
            DebugValue9                    = 199
            CurrentPIDError                = 200
            CurrentPIDErrorSum             = 201
            FluxPIDError                   = 202
            FluxPIDErrorSum                = 203
            UseSingleShunt                 = 205
            DualShuntFactor                = 208
            SingleShuntFactor              = 209
            ActualHallAngle                = 210
            ActualEncoderAngle             = 211
            ActualControlledAngle          = 212
            DriverDiagnosticValue          = 214
            DriverStatusAcknowledge        = 215
            DriverInitSPI                  = 216
            DriverStatusRegister2          = 217
            DriverStatusRegister3          = 218
            DriverStatusRegister4          = 219
            PositionPIDError               = 226
            VelocityPIDError               = 228
            VelocityPIDErrorSum            = 229
            PositionP                      = 230
            VelocityP                      = 234
            VelocityI                      = 235
            BrakeChopperEnabled            = 237
            BrakeChopperVoltage            = 238
            BrakeChopperHysteresis         = 239
            InitVelocity                   = 241
            InitSineDelay                  = 244
            EncoderInitMode                = 249
            EncoderSteps                   = 250
            EncoderDirection               = 251
            HallSensorInterpolation        = 252    # HallInterpolation
            MotorPoles                     = 253
            HallSensorPolarity             = 254    # HallSensorInvert
            EnableDriver                   = 255

        class ENUMs:
            COMM_MODE_BLOCK_HALL           = 0
            COMM_MODE_FOC_HALL             = 6
            COMM_MODE_FOC_ENCODER          = 7
            COMM_MODE_FOC_CONTROLLED       = 8

            ENCODER_INIT_MODE_0            = 0
            ENCODER_INIT_MODE_1            = 1
            ENCODER_INIT_MODE_2            = 2

            FLAG_POSITION_END              = 0x00004000

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

    class DIs:
        REF_R        = 0
        REF_L        = 1
        ENABLE       = 2

    class AINs:
        ADC_IN_0            = 0
        ADC_single_shunt    = 1
        ADC_phase_A         = 2
        ADC_phase_B         = 3
        ADC_VSupply         = 4
        ADC_Temp            = 5
