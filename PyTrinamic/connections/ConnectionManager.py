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

    @staticmethod
    def from_args(args=None):
        parser = argparse.ArgumentParser(description='ConnectionManager to setup connections dynamically and interactively')
        parser.add_argument('--interface', dest='interface', action='store', nargs="*", type=str, choices=ConnectionManager.get_available_interfaces().keys(), default=[],
                            help='Connection interface (default: %(default)s)')
        parser.add_argument('--port', dest='port', action='store', nargs="*", type=str, default=[],
                            help='Connection port (default: %(default)s, n: Use n-th available port, "any": Use any available port, "interactive": Interactive dialogue for port selection, String: Attempt to use the provided string - e.g. COM6 or /dev/tty3)')
        parser.add_argument('--exclude', dest='exclude', action='append', nargs='*', type=str, default=[],
                            help='Exclude ports')
        parser.add_argument('--data-rate', dest='data_rate', action='store', nargs="*", type=str, default=[],
                            help='Connection data-rate (default: %(default)s)')
        parser.add_argument('--host-id', dest='host_id', action='store', nargs="*", type=str, default=[],
                            help='TMCL host-id (default: %(default)s)')
        parser.add_argument('--module-id', dest='module_id', action='store', nargs="*", type=str, default=[],
                            help='TMCL module-id (default: %(default)s)')
        parser.add_argument('--interactive', dest='interactive', action='store_true',
                            help='TMCL module-id (default: %(default)s)')
        parsed = parser.parse_known_args(args)[0]

        params = {
            "interfaces": parsed.interface,
            "ports": parsed.port,
            "data_rates": parsed.data_rate,
            "exclude": parsed.exclude,
            "host_ids": parsed.host_id,
            "module_ids": parsed.module_id
        }

        if(parsed.interactive):
            params = ConnectionManager.interactive(params)

        return ConnectionManager(**params)


    def __init__(self, interfaces=[], ports=[], data_rates=[], exclude=[], host_ids=[], module_ids=[], debug=False):
        available = self.get_available_interfaces()
        # Filter for selected interface types
        interfaces = {available[key] for key in interfaces} if interfaces else set(available.values())
        ports = set(ports)
        self.configs = [{"interface": interface, "port": port} for interface in interfaces for port in (ports.intersection(interface.available_ports()).difference(exclude) if ports else interface.available_ports().difference(exclude))]
        for i in range(0, max(len(data_rates), len(host_ids), len(module_ids))):
            if(i >= len(self.configs)):
                break
            if(i < len(data_rates)):
                if(data_rates[i] != "d"):
                    self.configs[i]["data_rate"] = data_rates[i]
            if(i < len(host_ids)):
                if(host_ids[i] != "d"):
                    self.configs[i]["host_id"] = host_ids[i]
            if(i < len(module_ids)):
                if(module_ids[i] != "d"):
                    self.configs[i]["module_id"] = module_ids[i]

    def connect(self):

        connections = set()
        for config in self.configs:
            try:
                connections.add(config.pop("interface")(**config))
            except ConnectionError as e:
                raise ConnectionError("Connection to config {} failed.".format(config)) from e
        return connections

    @staticmethod
    def get_available_interfaces():
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

    @staticmethod
    def __interactive

    @staticmethod
    def interactive(params):
        while True:
            print("Available interfaces:")
            available = ConnectionManager.get_available_interfaces().keys()
            for i in range(0, len(available)):
                print("\t[{}] {}".format(i, available[i]))
            print("Options:")
            print("\t0 .. {}: Select the n-th interface.".format(len(available)))
            print("\t<interface_name>: Select the interface with the name <interface_name>.")
            print("\tr: Refresh list.")
            print("\tx: Abort selection.")
            selection = input(": ")
            if(selection == "r"):
                continue
            if(selection)

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
