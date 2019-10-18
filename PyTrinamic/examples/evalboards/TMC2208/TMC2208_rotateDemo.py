#!/usr/bin/env python3
'''
Move a motor back and forth using velocity and position mode of the TMC2208

Created on 17.10.2019

@author: JM
'''

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC2208_eval import TMC2208_eval


connectionManager = ConnectionManager()
myInterface = connectionManager.connect()

PyTrinamic.showInfo()

TMC2208 = TMC2208_eval(myInterface)

DEFAULT_MOTOR = 0

print("Rotating")
TMC2208.rotate(DEFAULT_MOTOR, 1*11000)

time.sleep(2);

print("Stopping")
TMC2208.stop(DEFAULT_MOTOR)

time.sleep(1);

print("Moving back to 0")
TMC2208.moveTo(DEFAULT_MOTOR, 0, 4000)
 
# Wait until position 0 is reached
while TMC2208.getAxisParameter(TMC2208.APs.ActualPosition, DEFAULT_MOTOR) != 0:
    pass

print("Reached Position 0")

myInterface.close()
