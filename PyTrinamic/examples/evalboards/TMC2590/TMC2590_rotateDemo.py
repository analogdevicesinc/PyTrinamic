#!/usr/bin/env python3
'''
Created on 07.02.2020

@author: JM
'''

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManagerPC import ConnectionManagerPC
from PyTrinamic.evalboards.TMC2590_eval import TMC2590_eval

myInterface = ConnectionManagerPC(interfaces=["usb_tmcl"]).connect()[0]

PyTrinamic.showInfo()

TMC2590 = TMC2590_eval(myInterface)
TMC2590.showChipInfo()

DEFAULT_MOTOR = 0

print("Rotating")
TMC2590.rotate(DEFAULT_MOTOR, 10*25600)

time.sleep(2);

print("Stopping")
TMC2590.stop(DEFAULT_MOTOR)

time.sleep(1);

print("Moving back to 0")
TMC2590.moveTo(DEFAULT_MOTOR, 0, 10*25600)

# Wait until position 0 is reached
while TMC2590.getAxisParameter(TMC2590.APs.ActualPosition, DEFAULT_MOTOR) != 0:
    pass

print("Reached Position 0")

myInterface.close()
