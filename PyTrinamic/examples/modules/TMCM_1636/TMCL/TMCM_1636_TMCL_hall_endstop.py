#!/usr/bin/env python3
'''

Created on 28.11.2019

@author: SW, ED, JH
'''

if __name__ == '__main__':
    pass

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1636.TMCM_1636 import TMCM_1636
import time

PyTrinamic.showInfo()

connectionManager = ConnectionManager("--interface serial_tmcl --port COM4 --data-rate 115200")
myInterface = connectionManager.connect()
module = TMCM_1636(myInterface)
motor = module.MOTORS[0]

"""
    Define motor configuration for the TMCM-1636.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not work.
"""

" motor configuration "
motor.BLDCMotor.type = motor.ENUMs.MOTOR_TYPE_THREE_PHASE_BLDC
motor.BLDCMotor.pole_pairs = 4
motor.BLDCMotor.max_torque = 2000
print(motor.BLDCMotor.__str__())

" hall sensor configuration "
motor.DigitalHallWeasel.direction = 0
motor.DigitalHallWeasel.polarity = 1
motor.DigitalHallWeasel.offset = 0
motor.DigitalHallWeasel.interpolation = 1
print(motor.DigitalHallWeasel.__str__())

" set commutation mode to FOC based on hall sensor signals "
motor.CommutationSelection.mode = motor.ENUMs.COMM_MODE_DIGITAL_HALL
print(motor.CommutationSelection.__str__())

" enable ref switch "
motor.set_axis_parameter(motor.APs.ReferenceSwitchEnable, 3)
motor.set_axis_parameter(motor.APs.ReferenceSwitchPolarity, 0)

print("\nRotate motor in clockwise direction...")
motor.rotate(500)

print("Waiting for right ref switch...")
while not motor.get_axis_parameter(motor.APs.RightStopSwitch) :
    time.sleep(0.1)

print("Triggered!")
motor.rotate(-500)

print("Waiting for left ref switch...")
while not motor.get_axis_parameter(motor.APs.LeftStopSwitch) :
    time.sleep(0.1)

print("Triggered!")
#print("Stopping motor...")
# module.setAxisParameter(module.APs.CommutationMode, 0);

myInterface.close()
print("\nReady.")
