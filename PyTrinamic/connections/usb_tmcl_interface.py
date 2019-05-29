'''
Created on 29.05.2019

@author: LH
'''

import PyTrinamic
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface

class usb_tmcl_interface(serial_tmcl_interface):
    """
    Opens a USB TMCL connection.

    This class is almost the same as the class for serial TMCL connections.
    The only difference are the functions for the connection manager, which
    filter the available serial connections to only include the serial over
    USB ones.
    """
    def __init__(self, comPort, datarate=115200, hostID=2, moduleID=1, debug=False):
        serial_tmcl_interface.__init__(self, comPort, datarate, hostID, moduleID, debug)

    def printInfo(self):
        print("Connection: type=usb_tmcl_interface com=" + self._serial.portstr + " baud=" + str(self._baudrate))

    @staticmethod
    def list():
        """
            Return a list of available connection ports as a list of strings.

            This function is required for using this interface with the
            connection manager.
        """
        return PyTrinamic.getAvailableUSBPorts()