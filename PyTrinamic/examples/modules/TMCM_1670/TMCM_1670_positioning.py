#!/usr/bin/env python3
'''
Created on 24.06.2019

@author: ED
'''

if __name__ == '__main__':
    pass

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM_1670 import TMCM_1670

PyTrinamic.showInfo()
connectionManager = ConnectionManager()
myInterface = connectionManager.connect()

module = TMCM_1670(myInterface)
 
# motor configuration
module.setMaxTorque(2000)
module.showMotorConfiguration()
 
# encoder configuration
module.showEncoderConfiguration()
 
# motion settings
module.setMaxVelocity(4000)
module.setAcceleration(2000)
module.setRampEnabled(1)
module.setTargetReachedVelocity(500)
module.setTargetReachedDistance(10)
module.setMotorHaltedVelocity(5)
module.showMotionConfiguration()
 
# PI configuration
module.setTorquePParameter(500)
module.setTorqueIParameter(500)
module.setVelocityPParameter(1000)
module.setVelocityIParameter(1000)
module.setPositionPParameter(300)
module.showPIConfiguration()

# use out_0 output for enable input (directly shortened)
module.setDigitalOutput(0);
 
# clear actual position counter
module.setActualPosition(0)

# move to first position
module.moveToPosition(300000)
while not module.positionReached():
    print("target position: " + str(module.targetPosition()) + " actual position: " + str(module.actualPosition()))
    time.sleep(0.2)
 
time.sleep(1.0)

# move to second position
module.moveToPosition(600000)
while not module.positionReached():
    print("target position: " + str(module.targetPosition()) + " actual position: " + str(module.actualPosition()))
    time.sleep(0.2)
 
time.sleep(1.0)

# move back to start position 
module.moveToPosition(0)
while not module.positionReached():
    print("target position: " + str(module.targetPosition()) + " actual position: " + str(module.actualPosition()))
    time.sleep(0.2)

print("Ready.")
myInterface.close()