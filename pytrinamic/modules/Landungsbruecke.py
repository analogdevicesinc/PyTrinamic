################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from pytrinamic.tmcl import TMCLCommand


class IDEEPROM:
    """
    This class represents an ID-EEPROM of an EVAL board that is connected to a Landungsbruecke.

    All accesses are in little-endian byte order. No alignment of addresses is
    required.

    This class is designed for usage with the Evalsystem ID EEPROM but can be
    used with any other EEPROM implementation providing the proper access
    functions.

    Possible extensions:
    - Add big-endian support
    - Add minimum alignment requirement support
    """

    # Addresses for Evalsystem ID EEPROM
    ADDR_DESCRIPTION       = 0
    ADDR_ID                = 16
    ADDR_HW_VERSION_MAJOR  = 18
    ADDR_HW_VERSION_MINOR  = 19
    ADDR_MAGIC_NUMBER      = 20
    # Magic number (little-endian) for the Evalsystem ID EEPROM
    MAGIC_NUMBER           = 0x3412

    """
    For initialization two functions need to be provided.
    A 32 bit read function (little endian) and an 8 bit write function.
    """
    def __init__(self, read32func, write8func):
        if not callable(read32func):
            raise ValueError("IDEEPROM class requires a callable read function")

        if not callable(write8func):
            raise ValueError("IDEEPROM class requires a callable write function")

        self._read32func = read32func
        self._write8func = write8func

    def read_byte(self, address):
        return self._read32func(address) & 0xFF

    def read_short(self, address):
        return self._read32func(address) & 0xFFFF

    def read_int(self, address):
        return self._read32func(address)

    def read_ascii(self, address, length):
        text = ""
        for i in range(address, address+length, 4):
            data = self.read_int(i)
            text += chr((data >>  0) & 0xFF)
            text += chr((data >>  8) & 0xFF)
            text += chr((data >> 16) & 0xFF)
            text += chr((data >> 24) & 0xFF)

        # In case we read more than needed, cut away excess characters
        text = text[0:length]

        return text

    def read_id_info(self):
        # Check magic number
        if self.read_short(self.ADDR_MAGIC_NUMBER) != self.MAGIC_NUMBER:
            return None

        desc     = self.read_ascii(self.ADDR_DESCRIPTION, 16)
        board_id = self.read_short(self.ADDR_ID)
        hw_major = self.read_byte(self.ADDR_HW_VERSION_MAJOR)
        hw_minor = self.read_byte(self.ADDR_HW_VERSION_MINOR)

        return {"description": desc.strip('\x00'), "id": board_id, "hw_major": hw_major, "hw_minor": hw_minor}

    def write_byte(self, address, value):
        self._write8func(address, value)

    def write_short(self, address, value):
        for i in range(2):
            self._write8func(address + i, value >> (i*8))

    def write_int(self, address, value):
        for i in range(4):
            self._write8func(address + i, value >> (i*8))

    def write_ascii(self, address, text):
        for i, c in enumerate(text):
            self._write8func(address + i, ord(c))

    def write_id_info(self, description, board_id, hw_major_version, hw_minor_version):
        if type(description) != str:
            raise TypeError("Description must be a string")

        if len(description) > 16:
            raise ValueError("Description cannot be longer than 16 characters")

        if not(type(board_id) == type(hw_major_version) == type(hw_minor_version) == int):
            raise TypeError("Board ID and Hardware versions must be integers")

        # Pad the string with zeros if necessary
        description += "\x00" * (16-len(description))

        self.write_ascii(self.ADDR_DESCRIPTION, description)
        self.write_short(self.ADDR_ID, board_id)
        self.write_byte(self.ADDR_HW_VERSION_MAJOR, hw_major_version)
        self.write_byte(self.ADDR_HW_VERSION_MINOR, hw_minor_version)
        self.write_short(self.ADDR_MAGIC_NUMBER, self.MAGIC_NUMBER)


