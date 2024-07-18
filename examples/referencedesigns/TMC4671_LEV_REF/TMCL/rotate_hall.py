################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Turn a motor using hall sensors
"""

import pytrinamic
from pytrinamic.connections.connection_manager import ConnectionManager
from pytrinamic.referencedesigns import TMC4671_LEV_REF
import time

pytrinamic.show_info()

# please select your CAN adapter
# my_interface = ConnectionManager("--interface pcan_tmcl").connect()
my_interface = ConnectionManager("--interface kvaser_tmcl").connect()

with my_interface:
    module = TMC4671_LEV_REF(my_interface)
    motor = module.motors[0]

    # Define motor configuration for the TMC4671-LEV-REF.
    #
    # The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not work.

    # drive configuration
    motor.drive_settings.motor_type = motor.ENUM.MOTOR_TYPE_THREE_PHASE_BLDC
    motor.drive_settings.pole_pairs = 4
    motor.drive_settings.max_current = 2000
    motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_DIGITAL_HALL
    motor.drive_settings.target_reached_distance = 5
    motor.drive_settings.target_reached_velocity = 500
    print(motor.drive_settings)

    # hall sensor configuration
    motor.digital_hall.direction = 0
    motor.digital_hall.polarity = 1
    motor.digital_hall.offset = 0
    motor.digital_hall.interpolation = 1
    print(motor.digital_hall)

    # motion settings
    motor.linear_ramp.max_velocity = 2000
    motor.linear_ramp.max_acceleration = 500
    motor.linear_ramp.enabled = 1
    print(motor.linear_ramp)

    print("Starting motor...")
    motor.rotate(1000)
    time.sleep(3)

    print("Changing motor direction...")
    motor.rotate(-1000)
    time.sleep(6)

    print("Stopping motor...")
    motor.rotate(0)
    time.sleep(3)

    # power of
    motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_DISABLED

print("\nReady.")
