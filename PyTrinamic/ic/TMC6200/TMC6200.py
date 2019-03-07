'''
Created on 06.03.2019

@author: ED
'''

from PyTrinamic.ic.ic_interface import ic_interface
from PyTrinamic.ic.TMC6200.TMC6200_register import TMC6200_register
from PyTrinamic.ic.TMC6200.TMC6200_register_variant import TMC6200_register_variant
from PyTrinamic.ic.TMC6200.TMC6200_mask_shift import TMC6200_mask_shift
from PyTrinamic.helpers import TMC_helpers

class TMC6200(ic_interface):

    def __init__(self, parent):
        self.parent = parent
        self.tmc6200_reg = TMC6200_register()
        self.tmc6200_var = TMC6200_register_variant() 
        self.tmc6200_ms = TMC6200_mask_shift()

    def register(self):
        return self.tmc6200_reg
    
    def variants(self):
        return self.tmc6200_var
        
    def maskShift(self):
        return self.tmc6200_ms;
 
    def showChipInfo(self):    
        print("TMC6200 chip info:")
        print("VERSION:    " + hex(self.readRegister(self.tmc6200_reg.IOIN_OUTPUT) >> 24))


    " use parent readRegister/writeRegister from evaluation board or interface"
    def writeRegister(self, registerAddress, value):
        self.parent.writeRegister(registerAddress, value);
        
    def readRegister(self, registerAddress):
        return self.parent.readRegister(registerAddress)

    def writeRegisterField(self, registerAddress, value, mask, shift):
        return self.writeRegister(registerAddress, TMC_helpers.field_set(self.readRegister(registerAddress), mask, shift, value))
     
    def readRegisterField(self, registerAddress, mask, shift):
        return TMC_helpers.field_get(self.readRegister(registerAddress), mask, shift)
