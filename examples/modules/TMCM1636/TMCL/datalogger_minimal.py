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

    # Do the logging - the default trigger is TRIGGER_UNCONDITIONAL which will start logging immediately
    dl.activate_trigger()

    # Wait for the logging to finish
    while not dl.is_done():
        pass

    # Pull the data from the module
    dl.download_logs()

    # Access the logged data
    adc_i0 = dl.logs["ADC_I0"]

    print(adc_i0.samples)
    print(adc_i0.rate_hz)



