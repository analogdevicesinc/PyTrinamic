import can
from can import CanError
from serial.tools.list_ports import comports
from ...connections.can_tmcl_interface import CanTmclInterface


class SlcanTmclInterface(CanTmclInterface):
    """
    This class implements a TMCL connection for CAN over Serial / SLCAN.
    Compatible with CANable running slcan firmware and similar.
    Set underlying serial device as channel. (e.g. /dev/ttyUSB0, COM8, …)
    Maybe SerialBaudrate has to be changed based on adapter.
    """

    def __init__(self, com_port, datarate=1000000, host_id=2, module_id=1, timeout_s=5, serial_baudrate=115200):
        if not isinstance(com_port, str):
            raise TypeError

        CanTmclInterface.__init__(self, com_port, datarate, host_id, module_id, timeout_s)
        self._serial_baudrate = serial_baudrate

        self.logger.info("Connect to bus. (Baudrate=%s)", self._serial_baudrate)
        try:
            self._connection = can.Bus(interface='slcan',
                                       channel=self._channel,
                                       bitrate=self._bitrate,
                                       ttyBaudrate=self._serial_baudrate)
            self._connection.set_filters([{"can_id": host_id, "can_mask": 0x7F}])
        except CanError as e:
            self._connection = None
            raise ConnectionError("Failed to connect to CAN bus") from e

    @classmethod
    def list(cls):
        """
            Return a list of available connection ports as a list of strings.

            This function is required for using this interface with the
            connection manager.
        """
        connected = []
        for element in sorted(comports()):
            connected.append(element.device)

        return connected
