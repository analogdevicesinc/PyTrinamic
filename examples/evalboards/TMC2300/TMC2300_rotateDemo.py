#!/usr/bin/env python3
'''
Move a motor back and forth using velocity and position mode of the TMC2300

Created on 27.03.2020

@author: JM
'''

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC2300_eval import TMC2300_eval

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()

PyTrinamic.showInfo()

TMC2300 = TMC2300_eval(myInterface)
TMC2300.showChipInfo()

DEFAULT_MOTOR = 0

TMC2300.ICStandby(DEFAULT_MOTOR, 0)

TMC2300.setMicrostepResolution(DEFAULT_MOTOR, 256)

print("Rotating")
TMC2300.rotate(DEFAULT_MOTOR, 10*25600)

time.sleep(2)

print("Stopping")
TMC2300.stop(DEFAULT_MOTOR)

time.sleep(1)

print("Moving back to 0")
TMC2300.moveTo(DEFAULT_MOTOR, 0, 10*25600)
 
# Wait until position 0 is reached
while TMC2300.getAxisParameter(TMC2300.APs.ActualPosition, DEFAULT_MOTOR) != 0:
    pass

print("Reached Position 0")

myInterface.close()
