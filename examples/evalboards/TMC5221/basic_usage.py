################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################
"""Example on how to use TMC5221-EVAL."""

import time

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC5221
from pytrinamic.evalboards import TMC5221_eval


with ConnectionManager().connect() as my_interface:

    tmc5221_eval = TMC5221_eval(my_interface)

    # Set the minimal ramp parameters
    tmc5221_eval.write(TMC5221.REGMAP.RGR_AMAX, 100)
    tmc5221_eval.write(TMC5221.REGMAP.RGR_DMAX, 100)

    # Set the ramp mode to velocity mode
    tmc5221_eval.write(TMC5221.REGMAP.RGR_RAMPMODE.RAMPMODE.choice.VEL_POS)

    # Start the motor - setting the target velocity to 51200 steps/s
    tmc5221_eval.write(TMC5221.REGMAP.RGR_VMAX, 51200)
    time.sleep(4)
    # Stop the motor
    tmc5221_eval.write(TMC5221.REGMAP.RGR_VMAX, 0)
    time.sleep(1)