'''
Created on 19.04.2021

@author: LK
'''

class TMCM_3214():

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
        HomeSwitch                     = 9
        RightEndstop                   = 10
        LeftEndstop                    = 11
        RightLimitSwitchDisable        = 12
        LeftLimitSwitchDisable         = 13
        SwapLimitSwitches              = 14
        A1                             = 15
        V1                             = 16
        MaxDeceleration                = 17
        D1                             = 18
        StartVelocity                  = 19
        StopVelocity                   = 20
        RampWaitTime                   = 21
        THIGH                          = 22
        min_dcStep_speed               = 23
        RightLimitSwitchPolarity       = 24
        LeftLimitSwitchPolarity        = 25
        softstop                       = 26
        HighSpeedChopperMode           = 27
        HighSpeedFullstepMode          = 28
        MeasuredSpeed                  = 29
        PowerDownRamp                  = 31
        dcStep_time                    = 32
        dcStep_stallGuard              = 33
        relative_positioning_option    = 127
        MicrostepResolution            = 140
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
        GlobalCurrentScaler            = 178
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
        ReferenceSwitchSpeed           = 195
        ReferenceSwitchDistance        = 196
        LastReferenceSwitchPosition    = 197
        FullstepResolution             = 202
        FreewheelingMode               = 204
        LoadValue                      = 206
        ExtendedErrorFlags             = 207
        DrvStatusFlags                 = 208
        EncoderPosition                = 209
        encoder_cleat                  = 210
        max_encoder_deviation          = 212
        PowerDownDelay                 = 214
        absolute_resolver_value        = 215
        external_encoder_position      = 216
        external_encoder_resolution    = 217
        external_encoder_max_deviation = 218
        reverse_shaft                  = 251
        step_direction_mode            = 254
        unit_mode                      = 255

    class ENUMs():
        pass

    class GPs():
        serialBaudRate                 = 65
        serialAddress                  = 66
        ASCIIMode                      = 67
        serialHeartbeat                = 68
        CANBitRate                     = 69
        CANreceiveID                   = 70
        CANsendID                      = 71
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
        SuppressReply                  = 255

    def __init__(self, connection, module_id=1):
        self.connection = connection

        self.MOTORS = 1
        self.MODULE_ID = module_id
        self.__default_motor = 0

    @staticmethod
    def getEdsFile():
        return __file__.replace("TMCM_3110.py", "TMCM_3110_V.320.eds")

    def showChipInfo(self):
        print("The TMCM-3110 is a 3-Axis Stepper Controller / Driver. Voltage supply: 12 - 48V");

    # Axis parameter access
    def getAxisParameter(self, apType, axis):
        return self.connection.axisParameter(apType, axis, self.MODULE_ID)

    def setAxisParameter(self, apType, axis, value):
        self.connection.setAxisParameter(apType, axis, value, self.MODULE_ID)

    # Global parameter access
    def getGlobalParameter(self, gpType, bank):
        return self.connection.globalParameter(gpType, bank, self.MODULE_ID)

    def setGlobalParameter(self, gpType, bank, value):
        self.connection.setGlobalParameter(gpType, bank, value, self.MODULE_ID)

    # Motion Control functions
    def rotate(self, axis, velocity):
        self.setAxisParameter(self.APs.TargetVelocity, axis, velocity)

    def stop(self, axis):
        self.rotate(axis, 0)

    def moveTo(self, axis, position, velocity=None):
        if velocity:
            self.setMaxVelocity(axis, velocity)

        return self.connection.moveTo(axis, position, self.MODULE_ID)

    def moveBy(self, axis, difference, velocity=None):
        if velocity:
            self.setMaxVelocity(axis, velocity)

        return self.connection.moveBy(axis, difference, self.MODULE_ID)

    # Current control functions
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

    def setTargetVelocity(self, velocity, axis):
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

    def getRampMode(self, axis):
        return self.getAxisParameter(self.APs.RampMode, axis)

    def setRampMode(self, axis, mode):
        return self.setAxisParameter(self.APs.RampMode, axis, mode)

    # Status functions
    def getStatusFlags(self, axis):
        return self.getAxisParameter(self.APs.DrvStatusFlags, axis)

    def getErrorFlags(self, axis):
        return self.getAxisParameter(self.APs.ExtendedErrorFlags, axis)

    def positionReached(self, axis):
        return self.getAxisParameter(self.APs.PositionReachedFlag, axis)

    # IO pin functions
    def analogInput(self, x):
        return self.connection.analogInput(x)

    def digitalInput(self, x):
        return self.connection.digitalInput(x)
