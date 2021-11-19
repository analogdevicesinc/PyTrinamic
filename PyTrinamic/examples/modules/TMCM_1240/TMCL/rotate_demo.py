#!/usr/bin/env python3
'''
Move a motor back and forth using the TMCM-1240 module

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
module = TMCM_1240(myInterface)

print("Preparing parameters")
module.setMaxAcceleration(40000)
module.setMaxCurrent(50)

" set moveBy() relative to the actual position "
module.setAxisParameter(module.APs.relative_positioning_option, 1)

print("Rotating")
module.rotate(20000)
time.sleep(5)

print("Stopping")
module.stop()
time.sleep(1);

print("Double moved distance")
module.moveBy(module.getActualPosition(), 10000)
module.getAxisParameter(module.APs.ActualPosition)
while not(module.positionReached()):
    print("target position: " + str(module.getTargetPosition()) + "   actual position: " + str(module.getActualPosition()))
    time.sleep(0.2)

print("Furthest point reached")
time.sleep(3)

print("Moving back to 0")
module.moveTo(0, 20000)

" wait until position 0 is reached "
while not(module.positionReached()):
    print("target position: " + str(module.getTargetPosition()) + "   actual position: " + str(module.getActualPosition()))
    time.sleep(0.2)

print("Reached position 0")

myInterface.close()
print("Ready.")
