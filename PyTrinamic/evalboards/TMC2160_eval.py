'''
Created on 23.10.2019

@author: JM
'''

from PyTrinamic.ic.TMC2160.TMC2160 import TMC2160

class TMC2160_eval(TMC2160):
    """
    This class represents a TMC2160 Evaluation board.

    Communication is done over the TMCL commands writeDRV and readDRV. An
    implementation without TMCL may still use this class if these two functions
    are provided properly. See __init__ for details on the function
    requirements.
    """
    
    def __init__(self, connection, moduleID=1):
        """
        Parameters:
            connection:
                Type: class
                A class that provides the neccessary functions for communicating
                with a TMC2160. The required functions are
                    connection.writeDRV(registerAddress, value, moduleID)
                    connection.readDRV(registerAddress, moduleID, signed)
                for writing/reading to registers of the TMC2160.
            moduleID:
                Type: int, optional, default value: 1
                The TMCL module ID of the TMC2160. This ID is used as a
                parameter for the writeDRV and readDRV functions.
        """
        TMC2160.__init__(self, moduleID)

        self.__connection = connection
        self._MODULE_ID = moduleID
        
        self.APs = _APs

    # Use the driver controller functions for register access
    def writeRegister(self, registerAddress, value, moduleID=None):
        # If the moduleID argument is omitted, use the stored module ID
        if not moduleID:
            moduleID = self._MODULE_ID

        return self.__connection.writeDRV(registerAddress, value, moduleID)

    def readRegister(self, registerAddress, moduleID=None, signed=False):
        # If the moduleID argument is omitted, use the stored module ID
        if not moduleID:
            moduleID = self._MODULE_ID

        return self.__connection.readDRV(registerAddress, moduleID, signed)

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

        self.__connection.rotate(motor, value, moduleID=self._MODULE_ID)
    
    def stop(self, motor):
        self.__connection.stop(motor, moduleID=self._MODULE_ID)
    
    
    def moveTo(self, motor, position, velocity):
        # Set maximum positioning velocity
        self.setAxisParameter(self.APs.MaxVelocity, motor, velocity)
        
        self.__connection.move(0, motor, position, moduleID=self._MODULE_ID)

class _APs():
    TargetPosition = 0
    ActualPosition = 1
    TargetVelocity = 2
    ActualVelocity = 3
    MaxVelocity = 4
    MaxAcceleration = 5
    MaxCurrent = 6
    StandbyCurrent = 7
    PositionReachedFlag = 8
    THIGH = 23
    VDCMIN = 24
    HighSpeedFullstepMode = 26
    HighSpeedChopperMode = 27
    internal_Rsense = 28
    MeasuredSpeed = 29
    StepDirSource = 50
    StepDirFrequency = 51
    MicrostepResolution = 140
    ChopperBlankTime = 162
    ConstantTOffMode = 163
    DisableFastDecayComparator = 164
    ChopperHysteresisEnd = 165
    ChopperHysteresisStart = 166
    TOff = 167
    SEIMIN = 168
    SECDS = 169
    smartEnergyHysteresis = 170
    SECUS = 171
    smartEnergyHysteresisStart = 172
    SG2FilterEnable = 173
    SG2Threshold = 174
    VSense = 179
    smartEnergyActualCurrent = 180
    smartEnergyStallVelocity = 181
    smartEnergyThresholdSpeed = 182
    RandomTOffMode = 184
    ChopperSynchronization = 185
    PWMThresholdSpeed = 186
    PWMGrad = 187
    PWMAmplitude = 188
    PWMFrequency = 191
    PWMAutoscale = 192
    FreewheelingMode = 204
    LoadValue = 206