import struct
from serial import Serial
import serial.tools.list_ports

REGISTER_PACKAGE_STRUCTURE = ">BI"
REGISTER_PACKAGE_LENGTH = 5


class RegisterRequest:
    def __init__(self, address, value):
        self.address = address
        self.value = value & 0xFFFFFFFF

    def to_buffer(self):
        return struct.pack(REGISTER_PACKAGE_STRUCTURE, self.address, self.value)

    def dump(self):
        print("RegisterRequest: " + str(self.address) + "," + str(self.value))


class RegisterReply:
    def __init__(self, reply_struct):
        self.address = reply_struct[0]
        self.value = reply_struct[1]

    def dump(self):
        print("RegisterReply:   " + str(self.address) + "," + str(self.value))

    def value(self):
        return self.value


class UartIcInterface:

    def __init__(self, com_port, datarate=9600, debug=False):
        self._debug = debug
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

    def close(self):
        if self._debug:
            print("Close port: " + self.serial.portstr)

        self.serial.close()

    def send_datagram(self, data, recv_size):
        self.serial.write(data)
        return self.serial.read(recv_size)

    def enable_debug(self, enable):
        self._debug = enable

    @staticmethod
    def supports_tmcl():
        return False

    def send(self, address, value):
        # prepare TMCL request
        request = RegisterRequest(address, value)

        if self._debug:
            request.dump()

        # send request, wait, and handle reply
        self.serial.write(request.to_buffer())
        reply = RegisterReply(struct.unpack(REGISTER_PACKAGE_STRUCTURE, self.serial.read(REGISTER_PACKAGE_LENGTH)))

        if self._debug:
            reply.dump()

        return reply

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

    def __str__(self):
        return "Connection: type={} port={} baudrate={}".format(type(self).__name__, self.serial.portstr, self.baudrate)