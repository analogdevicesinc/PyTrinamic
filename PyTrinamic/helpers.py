'''
Created on 09.01.2019

@author: LK
'''

from PyTrinamic import name, desc

def v_func(verbosity, minimum, func):
    if(verbosity >= minimum):
        func()

class TMC_helpers(object):

    @staticmethod
    def field_get(data, mask, shift):
        return (data & mask) >> shift

    @staticmethod
    def field_set(data, mask, shift, value):
        return (data & (~mask)) | ((value << shift) & mask)

    @staticmethod
    def toSigned32(x):
        m = x & 0xffffffff
        return (m ^ 0x80000000) - 0x80000000

    @staticmethod
    def showInfo():
        print(name + " - " + desc)

    @staticmethod
    def getComPort(name, return_default=True, CAN=False, Serial=False, USB=False):
        ports = [p for p in getAvailableComPorts(CAN, Serial, USB) if str(p) == name]
        if(ports):
            return ports[0]
        return (firstAvailableComPort(CAN, Serial, USB) if return_default else None)

    # Print all available Ports
    @staticmethod
    def showAvailableComPorts(CAN=False, Serial=False, USB=False):
        ports = getAvailableComPorts(CAN, Serial, USB)
        print("Available COM ports: " + str(ports))

    # Return a list of all available ports of the selected interfaces
    @staticmethod
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
    @staticmethod
    def getAvailableSerialPorts():
        return serial_tmcl_interface.list()

    # Return a list of all available USB ports with correct Vendor and Product IDs
    @staticmethod
    def getAvailableUSBPorts():
        return usb_tmcl_interface.list()

    # Return a list of all available CAN ports
    @staticmethod
    def getAvailableCANPorts():
        return pcan_tmcl_interface.list()

    @staticmethod
    def firstAvailableComPort(CAN=False, Serial=False, USB=False):
        ports = getAvailableComPorts(CAN, Serial, USB)

        if len(ports) > 0:
            return ports[0]
        return None
