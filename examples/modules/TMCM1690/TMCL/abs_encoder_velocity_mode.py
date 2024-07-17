################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################
"""Example script that shows how to use a TMCM-1690 with an absolute encoder in velocity mode.

The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
If you use a different motor be sure you have the right configuration setup otherwise the script may not work.
"""

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1690
import time

pytrinamic.show_info()

#cm = ConnectionManager("--interface pcan_tmcl")
cm = ConnectionManager("--interface kvaser_tmcl")
#cm = ConnectionManager("--interface serial_tmcl")

with cm.connect() as my_interface:

    module = TMCM1690(my_interface)
    print(module)
    motor = module.motors[0]

    # motor configuration
    motor.drive_settings.motor_type = motor.ENUM.MOTOR_TYPE_THREE_PHASE_BLDC
    motor.drive_settings.pole_pairs = 4
    motor.drive_settings.max_current = 2000
    print(motor.drive_settings)

    # absolute encoder configuration
    motor.abs_encoder.type = motor.ENUM.ABS_ENCODER_AM4096
    motor.abs_encoder.type = 1
    motor.abs_encoder.init_mode = motor.ENUM.ABS_ENCODER_INIT_MODE_USE_OFFSET

    # motion settings
    motor.ramp_settings.max_velocity = 2000
    motor.ramp_settings.max_acceleration = 4000
    motor.ramp_settings.enabled = 1
    motor.drive_settings.target_reached_distance = 50
    motor.drive_settings.target_reached_velocity = 500
    print(motor.ramp_settings)

    # PI configuration
    motor.pid.torque_p = 300
    motor.pid.torque_i = 600
    motor.pid.velocity_p = 300
    motor.pid.velocity_i = 600
    motor.pid.position_p = 10

    # Clear flags
    motor.set_axis_parameter(motor.AP.IITClearIITExceedFlags, 0)
    motor.set_axis_parameter(motor.AP.ClearVelocityWindowFlag, 0)
    motor.set_axis_parameter(motor.AP.ClearPositionWindowFlag, 0)

    # set commutation mode to absolute encoder
    motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_FOC_ABS_ENCODER

    # using sine ramp
    motor.ramp_settings.ramp_type = 1

    # Start rotating clockwise at 2000 rpm
    motor.target_velocity = 2000

    # wait for 5 second
    for i in range(5):
        print("target velocity: {} | actual velocity: {}".format(motor.target_velocity, motor.actual_velocity))
        time.sleep(1)

    # using linear ramp
    motor.ramp_settings.ramp_type = 0

    # Start rotating counter clockwise at 2000 rpm
    motor.target_velocity = -2000

    # wait for 5 second
    for i in range(5):
        print("target velocity: {} | actual velocity: {}".format(motor.target_velocity, motor.actual_velocity))
        time.sleep(1)

    # using sine ramp
    motor.ramp_settings.ramp_type = 1

    # Stop the motor.
    motor.target_velocity = 0

    print("\nReady.")
