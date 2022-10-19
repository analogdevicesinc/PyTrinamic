import can
from can import CanError
from ...connections.can_tmcl_interface import CanTmclInterface


class SocketcanTmclInterface(CanTmclInterface):
    """
    This class implements a TMCL connection over a SocketCAN adapter.

    Use following command under linux to activate can socket
    sudo ip link set can0 down type can bitrate 1000000
    """
    _CHANNELS = ["can0",  "can1",  "can2",  "can3",  "can4",  "can5",  "can6",  "can7"]

    def __init__(self, port, datarate=1000000, host_id=2, module_id=1, debug=False, timeout_s=5):
        if not isinstance(port, str):
            raise TypeError

        if port not in self._CHANNELS:
            raise ValueError("Invalid port")

        CanTmclInterface.__init__(self, host_id, module_id, debug, timeout_s)
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

    @classmethod
    def list(cls):
        """
            Return a list of available connection ports as a list of strings.

            This function is required for using this interface with the
            connection manager.
        """
        return cls._CHANNELS
