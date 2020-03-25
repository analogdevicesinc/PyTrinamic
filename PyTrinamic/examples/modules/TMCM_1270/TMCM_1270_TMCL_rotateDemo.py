#!/usr/bin/env python3
'''
Move a motor back and forth using the TMCM1270 module

Created on 03.12.2019

@author: JM
'''

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1270.TMCM_1270 import TMCM_1270
import time

PyTrinamic.showInfo()

connectionManager = ConnectionManager("--interface pcan_tmcl") #This setting is configurated for PCAN , if you want to use another Connection please change this line
myInterface = connectionManager.connect()
Module_1270 = TMCM_1270(myInterface)

DEFAULT_MOTOR = 0

print("Preparing parameters")
Module_1270.setMaxAcceleration(9000)

print("Rotating")
Module_1270.rotate(40000)

time.sleep(5);

print("Stopping")
Module_1270.stop()

print("ActualPostion") 
print(Module_1270.getActualPosition())
time.sleep(5);

print("Doubling moved distance")
Module_1270.moveBy(Module_1270.getActualPosition(), 50000)
Module_1270.getAxisParameter(Module_1270.APs.ActualPosition)
while not(Module_1270.positionReached()):
    pass

print("Furthest point reached")
print(Module_1270.getActualPosition())

time.sleep(5)

print("Moving back to 0")
Module_1270.moveTo(0, 100000)

# Wait until position 0 is reached
while not(Module_1270.positionReached()):
    pass

print("Reached Position 0")

print()

myInterface.close()
