'''
Created on 30.12.2018

@author: ED
'''

import serial.tools.list_ports;

name = "PyTrinamic"
desc = "TRINAMIC's Python Technology Access Package"
VERSION = "0.1.6"

# USB Vendor and Product IDs
USB_IDS = [
    { # Landungsbrücke
        "VID": 0x2A3C,
        "PID": 0x0700
    },
    { # TMCM1460
        "VID": 0x16D0,
        "PID": 0x0461
    },
    { # TMC_CDC_DEV
        "VID": 0x2A3C,
        "PID": 0x0200
    },
    { # TMCM1160, TMCM1161
        "VID": 0x2A3C,
        "PID": 0x0100
    }
]

def showInfo():
    print(name + " - " + desc)

# Print all available Ports
def showAvailableComPorts(CAN=False, Serial=False, USB=False):
    ports = getAvailableComPorts(CAN, Serial, USB)
    print("Available COM ports: " + str(ports))

# Return a list of all available ports of the selected interfaces
def getAvailableComPorts(CAN=False, Serial=False, USB=False):
    if CAN == False and Serial == False and USB == False:
        raise ValueError

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
    connected = []
    for element in serial.tools.list_ports.comports():
        connected.append(element.device)

    return connected

# Return a list of all available USB ports with correct Vendor and Product IDs
def getAvailableUSBPorts():
    connected = []
    for element in serial.tools.list_ports.comports():
        for entry in USB_IDS:
            if entry["VID"] == element.vid and entry["PID"] == element.pid:
                connected.append(element.device)

    return connected

# Return a list of all available CAN ports
def getAvailableCANPorts():
    print("CAN support is not implemented yet")

    connected = []

    return connected

def firstAvailableComPort(CAN=False, Serial=False, USB=False):
    ports = getAvailableComPorts(CAN, Serial, USB)

    if len(ports) > 0:
        return ports[0]
    return None
