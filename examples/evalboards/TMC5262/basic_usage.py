################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to use TMC5262-EVAL.

Please note that the Landungsbruecke firmware presets some registers on startup!
To actually operate a motor with the TMC5262, some more configuration might be necessary.
"""

import time

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC5262
from pytrinamic.evalboards import TMC5262_eval


with ConnectionManager().connect() as my_interface:
    tmc5262_eval = TMC5262_eval(my_interface)

    # Reduce the current
    tmc5262_eval.write(TMC5262.REGMAP.IHOLD_IRUN.IHOLD, 10)
    tmc5262_eval.write(TMC5262.REGMAP.IHOLD_IRUN.IRUN, 64)

    # Set the minimal ramp parameters
    tmc5262_eval.write(TMC5262.REGMAP.AMAX, 100)
    tmc5262_eval.write(TMC5262.REGMAP.DMAX, 100)

    # Set the ramp mode to velocity mode
    tmc5262_eval.write(TMC5262.REGMAP.RAMPMODE.RAMPMODE.choice.VEL_POS)

    # Start the motor - setting the target velocity to 51200 steps/s
    tmc5262_eval.write(TMC5262.REGMAP.VMAX, 51200)
    time.sleep(4)
    # Stop the motor
    tmc5262_eval.write(TMC5262.REGMAP.VMAX, 0)
    time.sleep(1)
