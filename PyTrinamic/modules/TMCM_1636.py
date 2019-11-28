'''
Created on 27.11.2019

@author: SW
'''

class TMCM_1636(object):

    " axis parameters "
    AP_AdcPhaseA                       = 0
    AP_AdcPhaseB                       = 1
    AP_CurrentPhaseA                   = 2
    AP_CurrentPhaseB                   = 3
    AP_CurrentPhaseC                   = 4
    AP_dualShuntOffsetPhaseA           = 5
    AP_dualShuntOffsetPhaseB           = 6
    AP_dualShuntFactor                 = 7
    AP_MotorPolePairs                  = 10
    AP_MaxTorque                       = 11
    AP_OpenLoopCurrent                 = 12
    AP_MotorType                       = 14
    AP_CommutationMode                 = 15
    AP_ActualControlledAngle           = 16
    AP_ActualEncoderAngle              = 17
    AP_ActualHallAngle                 = 18
    AP_ActualAbsoluteEncoderAngle      = 19
    AP_CommutationModePosition         = 25
    AP_TargetTorque                    = 30
    AP_ActualTorque                    = 31
    AP_TargetFlux                      = 32
    AP_TargetFlux                      = 33
    AP_TargetVelocity                  = 40
    AP_RampVelocity                    = 41
    AP_ActualVelocity                  = 42
    AP_MaxVelocity                     = 43
    AP_Acceleration                    = 44
    AP_EnableRamp                      = 45
    AP_TargetPosition                  = 50
    AP_RampPosition                    = 51
    AP_ActualPosition                  = 52
    AP_TargetReachedDistance           = 53
    AP_TargetReachedVelocity           = 54
    AP_PositionReachedFlag             = 55
    AP_TorqueP                         = 70
    AP_TorqueI                         = 71
    AP_VelocityP                       = 72
    AP_VelocityI                       = 73
    AP_PositionP                       = 74
    AP_CurrentPIDErrorSum              = 75
    AP_FluxPIDErrorSum                 = 76
    AP_VelocityPIDErrorSum             = 77
    AP_TorquePIDError                  = 78
    AP_FluxPIDError                    = 79
    AP_VelocityPIDError                = 80
    AP_PositionPIDError                = 81
    AP_HallSensorPolarity              = 90
    AP_HallSensorDirection             = 91
    AP_HallInterpolation               = 92
    AP_HallSensorOffset                = 93
    AP_EncoderSteps                    = 100
    AP_EncoderDirection                = 101
    AP_EncoderInitMode                 = 102
    AP_EncoderInitState                = 103
    AP_EncoderInitDelay                = 104
    AP_InitVelocity                    = 105
    AP_EncoderOffset                   = 106
    AP_ClearOnNull                     = 107
    AP_ClearOnce                       = 108
    AP_PWMFrequency                    = 110
    AP_BrakeEnabled                    = 120
    AP_BrakeDutyCycle0                 = 121
    AP_BrakeDutyCycle1                 = 122
    AP_BrakePhase0Duration             = 123
    AP_BrakeEnableFunctionality        = 124
    AP_BrakeInvert                     = 125
    AP_BrakeChopperEnabled             = 140
    AP_BrakeChopperVoltage             = 141
    AP_BrakeChopperHysteresis          = 142
    AP_BrakeChopperActive              = 144
    AP_StatusFlags                     = 156
    AP_AbsoluteEncoderType             = 160
    AP_AbsoluteEncoderInit             = 161
    AP_AbsoluteEncoderDirection        = 162
    AP_AbsoluteEncoderOffset           = 163
    AP_ReferenceSwitchEnable           = 209
    AP_ReferenceSwitchPolarity         = 210
    AP_RightStopSwitch                 = 211
    AP_LeftStopSwitch                  = 212
    AP_HomeStopSwitch                  = 213
    AP_SupplyVoltage                   = 220
    AP_DriverTemperature               = 221
        
    FLAG_POSITION_END               = 0x00004000

    COMM_MODE_DISABLED = 0
    COMM_MODE_OPENLOOP = 1
    COMM_MODE_HALL = 2
    COMM_MODE_ABN = 3
    COMM_MODE_ABS = 4
    
    POS_MODE_SAME = 0
    POS_MODE_ABN = 1
    POS_MODE_ABS = 2



    def __init__(self, connection):
        self.connection = connection
        self.motor = 0

    " axis parameter access "
    def axisParameter(self, apType):
        return self.connection.axisParameter(apType, self.motor)

    def setAxisParameter(self, apType, value):
        self.connection.setAxisParameter(apType, self.motor, value)

    " global parameter access "
    def globalParameter(self, gpType):
        return self.connection.globalParameter(gpType, self.motor)

    def setGlobalParameter(self, gpType, value):
        self.connection.setGlobalParameter(gpType, self.motor, value)

    " standard functions "
    def moveToPosition(self, position):
        self.setAxisParameter(self.AP_TargetPosition, position)

    def targetPosition(self):
        return self.axisParameter(self.AP_TargetPosition)

    def actualPosition(self):
        return self.axisParameter(self.AP_ActualPosition)

    def setActualPosition(self, position):
        return self.setAxisParameter(self.AP_ActualPosition, position)

    def rotate(self, velocity):
        self.setAxisParameter(self.AP_TargetVelocity, velocity)

    def actualVelocity(self):
        return self.axisParameter(self.AP_ActualVelocity)


