from abc import ABC
import canopen
from PyTrinamic.connections.ConnectionInterface import ConnectionInterface


class CANopenInterface(ConnectionInterface, ABC):

    def __init__(self, bustype, channel, bitrate, debug=False):
        self._debug = debug

        self.__network = canopen.Network()
        self.__network.connect(bustype=bustype, channel=channel, bitrate=bitrate)

        if self._debug:
            print("Opened Channel " + channel)

        self.__nodes = []

    # override ConnectionInterface
    def supports_tmcl(self):
        return False

    # override ConnectionInterface
    def supports_canopen(self):
        return True

    # override ConnectionInterface
    def enable_debug(self, enable):
        self._debug = enable

    def addDs402Node(self, eds_path, node_id, number_of_motors=1):
        if self._debug:
            print("Adding network node (id: {0:d}) with {1:d} motors using EDS file: {3:s}".format(node_id,
                                                                                                   number_of_motors,
                                                                                                   eds_path))

        # Add some nodes with corresponding Object Dictionaries
        node = canopen.BaseNode402(1, eds_path)
        self.__network.add_node(node)
        node.setup_402_state_machine()

        self.__nodes.append({
            "node_id": node_id,
            "node": node,
            })
        return node

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
            print("Close PCAN")

        self.__network.disconnect()
