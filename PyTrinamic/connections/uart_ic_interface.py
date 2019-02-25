'''
Created on 03.01.2019

@author: ED
'''

import struct
from serial import Serial
from PyTrinamic.helpers import TMC_helpers
from PyTrinamic.connections.connection_interface import connection_interface

REGISTER_PACKAGE_STRUCTURE   = ">BI"
REGISTER_PACKAGE_LENGTH      = 5

class Register_Request(object):
    def __init__(self, address, value):
        self.address = address
        self.value = value & 0xFFFFFFFF

    def toBuffer(self):
        return struct.pack(REGISTER_PACKAGE_STRUCTURE, self.address, self.value)
   
    def dump(self): 
        print("Register_Request: " + str(self.address) + "," + str(self.value))

class Register_Reply(object):
    def __init__(self, reply_struct):
        self.address = reply_struct[0]
        self.value = reply_struct[1]

    def dump(self): 
        print("Register_Reply:   " + str(self.address) + "," + str(self.value))

    def value(self):
        return self.value

    def valueLower16Bit(self):
        return (self.value) & 0xFFFF
    
    def valueUpper16Bit(self):
        return (self.value>>16) & 0xFFFF
    
class uart_ic_interface(connection_interface):

    def __init__(self, comPort):
        self.debugEnabled = False
        self.baudrate = 9600
        self.serial = Serial(comPort, self.baudrate)
        print("Open port: " + self.serial.portstr)
        
    def printInfo(self):
        print("Connection: type=uart_ic_interface com=" + self.serial.portstr + " baud=" + str(self.baudrate))
        
    def close( self ):
        print("Close port: " + self.serial.portstr)
        self.serial.close()
        return 0;
    
    def enableDebug(self, enable):
        self.debugEnabled = enable

    def send ( self, address, value ):
       
        "prepare TMCL request"
        request = Register_Request(address, value)
        
        if self.debugEnabled:
            request.dump()
        
        "send request, wait, and handle reply"
        self.serial.write(request.toBuffer())
        reply = Register_Reply(struct.unpack(REGISTER_PACKAGE_STRUCTURE, self.serial.read(REGISTER_PACKAGE_LENGTH)))
        
        if self.debugEnabled:
            reply.dump()

        return reply

    " direct register access "
    def writeRegister(self, registerAddress, value):
        return self.send(registerAddress | 0x80, value)
    
    def readRegister(self, registerAddress):
        return self.send(registerAddress, 0).value
    
    def writeRegisterField(self, registerAddress, value, mask, shift):
        return self.writeRegister(registerAddress, TMC_helpers.field_set(self.readRegister(registerAddress), mask, shift, value))
    
    def readRegisterField(self, registerAddress, mask, shift):
        return TMC_helpers.field_get(self.readRegister(registerAddress), mask, shift)
