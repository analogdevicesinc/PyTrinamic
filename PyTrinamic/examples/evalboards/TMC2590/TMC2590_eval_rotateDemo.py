#!/usr/bin/env python3
'''
Created on 07.02.2020

@author: JM
'''

if __name__ == '__main__':
    pass

import time
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC2590_eval import TMC2590_eval

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()

# Create an TMC2590-Eval class which communicates over the Landungsbruecke via TMCL
TMC2590 = TMC2590_eval(myInterface)

" read ChipInfo "

TMC2590.showChipInfo()

DEFAULT_MOTOR = 0

#TMC2590.setAxisParameter(TMC2590.APs.MaxVelocity,     DEFAULT_MOTOR, 1000)
TMC2590.setAxisParameter(TMC2590.APs.MaxAcceleration, DEFAULT_MOTOR, 10000)

print("Rotating")
TMC2590.rotate(DEFAULT_MOTOR, 30*25600)

time.sleep(10);

print("Stopping")
TMC2590.stop(DEFAULT_MOTOR)

time.sleep(1);

print("Moving back to 0")
TMC2590.moveTo(DEFAULT_MOTOR, 0, 30*25600)
 
# Wait until position 0 is reached
while TMC2590.getAxisParameter(TMC2590.APs.ActualPosition, DEFAULT_MOTOR) != 0:
    pass

print("Reached Position 0") 

myInterface.close()