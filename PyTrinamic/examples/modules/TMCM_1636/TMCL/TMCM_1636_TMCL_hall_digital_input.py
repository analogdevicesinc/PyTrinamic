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

connectionManager = ConnectionManager("--interface serial_tmcl --port COM4 --data-rate 115200")
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
    motor.DriveSetting.target_reached_distance = 5
    motor.DriveSetting.target_reached_velocity = 500
    motor.DriveSetting.commutation_mode = motor.ENUMs.COMM_MODE_DIGITAL_HALL
    print(motor.DriveSetting)

    # hall sensor configuration 
    motor.DigitalHall.direction = 0
    motor.DigitalHall.polarity = 1
    motor.DigitalHall.offset = 0
    motor.DigitalHall.interpolation = 1
    print(motor.DigitalHall)

    # motion settings 
    motor.LinearRamp.max_velocity = 2000
    motor.LinearRamp.max_acceleration = 1000
    motor.LinearRamp.enabled = 1 
    print(motor.LinearRamp)

    motor.set_axis_parameter(motor.APs.PositionScaler, 6*motor.DriveSetting.pole_pairs)
    # PI configuration 
    motor.PID.torque_p = 300 
    motor.PID.torque_i = 600
    motor.PID.velocity_p = 100
    motor.PID.velocity_i = 100
    motor.PID.position_p = 300
    print(motor.PID)

    # set position counter to zero
    motor.actual_position = 0

    print("\nRotate motor in clockwise direction...")
    motor.rotate(500)

    print("Press 'input_0' to swap the direction (waiting for input_0)")

    # wait for input_0 
    while (module.get_digital_input(module.IOs.GPI_0) == 1):
        print("actual position: %d   actual velocity: %d" % (motor.actual_position, motor.actual_velocity))
        time.sleep(0.2)

    print("\nRotate motor in counterclockwise direction...")
    motor.rotate(-500)

    print("Press 'input_1' to stop the motor (waiting for input_1)")

    # wait for input_1 
    while (module.get_digital_input(module.IOs.GPI_1) == 1):
        print("actual position: %d   actual velocity: %d" % (motor.actual_position, motor.actual_velocity))
        time.sleep(0.2)

    # stop motor 
    motor.rotate(0)

print("\nReady.")
