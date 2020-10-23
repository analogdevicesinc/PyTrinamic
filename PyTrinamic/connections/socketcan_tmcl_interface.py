'''
Created on 03.01.2020

@author: SW

Use following command under linux to activate can socket
sudo ip link set can0 down type can bitrate 1000000

'''

import can

from PyTrinamic.connections.tmcl_interface import tmcl_interface
from can import CanError

_CHANNELS = {
    "can0",  "can1",  "can2",  "can3",  "can4",  "can5",  "can6",  "can7"
}

class socketcan_tmcl_interface(tmcl_interface):
    """
    This class implements a TMCL connection over a SocketCAN adapter.
    """

    DEFAULT_DATA_RATE = 1000000
    DEFAULT_HOST_ID = 2
    DEFAULT_MODULE_ID = 1

    def __init__(self, port, data_rate=1000000, host_id=2, module_id=1, debug=False):
        if type(port) != str:
            raise TypeError

        if not port in _CHANNELS:
            raise ValueError("Invalid port")

        super().__init__(host_id, module_id, debug)

        self.__debug    = debug
        self.__channel  = port
        self.__bitrate  = data_rate

        try:
            self.__connection = can.Bus(interface="socketcan", channel=self.__channel, bitrate=self.__bitrate)

            self.__connection.set_filters([{ "can_id": host_id, "can_mask": 0x7F }])

        except CanError as e:
            self.__connection = None
            raise ConnectionError("Failed to connect to SocketCAN bus") from e

        if self.__debug:
            print("Opened bus on channel " + self.__channel)

    def __enter__(self):
        return self

    def __exit__(self, exitType, value, traceback):
        """
        Close the connection at the end of a with-statement block.
        """
        del exitType, value, traceback
        self.close()

    def close(self):
        if self.__debug:
            print("Closing PCAN bus")

        self.__connection.shutdown()

    def _send(self, hostID, moduleID, data):
        """
            Send the bytearray parameter [data].

            This is a required override function for using the tmcl_interface
            class.
        """
        del hostID

        msg = can.Message(arbitration_id=moduleID, is_extended_id=False, data=data[1:])

        try:
            self.__connection.send(msg)
        except CanError as e:
            raise ConnectionError("Failed to send a TMCL message") from e


    def _recv(self, hostID, moduleID):
        """
            Read 9 bytes and return them as a bytearray.

            This is a required override function for using the tmcl_interface
            class.
        """
        del moduleID



        try:
            msg = self.__connection.recv(timeout=3)
        except CanError as e:
            raise ConnectionError("Failed to receive a TMCL message") from e

        if not msg:
            # Todo: Timeout retry mechanism
            raise ConnectionError("Recv timed out")

        if msg.arbitration_id != hostID:
            # The filter shouldn't let wrong messages through.
            # This is just a sanity check
            raise ConnectionError("Received wrong ID")

        return bytearray([msg.arbitration_id]) + msg.data

    def printInfo(self):
        print("Connection: type=pcan_tmcl_interface channel=" + self.__channel + " bitrate=" + str(self.__bitrate))

    def enableDebug(self, enable):
        self.__debug = enable

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
        return _CHANNELS
