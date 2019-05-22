#!/usr/bin/env python3
'''
Move a motor back and forth using the TMCM6212 module

Created on 22.05.2019

@author: LH
'''

import PyTrinamic
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
from PyTrinamic.modules.TMCM_6212 import TMCM_6212
import time

PyTrinamic.showInfo()

myInterface = serial_tmcl_interface(PyTrinamic.firstAvailableComPort(USB=True))
TMCM_6212 = TMCM_6212(myInterface)

DEFAULT_MOTOR = 0
VELOCITY      = 25000

print("Preparing parameters")
TMCM_6212.setMaxAcceleration(DEFAULT_MOTOR, 100000)

print("Rotating")
TMCM_6212.rotate(DEFAULT_MOTOR, round(VELOCITY/2))

time.sleep(2);

print("Stopping")
TMCM_6212.stop(DEFAULT_MOTOR)

time.sleep(1);

print("Doubling moved distance")
TMCM_6212.moveBy(DEFAULT_MOTOR, TMCM_6212.getActualPosition(DEFAULT_MOTOR), round(VELOCITY/2))

while not(TMCM_6212.positionReached(DEFAULT_MOTOR)):
    pass

print("Furthest point reached")

time.sleep(1)

print("Moving back to 0")
TMCM_6212.moveTo(DEFAULT_MOTOR, 0, VELOCITY)

# Wait until position 0 is reached
while not(TMCM_6212.positionReached(DEFAULT_MOTOR)):
    pass

print("Reached Position 0")

print()

myInterface.close()
