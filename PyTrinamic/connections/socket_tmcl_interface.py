'''
Created on 05.08.2020

@author: SW

'''

import can

from PyTrinamic.connections.tmcl_interface import tmcl_interface
import json
import re
import socket

_CHANNELS = [
    "127.0.0.1:60000"
    ]

class socket_tmcl_interface(tmcl_interface):
    """
    This class implements a TMCL connection over a Socket.
    """

    def __init__(self, port, datarate=0, hostID=2, moduleID=1, debug=False):
        if type(port) != str:
            raise TypeError

        match = re.match('^"?((?:[0-9]{1,3}\.){3}[0-9]{1,3}):([0-9]{1,5})"?$', port)

        if match is None:
            raise ValueError("Invalid port")

        self.socket_ip = match.group(1)
        self.socket_port = int(match.group(2))

        tmcl_interface.__init__(self, hostID, moduleID, debug)

        self.__debug    = debug
        self.__channel  = port
        self.__bitrate  = datarate

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.socket_ip, self.socket_port))
        except socket.error as e:
            self.__connection = None
            raise ConnectionError("Failed to connect to Socket") from e

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
            print("Closing Socket Connection")

        self.socket.close()

    def _send(self, hostID, moduleID, data):
        """
            Send the bytearray parameter [data].

            This is a required override function for using the tmcl_interface
            class.
        """
        del hostID, moduleID
        self.socket.sendall(data)        

    def _recv(self, hostID, moduleID):
        data = self.socket.recv(9)
        print(data)
        
        return data

    def printInfo(self):
        print("Connection: type=socket_tmcl_interface ip=" + self.socket_ip + " port=" + str(self.socket_port))

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
