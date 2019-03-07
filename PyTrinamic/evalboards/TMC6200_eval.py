'''
Created on 06.03.2019

@author: ED
'''

from PyTrinamic.evalboards.eval_interface import eval_interface
from PyTrinamic.ic.TMC6200.TMC6200 import TMC6200
from PyTrinamic.helpers import TMC_helpers

class TMC6200_eval(eval_interface):
    
    def __init__(self, connection):
        self.connection = connection
        self.tmc6200 = TMC6200(self)
    
    def register(self):
        return self.tmc6200.register()
    
    def variants(self):
        return self.tmc6200.variants()
    
    def maskShift(self):
        return self.tmc6200.maskShift()
    
    def ic(self):
        return self.tmc6200

    " register access: use Landungsbrücke/Startrampe with DRV channel"
    def writeRegister(self, registerAddress, value):
        return self.connection.writeDRV(registerAddress, value)
    
    def readRegister(self, registerAddress):
        return self.connection.readDRV(registerAddress)
    
    def writeRegisterField(self, registerAddress, value, mask, shift):
        return self.writeRegister(registerAddress, TMC_helpers.field_set(self.readRegister(registerAddress), mask, shift, value))
     
    def readRegisterField(self, registerAddress, mask, shift):
        return TMC_helpers.field_get(self.readRegister(registerAddress), mask, shift)
