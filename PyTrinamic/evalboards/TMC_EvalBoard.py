# Created on: 06.07.2021
# Author: LK

from PyTrinamic.modules.tmcl_module import tmcl_module
from PyTrinamic.helpers import TMC_helpers

class TMC_EvalBoard(tmcl_module):

    class EVAL_TYPES:
        MOTION_CONTROLLER = 0
        DRIVER = 1
        UNDEFINED = 2

    def __init__(self, connection, module_id, ic, eval_type):
        super().__init__(connection, module_id)
        self.ic = ic
        self.eval_type = eval_type

    def write_register(self, channel, address, value):
        del channel
        return {
            self.EVAL_TYPES.MOTION_CONTROLLER: self.connection.writeMC,
            self.EVAL_TYPES.DRIVER: self.connection.writeDRV,
            self.EVAL_TYPES.UNDEFINED: self.connection.writeMC
        }.get(self.eval_type)(address, value, moduleID=self.module_id)

    def read_register(self, channel, address, signed=False):
        del channel
        return {
            self.EVAL_TYPES.MOTION_CONTROLLER: self.connection.readMC,
            self.EVAL_TYPES.DRIVER: self.connection.readDRV,
            self.EVAL_TYPES.UNDEFINED: self.connection.readMC
        }.get(self.eval_type)(address, moduleID=self.module_id, signed=signed)

    def write_register_field(self, channel, field, value):
        del channel
        return self.write_register(field[0], TMC_helpers.field_set(self.read_register(field[0]), field[1], field[2], value))

    def read_register_field(self, channel, field):
        del channel
        return TMC_helpers.field_get(self.read_register(field[0]), field[1], field[2])
