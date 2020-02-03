'''
Created on 24.06.2019

@author: ED
'''

class TMCM_1670():
    def __init__(self, connection):
        self.connection = connection

        self.GPs = _GPs
        self.APs = _APs

        self.MOTORS = 1
        self.__default_motor = 0

    def showChipInfo(self):
        ("TMCM-1670. Voltage supply: not implemented yet");

    # axis parameter access
    def axisParameter(self, apType):
        return self.connection.axisParameter(apType, self.__default_motor)

    def setAxisParameter(self, apType, value):
        self.connection.setAxisParameter(apType, self.__default_motor, value)

    # global parameter access
    def globalParameter(self, gpType, bank):
        return self.connection.globalParameter(gpType, bank)

    def setGlobalParameter(self, gpType, bank, value):
        self.connection.setGlobalParameter(gpType, bank, value)

    # standard functions
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

    # helpful functions

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
 
    def motorHaltedVelocity(self):
        return self.axisParameter(self.APs.MotorHaltedVelocity)
 
    def setMotorHaltedVelocity(self, velocity):
        self.setAxisParameter(self.APs.MotorHaltedVelocity, velocity)
 
    def positionReached(self):
        return ((self.statusFlags() & self.APs.FLAG_POSITION_END) != 0)
 
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
 
    def clearOnceOnNChannel(self):
        self.setAxisParameter(self.APs.ClearOnce, 1)
        self.setAxisParameter(self.APs.ClearOnNull, 1)
 
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

