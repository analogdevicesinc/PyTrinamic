'''
Created on 20.09.2019

@author: JM
'''

from PyTrinamic.ic.TMC5072.TMC5072 import TMC5072
from PyTrinamic.evalboards.tmc_eval import tmc_eval
from PyTrinamic.features.StallGuard2Module import StallGuard2Module
from PyTrinamic.features.LinearRampModule import LinearRampModule
from PyTrinamic.features.MotorControl import MotorControl
from PyTrinamic.features.StallGuard2Motor import StallGuard2Motor
from PyTrinamic.features.LinearRampMotor import LinearRampMotor
from PyTrinamic.features.MotorControlMotor import MotorControlMotor
from PyTrinamic.MotorManager import MotorManager

class TMC5072_eval(tmc_eval, StallGuard2Module, LinearRampModule, MotorControl):
    """
    This class represents a TMC5072 Evaluation board
    """

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
        RightEndstop                   = 10
        LeftEndstop                    = 11
        AutomaticRightStop             = 12
        AutomaticLeftStop              = 13
        SW_MODE                        = 14
        A1                             = 15
        V1                             = 16
        MaxDeceleration                = 17
        D1                             = 18
        StartVelocity                  = 19
        StopVelocity                   = 20
        RampWaitTime                   = 21
        smartEnergyThresholdSpeed      = 22
        THIGH                          = 23
        VDCMIN                         = 24
        HighSpeedFullstepMode          = 28
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
        VSense                         = 179
        smartEnergyActualCurrent       = 180
        smartEnergyStallVelocity       = 181
        RandomTOffMode                 = 184
        ChopperSynchronization         = 185
        LoadValue                      = 206
        EncoderPosition                = 209
        EncoderResolution              = 210

    def __init__(self, connection, module_id=1):
        tmc_eval.__init__(self, connection, module_id)

        self.ics = [TMC5072(self)]
        self.MOTORS = [
            MotorManager.motor(0, [self, self.ics[0]], features=[LinearRampMotor, MotorControlMotor, StallGuard2Motor]),
            MotorManager.motor(1, [self, self.ics[0]], features=[LinearRampMotor, MotorControlMotor, StallGuard2Motor])
        ]

    # Use the motion controller channel for register access
    def writeRegister(self, channel, address, value):
        del channel
        return self.connection.writeMC(address, value, self.module_id)

    def readRegister(self, channel, address, signed=False):
        del channel
        return self.connection.readMC(address, self.module_id, signed)

    # Motion Control functions
    def rotate(self, axis, value):
        self.connection.rotate(axis, value)

    def stop(self, axis):
        self.connection.stop(axis)

    def moveTo(self, axis, position, velocity=None):
        if velocity and velocity != 0:
            # Set maximum positioning velocity
            self.setAxisParameter(self.APs.MaxVelocity, axis, velocity)

        self.connection.move(0, axis, position)

    def moveBy(self, axis, difference, velocity=None):
        position = difference + self.getActualPosition(axis)

        self.moveTo(axis, position, velocity)

        return position
