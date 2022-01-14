from PyTrinamic.connections.CANopen_interface import CANopen_interface

_CHANNELS = [
    "PCAN_USBBUS1",  "PCAN_USBBUS2",  "PCAN_USBBUS3",  "PCAN_USBBUS4"
    ]

class pcan_CANopen_interface(CANopen_interface):

    def __init__(self, port, datarate, debug=False):
        if type(port) != str:
            raise TypeError

        if not port in _CHANNELS:
            raise ValueError("Invalid port")

        CANopen_interface.__init__(self, "pcan", port, datarate, debug=debug)
        
        self.__channel = port
        self.__bitrate = datarate

    def printInfo(self):
        print("Connection: type=pcan_CANopen_interface channel=" + self.__channel + " bitrate=" + str(self.__bitrate))

    @staticmethod
    def supportsTMCL():
        return False

    @staticmethod
    def supportsCANopen():
        return True

    @staticmethod
    def list():
        """
            Return a list of available connection ports as a list of strings.

            This function is required for using this interface with the
            connection manager.
        """
        return _CHANNELS
