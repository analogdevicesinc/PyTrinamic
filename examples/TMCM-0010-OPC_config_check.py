'''
Created on 30.12.2018

@author: ED
'''

if __name__ == '__main__':
    pass

import PyTrinamic
from PyTrinamic.SerialInterface import SerialInterface

PyTrinamic.showInfo()
PyTrinamic.showAvailableComPorts()

myInterface = SerialInterface('COM5')

print("Configuration:")
print("\tenabled:              " + str(myInterface.getAxisParameter(1, 0).value))
print("\tsupply voltage:       " + str(myInterface.getAxisParameter(0, 0).value / 10) + "V")
print("\tvoltage limit:        " + str(myInterface.getAxisParameter(2, 0).value / 10) + "V")
print("\thysteresis:           " + str(myInterface.getAxisParameter(3, 0).value / 10) + "V")
print("\tlower voltage limit:  " + str(myInterface.getAxisParameter(4, 0).value / 10) + "V")
print("\tbrake chopper active: " + str(myInterface.getAxisParameter(5, 0).value))
print("\tmain loops:           " + str(myInterface.getAxisParameter(200, 0).value))
print("\tUSB loops:            " + str(myInterface.getAxisParameter(201, 0).value))

myInterface.close()