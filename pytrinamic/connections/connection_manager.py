import sys
import logging
import argparse

from ..connections import DummyTmclInterface
from ..connections import PcanTmclInterface
from ..connections import SocketcanTmclInterface
from ..connections import KvaserTmclInterface
from ..connections import SerialTmclInterface
from ..connections import UartIcInterface
from ..connections import UsbTmclInterface
from ..connections import SlcanTmclInterface
from ..connections import IxxatTmclInterface

logger = logging.getLogger(__name__)


class ConnectionManager:
    """
    This class provides a centralized way of extracting connection-specific
    arguments out of a scripts command line arguments and using these to
    initiate connections.

    The constructor takes a string similar to command line arguments or a list
    of strings representing each commandline argument. This allows to directly
    pass the sys.argv parameter list. If nothing is passed sys.argv is used as
    default.

    The resulting filters for connections are stored in the instance of this
    class which allows repeated connect() and disconnect() calls.

    Supported commandline arguments:
        --interface <interface>
            Select an interface to use for connections. The possible values for
            this can be retrieved using the static function
                ConnectionManager.showInterfaces()
            which returns a list of interface strings.

            Default value: usb_tmcl

        --port <port>
            The port to use for connecting. The <port> value can be:
            - A number:
                Uses the n-th available port. Starts from 0, supports negative
                values to start counting from the end of the list of ports.
            - "any":
                Use any available port (the first one). Equivalent to using the
                number 0.
            - "interactive":
                Shows an interactive dialoge for selecting the port to use.
            - Any other string:
                Attempt to use the provided string to connect with the selected
                interface directly. E.g. for a serial connection you can use
                "COM3" on windows or "/dev/tty3" on linux.

            Default value: "any"

        --no-port <no-port>
            Ports to exclude when choosing a connection. This parameter can be
            added multiple times. E.g. "COM1" prevents the connection manager to
            select the port "COM1" for connections when using "any",
            "interactive" or a number as the --port argument.

        --data-rate <data-rate>
            The data rate to use for the connection. How this value is
            interpreted depends on the interface used. E.g. the serial
            connection uses this value as the baud rate.

            The Default value also depends on the interface.
                * for any CAN interface its 1000000
                * for the serial_tmcl and uard_id interface it is 9600
                * for usb_tmcl it is 115200

        --timeout <timeout in s>
            The rx timeout in seconds. Accepts only values >= 0.
            If 0 is given the rx function will block forever.
            This might be useful for debugging.

            Default value: 5.0

        --host-id <host-id>
            The host id to use with a TMCL connection.

            Default value: 2

        --module-id <module-id>
            The module id to use with a TMCL connection.

            Default value: 1
    """

    # All available interfaces
    # The tuples consist of (string representation, class type, default datarate)
    INTERFACES = [
        ("dummy_tmcl", DummyTmclInterface, 0),
        ("kvaser_tmcl", KvaserTmclInterface, 1000000),
        ("pcan_tmcl", PcanTmclInterface, 1000000),
        ("slcan_tmcl", SlcanTmclInterface, 1000000),
        ("socketcan_tmcl", SocketcanTmclInterface, 1000000),
        ("serial_tmcl", SerialTmclInterface, 9600),
        ("uart_ic", UartIcInterface, 9600),
        ("usb_tmcl", UsbTmclInterface, 115200),
        ("ixxat_tmcl", IxxatTmclInterface, 1000000),
    ]

    def __init__(self, arg_list=None, connection_type="any"):
        # Attributes
        self.__connection = None

        arg_parser = argparse.ArgumentParser(description='ConnectionManager to setup connections dynamically and interactively')
        ConnectionManager.argparse(arg_parser)

        if not arg_list:
            logger.info("Using arguments from the command line.")
            arg_list = sys.argv

        if isinstance(arg_list, str):
            arg_list = arg_list.split()

        logger.debug("List of input arguments: %s", arg_list)

        # Parse the command line
        args = arg_parser.parse_known_args(arg_list)[0]

        # Argument storage - default parameters are set here
        self.__interface  = UsbTmclInterface
        self.__port       = "any"
        self.__no_port    = []
        self.__data_rate  = 115200
        self.__host_id    = 2
        self.__module_id  = 1

        logger.debug("Combined default and parsed arguments: %s", args)

        # ## Interpret given arguments
        # Interface
        for actual_interface in self.INTERFACES:
            if connection_type == "tmcl" and not(actual_interface[1].supports_tmcl()):
                continue

            if args.interface[0] == actual_interface[0]:
                self.__interface = actual_interface[1]
                self.__data_rate = actual_interface[2]
                break
        else:
            # The for loop never hit the break statement -> invalid interface
            raise ValueError("Invalid interface: {0:s}".format(args.interface[0]))

        # Port
        # Any port string is valid. No check needed
        self.__port = args.port[0]

        # No-Port
        for port in args.exclude:
            if port in ["any", "interactive"]:
                raise ValueError("Port blacklist (no-port) cannot use the special port: " + port)

        # Data rate
        try:
            self.__data_rate = int(args.data_rate[0])
        except ValueError as exc:
            raise ValueError("Invalid data rate: " + args.data_rate[0]) from exc
        except TypeError:
            # No data rate has been set -> keep old value
            pass

        # Timeout
        self.__timeout_s = args.timeout_s

        # Host ID
        try:
            self.__host_id = int(args.host_id[0])
        except ValueError as exc:
            raise ValueError("Invalid host id: " + args.host_id[0]) from exc

        # Module ID
        try:
            self.__module_id = int(args.module_id[0])
        except ValueError as exc:
            raise ValueError("Invalid module id: " + args.module_id[0]) from exc

        logger.info("ConnectionManager created with ["
                    "Interface: %s; "
                    "Port: %s; "
                    "Blacklist: %s; "
                    "Data rate: %s; "
                    "Timeout: %s;"
                    "Host ID: %s; "
                    "Module ID: %s]",
                    self.__interface.__qualname__, self.__port, self.__no_port, self.__data_rate, self.__timeout_s,
                    self.__host_id, self.__module_id)

    def connect(self):
        """
        Attempt to connect to a module with the stored connection parameters.

        Returns a connection instance of a class based on the tmcl_interface.
        Which class type gets returned depends on the interface used.

        If no connections are available or a connection attempt fails, a
        ConnectionError exception is raised
        """
        # Get all available ports
        port_list = self.list_connections()

        # ## Parse the port string
        if self.__port == "interactive":
            # Check if ports are available
            if len(port_list) == 0:
                raise ConnectionError("No connections available")

            # "interactive" -> Show a selection dialog
            port = self.__interactive_port_selection()
        elif self.__port == "any":
            # Check if ports are available
            if len(port_list) == 0:
                raise ConnectionError("No connections available")

            # "any" -> Use the first port
            port = port_list[0]
        else:
            try:
                # Check if the port string is a number
                tmp = int(self.__port)

                # Check if ports are available
                if len(port_list) == 0:
                    raise ConnectionError("No connections available")

                # Port string is a Number -> Use the n-th port
                try:
                    port = port_list[tmp]
                except IndexError as exc:
                    raise ConnectionError("Couldn't connect to Port Number " + self.__port + ". Only "
                                          + str(len(port_list)) + " ports available") from exc
            except ValueError:
                # Not a number -> port string gets passed to interface directly
                # Do not check against the port list in this case. In certain
                # scenarios a port might be available without it being found by
                # the listConnections() method.
                port = self.__port
        try:
            if self.__interface.supports_tmcl():
                # Open the connection to a TMCL interface
                self.__connection = self.__interface(port, self.__data_rate, self.__host_id, self.__module_id,
                                                     timeout_s=self.__timeout_s)
            else:
                # Open the connection to a direct IC interface
                self.__connection = self.__interface(port, self.__data_rate, timeout_s=self.__timeout_s)
        except ConnectionError as e:
            raise ConnectionError("Couldn't connect to port " + port + ". Connection failed.") from e

        return self.__connection

    def disconnect(self):
        self.__connection.close()

    def list_connections(self):
        # Get the list of ports
        port_list = self.__interface.list()

        # Apply the port blacklist
        port_list = [port for port in port_list if port not in self.__no_port]

        return port_list

    def __interactive_port_selection(self):
        while True:
            # Get all available ports
            port_list = self.list_connections()

            print("Available options:")
            for i, entry in enumerate(port_list, 1):
                print("\t{0:2d}: {1:s}".format(i, entry))

            print("\t x: Abort selection")
            print("\t r: Refresh list")

            while True:
                selection = input("Enter your selection: ")
                print()

                if selection == "r":
                    # Break out of the inner while True loop
                    break
                if selection == "x":
                    raise ConnectionError("Port selection aborted by user")
                try:
                    selection = int(selection)
                    if not (1 <= selection <= len(port_list)):
                        raise ValueError

                    return port_list[selection-1]
                except ValueError:
                    continue

    @staticmethod
    def argparse(arg_parser):
        """
        Add ConnectionManager arguments to a argparse commandline parser

        When using the argparse package to create a command line interface in a
        script, this function adds the arguments of the ConnectionManager to the
        argparse parser.
        """
        def _positive_float(value):
            """
            Argparse checker for float a positive float type.
            """
            value_float = float(value)
            if value_float < 0:
                raise argparse.ArgumentTypeError("Expected a positive float, got {}".format(value_float))

            return value_float

        group = arg_parser.add_argument_group("ConnectionManager options")
        group.add_argument('--interface', dest='interface', action='store', nargs=1, type=str,
                           choices=[actual_interface[0] for actual_interface in ConnectionManager.INTERFACES],
                           default=['usb_tmcl'], help='Connection interface (default: %(default)s)')
        group.add_argument('--port', dest='port', action='store', nargs=1, type=str, default=['any'],
                           help='Connection port (default: %(default)s, n: Use n-th available port, "any": Use any available port, "interactive": Interactive dialogue for port selection, String: Attempt to use the provided string - e.g. COM6 or /dev/tty3)')
        group.add_argument('--no-port', dest='exclude', action='append', nargs='*', type=str, default=[],
                           help='Exclude ports')
        group.add_argument('--data-rate', dest='data_rate', action='store', nargs=1, type=int,
                           help='Connection data-rate (default: %(default)s)')
        group.add_argument('--timeout', dest='timeout_s', action='store', type=_positive_float, default=5.0,
                           help='Connection rx timeout in seconds (default: %(default)s)', metavar="SECONDS")

        group = arg_parser.add_argument_group("ConnectionManager TMCL options")

        group.add_argument('--host-id', dest='host_id', action='store', nargs=1, type=int, default=[2],
                           help='TMCL host-id (default: %(default)s)')
        group.add_argument('--module-id', dest='module_id', action='store', nargs=1, type=int, default=[1],
                           help='TMCL module-id (default: %(default)s)')

        return arg_parser

    @staticmethod
    def list_supported_interfaces():
        return [x[0] for x in ConnectionManager.INTERFACES]


