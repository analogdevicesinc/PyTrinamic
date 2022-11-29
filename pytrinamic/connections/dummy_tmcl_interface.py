from ..connections.tmcl_interface import TmclInterface
from ..tmcl import TMCLReply, TMCLStatus, TMCLRequest

class DummyTmclInterface(TmclInterface):

    def __init__(self, port, datarate=115200, host_id=2, module_id=1, debug=True, timeout_s=5):
        """
        Opens a dummy TMCL connection
        """
        if not isinstance(port, str):
            raise TypeError

        TmclInterface.__init__(self, host_id, module_id, debug)

        # Cache sent request to echo in reply
        self._cached_request = 0

        if self._debug:
            print("Opened dummy TMCL interface on port '" + port + "'")
            print("\tData rate:  " + str(datarate))
            print("\tHost ID:    " + str(host_id))
            print("\tModule ID:  " + str(module_id))
            print("\tTimeout:    " + str(timeout_s))

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        """
        Close the connection at the end of a with-statement block.
        """
        del exit_type, value, traceback
        self.close()

    def close(self):
        """
        Closes the dummy TMCL connection
        """
        if self._debug:
            print("Closed dummy TMCL interface")

    def _send(self, host_id, module_id, data):
        """
            Send the bytearray parameter [data].

            This is a required override function for using the tmcl_interface
            class.
        """
        self._cached_request = TMCLRequest.from_buffer(data)

        del host_id, module_id
        pass

    def _recv(self, host_id, module_id):
        """
            Read 9 bytes and return them as a bytearray.

            This is a required override function for using the tmcl_interface
            class.
        """
        command = self._cached_request.command
        value = self._cached_request.value

        # Prepare a dummy answer, we always return the SUCCESS status, should be safe enough for dummy stuff.
        reply = TMCLReply(host_id, module_id, TMCLStatus.SUCCESS, command, value)

        return reply.to_buffer()

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
        return ["dummy"]

    def __str__(self):
        return "Connection: type={}".format(type(self).__name__)


if __name__ == "__main__":
    interface = DummyTmclInterface("dummy")

    interface.send_boot()
    interface.close()
