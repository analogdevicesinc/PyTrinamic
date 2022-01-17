#!/usr/bin/env python3
'''
Move a motor back and forth using the TMCM1161 module

Created on 22.05.2019

@author: LH
'''

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1161.TMCM_1161 import TMCM_1161
import time

PyTrinamic.show_info()

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
Module_1161 = TMCM_1161(myInterface)

DEFAULT_MOTOR = 0

print("Preparing parameters")
Module_1161.setMaxAcceleration(1000)

print("Rotating")
Module_1161.rotate(500)

time.sleep(2);

print("Stopping")
Module_1161.stop()

time.sleep(1);

print("Doubling moved distance")
Module_1161.moveBy(Module_1161.getActualPosition(), 500)
Module_1161.getAxisParameter(Module_1161.AP.ActualPosition)
while not(Module_1161.positionReached()):
    pass

print("Furthest point reached")

time.sleep(1)

print("Moving back to 0")
Module_1161.moveTo(0, 1000)

# Wait until position 0 is reached
while not(Module_1161.positionReached()):
    pass

print("Reached Position 0")

print()

myInterface.close()
