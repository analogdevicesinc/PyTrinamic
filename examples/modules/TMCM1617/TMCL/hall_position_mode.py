################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import time
import statistics
from dataclasses import dataclass

from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1617


# connection_manager = ConnectionManager("--interface serial_tmcl --port COM4 --data-rate 115200")
connection_manager = ConnectionManager("--interface kvaser_tmcl")

with connection_manager.connect() as my_interface:
    module = TMCM1617(my_interface)
    motor = module.motors[0]

    # Define motor configuration for the TMCM-1636.
    #
    # The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not work.

    # Current measurement ADC offset compensation
    @dataclass
    class AdcChannel:
        value_ap: int
        offset_ap: int
    for ch in [AdcChannel(motor.AP.AdcPhaseA, motor.AP.AdcOffsetPhaseA), AdcChannel(motor.AP.AdcPhaseB, motor.AP.AdcOffsetPhaseB)]:
        adc_samples = [motor.get_axis_parameter(ch.value_ap) for _ in range(20)]
        adc_samples_mean = round(statistics.mean(adc_samples))
        motor.set_axis_parameter(ch.offset_ap, adc_samples_mean)
    
    # motor configuration 
    motor.drive_settings.motor_type = motor.ENUM.MOTOR_TYPE_THREE_PHASE_BLDC
    motor.drive_settings.pole_pairs = 4
    motor.drive_settings.max_current = 2000
    motor.drive_settings.target_reached_distance = 5
    motor.drive_settings.target_reached_velocity = 500
    motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_DIGITAL_HALL
    print(motor.drive_settings)

    # hall sensor configuration 
    motor.digital_hall.direction = 1
    motor.digital_hall.polarity = 0
    motor.digital_hall.offset = 10000
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
    motor.pid.torque_i = 600
    motor.pid.velocity_p = 10
    motor.pid.velocity_i = 10
    motor.pid.position_p = 30
    print(motor.pid)

    # set position counter to zero
    motor.actual_position = 0

    # move to zero position
    motor.move_to(0)

    print("starting positioning")
    motor.move_to(4000)

    # wait for position reached 
    while not(motor.get_position_reached()):
        print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
        time.sleep(0.2)

    # move back to zero
    motor.move_to(0)

    # wait for position reached
    while not(motor.get_position_reached()):
        print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
        time.sleep(0.2)

print("\nReady.")
