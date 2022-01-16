'''
Created on 05.06.2020

@author: JM
'''

from PyTrinamic.modules.tmcl_module import TMCLModule

class TMCM_3110(TMCLModule):
    MOTORS = 3

    class APs():
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

    @staticmethod
    def getEdsFile():
        return __file__.replace("TMCM_3110.py", "TMCM_3110_V.320.eds")

    def showChipInfo(self):
        print("The TMCM-3110 is a 3-Axis Stepper Controller / Driver. Voltage supply: 12 - 48V")

    # Motion Control functions
    def rotate(self, axis, velocity):
        self.setRampMode(axis, 2)

        self.setAxisParameter(self.APs.TargetVelocity, axis, velocity)

    def stop(self, axis):
        self.rotate(axis, 0)

    def moveTo(self, axis, position, velocity=None):
        if velocity:
            self.setMaxVelocity(axis, velocity)

        self.setTargetPosition(axis, position)

        self.setRampMode(axis, 0)

    def moveBy(self, axis, difference, velocity=None):
        position = difference + self.getActualPosition(axis)

        self.moveTo(axis, position, velocity)

        return position

    # Current control functions
    def setMotorRunCurrent(self, axis, current):
        self.setMaxCurrent(axis, current)

    def setMotorStandbyCurrent(self, axis, current):
        self.setAxisParameter(self.APs.StandbyCurrent, axis, current)

    def getMaxCurrent(self, axis):
        return self.axisParameter(self.APs.MaxCurrent, axis)

    def setMaxCurrent(self, axis, current):
        self.setAxisParameter(self.APs.MaxCurrent, axis, current)

    # StallGuard2 Functions
    def setStallguard2Filter(self, axis, enableFilter):
        self.setAxisParameter(self.APs.SG2FilterEnable, axis, enableFilter)

    def setStallguard2Threshold(self, axis, threshold):
        self.setAxisParameter(self.APs.SG2Threshold, axis, threshold)

    def setStopOnStallVelocity(self, axis, velocity):
        self.setAxisParameter(self.APs.smartEnergyStallVelocity, axis, velocity)

    # Motion parameter functions
    def getTargetPosition(self, axis):
        return self.axisParameter(self.APs.TargetPosition, axis)

    def setTargetPosition(self, axis, position):
        self.setAxisParameter(self.APs.TargetPosition, axis, position)

    def getActualPosition(self, axis):
        return self.axisParameter(self.APs.ActualPosition, axis)

    def setActualPosition(self, axis, position):
        return self.setAxisParameter(self.APs.ActualPosition, axis, position)

    def getTargetVelocity(self, axis):
        return self.axisParameter(self.APs.TargetVelocity, axis)

    def setTargetVelocity(self, velocity, axis):
        self.setAxisParameter(self.APs.TargetVelocity, axis, velocity)

    def getActualVelocity(self, axis):
        return self.axisParameter(self.APs.ActualVelocity, axis)

    def getMaxVelocity(self, axis):
        return self.axisParameter(self.APs.MaxVelocity, axis)

    def setMaxVelocity(self, axis, velocity):
        self.setAxisParameter(self.APs.MaxVelocity, axis, velocity)

    def getMaxAcceleration(self, axis):
        return self.axisParameter(self.APs.MaxAcceleration, axis)

    def setMaxAcceleration(self, axis, acceleration):
        self.setAxisParameter(self.APs.MaxAcceleration, axis, acceleration)

    def getRampMode(self, axis):
        return self.axisParameter(self.APs.RampMode, axis)

    def setRampMode(self, axis, mode):
        return self.setAxisParameter(self.APs.RampMode, axis, mode)

    # Status functions
    def getStatusFlags(self, axis):
        return self.axisParameter(self.APs.DrvStatusFlags, axis)

    def getErrorFlags(self, axis):
        return self.axisParameter(self.APs.ExtendedErrorFlags, axis)

    def positionReached(self, axis):
        return self.axisParameter(self.APs.PositionReachedFlag, axis)

    # IO pin functions
    def analogInput(self, x):
        return self.connection.analogInput(x, self.module_id)

    def digitalInput(self, x):
        return self.connection.digitalInput(x, self.module_id)
