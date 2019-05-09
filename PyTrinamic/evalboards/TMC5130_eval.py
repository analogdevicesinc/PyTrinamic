'''
Created on 09.01.2019

@author: LK, ED
'''

from PyTrinamic.ic.TMC5130.TMC5130 import TMC5130

class TMC5130_eval(TMC5130):
    """
    This class represents a TMC5130 Evaluation board
    """
    def __init__(self, connection):
        TMC5130.__init__(self, channel=0)
        self.__connection = connection

    # Use the motion controller channel for register access
    def writeRegister(self, registerAddress, value, channel=0):
        if channel != 0:
            raise ValueError

        return self.__connection.writeMC(registerAddress, value)

    def readRegister(self, registerAddress, channel=0):
        if channel != 0:
            raise ValueError

        return self.__connection.readMC(registerAddress)
