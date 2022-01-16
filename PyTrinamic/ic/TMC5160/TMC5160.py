from PyTrinamic.ic.TMC5160.TMC5160_register import TMC5160_register
from PyTrinamic.ic.TMC5160.TMC5160_fields import TMC5160_fields
from PyTrinamic.helpers import TMC_helpers


class TMC5160:
    """
    Class for the TMC5160 IC
    """
    def __init__(self, channel):
        self.__channel  = channel

        self.registers  = TMC5160_register
        self.fields     = TMC5160_fields

        self.MOTORS     = 2

    def showChipInfo(self):
        print("TMC5160 chip info: The TMC5160/A is a high-power stepper motor controller and driver IC with serial communication interfaces. Voltage supply: 8 - 60V")

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
