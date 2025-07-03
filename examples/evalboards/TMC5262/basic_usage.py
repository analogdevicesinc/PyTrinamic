################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to use TMC5262-EVAL."""

import time

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC5262
from pytrinamic.evalboards import TMC5262_eval


with ConnectionManager().connect() as my_interface:

    TMC5262_eval = TMC5262_eval(my_interface)

    # Reduce the current
    TMC5262_eval.write(TMC5262.REGMAP.IHOLD_IRUN.IHOLD, 10)
    TMC5262_eval.write(TMC5262.REGMAP.IHOLD_IRUN.IRUN, 64)

    # Set the minimal ramp parameters
    TMC5262_eval.write(TMC5262.REGMAP.AMAX, 100)
    TMC5262_eval.write(TMC5262.REGMAP.DMAX, 100)

    # Set the ramp mode to velocity mode
    TMC5262_eval.write(TMC5262.REGMAP.RAMPMODE.RAMPMODE.choice['VEL_POS'])

    # Start the motor - setting the target velocity to 51200 steps/s
    TMC5262_eval.write(TMC5262.REGMAP.VMAX, 51200)
    time.sleep(4)
    # Stop the motor
    TMC5262_eval.write(TMC5262.REGMAP.VMAX, 0)
    time.sleep(1)