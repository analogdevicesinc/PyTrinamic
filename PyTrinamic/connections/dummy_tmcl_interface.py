'''
Created on 27.05.2019

@author: LH
'''

from PyTrinamic.connections.tmcl_interface import tmcl_interface

class dummy_tmcl_interface(tmcl_interface):

    def __init__(self, port, datarate=115200, hostID=2, moduleID=1, debug=True):
        """
        Opens a dummy TMCL connection
        """
        if type(port) != str:
            raise TypeError

        del debug

        tmcl_interface.__init__(self, hostID, moduleID, debug=True)

        if self._debug:
            print("Opened dummy TMCL interface on port '" + port + "'")
            print("\tData rate:  " + str(datarate))
            print("\tHost ID:    " + str(hostID))
            print("\tModule ID:  " + str(moduleID))

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
    def list():
        """
            Return a list of available connection ports as a list of strings.

            This function is required for using this interface with the
            connection manager.
        """
        return ["dummy"]

if __name__ == "__main__":
    interface = dummy_tmcl_interface("dummy")

    interface.getVersionString()
    interface.sendBoot()

    interface.close()
