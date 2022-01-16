from PyTrinamic.ic.TMC2209.TMC2209_register import TMC2209_register
from PyTrinamic.ic.TMC2209.TMC2209_fields import TMC2209_fields
from PyTrinamic.helpers import TMC_helpers


class TMC2209:
    """
    Class for the TMC2209 IC
    """
    def __init__(self, channel):
        self.__channel  = channel

        self.registers  = TMC2209_register
        self.fields     = TMC2209_fields

        self.MOTORS     = 2

    def showChipInfo(self):
        print("TMC2209 chip info: The TMC2209 is an ultra-silent motor driver IC for two phase stepper motors. TMC2209 pinning is compatible to a number of legacy drivers as well as to the TMC2208. Voltage supply:  4,75 - 29V")

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
