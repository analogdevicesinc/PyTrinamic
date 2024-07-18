################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1633
import time

pytrinamic.show_info()

# please select your CAN adapter
# my_interface = ConnectionManager("--interface pcan_tmcl").connect()
my_interface = ConnectionManager("--interface kvaser_tmcl").connect()

with my_interface:
    module = TMCM1633(my_interface)
    motor = module.motors[0]

    # Define motor configuration for the TMCM-1633.
    #
    # The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not work.

    # drive configuration
    motor.drive_settings.poles = 8
    motor.drive_settings.max_current = 2000
    motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_FOC_HALL
    motor.drive_settings.target_reached_velocity = 500
    motor.drive_settings.target_reached_distance = 5
    motor.drive_settings.motor_halted_velocity = 5    # 50?
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

    print("\nRotate motor in clockwise direction...")
    motor.rotate(500)

    print("Press 'input_0' to swap the direction (waiting for input_0)\n")

    # wait for input_0
    while module.get_digital_input(module.DI.IN_0) == 1:
        print("actual position: %d   actual velocity: %d   actual torque: %d" % (motor.actual_position,
              motor.actual_velocity, motor.get_axis_parameter(motor.AP.ActualTorque, True)))
        time.sleep(0.2)

    print("\nRotate motor in counterclockwise direction...")
    motor.rotate(-500)

    print("Press 'input_1' to stop the motor (waiting for input_1)\n")

    # wait for input_1
    while module.get_digital_input(module.DI.IN_1) == 1:
        print("actual position: %d   actual velocity: %d   actual torque: %d" % (motor.actual_position,
              motor.actual_velocity, motor.get_axis_parameter(motor.AP.ActualTorque, True)))
        time.sleep(0.2)

    # stop motor
    motor.rotate(0)

print("\nReady.")
