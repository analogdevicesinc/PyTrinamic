#!/usr/bin/env python3
'''
Created on 31.01.2020

@author: JM, ED
'''

if __name__ == '__main__':
    pass

import PyTrinamic, time
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1630.TMCM_1630 import TMCM_1630

PyTrinamic.showInfo()

" please select your CAN adapter "
#myInterface = ConnectionManager("--interface pcan_tmcl").connect()
myInterface = ConnectionManager("--interface kvaser_tmcl").connect()

module = TMCM_1630(myInterface)
module.showModuleInfo()
motor = module.motor(0)

"""
    Define motor configuration for the TMCM-1630.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not work.
"""

" motor configuration "
motor.setMotorPolePairs(4)
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
motor.rotate(500)

print("Press 'input_0' to swap the direction (waiting for input_0)")
" wait for input_0 "
while (module.digitalInput(0) == 1):
     print("actual position: " + str(motor.actualPosition()))
     time.sleep(0.2)

print("\nRotate motor in counterclockwise direction...")
motor.rotate(-500)
print("Press 'input_1' to stop the motor (waiting for input_1)")

" wait for input_1 "
while (module.digitalInput(1) == 1):
#     print("actual position: " + str(module.actualPosition()))
#     time.sleep(0.2)
    pass

" stop motor"
motor.rotate(0)

myInterface.close()
print("Ready.")