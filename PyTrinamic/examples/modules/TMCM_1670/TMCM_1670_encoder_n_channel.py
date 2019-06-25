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

# sync actual position with encoder N-Channel 
module.setActualPosition(0)
module.rotate(200)
time.sleep(0.5)
module.clearOnceOnNChannel()
time.sleep(0.5)

# move to zero position
module.moveToPosition(0)
while not module.positionReached():
    print("target position: " + str(module.targetPosition()) + " actual position: " + str(module.actualPosition()))
    time.sleep(0.2)

# the actual position of 0 is now located at the N-Channel

print("Ready.")
myInterface.close()