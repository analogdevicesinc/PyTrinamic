################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import statistics
import time

from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1636


connection_manager = ConnectionManager("--interface kvaser_tmcl")

with connection_manager.connect() as my_interface:
    module = TMCM1636(my_interface)
    motor = module.motors[0]

    # Offset compensation for both current measurement ADCs (I0 and I1)
    for ap_adc_ix_raw, ap_adc_ix_offset in [(motor.AP.AdcPhaseA, motor.AP.AdcOffsetPhaseA), (motor.AP.AdcPhaseB, motor.AP.AdcOffsetPhaseB)]:
        adc_samples = [motor.get_axis_parameter(ap_adc_ix_raw) for _ in range(40)]
        adc_samples_mean = round(statistics.mean(adc_samples))
        motor.set_axis_parameter(ap_adc_ix_offset, adc_samples_mean)
        my_interface.store_axis_parameter(ap_adc_ix_offset, 0)

    # Define motor configuration for the TMCM-1636.
    #
    # The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not work.

    # Drive configuration
    motor.drive_settings.motor_type = motor.ENUM.MOTOR_TYPE_THREE_PHASE_BLDC
    motor.drive_settings.pole_pairs = 4
    motor.drive_settings.max_current = 2000
    motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_ABN_ENCODER
    motor.drive_settings.open_loop_current = 1000

    # Hall configuration
    motor.digital_hall.direction = 0
    motor.digital_hall.polarity = 1
    motor.digital_hall.offset = 0

    # Encoder configuration 
    motor.abn_encoder.resolution = 4096
    motor.abn_encoder.direction = 1
    motor.abn_encoder.init_mode = motor.ENUM.ENCODER_INIT_MODE_2 # Hall configuration must be correct for this to work

    # Motion settings 
    motor.linear_ramp.max_velocity = 2000
    motor.linear_ramp.max_acceleration = 1000
    motor.linear_ramp.enabled = 1

    # PI configuration 
    motor.pid.torque_p = 300 
    motor.pid.torque_i = 600
    motor.pid.velocity_p = 100
    motor.pid.velocity_i = 100

    # Set target velocity 
    motor.rotate(2000)
    time.sleep(4)

    # Stop the motor
    motor.stop()
    time.sleep(2)

    motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_DISABLED
