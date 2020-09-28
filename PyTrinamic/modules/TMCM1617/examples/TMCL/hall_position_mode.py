#!/usr/bin/env python3
'''
Created on 04.02.2020

@author: JM, ED
'''

if __name__ == '__main__':
    pass

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1617.TMCM_1617 import TMCM_1617
import time

PyTrinamic.showInfo()

" please select your CAN adapter "
#connectionManager = ConnectionManager("--interface pcan_tmcl")
connectionManager = ConnectionManager("--interface kvaser_tmcl")
myInterface = connectionManager.connect()

module = TMCM_1617(myInterface)

"""
    Define motor configuration for the TMCM-1617.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not work.
"""

" motor configuration "
module.setMotorPolePairs(4)
module.setMaxTorque(2000)
module.setMotorType(module.ENUMs.MOTOR_TYPE_THREE_PHASE_BLDC)
module.showMotorConfiguration()

" hall configuration "
module.setAxisParameter(module.APs.HallSensorDirection, 0)
module.setAxisParameter(module.APs.HallSensorInvert, 1)
module.setAxisParameter(module.APs.HallSensorOffset, 0)
module.setAxisParameter(module.APs.HallInterpolation, 1)
module.showHallConfiguration()

" motion settings "
module.setMaxVelocity(2000)
module.setAcceleration(1000)
module.setRampEnabled(1)
module.setTargetReachedVelocity(500)
module.setTargetReachedDistance(5)
module.setPositionScaler(6*module.motorPolePairs())
module.showMotionConfiguration()

" PI configuration "
module.setTorquePParameter(300)
module.setTorqueIParameter(600)
module.setVelocityPParameter(600)
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
module.moveToPosition(4000)

" wait for position reached "
while not module.positionReached():
    print("target position: " + str(module.targetPosition()) + " actual position: " + str(module.actualPosition()))
    time.sleep(0.2)

" move back to zero"
module.moveToPosition(0)

" wait for position reached "
while not module.positionReached():
    print("target position: " + str(module.targetPosition()) + " actual position: " + str(module.actualPosition()))
    time.sleep(0.2)

myInterface.close()
print("Ready.")
