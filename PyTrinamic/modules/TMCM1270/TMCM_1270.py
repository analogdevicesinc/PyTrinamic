'''
Created on 03.12.2019

@author: JM
'''

from PyTrinamic.modules.tmcl_module import tmcl_module
from PyTrinamic.features.LinearRampModule import LinearRampModule
from PyTrinamic.features.StallGuard2Module import StallGuard2Module
from PyTrinamic.features.CurrentModule import CurrentModule
from PyTrinamic.features.MotorControl import MotorControl

class TMCM_1270(tmcl_module):

    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)

        self.MOTORS = [self.MOTOR_0(self, 0)]

    @staticmethod
    def getEdsFile():
        return __file__.replace("TMCM_1270.py", "TMCM_1270_V3.22.eds")

    def showChipInfo(self):
        print("The TMCM-1270 is a smart stepper motor driver module. The module is controlled via a CAN bus interface. Voltage supply: 6 - 24V")

    def rotate(self, axis, velocity):
        self.connection.rotate(axis, velocity, self.module_id)

    def stop(self, axis):
        self.connection.stop(axis, self.module_id)

    def move_to(self, axis, position, velocity=None):
        if velocity:
            self.max_velocity = velocity
        self.connection.moveTo(axis, position, self.module_id)

    def move_by(self, axis, difference, velocity=None):
        if velocity:
            self.max_velocity = velocity
        self.connection.moveBy(axis, difference, self.module_id)

    # IO pin functions
    def analogInput(self, x):
        return self.connection.analogInput(x)

    def digitalInput(self, x):
        return self.connection.digitalInput(x)

    class MOTOR_0(tmcl_module.Motor, LinearRampModule, StallGuard2Module, CurrentModule, MotorControl):

        def __init__(self, module, axis):
            tmcl_module.Motor.__init__(self, module, axis)
            LinearRampMotor.__init__(self)
            StallGuard2Motor.__init__(self)
            CurrentModule.__init__(self)

        def get_position_reached(self):
            return self.get_axis_parameter(self.APs.PositionReachedFlag)

        class APs():
            TargetPosition                 = 0
            ActualPosition                 = 1
            TargetVelocity                 = 2
            ActualVelocity                 = 3
            MaxVelocity                    = 4
            MaxAcceleration                = 5
            RunCurrent                     = 6
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
            ErrorFlags                     = 207
            StatusFlags                    = 208
            EncoderPosition                = 209
            EncoderResolution              = 210
            max_EncoderDeviation           = 212
            PowerDownDelay                 = 214
            UnitMode                       = 255

    class ENUMs():
        pass

    class GPs():

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
