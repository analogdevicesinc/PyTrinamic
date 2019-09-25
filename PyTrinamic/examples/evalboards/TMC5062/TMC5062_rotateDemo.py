#!/usr/bin/env python3
'''
Move a motor back and forth using velocity and position mode of the TMC5062

Created on 24.09.2019

@author: JM
'''

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC5062_eval import TMC5062_eval

connectionManager = ConnectionManager()

myInterface = connectionManager.connect()

PyTrinamic.showInfo()

TMC5062 = TMC5062_eval(myInterface)

DEFAULT_MOTOR = 0

print("Preparing parameters")
TMC5062.writeRegister(TMC5062.registers.A1[DEFAULT_MOTOR], 1000)
TMC5062.writeRegister(TMC5062.registers.V1[DEFAULT_MOTOR], 50000)
TMC5062.writeRegister(TMC5062.registers.D1[DEFAULT_MOTOR], 500)
TMC5062.writeRegister(TMC5062.registers.DMAX[DEFAULT_MOTOR], 500)
TMC5062.writeRegister(TMC5062.registers.VSTART[DEFAULT_MOTOR], 0)
TMC5062.writeRegister(TMC5062.registers.VSTOP[DEFAULT_MOTOR], 10)
TMC5062.writeRegister(TMC5062.registers.AMAX[DEFAULT_MOTOR], 1000)

print("Rotating")
TMC5062.rotate(DEFAULT_MOTOR, 5*25600)

time.sleep(5);

print("Stopping")
TMC5062.stop(DEFAULT_MOTOR)

time.sleep(1);

print("Moving back to 0")
TMC5062.moveTo(DEFAULT_MOTOR, 0, 100000)

# Wait until position 0 is reached
while TMC5062.readRegister(TMC5062.registers.XACTUAL[DEFAULT_MOTOR]) != 0:
    pass

print("Reached Position 0")

myInterface.close()
