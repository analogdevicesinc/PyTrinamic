#!/usr/bin/env python3
'''
Move a motor back and forth using the TMCM1260 module

Created on 07.07.2020

@author: JM
'''

import pytrinamic2
from pytrinamic2.connections.connection_manager import ConnectionManager
from pytrinamic2.modules.TMCM1260 import TMCM1260
import time

pytrinamic2.show_info()

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
Module_1260 = TMCM1260(myInterface)

print("Preparing parameters")
Module_1260.setMaxAcceleration(40000)
Module_1260.setMaxCurrent(50)
# Set moveBy() relative to the actual position
Module_1260.setAxisParameter(Module_1260.AP.relative_positioning_option, 1)

print("Rotating")
Module_1260.rotate(-20000)

time.sleep(5)

print("Stopping")
Module_1260.stop()

time.sleep(1);

print("Doubling moved distance")
Module_1260.moveBy(Module_1260.getActualPosition(), 10000)
Module_1260.getAxisParameter(Module_1260.AP.ActualPosition)
while not(Module_1260.positionReached()):
    pass

print("Furthest point reached")

time.sleep(1)

print("Moving back to 0")
Module_1260.moveTo(0, 20000)

# Wait until position 0 is reached
while not(Module_1260.positionReached()):
    pass

print("Reached Position 0")

myInterface.close()
