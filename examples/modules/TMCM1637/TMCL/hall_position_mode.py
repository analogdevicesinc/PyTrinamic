################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1637
import time

pytrinamic.show_info()
# connection_manager = ConnectionManager("--interface serial_tmcl --port COM4 --data-rate 115200")
connection_manager = ConnectionManager("--interface kvaser_tmcl --module-id 1")

with connection_manager.connect() as my_interface:
    module = TMCM1637(my_interface)
    motor = module.motors[0]

    # Define motor configuration for the TMCM-1637.
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

    # ramp settings 
    motor.linear_ramp.max_velocity = 2000
    motor.linear_ramp.max_acceleration = 1000
    motor.linear_ramp.enabled = 1 
    print(motor.linear_ramp)

    motor.set_axis_parameter(motor.AP.PositionScaler, 6*motor.drive_settings.pole_pairs)

    # PI configuration 
    motor.pid.torque_p = 300 
    motor.pid.torque_i = 300
    motor.pid.velocity_p = 300
    motor.pid.velocity_i = 100
    motor.pid.position_p = 200
    print(motor.pid)

    # clear actual position
    motor.actual_position = 0

    # set target position
    motor.move_to(4000)

    # wait for position reached 
    while not(motor.get_position_reached()):
        print("target position: {} actual position: {}".format(motor.target_position, motor.actual_position))
        time.sleep(0.2)

    # move back to zero
    motor.move_to(0)

    # wait for position reached
    while not(motor.get_position_reached()):
        print("target position: {} actual position: {}".format(motor.target_position, motor.actual_position))
        time.sleep(0.2)

print("\nReady.")
