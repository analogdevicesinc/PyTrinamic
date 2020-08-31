'''
Created on 09.01.2019

@author: LK
'''

from PyTrinamic import name, desc

class TMC_helpers(object):

    @staticmethod
    def field_get(data, mask, shift):
        return (data & mask) >> shift

    @staticmethod
    def field_set(data, mask, shift, value):
        return (data & (~mask)) | ((value << shift) & mask)

    @staticmethod
    def toSigned32(x):
        m = x & 0xffffffff
        return (m ^ 0x80000000) - 0x80000000

    @staticmethod
    def showInfo():
        print(name + " - " + desc)

class EEPROM():
    """
    This class provides basic access to an EEPROM.

    All accesses are in little-endian byte order. No alignment of addresses is
    required.

    This class is designed for usage with the Evalsystem ID eeproms but can be
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
            raise ValueError("EEPROM class requires a callable read function")

        if not callable(write8func):
            raise ValueError("EEPROM class requires a callable write function")

        self._read32func = read32func
        self._write8func = write8func

    def readByte(self, address):
        return self._read32func(address) & 0xFF

    def readShort(self, address):
        return self._read32func(address) & 0xFFFF

    def readInt(self, address):
        return self._read32func(address)

    def readASCII(self, address, length):
        text = ""
        for i in range(address, address+length, 4):
            data = self.readInt(i)
            text += chr((data >>  0) & 0xFF)
            text += chr((data >>  8) & 0xFF)
            text += chr((data >> 16) & 0xFF)
            text += chr((data >> 24) & 0xFF)

        # In case we read more than needed, cut away excess characters
        text = text[0:length]

        return text

    def read_id_info(self):
        # Check magic number
        if self.readShort(self.ADDR_MAGIC_NUMBER) != self.MAGIC_NUMBER:
            return None

        desc     = self.readASCII(self.ADDR_DESCRIPTION, 16)
        board_id = self.readShort(self.ADDR_ID)
        hw_major = self.readByte(self.ADDR_HW_VERSION_MAJOR)
        hw_minor = self.readByte(self.ADDR_HW_VERSION_MINOR)

        return { "description":desc.strip('\x00'), "id":board_id, "hw_major":hw_major, "hw_minor":hw_minor }

    def writeByte(self, address, value):
        self._write8func(address, value)

    def writeShort(self, address, value):
        for i in range(2):
            self._write8func(address + i, value >> (i*8))

    def writeInt(self, address, value):
        for i in range(4):
            self._write8func(address + i, value >> (i*8))

    def writeASCII(self, address, text):
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

        self.writeASCII(self.ADDR_DESCRIPTION, description)
        self.writeShort(self.ADDR_ID, board_id)
        self.writeByte(self.ADDR_HW_VERSION_MAJOR, hw_major_version)
        self.writeByte(self.ADDR_HW_VERSION_MINOR, hw_minor_version)
        self.writeShort(self.ADDR_MAGIC_NUMBER, self.MAGIC_NUMBER)
