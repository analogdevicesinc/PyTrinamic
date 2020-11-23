#!/usr/bin/env python3
'''
Move a motor back and forth using velocity and position mode of the TMC2660

Created on 07.11.2019

@author: JM
'''

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManagerPC import ConnectionManagerPC
from PyTrinamic.evalboards.TMC2660_eval import TMC2660_eval

myInterface = ConnectionManagerPC(interfaces=["usb_tmcl"]).connect()[0]

PyTrinamic.showInfo()

TMC2660 = TMC2660_eval(myInterface)
TMC2660.showChipInfo()

DEFAULT_MOTOR = 0

print("Rotating")
TMC2660.rotate(DEFAULT_MOTOR, 10*25600)

time.sleep(2);

print("Stopping")
TMC2660.stop(DEFAULT_MOTOR)

time.sleep(1);

print("Moving back to 0")
TMC2660.moveTo(DEFAULT_MOTOR, 0, 10*25600)

# Wait until position 0 is reached
while TMC2660.getAxisParameter(TMC2660.APs.ActualPosition, DEFAULT_MOTOR) != 0:
    pass

print("Reached Position 0")

myInterface.close()
