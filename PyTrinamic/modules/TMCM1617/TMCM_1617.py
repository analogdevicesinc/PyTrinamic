'''
Created on 04.02.2020

@author: JM
'''

class TMCM_1617():
    MOTORS = 1

    def __init__(self, connection):
        
        self.GPs   = _GPs
        self.APs   = _APs
        self.ENUMs = _ENUMs

        self.connection = connection
        self.motor = 0

    @staticmethod
    def getEdsFile():
        return __file__.replace("TMCM_1617.py", "TMCM_1617_Hw1.2_Fw1.06.eds")

    def showChipInfo(self):
        ("The TMCM-1617 is a low-weight miniaturized single axis servo drive for 3-phase BLDC motors. Voltage supply: 10 - 28V");

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
        self.setAxisParameter(self.APs.TargetPosition, position)

    def targetPosition(self):
        return self.axisParameter(self.APs.TargetPosition)

    def actualPosition(self):
        return self.axisParameter(self.APs.ActualPosition)

    def setActualPosition(self, position):
        return self.setAxisParameter(self.APs.ActualPosition, position)

    def rotate(self, velocity):
        self.setAxisParameter(self.APs.TargetVelocity, velocity)

    def actualVelocity(self):
        return self.axisParameter(self.APs.ActualVelocity)

    " helpful functions "

    def maxVelocity(self):
        return self.axisParameter(self.APs.MaxVelocity)

    def setMaxVelocity(self, maxVelocity):
        self.setAxisParameter(self.APs.MaxVelocity, maxVelocity)

    def maxTorque(self):
        return self.axisParameter(self.APs.MaxTorque)

    def setMaxTorque(self, maxTorque):
        self.setAxisParameter(self.APs.MaxTorque, maxTorque)

    def openLoopTorque(self):
        return self.axisParameter(self.APs.StartCurrent)

    def setOpenLoopTorque(self, torque):
        self.setAxisParameter(self.APs.StartCurrent, torque)

    def acceleration(self):
        return self.axisParameter(self.APs.Acceleration)

    def setAcceleration(self, acceleration):
        self.setAxisParameter(self.APs.Acceleration, acceleration)

    def targetReachedVelocity(self):
        return self.axisParameter(self.APs.TargetReachedVelocity)

    def setTargetReachedVelocity(self, velocity):
        self.setAxisParameter(self.APs.TargetReachedVelocity, velocity)

    def targetReachedDistance(self):
        return self.axisParameter(self.APs.TargetReachedDistance)

    def setTargetReachedDistance(self, distance):
        self.setAxisParameter(self.APs.TargetReachedDistance, distance)

    def setPositionScalerM(self, ScaleV):
        self.setAxisParameter(self.APs.PositionScalerM, ScaleV)

    def motorHaltedVelocity(self):
        return self.axisParameter(self.APs.MotorHaltedVelocity)

    def setMotorHaltedVelocity(self, velocity):
        self.setAxisParameter(self.APs.MotorHaltedVelocity, velocity)

    def positionReached(self):
        return ((self.statusFlags() & self.ENUMs.FLAG_POSITION_END) != 0)

    def rampEnabled(self):
        return self.axisParameter(self.APs.EnableRamp)

    def setRampEnabled(self, enable):
        self.setAxisParameter(self.APs.EnableRamp, enable)

    def torquePParameter(self):
        return self.axisParameter(self.APs.TorqueP)

    def setTorquePParameter(self, pValue):
        self.setAxisParameter(self.APs.TorqueP, pValue)

    def torqueIParameter(self):
        return self.axisParameter(self.APs.TorqueI)

    def setTorqueIParameter(self, pValue):
        self.setAxisParameter(self.APs.TorqueI, pValue)

    def velocityPParameter(self):
        return self.axisParameter(self.APs.VelocityP)

    def setVelocityPParameter(self, pValue):
        self.setAxisParameter(self.APs.VelocityP, pValue)

    def velocityIParameter(self):
        return self.axisParameter(self.APs.VelocityI)

    def setVelocityIParameter(self, pValue):
        self.setAxisParameter(self.APs.VelocityI, pValue)

    def positionPParameter(self):
        return self.axisParameter(self.APs.PositionP)

    def setPositionPParameter(self, pValue):
        self.setAxisParameter(self.APs.PositionP, pValue)

    def motorPoles(self):
        return self.axisParameter(self.APs.MotorPoles)

    def setMotorPoles(self, poles):
        self.setAxisParameter(self.APs.MotorPoles, poles)

    def motorType(self):
        return self.axisParameter(self.APs.MotorType)

    def setMotorType(self, motorType):
        return self.setAxisParameter(self.APs.MotorType, motorType)

    def hallInvert(self):
        return self.axisParameter(self.APs.HallSensorInvert)

    def setHallInvert(self, invert):
        self.setAxisParameter(self.APs.HallSensorInvert, invert)

    def encoderInitMode(self):
        return self.axisParameter(self.APs.EncoderInitMode)

    def setEncoderInitMode(self, mode):
        self.setAxisParameter(self.APs.EncoderInitMode, mode)

    def encoderResolution(self):
        return self.axisParameter(self.APs.EncoderSteps)

    def setEncoderResolution(self, steps):
        self.setAxisParameter(self.APs.EncoderSteps, steps)

    def encoderDirection(self):
        return self.axisParameter(self.APs.EncoderDirection)

    def setEncoderDirection(self, direction):
        self.setAxisParameter(self.APs.EncoderDirection, direction)

    def commutationMode(self):
        return self.axisParameter(self.APs.CommutationMode)

    def setCommutationMode(self, mode):
        self.setAxisParameter(self.APs.CommutationMode, mode)

    def encoderInitState(self):
        return self.axisParameter(self.APs.EncoderInitState)
    
    def statusFlags(self):
        return self.axisParameter(self.APs.StatusFlags)

    def analogInput(self, x):
        return self.connection.analogInput(x)

    def digitalInput(self, x):
        return self.connection.digitalInput(x)

    def digitalOutput(self, x):
        return self.connection.digitalOutput(x)

    def setDigitalOutput(self, x):
        return self.connection.setDigitalOutput(x, 1)

    def clearDigitalOutput(self, x):
        return self.connection.setDigitalOutput(x, 0)

    def showMotorConfiguration(self):
        print("Motor configuration:")
        print("\tMotor poles: " + str(self.motorPoles()))
        print("\tMax torque:  " + str(self.maxTorque()) + " mA")
        print("\tMotor type:  " + str(self.motorType()))

    def showHallConfiguration(self):
        print("Hall configuration:")
