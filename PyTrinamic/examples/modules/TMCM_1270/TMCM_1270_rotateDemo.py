#!/usr/bin/env python3
'''
Move a motor back and forth using the TMCM1270 module

Created on 03.12.2019

@author: JM
'''

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM_1270 import TMCM_1270
import time

PyTrinamic.showInfo()

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
TMCM_1270 = TMCM_1270(myInterface)

DEFAULT_MOTOR = 0

print("Preparing parameters")
TMCM_1270.setMaxAcceleration(9000)

print("Rotating")
TMCM_1270.rotate(40000)

time.sleep(5);

print("Stopping")
TMCM_1270.stop()

print("ActualPostion") 
print(TMCM_1270.getActualPosition())
time.sleep(5);

print("Doubling moved distance")
TMCM_1270.moveBy(TMCM_1270.getActualPosition(), 50000)
TMCM_1270.getAxisParameter(TMCM_1270.APs.ActualPosition)
while not(TMCM_1270.positionReached()):
    pass

print("Furthest point reached")
print(TMCM_1270.getActualPosition())

time.sleep(5)

print("Moving back to 0")
TMCM_1270.moveTo(0, 100000)

# Wait until position 0 is reached
while not(TMCM_1270.positionReached()):
    pass

print("Reached Position 0")

print()

myInterface.close()
