'''
Created on 17.10.2019

@author: JM
'''

from PyTrinamic.ic.TMC2225.TMC2225 import TMC2225

class TMC2225_eval(TMC2225):
    """
    This class represents a TMC2225 Evaluation board.

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
                with a TMC2225. The required functions are
                    connection.writeDRV(registerAddress, value, moduleID)
                    connection.readDRV(registerAddress, moduleID, signed)
                for writing/reading to registers of the TMC2225.
            moduleID:
                Type: int, optional, default value: 1
                The TMCL module ID of the TMC2225. This ID is used as a
                parameter for the writeDRV and readDRV functions.
        """
        TMC2225.__init__(self, moduleID)

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
    
    def moveTo(self, motor, position, velocity=None):
        if velocity and velocity != 0:
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
    internal_Rsense = 28
    MeasuredSpeed = 29
    StepDirSource = 50
    StepDirFrequency = 51
    MicrostepResolution = 140
    ChopperBlankTime = 162
    ChopperHysteresisEnd = 165
    ChopperHysteresisStart = 166
    TOff = 167
    VSense = 179
    smartEnergyActualCurrent = 180
    smartEnergyStallVelocity = 181
    PWMThresholdSpeed = 186
    PWMGrad = 187
    PWMFrequency = 191
    PWMAutoscale = 192
    FreewheelingMode = 204