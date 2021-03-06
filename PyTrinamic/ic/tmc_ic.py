'''
Created on 22.02.2019

@author: ed
'''

from PyTrinamic.helpers import TMC_helpers

class tmc_ic(object):

    def showChipInfo(self):
        raise NotImplementedError

    def readRegister(self, axis, address, signed=False):
        raise NotImplementedError

    def writeRegister(self, axis, address, value):
        raise NotImplementedError

    def writeRegisterField(self, field, value):
        return self.writeRegister(field[0], TMC_helpers.field_set(self.readRegister(field[0]), field[1], field[2], value))

    def readRegisterField(self, field):
        return TMC_helpers.field_get(self.readRegister(field[0]), field[1], field[2])
