'''
Created on 30.12.2018

@author: ED
'''

from serial import Serial, SerialException
import serial.tools.list_ports;

from PyTrinamic.connections.tmcl_interface import tmcl_interface

class serial_tmcl_interface(tmcl_interface):

    DEFAULT_DATA_RATE = 115200
    DEFAULT_HOST_ID = 2
    DEFAULT_MODULE_ID = 1

    """
    Opens a serial TMCL connection
    """
    def __init__(self, port, data_rate=None, host_id=None, module_id=None, debug=False):
        if type(port) != str:
            raise TypeError;

        super().__init__(port, data_rate, host_id, module_id, debug)

        self._baudrate = self._DATA_RATE

        try:
            self._serial = Serial(port, self._baudrate)
        except SerialException as e:
            raise ConnectionError from e

        if self._debug:
            print("Open port: " + self._serial.portstr)

    def __enter__(self):
        return self

    def __exit__(self, exitType, value, traceback):
        """
        Close the connection at the end of a with-statement block.
        """
        del exitType, value, traceback
        self.close()

    def close(self):
        if self._debug:
            print("Close port: " + self._serial.portstr)

        self._serial.close()
        return 0;

    def _send(self, hostID, moduleID, data):
        """
            Send the bytearray parameter [data].

            This is a required override function for using the tmcl_interface
            class.
        """
        del hostID, moduleID

        self._serial.write(data)

    def _recv(self, hostID, moduleID):
        """
            Read 9 bytes and return them as a bytearray.

            This is a required override function for using the tmcl_interface
            class.
        """
        del hostID, moduleID

        return self._serial.read(9)

    def printInfo(self):
        print("Connection: type=serial_tmcl_interface com=" + self._serial.portstr + " baud=" + str(self._baudrate))

    def enableDebug(self, enable):
        self._debug = enable

    @staticmethod
    def supportsTMCL():
        return True

    @staticmethod
    def supportsCANopen():
        return False

    @staticmethod
    def available_ports():
        """
            Return a set of available connection ports as a list of strings.

            This function is required for using this interface with the
            connection manager.
        """

        return { port.device for port in sorted(serial.tools.list_ports.comports()) }
