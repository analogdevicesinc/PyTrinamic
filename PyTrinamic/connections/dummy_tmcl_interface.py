'''
Created on 27.05.2019

@author: LH
'''

from PyTrinamic.connections.tmcl_interface import tmcl_interface

class dummy_tmcl_interface(tmcl_interface):

    DEFAULT_DATA_RATE = 115200

    def __init__(self, port, data_rate=115200, host_id=2, module_id=1, debug=True):
        """
        Opens a dummy TMCL connection
        """
        if type(port) != str:
            raise TypeError

        del debug

        super().__init__(host_id, module_id, debug=True)

        if self._debug:
            print("Opened dummy TMCL interface on port '" + port + "'")
            print("\tData rate:  " + str(data_rate))
            print("\tHost ID:    " + str(host_id))
            print("\tModule ID:  " + str(module_id))

    def __enter__(self):
        return self

    def __exit__(self, exitType, value, traceback):
        """
        Close the connection at the end of a with-statement block.
        """
        del exitType, value, traceback
        self.close()

    def close(self):
        """
        Closes the dummy TMCL connection
        """
        if self._debug:
            print("Closed dummy TMCL interface")

    def _send(self, hostID, moduleID, data):
        """
            Send the bytearray parameter [data].

            This is a required override function for using the tmcl_interface
            class.
        """
        del hostID, moduleID, data
        pass

    def _recv(self, hostID, moduleID):
        """
            Read 9 bytes and return them as a bytearray.

            This is a required override function for using the tmcl_interface
            class.
        """
        del hostID, moduleID

        return bytearray(9)

    def printInfo(self):
        print("Connection: type=dummy_tmcl_interface")

    @staticmethod
    def supportsTMCL():
        return True

    @staticmethod
    def supportsCANopen():
        return False

    @staticmethod
    def available_ports():
        return { "dummy" }

if __name__ == "__main__":
    interface = dummy_tmcl_interface("dummy")

    interface.getVersionString()
    interface.sendBoot()

    interface.close()
