#!/usr/bin/env python3
'''
Move a motor back and forth using the TMCM6212 module

Created on 28.02.2019

@author: JM
'''

import pytrinamic
from pytrinamic.connections.connection_manager import ConnectionManager
from pytrinamic.modules.TMCM6212 import TMCM6212
import time

pytrinamic.show_info()

connectionManager = ConnectionManager() # If no Interface is selected , the default interface is usb_tmcl
myInterface = connectionManager.connect()
Module_6212 = TMCM6212(myInterface)

DEFAULT_MOTOR = 0

print("Preparing parameters")
Module_6212.setMaxAcceleration(9000)

print("Rotating")
Module_6212.rotate(40000)

time.sleep(5);

print("Stopping")
Module_6212.stop()

print("ActualPostion") 
print(Module_6212.getActualPosition())
time.sleep(5);

print("Doubling moved distance")
Module_6212.moveBy(Module_6212.getActualPosition(), 50000)
Module_6212.getAxisParameter(Module_6212.AP.ActualPosition)
while not(Module_6212.positionReached()):
    pass

print("Furthest point reached")
print(Module_6212.getActualPosition())

time.sleep(5)

print("Moving back to 0")
Module_6212.moveTo(0, 100000)

# Wait until position 0 is reached
while not(Module_6212.positionReached()):
    pass

print("Reached Position 0")

print()

myInterface.close()