'''
Created on 20.09.2019

@author: JM
'''

from PyTrinamic.ic.TMC5072.TMC5072 import TMC5072

class TMC5072_eval(TMC5072):
    """
    This class represents a TMC5072 Evaluation board
    """
    def __init__(self, connection):
        TMC5072.__init__(self, channel=0)
        self.__connection = connection

    # Use the motion controller channel for register access
    def writeRegister(self, registerAddress, value, channel=0):
        if channel != 0:
            raise ValueError

        return self.__connection.writeMC(registerAddress, value)

    def readRegister(self, registerAddress, channel=0, signed=False):
        if channel != 0:
            raise ValueError

        return self.__connection.readMC(registerAddress, signed=signed)
