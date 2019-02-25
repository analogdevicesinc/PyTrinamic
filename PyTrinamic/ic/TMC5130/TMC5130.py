'''
Created on 02.01.2019

@author: ed
'''

from PyTrinamic.ic.ic_interface import ic_interface
from PyTrinamic.ic.TMC5130.TMC5130_register import TMC5130_register
from PyTrinamic.ic.TMC5130.TMC5130_register_variant import TMC5130_register_variant
from PyTrinamic.ic.TMC5130.TMC5130_mask_shift import TMC5130_mask_shift
from PyTrinamic.helpers import TMC_helpers

class TMC5130(ic_interface):

    def __init__(self, parent):
        self.parent = parent
        self.tmc5130_reg = TMC5130_register()
        self.tmc5130_var = TMC5130_register_variant() 
        self.tmc5130_ms = TMC5130_mask_shift()

    def register(self):
        return self.tmc5130_reg
    
    def variants(self):
        return self.tmc5130_var
        
    def maskShift(self):
        return self.tmc5130_ms;
 
    def showChipInfo(self):    
        print("TMC5130 chip info: ?")

    " use parent readRegister/writeRegister from evaluation board or interface"
    def writeRegister(self, registerAddress, value):
        self.parent.writeRegister(registerAddress, value);
        
    def readRegister(self, registerAddress):
        return self.parent.readRegister(registerAddress)

    def writeRegisterField(self, registerAddress, value, mask, shift):
        return self.writeRegister(registerAddress, TMC_helpers.field_set(self.readRegister(registerAddress), mask, shift, value))
     
    def readRegisterField(self, registerAddress, mask, shift):
        return TMC_helpers.field_get(self.readRegister(registerAddress), mask, shift)
