
import can
from can import CanError
from can.interfaces.pcan.pcan import PcanError
from ..connections.tmcl_interface import TmclInterface

_CHANNELS = [
    "PCAN_USBBUS1",  "PCAN_USBBUS2",  "PCAN_USBBUS3",  "PCAN_USBBUS4",
    "PCAN_USBBUS5",  "PCAN_USBBUS6",  "PCAN_USBBUS7",  "PCAN_USBBUS8",
    "PCAN_USBBUS9",  "PCAN_USBBUS10", "PCAN_USBBUS11", "PCAN_USBBUS12",
    "PCAN_USBBUS13", "PCAN_USBBUS14", "PCAN_USBBUS15", "PCAN_USBBUS16",

    "PCAN_ISABUS1",  "PCAN_ISABUS2",  "PCAN_ISABUS3",  "PCAN_ISABUS4",
    "PCAN_ISABUS5",  "PCAN_ISABUS6",  "PCAN_ISABUS7",  "PCAN_ISABUS8",

    "PCAN_DNGBUS1",

    "PCAN_PCIBUS1",  "PCAN_PCIBUS2",  "PCAN_PCIBUS3",  "PCAN_PCIBUS4",
    "PCAN_PCIBUS5",  "PCAN_PCIBUS6",  "PCAN_PCIBUS7",  "PCAN_PCIBUS8",
    "PCAN_PCIBUS9",  "PCAN_PCIBUS10", "PCAN_PCIBUS11", "PCAN_PCIBUS12",
    "PCAN_PCIBUS13", "PCAN_PCIBUS14", "PCAN_PCIBUS15", "PCAN_PCIBUS16",

    "PCAN_PCCBUS1",  "PCAN_PCCBUS2",

    "PCAN_LANBUS1",  "PCAN_LANBUS2",  "PCAN_LANBUS3",  "PCAN_LANBUS4",
    "PCAN_LANBUS5",  "PCAN_LANBUS6",  "PCAN_LANBUS7",  "PCAN_LANBUS8",
    "PCAN_LANBUS9",  "PCAN_LANBUS10", "PCAN_LANBUS11", "PCAN_LANBUS12",
    "PCAN_LANBUS13", "PCAN_LANBUS14", "PCAN_LANBUS15", "PCAN_LANBUS16"
    ]


class PcanTmclInterface(TmclInterface):
    """
    This class implements a TMCL connection over a PCAN adapter.
    """
    def __init__(self, port, datarate=1000000, host_id=2, module_id=1, debug=False):
        if not isinstance(port, str):
            raise TypeError

        if port not in _CHANNELS:
            raise ValueError("Invalid port!")

        TmclInterface.__init__(self, host_id, module_id, debug)
        self._channel = port
        self._bitrate = datarate

        try:
            self._connection = can.Bus(interface="pcan", channel=self._channel, bitrate=self._bitrate)
            self._connection.set_filters([{"can_id": host_id, "can_mask": 0xFFFFFFFF}])
        except PcanError as e:
            self._connection = None
            raise ConnectionError("Failed to connect to PCAN bus") from e

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
            print("Closing PCAN bus")

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
