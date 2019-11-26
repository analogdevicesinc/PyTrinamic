'''
Created on 18.11.2019

@author: JM
'''

class TMCM_1276(object):

    # Axis Parameters
    AP_TargetPosition = 0
    AP_ActualPosition = 1
    AP_TargetVelocity = 2
    AP_ActualVelocity = 3
    AP_MaxVelocity = 4
    AP_MaxAcceleration = 5
    AP_MaxCurrent = 6
    AP_StandbyCurrent = 7
    AP_PositionReachedFlag = 8
    AP_HomeSwitch = 9
    AP_RightEndstop = 10
    AP_LeftEndstop = 11
    AP_AutomaticRightStop = 12
    AP_AutomaticLeftStop = 13
    AP_swap_switch_inputs = 14
    AP_A1 = 15
    AP_V1 = 16
    AP_MaxDeceleration = 17
    AP_D1 = 18
    AP_StartVelocity = 19
    AP_StopVelocity = 20
    AP_RampWaitTime = 21
    AP_THIGH = 22
    AP_VDCMIN = 23
    AP_right_switch_polarity = 24
    AP_left_switch_polarity = 25
    AP_softstop = 26
    AP_HighSpeedChopperMode = 27
    AP_HighSpeedFullstepMode = 28
    AP_MeasuredSpeed = 29
    AP_PowerDownRamp = 31
    AP_RelativePositioningOptionCode = 127
    AP_MicrostepResolution = 140
    AP_ChopperBlankTime = 162
    AP_ConstantTOffMode = 163
    AP_DisableFastDecayComparator = 164
    AP_ChopperHysteresisEnd = 165
    AP_ChopperHysteresisStart = 166
    AP_TOff = 167
    AP_SEIMIN = 168
    AP_SECDS = 169
    AP_smartEnergyHysteresis = 170
    AP_SECUS = 171
    AP_smartEnergyHysteresisStart = 172
    AP_SG2FilterEnable = 173
    AP_SG2Threshold = 174
    AP_ShortToGroundProtection = 177
    AP_smartEnergyActualCurrent = 180
    AP_smartEnergyStallVelocity = 181
    AP_smartEnergyThresholdSpeed = 182
    AP_RandomTOffMode = 184
    AP_ChopperSynchronization = 185
    AP_PWMThresholdSpeed = 186
    AP_PWMGrad = 187
    AP_PWMAmplitude = 188
    AP_PWMScale = 189
    AP_pwm_mode = 190
    AP_PWMFrequency = 191
    AP_PWMAutoscale = 192
    AP_ReferenceSearchMode = 193
    AP_ReferenceSearchSpeed = 194
    AP_RefSwitchSpeed = 195
    AP_RightLimitSwitchPosition = 196
    AP_LastReferencePosition = 197
    AP_encoder_mode = 201
    AP_MotorFullStepResolution = 202
    AP_pwm_symmetric = 203
    AP_FreewheelingMode = 204
    AP_LoadValue = 206
    AP_extended_error_flags = 207
    AP_DrvStatusFlags = 208
    AP_EncoderPosition = 209
    AP_EncoderResolution = 210
    AP_max_encoder_deviation = 212
    AP_PowerDownDelay = 214
    AP_UnitMode = 255
    AP_CurrentStepping = 0


    # Global Parameters
    GP_CANBitRate                   = 69
    GP_CANReplyID                   = 70
    GP_CANID                        = 71
    GP_CANSecondaryID               = 72
    GP_AutoStartMode                = 77
    GP_TMCLCodeProtection           = 81
    GP_CoordinateStorage            = 84
    GP_DoNotRestoreUserVariables    = 85

    GP_TMCLApplicationStatus        = 128
    GP_TMCLProgramCounter           = 130
    GP_TMCLLastError                = 131
    GP_TMCLTickTimer                = 132
    GP_RandomNumber                 = 133
    GP_SuppressReply                = 255

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
        self.setAxisParameter(self.AP_StandbyCurrent, current)

    def getMaxCurrent(self):
        return self.getAxisParameter(self.AP_MaxCurrent)

    def setMaxCurrent(self, current):
        self.setAxisParameter(self.AP_MaxCurrent, current)

    # StallGuard2 Functions
    def setStallguard2Filter(self, enableFilter):
        self.setAxisParameter(self.AP_StallGuard2FilterEnable, enableFilter)

    def setStallguard2Threshold(self, threshold):
        self.setAxisParameter(self.AP_StallGuard2Threshold, threshold)

    def setStopOnStallVelocity(self, velocity):
        self.setAxisParameter(self.AP_StopOnStall, velocity)

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
        return self.getAxisParameter(self.AP_TMC262ErrorFlags)

    def getErrorFlags(self):
        return self.getAxisParameter(self.AP_ExtendedErrorFlags)

    def positionReached(self):
        return self.getAxisParameter(self.AP_PositionReachedFlag)

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
