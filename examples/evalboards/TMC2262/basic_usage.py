################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to use TMC2262-EVAL."""

import time

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC2262
from pytrinamic.evalboards import TMC2262_eval


with ConnectionManager().connect() as my_interface:

    tmc2262_eval = TMC2262_eval(my_interface)
    motor = tmc2262_eval.motors[0]

    # Reduce the current
    tmc2262_eval.write(TMC2262.REGMAP.IHOLD_IRUN.IHOLD, 10)
    tmc2262_eval.write(TMC2262.REGMAP.IHOLD_IRUN.IRUN, 64)

    # Let the Landungsbruecke generate some STEP pulses
    # Set the STEP pulses acceleration and deceleration to 20,000 steps/s^2
    motor.set_axis_parameter(motor.AP.MaxAcceleration, 20_000)

    # Now let the STEP pulses ramp up to the a target velocity of 51200 steps/s which is 1 round per second for a 200 steps/rev motor
    motor.set_target_velocity(51200)
    time.sleep(5)

    # Now stop the motor - ramp down to 0 steps/s
    motor.set_target_velocity(0)
    time.sleep(1)