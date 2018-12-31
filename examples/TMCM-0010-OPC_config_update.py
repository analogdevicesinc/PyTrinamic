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

" enable break chopper "
myInterface.setAxisParameter(1, 0, 1)
myInterface.storeAxisParameter(1, 0)

" set voltage limit to 50V and hysteresis to 1V"
myInterface.setAxisParameter(2, 0, 500)
myInterface.storeAxisParameter(2, 0)

myInterface.setAxisParameter(3, 0, 10)
myInterface.storeAxisParameter(3, 0)

print("Configuration:")
print("\tenabled:              " + str(myInterface.getAxisParameter(1, 0).value))
print("\tvoltage limit:        " + str(myInterface.getAxisParameter(2, 0).value / 10) + "V")
print("\thysteresis:           " + str(myInterface.getAxisParameter(3, 0).value / 10) + "V")

myInterface.close()