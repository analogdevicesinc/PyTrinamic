import struct
from PyTrinamic.ic.TMC4671.TMC4671_register import TMC4671_register
from PyTrinamic.ic.TMC4671.TMC4671_register_variant import TMC4671_register_variant
from PyTrinamic.ic.TMC4671.TMC4671_fields import TMC4671_fields
from PyTrinamic.ic.TMC4671.TMC4671_enums import TMC4671_enums
from PyTrinamic.helpers import TMC_helpers

DATAGRAM_FORMAT = ">BI"
DATAGRAM_LENGTH = 5


class TMC4671:
    """
    The TMC4671 is a fully integrated servo controller, providing Field Oriented Control for BLDC/PMSM
    and 2-phase Stepper motors as well as DC motor support.
    """
    def __init__(self, connection):
        self.__connection = connection
        self.registers = TMC4671_register
        self.fields = TMC4671_fields
        self.variants = TMC4671_register_variant
        self.ENUMs = TMC4671_enums
        self.MOTORS = 1

    # only used for direct UART access without EvalSystem
    def write_register(self, register_address, value):
        datagram = struct.pack(DATAGRAM_FORMAT, register_address | 0x80, value & 0xFFFFFFFF)
        self.__connection.send_datagram(datagram, DATAGRAM_LENGTH)

    # only used for direct UART access without EvalSystem
    def read_register(self, register_address, signed=False):
        datagram = struct.pack(DATAGRAM_FORMAT, register_address, 0)
        reply = self.__connection.send_datagram(datagram, DATAGRAM_LENGTH)
        values = struct.unpack(DATAGRAM_FORMAT, reply)
        value = values[1]
        return TMC_helpers.toSigned32(value) if signed else value

    def write_register_field(self, field, value):
        return self.write_register(field[0], TMC_helpers.field_set(self.read_register(field[0]),
                                   field[1], field[2], value))

    def read_register_field(self, field):
        return TMC_helpers.field_get(self.read_register(field[0]), field[1], field[2])

