#!/usr/bin/env python3
'''
Move a motor back and forth using the TMCM1160 module

Created on 22.05.2019

@author: LH
'''

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM_1160 import TMCM_1160
import time

PyTrinamic.show_info()

connectionManager = ConnectionManager("--interface pcan_tmcl") #This setting is configurated for PCAN , if you want to use another Connection please change this line
myInterface = connectionManager.connect()
Module_1160 = TMCM_1160(myInterface)

DEFAULT_MOTOR = 0

print("Preparing parameters")
Module_1160.setMaxAcceleration(1000)

print("Rotating")
Module_1160.rotate(500)

time.sleep(2);

print("Stopping")
Module_1160.stop()

time.sleep(1);

print("Doubling moved distance")
Module_1160.moveBy(Module_1160.getActualPosition(), 500)
Module_1160.getAxisParameter(Module_1160.AP.ActualPosition)
while not(Module_1160.positionReached()):
    pass

print("Furthest point reached")

time.sleep(1)

print("Moving back to 0")
Module_1160.moveTo(0, 1000)

# Wait until position 0 is reached
while not(Module_1160.positionReached()):
    pass

print("Reached Position 0")

print()

myInterface.close()
