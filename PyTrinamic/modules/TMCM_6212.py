'''
Created on 21.05.2019

@author: LH
'''

class TMCM_6212():

    # Axis Parameters
    AP_TargetPosition                 = 0
    AP_ActualPosition                 = 1
    AP_TargetVelocity                 = 2
    AP_ActualVelocity                 = 3
    AP_MaxVelocity                    = 4
    AP_MaxAcceleration                = 5
    AP_MaxCurrent                     = 6
    AP_StandbyCurrent                 = 7
    AP_PositionReachedFlag            = 8
    AP_ReferenceSwitchStatus          = 9
    AP_RightEndstop                   = 10
    AP_LeftEndstop                    = 11
    AP_RightLimitSwitchDisable        = 12
    AP_LeftLimitSwitchDisable         = 13
    AP_SwapLimitSwitches              = 14
    AP_A1                             = 15
    AP_V1                             = 16
    AP_MaxDeceleration                = 17
    AP_D1                             = 18
    AP_StartVelocity                  = 19
    AP_StopVelocity                   = 20
    AP_RampWaitTime                   = 21
    AP_THIGH                          = 22
    AP_MinDcStepSpeed                 = 23
    AP_RightLimitSwitchPolarity       = 24
    AP_LeftLimitSwitchPolarity        = 25
    AP_Softstop                       = 26
    AP_HighSpeedChopperMode           = 27
    AP_HighSpeedFullstepMode          = 28
    AP_MeasuredSpeed                  = 29
    AP_PowerDownRamp                  = 31
    AP_DcStepTime                     = 32
    AP_DcStepStallGuard               = 33
    AP_RelativePositioningOption      = 127
    AP_MicrostepResolution            = 140
    AP_ChopperBlankTime               = 162
    AP_ConstantTOffMode               = 163
    AP_DisableFastDecayComparator     = 164
    AP_ChopperHysteresisEnd           = 165
    AP_ChopperHysteresisStart         = 166
    AP_TOff                           = 167
    AP_SEIMIN                         = 168
    AP_SECDS                          = 169
    AP_SmartEnergyHysteresis          = 170
    AP_SECUS                          = 171
    AP_SmartEnergyHysteresisStart     = 172
    AP_SG2FilterEnable                = 173
    AP_SG2Threshold                   = 174
    AP_DisableShortCircuitProtection  = 177
    AP_VSense                         = 179
    AP_SmartEnergyActualCurrent       = 180
    AP_SmartEnergyStallVelocity       = 181
    AP_SmartEnergyThresholdSpeed      = 182
    AP_RandomTOffMode                 = 184
    AP_ChopperSynchronization         = 185
    AP_PWMThresholdSpeed              = 186
    AP_PWMGrad                        = 187
    AP_PWMAmplitude                   = 188
    AP_PWMScale                       = 189
    AP_PWMMode                        = 190
    AP_PWMFrequency                   = 191
    AP_PWMAutoscale                   = 192
    AP_ReferenceSearchMode            = 193
    AP_ReferenceSearchSpeed           = 194
    AP_ReferenceSwitchSpeed           = 195
    AP_ReferenceSwitchDistance        = 196
    AP_LastReferenceSwitchPosition    = 197
    AP_EncoderMode                    = 201
    AP_MotorFullStepResolution        = 202
    AP_FreewheelingMode               = 204
    AP_LoadValue                      = 206
    AP_ExtendedErrorFlags             = 207
    AP_DriverErrorFlags               = 208
    AP_EncoderPosition                = 209
    AP_EncoderResolution              = 210
    AP_MaxEncoderDeviation            = 212
    AP_GroupIndex                     = 213
    AP_PowerDownDelay                 = 214
    AP_ReverseShaft                   = 251

    # Global Parameters
    GP_BaudRate                     = 65
    GP_SerialAddress                = 66
    GP_SerialHeartbeat              = 68
    GP_CANBitRate                   = 69
    GP_CANReplyID                   = 70
    GP_CANID                        = 71
    GP_TelegramPauseTime            = 75
    GP_SerialHostAddress            = 76
    GP_AutoStartMode                = 77
    GP_TMCLCodeProtection           = 81
    GP_CANHeartbeat                 = 82
    GP_CANSecondaryAddress          = 83
    GP_CoordinateStorage            = 84
    GP_DoNotRestoreUserVariables    = 85
    GP_SerialSecondaryAddress       = 87

    GP_TMCLApplicationStatus        = 128
    GP_DownloadMode                 = 129
    GP_TMCLProgramCounter           = 130
    GP_TMCLLastError                = 131
    GP_TMCLTickTimer                = 132
    GP_RandomNumber                 = 133

    def __init__(self, connection):
        self.__connection = connection

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
        self.setAxisParameter(self.AP_StandbyCurrent, axis, current)

    def getMaxCurrent(self, axis):
        return self.getAxisParameter(self.AP_MaxCurrent, axis)

    def setMaxCurrent(self, axis, current):
        self.setAxisParameter(self.AP_MaxCurrent, axis, current)

    # StallGuard2 Functions
    def setStallguard2Filter(self, axis, enableFilter):
        self.setAxisParameter(self.AP_SG2FilterEnable, axis, enableFilter)

    def setStallguard2Threshold(self, axis, threshold):
        self.setAxisParameter(self.AP_SG2Threshold, axis, threshold)

    def setStopOnStallVelocity(self, axis, velocity):
        self.setAxisParameter(self.AP_SmartEnergyStallVelocity, axis, velocity)

    # Motion parameter functions
    def getTargetPosition(self, axis):
        return self.getAxisParameter(self.AP_TargetPosition, axis)

    def setTargetPosition(self, axis, position):
        self.setAxisParameter(self.AP_TargetPosition, axis, position)

    def getActualPosition(self, axis):
        return self.getAxisParameter(self.AP_ActualPosition, axis)

    def setActualPosition(self, axis, position):
        return self.setAxisParameter(self.AP_ActualPosition, axis, position)

    def getTargetVelocity(self, axis):
        return self.getAxisParameter(self.AP_TargetVelocity, axis)

    def setTargetVelocity(self, axis, velocity):
        self.setAxisParameter(self.AP_TargetVelocity, axis, velocity)

    def getActualVelocity(self, axis):
        return self.getAxisParameter(self.AP_ActualVelocity, axis)

    def getMaxVelocity(self, axis):
        return self.getAxisParameter(self.AP_MaxVelocity, axis)

    def setMaxVelocity(self, axis, velocity):
        self.setAxisParameter(self.AP_MaxVelocity, axis, velocity)

    def getMaxAcceleration(self, axis):
        return self.getAxisParameter(self.AP_MaxAcceleration, axis)

    def setMaxAcceleration(self, axis, acceleration):
        self.setAxisParameter(self.AP_MaxAcceleration, axis, acceleration)

    # Status functions
    def getStatusFlags(self, axis):
        return self.getAxisParameter(self.AP_DriverErrorFlags, axis)

    def getErrorFlags(self, axis):
        return self.getAxisParameter(self.AP_ExtendedErrorFlags, axis)

    def positionReached(self, axis):
        return self.getAxisParameter(self.AP_PositionReachedFlag, axis)

    # IO pin functions
    def analogInput(self, x):
        return self.__connection.analogInput(x)

    def digitalInput(self, x):
        return self.__connection.digitalInput(x)
