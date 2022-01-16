#!/usr/bin/env python3
'''
Move a motor back and forth using velocity and position mode of the TMC5031

Created on 29.01.2020

@author: JM
'''

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC5031_eval import TMC5031_eval


connectionManager = ConnectionManager()

myInterface = connectionManager.connect()

PyTrinamic.showInfo()

TMC5031 = TMC5031_eval(myInterface)
TMC5031.showChipInfo()

DEFAULT_MOTOR = 0

print("Preparing parameters")
TMC5031.writeRegister(TMC5031.registers.A1[DEFAULT_MOTOR], 1000)
TMC5031.writeRegister(TMC5031.registers.V1[DEFAULT_MOTOR], 50000)
TMC5031.writeRegister(TMC5031.registers.D1[DEFAULT_MOTOR], 500)
TMC5031.writeRegister(TMC5031.registers.DMAX[DEFAULT_MOTOR], 500)
TMC5031.writeRegister(TMC5031.registers.VSTART[DEFAULT_MOTOR], 0)
TMC5031.writeRegister(TMC5031.registers.VSTOP[DEFAULT_MOTOR], 10)
TMC5031.writeRegister(TMC5031.registers.AMAX[DEFAULT_MOTOR], 1000)

print("Rotating")
TMC5031.rotate(DEFAULT_MOTOR, 10*25600)

time.sleep(5)

print("Stopping")
TMC5031.stop(DEFAULT_MOTOR)

time.sleep(1)

print("Moving back to 0")
TMC5031.moveTo(DEFAULT_MOTOR, 0, 100000)

# Wait until position 0 is reached
#while TMC5031.readRegister(TMC5031.registers.XACTUAL[DEFAULT_MOTOR]) != 0:
while TMC5031.getAxisParameter(TMC5031.APs.ActualPosition, DEFAULT_MOTOR) != 0:
    pass

print("Reached Position 0")

myInterface.close()
