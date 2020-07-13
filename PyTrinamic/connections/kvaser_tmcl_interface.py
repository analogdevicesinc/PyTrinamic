'''
Created on 03.01.2020

@author: JH



'''
import can
from PyTrinamic.connections.tmcl_interface import tmcl_interface
from can import CanError

_CHANNELS = [
     "0",  "1",  "2",
     ]

class kvaser_tmcl_interface(tmcl_interface):
    """
    This class implements a TMCL connection for Kvaser adapter using CANLIB.
    Try 0 as default channel.
    """

    def __init__(self, port = 0, datarate=1000000, hostID=2, moduleID=1, debug=False):
        if type(port) != str:
            raise TypeError

        if not port in _CHANNELS:
            raise ValueError("Invalid port")
        
        tmcl_interface.__init__(self, hostID, moduleID, debug)

        self.__debug    = debug
        self.__channel  = port
        self.__bitrate  = datarate

        try:
            if self.__debug:
                self.__connection = can.Bus(interface="kvaser", channel=self.__channel, bitrate=self.__bitrate)
            else:
                self.__connection = can.Bus(interface="kvaser", channel=self.__channel, bitrate=self.__bitrate,can_filters=[{ "can_id": hostID, "can_mask": 0x7F }])

        except CanError as e:
            self.__connection = None
            raise ConnectionError("Failed to connect to Kvaser CAN bus") from e

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
            print("Closing CAN bus")

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
            if self.__debug:
                print ("Received wrong ID")

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
    def list():
        """
            Return a list of available connection ports as a list of strings.

            This function is required for using this interface with the
            connection manager.
        """
        return _CHANNELS
