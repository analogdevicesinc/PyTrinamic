#!/usr/bin/env python3
'''
Move a motor back and forth using the TMCM1240 module

Created on 21.09.2020

@author: AA
'''

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1240.TMCM_1240 import TMCM_1240
import time

PyTrinamic.showInfo()

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
Module_1240 = TMCM_1240(myInterface)

print("Preparing parameters")
Module_1240.setMaxAcceleration(40000)
Module_1240.setMaxCurrent(50)
# Set moveBy() relative to the actual position
Module_1240.setAxisParameter(Module_1240.APs.relative_positioning_option, 1)

print("Rotating")
Module_1240.rotate(20000)

time.sleep(5)

print("Stopping")
Module_1240.stop()

time.sleep(1);

print("Doubling moved distance")
Module_1240.moveBy(Module_1240.getActualPosition(), 10000)
Module_1240.getAxisParameter(Module_1240.APs.ActualPosition)
while not(Module_1240.positionReached()):
    pass

print("Furthest point reached")

time.sleep(1)

print("Moving back to 0")
Module_1240.moveTo(0, 20000)

# Wait until position 0 is reached
while not(Module_1240.positionReached()):
    pass

print("Reached Position 0")

myInterface.close()
