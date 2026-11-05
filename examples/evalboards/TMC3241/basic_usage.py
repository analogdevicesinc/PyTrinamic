################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################
"""Example on how to use TMC3241-EVAL."""

import time

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC3241
from pytrinamic.evalboards import TMC3241_eval


F_CLK = 16_000_000  # 16 MHz external clock frequency provided by the Landungsbruecke

VEL_FACTOR = F_CLK / 2**24
ACC_FACTOR = F_CLK**2 / 2**41

with ConnectionManager().connect() as my_interface:
    tmc3241_eval = TMC3241_eval(my_interface)

    # Enable Motion Controller
    tmc3241_eval.write(TMC3241.REGMAP.GCONF.THREEPHASE_MCC, 1)

    # Example value for acceleration in steps/s^2
    acceleration_steps_per_s2 = 51200
    # Set the acceleration and deceleration for the two point velocity ramp
    tmc3241_eval.write(TMC3241.REGMAP.AMAX, round(acceleration_steps_per_s2 / ACC_FACTOR))
    tmc3241_eval.write(TMC3241.REGMAP.DMAX, round(acceleration_steps_per_s2 / ACC_FACTOR))

    # Set the ramp mode to velocity mode
    tmc3241_eval.write(TMC3241.REGMAP.RAMPMODE.RAMPMODE.choice.VEL_POS)

    # Start the motor - setting the target velocity to 51200 steps/s
    tmc3241_eval.write(TMC3241.REGMAP.VMAX, round(51200 / VEL_FACTOR))
    time.sleep(1)  # 1 second to reach the target velocity
    time.sleep(3)  # Maintain the target velocity for 3 seconds
    # Stop the motor
    tmc3241_eval.write(TMC3241.REGMAP.VMAX, 0)
    time.sleep(1)  # Wait for the motor to come to a complete stop
