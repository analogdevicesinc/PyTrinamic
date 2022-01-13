#!/usr/bin/env python3
'''
Created on 28.11.2019

@author: Trinamic Software Team
'''

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules import TMCM_1636
import time

PyTrinamic.showInfo()
# connectionManager = ConnectionManager("--interface serial_tmcl --port COM4 --data-rate 115200")
connectionManager = ConnectionManager("--interface kvaser_tmcl --module-id 1")

with connectionManager.connect() as myInterface: 
    module = TMCM_1636(myInterface)
    motor = module.motors[0]

    # Define motor configuration for the TMCM-1636.
    #
    # The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not work.

    # drive configuration
    motor.DriveSetting.motor_type = motor.ENUMs.MOTOR_TYPE_THREE_PHASE_BLDC
    motor.DriveSetting.pole_pairs = 4
    motor.DriveSetting.max_current = 2000
    motor.DriveSetting.commutation_mode = motor.ENUMs.COMM_MODE_DIGITAL_HALL
    print(motor.DriveSetting)

    # hall sensor configuration
    motor.DigitalHall.direction = 0
    motor.DigitalHall.polarity = 1
    motor.DigitalHall.offset = 0
    motor.DigitalHall.interpolation = 1
    print(motor.DigitalHall)

    # enable ref switch 
    motor.set_axis_parameter(motor.APs.ReferenceSwitchEnable, 3)
    motor.set_axis_parameter(motor.APs.ReferenceSwitchPolarity, 0)

    print("\nRotate motor in clockwise direction...")
    motor.rotate(500)

    print("Waiting for right ref switch...")
    while not motor.get_axis_parameter(motor.APs.RightStopSwitch):
        time.sleep(0.1)

    print("Triggered!")
    motor.rotate(-500)

    print("Waiting for left ref switch...")
    while not motor.get_axis_parameter(motor.APs.LeftStopSwitch):
        time.sleep(0.1)

    print("Triggered!")
    print("Stopping motor...")
    motor.rotate(0)

print("\nReady.")
