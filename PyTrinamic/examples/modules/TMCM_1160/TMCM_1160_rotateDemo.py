#!/usr/bin/env python3
'''
Move a motor back and forth using the TMCM1160 module

Created on 22.05.2019

@author: LH
'''

import PyTrinamic
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
from PyTrinamic.modules.TMCM_1160 import TMCM_1160
import time

PyTrinamic.showInfo()

myInterface = serial_tmcl_interface(PyTrinamic.firstAvailableComPort(USB=True))
TMCM_1160 = TMCM_1160(myInterface)

DEFAULT_MOTOR = 0

print("Preparing parameters")
TMCM_1160.setMaxAcceleration(1000)

print("Rotating")
TMCM_1160.rotate(500)

time.sleep(2);

print("Stopping")
TMCM_1160.stop()

time.sleep(1);

print("Doubling moved distance")
TMCM_1160.moveBy(TMCM_1160.getActualPosition(), 500)

while not(TMCM_1160.positionReached()):
    pass

print("Furthest point reached")

time.sleep(1)

print("Moving back to 0")
TMCM_1160.moveTo(0, 1000)

# Wait until position 0 is reached
while not(TMCM_1160.positionReached()):
    pass

print("Reached Position 0")

print()

myInterface.close()
