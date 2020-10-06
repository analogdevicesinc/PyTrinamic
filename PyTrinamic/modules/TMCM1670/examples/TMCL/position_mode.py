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

" motion control settings"
motor.linearRamp.setMaxVelocity(6000)
motor.linearRamp.setAcceleration(2000)
motor.linearRamp.setRampEnabled(1)
motor.linearRamp.setTargetReachedVelocity(500)
motor.linearRamp.setTargetReachedDistance(10)
motor.linearRamp.setMotorHaltedVelocity(5)
motor.linearRamp.showConfiguration()

" PI configuration "
motor.pid.setTorquePIParameter(500, 500)
motor.pid.setVelocityPIParameter(1000, 1000)
motor.pid.setPositionPParameter(300)
motor.pid.showConfiguration()

" use out_0 output for enable input (directly shortened) "
module.setDigitalOutput(0);

" clear actual position counter "
motor.setActualPosition(0)

" move to first position "
motor.moveToPosition(1000000)
while not motor.positionReachedFlag():
    print("target position: " + str(motor.targetPosition()) + " actual position: " + str(motor.actualPosition()))
    time.sleep(0.2)

time.sleep(1.0)

" move to second position "
motor.moveToPosition(2000000)
while not motor.positionReachedFlag():
    print("target position: " + str(motor.targetPosition()) + " actual position: " + str(motor.actualPosition()))
    time.sleep(0.2)
 
time.sleep(1.0)

" move back to start position " 
motor.moveToPosition(0)
while not motor.positionReachedFlag():
    print("target position: " + str(motor.targetPosition()) + " actual position: " + str(motor.actualPosition()))
    time.sleep(0.2)

myInterface.close()
print("\nReady.")
