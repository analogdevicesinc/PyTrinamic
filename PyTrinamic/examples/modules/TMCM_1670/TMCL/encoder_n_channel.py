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

module = TMCM_1670(myInterface, 1)
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
motor.pid.setTorquePParameter(1000)
motor.pid.setTorqueIParameter(1000)
motor.pid.setVelocityPParameter(2000)
motor.pid.setVelocityIParameter(1000)
motor.pid.setPositionPParameter(300)
motor.pid.showConfiguration()

" use out_0 output for enable input (directly shortened) "
module.setDigitalOutput(0);

" sync actual position with encoder N-Channel " 
motor.setActualPosition(0)
motor.setTargetVelocity(200)
time.sleep(0.5)
motor.spiEncoder.clearOnceOnNChannel()
time.sleep(0.5)
 
" move to zero position "
motor.moveToPosition(0)
while not motor.positionReachedFlag():
    print("target position: " + str(motor.targetPosition()) + " actual position: " + str(motor.actualPosition()))
    time.sleep(0.2)
 
" the actual position of 0 is now located at the N-Channel "
time.sleep(1.0)
print("target position: " + str(motor.targetPosition()) + " actual position: " + str(motor.actualPosition()))

myInterface.close()
print("\nReady.")
