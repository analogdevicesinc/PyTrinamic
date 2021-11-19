#!/usr/bin/env python3
'''
Move a motor back and forth using velocity and position mode of the TMC2225

Created on 17.10.2019

@author: JM
'''

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC2225_eval import TMC2225_eval


connectionManager = ConnectionManager()
myInterface = connectionManager.connect()

PyTrinamic.showInfo()

TMC2225 = TMC2225_eval(myInterface)
TMC2225.showChipInfo()

DEFAULT_MOTOR = 0

print("Rotating")
TMC2225.rotate(DEFAULT_MOTOR, 1*27000)

time.sleep(5);

print("Stopping")
TMC2225.stop(DEFAULT_MOTOR)

time.sleep(1);

print("Moving back to 0")
TMC2225.moveTo(DEFAULT_MOTOR, 0, 18000)
 
# Wait until position 0 is reached
while TMC2225.getAxisParameter(TMC2225.APs.ActualPosition, DEFAULT_MOTOR) != 0:
    pass

print("Reached Position 0")

myInterface.close()
