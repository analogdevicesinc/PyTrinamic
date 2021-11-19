#!/usr/bin/env python3
'''
Move a motor back and forth using velocity and position mode of the TMC6300

Created on 17.04.2020

@author: JM
'''

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC6300_eval import TMC6300_eval

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()

PyTrinamic.showInfo()

TMC6300 = TMC6300_eval(myInterface)
TMC6300.showChipInfo()

DEFAULT_MOTOR = 0

TMC6300.ICStandby(DEFAULT_MOTOR, 0)
TMC6300.setCommutationMode(DEFAULT_MOTOR, 0)

print()
print("Begin Openloop demo")
print("Rotating")
TMC6300.setTargetPWM(DEFAULT_MOTOR, 6000)

time.sleep(3);

print("Stopping")
TMC6300.setTargetPWM(DEFAULT_MOTOR, 0)

time.sleep(2)

print("Rotating back")
TMC6300.setTargetPWM(DEFAULT_MOTOR, -6000)

time.sleep(3);

print("Stopping")
TMC6300.setTargetPWM(DEFAULT_MOTOR, 0)

myInterface.close()
