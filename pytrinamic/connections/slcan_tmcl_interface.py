'''
Created on 03.01.2020

@author: JH
'''
import can
from pytrinamic.connections.TmclInterface import TmclInterface
from can import CanError
from serial.tools.list_ports import comports

class slcan_tmclInterface(TmclInterface):
    """
    This class implements a TMCL connection for CAN over Serial / SLCAN. Comatible with CANable running slcan firmware and similar.
    Set underlying serial device as channel. (e.g. /dev/ttyUSB0, COM8, …)
    Maybe SerialBaudrate has to be changed based on Adapter.
    """

    def __init__(self, comPort, datarate=1000000, hostID=2, moduleID=1, debug=True, SerialBaudrate=115200):
        if type(comPort) != str:
            raise TypeError

        TmclInterface.__init__(self, hostID, moduleID, debug)

        self.__debug = debug
        self.__bitrate = datarate
        self.__Port = comPort
        self.__serialBaudrate = SerialBaudrate

        try:
            self.__connection = can.Bus(interface='slcan', channel=self.__Port, bitrate=self.__bitrate,ttyBaudrate=self.__serialBaudrate)
            self.__connection.set_filters([{ "can_id": hostID, "can_mask": 0x7F }])

        except CanError as e:
            self.__connection = None
            raise ConnectionError("Failed to connect to CAN bus") from e

        if self.__debug:
            print("Opened slcan bus on channel " + self.__Port)

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        """
        Close the connection at the end of a with-statement block.
        """
        del exit_type, value, traceback
        self.close()

    def close(self):
        if self.__debug:
            print("Closing CAN bus")

        self.__connection.shutdown()

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
            msg = self.__connection.recv(timeout=3)
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

    def printInfo(self):
        print("Connection: type=slcan_tmcl_interface channel=" + self.__channel + " bitrate=" + str(self.__bitrate))

    def enableDebug(self, enable):
        self.__debug = enable

    @staticmethod
    def supportsTMCL():
        return True

    @staticmethod
    def supportsCANopen():
        return False

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
