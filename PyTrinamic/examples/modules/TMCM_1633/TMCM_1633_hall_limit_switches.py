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

# set commutation mode to FOC based on hall sensor signals
module.setCommutationMode(module.COMM_MODE_FOC_HALL)

# use velocity mode until switch is active

# set GPIO_LED
module.setDigitalOutput(1)

# velocity control
while module.digitalInput(0):
    analogValue0 = module.analogInput(0)
    targetVelocity = (analogValue0 - 1024) * 2;  
    print("analog input 0: " + str(analogValue0) + "   target velocity: " +str(targetVelocity))
    module.rotate(targetVelocity)
    time.sleep(0.2)

# use torque mode until switch is active

# clear GPIO_LED
module.setDigitalOutput(0)

# torqhe control
while module.digitalInput(1):
    analogValue1 = module.analogInput(1)
    targetTorque = analogValue1 - 1024;  
    print("analog input 1: " + str(analogValue1) + "   target torque: " +str(targetTorque))
    module.setTargetTorque(targetTorque)
    time.sleep(0.2)

# stop motor
module.rotate(0)

print("Ready.")
myInterface.close()