class Landungsbruecke:
    def __init__(self, connection):
        self._connection = connection

        self._mcId = 0
        self._drvId = 0

        self.id_eeprom_mc = IDEEPROM(self._read_mc_eeprom, self._write_mc_eeprom)
        self.id_eeprom_drv = IDEEPROM(self._read_drv_eeprom, self._write_drv_eeprom)

    def get_board_ids(self):
        """
        Read out the IDs of the detected boards.

        This does not start a detection.
        Returns a tuple of IDs: (drvId, mcId)
        """
        value = self._connection.get_global_parameter(self.GP.BoardAssignment, 0)

        drvStatus = (value >> 24) & 0xFF
        drvId     = (value >> 16) & 0xFF
        mcStatus  = (value >>  8) & 0xFF
        mcId      = (value      ) & 0xFF

        if mcStatus == 2:
            self._mcId = mcId
        if drvStatus == 2:
            self._drvId = drvId

        return self._mcId, self._drvId

    def detect_board_ids(self):
        """
        Start an IDDetection and read out the IDs of the detected boards.
        """
        while not self._connection.send(TMCLCommand.ASSIGNMENT, 0, 0, 0).is_valid():
            pass

        return self.get_board_ids()

    def get_board_names(self):
        board_ids = self.get_board_ids()

        try:
            mc_name = self.mc_id_names[board_ids[0]]
        except KeyError:
            mc_name = str(board_ids[0])

        try:
            drv_name = self.drv_id_names[board_ids[1]]
        except KeyError:
            drv_name = str(board_ids[1])

        return mc_name, drv_name

    def _read_mc_eeprom(self, address):
        reply = self._connection.send(TMCLCommand.TMCL_UF1, 1, 0, address)

        if not reply.is_valid():
            raise RuntimeError("Failed to read driver ID EEPROM")

        return reply.value

    def _write_mc_eeprom(self, address, value):
        self._connection.send(TMCLCommand.TMCL_UF2, 1, value, address)

    def _read_drv_eeprom(self, address):
        reply = self._connection.send(TMCLCommand.TMCL_UF1, 2, 0, address)

        if not reply.is_valid():
            raise RuntimeError("Failed to read driver ID EEPROM")

        return reply.value

    def _write_drv_eeprom(self, address, value):
        self._connection.send(TMCLCommand.TMCL_UF2, 2, value & 0xFF, address)

    mc_id_names = {
        0  : "None",
        2  : "TMC5031",
        4  : "TMC4361",
        5  : "TMC5130",
        6  : "TMC5041",
        7  : "TMC5072",
        9  : "TMC4670",
        10 : "TMC4331",
        11 : "TMC4361A",
        13 : "TMC4671",
        15 : "TMC4330",
        16 : "TMC5160",
        18 : "TMC5161",
        25 : "TMC5062",
        26 : "TMC8461",
        27 : "TMC8462",
        28 : "TMC5240",
        29 : "TMC5272",
        31 : "TMC5271",
    }

    drv_id_names = {
        0  : "None",
        1  : "TMC2660",
        3  : "TMC2130",
        4  : "TMC2100",
        5  : "TMC2041",
        6  : "TMC2208",
        7  : "TMC2224",
        8  : "TMC2209",
        9  : "TMCC160",
        10 : "TMC6200",
        11 : "TMC2160",
        12 : "TMC7300",
        13 : "TMC2590",
        18 : "TMC2225",
        19 : "TMC6100",
        14 : "TMC2300",
        21 : "TMC6300",
        22 : "TMC2226",
        23 : "TMC6140",
        25 : "TMC6100_BOB",
        28 : "TMC2240",
        29 : "TMC2210",
        30 : "MAX22216_EVAL",
        31 : "MAX22216_BOB",
        32 : "MAX22204_EVAL",
        33 : "MAX22210_EVAL",
        34 : "TMC8100",
    }

    class GP:
        VitalSignsErrorMask  = 1
        DriversEnable        = 2
        DebugMode            = 3
        BoardAssignment      = 4
        HWID                 = 5
        PinState             = 6
