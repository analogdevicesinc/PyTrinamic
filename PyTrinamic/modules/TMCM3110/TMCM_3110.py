'''
Created on 05.06.2020

@author: JM
'''

class TMCM_3110():
    MOTORS = 3

    def __init__(self, connection):
        self.connection = connection

        #self.GPs   = _GPs
        self.APs   = _APs
        #self.ENUMs = _ENUMs

    @staticmethod
    def getEdsFile():
        return __file__.replace("TMCM_3110.py", "TMCM_3110_V.320.eds")

    def showChipInfo(self):
        ("The TMCM-3110 is a 3-Axis Stepper Controller / Driver. Voltage supply: 12 - 48V");

    # Axis parameter access
    def getAxisParameter(self, apType, motor):
        return self.connection.axisParameter(apType, motor)

    def setAxisParameter(self, apType, motor, value):
        self.connection.setAxisParameter(apType, motor, value)

    # Global parameter access
    def getGlobalParameter(self, gpType, bank):
        return self.connection.globalParameter(gpType, bank)

    def setGlobalParameter(self, gpType, bank, value):
        self.connection.setGlobalParameter(gpType, bank, value)

    # Motion Control functions
    def rotate(self, motor, velocity):
        self.setRampMode(motor, 2)

        self.setAxisParameter(self.APs.TargetVelocity, motor, velocity)

    def stop(self, motor):
        self.rotate(motor, 0)

    def moveTo(self, motor, position, velocity=None):
        if velocity:
            self.setMaxVelocity(motor, velocity)

        self.setTargetPosition(motor, position)

        self.setRampMode(motor, 0)

    def moveBy(self, motor, difference, velocity=None):
        position = difference + self.getActualPosition(motor)

        self.moveTo(motor, position, velocity)

        return position

    def startReferenceSearch(self, motor, mode=None):
        if mode:
            self.setReferenceSearchMode(motor, mode)
        self.connection.referenceSearch(1, motor)

    # Current control functions
    def setMotorRunCurrent(self, motor, current):
        self.setMaxCurrent(motor, current)

    def setMotorStandbyCurrent(self, motor, current):
        self.setAxisParameter(self.APs.StandbyCurrent, motor, current)

    def getMaxCurrent(self, motor):
        return self.getAxisParameter(self.APs.MaxCurrent, motor)

    def setMaxCurrent(self, motor, current):
        self.setAxisParameter(self.APs.MaxCurrent, motor, current)

    # StallGuard2 Functions
    def setStallguard2Filter(self, motor, enableFilter):
        self.setAxisParameter(self.APs.SG2FilterEnable, motor, enableFilter)

    def setStallguard2Threshold(self, motor, threshold):
        self.setAxisParameter(self.APs.SG2Threshold, motor, threshold)

    def setStopOnStallVelocity(self, motor, velocity):
        self.setAxisParameter(self.APs.smartEnergyStallVelocity, motor, velocity)

    # Motion parameter functions
    def getTargetPosition(self, motor):
        return self.getAxisParameter(self.APs.TargetPosition, motor)

    def setTargetPosition(self, motor, position):
        self.setAxisParameter(self.APs.TargetPosition, motor, position)

    def getActualPosition(self, motor):
        return self.getAxisParameter(self.APs.ActualPosition, motor)

    def setActualPosition(self, motor, position):
        return self.setAxisParameter(self.APs.ActualPosition, motor, position)

    def getTargetVelocity(self, motor):
        return self.getAxisParameter(self.APs.TargetVelocity, motor)

    def setTargetVelocity(self, velocity, motor):
        self.setAxisParameter(self.APs.TargetVelocity, motor, velocity)

    def getActualVelocity(self, motor):
        return self.getAxisParameter(self.APs.ActualVelocity, motor)

    def getMaxVelocity(self, motor):
        return self.getAxisParameter(self.APs.MaxVelocity, motor)

    def setMaxVelocity(self, motor, velocity):
        self.setAxisParameter(self.APs.MaxVelocity, motor, velocity)

    def getMaxAcceleration(self, motor):
        return self.getAxisParameter(self.APs.MaxAcceleration, motor)

    def setMaxAcceleration(self, motor, acceleration):
        self.setAxisParameter(self.APs.MaxAcceleration, motor, acceleration)

    def getRampMode(self, motor):
        return self.getAxisParameter(self.APs.RampMode, motor)

    def setRampMode(self, motor, mode):
        return self.setAxisParameter(self.APs.RampMode, motor, mode)

    def setReferenceSearchMode(self, motor, mode):
        return self.setAxisParameter(self.APs.ReferenceSearchMode, motor, mode)

    def setReferenceSearchSpeed(self, motor, speed):
        return self.setAxisParameter(self.APs.ReferenceSearchSpeed, motor, speed)

    def setReferenceSwitchSpeed(self, motor, speed):
        return self.setAxisParameter(self.APs.ReferenceSwitchSpeed, motor, speed)

    # Status functions
    def getStatusFlags(self, motor):
        return self.getAxisParameter(self.APs.DrvStatusFlags, motor)

    def getErrorFlags(self, motor):
        return self.getAxisParameter(self.APs.ExtendedErrorFlags, motor)

    def positionReached(self, motor):
        return self.getAxisParameter(self.APs.PositionReachedFlag, motor)

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
    ReferenceSwitchStatus          = 9
    RightEndstop                   = 10
    LeftEndstop                    = 11
    RightLimitSwitchDisable        = 12
    LeftLimitSwitchDisable         = 13
    MinimumSpeed                   = 130
    ActualAcceleration             = 135
    RampMode                       = 138
    MicrostepResolution            = 140
    ReferenceSwitchTolerance       = 141
    SoftStopFlag                   = 149
    EndSwitchPowerDown             = 150
    RampDivisor                    = 153
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
    SlopeControlHighSide           = 175
    SlopeControlLowSide            = 176
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
    LastReferenceSwitchPosition    = 197
    BoostCurrent                   = 200
    EncoderMode                    = 201
    FreewheelingDelay              = 204
    LoadValue                      = 206
    ExtendedErrorFlags             = 207
    DrvStatusFlags                 = 208
    EncoderPosition                = 209
    EncoderPrescaler               = 210
    MaxEncoderDeviation            = 212
    GroupIndex                     = 213
    PowerDownDelay                 = 214
    StepDirectionMode              = 254
