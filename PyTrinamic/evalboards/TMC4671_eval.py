'''
Created on 02.01.2019

@author: ED
'''

from PyTrinamic.ic.TMC4671.TMC4671_register import TMC4671_register
from PyTrinamic.ic.TMC4671.TMC4671_mask_shift import TMC4671_mask_shift

class TMC4671_eval(object):
    
    def __init__(self, connection):
        self.connection = connection
        self.tmc4671_reg = TMC4671_register()
        self.tmc4671_ms = TMC4671_mask_shift()

    def showChipInfo(self):    
        print("TMC4671_Eval chip info:")
        " read ChipInfo "
        for i in range(5):
            self.connection.writeMC(self.tmc4671_reg.CHIPINFO_ADDR, i)
            reply = self.connection.readMC(self.tmc4671_reg.CHIPINFO_DATA)
            print("ChipInfo[" + str(i) + "]: " + hex(reply.value))
