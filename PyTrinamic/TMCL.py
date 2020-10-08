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

class TMCL_Version_Format(object):
    ASCII = 0
    BINARY = 1
    BUILD = 5

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
    def __init__(self, address=None, command=None, commandType=None, motorBank=None, value=None, checksum=None, request_data=None):
        request_struct = None
        if(request_data):
            request_struct = struct.unpack(_PACKAGE_STRUCTURE, request_data)

        self.moduleAddress = (address if address else (request_struct[0] if request_struct else 0)) & 0xFF
        self.command       = (command if command else (request_struct[1] if request_struct else 0)) & 0xFF
        self.commandType   = (commandType if commandType else (request_struct[2] if request_struct else 0)) & 0xFF
        self.motorBank     = (motorBank if motorBank else (request_struct[3] if request_struct else 0)) & 0xFF
        self.value         = (value if value else (request_struct[4] if request_struct else 0)) & 0xFFFFFFFF
        self.checksum      = (checksum if checksum else (request_struct[5] if request_struct else 0))

        if(not(checksum) and(not(request_struct))):
            self.calculate_checksum()

    def calculate_checksum(self):
        self.checksum = TMCL.calculate_checksum(self.toBuffer()[:-1])

    def toBuffer(self):
        return struct.pack(_PACKAGE_STRUCTURE, self.moduleAddress, self.command,
                           self.commandType, self.motorBank, self.value, self.checksum)

    def dump(self):
        d = "TMCL_Request: {0:02X},{1:02X},{2:02X},{3:02X},{4:08X},{5:02X}".format(
                self.moduleAddress,
                self.command,
                self.commandType,
                self.motorBank,
                self.value,
                self.checksum
            )
        print(d)
        return d

class TMCL_Reply(TMCL):
    def __init__(self, reply_data=None, reply_address=None, module_address=None, status=None, command=None, value=None, checksum=None, special=False):
        reply_struct = None
        if(reply_data):
            reply_struct = struct.unpack(_PACKAGE_STRUCTURE, reply_data)

        self.reply_address = (reply_struct[0] if reply_struct else (reply_address if reply_address else 0)) & 0xFF
        self.module_address = (reply_struct[1] if reply_struct else (module_address if module_address else 0)) & 0xFF
        self.status = (reply_struct[2] if reply_struct else (status if status else 0)) & 0xFF
        self.command = (reply_struct[3] if reply_struct else (command if command else 0)) & 0xFF
        self.value = (reply_struct[4] if reply_struct else (value if value else 0)) & 0xFFFFFFFF
        self.checksum = (reply_struct[5] if reply_struct else (checksum if checksum else 0))
        self.special = special

        if(not(checksum) and(not(reply_struct))):
            self.calculate_checksum()

    def calculate_checksum(self):
        self.checksum = TMCL.calculate_checksum(self.toBuffer()[:-1])

    def toBuffer(self):
        return struct.pack(_PACKAGE_STRUCTURE, self.reply_address, self.module_address,
                           self.status, self.command, self.value, self.checksum)

    def dump(self):
        d = "TMCL_Reply:   {0:02X},{1:02X},{2:02X},{3:02X},{4:08X},{5:02X}".format(
                self.reply_address,
                self.module_address,
                self.status,
                self.command,
                self.value,
                self.checksum
            )
        print(d)
        return d

    def value(self):
        return self.value

    def isValid(self):
        return self.status == TMCL_Status.SUCCESS

    def versionString(self):
        byteString = struct.pack(">BBBIB", self.module_address, self.status, self.command, self.value, self.checksum)
        return str(byteString, "ascii")
