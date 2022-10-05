import can
from ..connections.can_tmcl_interface import CanTmclInterface


class KvaserTmclInterface(CanTmclInterface):
    """
    This class implements a TMCL connection for Kvaser adapter using CANLIB.
    Try 0 as default channel.
    """
    _CHANNELS = ["0",  "1",  "2"]

    def __init__(self, port="0", datarate=1000000, host_id=2, module_id=1, debug=False, timeout_s=5):
        if not isinstance(port, str):
            raise TypeError

        if port not in self._CHANNELS:
            raise ValueError("Invalid port!")

        CanTmclInterface.__init__(self, host_id, module_id, debug, timeout_s)
        self._channel = port
        self._bitrate = datarate

        try:
            if self._debug:
                self._connection = can.Bus(interface="kvaser", channel=self._channel, bitrate=self._bitrate)
            else:
                self._connection = can.Bus(interface="kvaser", channel=self._channel, bitrate=self._bitrate,
                                           can_filters=[{"can_id": host_id, "can_mask": 0x7F}])
        except can.CanError as e:
            self._connection = None
            raise ConnectionError("Failed to connect to Kvaser CAN bus") from e

        if self._debug:
            print("Opened bus on channel " + str(self._channel))

    @classmethod
    def list(cls):
        """
            Return a list of available connection ports as a list of strings.

            This function is required for using this interface with the
            connection manager.
        """
        return cls._CHANNELS
