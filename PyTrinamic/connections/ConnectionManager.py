'''
Created on 28.05.2019

@author: LH
'''

import sys
import argparse

class interface_config(object):

    def __init__(self, interface=None, port=None, data_rate=None):
        self.interface = interface
        self.port = port
        self.data_rate = data_rate

class interface_config_tmcl(interface_config):

    def __init__(self, interface=None, port=None, data_rate=None, host_id=None, module_id=None):
        super().__init__(interface, port, data_rate)
        self.host_id = host_id
        self.module_id = module_id

class interface_config_canopen(interface_config):
    def __str__(self):
        return "interface_config_canopen(\n\tinterface={}, \n\tport={}, \n\tdata_rate={}\n)".format(
            self.interface, self.port, self.data_rate
        )


class ConnectionManager():
    """
    This class provides a centralized way of extracting connection-specific
    arguments out of a scripts command line arguments and using these to
    initiate connections.

    The constructor takes a string similar to command line arguments or a list
    of strings represeting each commandline argument. This allows to directly
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

            Default value: 115200

        --host-id <host-id>
            The host id to use with a TMCL connection.

            Default value: 2

        --module-id <module-id>
            The module id to use with a TMCL connection.

            Default value: 1
    """

    def __init__(self, argList=None, connectionType="any", debug=False):
        # Attributes
        self.__debug = debug
        available = self._get_available_interfaces()

        parser = argparse.ArgumentParser(description='ConnectionManager to setup connections dynamically and interactively')
        parser.add_argument('--interface', dest='interface', action='store', nargs="*", type=str, choices=available.keys(), default=["any"],
                            help='Connection interface (default: %(default)s)')
        parser.add_argument('--port', dest='port', action='store', nargs="*", type=str, default=["any"],
                            help='Connection port (default: %(default)s, n: Use n-th available port, "any": Use any available port, "interactive": Interactive dialogue for port selection, String: Attempt to use the provided string - e.g. COM6 or /dev/tty3)')
        parser.add_argument('--no-port', dest='exclude', action='append', nargs='*', type=str, default=[],
                            help='Exclude ports')
        parser.add_argument('--data-rate', dest='data_rate', action='store', nargs="*", type=str, default=[],
                            help='Connection data-rate (default: %(default)s)')
        parser.add_argument('--host-id', dest='host_id', action='store', nargs="*", type=str, default=[],
                            help='TMCL host-id (default: %(default)s)')
        parser.add_argument('--module-id', dest='module_id', action='store', nargs="*", type=str, default=[],
                            help='TMCL module-id (default: %(default)s)')
        parser.add_argument('--check-getversion', dest='check_getversion', action='store_true',
                            help='Check availability using GET_FIRMWARE_VERSION TMCL command.')

        connectionType = connectionType.lower()

        if(not argList):
            if self.__debug:
                print("Using arguments from the command line")
            argList = sys.argv

        if type(argList) == str:
            argList = argList.split()
            if self.__debug:
                print("Splitting string:", argList)

        args = parser.parse_known_args(argList)[0]

        # Parse the command line
        if self.__debug:
            print("Commandline argument list: {0:s}".format(str(argList)))
            print("Parsed commandline arguments: {0:s}".format(str(args)))
            print()

        ### Interpret given arguments
        # Interfaces
        if(("any" in args.interface) and (len(args.interface) > 1)):
            raise ValueError("Interface selection 'any' must be used exclusively.")
        self.__interfaces = []
        if(args.interface[0] == "any"):
            self.__interfaces = available.values()
        else:
            self.__interfaces = [available[interface_arg] for interface_arg in args.interface]

        # Data rates
        self.__data_rates = args.data_rate
        for data_rate in self.__data_rates:
            if((data_rate == "d") or (data_rate == "any")):
                continue
            try:
                int(data_rate)
            except ValueError:
                raise ValueError("Invalid data rate {}.".format(data_rate))

        # Ports
        # Any port string is valid.
        if((("any" in args.port) or ("interactive" in args.port)) and (len(args.port) > 1)):
            raise ValueError("Port selections 'any' and 'interactive' must be used exclusively.")
        self.__ports = set(args.port)

        # No-Port
        for port in args.exclude:
            if port in ["any", "interactive"]:
                raise ValueError("Port blacklist (no-port) cannot use the special port: " + port)
        self.__no_port = set(args.exclude)

        # Host ID
        self.__host_ids = args.host_id
        for host_id in self.__host_ids:
            if(host_id == "d"):
                continue
            try:
                int(host_id)
            except ValueError:
                raise ValueError("Invalid host id {}.".format(host_id))

        # Module ID
        self.__module_ids = args.module_id
        for module_id in self.__module_ids:
            if(module_id == "d"):
                continue
            try:
                int(module_id)
            except ValueError:
                raise ValueError("Invalid module id {}.".format(module_id))

        # Construct all configs
        self.__configs = []
        for interface in self.__interfaces:
            # Get all available ports for interface
            ports = interface.available_ports()
            # If selected ports does matter
            if(not("any" in self.__ports)):
                # Filter for selected ports
                ports = ports.intersection(self.__ports)
            # Filter for non-excluded ports
            ports = ports.difference(self.__no_port)
            for port in ports:
                self.__configs.append({ "interface": interface, "port": port })
        for i in range(0, len(self.__data_rates)):
            if(self.__data_rates[i] != "d"):
                self.__configs[i]["data_rate"] = self.__data_rates[i]
        for i in range(0, len(self.__module_ids)):
            if(self.__module_ids[i] != "d"):
                self.__configs[i]["module_id"] = self.__module_ids[i]
        for i in range(0, len(self.__host_ids)):
            if(self.__host_ids[i] != "d"):
                self.__configs[i]["host_id"] = self.__host_ids[i]

        if self.__debug:
            print("Configurations:")
            for config in self.__configs:
                print(config)

    def connect(self, debug_interface=None):
        """
        Attempt to connect to a module with the stored connection parameters.

        Returns a connection instance of a class based on the tmcl_interface.
        Which class type gets returned depends on the interface used.

        If no connections are available or a connection attempt fails, a
        ConnectionError exception is raised

        Parameters:
            debug_interface:
                Type: bool, optional, default value: None
                Control whether the connection should be created in
                debug mode. A boolean value will enable or disable the debug mode,
                a None value will set the connections debug mode according to the
                ConnectionManagers debug mode.
        """

        connections = set()
        for config in self.__configs:
            try:
                connections.add(config.pop("interface")(**config))
            except ConnectionError as e:
                raise ConnectionError("Connection to config {} failed.".format(config)) from e
        return connections

    @staticmethod
    def _get_available_interfaces():
        from PyTrinamic.connections.dummy_tmcl_interface import dummy_tmcl_interface
        from PyTrinamic.connections.pcan_tmcl_interface import pcan_tmcl_interface
        from PyTrinamic.connections.socketcan_tmcl_interface import socketcan_tmcl_interface
        from PyTrinamic.connections.kvaser_tmcl_interface import kvaser_tmcl_interface
        from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
        from PyTrinamic.connections.uart_ic_interface import uart_ic_interface
        from PyTrinamic.connections.usb_tmcl_interface import usb_tmcl_interface
        from PyTrinamic.connections.pcan_CANopen_interface import pcan_CANopen_interface
        from PyTrinamic.connections.slcan_tmcl_interface import slcan_tmcl_interface
        from PyTrinamic.connections.kvaser_CANopen_interface import kvaser_CANopen_interface
        # All available interfaces
        return {
            "dummy_tmcl": dummy_tmcl_interface,
            "pcan_tmcl": pcan_tmcl_interface,
            "socketcan_tmcl": socketcan_tmcl_interface,
            "kvaser_tmcl": kvaser_tmcl_interface,
            "slcan_tmcl": slcan_tmcl_interface,
            "serial_tmcl": serial_tmcl_interface,
            "uart_ic": uart_ic_interface,
            "usb_tmcl": usb_tmcl_interface,
            "pcan_CANopen": pcan_CANopen_interface,
            "kvaser_CANopen": kvaser_CANopen_interface
        }

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
        return [x[0] for x in ConnectionManager._get_available_interfaces()]

