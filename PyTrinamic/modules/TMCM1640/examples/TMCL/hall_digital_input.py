#!/usr/bin/env python3
'''
Created on 30.12.2018

@author: ED
'''

if __name__ == '__main__':
    pass

import PyTrinamic, time
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1640.TMCM_1640 import TMCM_1640

PyTrinamic.showInfo()

myInterface = ConnectionManager().connect()
module = TMCM_1640(myInterface)
module.showModuleInfo()
motor = module.motor(0)
    
"""
    Define motor configuration for the TMCM-1640.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not work.
"""

" motor configuration "
motor.setMotorPoles(8)
motor.setMaxTorque(2000)
motor.showConfiguration()

" hall configuration "
motor.digitalHall.setHallInvert(0)
motor.digitalHall.showConfiguration()

" motion settings "
motor.linearRamp.setMaxVelocity(1500)
motor.linearRamp.setAcceleration(2000)
motor.linearRamp.setRampEnabled(1)
motor.linearRamp.setTargetReachedVelocity(500)
motor.linearRamp.setTargetReachedDistance(5)
motor.linearRamp.setMotorHaltedVelocity(50)
motor.linearRamp.showConfiguration()

" PI configuration "
motor.pid.setTorquePIParameter(600, 600)
motor.pid.setVelocityPIParameter(800, 500)
motor.pid.setPositionPParameter(300)
motor.pid.showConfiguration()

" set commutation mode to FOC based on hall sensor signals "
motor.commutationSelection.setMode(motor.ENUM.COMM_MODE_FOC_HALL)
motor.commutationSelection.showConfiguration()

" clear actual position "
motor.setActualPosition(0)

print("\nRotate motor in clockwise direction...")
motor.setTargetVelocity(500)

print("Press 'input_0' to swap the direction (waiting for input_0)")

" wait for input_0 "
while (module.digitalInput(0) == 0):
    print("actual position: %d   actual velocity: %d   actual torque: %d" % (motor.actualPosition(), motor.actualVelocity(), motor.actualTorque()))
    time.sleep(0.2)

print("\nRotate motor in counterclockwise direction...")
motor.setTargetVelocity(-500)

print("Press 'input_1' to stop the motor (waiting for input_1)")
 
" wait for input_1 "
while (module.digitalInput(1) == 0):
    print("actual position: %d   actual velocity: %d   actual torque: %d" % (motor.actualPosition(), motor.actualVelocity(), motor.actualTorque()))
    time.sleep(0.2)
 
" stop motor"
motor.setTargetVelocity(0)

myInterface.close()
print("\nReady.")