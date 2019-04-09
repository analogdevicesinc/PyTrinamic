'''
Created on 09.04.2019

@author: ED, AH
'''

class TMCM_1160(object):
    
    " axis parameters "
    AP_TargetPosition               = 0
    AP_ActualPosition               = 1
    AP_TargetSpeed                  = 2
    AP_ActualSpeed                  = 3
    AP_MaxPositioningSpeed          = 4
    AP_MaxAcceleration              = 5
    AP_MaxCurrent                   = 6
    AP_StandbyCurrent               = 7
    AP_PositionReachedFlag          = 8
    AP_HomeSwitchState              = 9
    AP_RightLimitSwitchState        = 10 
    AP_LeftLimitSwitchState         = 11
    AP_RightLimitSwitchDisable      = 12
    AP_LeftLimitSwitchDisable       = 13
    AP_MinimumSpeed                 = 130
    AP_ActualAcceleration           = 135
    AP_RampMode                     = 138
    AP_MicrostepResolution          = 140
    AP_SoftStopFlag                 = 149
    AP_EndSwitchPowerDownMode       = 150
    AP_RampDivisor                  = 153
    AP_PulseDivisor                 = 154
    AP_StepInterpolationEnable      = 160
    AP_DoubleStepEnable             = 161
    AP_ChopperBlankTime             = 162
    AP_ConstantTOffMode             = 163
    AP_DisableFastDecayComperator   = 164
    AP_ChopperHysteresisEnd         = 165
    AP_ChopperHysteresisStart       = 166
    AP_ChopperOffTime               = 167
    AP_SmartEnergyCurrentMinimum    = 168
    AP_SmartEnergyCurrentDownStep   = 169
    AP_SmartEnergyHysteresis        = 170
    AP_SmartEnergyCurrentUpStep     = 171
    AP_SmartEnergyHysteresisStart   = 172
    AP_StallGuard2FilterEnable      = 173
    AP_StallGuard2Threshold         = 174
    AP_SlopeControlHighSide         = 175
    AP_SlopeControlLowSide          = 176
    AP_ShortProtectionDisable       = 177
    AP_ShortDetectionTimer          = 178
    AP_VSense                       = 179
    AP_SmartEnergyActualCurrent     = 180
    AP_StopOnStall                  = 181
    AP_SmartEnergyThresholdSpeed    = 182
    AP_SmartEnergySlowRunCurrent    = 183
    AP_RandomTOffMode               = 184
    AP_ReferenceSearchMode          = 193
    AP_ReferenceSearchSpeed         = 194
    AP_ReferenceSwitchSpeed         = 195
    AP_EndSwitchDistance            = 196
    AP_LastReferencePosition        = 197
    AP_BoostCurrent                 = 200
    AP_Freewheeling                 = 204
    AP_ActualLoadValue              = 206
    AP_ExtendedErrorFlags           = 207
    AP_TMC262ErrorFlags             = 208
    AP_EncoderPosition              = 209
    AP_EncoderPrescaler             = 210
    AP_MaximumEncoderDeviation      = 212
    AP_PowerDownDelay               = 214
    AP_AbsoluteResolverValue        = 215
    AP_ExternalEncoderPosition      = 216
    AP_ExternalEncoderPrescaler     = 217
    AP_MaxExternalEncoderDeviation  = 218
    AP_StepDirectionMode            = 254

    " global parameters "
    GP_BaudRate                     = 65
    GP_SerialAddress                = 66
    GP_ASCIIMode                    = 67
    GP_SerialHeartbeat              = 68
    GP_CANBitRate                   = 69
    GP_CANReplyID                   = 70
    GP_CANID                        = 71     
    GP_TelegramPauseTime            = 75
    GP_SerialHostAddress            = 76
    GP_AutoStartMode                = 77
    GP_EndSwitchPolarity            = 79
    GP_TMCLCodeProtection           = 81
    GP_CANHeartbeat                 = 82
    GP_CANSecondaryAddress          = 83
    GP_CoordinateStorage            = 84
    GP_DoNotRestoreUserVariables    = 85
    GP_SerialSecondaryAddress       = 87
    GP_ReverseShaft                 = 90

    GP_TMCLApplicationStatus        = 128
    GP_DownloadMode                 = 128
    GP_TMCLProgramCounter           = 130
    GP_TMCLTickTimer                = 132
    GP_RandomNumber                 = 133
    GP_SuppressReply                = 255
    
    FLAG_POSITION_END               = 0x00004000
     
    def __init__(self, connection):
        self.connection = connection
        self.motor = 0

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
        self.setAxisParameter(self.AP_TargetPosition, position)

    def targetPosition(self):
        return self.axisParameter(self.AP_TargetPosition)

    def actualPosition(self):
        return self.axisParameter(self.AP_ActualPosition)
   
    def setActualPosition(self, position):
        return self.setAxisParameter(self.AP_ActualPosition, position)

    def rotate(self, speed):
        self.setAxisParameter(self.AP_TargetSpeed, speed)

    def actualSpeed(self):
        return self.axisParameter(self.AP_ActualSpeed)

    " StallGuard functions " 
    def setMotorRunCurrent(self, runCurrent):
        self.setAxisParameter(self.AP_MaxCurrent, runCurrent)

    def setMotorStandbyCurrent(self, standbyCurrent):
        self.setAxisParameter(self.AP_StandbyCurrent, standbyCurrent)

    def setStallguard2Filter(self, filt):
        self.setAxisParameter(self.AP_StallGuard2FilterEnable, filt)

    def setStallguard2Threshold(self, threshold):
        self.setAxisParameter(self.AP_StallGuard2Threshold, threshold)

    def setStopOnStall(self, stopValue):
        self.setAxisParameter(self.AP_StopOnStall, stopValue)
        
        
    " helpful functions " 
    def maxVelocity(self):
        return self.axisParameter(self.AP_MaxPositioningSpeed)

    def setMaxVelocity(self, maxVelocity):
        self.setAxisParameter(self.AP_MaxPositioningSpeed, maxVelocity)

    def maxAcceleration(self):
        return self.axisParameter(self.AP_MaxAcceleration)

    def setMaxAcceleration(self, maxAcceleration):
        self.setAxisParameter(self.AP_MaxAcceleration, maxAcceleration)

    def maxCurrent(self):
        return self.axisParameter(self.AP_MaxCurrent)

    def setMaxCurrent(self, maxCurrent):
        self.setAxisParameter(self.AP_MaxCurrent, maxCurrent)
          
    def targetSpeed(self):
        return self.axisParameter(self.AP_TargetSpeed)
 
    def setTargetSpeed(self, speed):
        self.setAxisParameter(self.AP_TargetSpeed, speed)

    def positionReached(self):
        return ((self.statusFlags() & self.FLAG_POSITION_END) != 0)

    def rampMode(self):
        return self.axisParameter(self.AP_RampMode)

    def setRampMode(self, mode):
        return self.setAxisParameter(self.AP_RampMode, mode)

    def statusFlags(self):
        return self.axisParameter(self.AP_ExtendedErrorFlags)

    def analogInput(self, x):
        return self.connection.analogInput(x)

    def digitalInput(self, x):
        return self.connection.digitalInput(x)

    def showMotionConfiguration(self):
        print("Motion configuration:")
        print("\tMax velocity: " + str(self.maxVelocity()))
        print("\tAcceleration: " + str(self.maxAcceleration()))
        print("\tRamp mode: " + ("position" if (self.rampMode()==0) else "velocity"))
