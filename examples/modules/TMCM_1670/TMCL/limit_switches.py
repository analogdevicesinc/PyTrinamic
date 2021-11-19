#!/usr/bin/env python3
'''
Created on 24.06.2019

@author: ED
'''

if __name__ == '__main__':
    pass

import PyTrinamic, time
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1670.TMCM_1670 import TMCM_1670

PyTrinamic.showInfo()

" please select your CAN adapter "
#myInterface = ConnectionManager("--interface pcan_tmcl").connect()
myInterface = ConnectionManager("--interface kvaser_tmcl").connect()

module = TMCM_1670(myInterface)
module.showModuleInfo()
motor = module.motor(0)

" motor configuration "
motor.setMaxTorque(2000)
motor.showConfiguration()

" encoder configuration "
motor.spiEncoder.showConfiguration()

" motion control settings "
motor.linearRamp.setMaxVelocity(4000)
motor.linearRamp.setAcceleration(4000)
motor.linearRamp.setRampEnabled(1)
motor.linearRamp.setTargetReachedVelocity(500)
motor.linearRamp.setTargetReachedDistance(10)
motor.linearRamp.setMotorHaltedVelocity(5)
motor.linearRamp.showConfiguration()

" PI configuration "
motor.pid.setTorquePIParameter(1000, 1000)
motor.pid.setVelocityPIParameter(2000, 1000)
motor.pid.setPositionPParameter(300)
motor.pid.showConfiguration()

" use out_0 output for enable input (directly shortened) "
module.setDigitalOutput(0);

" rotate motor in right direction " 
motor.setTargetVelocity(1000)
while module.digitalInput(0):
    print("waiting for right switch...")
    time.sleep(0.2)

" rotate motor in left direction "
motor.setTargetVelocity(-1000)
while module.digitalInput(1):
    print("waiting for left switch...")
    time.sleep(0.2)

" stop motor "
motor.setTargetVelocity(0)

myInterface.close()
print("\nReady.")