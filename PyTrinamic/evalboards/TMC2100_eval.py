'''
Created on 16.10.2019

@author: JM
'''

from PyTrinamic.ic.TMC2100.TMC2100 import TMC2100

class TMC2100_eval(TMC2100):
    """
    This class represents a TMC2100 Evaluation board.

    Communication is done over the TMCL commands writeMC and readMC. An
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
                with a TMC2100. The required functions are
                    connection.writeMC(registerAddress, value, moduleID)
                    connection.readMC(registerAddress, moduleID, signed)
                for writing/reading to registers of the TMC2100.
            moduleID:
                Type: int, optional, default value: 1
                The TMCL module ID of the TMC2100. This ID is used as a
                parameter for the writeMC and readMC functions.
        """
        TMC2100.__init__(self, moduleID)

        self.__connection = connection
        self._MODULE_ID = moduleID
        
        self.APs = _APs

    # Use the motion controller functions for register access
    def writeRegister(self, registerAddress, value, moduleID=None):
        # If the moduleID argument is omitted, use the stored module ID
        if not moduleID:
            moduleID = self._MODULE_ID

        return self.__connection.writeMC(registerAddress, value, moduleID)

    def readRegister(self, registerAddress, moduleID=None, signed=False):
        # If the moduleID argument is omitted, use the stored module ID
        if not moduleID:
            moduleID = self._MODULE_ID

        return self.__connection.readMC(registerAddress, moduleID, signed)

    # Axis parameter access
    def getAxisParameter(self, apType, axis):
        if not(0 <= axis < self.MOTORS):
            raise ValueError("Axis index out of range")
        
        if not apType in self.APs._list:
            raise ValueError("Invalid axis parameter")

        return self.__connection.axisParameter(apType, axis)

    def setAxisParameter(self, apType, axis, value):
        if not(0 <= axis < self.MOTORS):
            raise ValueError("Axis index out of range")

        if not apType in self.APs._list:
            raise ValueError("Invalid axis parameter")

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
        self.setAxisParameter(self.APs.MAXIMUM_SPEED, motor, velocity)
        
        self.__connection.move(0, motor, position, moduleID=self._MODULE_ID)

class _APs():
    TARGET_POSITION                               =  0
    ACTUAL_POSITION                               =  1
    TARGET_SPEED                                  =  2
    ACTUAL_SPEED                                  =  3
    MAXIMUM_SPEED                                 =  4
    MAXIMUM_ACCELERATION                          =  5
    POSITION_REACHED_FLAG                         =  8
    CHOPPER_OFF_TIME                              = 14
    MICROSTEP_RESOLUTION_INTERPLATION_AND_CHOPPER = 15
    MAXIMUM_CURRENT                               = 16
    CHOPPER_HYSTERESIS                            = 17
    CHOPPER_BLANK_TIME                            = 18
    POWER_DOWN_DELAY                              = 19
    MICROSTEP_RESOLUTION                          = 140
    
    _list = (
        TARGET_POSITION                               ,
        ACTUAL_POSITION                               ,
        TARGET_SPEED                                  ,
        ACTUAL_SPEED                                  ,
        MAXIMUM_SPEED                                 ,
        MAXIMUM_ACCELERATION                          ,
        POSITION_REACHED_FLAG                         ,
        CHOPPER_OFF_TIME                              ,
        MICROSTEP_RESOLUTION_INTERPLATION_AND_CHOPPER ,
        MAXIMUM_CURRENT                               ,
        CHOPPER_HYSTERESIS                            ,
        CHOPPER_BLANK_TIME                            ,
        POWER_DOWN_DELAY                              ,
        MICROSTEP_RESOLUTION                          ,
        )

