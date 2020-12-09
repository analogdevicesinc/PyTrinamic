'''
Created on 21.05.2019

@author: LH
'''

class TMCM_1161():
    def __init__(self, connection):
        self.connection = connection

        self.GPs   = _GPs
        self.APs   = _APs
        self.ENUMs = _ENUMs

        self.MOTORS = 1
        self.__default_motor = 0

    def showChipInfo(self):
        ("The TMCM-1161 is a single axis controller/driver module for 2-phase bipolar stepper motors with state of theart feature set. Voltage supply: 10 - 30V");

    # Axis parameter access
    def getAxisParameter(self, apType, axis, signed=False):
        return self.connection.axisParameter(apType, self.__default_motor, signed=signed)

    def setAxisParameter(self, apType, axis, value):
        self.connection.setAxisParameter(apType, self.__default_motor, value)

    # Global parameter access
    def getGlobalParameter(self, gpType, bank):
        return self.connection.globalParameter(gpType, bank)

    def setGlobalParameter(self, gpType, bank, value):
        self.connection.setGlobalParameter(gpType, bank, value)

    # Motion Control functions
    def rotate(self, velocity):
        self.setRampMode(2)

        self.setAxisParameter(self.APs.TargetVelocity, self.__default_motor, velocity)

    def stop(self):
        self.rotate(0)

    def moveTo(self, position, velocity=None):
        if velocity:
            self.setMaxVelocity(velocity)

        self.setTargetPosition(position)

        self.setRampMode(0)

    def moveBy(self, difference, velocity=None):
        position = difference + self.getActualPosition()

        self.moveTo(position, velocity)

        return position

    # Current control functions
    def setMotorRunCurrent(self, current):
        self.setMaxCurrent(current)

    def setMotorStandbyCurrent(self, current):
        self.setAxisParameter(self.APs.StandbyCurrent, self.__default_motor, current)

    def getMaxCurrent(self):
        return self.getAxisParameter(self.APs.MaxCurrent, self.__default_motor)

    def setMaxCurrent(self, current):
        self.setAxisParameter(self.APs.MaxCurrent, self.__default_motor,  current)

    # StallGuard2 Functions
    def setStallguard2Filter(self, enableFilter):
        self.setAxisParameter(self.APs.SG2FilterEnable, self.__default_motor, enableFilter)

    def setStallguard2Threshold(self, threshold):
        self.setAxisParameter(self.APs.SG2Threshold, self.__default_motor, threshold)

    def setStopOnStallVelocity(self, velocity):
        self.setAxisParameter(self.APs.SmartEnergyStallVelocity, self.__default_motor, velocity)

    # Motion parameter functions
    def getTargetPosition(self):
        return self.getAxisParameter(self.APs.TargetPosition, self.__default_motor, signed=True)

    def setTargetPosition(self, position):
        self.setAxisParameter(self.APs.TargetPosition, self.__default_motor, position)

    def getActualPosition(self):
        return self.getAxisParameter(self.APs.ActualPosition, self.__default_motor, signed=True)

    def setActualPosition(self, position):
        return self.setAxisParameter(self.APs.ActualPosition, self.__default_motor, position)

    def getTargetVelocity(self):
        return self.getAxisParameter(self.APs.TargetVelocity, self.__default_motor, signed=True)

    def setTargetVelocity(self, velocity):
        self.setAxisParameter(self.APs.TargetVelocity, self.__default_motor, velocity)

    def getActualVelocity(self):
        return self.getAxisParameter(self.APs.ActualVelocity, self.__default_motor, signed=True)

    def getMaxVelocity(self):
        return self.getAxisParameter(self.APs.MaxVelocity, self.__default_motor)

    def setMaxVelocity(self, velocity):
        self.setAxisParameter(self.APs.MaxVelocity, self.__default_motor, velocity)

    def getMaxAcceleration(self):
        return self.getAxisParameter(self.APs.MaxAcceleration, self.__default_motor)

    def setMaxAcceleration(self, acceleration):
        self.setAxisParameter(self.APs.MaxAcceleration, self.__default_motor, acceleration)

    def getRampMode(self):
        return self.getAxisParameter(self.APs.RampMode, self.__default_motor)

    def setRampMode(self, mode):
        return self.setAxisParameter(self.APs.RampMode, self.__default_motor, mode)

    # Status functions
    def getStatusFlags(self):
        return self.getAxisParameter(self.APs.DrvStatusFlags, self.__default_motor)

    def getErrorFlags(self):
        return self.getAxisParameter(self.APs.ExtendedErrorFlags, self.__default_motor)

    def positionReached(self):
        return self.getAxisParameter(self.APs.PositionReachedFlag, self.__default_motor)

    # IO pin functions
    def analogInput(self, x):
        return self.connection.analogInput(x)

    def digitalInput(self, x):
        return self.connection.digitalInput(x)

