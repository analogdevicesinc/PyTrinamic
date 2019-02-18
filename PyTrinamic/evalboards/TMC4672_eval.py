'''
Created on 09.01.2019

@author: LK
'''

from PyTrinamic.ic.TMC4672.TMC4672_register import TMC4672_register
from PyTrinamic.ic.TMC4672.TMC4672_register_variant import TMC4672_register_variant
from PyTrinamic.ic.TMC4672.TMC4672_mask_shift import TMC4672_mask_shift

class TMC4672_eval(object):
    
    def __init__(self, connection):
        self.connection = connection
        self.tmc4672_reg = TMC4672_register()
        self.tmc4672_var = TMC4672_register_variant();
        self.tmc4672_ms = TMC4672_mask_shift()

    def showChipInfo(self):    
        print("TMC4672_Eval chip info:")

        self.connection.writeMC(self.tmc4672_reg.CHIPINFO_ADDR, self.tmc4672_var.CHIPINFO_ADDR_SI_TYPE)
        print("SI_TYPE:    " + hex(self.connection.readMC(self.tmc4672_reg.CHIPINFO_DATA).value))
        
        self.connection.writeMC(self.tmc4672_reg.CHIPINFO_ADDR, self.tmc4672_var.CHIPINFO_ADDR_SI_VERSION)
        print("SI_VERSION: " + hex(self.connection.readMC(self.tmc4672_reg.CHIPINFO_DATA).value))
        
        self.connection.writeMC(self.tmc4672_reg.CHIPINFO_ADDR, self.tmc4672_var.CHIPINFO_ADDR_SI_DATA)
        print("SI_DATA:    " + hex(self.connection.readMC(self.tmc4672_reg.CHIPINFO_DATA).value))
        
        self.connection.writeMC(self.tmc4672_reg.CHIPINFO_ADDR, self.tmc4672_var.CHIPINFO_ADDR_SI_TIME)
        print("SI_TIME:    " + hex(self.connection.readMC(self.tmc4672_reg.CHIPINFO_DATA).value))
        
        self.connection.writeMC(self.tmc4672_reg.CHIPINFO_ADDR, self.tmc4672_var.CHIPINFO_ADDR_SI_VARIANT)
        print("SI_VARIANT: " + hex(self.connection.readMC(self.tmc4672_reg.CHIPINFO_DATA).value))
        
        self.connection.writeMC(self.tmc4672_reg.CHIPINFO_ADDR, self.tmc4672_var.CHIPINFO_ADDR_SI_BUILD)
        print("SI_BUILD:   " + hex(self.connection.readMC(self.tmc4672_reg.CHIPINFO_DATA).value))        
