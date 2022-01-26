#!/usr/bin/env python3
'''
Move a motor back and forth using the TMCM3110 module

Created on 05.06.2020

@author: JM
'''

import pytrinamic
from pytrinamic.connections.connection_manager import ConnectionManager
from pytrinamic.modules.TMCM3110 import TMCM3110
import time

pytrinamic.show_info()

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
Module_3110 = TMCM3110(myInterface)

motor = 1

print("Preparing parameters")
Module_3110.setMaxAcceleration(motor, 1000)

print("Rotating")
Module_3110.rotate(motor, 500)

time.sleep(2);

print("Stopping")
Module_3110.stop(motor)

time.sleep(1);

print("Doubling moved distance")
Module_3110.moveBy(motor, Module_3110.getActualPosition(motor), 500)
Module_3110.getAxisParameter(Module_3110.AP.ActualPosition, motor)
while not(Module_3110.positionReached(motor)):
    pass

print("Furthest point reached")

time.sleep(1)

print("Moving back to 0")
Module_3110.moveTo(motor, 1000)

# Wait until position 0 is reached
while not(Module_3110.positionReached(motor)):
    pass

print("Reached Position 0")

print()

myInterface.close()
