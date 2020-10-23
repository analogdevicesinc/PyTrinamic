#!/usr/bin/env python3
'''
Created on 07.11.2019

@author: JM
'''

if __name__ == '__main__':
    pass

import time
from PyTrinamic.connections.ConnectionManagerPC import ConnectionManagerPC
from PyTrinamic.evalboards.TMC4361_eval import TMC4361_eval
from PyTrinamic.evalboards.TMC2660_eval import TMC2660_eval

myInterface = ConnectionManagerPC(interfaces=["usb_tmcl"]).connect()[0]

# Create an TMC4361-Eval class which communicates over the Landungsbruecke via TMCL
TMC4361 = TMC4361_eval(myInterface)

# Create an TMC2660-Eval class which communicates over the Landungsbruecke via TMCL
TMC2660 = TMC2660_eval(myInterface)

" read ChipInfo "

TMC4361.showChipInfo()
TMC2660.showChipInfo()

" configure TMC2660 pwm for use with TMC4361 (disable singleline)"
#TMC2660.writeRegister(TMC2660.registers.DRVCTRL,   0x00)
#TMC2660.writeRegister(TMC2660.registers.CHOPCONF,  0x0C)
#TMC2660.writeRegister(TMC2660.registers.SMARTEN,   0x0D)
#TMC2660.writeRegister(TMC2660.registers.SGCSCONF,  0x0E)
#TMC2660.writeRegister(TMC2660.registers.DRVCONF,   0x0F)

DEFAULT_MOTOR = 0

#TMC4361.setAxisParameter(TMC4361.APs.MaxVelocity,     DEFAULT_MOTOR, 1000)
TMC4361.setAxisParameter(TMC4361.APs.MaxAcceleration, DEFAULT_MOTOR, 10000)

print("Rotating")
TMC4361.rotate(DEFAULT_MOTOR, 30*25600)

time.sleep(10);

print("Stopping")
TMC4361.stop(DEFAULT_MOTOR)

time.sleep(1);

print("Moving back to 0")
TMC4361.moveTo(DEFAULT_MOTOR, 0, 30*25600)

# Wait until position 0 is reached
while TMC4361.getAxisParameter(TMC4361.APs.ActualPosition, DEFAULT_MOTOR) != 0:
    pass

print("Reached Position 0")

myInterface.close()
