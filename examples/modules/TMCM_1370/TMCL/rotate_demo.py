#!/usr/bin/env python3
'''
Move a motor back and forth using the TMCM1370 module

Created on 08.07.2020

@author: JM
'''

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1370.TMCM_1370 import TMCM_1370
import time

PyTrinamic.show_info()

connectionManager = ConnectionManager("--interface serial_tmcl")
myInterface = connectionManager.connect()
Module_1370 = TMCM_1370(myInterface)

DEFAULT_MOTOR = 0

print("Preparing parameters")
Module_1370.setMaxAcceleration(10000)

print("Rotating")
Module_1370.rotate(50000)

time.sleep(2);

print("Stopping")
Module_1370.stop()

time.sleep(1);

print("Doubling moved distance")
Module_1370.moveBy(Module_1370.getActualPosition(), 10000)
while not(Module_1370.positionReached()):
    print ("ActualPosition: %d" % Module_1370.getActualPosition())
    print ("TargetPosition: %d" % Module_1370.getTargetPosition())
    time.sleep(1)
    pass

print("Furthest point reached")

time.sleep(1)

print("Moving back to 0")
Module_1370.moveTo(0, 10000)

# Wait until position 0 is reached
while not(Module_1370.positionReached()):
    pass

print("Reached Position 0")

print()

myInterface.close()
