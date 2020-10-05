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
motor.linearRamp.setMaxVelocity(1000)
motor.linearRamp.setAcceleration(2000)
motor.linearRamp.setRampEnabled(1)
motor.linearRamp.setTargetReachedDistance(5)
motor.linearRamp.setTargetReachedVelocity(500)
motor.linearRamp.setTargetReachedDistance(5)
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

print("move to first position")
motor.moveToPosition(motor.motorPoles() * 3 * 50)

" wait for position reached "
while not motor.positionReachedFlag():
    print("target position: " + str(motor.targetPosition()) + " actual position: " + str(motor.actualPosition()))
    time.sleep(0.2)
 
print("move back to zero")
motor.moveToPosition(0)

" wait for position reached "
while not motor.positionReachedFlag():
    print("target position: " + str(motor.targetPosition()) + " actual position: " + str(motor.actualPosition()))
    time.sleep(0.2)

myInterface.close()
print("\nReady.")
