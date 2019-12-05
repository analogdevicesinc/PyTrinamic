'''
Created on 21.05.2019

@author: LH
'''

class TMCM_6212():
    def __init__(self, connection):
        self.__connection = connection

        self.GPs = _GPs
        self.APs = _APs

        self.MOTORS = 6

    # Axis parameter access
    def getAxisParameter(self, apType, axis):
        if not(0 <= axis < self.MOTORS):
            raise ValueError("Axis index out of range")

        return self.__connection.axisParameter(apType, axis)

    def setAxisParameter(self, apType, axis, value):
        if not(0 <= axis < self.MOTORS):
            raise ValueError("Axis index out of range")

        self.__connection.setAxisParameter(apType, axis, value)

    # Global parameter access
    def getGlobalParameter(self, gpType, bank):
        if not(0 <= bank < self.MOTORS):
            raise ValueError("Bank index out of range")

        return self.__connection.globalParameter(gpType, bank)

    def setGlobalParameter(self, gpType, bank, value):
        if not(0 <= bank < self.MOTORS):
            raise ValueError("Bank index out of range")

        self.__connection.setGlobalParameter(gpType, bank, value)

    # Motion Control functions
    def rotate(self, motor, velocity):
        if not(0 <= motor < self.MOTORS):
            raise ValueError("Motor index out of range")

        self.__connection.rotate(motor, velocity)

    def stop(self, motor):
        if not(0 <= motor < self.MOTORS):
            raise ValueError("Motor index out of range")

        self.__connection.stop(motor)

    def moveTo(self, motor, position, velocity=None):
        if not(0 <= motor < self.MOTORS):
            raise ValueError("Motor index out of range")

        if velocity:
            self.setMaxVelocity(motor, velocity)

        self.__connection.move(0, motor, position)

    def moveBy(self, motor, position, velocity=None):
        # The TMCL command MVP REL does not correctly work if the previous
        # motion was in velocity mode. The position used as offset for the
        # relative motion is the last target position, not the actual position.
        # Due to that we manually calculate the relative position and use the
        # moveTo function.
        position += self.getActualPosition(motor)

        self.moveTo(motor, position, velocity)

        return position

    # Current Control functions
    def setMotorRunCurrent(self, axis, current):
        self.setMaxCurrent(axis, current)

    def setMotorStandbyCurrent(self, axis, current):
        self.setAxisParameter(self.APs.StandbyCurrent, axis, current)

    def getMaxCurrent(self, axis):
        return self.getAxisParameter(self.APs.MaxCurrent, axis)

    def setMaxCurrent(self, axis, current):
        self.setAxisParameter(self.APs.MaxCurrent, axis, current)

    # StallGuard2 Functions
    def setStallguard2Filter(self, axis, enableFilter):
        self.setAxisParameter(self.APs.SG2FilterEnable, axis, enableFilter)

    def setStallguard2Threshold(self, axis, threshold):
        self.setAxisParameter(self.APs.SG2Threshold, axis, threshold)

    def setStopOnStallVelocity(self, axis, velocity):
        self.setAxisParameter(self.APs.SmartEnergyStallVelocity, axis, velocity)

    # Motion parameter functions
    def getTargetPosition(self, axis):
        return self.getAxisParameter(self.APs.TargetPosition, axis)

    def setTargetPosition(self, axis, position):
        self.setAxisParameter(self.APs.TargetPosition, axis, position)

    def getActualPosition(self, axis):
        return self.getAxisParameter(self.APs.ActualPosition, axis)

    def setActualPosition(self, axis, position):
        return self.setAxisParameter(self.APs.ActualPosition, axis, position)

    def getTargetVelocity(self, axis):
        return self.getAxisParameter(self.APs.TargetVelocity, axis)

    def setTargetVelocity(self, axis, velocity):
        self.setAxisParameter(self.APs.TargetVelocity, axis, velocity)

    def getActualVelocity(self, axis):
        return self.getAxisParameter(self.APs.ActualVelocity, axis)

    def getMaxVelocity(self, axis):
        return self.getAxisParameter(self.APs.MaxVelocity, axis)

    def setMaxVelocity(self, axis, velocity):
        self.setAxisParameter(self.APs.MaxVelocity, axis, velocity)

    def getMaxAcceleration(self, axis):
        return self.getAxisParameter(self.APs.MaxAcceleration, axis)

    def setMaxAcceleration(self, axis, acceleration):
        self.setAxisParameter(self.APs.MaxAcceleration, axis, acceleration)

    # Status functions
    def getStatusFlags(self, axis):
        return self.getAxisParameter(self.APs.DriverErrorFlags, axis)

    def getErrorFlags(self, axis):
        return self.getAxisParameter(self.APs.ExtendedErrorFlags, axis)

    def positionReached(self, axis):
        return self.getAxisParameter(self.APs.PositionReachedFlag, axis)

    # IO pin functions
    def analogInput(self, x):
        return self.__connection.analogInput(x)

    def digitalInput(self, x):
        return self.__connection.digitalInput(x)

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
    swapLimitSwitches              = 14
    A1                             = 15
    V1                             = 16
    MaxDeceleration                = 17
    D1                             = 18
    StartVelocity                  = 19
    StopVelocity                   = 20
    RampWaitTime                   = 21
    THIGH                          = 22
    min_DcStepSpeed                = 23
    rightLimitSwitchPolarity       = 24
    leftLimitSwitchPolarity        = 25
    softstop                       = 26
    HighSpeedChopperMode           = 27
    HighSpeedFullstepMode          = 28
    MeasuredSpeed                  = 29
    PowerDownRamp                  = 31
    dcStepTime                     = 32
    dcStepStallGuard               = 33
    relativePositioningOption      = 127
    MicrostepResolution            = 140
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
    disableShortCircuitProtection  = 177
    VSense                         = 179
    smartEnergyActualCurrent       = 180
    smartEnergyStallVelocity       = 181
    smartEnergyThresholdSpeed      = 182
    RandomTOffMode                 = 184
    ChopperSynchronization         = 185
    PWMThresholdSpeed              = 186
    PWMGrad                        = 187
    PWMAmplitude                   = 188
    PWMScale                       = 189
    PWMMode                        = 190
    PWMFrequency                   = 191
    PWMAutoscale                   = 192
    ReferenceSearchMode            = 193
    ReferenceSearchSpeed           = 194
    referenceSwitchSpeed           = 195
    referenceSwitchDistance        = 196
    lastReferenceSwitchPosition    = 197
    latchedActualPosition          = 198
    latchedEncoderPosition         = 199
    encoderMode                    = 201
    motorFullStepResolution        = 202
    FreewheelingMode               = 204
    LoadValue                      = 206
    extendedErrorFlags             = 207
    driverErrorFlags               = 208
    encoderPosition                = 209
    encoderResolution              = 210
    max_EncoderDeviation           = 212
    groupIndex                     = 213
    PowerDownDelay                 = 214
    reverseShaft                   = 251
    CurrentStepping                = 0

