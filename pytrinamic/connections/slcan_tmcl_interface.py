import can
from can import CanError
from serial.tools.list_ports import comports
from ..connections.tmcl_interface import TmclInterface


class SlcanTmclInterface(TmclInterface):
    """
    This class implements a TMCL connection for CAN over Serial / SLCAN.
    Compatible with CANable running slcan firmware and similar.
    Set underlying serial device as channel. (e.g. /dev/ttyUSB0, COM8, …)
    Maybe SerialBaudrate has to be changed based on adapter.
    """

    def __init__(self, com_port, datarate=1000000, host_id=2, module_id=1, debug=True, serial_baudrate=115200):
        if not isinstance(com_port, str):
            raise TypeError

        TmclInterface.__init__(self, host_id, module_id, debug)
        self._bitrate = datarate
        self._port = com_port
        self._serial_baudrate = serial_baudrate

        try:
            self._connection = can.Bus(interface='slcan', channel=self._port, bitrate=self._bitrate,
                                       ttyBaudrate=self._serialBaudrate)
            self._connection.set_filters([{"can_id": host_id, "can_mask": 0x7F}])
        except CanError as e:
            self.__connection = None
            raise ConnectionError("Failed to connect to CAN bus") from e

        if self._debug:
            print("Opened slcan bus on channel " + self._port)

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
            print("Closing CAN bus")

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
            self.__connection.send(msg)
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
        connected = []
        for element in sorted(comports()):
            connected.append(element.device)

        return connected

    def __str__(self):
        return "Connection: type={} channel={} bitrate={}".format(type(self).__name__, self._port, self._bitrate)
