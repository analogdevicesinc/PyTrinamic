from pytrinamic2.ic.TMC2300.TMC2300_register import TMC2300_register
from pytrinamic2.ic.TMC2300.TMC2300_fields import TMC2300_fields
from pytrinamic2.helpers import TMC_helpers


class TMC2300:
    """
    Class for the TMC2300 IC
    """
    def __init__(self, channel):
        self.__channel  = channel

        self.registers  = TMC2300_register
        self.fields     = TMC2300_fields

        self.MOTORS     = 2

    def showChipInfo(self):
        print("TMC2300 chip info: Low Voltage Driver for Two-Phase Stepper Motors up to 1.2A RMS - StealthChop™ for Quiet Movement - UART Interface Option. Voltage supply: 2 - 11V")

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
