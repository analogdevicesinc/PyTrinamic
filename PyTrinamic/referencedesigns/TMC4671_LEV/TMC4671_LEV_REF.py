'''
Created on 08.01.2021

@author: ED
'''

import PyTrinamic

" interfaces "
from PyTrinamic.modules.tmcl_module_interface import tmcl_module_interface
from PyTrinamic.modules.tmcl_motor_interface import tmcl_motor_interface

" features "
from PyTrinamic.modules.features.open_loop_ap_feature import open_loop_ap_feature
from PyTrinamic.modules.features.digital_hall_weasel_ap_feature import digital_hall_weasel_ap_feature
from PyTrinamic.modules.features.linear_ramp_ap_feature import linear_ramp_ap_feature
from PyTrinamic.modules.features.pid_ap_feature import pid_ap_feature
from PyTrinamic.modules.features.commutation_selection_ap_feature import commutation_selection_ap_feature

class TMC4671_LEV_REF(tmcl_module_interface):
    
    def __init__(self, connection, moduleID=1):
        tmcl_module_interface.__init__(self, connection, moduleID)
        self.GP = _GP

        " add the motor with available features "
        self._motors.append(TMC4671_LEV_REF_motor_interface(self, 0, PyTrinamic.MotorTypes.BLDC, _AP_MOTOR_0, _ENUM_MOTOR_0)) 

    def moduleName(self):
        return "TMC4671-LEV-REF"

    def moduleDescription(self):
        return "The TMC4671-LEV-REF is a highly compact controller/driver module for brushless DC (BLDC) motors with up to 30A coil current and hall sensor feedback. Supply voltage is 24-48V."

class _AP_MOTOR_0():
    AdcPhaseA                       = 3
    AdcPhaseB                       = 4
    AdcOffsetPhaseA                 = 5
    AdcOffsetPhaseB                 = 6
    CurrentPhaseA                   = 7
    CurrentPhaseB                   = 8
    CurrentPhaseC                   = 9
    DualShuntFactor                 = 10
    OpenLoopCurrent                 = 12
    " only for compatibility => "
    StartCurrent                    = 12
    " <= only for compatibility "
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
    DriverEnabled                   = 255

class _ENUM_MOTOR_0():
    COMM_MODE_DISABLED              = 0
    COMM_MODE_OPENLOOP              = 1
    COMM_MODE_HALL                  = 2
    COMM_MODE_HALL_PEDAL_CONTROLLED = 3

class _GP():
    SerialBaudRate      = 65
    SerialAddress       = 66
    CANBitRate          = 69
    CANsendID           = 70
    CANreceiveID        = 71
    SerialHostAddress   = 76
  
class TMC4671_LEV_REF_motor_interface(tmcl_motor_interface):
    
    def __init__(self, parent, axisID, motorType, axisParameter, constants):
        tmcl_motor_interface.__init__(self, parent, axisID, motorType, axisParameter, constants)
        
        " add features "
        
        self.openLoop = open_loop_ap_feature(self)
        self.feature.update({"open_loop" : self.openLoop})

        self.digitalHall = digital_hall_weasel_ap_feature(self)
        self.feature.update({"digital_hall" : self.digitalHall})

        self.linearRamp = linear_ramp_ap_feature(self)
        self.linearRamp.disableMotorHaltedVelocity()
        self.linearRamp.disableTargetReachedVelocity()
        self.linearRamp.disableTargetReachedDistance()
        self.feature.update({"linear_ramp" : self.linearRamp})
        
        self.pid = pid_ap_feature(self)
        self.feature.update({"pid" : self.pid})

        self.commutationSelection = commutation_selection_ap_feature(self)
        self.feature.update({"commutation_selection" : self.commutationSelection})

    " motor type (BLDC only) "
    def setMotorType(self, motorType):
        pass
    
    def motorType(self):
        return PyTrinamic.MotorTypes.BLDC

    " motor pole pairs "
    def setMotorPolePairs(self, polePairs):
        self.setAxisParameter(self.AP.MotorPolePairs, polePairs)
 
    def motorPolePairs(self):
        return self.axisParameter(self.AP.MotorPolePairs)
