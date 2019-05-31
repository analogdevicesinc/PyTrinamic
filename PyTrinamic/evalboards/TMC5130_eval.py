'''
Created on 09.01.2019

@author: LK, ED, LH
'''

from PyTrinamic.ic.TMC5130.TMC5130 import TMC5130

class TMC5130_eval(TMC5130):
    """
    This class represents a TMC5130 Evaluation board.

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
                with a TMC5130. The required functions are
                    connection.writeMC(registerAddress, value, moduleID)
                    connection.readMC(registerAddress, moduleID, signed)
                for writing/reading to registers of the TMC5130.
            moduleID:
                Type: int, optional, default value: 1
                The TMCL module ID of the TMC5130. This ID is used as a
                parameter for the writeMC and readMC functions.
        """
        TMC5130.__init__(self, moduleID)

        self.__connection = connection
        self._MODULE_ID = moduleID

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
