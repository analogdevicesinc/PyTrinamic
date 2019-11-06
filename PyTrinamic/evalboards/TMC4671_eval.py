'''
Created on 02.01.2019

@author: ED
'''

from PyTrinamic.ic.TMC4671.TMC4671 import TMC4671

class TMC4671_eval(TMC4671):

    def __init__(self, connection, moduleID=1):
        self.connection = connection
        
        TMC4671.__init__(self, connection=None, channel=0)

    def register(self):
        return self.tmc4671.register()

    def variants(self):
        return self.tmc4671.variants()

    def maskShift(self):
        return self.tmc4671.maskShift()

    def ic(self):
        return self.tmc4671

    " register access: use Landungsbrücke/Startrampe with MC channel"
    def writeRegister(self, registerAddress, value , channel=0):
        if channel != 0:
            raise ValueError
        return self.connection.writeMC(registerAddress, value)

    def readRegister(self, registerAddress, channel=0, signed=False):
        if channel != 0:
            raise ValueError
        return self.connection.readMC(registerAddress, signed=signed)