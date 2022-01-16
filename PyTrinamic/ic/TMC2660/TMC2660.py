from PyTrinamic.ic.TMC2660.TMC2660_register import TMC2660_register
from PyTrinamic.ic.TMC2660.TMC2660_fields import TMC2660_fields
from PyTrinamic.helpers import TMC_helpers


class TMC2660:
    """
    Class for the TMC2660 IC
    """
    def __init__(self, channel):
        self.__channel  = channel

        self.registers  = TMC2660_register
        self.fields     = TMC2660_fields

        self.MOTORS     = 2

    def showChipInfo(self):
        print("TMC2660 chip info: The TMC2660 is a driver for two-phase stepper motors. Voltage supply: up to 30V ")

    def writeRegister(self, registerAddress, value, channel):
        raise NotImplementedError

    def readRegister(self, registerAddress, channel):
        raise NotImplementedError

    def writeRegisterField(self, field, value):
        return self.writeRegister(field[0], TMC_helpers.field_set(self.readRegister(field[0], self.__channel), field[1], field[2], value), self.__channel)

    def readRegisterField(self, field):
        return TMC_helpers.field_get(self.readRegister(field[0], self.__channel), field[1], field[2])

    def get_pin_state(self):
        pass
