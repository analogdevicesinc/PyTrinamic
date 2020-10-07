'''
Created on 24.06.2019

@author: ED
'''

import PyTrinamic

" interfaces "
from PyTrinamic.modules.tmcl_module_interface import tmcl_module_interface
from PyTrinamic.modules.tmcl_motor_interface import tmcl_motor_interface

" features "
from PyTrinamic.modules.features.open_loop_ap_feature import open_loop_ap_feature
from PyTrinamic.modules.features.spi_encoder_ap_feature import spi_encoder_ap_feature
from PyTrinamic.modules.features.linear_ramp_ap_feature import linear_ramp_ap_feature
from PyTrinamic.modules.features.pid_ap_feature import pid_ap_feature
from PyTrinamic.modules.features.commutation_selection_ap_feature import commutation_selection_ap_feature

class TMCM_1670(tmcl_module_interface):
    
    def __init__(self, connection, moduleID=1):
        tmcl_module_interface.__init__(self, connection, moduleID)
        self.GPs = _GPs

        " add the motor with available features "
        self._motors.append(TMCM_1670_motor_interface(self, 0, PyTrinamic.MotorTypes.BLDC, _AP_MOTOR_0, _ENUM_MOTOR_0)) 

    def moduleName(self):
        return "TMCM-1670"
        
    def moduleDescription(self):
        return "The TMCM-1670 is an easy to use and rather compact PANdrive™ smart BLDC motor. Supply voltage is 10-28V."

class _AP_MOTOR_0():
    TargetPosition                 = 0
    ActualPosition                 = 1
    TargetVelocity                 = 2
    ActualVelocity                 = 3
    MaxVelocity                    = 4
    TorqueLimit                    = 5
    MaxTorque                      = 6
    TargetReachedVelocity          = 7
    PositionReachedFlag            = 8
    MotorHaltedVelocity            = 9
    TargetReachedDistance          = 10
    Acceleration                   = 11
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
    EncoderOffset                  = 165
    ReferenceSwitchPolarity        = 166
    TorqueP                        = 172
    TorqueI                        = 173
    StartCurrent                   = 177
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
    EncoderInitMode                = 249
    EncoderSteps                   = 250
    EncoderDirection               = 251
    MotorPoles                     = 253
    DriverEnabled                  = 255

class _ENUM_MOTOR_0():
    COMM_MODE_FOC_ENCODER           = 7
    COMM_MODE_FOC_CONTROLLED        = 8

    ENCODER_INIT_MODE_0             = 0
    ENCODER_INIT_MODE_2             = 2

    FLAG_POSITION_END               = 0x00004000

class _GPs():
    serialBaudRate                 = 65
    serialAddress                  = 66
    CANBitRate                     = 69
    CANsendID                      = 70
    CANreceiveID                   = 71
    telegramPauseTime              = 75
    serialHostAddress              = 76
    autoStartMode                  = 77
    applicationStatus              = 128
    programCounter                 = 130
    tickTimer                      = 132

class TMCM_1670_motor_interface(tmcl_motor_interface):
    
    def __init__(self, parent, axisID, motorType, axisParameter, constants):
        tmcl_motor_interface.__init__(self, parent, axisID, motorType, axisParameter, constants)
        
        " add features "
        
        self.openLoop = open_loop_ap_feature(self)
        self.feature.update({"open_loop" : self.openLoop})

        self.spiEncoder = spi_encoder_ap_feature(self)
        self.feature.update({"spi_encoder" : self.spiEncoder})

        self.linearRamp = linear_ramp_ap_feature(self)
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
        self.setAxisParameter(self.AP.MotorPoles, polePairs*2)
 
    def motorPolePairs(self):
        return int(self.axisParameter(self.AP.MotorPoles)/2)
