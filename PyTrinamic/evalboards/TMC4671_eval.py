'''
Created on 02.01.2019

@author: ED
'''

from PyTrinamic.ic.TMC4671.TMC4671_register import TMC4671_register
from PyTrinamic.ic.TMC4671.TMC4671_register_variant import TMC4671_register_variant
from PyTrinamic.ic.TMC4671.TMC4671_mask_shift import TMC4671_mask_shift

class TMC4671_eval(object):
    
    def __init__(self, connection):
        self.connection = connection
        self.tmc4671_reg = TMC4671_register()
        self.tmc4671_var = TMC4671_register_variant() 
        self.tmc4671_ms = TMC4671_mask_shift()

    def showChipInfo(self):    
        print("TMC4671_Eval chip info:")

        self.connection.writeMC(self.tmc4671_reg.CHIPINFO_ADDR, self.tmc4671_var.CHIPINFO_ADDR_SI_TYPE)
        print("SI_TYPE:    " + hex(self.connection.readMC(self.tmc4671_reg.CHIPINFO_DATA).value))
        
        self.connection.writeMC(self.tmc4671_reg.CHIPINFO_ADDR, self.tmc4671_var.CHIPINFO_ADDR_SI_VERSION)
        print("SI_VERSION: " + hex(self.connection.readMC(self.tmc4671_reg.CHIPINFO_DATA).value))
        
        self.connection.writeMC(self.tmc4671_reg.CHIPINFO_ADDR, self.tmc4671_var.CHIPINFO_ADDR_SI_DATA)
        print("SI_DATA:    " + hex(self.connection.readMC(self.tmc4671_reg.CHIPINFO_DATA).value))
        
        self.connection.writeMC(self.tmc4671_reg.CHIPINFO_ADDR, self.tmc4671_var.CHIPINFO_ADDR_SI_TIME)
        print("SI_TIME:    " + hex(self.connection.readMC(self.tmc4671_reg.CHIPINFO_DATA).value))
        
        self.connection.writeMC(self.tmc4671_reg.CHIPINFO_ADDR, self.tmc4671_var.CHIPINFO_ADDR_SI_VARIANT)
        print("SI_VARIANT: " + hex(self.connection.readMC(self.tmc4671_reg.CHIPINFO_DATA).value))
        
        self.connection.writeMC(self.tmc4671_reg.CHIPINFO_ADDR, self.tmc4671_var.CHIPINFO_ADDR_SI_BUILD)
        print("SI_BUILD:   " + hex(self.connection.readMC(self.tmc4671_reg.CHIPINFO_DATA).value))
                     