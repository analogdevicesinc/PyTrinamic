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
    module = TMCM1670(my_interface, 1)
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

    # sync actual position with encoder N-Channel
    motor.actual_position = 0
    motor.rotate(200)
    time.sleep(0.5)
    motor.set_axis_parameter(motor.AP.ClearOnce, 1)
    motor.set_axis_parameter(motor.AP.ClearOnNull, 1)
    time.sleep(0.5)
 
    # move to zero position which is now located at the N-Channel
    motor.move_to(0)
    while not motor.get_position_reached():
        print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
        time.sleep(0.2)
 
print("\nReady.")
