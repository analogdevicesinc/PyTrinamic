#!/usr/bin/env python3
'''
Move a motor back and forth using the TMCM1260 module

Created on 07.07.2020

@author: JM
'''

import PyTrinamic
from PyTrinamic.connections.ConnectionManagerPC import ConnectionManagerPC
from PyTrinamic.modules.TMCM1260.TMCM_1260 import TMCM_1260
import time

PyTrinamic.showInfo()

myInterface = ConnectionManagerPC(interfaces=["usb_tmcl"]).connect()[0]
Module_1260 = TMCM_1260(myInterface)

print("Preparing parameters")
Module_1260.setMaxAcceleration(40000)
Module_1260.setMaxCurrent(50)
# Set moveBy() relative to the actual position
Module_1260.setAxisParameter(Module_1260.APs.relative_positioning_option, 1)

print("Rotating")
Module_1260.rotate(-20000)

time.sleep(5)

print("Stopping")
Module_1260.stop()

time.sleep(1);

print("Doubling moved distance")
Module_1260.moveBy(Module_1260.getActualPosition(), 10000)
Module_1260.getAxisParameter(Module_1260.APs.ActualPosition)
while not(Module_1260.positionReached()):
    pass

print("Furthest point reached")

time.sleep(1)

print("Moving back to 0")
Module_1260.moveTo(0, 20000)

# Wait until position 0 is reached
while not(Module_1260.positionReached()):
    pass

print("Reached Position 0")

myInterface.close()
