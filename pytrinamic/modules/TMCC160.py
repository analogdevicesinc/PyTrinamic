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
from ..features import ABNEncoderModule, DigitalHallModule, PIDModule


class TMCC160(TMCLModule):
    """
    The TMCC160 is designed for evaluating all features of the TMCC160-LC motionCookie. Supply voltage is 7-24V.
    """
    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)

        self.name = "TMCC-160"
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

    def move_by(self, axis, delta, velocity=None):
        if velocity:
            self.motors[axis].linear_ramp.max_velocity = velocity
        self.connection.move_by(axis, delta, self.module_id)

    class _MotorTypeA(MotorControlModule):

        def __init__(self, module, axis):
            MotorControlModule.__init__(self, module, axis, self.AP)
            self.drive_settings = DriveSettingModule(module, axis, self.AP)
            self.linear_ramp = LinearRampModule(module, axis, self.AP)
            self.abn_encoder = ABNEncoderModule(module, axis, self.AP)
            self.digital_hall = DigitalHallModule(module, axis, self.AP)
            self.pid = PIDModule(module, axis, self.AP)

        def get_position_reached(self):
            return self.get_axis_parameter(self.AP.StatusFlags) & self.ENUM.FLAG_POSITION_END

        class AP:
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

        class ENUM:
            COMM_MODE_BLOCK_HALL           = 0
            COMM_MODE_FOC_HALL             = 6
            COMM_MODE_FOC_ENCODER          = 7
            COMM_MODE_FOC_CONTROLLED       = 8

            ENCODER_INIT_MODE_0            = 0
            ENCODER_INIT_MODE_1            = 1
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
        REF_R        = 0
        REF_L        = 1
        ENABLE       = 2

    class AIN:
        ADC_IN_0            = 0
        ADC_single_shunt    = 1
        ADC_phase_A         = 2
        ADC_phase_B         = 3
        ADC_VSupply         = 4
        ADC_Temp            = 5
