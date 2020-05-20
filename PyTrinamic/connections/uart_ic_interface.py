'''
Created on 03.01.2019

@author: ED
'''

import struct
from serial import Serial
import serial.tools.list_ports;
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

class uart_ic_interface(connection_interface):

    def __init__(self, comPort, datarate=9600, debug=False):
        self.debugEnabled = debug
        self.baudrate = datarate
        self.serial = Serial(comPort, self.baudrate)
        print("Open port: " + self.serial.portstr)

    def __enter__(self):
        return self

    def __exit__(self, exitType, value, traceback):
        """
        Close the connection at the end of a with-statement block.
        """
        del exitType, value, traceback
        self.close()

    def send_datagram(self, data, recv_size , channel):
        del channel
        self.serial.write(data)
        return self.serial.read(recv_size)

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

    @staticmethod
    def supportsTMCL():
        return False

    @staticmethod
    def supportsCANopen():
        return False

    @staticmethod
    def list():
        """
            Return a list of available connection ports as a list of strings.

            This function is required for using this interface with the
            connection manager.
        """
        connected = []
        for element in sorted(serial.tools.list_ports.comports()):
            connected.append(element.device)

        return connected
