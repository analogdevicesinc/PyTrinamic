#!/usr/bin/env python3
'''
Created on 25.06.2019

@author: ED
'''

if __name__ == '__main__':
    pass

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM_1633 import TMCM_1633

PyTrinamic.showInfo()
connectionManager = ConnectionManager("--interface pcan_tmcl".split()) #This setting is configurated for PCAN , if you want to use another Connection please change this line
myInterface = connectionManager.connect()

module = TMCM_1633(myInterface)

"""
    Define all motor configurations for the the TMCM-1633.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not working.
"""

# motor configuration
module.setMotorPoles(4)
module.setMaxTorque(4000)
module.showMotorConfiguration()

# hall configuration
module.setHallInvert(0)
module.showHallConfiguration()

# encoder configuration
module.setEncoderResolution(4096)
module.setEncoderDirection(0)
module.setEncoderInitMode(1)
module.showEncoderConfiguration()

# motion settings
module.setMaxVelocity(2000)
module.setAcceleration(2000)
module.setRampEnabled(1)
module.setTargetReachedVelocity(500)
module.setTargetReachedDistance(5)
module.showMotionConfiguration()

# PI configuration
module.setTorquePParameter(600)
module.setTorqueIParameter(600)
module.setVelocityPParameter(800)
module.setVelocityIParameter(800)
module.setPositionPParameter(1000)
module.showPIConfiguration()

# set commutation mode to FOC based on encoder
module.setCommutationMode(module.ENUMs.COMM_MODE_FOC_ENCODER)

targetVelocity = 1000

# velocity control
while module.digitalInput(0):
    print("target velocity: " +str(targetVelocity))
    module.rotate(targetVelocity)
    time.sleep(0.2)

# velocity control
while module.digitalInput(1):
    print("target velocity: " +str(-targetVelocity))
    module.rotate(-targetVelocity)
    time.sleep(0.2)

# stop motor
module.rotate(0)

print("Ready.")
myInterface.close()