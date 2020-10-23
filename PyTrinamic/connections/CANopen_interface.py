'''
Created on 13.02.2020

@author: JM
'''

import canopen

class CANopen_interface():

    def __init__(self, bustype, channel, data_rate, debug=False):
        self._debug = debug

        self.__network = canopen.Network()
        self.__network.connect(bustype=bustype, channel=channel, bitrate=data_rate)

        if self._debug:
            print("Opened Channel " + channel)

        self.__nodes = []

    def addDs402Node(self, eds_path, node_id, number_of_motors=1):
        if self._debug:
            print("Adding network node (id: {0:d}) with {1:d} motors using EDS file: {3:s}".format(node_id, number_of_motors, eds_path))

        # Add some nodes with corresponding Object Dictionaries
        node = canopen.BaseNode402(1, eds_path)
        self.__network.add_node(node)
        node.setup_402_state_machine()

        self.__nodes.append({
            "node_id" : node_id,
            "node"    : node,
            })
        return node

    def __enter__(self):
        return self

    def __exit__(self, exitType, value, traceback):
        """
        Close the connection at the end of a with-statement block.
        """
        del exitType, value, traceback
        self.close()

    def close(self):
        if self._debug:
            print("Close PCAN")

        self.__network.disconnect()

    def enableDebug(self, enable):
        self._debug = enable

    @staticmethod
    def supportsTMCL():
        return False

    @staticmethod
    def supportsCANOpen():
        return True
