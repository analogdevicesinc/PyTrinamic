'''
Created on 21.05.2019

@author: LH
'''

class TMCM_1161():

    # Axis Parameters
    AP_TargetPosition               = 0
    AP_ActualPosition               = 1
    AP_TargetVelocity               = 2
    AP_ActualVelocity               = 3
    AP_MaxVelocity                  = 4
    AP_MaxAcceleration              = 5
    AP_MaxCurrent                   = 6
    AP_StandbyCurrent               = 7
    AP_PositionReachedFlag          = 8
    AP_ReferenceSwitchStatus        = 9
    AP_RightLimitSwitchStatus       = 10
    AP_LeftLimitSwitchStatus        = 11
    AP_RightLimitSwitchDisable      = 12
    AP_LeftLimitSwitchDisable       = 13
    AP_MinimumSpeed                 = 130
    AP_ActualAcceleration           = 135
    AP_RampMode                     = 138
    AP_MicrostepResolution          = 140
    AP_RefSwitchTolerance           = 141
    AP_SoftStopFlag                 = 149
    AP_EndSwitchPowerDown           = 150
    AP_RampDivisor                  = 153
    AP_PulseDivisor                 = 154
    AP_Intpol                       = 160
    AP_DoubleEdgeSteps              = 161
    AP_ChopperBlankTime             = 162
    AP_ConstantTOffMode             = 163
    AP_DisableFastDecayComparator   = 164
    AP_ChopperHysteresisEnd         = 165
    AP_ChopperHysteresisStart       = 166
    AP_TOff                         = 167
    AP_SEIMIN                       = 168
    AP_SECDS                        = 169
    AP_SmartEnergyHysteresis        = 170
    AP_SECUS                        = 171
    AP_SmartEnergyHysteresisStart   = 172
    AP_SG2FilterEnable              = 173
    AP_SG2Threshold                 = 174
    AP_SlopeControlHighSide         = 175
    AP_SlopeControlLowSide          = 176
    AP_ShortToGroundProtection      = 177
    AP_ShortDetectionTime           = 178
    AP_VSense                       = 179
    AP_SmartEnergyActualCurrent     = 180
    AP_SmartEnergyStallVelocity     = 181
    AP_SmartEnergyThresholdSpeed    = 182
    AP_SmartEnergySlowRunCurrent    = 183
    AP_RandomTOffMode               = 184
    AP_ReferenceSearchMode          = 193
    AP_ReferenceSearchSpeed         = 194
    AP_ReferenceSwitchSpeed         = 195
    AP_ReferenceSwitchDistance      = 196
    AP_LastReferenceSwitchPosition  = 197
    AP_BoostCurrent                 = 200
    AP_FreewheelingDelay            = 204
    AP_LoadValue                    = 206
    AP_ExtendedErrorFlags           = 207
    AP_DrvStatusFlags               = 208
    AP_EncoderPosition              = 209
    AP_EncoderResolution            = 210
    AP_MaxEncoderDeviation          = 212
    AP_PowerDownDelay               = 214
    AP_AbsoluteResolverValue        = 215
    AP_StepDirectionMode            = 254

    # Global Parameters
    GP_BaudRate                     = 65
    GP_SerialAddress                = 66
    GP_ASCIIMode                    = 67
    GP_SerialHeartbeat              = 68
    GP_TelegramPauseTime            = 75
    GP_SerialHostAddress            = 76
    GP_AutoStartMode                = 77
    GP_EndSwitchPolarity            = 79
    GP_TMCLCodeProtection           = 81
    GP_CoordinateStorage            = 84
    GP_DoNotRestoreUserVariables    = 85
    GP_SerialSecondaryAddress       = 87
    GP_ReverseShaft                 = 90

    GP_TMCLApplicationStatus        = 128
    GP_DownloadMode                 = 129
    GP_TMCLProgramCounter           = 130
    GP_TMCLLastError                = 131
    GP_TMCLTickTimer                = 132
    GP_RandomNumber                 = 133
    GP_SuppressReply                = 255

    FLAG_POSITION_END = 0x00004000

    def __init__(self, connection):
        self.connection = connection

        self.MOTORS = 1
        self.__default_motor = 0

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
        self.setRampMode(2)

        self.setAxisParameter(self.AP_TargetVelocity, velocity)

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
        self.setAxisParameter(self.AP_StandbyCurrent, current)

    def getMaxCurrent(self):
        return self.getAxisParameter(self.AP_MaxCurrent)

    def setMaxCurrent(self, current):
        self.setAxisParameter(self.AP_MaxCurrent, current)

    # StallGuard2 Functions
    def setStallguard2Filter(self, enableFilter):
        self.setAxisParameter(self.AP_SG2FilterEnable, enableFilter)

    def setStallguard2Threshold(self, threshold):
        self.setAxisParameter(self.AP_SG2Threshold, threshold)

    def setStopOnStallVelocity(self, velocity):
        self.setAxisParameter(self.AP_SmartEnergyStallVelocity, velocity)

    # Motion parameter functions
    def getTargetPosition(self):
        return self.getAxisParameter(self.AP_TargetPosition)

    def setTargetPosition(self, position):
        self.setAxisParameter(self.AP_TargetPosition, position)

    def getActualPosition(self):
        return self.getAxisParameter(self.AP_ActualPosition)

    def setActualPosition(self, position):
        return self.setAxisParameter(self.AP_ActualPosition, position)

    def getTargetVelocity(self):
        return self.getAxisParameter(self.AP_TargetVelocity)

    def setTargetVelocity(self, velocity):
        self.setAxisParameter(self.AP_TargetVelocity, velocity)

    def getActualVelocity(self):
        return self.getAxisParameter(self.AP_ActualVelocity)

    def getMaxVelocity(self):
        return self.getAxisParameter(self.AP_MaxVelocity)

    def setMaxVelocity(self, velocity):
        self.setAxisParameter(self.AP_MaxVelocity, velocity)

    def getMaxAcceleration(self):
        return self.getAxisParameter(self.AP_MaxAcceleration)

    def setMaxAcceleration(self, acceleration):
        self.setAxisParameter(self.AP_MaxAcceleration, acceleration)

    def getRampMode(self):
        return self.getAxisParameter(self.AP_RampMode)

    def setRampMode(self, mode):
        return self.setAxisParameter(self.AP_RampMode, mode)

    # Status functions
    def getStatusFlags(self):
        return self.getAxisParameter(self.AP_DrvStatusFlags)

    def getErrorFlags(self):
        return self.getAxisParameter(self.AP_ExtendedErrorFlags)

    def positionReached(self):
        return self.getAxisParameter(self.AP_PositionReachedFlag)

    # IO pin functions
    def analogInput(self, x):
        return self.connection.analogInput(x)

    def digitalInput(self, x):
        return self.connection.digitalInput(x)

