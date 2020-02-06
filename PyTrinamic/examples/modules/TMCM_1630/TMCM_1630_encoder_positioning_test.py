#!/usr/bin/env python3
'''
Created on 31.01.2020

@author: JM
'''

if __name__ == '__main__':
    pass

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM_1630 import TMCM_1630

PyTrinamic.showInfo()
connectionManager = ConnectionManager("--interface pcan_tmcl".split()) #This setting is configurated for PCAN , if you want to use another Connection please change this line
myInterface = connectionManager.connect()

module = TMCM_1630(myInterface)

"""
    Define all motor configurations for the the TMCM-1630.

    The configuration is based on our standard BLDC motor(TMCS-28-5-1024-AT.01).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not working.
"""

" motor configuration "
module.setMotorPoles(4)
module.setMaxTorque(2000)
module.showMotorConfiguration()

" encoder configuration "
module.setOpenLoopTorque(1000)
module.setEncoderResolution(4096)
module.setEncoderDirection(0)
module.setEncoderInitMode(module.ENUMs.ENCODER_INIT_MODE_0)
module.showEncoderConfiguration()

" motion settings "
module.setMaxVelocity(1000)
module.setAcceleration(2000)
module.setRampEnabled(1)
module.setTargetReachedVelocity(500)
module.setTargetReachedDistance(5)
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

" set position counter to zero"
module.setActualPosition(0)

" move to zero position"
module.moveToPosition(0)

print("starting positioning")

module.moveToPosition(300000)
while not module.positionReached():
    print("target position: " + str(module.targetPosition()) + " actual position: " + str(module.actualPosition()))
    time.sleep(0.2)

module.moveToPosition(0)
while not module.positionReached():
    print("target position: " + str(module.targetPosition()) + " actual position: " + str(module.actualPosition()))
    time.sleep(0.2)

print("Ready.")
myInterface.close()