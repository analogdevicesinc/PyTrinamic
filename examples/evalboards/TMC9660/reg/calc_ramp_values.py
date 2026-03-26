################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Calculate register values for the ramp generator configuration

The results are based on the selected feedback and the desired ramp behavior
given in RPM for the velocity and RPM per second for the acceleration.
"""

from typing import Literal, Callable


# Select the FOC feedback
commutation_feedback_select: Literal["ABN encoder", "Digital hall"] = "Digital hall"

# Select the velocity feedback
# Ideally the "count" selection is used.
velocity_feedback_select: Literal["Same as commutation", "ABN encoder count", "Digital hall count"] = "Digital hall count"

number_of_ramp_points: Literal[4, 6, 8] = 6

MOTOR_POLE_PAIRS = 4
ABN_COUNTS_PER_REVOLUTION = 4096

if velocity_feedback_select == "Same as commutation":
    velocity_scaling_factor = 2**40*MOTOR_POLE_PAIRS/40e6/60
elif velocity_feedback_select == "ABN encoder count":
    velocity_scaling_factor = 2**24*ABN_COUNTS_PER_REVOLUTION/40e6/60
elif velocity_feedback_select == "Digital hall count":
    velocity_scaling_factor = 2**24*6*MOTOR_POLE_PAIRS/40e6/60

acceleration_scaling_factor = velocity_scaling_factor*2**17/40e6


def velocity_rpm_to_internal(rpm_value):
    return int(rpm_value*velocity_scaling_factor)


def acceleration_rpms_to_internal(rpms_value):
    return int(rpms_value*acceleration_scaling_factor)

    
if number_of_ramp_points == 4:
    RAMPER_A_MAX = acceleration_rpms_to_internal(1000)  # Acceleration 1000 RPM per second
    RAMPER_D_MAX = acceleration_rpms_to_internal(1000)  # Deceleration 1000 RPM per second
    RAMPER_V2 = 0
    RAMPER_V1 = 0
elif number_of_ramp_points == 6:
    RAMPER_A_MAX = acceleration_rpms_to_internal(1000)  # Acceleration 1000 RPM per second
    RAMPER_D_MAX = acceleration_rpms_to_internal(1000)  # Deceleration 1000 RPM per second
    RAMPER_V2 = velocity_rpm_to_internal(1000)
    RAMPER_A2 = acceleration_rpms_to_internal(500) # Acceleration 500 RPM per second
    RAMPER_D2 = acceleration_rpms_to_internal(500)  # Deceleration 500 RPM per second
    RAMPER_V1 = velocity_rpm_to_internal(0)
elif number_of_ramp_points == 8:
    RAMPER_A_MAX = acceleration_rpms_to_internal(500)  # Acceleration 500 RPM per second
    RAMPER_D_MAX = acceleration_rpms_to_internal(500)  # Deceleration 500 RPM per second
    RAMPER_V2 = velocity_rpm_to_internal(1600)
    RAMPER_A2 = acceleration_rpms_to_internal(1000)  # Acceleration 1000 RPM per second
    RAMPER_D2 = acceleration_rpms_to_internal(1000)  # Deceleration 1000 RPM per second
    RAMPER_V1 = velocity_rpm_to_internal(400)
    RAMPER_A1 = acceleration_rpms_to_internal(500)  # Acceleration 500 RPM per second
    RAMPER_D1 = acceleration_rpms_to_internal(500)  # Deceleration 500 RPM per second

for var_name, var_value in dict(vars()).items():
    if not var_name.startswith("_") and not isinstance(var_value, Callable):
        print(f"{var_name}: {var_value}")