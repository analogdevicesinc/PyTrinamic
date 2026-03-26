################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""PI coefficient conversion for the velocity control loop.

If you found good PI values for your application with "ABN encoder count" feedback,
you can use this script to calculate the corresponding register values, even for different feedback selections.
"""

from typing import Literal


# Select the FOC feedback
commutation_feedback_select: Literal["ABN encoder", "Digital hall"] = "ABN encoder"

# Select the velocity feedback
# Ideally the "count" selection is used.
velocity_feedback_select: Literal["Same as commutation", "ABN encoder count", "Digital hall count"] = "ABN encoder count"

if commutation_feedback_select == "Digital hall" and velocity_feedback_select == "Same as commutation":
    print("This feedback combination is not recommended!") 


MOTOR_POLE_PAIRS = 4
ABN_COUNTS_PER_REVOLUTION = 4096

if velocity_feedback_select == "Same as commutation":
    velocity_scaling_factor = 2**40*MOTOR_POLE_PAIRS/40e6/60
elif velocity_feedback_select == "ABN encoder count":
    velocity_scaling_factor = 2**24*ABN_COUNTS_PER_REVOLUTION/40e6/60
elif velocity_feedback_select == "Digital hall count":
    velocity_scaling_factor = 2**24*6*MOTOR_POLE_PAIRS/40e6/60

# Note the first term is the `velocity_scaling_factor` in case `velocity_feedback_select == "ABN encoder count"`.
velocity_pid_rescaling_factor = (2**24*ABN_COUNTS_PER_REVOLUTION/40e6/60) / velocity_scaling_factor


def get_proper_norm_and_coeff(pid_value):
    shift_8x = 0
    for shift_8x in range(4):
        if pid_value*2**(8*(shift_8x + 1)) > 2**15:
            break        
    return shift_8x, int(pid_value*2**(8*(shift_8x)))


good_velocity_p_value = 100.0  # Reference: velocity_feedback_select == "ABN encoder count"; P: 100; Shift: 0
good_velocity_i_value = 0.0078125  # Reference: velocity_feedback_select == "ABN encoder count"; I: 2; Shift 8
if velocity_feedback_select == "Digital hall count" or (commutation_feedback_select == "Digital hall" and velocity_feedback_select == "Same as commutation"):
    # Reduce the PI values in case digital hall is used for velocity feedback,
    # because the digital hall resolution is too low for good velocity acquisition and control loop behavior.
    good_velocity_p_value /= 8
    good_velocity_i_value /= 8
velocity_p_norm, velocity_p_coeff = get_proper_norm_and_coeff(good_velocity_p_value*velocity_pid_rescaling_factor)
velocity_i_norm, velocity_i_coeff = get_proper_norm_and_coeff(good_velocity_i_value*velocity_pid_rescaling_factor)

print(f"velocity_p_norm: {velocity_p_norm}")
print(f"velocity_p_coeff: {velocity_p_coeff}")
print(f"velocity_i_norm: {velocity_i_norm}")
print(f"velocity_i_coeff: {velocity_i_coeff}")