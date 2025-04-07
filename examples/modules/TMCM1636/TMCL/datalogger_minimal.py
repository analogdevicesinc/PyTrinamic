################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import logging

from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1636


logging.basicConfig(level=logging.DEBUG)

connection_manager = ConnectionManager("--interface kvaser_tmcl")

with connection_manager.connect() as my_interface:
    module = TMCM1636(my_interface)
    motor = module.motors[0]

    # Add a shorter reference to the modules DataLogger.
    dl = module.datalogger

    # Configure
    dl.config.samples_per_channel = 10
    dl.config.log_data = {
        "ADC_I0": dl.DataTypeAp(index=motor.AP.AdcPhaseA),
    }

    # Do the logging logging immediately, without setting up any trigger condition.
    dl.start_capture()

    # Wait for the logging to finish
    dl.wait_for_capture_completion()

    # Pull the data from the module
    dl.download_log()

    # Access the logged data
    adc_i0 = dl.log.data["ADC_I0"]

    print(adc_i0.samples)
    print(dl.log.rate_hz)
