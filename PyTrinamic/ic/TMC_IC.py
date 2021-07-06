# Created on: 06.07.2021
# Author: LK

from PyTrinamic.helpers import TMC_helpers

class TMC_IC(object):

    class Motor(object):

        def __init__(self, ic, axis):
            self.ic = ic
            self.axis = axis

        def write_axis_field(self, field, value):
            return self.ic.write_axis_field(self.axis, field, value)

        def read_axis_field(self, field):
            return self.ic.read_axis_field(self.axis, field)

    def __init__(self, handler, channel):
        self.handler = handler
        self.channel = channel

    def write_register(self, address, value):
        return self.handler.write_register(self.channel, address, value)

    def read_register(self, address, signed=False):
        return self.handler.read_register(self.channel, address, signed)

    def write_register_field(self, field, value):
        return self.write_register(field[0], TMC_helpers.field_set(self.read_register(field[0]), field[1], field[2], value))

    def read_register_field(self, field):
        return TMC_helpers.field_get(self.read_register(field[0]), field[1], field[2])

    # write and read wrappers for field access with respect to axis.
    # These are used in feature implementations for the motors.
    # Base field is used to identify what to access. With given axis the
    # actual field to be accessed can be resolved for multi-axis ICs in the implementation of this
    # wrapper functions within the IC class.

    def write_axis_field(self, axis, field, value):
        raise NotImplementedError()

    def read_axis_field(self, axis, field):
        raise NotImplementedError()