class _APs():
    TargetPosition                 = 0
    ActualPosition                 = 1
    TargetVelocity                 = 2
    ActualVelocity                 = 3
    MaxVelocity                    = 4
    MaxAcceleration                = 5
    MaxCurrent                     = 6
    StandbyCurrent                 = 7
    PositionReachedFlag            = 8
    referenceSwitchStatus          = 9
    RightEndstop                   = 10
    LeftEndstop                    = 11
    rightLimitSwitchDisable        = 12
    leftLimitSwitchDisable         = 13
    minimumSpeed                   = 130
    actualAcceleration             = 135
    RampMode                       = 138
    MicrostepResolution            = 140
    Ref_SwitchTolerance            = 141
    softStopFlag                   = 149
    EndSwitchPowerDown             = 150
    rampDivisor                    = 153
    PulseDivisor                   = 154
    Intpol                         = 160
    DoubleEdgeSteps                = 161
    ChopperBlankTime               = 162
    ConstantTOffMode               = 163
    DisableFastDecayComparator     = 164
    ChopperHysteresisEnd           = 165
    ChopperHysteresisStart         = 166
    TOff                           = 167
    SEIMIN                         = 168
    SECDS                          = 169
    smartEnergyHysteresis          = 170
    SECUS                          = 171
    smartEnergyHysteresisStart     = 172
    SG2FilterEnable                = 173
    SG2Threshold                   = 174
    slopeControlHighSide           = 175
    slopeControlLowSide            = 176
    ShortToGroundProtection        = 177
    ShortDetectionTime             = 178
    VSense                         = 179
    smartEnergyActualCurrent       = 180
    smartEnergyStallVelocity       = 181
    smartEnergyThresholdSpeed      = 182
    smartEnergySlowRunCurrent      = 183
    RandomTOffMode                 = 184
    ReferenceSearchMode            = 193
    ReferenceSearchSpeed           = 194
    referenceSwitchSpeed           = 195
    referenceSwitchDistance        = 196
    lastReferenceSwitchPosition    = 197
    BoostCurrent                   = 200
    freewheelingDelay              = 204
    LoadValue                      = 206
    extendedErrorFlags             = 207
    DrvStatusFlags                 = 208
    EncoderPosition                = 209
    EncoderResolution              = 210
    max_EncoderDeviation           = 212
    PowerDownDelay                 = 214
    absoluteResolverValue          = 215
    Step_DirectionMode             = 254

class _ENUMs():
    FLAG_POSITION_END = 0x00004000

class _GPs():
    timer_0                        = 0
    timer_1                        = 1
    timer_2                        = 2
    stopLeft_0                     = 27
    stopRight_0                    = 28
    input_0                        = 39
    input_1                        = 40
    input_2                        = 41
    input_3                        = 42
    serialBaudRate                 = 65
    serialAddress                  = 66
    ASCIIMode                      = 67
    serialHeartbeat                = 68
    telegramPauseTime              = 75
    serialHostAddress              = 76
    autoStartMode                  = 77
    limitSwitchPolarity            = 79
    protectionMode                 = 81
    eepromCoordinateStore          = 84
    zeroUserVariables              = 85
    serialSecondaryAddress         = 87
    reverseShaftDirection          = 90
    applicationStatus              = 128
    downloadMode                   = 129
    programCounter                 = 130
    lastTmclError                  = 131
    tickTimer                      = 132
    randomNumber                   = 133
    Intpol                         = 255
