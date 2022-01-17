#!/usr/bin/env python3
'''
Move a motor back and forth using velocity and position mode of the TMC2224

Created on 07.02.2020

@author: JM
'''

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC2224_eval import TMC2224_eval


connectionManager = ConnectionManager()
myInterface = connectionManager.connect()

PyTrinamic.show_info()

TMC2224 = TMC2224_eval(myInterface)
TMC2224.showChipInfo()

DEFAULT_MOTOR = 0

print("Rotating")
TMC2224.rotate(DEFAULT_MOTOR, 1*11000)

time.sleep(2)

print("Stopping")
TMC2224.stop(DEFAULT_MOTOR)

time.sleep(3)

print("Moving back to 0")
TMC2224.moveTo(DEFAULT_MOTOR, 0, 10000)
 
# Wait until position 0 is reached
while TMC2224.getAxisParameter(TMC2224.APs.ActualPosition, DEFAULT_MOTOR) != 0:
    pass

print("Reached Position 0")

myInterface.close()
