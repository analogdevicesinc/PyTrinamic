################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1640
import time

pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
    print(my_interface)

    module = TMCM1640(my_interface)
    motor = module.motors[0]

    # Define motor configuration for the TMCM-1640.
    #
    # The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not work.

    # drive configuration
    motor.drive_settings.poles = 8
    motor.drive_settings.max_current = 2000
    motor.drive_settings.target_reached_velocity = 500
    motor.drive_settings.target_reached_distance = 5

    # hall sensor configuration
    motor.digital_hall.polarity = 0
    motor.digital_hall.interpolation = 0
    print(motor.digital_hall)

    # encoder configuration
    motor.abn_encoder.resolution = 4096
    # motor.abn_encoder.resolution = 16384
    motor.abn_encoder.direction = 0
    motor.abn_encoder.init_mode = motor.ENUM.ENCODER_INIT_MODE_1
    print(motor.abn_encoder)

    # motion settings
    motor.linear_ramp.max_velocity = 2048
    motor.linear_ramp.max_acceleration = 10000
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

    # set commutation mode to FOC based on encoder feedback
    motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_FOC_ENCODER
    print(motor.drive_settings)

    # read adc value and compute new target velocity
    while True:
        adcValue = module.get_analog_input(0)
        targetVelocity = (adcValue - 1024) * 2
        motor.rotate(targetVelocity)
        print("adc value: " + str(adcValue) + " target velocity: " + str(targetVelocity)
              + " actual velocity: " + str(motor.actual_velocity))
        time.sleep(0.2)
