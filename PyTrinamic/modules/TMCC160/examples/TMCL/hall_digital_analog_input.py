#!/usr/bin/env python3
'''
Created on 04.02.2020

@author: JM, ED
'''

if __name__ == '__main__':
    pass

import PyTrinamic, time
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCC160.TMCC_160 import TMCC_160

PyTrinamic.showInfo()

" please select your CAN adapter "
#myInterface = ConnectionManager("--interface pcan_tmcl").connect()
myInterface = ConnectionManager("--interface kvaser_tmcl").connect()

module = TMCC_160(myInterface)
module.showModuleInfo()
motor = module.motor(0)

"""
    Define motor configurations for the TMCC160-EVAL.

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
motor.linearRamp.setMaxVelocity(4000)
motor.linearRamp.setAcceleration(2000)
motor.linearRamp.setRampEnabled(1)
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

motor.rotate(500)
print("\nCurrent direction: rotate forward")
print("Press 'input_0' to swap the direction (waiting for input_0)")

" wait for input_0 "
while (module.digitalInput(0) == 1):
    pass

" rotate motor in other direction"
motor.rotate(-500)
print("\nCurrent direction: rotate backwards")
print("Press 'input_1' to stop the motor (waiting for input_1)")

" wait for input_1 "
while (module.digitalInput(1) == 1):
    pass

" stop motor "
motor.rotate(0)

myInterface.close()
print("\nReady.")