################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1630
import time

pytrinamic.show_info()

# please select a CAN or USB interface

# CAN
# my_interface = ConnectionManager("--interface pcan_tmcl").connect()
# my_interface = ConnectionManager("--interface kvaser_tmcl").connect()

# USB
my_interface = ConnectionManager().connect()

with my_interface:
    module = TMCM1630(my_interface)
    motor = module.motors[0]

    # Define motor configuration for the TMCM-1630.
    #
    # The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not work.

    # drive configuration
    motor.drive_settings.poles = 8
    motor.drive_settings.max_current = 2000
    motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_FOC_HALL
    motor.drive_settings.target_reached_velocity = 500
    motor.drive_settings.target_reached_distance = 5
    motor.drive_settings.motor_halted_velocity = 5
    print(motor.drive_settings)

    # hall sensor configuration
    motor.digital_hall.polarity = 0
    motor.digital_hall.interpolation = 0
    print(motor.digital_hall)

    # motion settings
    motor.linear_ramp.max_velocity = 1000
    motor.linear_ramp.max_acceleration = 2000
    motor.linear_ramp.enabled = 1
    print(motor.linear_ramp)

    # PI configuration
    motor.pid.torque_p = 600
    motor.pid.torque_i = 600
    motor.pid.velocity_p = 800
    motor.pid.velocity_i = 500
    motor.pid.position_p = 300
    print(motor.pid)

    time.sleep(1.0)

    # clear actual position
    motor.actual_position = 0

    print("move to first position")
    motor.move_to(motor.drive_settings.poles * 3 * 50)

    # wait for position reached
    while not motor.get_position_reached():
        print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
        time.sleep(0.2)

    print("move back to zero")
    motor.move_to(0)

    # wait for position reached
    while not motor.get_position_reached():
        print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
        time.sleep(0.2)

print("\nReady.")
