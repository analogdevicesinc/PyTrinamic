#!/usr/bin/env python3
'''
Move a motor back and forth using velocity and position mode of the TMC5161

Created on 30.01.2020

@author: JM
'''

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManagerPC import ConnectionManagerPC
from PyTrinamic.evalboards.TMC5161_eval import TMC5161_eval

myInterface = ConnectionManagerPC(interfaces=["usb_tmcl"]).connect()[0]

PyTrinamic.showInfo()

TMC5161 = TMC5161_eval(myInterface)
TMC5161.showChipInfo()

DEFAULT_MOTOR = 0

print("Preparing parameters")
TMC5161.writeRegister(TMC5161.registers.A1, 1000)
TMC5161.writeRegister(TMC5161.registers.V1, 50000)
TMC5161.writeRegister(TMC5161.registers.D1, 500)
TMC5161.writeRegister(TMC5161.registers.DMAX, 500)
TMC5161.writeRegister(TMC5161.registers.VSTART, 0)
TMC5161.writeRegister(TMC5161.registers.VSTOP, 10)
TMC5161.writeRegister(TMC5161.registers.AMAX, 1000)

print("Rotating")
TMC5161.rotate(DEFAULT_MOTOR, 7*25600)

time.sleep(5);

print("Stopping")
TMC5161.stop(DEFAULT_MOTOR)

time.sleep(1);

print("Moving back to 0")
TMC5161.moveTo(DEFAULT_MOTOR, 0, 100000)

# Wait until position 0 is reached
#while TMC5161.readRegister(TMC5161.registers.XACTUAL[DEFAULT_MOTOR]) != 0:
while TMC5161.getAxisParameter(TMC5161.APs.ActualPosition, DEFAULT_MOTOR) != 0:
    pass

print("Reached Position 0")

myInterface.close()
