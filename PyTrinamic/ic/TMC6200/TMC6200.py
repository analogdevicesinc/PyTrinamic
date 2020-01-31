'''
Created on 06.03.2019

@author: ED
'''

import struct
from PyTrinamic.ic.TMC6200.TMC6200_register import TMC6200_register
from PyTrinamic.ic.TMC6200.TMC6200_register_variant import TMC6200_register_variant
from PyTrinamic.ic.TMC6200.TMC6200_fields import TMC6200_fields
from PyTrinamic.helpers import TMC_helpers

DATAGRAM_FORMAT = ">BI"
DATAGRAM_LENGTH = 5

class TMC6200():
    """
    Class for the TMC6200 IC
    """
    def __init__(self, connection, channel=0):
        self.__connection = connection
        self.__channel    = channel

        self.registers    = TMC6200_register
        self.fields       = TMC6200_fields
        self.variants     = TMC6200_register_variant

        self.MOTORS       = 1

    def showChipInfo(self):
        print("TMC6200 chip info: The TMC6200 is a high-power gate-driver for PMSM servo or BLDC motors. Voltage supply: 8 - 60V")
        #print("VERSION:    " + hex(self.readRegister(self.TMC6200_register.IOIN_OUTPUT) >> 24))
     
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
