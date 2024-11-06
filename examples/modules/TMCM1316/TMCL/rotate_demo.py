################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""
Rotate the motor with the specified velocity to reach the target position.
"""

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1316
import time

pytrinamic.show_info()

connection_manager = ConnectionManager()  # If no Interface is selected , the default interface is usb_tmcl
with connection_manager.connect() as my_interface:
    module = TMCM1316(my_interface)
    motor = module.motors[0]

    # Please be sure not to use a too high current setting for your motor.

    print("Preparing parameters")
    # preparing drive settings
    motor.drive_settings.max_current = 128
    motor.drive_settings.standby_current = 0
    motor.drive_settings.boost_current = 0
    motor.drive_settings.microstep_resolution = motor.ENUM.microstep_resolution_256_microsteps
    print(motor.drive_settings)

    # preparing linear ramp settings
    motor.max_acceleration = 51200
    motor.max_velocity = 51200

    # reset actual position
    motor.actual_position = 0

    # start rotating motor in different directions
    print("Rotating...")
    motor.rotate(51200)
    time.sleep(5)

    # stop rotating motors
    print("Stopping...")
    motor.stop()

    # read actual position
    print("ActualPostion = {}".format(motor.actual_position))
    time.sleep(2)

    # short delay and move back to start
    print("Moving back to 0")
    motor.move_to(0)

    # wait until position 0 is reached
    while not(motor.get_position_reached()):
        print("target position motor: " + str(motor.target_position) + " actual position motor: " + str(motor.actual_position))
        time.sleep(0.2)

    print("Reached Position 0")

print("\nReady.")
