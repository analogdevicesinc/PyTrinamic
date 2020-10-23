#!/usr/bin/env python3
'''
Move a motor back and forth using velocity and position mode of the TMC5160

Created on 24.10.2019

@author: JM
'''

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManagerPC import ConnectionManagerPC
from PyTrinamic.evalboards.TMC5160_eval import TMC5160_eval

myInterface = ConnectionManagerPC(interfaces=["usb_tmcl"]).connect()[0]

PyTrinamic.showInfo()

TMC5160 = TMC5160_eval(myInterface)
TMC5160.showChipInfo()

DEFAULT_MOTOR = 0

print("Preparing parameters")
TMC5160.writeRegister(TMC5160.registers.A1, 1000)
TMC5160.writeRegister(TMC5160.registers.V1, 50000)
TMC5160.writeRegister(TMC5160.registers.D1, 500)
TMC5160.writeRegister(TMC5160.registers.DMAX, 500)
TMC5160.writeRegister(TMC5160.registers.VSTART, 0)
TMC5160.writeRegister(TMC5160.registers.VSTOP, 10)
TMC5160.writeRegister(TMC5160.registers.AMAX, 1000)

print("Rotating")
TMC5160.rotate(DEFAULT_MOTOR, 7*25600)

time.sleep(5);

print("Stopping")
TMC5160.stop(DEFAULT_MOTOR)

time.sleep(1);

print("Moving back to 0")
TMC5160.moveTo(DEFAULT_MOTOR, 0, 100000)

# Wait until position 0 is reached
#while TMC5160.readRegister(TMC5160.registers.XACTUAL[DEFAULT_MOTOR]) != 0:
while TMC5160.getAxisParameter(TMC5160.APs.ActualPosition, DEFAULT_MOTOR) != 0:
    pass

print("Reached Position 0")

myInterface.close()
