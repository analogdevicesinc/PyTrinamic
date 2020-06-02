'''
Created on 04.05.2020

@author: JM
'''

class _APs():
    AdcPhaseA                      = 0
    AdcPhaseB                      = 1
    CurrentPhaseA                  = 2
    CurrentPhaseB                  = 3
    CurrentPhaseC                  = 4
    dualShuntOffsetPhaseA          = 5
    dualShuntOffsetPhaseB          = 6
    dualShuntFactor                = 7
    MotorPolePairs                 = 10
    MaxTorque                      = 11
    OpenLoopCurrent                = 12
    MotorType                      = 14
    CommutationMode                = 15
    ActualControlledAngle          = 16
    ActualEncoderAngle             = 17
    ActualHallAngle                = 18
    ActualAbsoluteEncoderAngle     = 19
    CommutationModePosition        = 25
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
    HallSensorPolarity             = 90
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
    PWMFrequency                   = 110
    BrakeEnabled                   = 120
    BrakeDutyCycle0                = 121
    BrakeDutyCycle1                = 122
    BrakePhase0Duration            = 123
    BrakeEnableFunctionality       = 124
    BrakeInvert                    = 125
    BrakeChopperEnabled            = 140
    BrakeChopperVoltage            = 141
    BrakeChopperHysteresis         = 142
    BrakeChopperActive             = 144
    StatusFlags                    = 156
    AbsoluteEncoderType            = 160
    AbsoluteEncoderInit            = 161
    AbsoluteEncoderDirection       = 162
    AbsoluteEncoderOffset          = 163
    ReferenceSwitchEnable          = 209
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
    DriverEnabled                  = 255

class _ENUMs():
    COMM_MODE_DISABLED = 0
    COMM_MODE_OPENLOOP = 1
    COMM_MODE_HALL = 2
    COMM_MODE_ABN = 3
    COMM_MODE_ABS = 4

    POS_MODE_SAME = 0
    POS_MODE_ABN = 1
    POS_MODE_ABS = 2

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


class TMCM_1636():
    ENUMs = _ENUMs
    APs   = _APs
    GPs   = _GPs

    def __init__(self, connection):

        self.connection = connection
        self.motor = 0

    @staticmethod
    def getEdsFile():
        return __file__.replace("TMCM_1636.py", "TMCM_1636_Hw1.1_Fw1.08.eds")

    def showChipInfo(self):
        ("The TMCM-1636 is a single axis servo drive platform for 3-phase BLDC motors and DC motors. Voltage supply: 8 - 28V");

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
