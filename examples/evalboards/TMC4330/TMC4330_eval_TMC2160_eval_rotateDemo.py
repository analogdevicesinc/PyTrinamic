#!/usr/bin/env python3
'''
Created on 06.02.2020

@author: JM
'''

if __name__ == '__main__':
    pass

import time
from pytrinamic.connections.ConnectionManager import ConnectionManager
from pytrinamic.evalboards.TMC4330_eval import TMC4330_eval
from pytrinamic.evalboards.TMC2160_eval import TMC2160_eval

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()

# Create an TMC4330-Eval class which communicates over the Landungsbruecke via TMCL
TMC4330 = TMC4330_eval(myInterface)

# Create an TMC2160-Eval class which communicates over the Landungsbruecke via TMCL
TMC2160 = TMC2160_eval(myInterface)

" read ChipInfo "

TMC4330.showChipInfo()
TMC2160.showChipInfo()

" configure TMC2160 pwm for use with TMC4330 (disable singleline)"
#TMC2160.writeRegister(TMC2160.registers.DRVCTRL,   0x00)
#TMC2160.writeRegister(TMC2160.registers.CHOPCONF,  0x0C)
#TMC2160.writeRegister(TMC2160.registers.SMARTEN,   0x0D)
#TMC2160.writeRegister(TMC2160.registers.SGCSCONF,  0x0E)
#TMC2160.writeRegister(TMC2160.registers.DRVCONF,   0x0F)

DEFAULT_MOTOR = 0

#TMC4330.setAxisParameter(TMC4330.APs.MaxVelocity,     DEFAULT_MOTOR, 1000)
TMC4330.setAxisParameter(TMC4330.APs.MaxAcceleration, DEFAULT_MOTOR, 10000)

print("Rotating")
TMC4330.rotate(DEFAULT_MOTOR, 30*25600)

time.sleep(12)

print("Stopping")
TMC4330.stop(DEFAULT_MOTOR)

time.sleep(3)

print("Moving back to 0")
TMC4330.moveTo(DEFAULT_MOTOR, 0, 30*25600)
 
# Wait until position 0 is reached
while TMC4330.getAxisParameter(TMC4330.APs.ActualPosition, DEFAULT_MOTOR) != 0:
    pass

print("Reached Position 0") 

myInterface.close()