#!/usr/bin/env python3
'''
Move a motor back and forth using velocity and position mode of the TMC5041

Created on 18.10.2019

@author: JM
'''

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC5041_eval import TMC5041_eval


connectionManager = ConnectionManager()

myInterface = connectionManager.connect()

PyTrinamic.showInfo()

TMC5041 = TMC5041_eval(myInterface)

DEFAULT_MOTOR = 0

print("Preparing parameters")
TMC5041.writeRegister(TMC5041.registers.A1[DEFAULT_MOTOR], 1000)
TMC5041.writeRegister(TMC5041.registers.V1[DEFAULT_MOTOR], 50000)
TMC5041.writeRegister(TMC5041.registers.D1[DEFAULT_MOTOR], 500)
TMC5041.writeRegister(TMC5041.registers.DMAX[DEFAULT_MOTOR], 500)
TMC5041.writeRegister(TMC5041.registers.VSTART[DEFAULT_MOTOR], 0)
TMC5041.writeRegister(TMC5041.registers.VSTOP[DEFAULT_MOTOR], 10)
TMC5041.writeRegister(TMC5041.registers.AMAX[DEFAULT_MOTOR], 1000)

print("Rotating")
TMC5041.rotate(DEFAULT_MOTOR, 10*25600)

time.sleep(5);

print("Stopping")
TMC5041.stop(DEFAULT_MOTOR)

time.sleep(1);

print("Moving back to 0")
TMC5041.moveTo(DEFAULT_MOTOR, 0, 100000)

# Wait until position 0 is reached
#while TMC5041.readRegister(TMC5041.registers.XACTUAL[DEFAULT_MOTOR]) != 0:
while TMC5041.getAxisParameter(TMC5041.APs.ActualPosition, DEFAULT_MOTOR) != 0:
    pass

print("Reached Position 0")

myInterface.close()
