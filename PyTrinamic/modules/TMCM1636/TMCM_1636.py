'''
Created on 12.04.2021

@author: ED
'''
import PyTrinamic

" interfaces "
from PyTrinamic.modules.tmcl_module_interface import tmcl_module_interface
from PyTrinamic.modules.tmcl_motor_interface import tmcl_motor_interface

" features "
from PyTrinamic.modules.features.open_loop_ap_feature import open_loop_ap_feature
from PyTrinamic.modules.features.digital_hall_weasel_ap_feature import digital_hall_weasel_ap_feature
from PyTrinamic.modules.features.abn_encoder_ap_feature import abn_encoder_ap_feature
from PyTrinamic.modules.features.linear_ramp_ap_feature import linear_ramp_ap_feature
from PyTrinamic.modules.features.pid_ap_feature import pid_ap_feature
from PyTrinamic.modules.features.commutation_selection_ap_feature import commutation_selection_ap_feature

class TMCM_1636(tmcl_module_interface):

    def __init__(self, connection, moduleID=1):
        tmcl_module_interface.__init__(self, connection, moduleID)
        self.GP = _GP
        self.IO = _IO

        " add the motor with available features "
        self._motors.append(TMCM_1636_motor_interface(self, 0, PyTrinamic.MotorTypes.BLDC, _AP_MOTOR_0, _ENUM_MOTOR_0))

    def moduleName(self):
        return "TMCM-1636"

    def moduleDescription(self):
        return "The TMCM-1636 is a single axis servo drive platform for 3-phase BLDC motors and DC motors. Supply voltage is 8-48V."

class _AP_MOTOR_0():
    AdcPhaseA                       = 0
    AdcPhaseB                       = 1
    CurrentPhaseA                   = 2
    CurrentPhaseB                   = 3
    CurrentPhaseC                   = 4
    AdcOffsetPhaseA                 = 5
    AdcOffsetPhaseB                 = 6
    MotorPolePairs                  = 10
    MaxTorque                       = 11
    StartCurrent                    = 12
    MotorDirection                  = 13
    MotorType                       = 14
    CommutationMode                 = 15
    ActualOpenLoopAngle             = 16
    ActualEncoderAngle              = 17
    ActualHallAngle                 = 18
    ActualAbsoluteEncoderAngle      = 19
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
    Acceleration                    = 44
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
    BrakeEnabled                    = 120
    BrakeDutyCycle0                 = 121
    BrakeDutyCycle1                 = 122
    BrakePhase0Duration             = 123
    EnableBrakeOutput               = 124
    InvertBrakeOutput               = 125
    BrakeChopperEnabled             = 140
    BrakeChopperVoltage             = 141
    BrakeChopperHysteresis          = 142
    BrakeChopperActive              = 144
    StatusFlags                     = 156
    AbsoluteEncoderType             = 160
    AbsoluteEncoderInit             = 161
    AbsoluteEncoderDirection        = 162
    AbsoluteEncoderOffset           = 163
    AbsoluteEncoderDataLength       = 165
    AbsoluteEncoderPositionStart    = 166
    AbsoluteEncoderPositionLength   = 167
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

class _ENUM_MOTOR_0():
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

class _GP():
    serialBaudRate                  = 65
    serialAddress                   = 66
    CANBitRate                      = 69
    CANsendID                       = 70
    CANreceiveID                    = 71
    telegramPauseTime               = 75
    serialHostAddress               = 76
    autoStartMode                   = 77
    applicationStatus               = 128
    programCounter                  = 130
    tickTimer                       = 132

class _IO():
    GPI_0   = 0
    GPI_1   = 1
    GPI_2   = 2
    GPI_3   = 3

class TMCM_1636_motor_interface(tmcl_motor_interface):

    def __init__(self, parent, axisID, motorType, axisParameter, constants):
        tmcl_motor_interface.__init__(self, parent, axisID, motorType, axisParameter, constants)

        " add features "

        self.openLoop = open_loop_ap_feature(self)
        self.feature.update({"open_loop" : self.openLoop})

        self.digitalHall = digital_hall_weasel_ap_feature(self)
        self.feature.update({"digital_hall" : self.digitalHall})

        self.abnEncoder = abn_encoder_ap_feature(self)
        self.feature.update({"abn_encoder" : self.abnEncoder})

        self.linearRamp = linear_ramp_ap_feature(self)
        self.linearRamp.disableMotorHaltedVelocity()
        self.feature.update({"linear_ramp" : self.linearRamp})

        self.pid = pid_ap_feature(self)
        self.feature.update({"pid" : self.pid})

        self.commutationSelection = commutation_selection_ap_feature(self)
        self.feature.update({"commutation_selection" : self.commutationSelection})

    " motor type "
    def setMotorType(self, motorType):
        self.setAxisParameter(self.AP.MotorType, motorType)

    def motorType(self):
        return self.axisParameter(self.AP.MotorType)

    " motor pole pairs "
    def setMotorPolePairs(self, polePairs):
        self.setAxisParameter(self.AP.MotorPolePairs, polePairs)

    def motorPolePairs(self):
        return self.axisParameter(self.AP.MotorPolePairs)
