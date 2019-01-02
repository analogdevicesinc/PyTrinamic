'''
Created on 02.01.2019

@author: ED
'''

from PyTrinamic.ICs.TMC4671.TMC4671_Register import TMC4671_Register
from PyTrinamic.ICs.TMC4671.TMC4671_Mask_Shift import TMC4671_Mask_Shift

class TMC4671_Eval(object):
    
    def __init__(self, connection):
        self.connection = connection
        self.tmc4671_reg = TMC4671_Register()
        self.tmc4671_ms = TMC4671_Mask_Shift()

    def showChipInfo(self):    
        print("TMC4671_Eval chip info:")
        " read ChipInfo "
        for i in range(5):
            self.connection.writeMC(self.tmc4671_reg.CHIPINFO_ADDR, i)
            reply = self.connection.readMC(self.tmc4671_reg.CHIPINFO_DATA)
            print("ChipInfo[" + str(i) + "]: " + hex(reply.value))
