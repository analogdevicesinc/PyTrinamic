'''
Created on 02.01.2019

@author: ED
'''

import struct
from PyTrinamic.ic.TMC4671.TMC4671_register import TMC4671_register
from PyTrinamic.ic.TMC4671.TMC4671_register_variant import TMC4671_register_variant
from PyTrinamic.ic.TMC4671.TMC4671_fields import TMC4671_fields
from PyTrinamic.helpers import TMC_helpers

DATAGRAM_FORMAT = ">BI"
DATAGRAM_LENGTH = 5

class TMC4671():
    """
    Class for the TMC4671 IC
    """
    def __init__(self, connection, channel=0):
        self.__connection = connection
        self.__channel    = channel

        self.registers    = TMC4671_register
        self.fields       = TMC4671_fields
        self.variants     = TMC4671_register_variant

        self.MOTORS       = 1

    def showChipInfo(self):
        print("TMC4671 chip info: The TMC4671 is a fully integreated servo controller, providing Field Orianted Control for BLDC/PMSM and 2-phase Stepper Motors as well as DC motors and voice coils. Voltage supply: 0 - 80V")

    def writeRegister(self, registerAddress, value):
        datagram = struct.pack(DATAGRAM_FORMAT, registerAddress | 0x80, value & 0xFFFFFFFF)
        self.__connection.send_datagram(datagram, DATAGRAM_LENGTH, self.__channel)

    def readRegister(self, registerAddress, signed=False):
        datagram = struct.pack(DATAGRAM_FORMAT, registerAddress, 0)
        reply = self.__connection.send_datagram(datagram, DATAGRAM_LENGTH, self.__channel)

        values = struct.unpack(DATAGRAM_FORMAT, reply)
        value = values[1]

        return TMC_helpers.toSigned32(value) if signed else value

    def writeRegisterField(self, field, value):
        return self.writeRegister(field[0], TMC_helpers.field_set(self.readRegister(field[0]), field[1], field[2], value))

    def readRegisterField(self, field):
        return TMC_helpers.field_get(self.readRegister(field[0]), field[1], field[2])

    def moveBy(self, motor, distance, velocity):
        if not(0 <= motor < self.MOTORS):
            raise ValueError

        position = self.readRegister(self.registers.XACTUAL, signed=True)

        self.moveTo(motor, position + distance, velocity)

        return position + distance

    def get_pin_state(self):
        pass
