#!/usr/bin/env python3
'''
Created on 04.02.2020

@author: JM, ED
'''

if __name__ == '__main__':
    pass

import PyTrinamic, time
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1617.TMCM_1617 import TMCM_1617

PyTrinamic.showInfo()

" please select your CAN adapter "
#myInterface = ConnectionManager("--interface pcan_tmcl").connect()
myInterface = ConnectionManager("--interface kvaser_tmcl").connect()

module = TMCM_1617(myInterface)
module.showModuleInfo()
motor = module.motor(0)

"""
    Define motor configuration for the TMCM-1617.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not work.
"""

" motor configuration "
motor.setMotorType(motor.ENUM.MOTOR_TYPE_THREE_PHASE_BLDC)
motor.setMotorPolePairs(4)
motor.setMaxTorque(2000)
motor.showConfiguration()

" hall configuration "
motor.digitalHall.setDirection(0)
motor.digitalHall.setPolarity(1)
motor.digitalHall.setOffset(0)
motor.digitalHall.setInterpolation(1)
motor.digitalHall.showConfiguration()

" motion settings "
motor.linearRamp.setMaxVelocity(2000)
motor.linearRamp.setAcceleration(1000)
motor.linearRamp.setRampEnabled(1)
motor.linearRamp.setTargetReachedDistance(5)
motor.linearRamp.setTargetReachedVelocity(500)
motor.setAxisParameter(motor.AP.PositionScaler, 6*motor.motorPolePairs())
motor.linearRamp.showConfiguration()

" PI configuration "
motor.pid.setTorquePIParameter(300, 600)
motor.pid.setVelocityPIParameter(600, 500)
motor.pid.setPositionPParameter(300)
motor.pid.showConfiguration()

" set commutation mode to FOC based on hall sensor signals "
motor.commutationSelection.setMode(motor.ENUM.COMM_MODE_DIGITAL_HALL)
motor.commutationSelection.showConfiguration()

" set position counter to zero"
motor.setActualPosition(0)

" move to zero position"
motor.moveToPosition(0)

print("starting positioning")
motor.moveToPosition(4000)

" wait for position reached "
while not motor.positionReachedFlag():
    print("target position: " + str(motor.targetPosition()) + " actual position: " + str(motor.actualPosition()))
    time.sleep(0.2)

" move back to zero"
motor.moveToPosition(0)

" wait for position reached "
while not motor.positionReachedFlag():
    print("target position: " + str(motor.targetPosition()) + " actual position: " + str(motor.actualPosition()))
    time.sleep(0.2)

myInterface.close()
print("\nReady.")
