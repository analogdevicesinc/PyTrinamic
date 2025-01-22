################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to use TMC5241-EVAL."""

import time

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC5241
from pytrinamic.evalboards import TMC5241_eval


with ConnectionManager().connect() as my_interface:

    tmc5241_eval = TMC5241_eval(my_interface)

    # Set the minimal ramp parameters
    tmc5241_eval.write(TMC5241.REGMAP.AMAX, 100)
    tmc5241_eval.write(TMC5241.REGMAP.DMAX, 100)

    # Set the ramp mode to velocity mode
    tmc5241_eval.write(TMC5241.REGMAP.RAMPMODE.RAMPMODE.choice["Velocity mode (target +VMAX)"])

    # Start the motor - setting the target velocity to 51200 steps/s
    tmc5241_eval.write(TMC5241.REGMAP.VMAX, 51200)
    time.sleep(4)
    # Stop the motor
    tmc5241_eval.write(TMC5241.REGMAP.VMAX, 0)
    time.sleep(1)

