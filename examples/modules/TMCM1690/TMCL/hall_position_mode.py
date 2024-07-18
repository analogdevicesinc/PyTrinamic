################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

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

    # hall sensor configuration
    motor.digital_hall.direction = 1
    motor.digital_hall.sector_offset = 1
    motor.digital_hall.interpolation = 1
    print(motor.digital_hall)

    # motion settings
    motor.ramp_settings.max_velocity = 2000
    motor.ramp_settings.max_acceleration = 2000
    motor.ramp_settings.enabled = 1
    motor.drive_settings.target_reached_distance = 10
    motor.drive_settings.target_reached_velocity = 500
    print(motor.ramp_settings)

    # PI configuration
    motor.pid.torque_p = 300
    motor.pid.torque_i = 600
    motor.pid.velocity_p = 600
    motor.pid.velocity_i = 300
    motor.pid.position_p = 20
    print(motor.pid)

    # Clear flags
    motor.set_axis_parameter(motor.AP.IITClearIITExceedFlags, 0)
    motor.set_axis_parameter(motor.AP.ClearVelocityWindowFlag, 0)
    motor.set_axis_parameter(motor.AP.PositionWindow, 16384000)
    motor.set_axis_parameter(motor.AP.ClearPositionWindowFlag, 0)

    # Disable brake chopper
    motor.brake_chopper.enabled = 0

    # set commutation mode to absolute encoder
    motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_FOC_DIGITAL_HALL

    # set position counter to zero
    motor.actual_position = 0

    # move to zero position
    motor.target_position = 0

    # using linear ramp
    motor.ramp_settings.ramp_type = 0

    print("starting positioning")
    motor.target_position = 4000

    # wait for position reached
    while not motor.get_position_reached():
        print("target position: {} | actual position: {}".format(motor.target_position, motor.actual_position))
        time.sleep(0.2)

    # using sine ramp
    motor.ramp_settings.ramp_type = 1

    # move back to zero
    motor.target_position = 0

    # wait for position reached
    while not motor.get_position_reached():
        print("target position: {} | actual position: {}".format(motor.target_position, motor.actual_position))
        time.sleep(0.2)

    print("\nReady.")
