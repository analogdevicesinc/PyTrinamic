'''
Created on 16.02.2018

@author: TS, ED
'''

import struct

_PACKAGE_STRUCTURE = ">BBBBIB"

class TMCL(object):
    @staticmethod
    def validate_host_id(host_id):
        if(not(type(host_id) == int)):
            raise TypeError
        if(not(0 <= host_id < 256)):
            raise ValueError("Incorrect Host ID value. Must be between 0 and 255 inclusively.")

    @staticmethod
    def validate_module_id(module_id):
        if(not(type(module_id) == int)):
            raise TypeError
        if(not(0 <= module_id < 256)):
            raise ValueError("Incorrect Module ID value. Must be between 0 and 255 inclusively.")

    @staticmethod
    def calculate_checksum(data):
        checksum = 0
        for d in data:
            checksum += d
        checksum %= 256
        return checksum

class TMCL_Command(object):
    ROR                         = 1
    ROL                         = 2
    MST                         = 3
    MVP                         = 4
    SAP                         = 5
    GAP                         = 6
    STAP                        = 7
    RSAP                        = 8
    SGP                         = 9
    GGP                         = 10
    STGP                        = 11
    RSGP                        = 12
    RFS                         = 13
    SIO                         = 14
    GIO                         = 15
    CALC                        = 19
    COMP                        = 20
    JC                          = 21
    JA                          = 22
    CSUB                        = 23
    RSUB                        = 24
    WAIT                        = 27
    STOP                        = 28
    SAC                         = 29
    SCO                         = 30
    GCO                         = 31
    CCO                         = 32
    CALCX                       = 33
    AAP                         = 34
    AGP                         = 35
    CLE                         = 36
    TMCL_UF0                    = 64
    TMCL_UF1                    = 65
    TMCL_UF2                    = 66
    TMCL_UF3                    = 67
    TMCL_UF4                    = 68
    TMCL_UF5                    = 69
    TMCL_UF6                    = 70
    TMCL_UF7                    = 71
    STOP_APPLICATION            = 128
    RUN_APPLICATION             = 129
    STEP_APPLICATION            = 130
    RESET_APPLICATION           = 131
    START_DOWNLOAD_MODE         = 132
    QUIT_DOWNLOAD_MODE          = 133
    READ_TMCL_MEMORY            = 134
    GET_APPLICATION_STATUS      = 135
    GET_FIRMWARE_VERSION        = 136
    RESTORE_FACTORY_SETTINGS    = 137
    TARGET_POSITION_REACHED     = 138
    RAMDEBUG                    = 142
    ASSIGNMENT                  = 143
    WRITE_MC                    = 146
    WRITE_DRV                   = 147
    READ_MC                     = 148
    READ_DRV                    = 149

    BOOT_ERASE_ALL              = 200
    BOOT_WRITE_BUFFER           = 201
    BOOT_WRITE_PAGE             = 202
    BOOT_GET_CHECKSUM           = 203
    BOOT_READ_MEMORY            = 204
    BOOT_START_APPL             = 205
    BOOT_GET_INFO               = 206
    BOOT_WRITE_LENGTH           = 208
    BOOT                        = 242

class TMCL_Status(object):
    SUCCESS               = 100
    COMMAND_LOADED        = 101
    WRONG_CHECKSUM        = 1
    INVALID_COMMAND       = 2
    WRONG_TYPE            = 3
    INVALID_VALUE         = 4
    EEPROM_LOCKED         = 5
    COMMAND_NOT_AVAILABLE = 6

    messages = {
        1: "Incorrect Checksum",
        2: "Invalid Command",
        3: "Wrong Type",
        4: "Invalid Value",
        5: "EEPROM Locked",
        6: "Command not Available"
    }

class TMCL_Request(TMCL):
    def __init__(self, address, command, commandType, motorBank, value, checksum=None):
        self.moduleAddress = address     & 0xFF
        self.command       = command     & 0xFF
        self.commandType   = commandType & 0xFF
        self.motorBank     = motorBank   & 0xFF
        self.value         = value       & 0xFFFFFFFF
        self.checksum      = checksum if checksum else 0

        if(checksum is None):
            self.calculate_checksum()

    @staticmethod
    def from_buffer(data):
        request_struct = struct.unpack(_PACKAGE_STRUCTURE, data)
        return TMCL_Request(request_struct[0], request_struct[1], request_struct[2], request_struct[3], request_struct[4], request_struct[5])

    def calculate_checksum(self):
        self.checksum = TMCL.calculate_checksum(self.toBuffer()[:-1])

    def toBuffer(self):
        return struct.pack(_PACKAGE_STRUCTURE, self.moduleAddress, self.command,
                           self.commandType, self.motorBank, self.value, self.checksum)

    def __str__(self):
        return "TMCL_Request: {0:02X},{1:02X},{2:02X},{3:02X},{4:08X},{5:02X}".format(
            self.moduleAddress,
            self.command,
            self.commandType,
            self.motorBank,
            self.value,
            self.checksum
        )

    def dump(self):
        print(self)

class TMCL_Reply(TMCL):
    def __init__(self, reply_address, module_address, status, command, value, checksum=None, special=False):
        self.reply_address  = reply_address  & 0xFF
        self.module_address = module_address & 0xFF
        self.status         = status         & 0xFF
        self.command        = command        & 0xFF
        self.value          = value          & 0xFFFFFFFF
        self.checksum       = checksum if checksum else 0
        self.special        = special

        if(checksum is None):
            self.calculate_checksum()

    @staticmethod
    def from_buffer(data):
        reply_struct = struct.unpack(_PACKAGE_STRUCTURE, data)
        return TMCL_Reply(reply_struct[0], reply_struct[1], reply_struct[2], reply_struct[3], reply_struct[4], reply_struct[5])

    def calculate_checksum(self):
        self.checksum = TMCL.calculate_checksum(self.toBuffer()[:-1])

    def toBuffer(self):
        return struct.pack(_PACKAGE_STRUCTURE, self.reply_address, self.module_address,
                           self.status, self.command, self.value, self.checksum)

    def __str__(self):
        return "TMCL_Reply:   {0:02X},{1:02X},{2:02X},{3:02X},{4:08X},{5:02X}".format(
            self.reply_address,
            self.module_address,
            self.status,
            self.command,
            self.value,
            self.checksum
        )

    def dump(self):
        print(self)

    def value(self):
        return self.value

    def isValid(self):
        return self.status == TMCL_Status.SUCCESS

    def versionString(self):
        byteString = struct.pack(">BBBIB", self.module_address, self.status, self.command, self.value, self.checksum)
        return str(byteString, "ascii")
