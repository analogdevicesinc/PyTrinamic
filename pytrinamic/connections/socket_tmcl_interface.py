"""
Created on 05.08.2020

@author: SW
BRP mod: Found this code on https://github.com/trinamic/PyTrinamic/blob/11c36a3d8d8333c1f21c7daee4e62eb4ff43892e/PyTrinamic/connections/socket_tmcl_interface.py
Seems to be a dead branch left by someone else, but implementing what I need. 
Adapting it to follow the structure of serial_tmcl_interface.py and socketcan_tmcl_interface.py
"""

import logging
from .tmcl_interface import TmclInterface
from ..tmcl import TMCLReplyChecksumError
import re
import socket


class SocketTmclInterface(TmclInterface):
    """
    This class implements a TMCL connection over a Socket, for use with e.g. an ethernet-to-serial converter further down the line.
    """

    _CHANNELS = []
    _socket = None

    # mod from socketcan_tmcl_interface.py and serial_tmcl_interface.py
    def __init__(
        self,
        ip_and_port: str,
        datarate: int = 1000000,
        host_id: int = 2,
        module_id: int = 1,
        timeout_s: int = 5,
    ):
        if not isinstance(ip_and_port, str):
            raise TypeError

        match = re.match(
            '^"?((?:[0-9]{1,3}\.){3}[0-9]{1,3}):([0-9]{1,5})"?$', ip_and_port
        )
        if match is None:
            raise ValueError("Invalid ip:port combination")

        self._socket_ip = match.group(1)
        self._socket_port = int(match.group(2))
        self._CHANNELS += [ip_and_port]
        TmclInterface.__init__(self, host_id, module_id)

        if timeout_s == 0:
            timeout_s = None

        self.logger = logging.getLogger(
            "{}.{}".format(self.__class__.__name__, ip_and_port)
        )

        self.logger.debug(
            f"Opening {self._socket_ip=} {self._socket_port=} for TMCL control"
        )
        self._check_socket()  # connect to the socket
        self.set_timeout(timeout_s)

    def _check_socket(self):
        """
        Check if the socket is still open. If not, try to reconnect. Not sure it is necessary here, but it helped in the past.
        """
        if self._socket is None:
            try:
                self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self._socket.connect((self._socket_ip, self._socket_port))
            except socket.error as e:
                self._connection = None
                raise ConnectionError(
                    "Failed to (re-)connect to Socket connection"
                ) from e

    def __enter__(self):
        return self

    def __exit__(self, exitType, value, traceback):
        """
        Close the connection at the end of a with-statement block.
        """
        del exitType, value, traceback
        self.close()

    def close(self):
        self.logger.info("Closing Socket Connection")
        self._socket.close()

    def _send(self, host_id, module_id, data):
        """
        Send the bytearray parameter [data].

        This is a required override function for using the tmcl_interface
        class.
        """
        del host_id, module_id
        self._check_socket()
        self._socket.sendall(data)

    def _recv(self, host_id, module_id):
        """
        Read 9 bytes and return them as a bytearray.

        This is a required override function for using the tmcl_interface
        class.
        """
        del host_id, module_id
        self._check_socket()
        data = self._socket.recv(9)
        if len(data) != 9:
            raise RuntimeError("TMCL datagram timed out")

        return data

    def _reply_check(self, reply):
        if not reply.is_checksum_correct():
            raise TMCLReplyChecksumError(reply)

    def set_timeout(self, timeout):
        self._socket.settimeout(timeout) if timeout != 0 else None

    def get_timeout(self):
        return self._socket.gettimeout()

    @staticmethod
    def supports_tmcl():
        return True

    @classmethod
    def list(cls):
        """
        Return a list of available connection ports as a list of strings.

        This function is required for using this interface with the
        connection manager.
        """
        return cls._CHANNELS

    def __str__(self):
        print(
            "Connection: type=socket_tmcl_interface ip="
            + self._socket_ip
            + " port="
            + str(self._socket_port)
        )
