import struct
from ..ic.tmc_ic import TMCIc
from ..helpers import TMC_helpers

DATAGRAM_FORMAT = ">BI"
DATAGRAM_LENGTH = 5


class TMC7300(TMCIc):
    """
    The TMC7300 is a low voltage driver for one or two DC motors up to 2A, with UART based control for torque and
    velocity. Supply voltage: 2-11V
    """
    def __init__(self, connection=None):
        super().__init__("TMC7300", self.__doc__)
        self._connection = connection

    # Only used for direct UART access without EvalSystem
    def write_register(self, register_address, value):
        datagram = struct.pack(DATAGRAM_FORMAT, register_address | 0x80, value & 0xFFFFFFFF)
        self._connection.send_datagram(datagram, DATAGRAM_LENGTH)

    # Only used for direct UART access without EvalSystem
    def read_register(self, register_address, signed=False):
        datagram = struct.pack(DATAGRAM_FORMAT, register_address, 0)
        reply = self._connection.send_datagram(datagram, DATAGRAM_LENGTH)
        values = struct.unpack(DATAGRAM_FORMAT, reply)
        value = values[1]
        return TMC_helpers.to_signed_32(value) if signed else value

    def write_register_field(self, field, value):
        return self.write_register(field[0], TMC_helpers.field_set(self.read_register(field[0]),
                                   field[1], field[2], value))

    def read_register_field(self, field):
        return TMC_helpers.field_get(self.read_register(field[0]), field[1], field[2])

    class REG:
        GCONF         = 0x00
        GSTAT         = 0x01
        IFCNT         = 0x02
        SLAVECONF     = 0x03
        IOIN          = 0x06
        CURRENT_LIMIT = 0x10
        PWM_AB        = 0x22
        CHOPCONF      = 0x6C
        DRV_STATUS    = 0x6F
        PWMCONF       = 0x70

    class FIELD:
        """
        Define all register bitfields of the TMC7300.

        Each field is defined as a tuple consisting of ( Address, Mask, Shift ).

        The name of the register is written as a comment behind each tuple. This is
        intended for IDE users viewing the definition of a field by hovering over
        it. This allows the user to see the corresponding register name of a field
        without opening this file and searching for the definition.
        """

        # GCONF
        PWM_DIRECT    = (0x00, 0x00000001,  0)
        EXTCAP        = (0x00, 0x00000002,  1)
        PAR_MODE      = (0x00, 0x00000004,  2)
        TEST_MODE     = (0x00, 0x00000080,  7)

        # GSTAT
        RESET         = (0x01, 0x00000001,  0)
        DRV_ERR       = (0x01, 0x00000002,  1)
        U3V5          = (0x01, 0x00000004,  2)

        # IFCNT
        IFCNT         = (0x02, 0x000000FF,  0)

        # SLAVECONF
        SLAVECONF     = (0x03, 0x00000F00,  8)

        # IOIN
        EN            = (0x06, 0x00000001,  0)
        NSTDBY        = (0x06, 0x00000002,  1)
        AD0           = (0x06, 0x00000004,  2)
        AD1           = (0x06, 0x00000008,  3)
        DIAG          = (0x06, 0x00000010,  4)
        UART_ENABLED  = (0x06, 0x00000020,  5)
        UART_INPUT    = (0x06, 0x00000040,  6)
        MODE_INPUT    = (0x06, 0x00000080,  7)
        A2            = (0x06, 0x00000100,  8)
        A1            = (0x06, 0x00000200,  9)
        COMP_A1A2     = (0x06, 0x00000400, 10)
        COMP_B1B2     = (0x06, 0x00000800, 11)
        VERSION       = (0x06, 0xFF000000, 24)

        # CURRENT_LIMIT
        MOTORRUN      = (0x10, 0x00000001,  0)
        IRUN          = (0x10, 0x00001F00,  8)

        # PWM_AB
        PWM_A         = (0x22, 0x000001FF,  0)
        PWM_B         = (0x22, 0x01FF0000, 16)
        PWM_AB        = (0x22, 0x000001FF,  0)

        # CHOPCONF
        ENABLEDRV     = (0x6C, 0x00000001,  0)
        TBL           = (0x6C, 0x00018000, 15)
        DISS2G        = (0x6C, 0x40000000, 30)
        DISS2VS       = (0x6C, 0x80000000, 31)

        # DRV_STATUS
        OTPW          = (0x6F, 0x00000001,  0)
        OT            = (0x6F, 0x00000002,  1)
        S2GA          = (0x6F, 0x00000004,  2)
        S2GB          = (0x6F, 0x00000008,  3)
        S2VSA         = (0x6F, 0x00000010,  4)
        S2VSB         = (0x6F, 0x00000020,  5)
        OLA           = (0x6F, 0x00000040,  6)
        OLB           = (0x6F, 0x00000080,  7)
        T120          = (0x6F, 0x00000100,  8)
        T150          = (0x6F, 0x00000200,  9)

        # PWMCONF
        PWM_FREQ      = (0x70, 0x00030000, 16)
        FREEWHEEL     = (0x70, 0x00300000, 20)