#       print("\tHall invert: " + str(self.hallInvert()))

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
#       print("\tMotor halted velocity:   " + str(self.motorHaltedVelocity()))
        print("\tTarget reached velocity: " + str(self.targetReachedVelocity()))
        print("\tTarget reached distance: " + str(self.targetReachedDistance()))

    def showPIConfiguration(self):
        print("PI configuration:")
        print("\tTorque   P: " + str(self.torquePParameter()) + " I: " + str(self.torqueIParameter()))
        print("\tVelocity P: " + str(self.velocityPParameter()) + " I: " + str(self.velocityIParameter()))
        print("\tPosition P: " + str(self.positionPParameter()))

    def showCommutationMode(self):
        print("Commutation configuration:")
        print("\tCommutationMode:" + str(self.commutationMode()))

class _APs():
    AdcPhaseA                      = 0
    AdcPhaseB                      = 1
    CurrentPhaseA                  = 2
    CurrentPhaseB                  = 3
    CurrentPhaseC                  = 4
    AdcOffsetPhaseA                = 5
    AdcOffsetPhaseB                = 6
    dualShuntFactor                = 7
    MotorPoles                     = 10
    MaxTorque                      = 11
    StartCurrent                   = 12
    MotorType                      = 14
    CommutationMode                = 15
    ActualControlledAngle          = 16
    ActualEncoderAngle             = 17
    ActualHallAngle                = 18
    TargetTorque                   = 30
    ActualTorque                   = 31
    TargetFlux                     = 32
    ActualFlux                     = 33
    TargetVelocity                 = 40
    RampVelocity                   = 41
    ActualVelocity                 = 42
    MaxVelocity                    = 43
    Acceleration                   = 44
    EnableRamp                     = 45
    TargetPosition                 = 50
    RampPosition                   = 51
    ActualPosition                 = 52
    TargetReachedDistance          = 53
    TargetReachedVelocity          = 54
    PositionReachedFlag            = 55
    PositionScalerM                = 56
    TorqueP                        = 70
    TorqueI                        = 71
    VelocityP                      = 72
    VelocityI                      = 73
    PositionP                      = 74
    CurrentPIDErrorSum             = 75
    FluxPIDErrorSum                = 76
    VelocityPIDErrorSum            = 77
    TorquePIDError                 = 78
    FluxPIDError                   = 79
    VelocityPIDError               = 80
    PositionPIDError               = 81
    HallSensorInvert               = 90
    HallSensorDirection            = 91
    HallInterpolation              = 92
    HallSensorOffset               = 93
    EncoderSteps                   = 100
    EncoderDirection               = 101
    EncoderInitMode                = 102
    EncoderInitState               = 103
    EncoderInitDelay               = 104
    InitVelocity                   = 105
    EncoderOffset                  = 106
    ClearOnNull                    = 107
    ClearOnce                      = 108
    StatusFlags                    = 156
    ReferenceSwitchPolarity        = 210
    RightStopSwitch                = 211
    LeftStopSwitch                 = 212
    HomeStopSwitch                 = 213
    SupplyVoltage                  = 220
    DriverTemperature              = 221
    MainLoopsPerSecond             = 230
    TorqueLoopsPerSecond           = 231
    VelocityLoopsPerSecond         = 232
    DebugValue0                    = 240
    DebugValue1                    = 241
    DebugValue2                    = 242
    DebugValue3                    = 243
    DebugValue4                    = 244
    DebugValue5                    = 245
    DebugValue6                    = 246
    DebugValue7                    = 247
    DebugValue8                    = 248
    DebugValue9                    = 249
    EnableDriver                   = 255

class _ENUMs():
    COMM_MODE_BLOCK_HALL            = 0
    COMM_MODE_FOC_CONTROLLED        = 1
    COMM_MODE_FOC_HALL              = 2
    COMM_MODE_FOC_ENCODER           = 3

    ENCODER_INIT_MODE_0             = 0
    ENCODER_INIT_MODE_1             = 1
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
