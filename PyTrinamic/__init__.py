'''
Created on 30.12.2018

@author: ED
'''

from PyTrinamic.connections.pcan_tmcl_interface import pcan_tmcl_interface
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
from PyTrinamic.connections.usb_tmcl_interface import usb_tmcl_interface

name = "PyTrinamic"
desc = "TRINAMIC's Python Technology Access Package"
__version__ = "0.1.12"

def showInfo():
    print(name + " - " + desc)

def getComPort(name, return_default=True, CAN=False, Serial=False, USB=False):
    ports = [p for p in getAvailableComPorts(CAN, Serial, USB) if str(p) == name]
    if(ports):
        return ports[0]
    return (firstAvailableComPort(CAN, Serial, USB) if return_default else None)

# Print all available Ports
def showAvailableComPorts(CAN=False, Serial=False, USB=False):
    ports = getAvailableComPorts(CAN, Serial, USB)
    print("Available COM ports: " + str(ports))

# Return a list of all available ports of the selected interfaces
def getAvailableComPorts(CAN=False, Serial=False, USB=False):
    if CAN == False and Serial == False and USB == False:
        raise ValueError()

    connected = []

    if CAN:
        connected = connected + getAvailableCANPorts()

    if Serial:
        connected = connected + getAvailableSerialPorts()

    if USB:
        connected = connected + getAvailableUSBPorts()

    return sorted(list(set(connected)))

# Return a list of all available serial ports
def getAvailableSerialPorts():
    return serial_tmcl_interface.list()

# Return a list of all available USB ports with correct Vendor and Product IDs
def getAvailableUSBPorts():
    return usb_tmcl_interface.list()

# Return a list of all available CAN ports
def getAvailableCANPorts():
    return pcan_tmcl_interface.list()

def firstAvailableComPort(CAN=False, Serial=False, USB=False):
    ports = getAvailableComPorts(CAN, Serial, USB)

    if len(ports) > 0:
        return ports[0]
    return None
