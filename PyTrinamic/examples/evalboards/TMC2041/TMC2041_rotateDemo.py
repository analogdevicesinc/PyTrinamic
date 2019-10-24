#!/usr/bin/env python3
'''
Move a motor back and forth using velocity and position mode of the TMC2041

Created on 24.10.2019

@author: JM
'''

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC2041_eval import TMC2041_eval

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()

PyTrinamic.showInfo()

TMC2041 = TMC2041_eval(myInterface)

DEFAULT_MOTOR = 0

print("Rotating")
TMC2041.rotate(DEFAULT_MOTOR, 20*51200)

time.sleep(5);

print("Stopping")
TMC2041.stop(DEFAULT_MOTOR)

time.sleep(1);

print("Moving back to 0")
TMC2041.moveTo(DEFAULT_MOTOR, 0, 35000)
 
# Wait until position 0 is reached
while TMC2041.getAxisParameter(TMC2041.APs.ActualPosition, DEFAULT_MOTOR) != 0:
    pass

print("Reached Position 0")

myInterface.close()