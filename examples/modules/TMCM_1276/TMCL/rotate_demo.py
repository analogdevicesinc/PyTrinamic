#!/usr/bin/env python3
'''
Move a motor back and forth using the TMCM1276 module

Created on 18.11.2019

@author: JM
'''

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1276.TMCM_1276 import TMCM_1276
import time

PyTrinamic.show_info()

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
Module_1276 = TMCM_1276(myInterface)

DEFAULT_MOTOR = 0

print("Preparing parameters")
Module_1276.setMaxAcceleration(9000)

print("Rotating")
Module_1276.rotate(40000)

time.sleep(5);

print("Stopping")
Module_1276.stop()

print("ActualPostion") 
print(Module_1276.getActualPosition())
time.sleep(5);

print("Doubling moved distance")
Module_1276.moveBy(Module_1276.getActualPosition(), 50000)
Module_1276.getAxisParameter(Module_1276.AP.ActualPosition)
while not(Module_1276.positionReached()):
    pass

print("Furthest point reached")
print(Module_1276.getActualPosition())

time.sleep(5)

print("Moving back to 0")
Module_1276.moveTo(0, 100000)

# Wait until position 0 is reached
while not(Module_1276.positionReached()):
    pass

print("Reached Position 0")

print()

myInterface.close()
