from pytrinamic.ic.TMC5161.TMC5161_register import TMC5161_register
from pytrinamic.ic.TMC5161.TMC5161_fields import TMC5161_fields
from pytrinamic.helpers import TMC_helpers


class TMC5161:
    """
    Class for the TMC5161 IC
    """
    def __init__(self, channel):
        self.__channel  = channel

        self.registers  = TMC5161_register
        self.fields     = TMC5161_fields

        self.MOTORS     = 2

    def showChipInfo(self):
        print("TMC5161 chip info: The TMC5161 is a high-power two phase stepper motor controller and driver IC with serial communication interfaces. Voltage supply: 8 - 55V")

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
