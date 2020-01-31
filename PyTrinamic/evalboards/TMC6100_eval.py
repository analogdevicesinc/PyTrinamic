'''
Created on 31.01.2020

@author: JM
'''

from PyTrinamic.ic.TMC6100.TMC6100 import TMC6100
from PyTrinamic.helpers import TMC_helpers

class TMC6100_eval(TMC6100):

    def __init__(self, connection, moduleID=1):
        self.connection = connection
        TMC6100.__init__(self, connection=None, channel=moduleID)

    def register(self):
        return self.TMC6100.register()

    def variants(self):
        return self.TMC6100.variants()

    def maskShift(self):
        return self.TMC6100.maskShift()

    def ic(self):
        return self.TMC6100

    " register access: use Landungsbrücke/Startrampe with DRV channel"
    def writeRegister(self, registerAddress, value):
        return self.connection.writeDRV(registerAddress, value)

    def readRegister(self, registerAddress):
        return self.connection.readDRV(registerAddress)

    def writeRegisterField(self, registerAddress, value, mask, shift):
        return self.writeRegister(registerAddress, TMC_helpers.field_set(self.readRegister(registerAddress), mask, shift, value))

    def readRegisterField(self, registerAddress, mask, shift):
        return TMC_helpers.field_get(self.readRegister(registerAddress), mask, shift)

class _APs():
    pass
