#!/usr/bin/env python3
'''
Created on 24.06.2019

@author: ED
'''

if __name__ == '__main__':
    pass

import time
import PyTrinamic
from PyTrinamic.connections.pcan_tmcl_interface import pcan_tmcl_interface
from PyTrinamic.modules.TMCM_1670 import TMCM_1670

PyTrinamic.showInfo()
PyTrinamic.showAvailableComPorts(CAN=True)

# for peak can connection
myInterface = pcan_tmcl_interface('PCAN_USBBUS1', 1000000)

module = TMCM_1670(myInterface)
 
# motor configuration
module.setMaxTorque(2000)
module.showMotorConfiguration()
 
# encoder configuration
module.showEncoderConfiguration()
 
# motion settings
module.setMaxVelocity(4000)
module.setAcceleration(4000)
module.setRampEnabled(1)
module.setTargetReachedVelocity(500)
module.setTargetReachedDistance(10)
module.setMotorHaltedVelocity(5)
module.showMotionConfiguration()
 
# PI configuration
module.setTorquePParameter(1000)
module.setTorqueIParameter(1000)
module.setVelocityPParameter(2000)
module.setVelocityIParameter(1000)
module.setPositionPParameter(300)
module.showPIConfiguration()

# use out_0 output for enable input (directly shortened)
module.setDigitalOutput(0);

# rotate motor in right direction 
module.rotate(1000)
while module.digitalInput(0):
    print("waiting for right switch...")
    time.sleep(0.2)

# rotate motor in left direction
module.rotate(-1000)
while module.digitalInput(1):
    print("waiting for left switch...")
    time.sleep(0.2)

# stop motor
module.rotate(0)

print("Ready.")
myInterface.close()