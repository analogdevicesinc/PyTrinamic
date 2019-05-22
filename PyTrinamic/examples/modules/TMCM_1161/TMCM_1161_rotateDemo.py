#!/usr/bin/env python3
'''
Move a motor back and forth using the TMCM1161 module

Created on 22.05.2019

@author: LH
'''

import PyTrinamic
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
from PyTrinamic.modules.TMCM_1161 import TMCM_1161
import time

PyTrinamic.showInfo()

myInterface = serial_tmcl_interface(PyTrinamic.firstAvailableComPort(USB=True))
TMCM_1161 = TMCM_1161(myInterface)

DEFAULT_MOTOR = 0

print("Preparing parameters")
TMCM_1161.setMaxAcceleration(1000)

print("Rotating")
TMCM_1161.rotate(500)

time.sleep(2);

print("Stopping")
TMCM_1161.stop()

time.sleep(1);

print("Doubling moved distance")
TMCM_1161.moveBy(TMCM_1161.getActualPosition(), 500)

while not(TMCM_1161.positionReached()):
    pass

print("Furthest point reached")

time.sleep(1)

print("Moving back to 0")
TMCM_1161.moveTo(0, 1000)

# Wait until position 0 is reached
while not(TMCM_1161.positionReached()):
    pass

print("Reached Position 0")

print()

myInterface.close()
