'''
Created on 09.01.2019

@author: LK
'''

from PyTrinamic.ic.TMC4672.TMC4672_register import TMC4672_register
from PyTrinamic.ic.TMC4672.TMC4672_mask_shift import TMC4672_mask_shift

class TMC4672_eval(object):
    
    def __init__(self, connection):
        self.connection = connection
        self.tmc4672_reg = TMC4672_register()
        self.tmc4672_ms = TMC4672_mask_shift()

    def showChipInfo(self):    
        print("TMC4672_Eval chip info:")
        " read ChipInfo "
        for i in range(5):
            self.connection.writeMC(self.tmc4672_reg.CHIPINFO_ADDR, i)
            reply = self.connection.readMC(self.tmc4672_reg.CHIPINFO_DATA)
            print("ChipInfo[" + str(i) + "]: " + hex(reply.value))
