'''
Created on 09.01.2019

@author: LK, ED
'''

from PyTrinamic.ic.TMC5130.TMC5130 import TMC5130

class TMC5130_eval(TMC5130):
    """
    This class represents a TMC5130 Evaluation board
    """
    def __init__(self, connection, moduleID=1):
        TMC5130.__init__(self, moduleID)

        self.__connection = connection
        self._MODULE_ID = moduleID

    # Use the motion controller channel for register access
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
