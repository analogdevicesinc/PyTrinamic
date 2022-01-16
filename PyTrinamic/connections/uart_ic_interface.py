import struct
from serial import Serial
import serial.tools.list_ports
from PyTrinamic.helpers import TMC_helpers

REGISTER_PACKAGE_STRUCTURE = ">BI"
REGISTER_PACKAGE_LENGTH = 5


class RegisterRequest:
    def __init__(self, address, value):
        self.address = address
        self.value = value & 0xFFFFFFFF

    def to_buffer(self):
        return struct.pack(REGISTER_PACKAGE_STRUCTURE, self.address, self.value)

    def dump(self):
        print("Register_Request: " + str(self.address) + "," + str(self.value))


class RegisterReply:
    def __init__(self, reply_struct):
        self.address = reply_struct[0]
        self.value = reply_struct[1]

    def dump(self):
        print("Register_Reply:   " + str(self.address) + "," + str(self.value))

    def value(self):
        return self.value


class uart_ic_interface:

    def __init__(self, com_port, datarate=9600, debug=False):
        self.debugEnabled = debug
        self.baudrate = datarate
        self.serial = Serial(com_port, self.baudrate)
        print("Open port: " + self.serial.portstr)

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        """
        Close the connection at the end of a with-statement block.
        """
        del exit_type, value, traceback
        self.close()

    def send_datagram(self, data, recv_size, channel):
        del channel
        self.serial.write(data)
        return self.serial.read(recv_size)

    def print_info(self):
        print("Connection: type=uart_ic_interface com=" + self.serial.portstr + " baud=" + str(self.baudrate))

    def close( self ):
        print("Close port: " + self.serial.portstr)
        self.serial.close()
        return 0

    def enable_debug(self, enable):
        self.debugEnabled = enable

    def send(self, address, value):

        "prepare TMCL request"
        request = RegisterRequest(address, value)

        if self.debugEnabled:
            request.dump()

        "send request, wait, and handle reply"
        self.serial.write(request.to_buffer())
        reply = RegisterReply(struct.unpack(REGISTER_PACKAGE_STRUCTURE, self.serial.read(REGISTER_PACKAGE_LENGTH)))

        if self.debugEnabled:
            reply.dump()

        return reply

    " direct register access "
    def writeRegister(self, register_address, value):
        return self.send_receive(register_address | 0x80, value)

    def readRegister(self, register_address):
        return self.send_receive(register_address, 0).value

    def writeRegisterField(self, register_address, value, mask, shift):
        return self.writeRegister(register_address, TMC_helpers.field_set(self.readRegister(register_address), mask,
                                                                          shift, value))

    def readRegisterField(self, register_address, mask, shift):
        return TMC_helpers.field_get(self.readRegister(register_address), mask, shift)

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
