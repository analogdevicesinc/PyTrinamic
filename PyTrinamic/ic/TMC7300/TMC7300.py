import struct
from PyTrinamic.ic.TMC7300.TMC7300_register import TMC7300_register
from PyTrinamic.ic.TMC7300.TMC7300_fields import TMC7300_fields
from PyTrinamic.helpers import TMC_helpers

DATAGRAM_FORMAT = ">BI"
DATAGRAM_LENGTH = 5


class TMC7300:
    """
    Class for the TMC7300 IC
    """
    def __init__(self, connection, channel=0):
        self.__connection = connection
        self.__channel    = channel

        self.registers    = TMC7300_register
        self.fields       = TMC7300_fields

        self.MOTORS       = 1

    def showChipInfo(self):
        print("TMC7300 chip info: Low Voltage Driver for One or Two DC Motors up to 2A (2.4A) peak – UART based Control for Torque and Velocity. Voltage supply: 2 - 11V")
     
    def writeRegister(self, registerAddress, value, channel=None):
        del channel
        datagram = struct.pack(DATAGRAM_FORMAT, registerAddress | 0x80, value)
        self.__connection.send_datagram(datagram, DATAGRAM_LENGTH)

    def readRegister(self, registerAddress, signed=False, channel=None):
        del channel
        datagram = struct.pack(DATAGRAM_FORMAT, registerAddress, 0)
        reply = self.__connection.send_datagram(datagram, DATAGRAM_LENGTH)

        values = struct.unpack(DATAGRAM_FORMAT, reply)
        value = values[1]

        return TMC_helpers.toSigned32(value) if signed else value

    def writeRegisterField(self, field, value):
        return self.writeRegister(field[0], TMC_helpers.field_set(self.readRegister(field[0], self.__channel), field[1], field[2], value), self.__channel)

    def readRegisterField(self, field):
        return TMC_helpers.field_get(self.readRegister(field[0], self.__channel), field[1], field[2])

    def get_pin_state(self):
        pass
