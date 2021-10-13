#!/usr/bin/env python3
'''

Created on 28.11.2019

@author: SW, ED
'''

if __name__ == '__main__':
    pass

import PyTrinamic, time
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1636.TMCM_1636 import TMCM_1636

PyTrinamic.showInfo()

" please select your CAN adapter "
#myInterface = ConnectionManager("--interface pcan_tmcl").connect()
myInterface = ConnectionManager("--interface kvaser_tmcl").connect()

module = TMCM_1636(myInterface)
module.showModuleInfo()
motor = module.motor(0)

"""
    Define motor configuration for the TMCM-1636.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not work.
"""

" motor configuration "
motor.setMotorType(motor.ENUM.MOTOR_TYPE_THREE_PHASE_BLDC)
motor.setMotorPolePairs(4)
motor.setMaxTorque(2000)
motor.showConfiguration()

" hall sensor configuration "
motor.digitalHall.setDirection(0)
motor.digitalHall.setPolarity(1)
motor.digitalHall.setOffset(0)
motor.digitalHall.setInterpolation(1)
motor.digitalHall.showConfiguration()

" enable ref switch "
motor.setAxisParameter(motor.AP.ReferenceSwitchEnable, 3);
motor.setAxisParameter(motor.AP.ReferenceSwitchPolarity, 0);

print("\nRotate motor in clockwise direction...")
motor.rotate(500)

print("Waiting for right ref switch...")
while not motor.axisParameter(motor.AP.RightStopSwitch) :
    time.sleep(0.1);

print("Triggered!")
motor.rotate(-500)

print("Waiting for left ref switch...")
while not motor.axisParameter(motor.AP.LeftStopSwitch) :
    time.sleep(0.1);

print("Triggered!")
#print("Stopping motor...")
# module.setAxisParameter(module.APs.CommutationMode, 0);

myInterface.close()
print("\nReady.")
