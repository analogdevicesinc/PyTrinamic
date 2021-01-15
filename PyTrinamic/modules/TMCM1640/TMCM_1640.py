'''
Created on 25.02.2019
@author: ED
'''

class TMCM_1640():
    def __init__(self, connection, module_id=1):
        self.connection = connection

        self.GPs   = _GPs
        self.APs   = _APs
        self.ENUMs = _ENUMs

        self.MODULE_ID = module_id

        self.motor = 0

    def showChipInfo(self):
        ("The TMCM-1640 is a highly compact controller/driver module for brushless DC (BLDC) motors with up to 5A coil current, optional encoder and/or hall sensor feedback. Voltage supply: 12 - 28,5");

    " axis parameter access "
    def axisParameter(self, apType, axis):
        return self.connection.axisParameter(apType, axis, self.MODULE_ID)

    def setAxisParameter(self, apType, axis, value):
        self.connection.setAxisParameter(apType, axis, value, self.MODULE_ID)

    " global parameter access "
    def globalParameter(self, gpType, bank):
        return self.connection.globalParameter(gpType, bank, self.MODULE_ID)

    def setGlobalParameter(self, gpType, bank, value):
        self.connection.setGlobalParameter(gpType, bank, value, self.MODULE_ID)

    " standard functions "
    def moveToPosition(self, axis, position):
        self.setAxisParameter(self.APs.TargetPosition, axis, position)

    def targetPosition(self, axis):
        return self.axisParameter(self.APs.TargetPosition, axis)

    def actualPosition(self, axis):
        return self.axisParameter(self.APs.ActualPosition, axis)

    def setActualPosition(self, axis, position):
        return self.setAxisParameter(self.APs.ActualPosition, axis, position)

    def rotate(self, axis, velocity):
        self.setAxisParameter(self.APs.TargetVelocity, axis, velocity)

    def actualVelocity(self, axis):
        return self.axisParameter(self.APs.ActualVelocity, axis)

    def setTargetTorque(self, axis, torque):
        self.setAxisParameter(self.APs.TargetTorque, axis, torque)

    def targetTorque(self, axis):
        return self.axisParameter(self.APs.TargetTorque, axis)

    def actualTorque(self, axis):
        return self.axisParameter(self.APs.ActualTorque, axis)

    " helpful functions "

    def maxVelocity(self, axis):
        return self.axisParameter(self.APs.MaxVelocity, axis)

    def setMaxVelocity(self, axis, maxVelocity):
        self.setAxisParameter(self.APs.MaxVelocity, axis, maxVelocity)

    def maxTorque(self, axis):
        return self.axisParameter(self.APs.MaxTorque, axis)

    def setMaxTorque(self, axis, maxTorque):
        self.setAxisParameter(self.APs.MaxTorque, axis, maxTorque)

    def openLoopTorque(self, axis):
        return self.axisParameter(self.APs.StartCurrent, axis)

    def setOpenLoopTorque(self, axis, torque):
        self.setAxisParameter(self.APs.StartCurrent, axis, torque)

    def acceleration(self, axis):
        return self.axisParameter(self.APs.Acceleration, axis)

    def setAcceleration(self, axis, acceleration):
        self.setAxisParameter(self.APs.Acceleration, axis, acceleration)

    def targetReachedVelocity(self, axis):
        return self.axisParameter(self.APs.TargetReachedVelocity, axis)

    def setTargetReachedVelocity(self, axis, velocity):
        self.setAxisParameter(self.APs.TargetReachedVelocity, axis, velocity)

    def targetReachedDistance(self, axis):
        return self.axisParameter(self.APs.TargetReachedDistance, axis)

    def setTargetReachedDistance(self, axis, distance):
        self.setAxisParameter(self.APs.TargetReachedDistance, axis, distance)

    def motorHaltedVelocity(self, axis):
        return self.axisParameter(self.APs.MotorHaltedVelocity, axis)

    def setMotorHaltedVelocity(self, axis, velocity):
        self.setAxisParameter(self.APs.MotorHaltedVelocity, axis, velocity)

    def positionReached(self, axis):
        return ((self.statusFlags(axis) & self.ENUMs.FLAG_POSITION_END) != 0)

    def rampEnabled(self, axis):
        return self.axisParameter(self.APs.EnableRamp, axis)

    def setRampEnabled(self, axis, enable):
        self.setAxisParameter(self.APs.EnableRamp, axis, enable)

    def torquePParameter(self, axis):
        return self.axisParameter(self.APs.TorqueP, axis)

    def setTorquePParameter(self, axis, pValue):
        self.setAxisParameter(self.APs.TorqueP, axis, pValue)

    def torqueIParameter(self, axis):
        return self.axisParameter(self.APs.TorqueI, axis)

    def setTorqueIParameter(self, axis, pValue):
        self.setAxisParameter(self.APs.TorqueI, axis, pValue)

    def velocityPParameter(self, axis):
        return self.axisParameter(self.APs.VelocityP, axis)

    def setVelocityPParameter(self, axis, pValue):
        self.setAxisParameter(self.APs.VelocityP, axis, pValue)

    def velocityIParameter(self, axis):
        return self.axisParameter(self.APs.VelocityI, axis)

    def setVelocityIParameter(self, axis, pValue):
        self.setAxisParameter(self.APs.VelocityI, axis, pValue)

    def positionPParameter(self, axis):
        return self.axisParameter(self.APs.PositionP, axis)

    def setPositionPParameter(self, axis, pValue):
        self.setAxisParameter(self.APs.PositionP, axis, pValue)

    def motorPoles(self, axis):
        return self.axisParameter(self.APs.MotorPoles, axis)

    def setMotorPoles(self, axis, poles):
        self.setAxisParameter(self.APs.MotorPoles, axis, poles)

    def hallInvert(self, axis):
        return self.axisParameter(self.APs.HallSensorInvert, axis)

    def setHallInvert(self, axis, invert):
        self.setAxisParameter(self.APs.HallSensorInvert, axis, invert)

    def encoderInitMode(self, axis):
        return self.axisParameter(self.APs.EncoderInitMode, axis)

    def setEncoderInitMode(self, axis, mode):
        self.setAxisParameter(self.APs.EncoderInitMode, axis, mode)

    def encoderResolution(self, axis):
        return self.axisParameter(self.APs.EncoderSteps, axis)

    def setEncoderResolution(self, axis, steps):
        self.setAxisParameter(self.APs.EncoderSteps, axis, steps)

    def encoderDirection(self, axis):
        return self.axisParameter(self.APs.EncoderDirection, axis)

    def setEncoderDirection(self, axis, direction):
        self.setAxisParameter(self.APs.EncoderDirection, axis, direction)

    def commutationMode(self, axis):
        return self.axisParameter(self.APs.CommutationMode, axis)

    def setCommutationMode(self, axis, mode):
        self.setAxisParameter(self.APs.CommutationMode, axis, mode)

    def statusFlags(self, axis):
        return self.axisParameter(self.APs.StatusFlags, axis)

    def analogInput(self, x):
        return self.connection.analogInput(x, self.MODULE_ID)

    def digitalInput(self, x):
        return self.connection.digitalInput(x, self.MODULE_ID)

    def digitalOutput(self, x):
        return self.connection.digitalOutput(x, self.MODULE_ID)

    def setDigitalOutput(self, x):
        return self.connection.setDigitalOutput(x, 1, self.MODULE_ID)

    def clearDigitalOutput(self, x):
        return self.connection.setDigitalOutput(x, 0, self.MODULE_ID)

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

