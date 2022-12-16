import logging
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

    def __str__(self):
        return "RegisterRequest: [Addr:{:02x}, Value:{}]".format(self.address, self.value)


class RegisterReply:
    def __init__(self, reply_struct):
        self.address = reply_struct[0]
        self.value = reply_struct[1]

    def __str__(self):
        return "RegisterReply:   [Addr:{:02x}, Value:{}]".format(self.address, self.value)

    def value(self):
        return self.value


class UartIcInterface:

    def __init__(self, com_port, datarate=9600, timeout_s=5):
        self.baudrate = datarate
        if timeout_s == 0:
            timeout_s = None

        self.logger = logging.getLogger("{}.{}".format(self.__class__.__name__, com_port))

        self.logger.debug("Opening port (baudrate=%s).", datarate)
        self.serial = Serial(com_port, self.baudrate, timeout=timeout_s)

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        """
        Close the connection at the end of a with-statement block.
        """
        del exit_type, value, traceback
        self.close()

    def close(self):
        self.logger.info("Closing port.")
        self.serial.close()

    def send_datagram(self, data, recv_size):
        self.serial.write(data)
        return self.serial.read(recv_size)

    @staticmethod
    def supports_tmcl():
        return False

    def send(self, address, value):
        # prepare TMCL request
        request = RegisterRequest(address, value)

        # send request, wait, and handle reply
        self.logger.debug("Tx %s", request)
        self.serial.write(request.to_buffer())
        reply = RegisterReply(struct.unpack(REGISTER_PACKAGE_STRUCTURE, self.serial.read(REGISTER_PACKAGE_LENGTH)))
        self.logger.debug("Rx %s", reply)

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