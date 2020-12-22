'''
Created on 23.10.2020

@author: LK
'''

from PyTrinamic.connections.ConnectionManager import ConnectionManager
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

class ConnectionManagerPC(ConnectionManager):

    @staticmethod
    def interactive():
        params = {
            "interfaces": [],
            "ports": [],
            "data_rates": [],
            "exclude": [],
            "host_ids": [],
            "module_ids": []
        }

        return ConnectionManagerPC(**ConnectionManager._interactive(ConnectionManagerPC, params))

    @staticmethod
    def from_args(args=None):
        return ConnectionManager.from_args(ConnectionManagerPC, args)

    @staticmethod
    def get_available_interfaces():
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
