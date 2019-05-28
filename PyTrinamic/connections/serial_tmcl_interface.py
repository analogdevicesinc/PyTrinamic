'''
Created on 30.12.2018

@author: ED
'''

from serial import Serial
from PyTrinamic.connections.tmcl_interface import tmcl_interface

class serial_tmcl_interface(tmcl_interface):

    def __init__(self, comPort, baudrate=115200, hostID=2, moduleID=1, debug=False):
        if type(comPort) != str:
            raise TypeError;

        tmcl_interface.__init__(self, hostID, moduleID, debug)

        self.__baudrate = baudrate

        self.__serial = Serial(comPort, self.__baudrate)
        if self._debug:
            print("Open port: " + self.__serial.portstr)

    # Overridden functions for the tmcl_interface
    def _send(self, hostID, moduleID, data):
        del hostID, moduleID

        self.__serial.write(data)

    def _recv(self, hostID, moduleID):
        del hostID, moduleID

        return self.__serial.read(9)

    def printInfo(self):
        print("Connection: type=serial_tmcl_interface com=" + self.__serial.portstr + " baud=" + str(self.baudrate))

    def close(self):
        if self._debug:
            print("Close port: " + self.__serial.portstr)

        self.__serial.close()
        return 0;

    def enableDebug(self, enable):
        self._debug = enable
