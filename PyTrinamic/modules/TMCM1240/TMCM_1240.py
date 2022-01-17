'''
Created on 21.09.2020

@author: AA
'''

from PyTrinamic.modules.tmcl_module import TMCLModule

class TMCM_1240(TMCLModule):

    class AP():
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
        FLAG_POSITION_END = 0x00004000

    class GPs():
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

    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)

        self.MOTORS = 1
        self.__default_motor = 0

    def showChipInfo(self):
        print("The TMCM-1240 is a single axis controller/driver module. Voltage supply: 24V");

    " motion Control functions "
    def rotate(self, axis, velocity):
        self.setAxisParameter(self.APs.TargetVelocity, axis, velocity)

    def stop(self, axis):
        self.rotate(axis, 0)

    def moveTo(self, axis, position, velocity=None):
        if velocity:
            self.setMaxVelocity(axis, velocity)

        return self.connection.moveTo(axis, position, self.module_id)

    def moveBy(self, axis, difference, velocity=None):
        if velocity:
            self.setMaxVelocity(velocity)

        return self.connection.moveBy(axis, difference, self.module_id)

    " current control functions "
    def setMotorRunCurrent(self, axis, current):
        self.setMaxCurrent(current)

    def setMotorStandbyCurrent(self, axis, current):
        self.setAxisParameter(self.APs.StandbyCurrent, axis, current)

    def getMaxCurrent(self, axis):
        return self.axisParameter(self.APs.MaxCurrent, axis)

    def setMaxCurrent(self, axis, current):
        self.setAxisParameter(self.APs.MaxCurrent, axis, current)

    " StallGuard2 functions "
    def setStallguard2Filter(self, axis, enableFilter):
        self.setAxisParameter(self.APs.SG2FilterEnable, axis, enableFilter)

    def setStallguard2Threshold(self, axis, threshold):
        self.setAxisParameter(self.APs.SG2Threshold, axis, threshold)

    def setStopOnStallVelocity(self, axis, velocity):
        self.setAxisParameter(self.APs.smartEnergyStallVelocity, axis, velocity)

    " motion parameter functions "
    def getTargetPosition(self, axis):
        return self.axisParameter(self.APs.TargetPosition, axis, signed=True)

    def setTargetPosition(self, axis, position):
        self.setAxisParameter(self.APs.TargetPosition, axis, position)

    def getActualPosition(self, axis):
        return self.axisParameter(self.APs.ActualPosition, axis, signed=True)

    def setActualPosition(self, position):
        return self.setAxisParameter(self.APs.ActualPosition, axis, position)

    def getTargetVelocity(self, axis):
        return self.axisParameter(self.APs.TargetVelocity, axis, signed=True)

    def setTargetVelocity(self, axis, velocity):
        self.setAxisParameter(self.APs.TargetVelocity, axis, velocity)

    def getActualVelocity(self, axis):
        return self.axisParameter(self.APs.ActualVelocity, axis, signed=True)

    def getMaxVelocity(self, axis):
        return self.axisParameter(self.APs.MaxVelocity, axis)

    def setMaxVelocity(self, axis, velocity):
        self.setAxisParameter(self.APs.MaxVelocity, axis, velocity)

    def getMaxAcceleration(self, axis):
        return self.axisParameter(self.APs.MaxAcceleration, axis)

    def setMaxAcceleration(self, axis, acceleration):
        self.setAxisParameter(self.APs.MaxAcceleration, axis, acceleration)

    def setMicrostepResolution(self, axis, microstepResolution):
        self.setAxisParameter(self.APs.MicrostepResolution, axis, microstepResolution)

    " status functions "
    def getStatusFlags(self, axis):
        return self.axisParameter(self.APs.DrvStatusFlags, axis)

    def getErrorFlags(self, axis):
        return self.axisParameter(self.APs.ExtendedErrorFlags, axis)

    def positionReached(self, axis):
        return self.axisParameter(self.APs.PositionReachedFlag, axis)

    " IO pin functions "
    def analogInput(self, x):
        return self.connection.analogInput(x, self.module_id)

    def digitalInput(self, x):
        return self.connection.digitalInput(x, self.module_id)