if __name__ == "__main__":
    # Test if everything is working correctly

    print("Verifying interfaces list...\n")
    for interface in ConnectionManager._get_available_interfaces():
        if not hasattr(interface[1], "supportsTMCL"):
            raise NotImplementedError("Interface " + interface[0] + " is missing the supportsTMCL() function")
        if not hasattr(interface[1], "supportsCANopen"):
            raise NotImplementedError("Interface " + interface[0] + " is missing the supportsCANopen() function")
        if not hasattr(interface[1], "close"):
            raise NotImplementedError("Interface " + interface[0] + " is missing the close() function")
        if not hasattr(interface[1], "__enter__"):
            raise NotImplementedError("Interface " + interface[0] + " is missing the __enter__() function")
        if not hasattr(interface[1], "__exit__"):
            raise NotImplementedError("Interface " + interface[0] + " is missing the __exit__() function")
        if not hasattr(interface[1], "list"):
            raise NotImplementedError("Interface " + interface[0] + " is missing the list() function")

    print("List of interfaces: " + str(ConnectionManager.listInterfaces()) + "\n")

    print("Performing test run...\n")
    connectionManager = ConnectionManager()
    try:
        connection = connectionManager.connect()
        connectionManager.disconnect()
    except ConnectionError:
        print("Error: No connections available")

    print("Test run complete")
