'''
Created on 28.05.2019

@author: LH
'''

import sys
import argparse


class ConnectionManager():

    class InteractiveReturn(object):
        pass
    class InteractiveAbort(InteractiveReturn):
        pass

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

        print(parsed.interactive)

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
    def __interactive_interface():
        while(True):
            print("Available interfaces:")
            available = list(ConnectionManager.get_available_interfaces().keys())
            for i in range(0, len(available)):
                print("\t[{}] {}".format(i, available[i]))
            print("Options:")
            print("\t0 .. {}: Select the n-th interface.".format(max(len(available) - 1, 0)))
            print("\tr: Refresh list.")
            print("\tx: Abort selection.")
            selection = input(": ")
            if(selection == "r"):
                continue
            elif(selection == "x"):
                return ConnectionManager.InteractiveAbort
            return available[int(selection)]

    @staticmethod
    def __interactive_port(interface):
        while(True):
            print("Available ports for interface:")
            ports = list(interface.available_ports())
            for i in range(0, len(ports)):
                print("\t[{}] {}".format(i, ports[i]))
            print("Options:")
            print("\t0 .. {}: Select the n-th port.".format(max(len(ports) - 1, 0)))
            print("\tr: Refresh list.")
            print("\tx: Abort selection.")
            selection = input(": ")
            if(selection == "r"):
                continue
            elif(selection == "x"):
                return ConnectionManager.InteractiveAbort
            return ports[int(selection)]

    @staticmethod
    def __interactive_data_rate(interface):
        while(True):
            print("Enter the data rate to be used with this connection. Default: {}.".format(interface.DEFAULT_DATA_RATE))
            print("Options:")
            print("\tn: Choose n as default data rate.")
            print("\td: Go with the defaults of this connection interface.")
            print("\tx: Abort selection.")
            selection = input(": ")
            if(selection == "d"):
                return None
            elif(selection == "x"):
                return ConnectionManager.InteractiveAbort
            return int(selection)

    @staticmethod
    def __interactive_host_id(interface):
        while(True):
            print("Enter the default Host ID to be used with this connection. Default: {}.".format(interface.DEFAULT_HOST_ID))
            print("Options:")
            print("\tn: Choose n as default Host ID.")
            print("\td: Go with the defaults of this connection interface.")
            print("\tx: Abort selection.")
            selection = input(": ")
            if(selection == "d"):
                return None
            elif(selection == "x"):
                return ConnectionManager.InteractiveAbort
            return int(selection)

    @staticmethod
    def __interactive_module_id(interface):
        while(True):
            print("Enter the default Module ID to be used with this connection. Default: {}.".format(interface.DEFAULT_MODULE_ID))
            print("Options:")
            print("\tn: Choose n as default Module ID.")
            print("\td: Go with the defaults of this connection interface.")
            print("\tx: Abort selection.")
            selection = input(": ")
            if(selection == "d"):
                return None
            elif(selection == "x"):
                return ConnectionManager.InteractiveAbort
            return int(selection)

    @staticmethod
    def interactive(params):
        while(True):
            available = ConnectionManager.get_available_interfaces()
            interface = ConnectionManager.__interactive_interface()
            if(interface == ConnectionManager.InteractiveAbort):
                break
            else:
                params["interfaces"].append(interface)
            interface = available[interface]
            port = ConnectionManager.__interactive_port(interface)
            if(port == ConnectionManager.InteractiveAbort):
                break
            else:
                params["ports"].append(port)
            data_rate = ConnectionManager.__interactive_data_rate(interface)
            if(data_rate == ConnectionManager.InteractiveAbort):
                break
            elif(type(data_rate) == int):
                params["data_rates"].append(data_rate)
            host_id = ConnectionManager.__interactive_host_id(interface)
            if(host_id == ConnectionManager.InteractiveAbort):
                break
            elif(type(host_id) == int):
                params["host_ids"].append(host_id)
            module_id = ConnectionManager.__interactive_module_id(interface)
            if(module_id == ConnectionManager.InteractiveAbort):
                break
            elif(type(module_id) == int):
                params["module_ids"].append(module_id)

            print("Connection parameters: \n{}".format(params))

            another = input("Do you want to add another connection (y/N): ")
            if(another.lower() != "y"):
                break

        return params
