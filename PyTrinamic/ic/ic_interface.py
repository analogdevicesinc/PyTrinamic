'''
Created on 22.02.2019

@author: ed
'''

class ic_interface(object):

    def showChipInfo(self):
        raise NotImplementedError

    def readRegister(self, address):
        raise NotImplementedError

    def writeRegister(self, address, value):
        raise NotImplementedError

    def writeRegisterField(self, registerAddress, field, value):
        return self.writeRegister(field[0], TMC_helpers.field_set(self.readRegister(field[0]), field[1], field[2], value))

    def readRegisterField(self, registerAddress, field):
        return TMC_helpers.field_get(self.readRegister(field[0]), field[1], field[2])
