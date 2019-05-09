'''
Created on 29.04.2019

@author: LH
'''

from PyTrinamic.ic.TMC5041.TMC5041 import TMC5041

class TMC5041_eval(TMC5041):
    """
    This class represents a TMC5041 Evaluation board
    """
    def __init__(self, connection):
        TMC5041.__init__(self, channel=0)
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
