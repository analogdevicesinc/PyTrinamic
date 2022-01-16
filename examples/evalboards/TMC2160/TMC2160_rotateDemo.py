#!/usr/bin/env python3
'''
Move a motor back and forth using velocity and position mode of the TMC2160

Created on 23.10.2019

@author: JM
'''

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC2160_eval import TMC2160_eval


connectionManager = ConnectionManager()
myInterface = connectionManager.connect()

PyTrinamic.showInfo()

TMC2160 = TMC2160_eval(myInterface)
TMC2160.showChipInfo()

DEFAULT_MOTOR = 0

print("Rotating")
TMC2160.rotate(DEFAULT_MOTOR, 12800)

time.sleep(5)

print("Stopping")
TMC2160.stop(DEFAULT_MOTOR)

time.sleep(1)

print("Moving back to 0")
TMC2160.moveTo(DEFAULT_MOTOR, 0, 10000)
 
# Wait until position 0 is reached
while TMC2160.getAxisParameter(TMC2160.APs.ActualPosition, DEFAULT_MOTOR) != 0:
    pass

print("Reached Position 0")

myInterface.close()
