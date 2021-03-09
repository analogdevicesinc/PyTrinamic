'''
Created on 22.02.2019

@author: LK
'''

from PyTrinamic.helpers import TMC_helpers
from PyTrinamic.modules.tmcl_module import tmcl_module

class tmc_eval(tmcl_module):

    def __init__(self, connection, module_id):
        super().__init__(connection, module_id)
        self.ics = []

    def readRegister(self, axis, address, signed=False):
        raise NotImplementedError()

    def writeRegister(self, axis, address, value):
        raise NotImplementedError()

    def writeRegisterField(self, field, value):
        return self.writeRegister(field[0], TMC_helpers.field_set(self.readRegister(field[0]), field[1], field[2], value))

    def readRegisterField(self, field):
        return TMC_helpers.field_get(self.readRegister(field[0]), field[1], field[2])
