#!/usr/bin/env python3
'''
Move a motor back and forth using velocity and position mode of the TMC2209

Created on 18.10.2019

@author: JM
'''

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC2209_eval import TMC2209_eval


connectionManager = ConnectionManager()
myInterface = connectionManager.connect()

PyTrinamic.showInfo()

TMC2209 = TMC2209_eval(myInterface)
TMC2209.showChipInfo()

DEFAULT_MOTOR = 0

print("Rotating")
TMC2209.rotate(DEFAULT_MOTOR, 1*4000)

time.sleep(2);

print("Stopping")
TMC2209.stop(DEFAULT_MOTOR)

time.sleep(1);

print("Moving back to 0")
TMC2209.moveTo(DEFAULT_MOTOR, 0, 2000)
 
# Wait until position 0 is reached
while TMC2209.getAxisParameter(TMC2209.APs.ActualPosition, DEFAULT_MOTOR) != 0:
    pass

print("Reached Position 0")

myInterface.close()
