'''
Created on 13.02.2020

@author: JM
'''
#import canopen
from PyTrinamic.connections.CANopen_interface import CANopen_interface
#from canopen import import CanError

_CHANNELS = {
    "0",  "1",  "2",  "3"
}

class kvaser_CANopen_interface(CANopen_interface):

    DEFAULT_DATA_RATE = 0

    def __init__(self, port, data_rate=None, debug=False):
        if not port in _CHANNELS:
            raise ValueError("Invalid port")

        super().__init__("kvaser", int(port), data_rate, debug=debug)

        self.__channel = str(port)
        self.__bitrate = self._DATA_RATE

    def printInfo(self):
        print("Connection: type=kvaser_CANopen_interface channel=" + self.__channel + " bitrate=" + str(self.__bitrate))

    @staticmethod
    def supportsTMCL():
        return False

    @staticmethod
    def supportsCANopen():
        return True

    @staticmethod
    def available_ports():
        """
            Return a set of available connection ports as a list of strings.

            This function is required for using this interface with the
            connection manager.
        """


        #num_channels = ctypes.c_int(0)
        #res = canGetNumberOfChannels(ctypes.byref(num_channels))
        #num_channels = int(num_channels.value)
        #print(res)
        #print(num_channels)


        return _CHANNELS #range(num_channels)

if __name__ == "__main__":
    available_ports()
