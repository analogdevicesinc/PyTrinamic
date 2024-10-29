################################################################################
# Copyright © 2022 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

import pytrinamic

" interfaces "
from ..modules import TMCLModule
from ..features import MotorControlModule, DriveSettingModule, LinearRampModule
from ..features import ABNEncoderModule, AbsoluteEncoderModule, DigitalHallModule, PIDModule

from ..features.ramp_settings_module import RampSettingsModule
from ..features.brakechopper_module import BrakeChopperModule
from ..features.referenceswitches_module import ReferenceSwitchesModule


class TMCM1690(TMCLModule):
    """
    The TMCM-1690 is a single axis servo drive platform for 3-phase BLDC motors and DC motors. Supply voltage is 8-48V.
    """
    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id, ap_index_bit_width=12)

        self.name = "TMCM-1690"
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
            self.abs_encoder = AbsoluteEncoderModule(module, axis, self.AP)
            self.digital_hall = DigitalHallModule(module, axis, self.AP)
            self.pid = PIDModule(module, axis, self.AP)
            self.brake_chopper = BrakeChopperModule(module, axis, self.AP)
            self.reference_switches = ReferenceSwitchesModule(module, axis, self.AP)
            self.ramp_settings = RampSettingsModule(module, axis, self.AP)

        def get_position_reached(self):
            return self.get_axis_parameter(self.AP.StatusFlags) & self.ENUM.FLAG_POSITION_END

        def get_target_current(self):
            return self.get_axis_parameter(self.AP.TargetTorque, signed=True)

        def set_target_current(self, value):
            return self.set_axis_parameter(self.AP.TargetTorque, value)

        def set_target_current(self):
            return self.get_axis_parameter(self.AP.ActualTorque, signed=True)

        class AP:
            MotorType                       = 0
            MotorFamily                     = 1
            MotorPolePairs                  = 2
            MotorPolePairDistance           = 3
            MotorNominalCurrent             = 4
            MotorPeakCurrent                = 5
            MotorLineToLineResistance       = 6
            MotorLineToLineInductance       = 7
            MotorTorqueConstant             = 8
            MotorInertia                    = 9
            
            RampType                        = 11
            MotorDirection                  = 12
            CommutationMode                 = 13
            Peripherals                     = 14
            CurrentSensorSelection          = 15
            MaxTorque                       = 16
            PWMScheme                       = 17
            PWMFrequency                    = 18
            PWMDeadTime                     = 19
            
            AdcPhaseA                       = 21
            AdcPhaseB                       = 22
            AdcPhaseC                       = 23
            AdcOffsetPhaseA                 = 24
            AdcOffsetPhaseB                 = 25
            AdcOffsetPhaseC                 = 26
            CurrentPhaseA                   = 27
            CurrentPhaseB                   = 28
            CurrentPhaseC                   = 29
            
            ActualOpenLoopAngle             = 31
            StartCurrent                    = 32
            OpenLoopVelocity                = 33
            OpenLoopPosition                = 34
            
            ActualHallAngle                 = 36
            HallOpenLoopAngleDiff           = 37
            HallVelocity                    = 38
            HallPosition                    = 39
            HallSensorSectorOffset          = 40
            HallSensorDirection             = 41
            HallSensorInterpolation         = 42
            HallSensorOffset                = 43
            HallSensorInputs                = 44
            HallSensorAutoConfigTrig        = 45
            
            ActualEncoderAngle              = 46
            EncoderOpenLoopAngleDiff        = 47
            EncoderVelocity                 = 48
            EncoderPosition                 = 49
            EncoderSteps                    = 50
            EncoderDirection                = 51
            EncoderInitMode                 = 52
            EncoderInitState                = 53
            EncoderInitDelay                = 54
            EncoderInitVelocity             = 55
            EncoderOffset                   = 56
            ClearOnNull                     = 57
            ClearOnce                       = 58
            EncoderInputs                   = 59
            EncoderValue                    = 60
            EncoderSensorSide               = 61
            
            Encoder2Velolcity               = 62
            Encoder2Position                = 63
            Encoder2Steps                   = 64
            Encoder2Direction               = 65
            Encoder2Inputs                  = 66
            Encoder2SensorSide              = 67
            
            ActualAbsoluteEncoderAngle      = 68
            AbsoluteEncoderOpenLoopDiff     = 69
            AbsoluteEncoderVelocity         = 70
            AbsoluteEncoderPosition         = 71
            AbsoluteEncoderType             = 72
            AbsoluteEncoderInitMode         = 73
            AbsoluteEncoderDirection        = 74
            AbsoluteEncoderOffset           = 75
            AbsoluteEncoderSensorSide       = 76
            
            TargetTorque                    = 77
            ActualTorque                    = 78
            TargetFlux                      = 79
            ActualFlux                      = 80
            TorqueOffset                    = 82
            TorqueP                         = 83
            TorqueI                         = 84
            CurrentPIDErrorSum              = 85
            FluxPIDErrorSum                 = 86
            TorquePIDError                  = 87
            FluxPIDError                    = 88
            
            VelocitySensorSelection         = 90
            VelocityUnitSelection           = 91
            TargetVelocity                  = 92
            ActualVelocity                  = 93
            MaxVelocity                     = 94
            MaxAcceleration                 = 95
            HaltedVelocity                  = 96
            VelocityOffset                  = 98
            VelocityP                       = 99
            VelocityI                       = 100
            VelocityPIDErrorSum             = 101
            VelocityPIDError                = 102
            
            PositionSensorSelection         = 104
            TargetPosition                  = 105
            ActualPosition                  = 106
            TargetReachedDistance           = 107
            TargetReachedVelocity           = 108
            PositionReachedFlag             = 109
            PositionP                       = 110
            PositionPIDError                = 111
            
            GearboxTransmissionType         = 113
            GearboxInputDisplacement        = 114
            GearboxOutputDisplacement       = 115
            GearboxInvertDirection          = 116
            
            IITThermalWindingTimeConstant1  = 118
            IITLimit1                       = 119
            IITSum1                         = 120
            IITThermalWindingTimeConstant2  = 121
            IITLimit2                       = 122
            IITSum2                         = 123
            IITClearIITExceedFlags          = 124
            
            VelocityWindow                  = 126
            ClearVelocityWindowFlag         = 127
            PositionWindow                  = 128
            ClearPositionWindowFlag         = 129
            
            RampAcceleration                = 131
            RampVelocity                    = 132
            EnableRamp                      = 133
            EnableVelocityFeedForward       = 134
            RampPosition                    = 135

            HomingMode                      = 137
            HomingState                     = 138
            HomingFastVelocity              = 139
            HomingSlowVelocity              = 140
            HomingMaxTorque                 = 141
            HomingPositionOffsetCW          = 142
            HomingPositionOffsetCCW         = 143
            HomingMinPositionLim            = 144
            HomingMaxPositionLim            = 145
            HomingTeachLim                  = 146
            
            FilterTargetTorType             = 148
            FilterTargetTorAverageFilterSize= 149
            FilterTargetTorBiquadA1         = 150
            FilterTargetTorBiquadA2         = 151
            FilterTargetTorBiquadB0         = 152
            FilterTargetTorBiquadB1         = 153
            FilterTargetTorBiquadB2         = 154
            FilterTargetTorReservedPlace    = 155
            
            FilterActualTorType             = 156
            FilterActualTorAverageFilterSize= 157
            FilterActualTorBiquadA1         = 158
            FilterActualTorBiquadA2         = 159
            FilterActualTorBiquadB0         = 160
            FilterActualTorBiquadB1         = 161
            FilterActualTorBiquadB2         = 162
            FilterActualTorReservedPlace    = 163
            
            FilterTargetVelType             = 164
            FilterTargetVelAverageFilterSize= 165
            FilterTargetVelBiquadA1         = 166
            FilterTargetVelBiquadA2         = 167
            FilterTargetVelBiquadB0         = 168
            FilterTargetVelBiquadB1         = 169
            FilterTargetVelBiquadB2         = 170
            FilterTargetVelReservedPlace    = 171
            
            FilterActualVelType             = 172
            FilterActualVelAverageFilterSize= 173
            FilterActualVelBiquadA1         = 174
            FilterActualVelBiquadA2         = 175
            FilterActualVelBiquadB0         = 176
            FilterActualVelBiquadB1         = 177
            FilterActualVelBiquadB2         = 178
            FilterActualVelReservedPlace    = 179
            
            FilterTargetPosType             = 180
            FilterTargetPosAverageFilterSize= 181
            FilterTargetPosBiquadA1         = 182
            FilterTargetPosBiquadA2         = 183
            FilterTargetPosBiquadB0         = 184
            FilterTargetPosBiquadB1         = 185
            FilterTargetPosBiquadB2         = 186
            FilterTargetPosReservedPlace    = 187
            
            ReleaseBrake                    = 188
            BrakeReleasingDutyCycle         = 189
            BrakeHoldingDutyDutyCycle       = 190
            BrakeReleasingDuration          = 191
            EnableBrakeOutput               = 192
            InvertBrakeOutput               = 193
            BrakeSupplyVoltage              = 194
            BrakeResistance                 = 195
            
            BrakeChopperEnabled             = 197
            BrakeChopperVoltage             = 198
            BrakeChopperHysteresis          = 199
            BrakeChopperType                = 200
            BrakeChopperActive              = 201
            BrakeChopperSupplyVoltage       = 202
            BrakeChopperResistance          = 203
            
            ReferenceSwitchEnable           = 205
            ReferenceSwitchPolarity         = 206
            RightStopSwitch                 = 207
            LeftStopSwitch                  = 208
            
            StatusFlags                     = 210
            SupplyVoltage                   = 211
            SupplyVoltageThreshold          = 212
            DriverTemperature               = 213
            DriverTemperatureThreshold      = 214

            Encoder2CommutationAngle        = 216

            SwitchOverVelocity              = 220
            LowerVelocityP                  = 221
            LowerVelocityI                  = 222

            DriverStatusRegistert           = 238
            ClearDriverErrorFlag            = 239
            MainLoopsPerSecond              = 240
            PWMLoopsPerSecond               = 241
            TorqueLoopsPerSecond            = 242
            VelocityLoopsPerSecond          = 243
            DebugValue0                     = 244
            DebugValue1                     = 245
            DebugValue2                     = 246
            DebugValue3                     = 247
            DebugValue4                     = 248
            DebugValue5                     = 249
            DebugValue6                     = 250
            DebugValue7                     = 251
            DebugValue8                     = 252
            DebugValue9                     = 253
            
            ReinitBLDCRegulation            = 254
            EnableDriver                    = 255

            LinearVelocityWindow            = 260
            LinearPositionWindow            = 261
            EncoderLinearResolution         = 262
            LinearMaximumVelocity           = 263
            LinearMaximumAcceleration       = 264
            LinearTargetVelocity            = 265
            LinearActualVelocity            = 266
            LinearTargetPosition            = 267
            LinearActualPosition            = 268
            LinearRampVelocity              = 269
            LinearRampPosition              = 270
            LinearVelocityOffset            = 271
            LinearSwitchOverVelocity        = 272
            LinearCatchUpVelocity           = 273

        class ENUM:
            COMM_MODE_DISABLED              = 0
            COMM_MODE_OPENLOOP              = 1
            COMM_MODE_FOC_DIGITAL_HALL      = 2
            COMM_MODE_BLOCK_HALL            = 3
            COMM_MODE_FOC_ABN_ENCODER       = 4
            COMM_MODE_FOC_ABS_ENCODER       = 5
        
            ENCODER_INIT_MODE_0             = 0
            ENCODER_INIT_MODE_1             = 1
            ENCODER_INIT_MODE_2             = 2
            ENCODER_INIT_MODE_3             = 3
            ENCODER_INIT_MODE_4             = 4
        
            ABS_ENCODER_TYPE_DISABLED       = 0
            ABS_ENCODER_AM4096              = 1
            ABS_ENCODER_MU150               = 2

            ABS_ENCODER_INIT_MODE_ESTIMATE_OFFSET = 0
            ABS_ENCODER_INIT_MODE_ESTIMATE_OFFSET_SHAKING = 1
            ABS_ENCODER_INIT_MODE_USE_OFFSET = 2

            POS_SELECTION_SAME              = 0
            POS_SELECTION_HALL              = 1
            POS_SELECTION_ABN               = 2
            POS_SELECTION_ABN2              = 3
            POS_SELECTION_ABS               = 4
        
            VEL_SELECTION_SAME              = 0
            VEL_SELECTION_HALL              = 1
            VEL_SELECTION_ABN               = 2
            VEL_SELECTION_ABN2              = 3
            VEL_SELECTION_ABS               = 4
        
            MOTOR_TYPE_THREE_PHASE_BLDC     = 0
            MOTOR_TYPE_SINGLE_PHASE_DC      = 1
            
            FILTER_TYPE_DISABLE             = 0
            FILTER_TYPE_AVERAGE             = 1
            FILTER_TYPE_BIQUAD              = 2
            
            SIGNAL_TYPE_TARGET_TORQUE       = 0
            SIGNAL_TYPE_ACTUAL_TORQUE       = 1
            SIGNAL_TYPE_TARGET_VELOCITY     = 2
            SIGNAL_TYPE_ACTUAL_VELOCITY     = 3
            SIGNAL_TYPE_TARGET_POSITION     = 4

            FLAG_OVERCURRENT                = 0x00000001    #    0
            FLAG_UNDERVOLTAGE               = 0x00000002    #    1
            FLAG_OVERVOLTAGE                = 0x00000004    #    2
            FLAG_OVERTEMPERATURE            = 0x00000008    #    3
            
            FLAG_MOTORHALTED                = 0x00000010    #    4
            FLAG_HALLERROR                  = 0x00000020    #    5
            FLAG_DRIVER_ERROR               = 0x00000040    #    6
            FLAG_INIT_ERROR                 = 0x00000080    #    7
            
            FLAG_STOP_MODE                  = 0x00000100    #    8
            FLAG_VELOCITY_MODE              = 0x00000200    #    9
            FLAG_POSITION_MODE              = 0x00000400    #    10
            FLAG_TORQUE_MODE                = 0x00000800    #    11
            
            FLAG_VELOCITY_WINDOW_ERROR      = 0x00001000    #    12
            FLAG_POSITION_WINDOW_ERROR      = 0x00002000    #    13
            FLAG_POSITION_END               = 0x00004000    #    14
            FLAG_MODULE_INITIALIZED         = 0x00008000    #    15
            
            FLAG_ETHERCAT_TIMEOUT           = 0x00010000    #    16
            FLAG_IIT_EXCEEDED_1             = 0x00020000    #    17
            FLAG_IIT_EXCEEDED_2             = 0x00040000    #    18
            FLAG_BRAKE_ACTIVE               = 0x00080000    #    19
            
            FLAG_HOMED                      = 0x00100000    #    21
            FLAG_HOMING                     = 0x00200000    #    22
            FLAG_MIN_POS_LIMIT              = 0x00400000    #    23
            FLAG_MAX_POS_LIMIT              = 0x00800000    #    24
    
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
        GPI_2               = 0
        GPI_3               = 1
        GPI_4               = 2
        GPI_5               = 3
        GPI_6               = 4
        GPI_7               = 5
        REF_R               = 6
        REF_L               = 7
        # ENABLE              = 2

    class AIN:
        ADC_phase_A         = 0
        ADC_phase_B         = 1
        ADC_phase_C         = 2
        ADC_VSupply         = 3
        ADC_Temp            = 4
        ADC_VSupply_12V     = 5
        ADC_VSupply_5V      = 6
        ADC_IN_0            = 7
