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
from PyTrinamic.modules.TMCM_1617 import TMCM_1617

PyTrinamic.showInfo()
connectionManager = ConnectionManager("--interface pcan_tmcl".split()) #This setting is configurated for PCAN , if you want to use another Connection please change this line
myInterface = connectionManager.connect()

module = TMCM_1617(myInterface)

" motor configuration "
module.setMotorPoles(4)
module.setMaxTorque(2000)
module.setMotorType(3)
module.showMotorConfiguration()

" encoder configuration "
module.setOpenLoopTorque(1000)
module.setEncoderResolution(4096)
module.setEncoderDirection(1)
module.setEncoderInitMode(module.ENUMs.ENCODER_INIT_MODE_0)
module.showEncoderConfiguration()

" motion settings "
module.setMaxVelocity(400)
module.setAcceleration(200)
module.setRampEnabled(1)
module.setTargetReachedVelocity(500)
module.setTargetReachedDistance(5)
module.setPositionScalerM(2048)
module.showMotionConfiguration()

" PI configuration "
module.setTorquePParameter(500)
module.setTorqueIParameter(500)
module.setVelocityPParameter(1000)
module.setVelocityIParameter(1000)
module.setPositionPParameter(300)
module.showPIConfiguration()

" set commutation mode to FOC based on hall sensor signals "
module.setCommutationMode(module.ENUMs.COMM_MODE_FOC_ENCODER)

" Commutation Mode "
module.showCommutationMode()

" set position counter to zero "
module.setActualPosition(0)

" move to zero position "
module.moveToPosition(0)

module.moveToPosition(300000)

print("Motor move to new target position")
while not module.positionReached():
    print("target position: " + str(module.targetPosition()) + " actual position: " + str(module.actualPosition()))
    time.sleep(0.6)

print()
print("Motor reached new target position")
time.sleep(5)

module.moveToPosition(0)

print()
print("Motor return to old target position")
while not module.positionReached():
    print("target position: " + str(module.targetPosition()) + " actual position: " + str(module.actualPosition()))
    time.sleep(0.6)

print()
print("Motor reached old target position")
time.sleep(1)

print()
print("Ready.")
myInterface.close()
