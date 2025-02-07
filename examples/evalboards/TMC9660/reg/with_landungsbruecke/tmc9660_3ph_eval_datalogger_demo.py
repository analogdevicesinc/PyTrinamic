################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Demo on how to use the data-logging with TMC9660-3PH-EVKIT.

Note: To run this script the TMC9660-3PH-EVAL first needs an uploaded/burned configuration
and the register app must have been started.

                            +-----+  +-------------------+
                     USB    |     |==|                   |
                     -------|     |==|                   |
Connected to the machine    |     |==|                   |
running this script.        |LB   |==|TMC9660-3PH-EVAL   |
                            +-----+  +-------------------+

Expected output:
  DataLogger.Log(rate_hz=25000.0, samples=[-21, 43, -37, -29, -93, -45, -21, -61, 11, 11])
  DataLogger.Log(rate_hz=25000.0, samples=[51, -5, -21, 67, 51, 19, 59, -21, 27, 51])
  DataLogger.Log(rate_hz=25000.0, samples=[-9, -49, -65, -57, -81, -105, -25, -73, -105, -9])
"""

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC9660
from pytrinamic.evalboards import TMC9660_3PH_eval


with ConnectionManager().connect() as my_interface:

    tmc9660_eval = TMC9660_3PH_eval(my_interface)

    dl = tmc9660_eval.datalogger

    dl.config.samples_per_channel = 2
    dl.config.set_sample_rate(1250.0)
    dl.config.log_data = [
       TMC9660.MCC.ADC_I1_I0_SCALED.I0,
       TMC9660.MCC.ADC_I1_I0_SCALED.I1,
       TMC9660.MCC.ADC_I3_I2_SCALED.I2,
    ]
    

    dl.start_logging()

    dl.wait_till_done()

    dl.download_log()

    print(dl.log.data["ADC_I1_I0_SCALED.I0"])
    print(dl.log.data["ADC_I1_I0_SCALED.I1"])
    print(dl.log.data["ADC_I3_I2_SCALED.I2"])
