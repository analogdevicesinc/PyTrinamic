'''
Created on 09.01.2019

@author: LK
'''

from PyTrinamic.ic.TMC5130.TMC5130_register import TMC5130_register
from PyTrinamic.ic.TMC5130.TMC5130_mask_shift import TMC5130_mask_shift

class TMC5130_eval(object):
    
    def __init__(self, connection):
        self.connection = connection
        self.tmc5130_reg = TMC5130_register()
        self.tmc5130_ms = TMC5130_mask_shift()
