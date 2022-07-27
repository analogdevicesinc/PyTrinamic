import can
from can import CanError
from ..connections.tmcl_interface import TmclInterface

# Providing 5 channels here, this should cover all use cases.
# Ixxat USB-to-CAN provides 1, 2 or 4 channels.
_CHANNELS = ["0", "1", "2", "3", "4"]


class IxxatTmclInterface(TmclInterface):
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

    def __init__(self, port="0", datarate=1000000, host_id=2, module_id=1, debug=False):
        if not isinstance(port, str):
            raise TypeError

        if port not in _CHANNELS:
            raise ValueError("Invalid port!")

        TmclInterface.__init__(self, host_id, module_id, debug)
        self._channel = port
        self._bitrate = datarate

        try:
            if self._debug:
                self._connection = can.Bus(interface="ixxat", channel=self._channel, bitrate=self._bitrate)
            else:
                self._connection = can.Bus(
                    interface="ixxat",
                    channel=self._channel,
                    bitrate=self._bitrate,
                    can_filters=[{"can_id": host_id, "can_mask": 0x7F}],
                )
        except CanError as e:
            self._connection = None
            raise ConnectionError(
                f"Failed to connect to {self.__class__.__name__} on channel {str(self._channel)}"
            ) from e

        if self._debug:
            print(f"Opened {self.__class__.__name__} on channel {str(self._channel)}")

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
            print(f"Closing {self.__class__.__name__} (channel {str(self._channel)})")

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
            raise ConnectionError(
                f"Failed to send a TMCL message on {self.__class__.__name__} (channel {str(self._channel)})"
            ) from e

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
            raise ConnectionError(
                f"Failed to receive a TMCL message from {self.__class__.__name__} (channel {str(self._channel)})"
            ) from e

        if not msg:
            # Todo: Timeout retry mechanism
            raise ConnectionError(f"Recv timed out ({self.__class__.__name__}, on channel {str(self._channel)})")

        if msg.arbitration_id != host_id:
            # The filter shouldn't let wrong messages through.
            # This is just a sanity check
            if self._debug:
                print(f"Received wrong ID ({self.__class__.__name__}, on channel {str(self._channel)})")

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
        return f"Connection: Type = {self.__class__.__name__}, Channel = {self._channel}, Bitrate = {self._bitrate}"


"""
# Snippet to test connection between one (or two) ports of a single IXXAT USB-to-CAN and TMCL device(s).
if __name__ == "__main__":
    CAN1 = IxxatTmclInterface(port="0")
    # CAN2 = IxxatTmclInterface(port="1")
    print(CAN1)
    # print(CAN2)

    print(CAN1.get_version_string())
    # print(CAN2.get_version_string())
"""
