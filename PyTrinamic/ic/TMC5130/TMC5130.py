'''
Created on 02.01.2019

@author: ed
'''

from PyTrinamic.ic.TMC5130.TMC5130_register import TMC5130_register
from PyTrinamic.ic.TMC5130.TMC5130_register_variant import TMC5130_register_variant
from PyTrinamic.ic.TMC5130.TMC5130_fields import TMC5130_fields
from PyTrinamic.helpers import TMC_helpers

class TMC5130():
    """
    Class for the TMC5130 IC
    """
    def __init__(self, channel):
        self.__channel  = channel

        self.registers  = TMC5130_register
        self.fields     = TMC5130_fields
        self.variants   = TMC5130_register_variant

        self.MOTORS     = 2

    def showChipInfo(self):
        print("TMC5130 chip info: ?")

    def writeRegister(self, registerAddress, value, channel):
        raise NotImplementedError

    def readRegister(self, registerAddress, channel):
        raise NotImplementedError

    def writeRegisterField(self, field, value):
        return self.writeRegister(field[0], TMC_helpers.field_set(self.readRegister(field[0], self.__channel), field[1], field[2], value), self.__channel)

    def readRegisterField(self, field):
        return TMC_helpers.field_get(self.readRegister(field[0], self.__channel), field[1], field[2])
