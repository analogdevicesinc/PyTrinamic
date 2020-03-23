'''
Created on 18.03.2020

@author: LK
'''

from PyTrinamic.ic.TMC5160.TMC5160 import TMC5160
from PyTrinamic.TMCL import TMCL_Command

class TMC5160_shield(TMC5160):
    """
    This class represents a TMC5160 Evaluation Shield.

    Communication is done over the TMCL commands writeMC and readMC,
    wrapped in writeRegister and readRegister respectively.
    In the wrapper function, an additional channel number can be assigned to
    distinguish between 3+ ICs. An implementation without TMCL may still use
    this class if these two functions are provided properly. See __init__ for
    details on the function requirements.
    """

    def __init__(self, connection, channel, moduleID=1):
        """
        Parameters:
            connection:
                Type: class
                A class that provides the neccessary functions for communicating
                with a TMC5160. The required functions are
                    connection.writeRegister(registerAddress, command, channel, value, moduleID)
                    connection.readRegister(registerAddress, command, channel, moduleID, signed)
                for writing/reading to registers of the TMC5160.
            channel:
                Type: int
                IC index for the given module. It is used to distinguish between
                multiple ICs of the same type on a single module.
            moduleID:
                Type: int, optional, default value: 1
                The TMCL module ID of the TMC5160. This ID is used as a
                parameter for the writeRegister and readRegister functions.
        """
        TMC5160.__init__(self, moduleID)

        self.__connection = connection
        self.__channel = channel
        self._MODULE_ID = moduleID

        self.APs = _APs

    def __str__(self):
        return f"{self.__class__.__name__}[{self.__channel}]"

    # Use the motion controller functions for register access
    def writeRegister(self, registerAddress, value, moduleID=None):
        # If the moduleID argument is omitted, use the stored module ID
        if not moduleID:
            moduleID = self._MODULE_ID

        return self.__connection.writeRegister(registerAddress, TMCL_Command.WRITE_MC, self.__channel, value, moduleID)

    def readRegister(self, registerAddress, moduleID=None, signed=False):
        # If the moduleID argument is omitted, use the stored module ID
        if not moduleID:
            moduleID = self._MODULE_ID

        return self.__connection.readRegister(registerAddress, TMCL_Command.READ_MC, self.__channel, moduleID, signed)

    # Axis parameter access
    def getAxisParameter(self, apType, axis):
        return self.__connection.axisParameter(apType, self.__channel)

    def setAxisParameter(self, apType, axis, value):
        self.__connection.setAxisParameter(apType, self.__channel, value)

    # Motion Control functions
    def rotate(self, motor, value):
        if not(0 <= motor < self.MOTORS):
            raise ValueError

        self.__connection.rotate(self.__channel, value, moduleID=self._MODULE_ID)

    def stop(self, motor):
        self.__connection.stop(motor, moduleID=self._MODULE_ID)

    def moveTo(self, motor, position, velocity=None):
        if velocity and velocity != 0:
            # Set maximum positioning velocity
            self.setAxisParameter(self.APs.MaxVelocity, motor, velocity)

        self.__connection.move(0, motor, position, moduleID=self._MODULE_ID)

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
    THIGH                          = 23
    VDCMIN                         = 24
    HighSpeedChopperMode           = 27
    HighSpeedFullstepMode          = 28
    MeasuredSpeed                  = 29
    I_scale_analog                 = 33
    internal_Rsense                = 34
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
    smartEnergyActualCurrent       = 180
    smartEnergyStallVelocity       = 181
    smartEnergyThresholdSpeed      = 182
    RandomTOffMode                 = 184
    ChopperSynchronization         = 185
    PWMThresholdSpeed              = 186
    PWMGrad                        = 187
    PWMAmplitude                   = 188
    PWMFrequency                   = 191
    PWMAutoscale                   = 192
    FreewheelingMode               = 204
    LoadValue                      = 206
    EncoderPosition                = 209
    EncoderResolution              = 210
