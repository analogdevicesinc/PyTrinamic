'''
Created on 24.09.2019

@author: JM
'''

from PyTrinamic.ic.TMC5062.TMC5062 import TMC5062

class TMC5062_eval(TMC5062):
    """
    This class represents a TMC5062 Evaluation board
    """
    def __init__(self, connection):
        TMC5062.__init__(self, channel=0)
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
