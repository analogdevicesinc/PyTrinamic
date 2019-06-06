'''
Created on 31.05.2019

@author: LH
'''

import can

from PyTrinamic.connections.tmcl_interface import tmcl_interface
from can.interfaces.pcan.pcan import PcanError
from can import CanError

_CHANNELS = [
    "PCAN_USBBUS1",  "PCAN_USBBUS2",  "PCAN_USBBUS3",  "PCAN_USBBUS4",
    "PCAN_USBBUS5",  "PCAN_USBBUS6",  "PCAN_USBBUS7",  "PCAN_USBBUS8",
    "PCAN_USBBUS9",  "PCAN_USBBUS10", "PCAN_USBBUS11", "PCAN_USBBUS12",
    "PCAN_USBBUS13", "PCAN_USBBUS14", "PCAN_USBBUS15", "PCAN_USBBUS16",

    "PCAN_ISABUS1",  "PCAN_ISABUS2",  "PCAN_ISABUS3",  "PCAN_ISABUS4",
    "PCAN_ISABUS5",  "PCAN_ISABUS6",  "PCAN_ISABUS7",  "PCAN_ISABUS8",

    "PCAN_DNGBUS1",

    "PCAN_PCIBUS1",  "PCAN_PCIBUS2",  "PCAN_PCIBUS3",  "PCAN_PCIBUS4",
    "PCAN_PCIBUS5",  "PCAN_PCIBUS6",  "PCAN_PCIBUS7",  "PCAN_PCIBUS8",
    "PCAN_PCIBUS9",  "PCAN_PCIBUS10", "PCAN_PCIBUS11", "PCAN_PCIBUS12",
    "PCAN_PCIBUS13", "PCAN_PCIBUS14", "PCAN_PCIBUS15", "PCAN_PCIBUS16",

    "PCAN_PCCBUS1",  "PCAN_PCCBUS2",

    "PCAN_LANBUS1",  "PCAN_LANBUS2",  "PCAN_LANBUS3",  "PCAN_LANBUS4",
    "PCAN_LANBUS5",  "PCAN_LANBUS6",  "PCAN_LANBUS7",  "PCAN_LANBUS8",
    "PCAN_LANBUS9",  "PCAN_LANBUS10", "PCAN_LANBUS11", "PCAN_LANBUS12",
    "PCAN_LANBUS13", "PCAN_LANBUS14", "PCAN_LANBUS15", "PCAN_LANBUS16"
    ]

class pcan_tmcl_interface(tmcl_interface):
    """
    This class implements a TMCL connection over a PCAN adapter.
    """

    def __init__(self, port, datarate=1000000, hostID=2, moduleID=1, debug=False):
        if type(port) != str:
            raise TypeError

        if not port in _CHANNELS:
            raise ValueError("Invalid port")

        tmcl_interface.__init__(self, hostID, moduleID, debug)

        self.__debug    = debug
        self.__channel  = port
        self.__bitrate  = datarate

        try:
            self.__connection = can.Bus(interface="pcan", channel=self.__channel, bitrate=self.__bitrate)

            self.__connection.set_filters([{ "can_id": hostID, "can_mask": 0xFFFFFFFF }])

        except PcanError as e:
            self.__connection = None
            raise ConnectionError("Failed to connect to PCAN bus") from e

        if self.__debug:
            print("Opened bus on channel " + self.__channel)

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
    def list():
        """
            Return a list of available connection ports as a list of strings.

            This function is required for using this interface with the
            connection manager.
        """
        return _CHANNELS