class _APs():
    TargetPosition                 = 0
    ActualPosition                 = 1
    TargetVelocity                 = 2
    ActualVelocity                 = 3
    MaxVelocity                    = 4
    MaxTorque                      = 6
    TargetReachedVelocity          = 7
    MotorHaltedVelocity            = 9
    TargetReachedDistance          = 10
    Acceleration                   = 11
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
    EncoderOffset                  = 165
    TorqueP                        = 172
    TorqueI                        = 173
    StartCurrent                   = 177
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
    ActualHallAngle                = 210
    ActualEncoderAngle             = 211
    ActualControlledAngle          = 212
    PositionPIDError               = 226
    VelocityPIDError               = 228
    VelocityPIDErrorSum            = 229
    PositionP                      = 230
    VelocityP                      = 234
    VelocityI                      = 235
    InitVelocity                   = 241
    InitSineDelay                  = 244
    EncoderInitMode                = 249
    EncoderSteps                   = 250
    EncoderDirection               = 251
    HallInterpolation              = 252
    MotorPoles                     = 253
    HallSensorInvert               = 254
    EnableDriver                   = 255

class _ENUMs():
    COMM_MODE_BLOCK_HALL            = 0
    COMM_MODE_FOC_HALL              = 6
    COMM_MODE_FOC_ENCODER           = 7
    COMM_MODE_FOC_CONTROLLED        = 8

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
