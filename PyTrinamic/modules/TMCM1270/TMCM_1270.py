'''
Created on 03.12.2019

@author: JM
'''

class TMCM_1270():
    def __init__(self, connection):
        self.connection = connection

        self.GPs   = _GPs
        self.APs   = _APs
        self.ENUMs = _ENUMs

        self.MOTORS = 1
        self.__default_motor = 0

    @staticmethod
    def getEdsFile():
        return __file__.replace("TMCM_1270.py", "TMCM_1270_V3.22.eds")

    def showChipInfo(self):
        ("The TMCM-1270 is a smart stepper motor driver module. The module is controlled via a CAN bus interface. Voltage supply: 6 - 24V");

    # Axis parameter access
    def getAxisParameter(self, apType):
        return self.connection.axisParameter(apType, self.__default_motor)

    def setAxisParameter(self, apType, value):
        self.connection.setAxisParameter(apType, self.__default_motor, value)

    # Global parameter access
    def getGlobalParameter(self, gpType, bank):
        return self.connection.globalParameter(gpType, bank)

    def setGlobalParameter(self, gpType, bank, value):
        self.connection.setGlobalParameter(gpType, bank, value)

    # Motion Control functions
    def rotate(self, velocity):
        self.setTargetVelocity(velocity)

    def stop(self):
        self.rotate(0)

    def moveTo(self, position, velocity=None):
        if velocity:
            self.setMaxVelocity(velocity)

        self.connection.move(0, self.__default_motor, position)
        self.setTargetPosition(position)

    def moveBy(self, difference, velocity=None):
        position = difference + self.getActualPosition()

        self.moveTo(position, velocity)

        return position

    # Current control functions
    def setMotorRunCurrent(self, current):
        self.setMaxCurrent(current)

    def setMotorStandbyCurrent(self, current):
        self.setAxisParameter(self.APs.StandbyCurrent, current)

    def getMaxCurrent(self):
        return self.getAxisParameter(self.APs.MaxCurrent)

    def setMaxCurrent(self, current):
        self.setAxisParameter(self.APs.MaxCurrent, current)

    # StallGuard2 Functions
    def setStallguard2Filter(self, enableFilter):
        self.setAxisParameter(self.APs.StallGuard2FilterEnable, enableFilter)

    def setStallguard2Threshold(self, threshold):
        self.setAxisParameter(self.APs.StallGuard2Threshold, threshold)

    def setStopOnStallVelocity(self, velocity):
        self.setAxisParameter(self.APs.StopOnStall, velocity)

    # Motion parameter functions
    def getTargetPosition(self):
        return self.getAxisParameter(self.APs.TargetPosition)

    def setTargetPosition(self, position):
        self.setAxisParameter(self.APs.TargetPosition, position)

    def getActualPosition(self):
        return self.getAxisParameter(self.APs.ActualPosition)

    def setActualPosition(self, position):
        return self.setAxisParameter(self.APs.ActualPosition, position)

    def getTargetVelocity(self):
        return self.getAxisParameter(self.APs.TargetVelocity)

    def setTargetVelocity(self, velocity):
        self.setAxisParameter(self.APs.TargetVelocity, velocity)

    def getActualVelocity(self):
        return self.getAxisParameter(self.APs.ActualVelocity)

    def getMaxVelocity(self):
        return self.getAxisParameter(self.APs.MaxVelocity)

    def setMaxVelocity(self, velocity):
        self.setAxisParameter(self.APs.MaxVelocity, velocity)

    def getMaxAcceleration(self):
        return self.getAxisParameter(self.APs.MaxAcceleration)

    def setMaxAcceleration(self, acceleration):
        self.setAxisParameter(self.APs.MaxAcceleration, acceleration)

    def getRampMode(self):
        return self.getAxisParameter(self.APs.RampMode)

    def setRampMode(self, mode):
        return self.setAxisParameter(self.APs.RampMode, mode)

    # Status functions
    def getStatusFlags(self):
        return self.getAxisParameter(self.APs.TMC262ErrorFlags)

    def getErrorFlags(self):
        return self.getAxisParameter(self.APs.ExtendedErrorFlags)

    def positionReached(self):
        return self.getAxisParameter(self.APs.PositionReachedFlag)

    # IO pin functions
    def analogInput(self, x):
        return self.connection.analogInput(x)

    def digitalInput(self, x):
        return self.connection.digitalInput(x)

    def showMotionConfiguration(self):
        print("Motion configuration:")
        print("\tMax velocity: " + str(self.getMaxVelocity()))
        print("\tAcceleration: " + str(self.getMaxAcceleration()))
        print("\tRamp mode: " + ("position" if (self.getRampMode()==0) else "velocity"))

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
    HomeSwitch                     = 9
    RightEndstop                   = 10
    LeftEndstop                    = 11
    AutomaticRightStop             = 12
    AutomaticLeftStop              = 13
    swapSwitchInputs               = 14
    A1                             = 15
    V1                             = 16
    MaxDeceleration                = 17
    D1                             = 18
    StartVelocity                  = 19
    StopVelocity                   = 20
    RampWaitTime                   = 21
    THIGH                          = 22
    VDCMIN                         = 23
    rightSwitchPolarity            = 24
    leftSwitchPolarity             = 25
    softstop                       = 26
    HighSpeedChopperMode           = 27
    HighSpeedFullstepMode          = 28
    MeasuredSpeed                  = 29
    PowerDownRamp                  = 31
    RelativePositioningOptionCode  = 127
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
    ShortToGroundProtection        = 177
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
    pwmMode                        = 190
    PWMFrequency                   = 191
    PWMAutoscale                   = 192
    ReferenceSearchMode            = 193
    ReferenceSearchSpeed           = 194
    RefSwitchSpeed                 = 195
    RightLimitSwitchPosition       = 196
    LastReferencePosition          = 197
    encoderMode                    = 201
    MotorFullStepResolution        = 202
    pwmSymmetric                   = 203
    FreewheelingMode               = 204
    LoadValue                      = 206
    extendedErrorFlags             = 207
    DrvStatusFlags                 = 208
    EncoderPosition                = 209
    EncoderResolution              = 210
    max_EncoderDeviation           = 212
    PowerDownDelay                 = 214
    UnitMode                       = 255

class _ENUMs():
    pass

class _GPs():

    CANBitrate                    = 69
    CANSendId                     = 70
    CANReceiveId                  = 71
    CANSecondaryId                = 72
    autoStartMode                 = 77
    protectionMode                = 81
    eepromCoordinateStore         = 84
    zeroUserVariables             = 85
    applicationStatus             = 128
    programCounter                = 130
    lastTmclError                 = 131
    tickTimer                     = 132
    randomNumber                  = 133