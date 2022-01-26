from pytrinamic2.ic.TMC2100.TMC2100_register import TMC2100_register
from pytrinamic2.ic.TMC2100.TMC2100_fields import TMC2100_fields
from pytrinamic2.helpers import TMC_helpers


class TMC2100:
    """
    Class for the TMC2100 IC
    """
    def __init__(self, channel):
        self.__channel  = channel

        self.registers  = TMC2100_register
        self.fields     = TMC2100_fields

        self.MOTORS     = 2

    def showChipInfo(self):
        print("TMC2100 chip info: The TMC2100 is a standalone driver IC for two-phase stepper motors. Voltage supply: 4.75 - 46V")

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
