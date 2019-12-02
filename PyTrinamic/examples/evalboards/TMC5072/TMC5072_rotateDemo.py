#!/usr/bin/env python3
'''
Move a motor back and forth using velocity and position mode of the TMC5072

Created on 20.09.2019

@author: JM
'''

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC5072_eval import TMC5072_eval


connectionManager = ConnectionManager()

myInterface = connectionManager.connect()

PyTrinamic.showInfo()

TMC5072 = TMC5072_eval(myInterface)
TMC5072.showChipInfo()

DEFAULT_MOTOR = 0

print("Preparing parameters")
TMC5072.writeRegister(TMC5072.registers.A1[DEFAULT_MOTOR], 1000)
TMC5072.writeRegister(TMC5072.registers.V1[DEFAULT_MOTOR], 50000)
TMC5072.writeRegister(TMC5072.registers.D1[DEFAULT_MOTOR], 500)
TMC5072.writeRegister(TMC5072.registers.DMAX[DEFAULT_MOTOR], 500)
TMC5072.writeRegister(TMC5072.registers.VSTART[DEFAULT_MOTOR], 0)
TMC5072.writeRegister(TMC5072.registers.VSTOP[DEFAULT_MOTOR], 10)
TMC5072.writeRegister(TMC5072.registers.AMAX[DEFAULT_MOTOR], 1000)

print("Rotating")
TMC5072.rotate(DEFAULT_MOTOR, 10*25600)

time.sleep(5);

print("Stopping")
TMC5072.stop(DEFAULT_MOTOR)

time.sleep(1);

print("Moving back to 0")
TMC5072.moveTo(DEFAULT_MOTOR, 0, 100000)

# Wait until position 0 is reached
#while TMC5072.readRegister(TMC5072.registers.XACTUAL[DEFAULT_MOTOR]) != 0:
while TMC5072.getAxisParameter(TMC5072.APs.ActualPosition, DEFAULT_MOTOR) != 0:
    pass

print("Reached Position 0")

myInterface.close()
