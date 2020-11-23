#!/usr/bin/env python3
'''
Created on 31.01.2020

@author: JM, ED
'''

if __name__ == '__main__':
    pass

import PyTrinamic, time
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1630.TMCM_1630 import TMCM_1630

PyTrinamic.showInfo()

" please select your CAN adapter "
#myInterface = ConnectionManager("--interface pcan_tmcl").connect()
myInterface = ConnectionManager("--interface kvaser_tmcl").connect()

module = TMCM_1630(myInterface)
module.showModuleInfo()
motor = module.motor(0)

"""
    Define motor configuration for the TMCM-1630.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not work.
"""

" motor configuration "
motor.setMotorPolePairs(4)
motor.setMaxTorque(2000)
motor.showConfiguration()

" hall configuration "
motor.digitalHall.setHallInvert(0)
motor.digitalHall.showConfiguration()

" encoder configuration "
motor.abnEncoder.setResolution(4096)
motor.abnEncoder.setDirection(0)
motor.abnEncoder.setInitMode(motor.ENUM.ENCODER_INIT_MODE_0)
motor.abnEncoder.showConfiguration()

" motion settings "
motor.linearRamp.setMaxVelocity(2048)
motor.linearRamp.setAcceleration(10000)
motor.linearRamp.setRampEnabled(1)
motor.linearRamp.setTargetReachedVelocity(500)
motor.linearRamp.setTargetReachedDistance(5)
motor.linearRamp.showConfiguration()

" PI configuration "
motor.pid.setTorquePIParameter(600, 600)
motor.pid.setVelocityPIParameter(800, 600)
motor.pid.setPositionPParameter(300)
motor.pid.showConfiguration()

" set commutation mode to FOC based on hall sensor signals "
motor.commutationSelection.setMode(motor.ENUM.COMM_MODE_FOC_ENCODER)
motor.commutationSelection.showConfiguration()

" read adc value and compute new target velocity "
while True:
    adcValue = module.analogInput(0)
    targetVelocity = (adcValue - 1024) * 2
    motor.rotate(targetVelocity)
    print("adc value: " + str(adcValue) + " target velocity: " + str(targetVelocity) + " actual velocity: " + str(motor.actualVelocity()))
    time.sleep(0.2)

myInterface.close()
print("\nReady.")