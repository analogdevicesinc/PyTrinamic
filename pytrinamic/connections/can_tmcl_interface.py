
import logging
import can
from ..connections.tmcl_interface import TmclInterface


class CanTmclInterface(TmclInterface):
    """Generic CAN interface class for the CAN adapters."""

    def __init__(self, channel, datarate, host_id, default_module_id, timeout_s):

        TmclInterface.__init__(self, host_id, default_module_id)
        self._connection = None
        self._channel = channel
        self._bitrate = datarate
        if timeout_s == 0:
            self._timeout_s = None
        else:
            self._timeout_s = timeout_s

        self.logger = logging.getLogger(f"{self.__class__.__name__}.{self._channel}")

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        """
        Close the connection at the end of a with-statement block.
        """
        del exit_type, value, traceback
        self.close()

    def close(self):
        self.logger.info("Shutdown.")

        self._connection.shutdown()

    def _send(self, host_id, module_id, data):
        """
        Send the bytearray parameter [data].

        This is a required override function for using the tmcl_interface class.
        """
        del host_id

        msg = can.Message(arbitration_id=module_id, is_extended_id=False, data=data[1:])

        try:
            self._connection.send(msg)
        except can.CanError as e:
            raise ConnectionError(
                f"Failed to send a TMCL message on {self.__class__.__name__} (channel {str(self._channel)})"
            ) from e

    def _recv(self, host_id, module_id):
        """
        Read 9 bytes and return them as a bytearray.

        This is a required override function for using the tmcl_interface class.
        """
        del module_id

        try:
            msg = self._connection.recv(timeout=self._timeout_s)
        except can.CanError as e:
            raise ConnectionError(
                f"Failed to receive a TMCL message from {self.__class__.__name__} (channel {str(self._channel)})"
            ) from e

        if not msg:
            raise ConnectionError(f"Recv timed out ({self.__class__.__name__}, on channel {str(self._channel)})")

        if msg.arbitration_id != host_id:
            # The filter shouldn't let wrong messages through.
            # This is just a sanity check
            self.logger.warning("Received a CAN Frame with unexpected ID (received: %d; expected: %d)", msg.arbitration_id, host_id)

        return bytearray([msg.arbitration_id]) + msg.data

    @staticmethod
    def supports_tmcl():
        return True

    def __str__(self):
        return f"Connection: Type = {self.__class__.__name__}, Channel = {self._channel}, Bitrate = {self._bitrate}"
