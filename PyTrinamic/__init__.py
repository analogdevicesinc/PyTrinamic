'''
Created on 30.12.2018

@author: ED
'''

import serial.tools.list_ports;

name = "PyTrinamic"
desc = "TRINAMIC's Python Technology Access Package"

def showInfo():
    print(name + " - " + desc)

def showAvailableComPorts():
    comlist = serial.tools.list_ports.comports()
    connected = []
    for element in comlist:
        connected.append(element.device)
       
    print("Available COM ports: " + str(connected))
    return 0;

def firstAvailableComPort():
    comlist = serial.tools.list_ports.comports()
    connected = []
    for element in comlist:
        connected.append(element.device)
        return element.device;
