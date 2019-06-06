'''
Created on 16.02.2018

@author: TS, ED
'''

import struct

class TMCL:
    PACKAGE_STRUCTURE   = ">BBBBIB"

class TMCL_Command:
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

class TMCL_Status (object):
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

class TMCL_Request(object):
    def __init__(self, address, command, commandType, motorBank, value):
        self.moduleAddress = address
        self.command = command
        self.commandType = commandType
        self.motorBank = motorBank
        self.value = value & 0xFFFFFFFF
        self.checksum = 0
        checksum_struct = struct.pack(TMCL.PACKAGE_STRUCTURE[:-1], address, command, commandType, motorBank, value & 0xFFFFFFFF)
        for s in checksum_struct:
            self.checksum += s
        self.checksum %= 256

    def toBuffer(self):
        return struct.pack(TMCL.PACKAGE_STRUCTURE, self.moduleAddress, self.command,
                           self.commandType, self.motorBank, self.value, self.checksum)

    def dump(self):
        print("TMCL_Request: {0:02X},{1:02X},{2:02X},{3:02X},{4:08X},{5:02X}"
            .format(
                self.moduleAddress,
                self.command,
                self.commandType,
                self.motorBank,
                self.value,
                self.checksum
            )
        )

class TMCL_Reply(object):
    def __init__(self, reply_data):
        reply_struct = struct.unpack(TMCL.PACKAGE_STRUCTURE, reply_data)
        self.reply_address = reply_struct[0]
        self.module_address = reply_struct[1]
        self.status = reply_struct[2]
        self.command = reply_struct[3]
        self.value = reply_struct[4]
        self.checksum = reply_struct[5]

    def dump(self):
        print("TMCL_Reply:   {0:02X},{1:02X},{2:02X},{3:02X},{4:08X},{5:02X}"
            .format(
                self.reply_address,
                self.module_address,
                self.status,
                self.command,
                self.value,
                self.checksum
            )
        )

    def value(self):
        return self.value

    def versionString(self):
        byteString = struct.pack(">BBBIB", self.module_address, self.status, self.command, self.value, self.checksum)
        return str(byteString, "ascii")
