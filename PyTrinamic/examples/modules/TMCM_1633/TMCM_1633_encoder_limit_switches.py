#!/usr/bin/env python3
'''
Created on 25.06.2019

@author: ED
'''

if __name__ == '__main__':
    pass

import time
import PyTrinamic
from PyTrinamic.connections.pcan_tmcl_interface import pcan_tmcl_interface
from PyTrinamic.modules.TMCM_1633 import TMCM_1633

PyTrinamic.showInfo()
PyTrinamic.showAvailableComPorts(CAN=True)

# for peak can connection
myInterface = pcan_tmcl_interface('PCAN_USBBUS1', 1000000)

module = TMCM_1633(myInterface)

# motor configuration
module.setMotorPoles(8)
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
module.setCommutationMode(module.COMM_MODE_FOC_ENCODER)

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