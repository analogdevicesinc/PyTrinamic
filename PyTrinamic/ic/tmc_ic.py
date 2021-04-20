'''
Created on 22.02.2019

@author: LK
'''

from PyTrinamic.helpers import TMC_helpers

class tmc_ic(object):

    def __init__(self, module, channel):
        self._module = module
        self._channel = channel

    def showChipInfo(self):
        raise NotImplementedError

    def _address_axis(self, address, axis):
        del axis
        return address

    def readRegister(self, address, axis=0, signed=False):
        return self._module.readRegister(self._channel, self._address_axis(address, axis), signed)

    def writeRegister(self, address, value, axis=0):
        self._module.writeRegister(self._channel, self._address_axis(address, axis), value)

    def writeRegisterField(self, field, value, axis=0):
        return self.writeRegister(field[0], TMC_helpers.field_set(self.readRegister(field[0], axis), field[1], field[2], value))

    def readRegisterField(self, field, axis=0):
        return TMC_helpers.field_get(self.readRegister(field[0], axis), field[1], field[2])
