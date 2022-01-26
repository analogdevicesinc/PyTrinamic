#!/usr/bin/env python3
'''
Created on 06.02.2020

@author: JM
'''

if __name__ == '__main__':
    pass

import time
from pytrinamic.connections.ConnectionManager import ConnectionManager
from pytrinamic.evalboards.TMC4331_eval import TMC4331_eval
from pytrinamic.evalboards.TMC2130_eval import TMC2130_eval

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()

# Create an TMC4331-Eval class which communicates over the Landungsbruecke via TMCL
TMC4331 = TMC4331_eval(myInterface)

# Create an TMC2130-Eval class which communicates over the Landungsbruecke via TMCL
TMC2130 = TMC2130_eval(myInterface)

" read ChipInfo "

TMC4331.showChipInfo()
TMC2130.showChipInfo()

" configure TMC2130 pwm for use with TMC4331 (disable singleline)"
#TMC2130.writeRegister(TMC2130.registers.DRVCTRL,   0x00)
#TMC2130.writeRegister(TMC2130.registers.CHOPCONF,  0x0C)
#TMC2130.writeRegister(TMC2130.registers.SMARTEN,   0x0D)
#TMC2130.writeRegister(TMC2130.registers.SGCSCONF,  0x0E)
#TMC2130.writeRegister(TMC2130.registers.DRVCONF,   0x0F)

DEFAULT_MOTOR = 0

#TMC4331.setAxisParameter(TMC4331.APs.MaxVelocity,     DEFAULT_MOTOR, 1000)
TMC4331.setAxisParameter(TMC4331.APs.MaxAcceleration, DEFAULT_MOTOR, 10000)

print("Rotating")
TMC4331.rotate(DEFAULT_MOTOR, 30*25600)

time.sleep(10)

print("Stopping")
TMC4331.stop(DEFAULT_MOTOR)

time.sleep(1)

print("Moving back to 0")
TMC4331.moveTo(DEFAULT_MOTOR, 0, 30*25600)
 
# Wait until position 0 is reached
while TMC4331.getAxisParameter(TMC4331.APs.ActualPosition, DEFAULT_MOTOR) != 0:
    pass

print("Reached Position 0") 

myInterface.close()