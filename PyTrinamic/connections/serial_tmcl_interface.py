'''
Created on 30.12.2018

@author: ED
'''

from serial import Serial
from serial import SerialException
import PyTrinamic
from PyTrinamic.connections.tmcl_interface import tmcl_interface

class serial_tmcl_interface(tmcl_interface):
    """
    Opens a serial TMCL connection
    """
    def __init__(self, comPort, datarate=115200, hostID=2, moduleID=1, debug=False):
        if type(comPort) != str:
            raise TypeError;

        tmcl_interface.__init__(self, hostID, moduleID, debug)

        self._baudrate = datarate

        try:
            self._serial = Serial(comPort, self._baudrate)
        except SerialException as e:
            raise ConnectionError from e

        if self._debug:
            print("Open port: " + self._serial.portstr)

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
    def list():
        """
            Return a list of available connection ports as a list of strings.

            This function is required for using this interface with the
            connection manager.
        """
        return PyTrinamic.getAvailableSerialPorts()