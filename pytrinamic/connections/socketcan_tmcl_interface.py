import can
from can import CanError
from ..connections.tmcl_interface import TmclInterface

_CHANNELS = ["can0",  "can1",  "can2",  "can3",  "can4",  "can5",  "can6",  "can7"]


class SocketcanTmclInterface(TmclInterface):
    """
    This class implements a TMCL connection over a SocketCAN adapter.

    Use following command under linux to activate can socket
    sudo ip link set can0 down type can bitrate 1000000
    """
    def __init__(self, port, datarate=1000000, host_id=2, module_id=1, debug=False):
        if not isinstance(port, str):
            raise TypeError

        if port not in _CHANNELS:
            raise ValueError("Invalid port")

        TmclInterface.__init__(self, host_id, module_id, debug)
        self._channel = port
        self._bitrate = datarate

        try:
            self._connection = can.Bus(interface="socketcan", channel=self._channel, bitrate=self._bitrate)
            self._connection.set_filters([{"can_id": host_id, "can_mask": 0x7F}])

        except CanError as e:
            self._connection = None
            raise ConnectionError("Failed to connect to SocketCAN bus") from e

        if self._debug:
            print("Opened bus on channel " + self._channel)

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        """
        Close the connection at the end of a with-statement block.
        """
        del exit_type, value, traceback
        self.close()

    def close(self):
        if self._debug:
            print("Closing socketcan bus")

        self._connection.shutdown()

    def _send(self, host_id, module_id, data):
        """
            Send the bytearray parameter [data].

            This is a required override function for using the tmcl_interface
            class.
        """
        del host_id

        msg = can.Message(arbitration_id=module_id, is_extended_id=False, data=data[1:])

        try:
            self._connection.send(msg)
        except CanError as e:
            raise ConnectionError("Failed to send a TMCL message") from e

    def _recv(self, host_id, module_id):
        """
            Read 9 bytes and return them as a bytearray.

            This is a required override function for using the tmcl_interface
            class.
        """
        del module_id

        try:
            msg = self._connection.recv(timeout=3)
        except CanError as e:
            raise ConnectionError("Failed to receive a TMCL message") from e

        if not msg:
            # Todo: Timeout retry mechanism
            raise ConnectionError("Recv timed out")

        if msg.arbitration_id != host_id:
            # The filter shouldn't let wrong messages through.
            # This is just a sanity check
            raise ConnectionError("Received wrong ID")

        return bytearray([msg.arbitration_id]) + msg.data

    @staticmethod
    def supports_tmcl():
        return True

    @staticmethod
    def list():
        """
            Return a list of available connection ports as a list of strings.

            This function is required for using this interface with the
            connection manager.
        """
        return _CHANNELS

    def __str__(self):
        return "Connection: type={} channel={} bitrate={}".format(type(self).__name__, self._channel, self._bitrate)
