import struct
from pytrinamic2.ic.TMC4331.TMC4331_register import TMC4331_register
from pytrinamic2.ic.TMC4331.TMC4331_fields import TMC4331_fields
from pytrinamic2.helpers import TMC_helpers

DATAGRAM_FORMAT = ">BI"
DATAGRAM_LENGTH = 5


class TMC4331:
    """
    Class for the TMC4331 IC
    """
    def __init__(self, connection, channel=0):
        self.__connection = connection
        self.__channel    = channel

        self.registers    = TMC4331_register
        self.fields       = TMC4331_fields

        self.MOTORS       = 1

    def showChipInfo(self):
        print("TMC4331 chip info: The TMC4331 is a miniaturized high-performance motion controller for stepper motor drivers, particulary designed for fast jerk-limited motion profile applications with a wide range of ramp profiles. Voltage supply: - ")

    def writeRegister(self, registerAddress, value):
        datagram = struct.pack(DATAGRAM_FORMAT, registerAddress | 0x80, value & 0xFFFFFFFF)
        self.__connection.send_datagram(datagram, DATAGRAM_LENGTH)

    def readRegister(self, registerAddress, signed=False):
        datagram = struct.pack(DATAGRAM_FORMAT, registerAddress, 0)
        reply = self.__connection.send_datagram(datagram, DATAGRAM_LENGTH)

        values = struct.unpack(DATAGRAM_FORMAT, reply)
        value = values[1]

        return TMC_helpers.to_signed_32(value) if signed else value

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
