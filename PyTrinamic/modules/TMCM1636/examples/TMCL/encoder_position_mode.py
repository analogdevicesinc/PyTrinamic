#!/usr/bin/env python3
'''
Created on 12.04.2021

@author: JM, ED
'''

if __name__ == '__main__':
    pass

import PyTrinamic, time
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1636.TMCM_1636 import TMCM_1636

PyTrinamic.showInfo()

" please select your CAN adapter "
#myInterface = ConnectionManager("--interface pcan_tmcl").connect()
myInterface = ConnectionManager("--interface kvaser_tmcl").connect()

module = TMCM_1636(myInterface)
module.showModuleInfo()
motor = module.motor(0)

"""
    Define motor configuration for the TMCM-1636.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not work.
"""

" motor configuration "
motor.setMotorType(motor.ENUM.MOTOR_TYPE_THREE_PHASE_BLDC)
motor.setMotorPolePairs(4)
motor.setMaxTorque(2000)
motor.showConfiguration()

" encoder configuration "
motor.openLoop.setOpenLoopTorque(1000)
motor.abnEncoder.setResolution(4096)
motor.abnEncoder.setDirection(1)
motor.abnEncoder.setInitMode(motor.ENUM.ENCODER_INIT_MODE_0)
motor.showConfiguration()

" motion settings "
motor.linearRamp.setMaxVelocity(2000)
motor.linearRamp.setAcceleration(1000)
motor.linearRamp.setRampEnabled(1)
motor.linearRamp.setTargetReachedVelocity(500)
motor.linearRamp.setTargetReachedDistance(5)
motor.setAxisParameter(motor.AP.PositionScaler, motor.abnEncoder.resolution())
motor.linearRamp.showConfiguration()

" PI configuration "
motor.pid.setTorquePIParameter(300, 500)
motor.pid.setVelocityPIParameter(300, 100)
motor.pid.setPositionPParameter(100)
motor.pid.showConfiguration()

" set commutation mode to FOC based on hall sensor signals "
motor.commutationSelection.setMode(motor.ENUM.COMM_MODE_ABN_ENCODER)
motor.commutationSelection.showConfiguration()

time.sleep(1.0)

" clear actual position "
motor.setActualPosition(0)

" set target position "
motor.moveToPosition(motor.abnEncoder.resolution() * 50)
while not motor.positionReachedFlag():
    print("target position: " + str(motor.targetPosition()) + " actual position: " + str(motor.actualPosition()))
    time.sleep(0.2)

" move back to zero position "
motor.moveToPosition(0)
while not motor.positionReachedFlag():
    print("target position: " + str(motor.targetPosition()) + " actual position: " + str(motor.actualPosition()))
    time.sleep(0.2)

myInterface.close()
print("\nReady.")
