'''
Created on 25.02.2019

@author: ED
'''

class TMCM_1640(object):
    
    " axis parameters "
    AP_TargetPosition               = 0
    AP_ActualPosition               = 1
    AP_TargetVelocity               = 2
    AP_ActualVelocity               = 3
    AP_MaxVelocity                  = 4
    AP_MaxTorque                    = 6
    AP_TargetReachedVelocity        = 7
    AP_MotorHaltedVelocity          = 9
    AP_TargetReachedDistance        = 10 
    AP_Acceleration                 = 11
    AP_RampVelocity                 = 13
    AP_ThermalWindingTimeConstant   = 25
    AP_IItlimit                     = 26
    AP_IItSum                       = 27
    AP_IItExceededCounter           = 28
    AP_ClearIItExceededFlag         = 29
    AP_ReinitBldcRegulation         = 31
    AP_EnableRamp                   = 146
    AP_ActualTorque                 = 150
    AP_SupplyVoltage                = 151
    AP_DriverTemperature            = 152
    AP_TargetTorque                 = 155
    AP_StatusFlags                  = 156
    AP_CommutationMode              = 159
    AP_ClearOnNull                  = 161
    AP_ClearOnce                    = 163
    AP_EncoderOffset                = 165
    AP_TorqueP                      = 172
    AP_TorqueI                      = 173
    AP_StartCurrent                 = 177
    AP_CurrentPIDError              = 200
    AP_CurrentPIDErrorSum           = 201
    AP_ActualHallAngle              = 210
    AP_ActualEncoderAngle           = 211
    AP_ActualControlledAngle        = 212
    AP_PositionPIDError             = 226
    AP_VelocityPIDError             = 228
    AP_VelocityPIDErrorSum          = 229
    AP_PositionP                    = 230
    AP_VelocityP                    = 234
    AP_VelocityI                    = 235
    AP_InitVelocity                 = 241
    AP_InitSineDelay                = 244
    AP_EncoderInitMode              = 249
    AP_EncoderSteps                 = 250
    AP_EncoderDirection             = 251
    AP_HallInterpolation            = 252
    AP_MotorPoles                   = 253
    AP_HallSensorInvert             = 254
    
    COMM_MODE_BLOCK_HALL            = 0
    COMM_MODE_FOC_HALL              = 6
    COMM_MODE_FOC_ENCODER           = 7
    COMM_MODE_FOC_CONTROLLED        = 8
    
    ENCODER_INIT_MODE_0             = 0
    ENCODER_INIT_MODE_1             = 1
    ENCODER_INIT_MODE_2             = 2
    
    FLAG_POSITION_END               = 0x00004000
    
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

    " helpful functions "

    def maxVelocity(self):
        return self.axisParameter(self.AP_MaxVelocity)
    
    def setMaxVelocity(self, maxVelocity):
        self.setAxisParameter(self.AP_MaxVelocity, maxVelocity)
    
    def maxTorque(self):
        return self.axisParameter(self.AP_MaxTorque)
        
    def setMaxTorque(self, maxTorque):
        self.setAxisParameter(self.AP_MaxTorque, maxTorque)

    def openLoopTorque(self):
        return self.axisParameter(self.AP_StartCurrent)
    
    def setOpenLoopTorque(self, torque):
        self.setAxisParameter(self.AP_StartCurrent, torque)

    def acceleration(self):
        return self.axisParameter(self.AP_Acceleration)

    def setAcceleration(self, acceleration):
        self.setAxisParameter(self.AP_Acceleration, acceleration)

    def targetReachedVelocity(self):
        return self.axisParameter(self.AP_TargetReachedVelocity)
    
    def setTargetReachedVelocity(self, velocity):
        self.setAxisParameter(self.AP_TargetReachedVelocity, velocity)

    def targetReachedDistance(self):
        return self.axisParameter(self.AP_TargetReachedDistance)
    
    def setTargetReachedDistance(self, distance):
        self.setAxisParameter(self.AP_TargetReachedDistance, distance)

    def motorHaltedVelocity(self):
        return self.axisParameter(self.AP_MotorHaltedVelocity)
    
    def setMotorHaltedVelocity(self, velocity):
        self.setAxisParameter(self.AP_MotorHaltedVelocity, velocity)

    def positionReached(self):
        return ((self.statusFlags() & self.FLAG_POSITION_END) != 0)

    def rampEnabled(self):
        return self.axisParameter(self.AP_EnableRamp)
    
    def setRampEnabled(self, enable):
        self.setAxisParameter(self.AP_EnableRamp, enable) 

    def torquePParameter(self):
        return self.axisParameter(self.AP_TorqueP)
    
    def setTorquePParameter(self, pValue):
        self.setAxisParameter(self.AP_TorqueP, pValue)

    def torqueIParameter(self):
        return self.axisParameter(self.AP_TorqueI)
    
    def setTorqueIParameter(self, pValue):
        self.setAxisParameter(self.AP_TorqueI, pValue)

    def velocityPParameter(self):
        return self.axisParameter(self.AP_VelocityP)
    
    def setVelocityPParameter(self, pValue):
        self.setAxisParameter(self.AP_VelocityP, pValue)

    def velocityIParameter(self):
        return self.axisParameter(self.AP_VelocityI)
    
    def setVelocityIParameter(self, pValue):
        self.setAxisParameter(self.AP_VelocityI, pValue)

    def positionPParameter(self):
        return self.axisParameter(self.AP_PositionP)
    
    def setPositionPParameter(self, pValue):
        self.setAxisParameter(self.AP_PositionP, pValue)

    def motorPoles(self):
        return self.axisParameter(self.AP_MotorPoles)
    
    def setMotorPoles(self, poles):
        self.setAxisParameter(self.AP_MotorPoles, poles)
        
    def hallInvert(self):
        return self.axisParameter(self.AP_HallSensorInvert)
    
    def setHallInvert(self, invert):
        self.setAxisParameter(self.AP_HallSensorInvert, invert)

    def encoderInitMode(self):
        return self.axisParameter(self.AP_EncoderInitMode)
    
    def setEncoderInitMode(self, mode):
        self.setAxisParameter(self.AP_EncoderInitMode, mode)

    def encoderResolution(self):
        return self.axisParameter(self.AP_EncoderSteps)
    
    def setEncoderResolution(self, steps):
        self.setAxisParameter(self.AP_EncoderSteps, steps)

    def encoderDirection(self):
        return self.axisParameter(self.AP_EncoderDirection)
    
    def setEncoderDirection(self, direction):
        self.setAxisParameter(self.AP_EncoderDirection, direction)

    def commutationMode(self):
        return self.axisParameter(self.AP_CommutationMode)
            
    def setCommutationMode(self, mode):
        self.setAxisParameter(self.AP_CommutationMode, mode)
        
    def statusFlags(self):
        return self.axisParameter(self.AP_StatusFlags)

    def analogInput(self, x):
        return self.connection.analogInput(x)

    def digitalInput(self, x):
        return self.connection.digitalInput(x)

    def showMotorConfiguration(self):
        print("Motor configuration:")
        print("\tMotor poles: " + str(self.motorPoles()))
        print("\tMax torque:  " + str(self.maxTorque()) + " mA")
        
    def showHallConfiguration(self):
        print("Hall configuration:")
        print("\tHall invert: " + str(self.hallInvert()))

    def showEncoderConfiguration(self):
        print("Encoder configuration:")
        print("\tOpen loop torque:   " + str(self.openLoopTorque()) + " mA")
        print("\tEncoder resolution: " + str(self.encoderResolution()))
        print("\tEncoder direction:  " + str(self.encoderDirection()))
        print("\tEncoder init mode:  " + str(self.encoderInitMode()))
    
    def showMotionConfiguration(self):
        print("Motion configuration:")
        print("\tMax velocity: " + str(self.maxVelocity()))
        print("\tAcceleration: " + str(self.acceleration()))
        print("\tRamp enabled: " + ("disabled" if (self.rampEnabled()==0) else "enabled"))
        print("\tMotor halted velocity:   " + str(self.motorHaltedVelocity()))        
        print("\tTarget reached velocity: " + str(self.targetReachedVelocity()))
        print("\tTarget reached distance: " + str(self.targetReachedDistance()))
        
    def showPIConfiguration(self):
        print("PI configuration:")
        print("\tTorque   P: " + str(self.torquePParameter()) + " I: " + str(self.torqueIParameter())) 
        print("\tVelocity P: " + str(self.velocityPParameter()) + " I: " + str(self.velocityIParameter()))
        print("\tPosition P: " + str(self.positionPParameter()))
        