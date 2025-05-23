################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import logging

from ..connections.tmcl_interface import TmclInterface


class DummyTmclInterface(TmclInterface):

    def __init__(self, port, datarate=115200, host_id=2, module_id=1, timeout_s=5):
        """
        Opens a dummy TMCL connection
        """
        if not isinstance(port, str):
            raise TypeError

        TmclInterface.__init__(self, host_id, module_id)

        self.logger = logging.getLogger("{}.{}".format(self.__class__.__name__, port))

        self.logger.debug("Opening port (baudrate=%s).", datarate)

    def _send(self, host_id, module_id, data):
        """
            Send the bytearray parameter [data].

            This is a required override function for using the tmcl_interface
            class.
        """
        del host_id, module_id, data
        pass

    def _recv(self, host_id, module_id):
        """
            Read 9 bytes and return them as a bytearray.

            This is a required override function for using the tmcl_interface
            class.
        """
        del host_id, module_id

        return bytearray(9)

    @staticmethod
    def list():
        """
            Return a list of available connection ports as a list of strings.

            This function is required for using this interface with the
            connection manager.
        """
        return ["dummy"]

    def __str__(self):
        return "Connection: type={}".format(type(self).__name__)
