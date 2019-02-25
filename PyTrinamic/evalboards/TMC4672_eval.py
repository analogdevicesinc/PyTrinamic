'''
Created on 09.01.2019

@author: LK, ED
'''

from PyTrinamic.evalboards.eval_interface import eval_interface
from PyTrinamic.ic.TMC4672.TMC4672 import TMC4672
from PyTrinamic.helpers import TMC_helpers

class TMC4672_eval(eval_interface):
    
    def __init__(self, connection):
        self.connection = connection
        self.tmc4672 = TMC4672(self)

    def register(self):
        return self.tmc4672.register()
    
    def variants(self):
        return self.tmc4672.variants()
    
    def maskShift(self):
        return self.tmc4672.maskShift()
    
    def ic(self):
        return self.tmc4672

    " register access: use Landungsbrücke/Startrampe with MC channel"
    def writeRegister(self, registerAddress, value):
        return self.connection.writeMC(registerAddress, value)
    
    def readRegister(self, registerAddress):
        return self.connection.readMC(registerAddress)

    def writeRegisterField(self, registerAddress, value, mask, shift):
        return self.writeRegister(registerAddress, TMC_helpers.field_set(self.readRegister(registerAddress), mask, shift, value))
     
    def readRegisterField(self, registerAddress, mask, shift):
        return TMC_helpers.field_get(self.readRegister(registerAddress), mask, shift)
