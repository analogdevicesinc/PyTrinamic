from PyTrinamic.ic.TMC2590.TMC2590_register import TMC2590_register
from PyTrinamic.ic.TMC2590.TMC2590_fields import TMC2590_fields
from PyTrinamic.helpers import TMC_helpers


class TMC2590:
    """
    Class for the TMC2590 IC
    """
    def __init__(self, channel):
        self.__channel  = channel

        self.registers  = TMC2590_register
        self.fields     = TMC2590_fields

        self.MOTORS     = 2

    def showChipInfo(self):
        print("TMC2590 chip info: The TMC2590 driver for two-phase stepper motors including high-resolution microstepping, sensorless mechanical load measurement and low-resonance chopper operation. Voltage supply: 5 - 60V")

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
