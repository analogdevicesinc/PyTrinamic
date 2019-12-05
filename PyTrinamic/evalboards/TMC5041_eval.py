'''
Created on 29.04.2019

@author: LH , JM
'''

from PyTrinamic.ic.TMC5041.TMC5041 import TMC5041

class TMC5041_eval(TMC5041):
    """
    This class represents a TMC5041 Evaluation board
    """
    def __init__(self, connection):
        TMC5041.__init__(self, channel=0)
        self.__connection = connection

        self.APs = _APs
        
    # Use the motion controller channel for register access
    def writeRegister(self, registerAddress, value, channel=0):
        if channel != 0:
            raise ValueError

        return self.__connection.writeMC(registerAddress, value)

    def readRegister(self, registerAddress, channel=0, signed=False):
        if channel != 0:
            raise ValueError

        return self.__connection.readMC(registerAddress, signed=signed)
        # Axis parameter access
    def getAxisParameter(self, apType, axis):
        if not(0 <= axis < self.MOTORS):
            raise ValueError("Axis index out of range")

        return self.__connection.axisParameter(apType, axis)

    def setAxisParameter(self, apType, axis, value):
        if not(0 <= axis < self.MOTORS):
            raise ValueError("Axis index out of range")

        self.__connection.setAxisParameter(apType, axis, value)

    # Motion Control functions
    def rotate(self, motor, value):
        if not(0 <= motor < self.MOTORS):
            raise ValueError

        self.__connection.rotate(motor, value)

    def stop(self, motor):
        self.__connection.stop(motor)

    def moveTo(self, motor, position, velocity=None):
        if velocity and velocity != 0:
            # Set maximum positioning velocity
            self.setAxisParameter(self.APs.MaxVelocity, motor, velocity)

        self.__connection.move(0, motor, position)

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
    LoadValue                      = 206
    EncoderPosition                = 209
    EncoderResolution              = 210
