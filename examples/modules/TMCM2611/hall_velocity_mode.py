################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM2611
import time


connection_manager = ConnectionManager()

with connection_manager.connect() as my_interface:
    module = TMCM2611(my_interface)
    motor = module.motors[0]

    # Define motor configuration for the TMCM-2611.
    # The configuration is based on the Trinamic standard BLDC motor (QBL4208-100-04-025-1024-AT).
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not work.

    # motor configuration
    motor.drive_settings.pole_pairs = 4
    motor.drive_settings.max_current = 2000
    motor.drive_settings.target_reached_distance = 5
    motor.drive_settings.target_reached_velocity = 500
    motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_DIGITAL_HALL

    # hall sensor configuration
    motor.digital_hall.direction = 0
    motor.digital_hall.polarity = 1
    motor.digital_hall.offset = 0

    # ramp settings
    motor.linear_ramp.max_velocity = 2000
    motor.linear_ramp.max_acceleration = 1000
    motor.linear_ramp.enabled = 1

    motor.set_axis_parameter(motor.AP.PositionScaler, 6 * motor.drive_settings.pole_pairs)

    # PI configuration
    motor.pid.torque_p = 2600
    motor.pid.torque_i = 128
    motor.pid.velocity_p = 2300
    motor.pid.velocity_i = 500

    motor.target_velocity = 500  # RPM
    time.sleep(3)
    motor.target_velocity = 0

    motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_DISABLED