class _GPs():
    timer_0                        = 0
    timer_1                        = 1
    timer_2                        = 2
    stopLeft_0                     = 27
    stopRight_0                    = 28
    stopLeft_1                     = 29
    stopRight_1                    = 30
    stopLeft_2                     = 31
    stopRight_2                    = 32
    stopLeft_3                     = 33
    stopRight_3                    = 34
    stopLeft_4                     = 35
    stopRight_4                    = 36
    stopLeft_5                     = 37
    stopRight_5                    = 38
    input_0                        = 39
    input_1                        = 40
    input_2                        = 41
    input_3                        = 42
    serialBaudRate                 = 65
    serialAddress                  = 66
    serialHeartbeat                = 68
    CANBitrate                     = 69
    CANSendId                      = 70
    CANReceiveId                   = 71
    telegrmPauseTime               = 75
    serialHostAddress              = 76
    autoStartMode                  = 77
    protectionMode                 = 81
    CANHeartbeat                   = 82
    CANSecondaryAddress            = 83
    StoreCoordinatesIn_EEPROM      = 84
    doNotRestoreUserVariables      = 85
    serialSecondaryAddress         = 87
    applicationStatus              = 128
    downloadMode                   = 129
    programCounter                 = 130
    lastTmclError                  = 131
    tickTimer                      = 132
    randomNumber                   = 133