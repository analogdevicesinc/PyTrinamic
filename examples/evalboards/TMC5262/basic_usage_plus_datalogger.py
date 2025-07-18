################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to use TMC5262-EVAL while logging register data with the Landungsbruecke."""

import time

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC5262
from pytrinamic.evalboards import TMC5262_eval

from pytrinamic.datalogger import DataLogger

try:
    from matplotlib import pyplot as plt
except ImportError:
    print("Matplotlib is not installed. Skipping plotting functionality.")
    plt = None


with ConnectionManager().connect() as my_interface:

    tmc5262_eval = TMC5262_eval(my_interface)
    dl = DataLogger(my_interface)

    # Reduce the current
    tmc5262_eval.write(TMC5262.REGMAP.IHOLD_IRUN.IHOLD, 10)
    tmc5262_eval.write(TMC5262.REGMAP.IHOLD_IRUN.IRUN, 64)

    # Set the minimal ramp parameters
    tmc5262_eval.write(TMC5262.REGMAP.AMAX, 100)
    tmc5262_eval.write(TMC5262.REGMAP.DMAX, 100)

    # Set the ramp mode to velocity mode
    tmc5262_eval.write(TMC5262.REGMAP.RAMPMODE.RAMPMODE.choice['VEL_POS'])

    dl.config.samples_per_channel = 512
    dl.config.sample_rate_hz = 1000
    dl.config.log_data = [
        TMC5262.REGMAP.VACTUAL,
        TMC5262.REGMAP.XACTUAL,
    ]

    # Start the motor - setting the target velocity to 51200 steps/s
    dl.start_capture()
    tmc5262_eval.write(TMC5262.REGMAP.VMAX, 51200)
    dl.wait_for_capture_completion()
    # Stop the motor
    tmc5262_eval.write(TMC5262.REGMAP.VMAX, 0)
    time.sleep(1)

    dl.wait_for_capture_completion()
    dl.download_log()

    print(dl.log.data["VACTUAL"])
    print(dl.log.data["XACTUAL"])

    if plt:
        fix, (axis1, axis2) = plt.subplots(2, 1)
        axis1.plot(dl.log.time_vector, dl.log.data["VACTUAL"].samples, label="VACTUAL")
        axis2.plot(dl.log.time_vector, dl.log.data["XACTUAL"].samples, label="XACTUAL")
        for axis in (axis1, axis2):
            axis.grid()
            axis.set_xlabel("Time [s]")
            axis.legend()
        plt.show()