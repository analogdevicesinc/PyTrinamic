from ..modules import TMCLModule
from ..features import MotorControlModule, DriveSettingModule, LinearRampModule, AbsoluteEncoderModule
from ..features import PIDModule


class TMCM1670(TMCLModule):
    """
    The TMCM-1670 is an easy to use and rather compact PANdrive™ smart BLDC motor. Supply voltage is 10-28V.
    """
    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)
        self.name = "TMCM-1670"
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
            self.absolute_encoder = AbsoluteEncoderModule(module, axis, self.AP)
            self.pid = PIDModule(module, axis, self.AP)

        def get_position_reached(self):
            return self.get_axis_parameter(self.AP.StatusFlags) & self.ENUM.FLAG_POSITION_END

        class AP:
            TargetPosition                 = 0
            ActualPosition                 = 1
            TargetVelocity                 = 2
            ActualVelocity                 = 3
            MaxVelocity                    = 4
            TorqueLimit                    = 5
            MaxCurrent                     = 6      # MaxTorque
            TargetReachedVelocity          = 7
            PositionReachedFlag            = 8
            MotorHaltedVelocity            = 9
            TargetReachedDistance          = 10
            MaxAcceleration                = 11
            RampVelocity                   = 13
            RampPosition                   = 14
            RightStopSwitch                = 20
            LeftStopSwitch                 = 21
            ReinitBldcRegulation           = 31
            BodeControlMode                = 100
            BodeTargetMode                 = 101
            BodePlotMagnitude              = 102
            BodePlotPhi                    = 103
            BodePlotSweepFrequency         = 104
            BodePlotSweepDataCount         = 105
            BodeTargetValue                = 106
            BodeActualValue                = 107
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
            AbsoluteEncoderOffset          = 165    # EncoderOffset
            ReferenceSwitchPolarity        = 166
            TorqueP                        = 172
            TorqueI                        = 173
            OpenLoopCurrent                = 177    # StartCurrent
            MainLoopsPerSecond             = 180
            PwmLoopsPerSecond              = 181
            TorqueLoopsPerSecond           = 182
            VelocityLoopsPerSecond         = 183
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
            VelocityFilter                 = 236
            InitVelocity                   = 241
            InitSineDelay                  = 244
            AbsoluteEncoderInitMode        = 249    # EncoderInitMode
            AbsoluteEncoderSteps           = 250    # EncoderSteps
            AbsoluteEncoderDirection       = 251    # EncoderDirection
            MotorPoles                     = 253
            EnableDriver                   = 255

        class ENUM:
            COMM_MODE_FOC_ENCODER          = 7
            COMM_MODE_FOC_CONTROLLED       = 8

            ENCODER_INIT_MODE_0            = 0
            ENCODER_INIT_MODE_2            = 2

            FLAG_POSITION_END              = 0x00004000

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

    class DI:
        REF_R       = 0
        REF_L       = 1
        IN_0        = 2
        ENABLE      = 3

    class AIN:
        ADC_phase_A = 0
        ADC_phase_C = 1
        ADC_VSupply = 2
        ADC_Temp    = 3

    class DO:
        OUT_0       = 0
