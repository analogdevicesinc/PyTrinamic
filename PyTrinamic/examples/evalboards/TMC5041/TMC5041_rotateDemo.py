'''
Created on 29.04.2019

@author: LH
'''

import PyTrinamic
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
from PyTrinamic.evalboards.TMC5041_eval import TMC5041_eval
import time

PyTrinamic.showInfo()

myInterface = serial_tmcl_interface(PyTrinamic.firstAvailableComPort(USB=True))
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
TMC5041.rotate(DEFAULT_MOTOR, 25600)

time.sleep(5);

print("Stopping")
TMC5041.stop(DEFAULT_MOTOR)

time.sleep(1);

print("Moving back to 0")
TMC5041.moveTo(DEFAULT_MOTOR, 0, 100000)

# Wait until position 0 is reached
while TMC5041.readRegister(TMC5041.registers.XACTUAL[DEFAULT_MOTOR]) != 0:
    pass

print("Reached Position 0")

myInterface.close()