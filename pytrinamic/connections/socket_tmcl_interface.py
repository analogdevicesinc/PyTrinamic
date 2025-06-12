################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Serial socket interface"""

import logging
import time
import re
import socket

from .tmcl_interface import TmclInterface
from ..tmcl import TMCLReplyChecksumError


class SocketTmclInterface(TmclInterface):
    """
    This class implements a TMCL connection over a Socket, for use with e.g. an Ethernet-to-Serial converter further down the line.

    Note, with the current implementation only one Ethernet-to-Serial converter can be used at a time.
    """

    _socket = None

    def __init__(
        self,
        ip_and_port: str,
        baudrate: None = None,
        host_id: int = 2,
        module_id: int = 1,
        timeout_s: int = 5,
    ) -> None:
        del baudrate

        if not isinstance(ip_and_port, str):
            raise TypeError

        match = re.match(
            r'^"?((?:[0-9]{1,3}\.){3}[0-9]{1,3}):([0-9]{1,5})"?$', ip_and_port
        )
        if match is None:
            raise ValueError("Invalid ip:port combination")

        self._socket_ip = match.group(1)
        self._socket_port = int(match.group(2))
        TmclInterface.__init__(self, host_id, module_id)

        if timeout_s == 0:
            timeout_s = None

        self.logger = logging.getLogger(
            "{}.{}".format(self.__class__.__name__, ip_and_port)
        )

        self.logger.debug("Opening %s:%s.", self._socket_ip, self._socket_port)
        self._check_socket() # connect to the socket
        self._timeout_s = timeout_s

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

    def close(self):
        self.logger.info("Closing Socket connection.")
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

        data = bytearray()
        start_time = time.time()
        while len(data) < 9:
            packet = self._socket.recv(9 - len(data))
            if not packet:
                if time.time() - start_time > self._timeout_s:
                    raise TimeoutError("No reply received within timeout")
            data.extend(packet)

        return data

    def _reply_check(self, reply):
        if not reply.is_checksum_correct():
            raise TMCLReplyChecksumError(reply)

    def set_timeout(self, timeout):
        self._timeout_s = timeout

    def get_timeout(self):
        return self._timeout_s

    @staticmethod
    def list():
        return []

    def __str__(self):
        return "Connection: type={} ip={} port={}".format(type(self).__name__, self._socket_ip, self._socket_port)
