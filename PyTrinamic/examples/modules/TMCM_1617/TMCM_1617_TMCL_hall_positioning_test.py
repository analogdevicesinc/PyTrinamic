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
from PyTrinamic.modules.TMCM1617.TMCM_1617 import TMCM_1617

PyTrinamic.showInfo()
connectionManager = ConnectionManager("--interface pcan_tmcl".split()) #This setting is configurated for PCAN , if you want to use another Connection please change this line
myInterface = connectionManager.connect()

module = TMCM_1617(myInterface)

"""
    Define all motor configurations for the the TMCM-1617.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not working.
"""

" motor configuration "
module.setMotorPoles(4)
module.setMaxTorque(2000)
module.setMotorType(3)
module.showMotorConfiguration()

" hall configuration "
#module.setHallInvert(0)
module.showHallConfiguration()

" motion settings "
module.setMaxVelocity(400)
module.setAcceleration(200)
module.setRampEnabled(1)
module.setTargetReachedVelocity(500)
module.setTargetReachedDistance(5)
module.setPositionScalerM(2048)
module.showMotionConfiguration()

" PI configuration "
module.setTorquePParameter(600)
module.setTorqueIParameter(600)
module.setVelocityPParameter(800)
module.setVelocityIParameter(500)
module.setPositionPParameter(300)
module.showPIConfiguration()

" set commutation mode to FOC based on hall sensor signals "
module.setCommutationMode(module.ENUMs.COMM_MODE_FOC_HALL)

" set position counter to zero"
module.setActualPosition(0)

" move to zero position"
module.moveToPosition(0)

print("starting positioning")

module.moveToPosition(300000)

print("Motor move to new target position")
while not module.positionReached():
    print("target position: " + str(module.targetPosition()) + " actual position: " + str(module.actualPosition()))
    time.sleep(0.6)

    if(module.actualPosition() > 299800): # <------ Hall cant reach the exactly targetPosition
        break

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
