################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM6212
import time

pytrinamic.show_info()

connection_manager = ConnectionManager()  # If no Interface is selected , the default interface is usb_tmcl
with connection_manager.connect() as my_interface:
    module = TMCM6212(my_interface)
    motor_0 = module.motors[0]  # Using motors 0, 3, and 5; change here to use different motors
    motor_1 = module.motors[3]
    motor_2 = module.motors[5]

    # Please be sure not to use a too high current setting for your motor.

    print("Preparing parameters")
    # preparing drive settings
    motor_0.drive_settings.max_current = 128
    motor_0.drive_settings.standby_current = 0
    motor_0.drive_settings.boost_current = 0
    motor_0.drive_settings.microstep_resolution = motor_0.ENUM.microstep_resolution_256_microsteps
    print(motor_0.drive_settings)
    motor_1.drive_settings.max_current = 128
    motor_1.drive_settings.standby_current = 0
    motor_1.drive_settings.boost_current = 0
    motor_1.drive_settings.microstep_resolution = motor_0.ENUM.microstep_resolution_256_microsteps
    print(motor_1.drive_settings)
    motor_2.drive_settings.max_current = 128
    motor_2.drive_settings.standby_current = 0
    motor_2.drive_settings.boost_current = 0
    motor_2.drive_settings.microstep_resolution = motor_0.ENUM.microstep_resolution_256_microsteps
    print(motor_2.drive_settings)

    # preparing linear ramp settings
    motor_0.max_acceleration = 51200
    motor_0.max_velocity = 51200
    motor_1.max_acceleration = 25600
    motor_1.max_velocity = 25600
    motor_2.max_acceleration = 102400
    motor_2.max_velocity = 51200

    # reset actual position
    motor_0.actual_position = 0
    motor_1.actual_position = 0
    motor_2.actual_position = 0

    print(motor_0.linear_ramp)    
    print(motor_1.linear_ramp)
    print(motor_2.linear_ramp)

    # start rotating motor_0 and motor_1 in different directions
    print("Rotating")
    motor_0.rotate(51200)
    motor_1.rotate(-25600)
    motor_2.rotate(102400)
    time.sleep(5)

    # stop rotating motors
    print("Stopping")
    motor_0.stop()
    motor_1.stop()
    motor_2.stop()

    # read actual position
    print("ActualPostion = {}".format(motor_0.actual_position))
    print("ActualPostion = {}".format(motor_1.actual_position))
    print("ActualPostion = {}".format(motor_2.actual_position))
    time.sleep(2)
    
    # doubling moved distance
    print("Doubling moved distance")
    motor_0.move_by(motor_0.actual_position)
    motor_1.move_by(motor_1.actual_position)
    motor_2.move_by(motor_2.actual_position)

    # wait till  position_reached
    while not(motor_0.get_position_reached() and motor_1.get_position_reached() and motor_2.get_position_reached()):
        print("target position motor_0: " + str(motor_0.target_position) + " actual position motor_0: " + str(motor_0.actual_position))
        print("target position motor_1: " + str(motor_1.target_position) + " actual position motor_1: " + str(motor_1.actual_position))
        print("target position motor_2: " + str(motor_2.target_position) + " actual position motor_2: " + str(motor_2.actual_position))

    time.sleep(0.2)
    print("Furthest point reached")
    print("ActualPostion motor_0 = {}".format(motor_0.actual_position))
    print("ActualPostion motor_1 = {}".format(motor_1.actual_position))
    print("ActualPostion motor_2 = {}".format(motor_2.actual_position))

    # short delay and move back to start
    time.sleep(2)
    print("Moving back to 0")
    motor_0.move_to(0)
    motor_1.move_to(0)
    motor_2.move_to(0)

    # wait until position 0 is reached
    while not(motor_0.get_position_reached() and motor_1.get_position_reached() and motor_2.get_position_reached()):
        print("target position motor_0: " + str(motor_0.target_position) + " actual position motor_0: " + str(motor_0.actual_position))
        print("target position motor_1: " + str(motor_1.target_position) + " actual position motor_1: " + str(motor_1.actual_position))        
        print("target position motor_2: " + str(motor_2.target_position) + " actual position motor_2: " + str(motor_2.actual_position))        
        time.sleep(0.2)

    print("Reached Position 0")

print("\nReady.")
