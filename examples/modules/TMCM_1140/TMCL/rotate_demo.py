#!/usr/bin/env python3
'''
Move a motor back and forth using the TMCM1140 module

Created on 13.07.2021

@author: Trinamic Software Team
'''

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules import TMCM_1140
import time

PyTrinamic.showInfo()
connectionManager = ConnectionManager("--interface serial_tmcl --port COM6 --data-rate 115200")

with connectionManager.connect() as myInterface: 
    module = TMCM_1140(myInterface)
    motor = module.motors[0]

    # The configuration is based on our PD42-1-1140-TMCL
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not working.

    print("Preparing parameters")
    #preparing drive settings 
    motor.DriveSetting.max_current= 1000
    motor.DriveSetting.standby_current = 0
    motor.DriveSetting.boost_current = 0
    motor.DriveSetting.microstep_resolution = motor.ENUMs.microstep_resolution_256_microsteps
    print(motor.DriveSetting)

    #preparing linear ramp settings 
    motor.max_acceleration = 1000
    motor.max_velocity = 1000

    #reset actual position 
    motor.actual_position = 0

    #start rotating motor for 5 sek 
    print("Rotating")
    motor.rotate(1000)
    time.sleep(5)

    #stop rotating motor
    print("Stopping")
    motor.stop()
    
    #read actual position
    print("ActualPostion = {}".format(motor.actual_position))
    time.sleep(2)
    
    #Doubling moved distance
    print("Doubling moved distance")
    motor.move_by(motor.actual_position)
    #wait till  position_reached
    while not(motor.get_position_reached()):
        print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
        time.sleep(0.2)
    print("Furthest point reached")
    print("ActualPostion = {}".format(motor.actual_position))

    #short delay and move back to start
    time.sleep(2)
    print("Moving back to 0")
    motor.move_to(0)

    # Wait until position 0 is reached
    while not(motor.get_position_reached()):
        print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
        time.sleep(0.2)

    print("Reached Position 0")

print("\nReady.")
