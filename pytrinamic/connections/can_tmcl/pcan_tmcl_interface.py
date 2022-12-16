
import can
from can.interfaces.pcan.pcan import PcanError
from ...connections.can_tmcl_interface import CanTmclInterface


class PcanTmclInterface(CanTmclInterface):
    """
    This class implements a TMCL connection over a PCAN adapter.
    """
    _CHANNELS = [
        "PCAN_USBBUS1", "PCAN_USBBUS2", "PCAN_USBBUS3", "PCAN_USBBUS4",
        "PCAN_USBBUS5", "PCAN_USBBUS6", "PCAN_USBBUS7", "PCAN_USBBUS8",
        "PCAN_USBBUS9", "PCAN_USBBUS10", "PCAN_USBBUS11", "PCAN_USBBUS12",
        "PCAN_USBBUS13", "PCAN_USBBUS14", "PCAN_USBBUS15", "PCAN_USBBUS16",

        "PCAN_ISABUS1", "PCAN_ISABUS2", "PCAN_ISABUS3", "PCAN_ISABUS4",
        "PCAN_ISABUS5", "PCAN_ISABUS6", "PCAN_ISABUS7", "PCAN_ISABUS8",

        "PCAN_DNGBUS1",

        "PCAN_PCIBUS1", "PCAN_PCIBUS2", "PCAN_PCIBUS3", "PCAN_PCIBUS4",
        "PCAN_PCIBUS5", "PCAN_PCIBUS6", "PCAN_PCIBUS7", "PCAN_PCIBUS8",
        "PCAN_PCIBUS9", "PCAN_PCIBUS10", "PCAN_PCIBUS11", "PCAN_PCIBUS12",
        "PCAN_PCIBUS13", "PCAN_PCIBUS14", "PCAN_PCIBUS15", "PCAN_PCIBUS16",

        "PCAN_PCCBUS1", "PCAN_PCCBUS2",

        "PCAN_LANBUS1", "PCAN_LANBUS2", "PCAN_LANBUS3", "PCAN_LANBUS4",
        "PCAN_LANBUS5", "PCAN_LANBUS6", "PCAN_LANBUS7", "PCAN_LANBUS8",
        "PCAN_LANBUS9", "PCAN_LANBUS10", "PCAN_LANBUS11", "PCAN_LANBUS12",
        "PCAN_LANBUS13", "PCAN_LANBUS14", "PCAN_LANBUS15", "PCAN_LANBUS16"
    ]

    def __init__(self, port, datarate=1000000, host_id=2, module_id=1, timeout_s=5):
        if not isinstance(port, str):
            raise TypeError

        if port not in self._CHANNELS:
            raise ValueError("Invalid port!")

        CanTmclInterface.__init__(self, port, datarate, host_id, module_id, timeout_s)
        self._channel = port
        self._bitrate = datarate

        self.logger.info("Connect to bus with bit-rate %s.", self._bitrate)
        try:
            self._connection = can.Bus(interface="pcan", channel=self._channel, bitrate=self._bitrate)
            self._connection.set_filters([{"can_id": host_id, "can_mask": 0xFFFFFFFF}])
        except PcanError as e:
            self._connection = None
            raise ConnectionError("Failed to connect to PCAN bus") from e

    @classmethod
    def list(cls):
        """
            Return a list of available connection ports as a list of strings.

            This function is required for using this interface with the
            connection manager.
        """
        return cls._CHANNELS