if __name__ == "__main__":
    # Test if everything is working correctly

    print("Verifying interfaces list...\n")
    for interface in ConnectionManager.INTERFACES:
        if not hasattr(interface[1], "supports_tmcl"):
            raise NotImplementedError("Interface " + interface[0] + " is missing the supports_tmcl() function")
        if not hasattr(interface[1], "close"):
            raise NotImplementedError("Interface " + interface[0] + " is missing the close() function")
        if not hasattr(interface[1], "__enter__"):
            raise NotImplementedError("Interface " + interface[0] + " is missing the __enter__() function")
        if not hasattr(interface[1], "__exit__"):
            raise NotImplementedError("Interface " + interface[0] + " is missing the __exit__() function")
        if not hasattr(interface[1], "list"):
            raise NotImplementedError("Interface " + interface[0] + " is missing the list() function")

    print("List of interfaces: " + str(ConnectionManager.list_supported_interfaces()) + "\n")

    print("---------------------------------------------------")
    print("Performing test run...\n")
    connectionManager = ConnectionManager()
    try:
        connection = connectionManager.connect()
        connectionManager.disconnect()
    except ConnectionError:
        print("Error: No connections available")

    print("Test run complete")
    print("---------------------------------------------------")
    print("Showing help...")
    parser = argparse.ArgumentParser()
    ConnectionManager.argparse(parser)
    parser.print_help()
