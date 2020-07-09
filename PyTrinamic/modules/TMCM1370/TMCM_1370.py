'''
Created on 08.07.2020

@author: JM
'''

class TMCM_1370():
    def __init__(self, connection):
        self.connection = connection

        self.GPs   = _GPs
        self.APs   = _APs
        self.ENUMs = _ENUMs

        self.MOTORS = 1
        self.__default_motor = 0

    def showChipInfo(self):
        ("The PD42-x-1370 is a stepper motor driver, made up of the TMCM-1370 module and a 42mm flange motor. Voltage supply: 24V");

    # Axis parameter access
    def getAxisParameter(self, apType, signed=False):
        return self.connection.axisParameter(apType, self.__default_motor, signed=signed)

    def setAxisParameter(self, apType, value):
        self.connection.setAxisParameter(apType, self.__default_motor, value)

    # Global parameter access
    def getGlobalParameter(self, gpType, bank):
        return self.connection.globalParameter(gpType, bank)

    def setGlobalParameter(self, gpType, bank, value):
        self.connection.setGlobalParameter(gpType, bank, value)

    # Motion Control functions
    def rotate(self, velocity):
        self.connection.rotate(0, velocity)

    def stop(self):
        self.rotate(0)

    def moveTo(self, position, velocity=None):
        if velocity:
            self.setMaxVelocity(velocity)

        self.connection.move(0, 0, position)
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
        self.setAxisParameter(self.APs.SG2FilterEnable, enableFilter)

    def setStallguard2Threshold(self, threshold):
        self.setAxisParameter(self.APs.SG2Threshold, threshold)

    def setStopOnStallVelocity(self, velocity):
        self.setAxisParameter(self.APs.SmartEnergyStallVelocity, velocity)

    # Motion parameter functions
    def getTargetPosition(self):
        return self.getAxisParameter(self.APs.TargetPosition, signed=True)

    def setTargetPosition(self, position):
        self.setAxisParameter(self.APs.TargetPosition, position)

    def getActualPosition(self):
        return self.getAxisParameter(self.APs.ActualPosition, signed=True)

    def setActualPosition(self, position):
        return self.setAxisParameter(self.APs.ActualPosition, position)

    def getTargetVelocity(self):
        return self.getAxisParameter(self.APs.TargetVelocity, signed=True)

    def setTargetVelocity(self, velocity):
        self.setAxisParameter(self.APs.TargetVelocity, velocity)

    def getActualVelocity(self):
        return self.getAxisParameter(self.APs.ActualVelocity, signed=True)

    def getMaxVelocity(self):
        return self.getAxisParameter(self.APs.MaxVelocity)

    def setMaxVelocity(self, velocity):
        self.setAxisParameter(self.APs.MaxVelocity, velocity)

    def getMaxAcceleration(self):
        return self.getAxisParameter(self.APs.MaxAcceleration)

    def setMaxAcceleration(self, acceleration):
        self.setAxisParameter(self.APs.MaxAcceleration, acceleration)

    # Status functions
    def getStatusFlags(self):
        return self.getAxisParameter(self.APs.DrvStatusFlags)

    def getErrorFlags(self):
        return self.getAxisParameter(self.APs.ExtendedErrorFlags)

    def positionReached(self):
        return self.getAxisParameter(self.APs.PositionReachedFlag)

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
    HomeSwitch                     = 9
    RightEndstop                   = 10
    LeftEndstop                    = 11
    RightLimitSwitchEnablePolarity = 12
    LeftLimitSwitchEnablePolarity  = 13
    StartVelocity                  = 15
    StartAcceleration              = 16
    MaxDeceleration                = 17
    breakVelocity                  = 18
    FinalDeceleration              = 19
    StopVelocity                   = 20
    StopDeceleration               = 21
    BOW1                           = 22
    BOW2                           = 23
    BOW3                           = 24
    BOW4                           = 25
    VirtualStopLeft                = 26
    VirtualStopRight               = 27
    VirtualStopEnable              = 28
    VirtualStopMode                = 29
    SwapLimitSwitches              = 33
    LimitSwitchSoftStop            = 34
    BOW_SCALER                     = 35
    PositionCompareValue           = 40
    PositionComparePulseLength     = 41
    PositionCompareOutput          = 42
    PositionCompareRepeat          = 43
    torque                         = 50
    CLGammaVMin                    = 108
    CLGammaVMax                    = 109
    CLMaxGamma                     = 110
    CLBeta                         = 111
    CLOffset                       = 112
    CLCurrentMin                   = 113
    CLCurrentMax                   = 114
    CLCorrectionVelocityP          = 115
    CLCorrectionVelocityI          = 116
    CLCorrectionVelIClip           = 117
    CLCorrectionVelDVClock         = 118
    CLCorrectionVelDVClip          = 119
    CLUpscaleDelay                 = 120
    CLDownscaleDelay               = 121
    ActualScalerValue              = 123
    CLCorrectionPositionP          = 124
    CLMaxCorrectionTolerance       = 125
    CLStartUp                      = 126
    RelativePositioningOption      = 127
    ClosedLoop                     = 129
    InitMode                       = 130
    MeasuredSpeed                  = 131
    CurrentMeasuredSpeed           = 132
    CL_init_flag                   = 133
    EncoderDeviation               = 134
    enc_vmean_wait                 = 136
    enc_vmean_filter               = 137
    enc_vmean_int                  = 138
    ChopperBlankTime               = 162
    ConstantTOffMode               = 163
    ChopperHysteresisDecrement     = 164
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
    ReferenceSwitchSpeed           = 195
    ReferenceSwitchDistance        = 196
    LastReferenceSwitchPosition    = 196
    BoostCurrent                   = 200
    FullstepResolution             = 202
    LoadValue                      = 206
    ExtendedErrorFlags             = 207
    DriverErrorFlags               = 208
    EncoderPosition                = 209
    EncoderResolution              = 210
    StopOnErrorMode                = 211
    max_positionEncoderDeviation   = 212
    max_velocityEncoderDeviation   = 213
    SettingDelay                   = 214
    AbsoluteEncoder                = 215
    EncoderErrorBits               = 219
    AllStatusBits                  = 250
    ReverseShaft                   = 251
    ClearAlarmOutputs              = 252
    CurrentStepping                = 0


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
