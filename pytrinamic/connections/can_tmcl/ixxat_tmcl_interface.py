import can
from ...connections.can_tmcl_interface import CanTmclInterface


class IxxatTmclInterface(CanTmclInterface):
    """
    This class implements a TMCL connection for IXXAT USB-to-CAN adapter.
    Backend is provided by the IXXAT Virtual CAN Interface V3 SDK.

    Port number is assigned as adapters are plugged in, arbitrarely,
    it is possible to use multiple channels of one IXXAT, CAN1 is port "0", CAN2 is port "1", etc.

    This class, and the parser implementation DOES NOT support multiple IXXATs connected to one computer.

    To add this functionality, python-can version 4.0.0 is necessary as it allows enumerating IXXAT devices IDs,
    (see https://github.com/hardbyte/python-can/pull/926).
    To use multiple IXXAT devices, you must provide hardware IDs (this needs to be added to this class and to the parser).

    Snippet to list IXXAT by hardware ID using python-can 4.0.0:
        from can.interfaces.ixxat import IXXATBus
        for hwid in IXXATBus.list_adapters():
            print("Found IXXAT adapter with hardware id '%s'." % hwid)
    """

    # Providing 5 channels here, this should cover all use cases.
    # Ixxat USB-to-CAN provides 1, 2 or 4 channels.
    _CHANNELS = ["0", "1", "2", "3", "4"]

    def __init__(self, port="0", datarate=1000000, host_id=2, module_id=1, timeout_s=5):
        if not isinstance(port, str):
            raise TypeError

        if port not in self._CHANNELS:
            raise ValueError("Invalid port!")

        CanTmclInterface.__init__(self, port, datarate, host_id, module_id, timeout_s)

        self.logger.info("Connect to bus with bit-rate %s.", self._bitrate)
        try:
            self._connection = can.Bus(interface="ixxat",
                                       channel=self._channel,
                                       bitrate=self._bitrate,
                                       can_filters=[{"can_id": host_id, "can_mask": 0x7F}])
        except can.CanError as e:
            self._connection = None
            raise ConnectionError(
                f"Failed to connect to {self.__class__.__name__} on channel {str(self._channel)}"
            ) from e

    @classmethod
    def list(cls):
        """
        Return a list of available connection ports as a list of strings.

        This function is required for using this interface with the
        connection manager.
        """
        return cls._CHANNELS
