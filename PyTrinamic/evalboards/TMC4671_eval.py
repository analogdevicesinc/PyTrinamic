'''
Created on 02.01.2019

@author: ED
'''

from PyTrinamic.evalboards.eval_interface import eval_interface
from PyTrinamic.ic.TMC4671.TMC4671 import TMC4671
from PyTrinamic.helpers import TMC_helpers

class TMC4671_eval(eval_interface):
    
    def __init__(self, connection):
        self.connection = connection
        self.tmc4671 = TMC4671(self)
    
    def register(self):
        return self.tmc4671.register()
    
    def variants(self):
        return self.tmc4671.variants()
    
    def maskShift(self):
        return self.tmc4671.maskShift()
    
    def ic(self):
        return self.tmc4671

    " register access: use Landungsbrücke/Startrampe with MC channel"
    def writeRegister(self, registerAddress, value):
        return self.connection.writeMC(registerAddress, value)
    
    def readRegister(self, registerAddress):
        return self.connection.readMC(registerAddress)
    
    def writeRegisterField(self, registerAddress, value, mask, shift):
        return self.writeRegister(registerAddress, TMC_helpers.field_set(self.readRegister(registerAddress), mask, shift, value))
     
    def readRegisterField(self, registerAddress, mask, shift):
        return TMC_helpers.field_get(self.readRegister(registerAddress), mask, shift)
