'''
Created on 23.10.2019

@author: JM
'''

from PyTrinamic.ic.TMC2160.TMC2160_register import TMC2160_register
from PyTrinamic.ic.TMC2160.TMC2160_register_variant import TMC2160_register_variant
from PyTrinamic.ic.TMC2160.TMC2160_fields import TMC2160_fields
from PyTrinamic.helpers import TMC_helpers

class TMC2160():
    """
    Class for the TMC2160 IC
    """
    def __init__(self, channel):
        self.__channel  = channel

        self.registers  = TMC2160_register
        self.fields     = TMC2160_fields
        self.variants   = TMC2160_register_variant

        self.MOTORS     = 2

    def showChipInfo(self):
        print("TMC2160 chip info: The TMC2160 is a high-power stepper motor driver IC with SPI interface. Voltage supply: 8 - 60V")

    def writeRegister(self, registerAddress, value, channel):
        raise NotImplementedError

    def readRegister(self, registerAddress, channel):
        raise NotImplementedError

    def writeRegisterField(self, field, value):
        return self.writeRegister(field[0], TMC_helpers.field_set(self.readRegister(field[0], self.__channel), field[1], field[2], value), self.__channel)

    def readRegisterField(self, field):
        return TMC_helpers.field_get(self.readRegister(field[0], self.__channel), field[1], field[2])

    def moveBy(self, motor, distance, velocity):
        if not(0 <= motor < self.MOTORS):
            raise ValueError

        position = self.readRegister(self.registers.XACTUAL, self.__channel, signed=True)

        self.moveTo(motor, position + distance, velocity)

        return position + distance

    def get_pin_state(self):
        pass
