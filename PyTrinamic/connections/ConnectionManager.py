'''
Created on 28.05.2019

@author: LH
'''

import sys

from PyTrinamic.connections.dummy_tmcl_interface import dummy_tmcl_interface
from PyTrinamic.connections.pcan_tmcl_interface import pcan_tmcl_interface
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
from PyTrinamic.connections.usb_tmcl_interface import usb_tmcl_interface

class ConnectionManager():
    """
    This class provides a centralized way of extracting connection-specific
    arguments out of a scripts command line arguments and using these to
    initiate connections.

    The constructor takes the list of commandline arguments as a list of
    strings. This allows to directly pass the sys.argv parameter list. If no
    list is passed sys.argv is used as default.

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

            Default value: 115200

        --host-id <host-id>
            The host id to use with a TMCL connection.

            Default value: 2

        --module-id <module-id>
            The module id to use with a TMCL connection.

            Default value: 1
    """

    # All available interfaces
    # The tuples consist of (string representation, class type, default datarate)
    _INTERFACES = [
        ("dummy_tmcl",  dummy_tmcl_interface,  0),
        ("pcan_tmcl",   pcan_tmcl_interface,   1000000),
        ("serial_tmcl", serial_tmcl_interface, 9600),
        ("uart_ic",     dummy_tmcl_interface,  9600),
        ("usb_tmcl",    usb_tmcl_interface,    115200)
    ]

    def __init__(self, argList=None, debug=False):
        # Attributes
        self.__argList          = argList if argList else sys.argv
        self.__debug            = debug
        self.__strippedArgList  = []

        # Storage for extracted commandline strings
        self.__str_interface  = None
        self.__str_port       = None
        self.__str_data_rate  = None
        self.__str_host_id    = None
        self.__str_module_id  = None

        # Argument storage - default parameters are set here
        self.__interface  = usb_tmcl_interface
        self.__port       = "any"
        self.__no_port    = []
        self.__data_rate  = 115200
        self.__host_id    = 2
        self.__module_id  = 1

        # Parse the command line
        if self.__debug:
            print("Commandline argument list: {0:s}".format(str(self.__argList)))
            print("Parsing {0:d} commandline arguments:".format(len(self.__argList)))

        skip = 0
        for i, arg in enumerate(self.__argList, 1):
            if i == len(self.__argList):
                break

            if arg == "--interface":
                if self.__str_interface:
                    raise ValueError("Found two --interface parameters")

                self.__str_interface = self.__argList[i]
                if self.__debug:
                    print("\tInterface:  " + self.__str_interface)

                skip = 2

            if arg == "--port":
                if self.__str_port:
                    raise ValueError("Found two --port parameters")

                self.__str_port = self.__argList[i]
                if self.__debug:
                    print("\tPort:       " + self.__str_port)

                skip = 2

            if arg == "--no-port":
                # Append the blacklisted port
                self.__no_port += [self.__argList[i]]
                if self.__debug:
                    print("\tNo Port:    " + self.__argList[i])

                skip = 2

            if arg == "--data-rate":
                if self.__str_data_rate:
                    raise ValueError("Found two --data-rate parameters")

                self.__str_data_rate = self.__argList[i]
                if self.__debug:
                    print("\tData rate:  " + self.__str_data_rate)

                skip = 2

            if arg == "--host-id":
                if self.__str_host_id:
                    raise ValueError("Found two --host-id parameters")

                self.__str_host_id = self.__argList[i]
                if self.__debug:
                    print("\tHost ID:    " + self.__str_host_id)

                skip = 2

            if arg == "--module-id":
                if self.__str_module_id:
                    raise ValueError("Found two --module-id parameters")

                self.__str_module_id = self.__argList[i]
                if self.__debug:
                    print("\tModule ID:  " + self.__str_module_id)

            # Check if the last argument needs to be added to the stripped
            # argument list.
            if skip == 0:
                self.__strippedArgList += [arg]
            else:
                skip -= 1;

        # The loop skips the last element of the argument list.
        # Check if that last argument needs to be added to the stripped argument
        # list.
        if skip == 0:
            self.__strippedArgList += [self.__argList[-1]]

        if self.__debug:
            print()

        ### Verify the given arguments
        # Interface
        if self.__str_interface:
            for interface in self._INTERFACES:
                if self.__str_interface == interface[0]:
                    self.__interface = interface[1]
                    self.__data_rate = interface[2]
                    break
            else:
                # The for loop never hit the break statement -> invalid interface
                raise ValueError("Invalid interface: {0:s}".format(self.__str_interface))

        # Port
        # Any port string is valid. No check needed
        if self.__str_port:
            self.__port = self.__str_port

        # No-Port
        for port in self.__no_port:
            if port in ["any", "interactive"]:
                raise ValueError("Port blacklist (no-port) cannot use the special port: " + self.__no_port)

        # Data rate
        if self.__str_data_rate:
            try:
                self.__data_rate = int(self.__str_data_rate)
            except ValueError:
                raise ValueError("Invalid data rate: " + self.__str_data_rate)

        # Host ID
        if self.__str_host_id:
            try:
                self.__host_id = int(self.__str_host_id)
            except ValueError:
                raise ValueError("Invalid host id: " + self.__str_host_id)

        # Module ID
        if self.__str_module_id:
            try:
                self.__module_id = int(self.__str_module_id)
            except ValueError:
                raise ValueError("Invalid module id: " + self.__str_module_id)

        if self.__debug:
            print("Connection parameters:")
            print("\tInterface:  " + self.__interface.__qualname__)
            print("\tPort:       " + self.__port)
            print("\tBlacklist:  " + str(self.__no_port))
            print("\tData rate:  " + str(self.__data_rate))
            print("\tHost ID:    " + str(self.__host_id))
            print("\tModule ID:  " + str(self.__module_id))
            print()

            print("Leftover commandline arguments: " + str(self.__strippedArgList))

    def connect(self):
        """
        Attempt to connect to a module with the stored connection parameters.

        Returns a connection instance of a class based on the tmcl_interface.
        Which class type gets returned depends on the interface used.

        If no connections are available or a connection attempt fails, a
        ConnectionError exception is raised

        """
        # Get all available ports
        portList = self.listConnections()

        # Check if ports are available
        if len(portList) == 0:
            raise ConnectionError("No connections available")

        ### Parse the port string
        if self.__port == "interactive":
            # "interactive" -> Show a selection dialog
            port = self.__interactivePortSelection()
        elif self.__port == "any":
            # "any" -> Use the first port
            port = portList[0]
        else:
            try:
                # Check if the port string is a number
                tmp = int(self.__port)

                # Port string is a Number -> Use the n-th port
                try:
                    port = portList[tmp]
                except IndexError:
                    raise ConnectionError("Couldn't connect to Port Number " + self.__port + ". Only " + str(len(portList)) +" ports available")
            except ValueError:
                # Not a number -> port string gets passed to interface directly
                port = self.__port
        try:
            self.__connection = self.__interface(port, self.__data_rate, self.__host_id, self.__module_id, debug=self.__debug)
        except ConnectionError as e:
            raise ConnectionError("Couldn't connect to port " + port + ". Connection failed.") from e

        return self.__connection

    def disconnect(self):
        self.__connection.close()

    def listConnections(self):
        # Get the list of ports
        portList = self.__interface.list()

        # Apply the port blacklist
        portList = [port for port in portList if port not in self.__no_port]

        return portList

    def __interactivePortSelection(self):
        while True:
            # Get all available ports
            portList = self.listConnections()

            print("Available options:")
            for i, entry in enumerate(portList, 1):
                print("\t{0:2d}: {1:s}".format(i, entry))

            print("\t x: Abort selection")
            print("\t r: Refresh list")

            while True:
                selection = input("Enter your selection: ")
                print()

                if selection == "r":
                    # Break out of the inner while True loop
                    break
                elif selection == "x":
                    raise ConnectionError("Port selection aborted by user")
                else:
                    try:
                        selection = int(selection)
                        if not (1 <= selection <= len(portList)):
                            raise ValueError

                        return portList[selection-1]
                    except ValueError:
                        continue;

    @staticmethod
    def listInterfaces():
        return [x[0] for x in ConnectionManager._INTERFACES]

if __name__ == "__main__":
    # Test if everything is working correctly

    print("Verifying interfaces list...\n")
    for interface in ConnectionManager._INTERFACES:
        if not hasattr(interface[1], "close"):
            raise NotImplementedError("Interface " + interface[0] + " is missing the close() function")
        if not hasattr(interface[1], "list"):
            raise NotImplementedError("Interface " + interface[0] + " is missing the list() function")

    print("List of interfaces: " + str(ConnectionManager.listInterfaces()) + "\n")

    print("Performing test run...\n")
    connectionManager = ConnectionManager()
    try:
        connection = connectionManager.connect()
        connectionManager.disconnect()
    except RuntimeError:
        print("Couldn't connect to the specified port(s)")

    print("Test run complete")
