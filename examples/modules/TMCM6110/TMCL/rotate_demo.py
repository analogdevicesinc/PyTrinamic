#!/usr/bin/env python3
'''
Move a motor_0 and motor_1 back and forth using the TMCM1636 module

Created on 13.07.2021

@author: Trinamic Software Team
'''

import pytrinamic2
from pytrinamic2.connections.connection_manager import ConnectionManager
from pytrinamic2.modules import TMCM6110
import time

pytrinamic2.show_info()
connectionManager = ConnectionManager("--interface serial_tmcl --port COM6 --data-rate 115200")

with connectionManager.connect() as myInterface: 
    module = TMCM6110(myInterface)
    motor_0 = module.motors[0]
    motor_1 = module.motors[1]
    motor_2 = module.motors[2]
    motor_3 = module.motors[3]
    motor_4 = module.motors[4]
    motor_5 = module.motors[5]

    # The configuration is based on our 
    # If you use a different motor_0 be sure you have the right configuration setup otherwise the script may not working.

    print("Preparing parameters")
    #preparing drive settings 
    motor_0.drive_settings.max_current= 1000
    motor_0.drive_settings.standby_current = 0
    motor_0.drive_settings.boost_current = 0
    motor_0.drive_settings.microstep_resolution = motor_0.ENUM.microstep_resolution_256_microsteps
    print(motor_0.drive_settings)
    motor_1.drive_settings.max_current= 1000
    motor_1.drive_settings.standby_current = 0
    motor_1.drive_settings.boost_current = 0
    motor_1.drive_settings.microstep_resolution = motor_0.ENUM.microstep_resolution_256_microsteps
    print(motor_1.drive_settings)

    #preparing linear ramp settings 
    motor_0.max_acceleration = 1000
    motor_0.max_velocity = 1000
    motor_1.max_acceleration = 1000
    motor_1.max_velocity = 1000
    #reset actual position 
    motor_0.actual_position = 0
    motor_1.actual_position = 0

    print(motor_0.linear_ramp)    
    print(motor_1.linear_ramp)

    #start rotating motor_0 and motor_1 in different directions
    print("Rotating")
    motor_0.rotate(1500)
    motor_1.rotate(-1500)
    time.sleep(5)

    #stop rotating motors
    print("Stopping")
    motor_0.stop()
    motor_1.stop()

    #read actual position
    print("ActualPostion = {}".format(motor_0.actual_position))
    print("ActualPostion = {}".format(motor_1.actual_position))
    time.sleep(2)
    
    #Doubling moved distance
    print("Doubling moved distance")
    motor_0.move_by(motor_0.actual_position)
    motor_1.move_by(motor_1.actual_position)

    #wait till  position_reached
    while not(motor_0.get_position_reached() and motor_1.get_position_reached()):
        print("target position motor_0: " + str(motor_0.target_position) + " actual position motor_0: " + str(motor_0.actual_position))
        print("target position motor_1: " + str(motor_0.target_position) + " actual position motor_1: " + str(motor_0.actual_position))

    time.sleep(0.2)
    print("Furthest point reached")
    print("ActualPostion motor_0 = {}".format(motor_0.actual_position))
    print("ActualPostion motor_1 = {}".format(motor_1.actual_position))

    #short delay and move back to start
    time.sleep(2)
    print("Moving back to 0")
    motor_0.move_to(0)
    motor_1.move_to(0)

    # Wait until position 0 is reached
    while not(motor_0.get_position_reached() and motor_1.get_position_reached()):
        print("target position motor_0: " + str(motor_0.target_position) + " actual position motor_0: " + str(motor_0.actual_position))
        print("target position motor_1: " + str(motor_0.target_position) + " actual position motor_1: " + str(motor_0.actual_position))        
        time.sleep(0.2)
    print("Reached Position 0")

print("\nReady.")
