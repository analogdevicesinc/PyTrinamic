#!/usr/bin/env python3
'''
Created on 31.01.2020

@author: Trinamic Software Team
'''

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules import TMCM_1630
import time

PyTrinamic.showInfo()

# please select a CAN or USB interface

# CAN
# myInterface = ConnectionManager("--interface pcan_tmcl").connect()
# myInterface = ConnectionManager("--interface kvaser_tmcl").connect()

# USB
myInterface = ConnectionManager().connect()

with myInterface:
    module = TMCM_1630(myInterface)
    motor = module.motors[0]

    # Define motor configuration for the TMCM-1630.
    #
    # The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not work.

    # drive configuration
    motor.DriveSetting.poles = 8
    motor.DriveSetting.max_current = 2000
    motor.DriveSetting.commutation_mode = motor.ENUMs.COMM_MODE_FOC_HALL
    motor.DriveSetting.target_reached_velocity = 500
    motor.DriveSetting.target_reached_distance = 5
    motor.DriveSetting.motor_halted_velocity = 5    # 50?
    print(motor.DriveSetting)

    # hall sensor configuration
    motor.DigitalHall.polarity = 0
    motor.DigitalHall.interpolation = 0
    print(motor.DigitalHall)

    # motion settings
    motor.LinearRamp.max_velocity = 1500
    motor.LinearRamp.max_acceleration = 2000
    motor.LinearRamp.enabled = 1
    print(motor.LinearRamp)

    # PI configuration
    motor.PID.torque_p = 600
    motor.PID.torque_i = 600
    motor.PID.velocity_p = 800
    motor.PID.velocity_i = 500
    motor.PID.position_p = 300
    print(motor.PID)

    time.sleep(1.0)

    # clear actual position
    motor.actual_position = 0

    print("\nRotate motor in clockwise direction...")
    motor.rotate(500)

    print("Press 'input_0' to swap the direction (waiting for input_0)\n")

    # wait for input_0
    while module.get_digital_input(0) == 1:
        print("actual position: %d   actual velocity: %d   actual torque: %d" % (motor.actual_position,
              motor.actual_velocity, motor.get_axis_parameter(motor.APs.ActualTorque, True)))
        time.sleep(0.2)

    print("\nRotate motor in counterclockwise direction...")
    motor.rotate(-500)

    print("Press 'input_1' to stop the motor (waiting for input_1)\n")

    # wait for input_1
    while module.get_digital_input(1) == 1:
        print("actual position: %d   actual velocity: %d   actual torque: %d" % (motor.actual_position,
              motor.actual_velocity, motor.get_axis_parameter(motor.APs.ActualTorque, True)))
        time.sleep(0.2)

    # stop motor
    motor.rotate(0)

print("\nReady.")
