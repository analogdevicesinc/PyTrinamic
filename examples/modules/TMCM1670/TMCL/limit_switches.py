################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1670
import time

pytrinamic.show_info()

# please select your CAN adapter
# my_interface = ConnectionManager("--interface pcan_tmcl").connect()
my_interface = ConnectionManager("--interface kvaser_tmcl").connect()

with my_interface:
    module = TMCM1670(my_interface)
    motor = module.motors[0]

    # drive configuration
    motor.drive_settings.poles = 8
    motor.drive_settings.max_current = 2000
    motor.drive_settings.target_reached_velocity = 500
    motor.drive_settings.target_reached_distance = 10
    motor.drive_settings.motor_halted_velocity = 5
    motor.drive_settings.open_loop_current = 1000
    print(motor.drive_settings)

    # encoder configuration
    print(motor.absolute_encoder)

    # motion settings
    motor.linear_ramp.max_velocity = 4000
    motor.linear_ramp.max_acceleration = 4000
    motor.linear_ramp.enabled = 1
    print(motor.linear_ramp)

    # PI configuration
    motor.pid.torque_p = 1000
    motor.pid.torque_i = 1000
    motor.pid.velocity_p = 2000
    motor.pid.velocity_i = 1000
    motor.pid.position_p = 300
    print(motor.pid)

    time.sleep(1.0)

    # use out_0 output for enable input (directly shortened)
    module.set_digital_output(module.DO.OUT_0)

    # rotate motor in right direction
    motor.rotate(1000)
    while module.get_digital_input(module.DI.REF_R):
        print("waiting for right switch...")
        time.sleep(0.2)

    # rotate motor in left direction
    motor.rotate(-1000)
    while module.get_digital_input(module.DI.REF_L):
        print("waiting for left switch...")
        time.sleep(0.2)

    # stop motor
    motor.rotate(0)

print("\nReady.")
