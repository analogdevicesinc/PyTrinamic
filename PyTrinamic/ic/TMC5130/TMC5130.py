# Created on: 06.07.2021
# Author: LK

# General imports
from PyTrinamic.ic.TMC_IC import TMC_IC
from PyTrinamic.ic.TMC5130.TMC5130_Registers import TMC5130_Registers
from PyTrinamic.ic.TMC5130.TMC5130_Register_Variants import TMC5130_Register_Variants
from PyTrinamic.ic.TMC5130.TMC5130_Fields import TMC5130_Fields

# Feature imports
from PyTrinamic.features.MotorControlIC import MotorControlIC
from PyTrinamic.features.LinearRampIC import LinearRampIC

class TMC5130(TMC_IC):
    # Constant registers, variants, fields
    REGISTERS = TMC5130_Registers
    VARIANTS = TMC5130_Register_Variants
    FIELDS = TMC5130_Fields

    def __init__(self, handler, channel):
        super().__init__(handler, channel)
        self.MOTORS = [self.MOTOR_0(self, 0)]

    # write and read wrappers for field access with respect to axis.
    # These are used in feature implementations for the motors.
    # Base field is used to identify what to access. With given axis the
    # actual field to be accessed can be resolved in this wrapper function
    # for multi-axis ICs.
    # TMC5130 has one axis only, so it can just be handled as a normal field access.

    def write_axis_field(self, axis, field, value):
        del axis
        return self.write_register_field(field, value)

    def read_axis_field(self, axis, field):
        del axis
        return self.read_register_field(field)

    def showChipInfo(self):
        print("TMC5130 chip info: The TMC5130/A is a high-performance stepper motor controller and driver IC with serial communication interfaces. Voltage supply: 4,75 - 46V")

    # Motion Control functions
    def rotate(self, axis, value):
        self.write_register(self.REGISTERS.AMAX, 1000)

        if value >= 0:
            self.write_register(self.REGISTERS.VMAX, value)
            self.write_register(self.REGISTERS.RAMPMODE, 1)
        else:
            self.write_register(self.REGISTERS.VMAX, -value)
            self.write_register(self.REGISTERS.RAMPMODE, 2)

    def stop(self, axis):
        self.rotate(axis, 0)

    def move_to(self, axis, position, velocity):
        self.write_register(self.REGISTERS.RAMPMODE, 0)

        if velocity != 0:
            self.write_register(self.REGISTERS.VMAX, velocity)

        self.write_register(self.REGISTERS.XTARGET, position)

    def move_by(self, axis, distance, velocity):
        position = self.read_register(self.REGISTERS.XACTUAL, signed=True)

        self.move_to(motor, position + distance, velocity)

        return position + distance

    class MOTOR_0(TMC_IC.Motor, LinearRampIC, MotorControlIC):

        def __init__(self, ic, axis):
            TMC_IC.Motor.__init__(self, ic, axis)
            LinearRampIC.__init__(self)
