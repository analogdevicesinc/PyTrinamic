################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to use TMC9660-3PH-EVKIT.

Note: To run this script the TMC9660-3PH-EVAL first needs an uploaded/burned configuration
and the register app must have been started.

                            +-----+  +-------------------+
                     USB    |     |==|                   |
                     -------|     |==|                   |
Connected to the machine    |     |==|                   |
running this script.        |LB   |==|TMC9660-3PH-EVAL   |
                            +-----+  +-------------------+

"""

import time

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC9660
from pytrinamic.evalboards import TMC9660_3PH_eval


with ConnectionManager().connect() as my_interface:

    tmc9660_eval = TMC9660_3PH_eval(my_interface)

    tmc9660_eval.write(TMC9660.MCC.MOTOR_CONFIG.TYPE.choice.BLDC)
    tmc9660_eval.write(TMC9660.MCC.MOTOR_CONFIG.N_POLE_PAIRS, 4)

    for _ in range(20):
        print(f"I0 = {tmc9660_eval.read(TMC9660.MCC.ADC_I1_I0_SCALED.I0)}")
        print(f"I1 = {tmc9660_eval.read(TMC9660.MCC.ADC_I1_I0_SCALED.I1)}")
        print(f"I2 = {tmc9660_eval.read(TMC9660.MCC.ADC_I3_I2_SCALED.I2)}")
        time.sleep(0.2)
