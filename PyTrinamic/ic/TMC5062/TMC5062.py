'''
Created on 24.09.2019

@author: JM
'''

from PyTrinamic.ic.TMC5062.TMC5062_register import TMC5062_register
from PyTrinamic.ic.TMC5062.TMC5062_register_variant import TMC5062_register_variant
from PyTrinamic.ic.TMC5062.TMC5062_fields import TMC5062_fields
from PyTrinamic.helpers import TMC_helpers

class TMC5062():
    """
    Class for the TMC5062 IC
    """
    def __init__(self, channel):
        self.__channel  = channel

        self.registers  = TMC5062_register
        self.fields     = TMC5062_fields
        self.variants   = TMC5062_register_variant

        self.MOTORS     = 2

    def showChipInfo(self):
        print("TMC5062 chip info: The TMC5062 is a high performance motion controller and driver for up two stepper motors. Voltage supply: 4,75 - 20V")

    def writeRegister(self, registerAddress, value, channel):
        raise NotImplementedError

    def readRegister(self, registerAddress, channel):
        raise NotImplementedError

    def writeRegisterField(self, field, value):
        return self.writeRegister(field[0], TMC_helpers.field_set(self.readRegister(field[0], self.__channel), field[1], field[2], value), self.__channel)

    def readRegisterField(self, field):
        return TMC_helpers.field_get(self.readRegister(field[0], self.__channel), field[1], field[2])

    # Motion Control functions
    def rotate(self, motor, value):
        if not(0 <= motor < self.MOTORS):
            raise ValueError

        self.writeRegister(self.registers.AMAX[motor], 1000, self.__channel)

        if value >= 0:
            self.writeRegister(self.registers.VMAX[motor], value, self.__channel)
            self.writeRegister(self.registers.RAMPMODE[motor], 1, self.__channel)
        else:
            self.writeRegister(self.registers.VMAX[motor], -value, self.__channel)
            self.writeRegister(self.registers.RAMPMODE[motor], 2, self.__channel)

    def stop(self, motor):
        self.rotate(motor, 0)

    def moveTo(self, motor, position, velocity):
        if not(0 <= motor < self.MOTORS):
            raise ValueError

        self.writeRegister(self.registers.RAMPMODE[motor], 0, self.__channel)

        if velocity != 0:
            self.writeRegister(self.registers.VMAX[motor], velocity, self.__channel)

        self.writeRegister(self.registers.XTARGET[motor], position, self.__channel)
