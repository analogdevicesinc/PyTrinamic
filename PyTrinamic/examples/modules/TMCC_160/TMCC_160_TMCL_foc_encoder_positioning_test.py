#!/usr/bin/env python3
'''
Created on 04.02.2020

@author: JM
'''

if __name__ == '__main__':
    pass

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCC160.TMCC_160 import TMCC_160

PyTrinamic.showInfo()
#connectionManager = ConnectionManager("--interface pcan_tmcl")
connectionManager = ConnectionManager("--interface kvaser_tmcl")
myInterface = connectionManager.connect()

module = TMCC_160(myInterface)

"""
    Define all motor configurations for the TMCC160.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not work.
"""

" motor/module settings "
module.setMotorPoles(8)
module.setMaxTorque(2000)
module.showMotorConfiguration()

" hall configuration "
module.setHallInvert(0)
module.showHallConfiguration()

" encoder settings "
module.setOpenLoopTorque(1000)
module.setEncoderResolution(4096)
module.setEncoderDirection(1)
module.setEncoderInitMode(module.ENUMs.ENCODER_INIT_MODE_1)
module.showEncoderConfiguration()

" motion settings "
module.setMaxVelocity(4000)
module.setAcceleration(2000)
module.setRampEnabled(1)
module.setTargetReachedVelocity(500)
module.setTargetReachedDistance(5)
module.showMotionConfiguration()

" current PID values "
module.setTorquePParameter(500)
module.setTorqueIParameter(500)

" velocity PID values "
module.setVelocityPParameter(1000)
module.setVelocityIParameter(1000)

" position PID values "
module.setPositionPParameter(300)
module.showPIConfiguration()

" set commutation mode to FOC based on hall sensor signals "
module.setCommutationMode(module.ENUMs.COMM_MODE_FOC_ENCODER)

" set position counter to zero"
module.setActualPosition(0)

print("\nMotor move to first target position")
module.moveToPosition(40960)
while not module.positionReached():
    print("target position: " + str(module.targetPosition()) + " actual position: " + str(module.actualPosition()))
    time.sleep(0.1)

print("Motor reached first target position")
time.sleep(3)

print("\nMotor move to second target position")
module.moveToPosition(81920)
while not module.positionReached():
    print("target position: " + str(module.targetPosition()) + " actual position: " + str(module.actualPosition()))
    time.sleep(0.1)

print("Motor reached second target position")
time.sleep(3)

print("\nReturn to zero position")
module.moveToPosition(0)
while not module.positionReached():
    print("target position: " + str(module.targetPosition()) + " actual position: " + str(module.actualPosition()))
    time.sleep(0.1)

print("Motor reached zero position")
print("\nReady.")
myInterface.close()
