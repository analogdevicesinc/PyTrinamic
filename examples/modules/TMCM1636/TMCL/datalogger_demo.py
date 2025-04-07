################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import math

from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1636


connection_manager = ConnectionManager("--interface kvaser_tmcl")

with connection_manager.connect() as my_interface:
    module = TMCM1636(my_interface)
    motor = module.motors[0]

    # Create a shorter reference to the modules DataLogger.
    dl = module.datalogger

    dl_info = dl.get_info()  # This will read some information from the module.
    print(f"RAMdebug's base frequency is {dl_info.base_frequency_hz} Hz.")
    print(f"RAMdebug can sample up to {dl_info.number_of_channels} signals in parallel.")
    print(f"RAMdebug's total number of samples is {dl_info.sample_buffer_length}")
    for i in range(dl_info.number_of_channels):
        print(f"  If you sample {i+1} signal, you can have up to {math.floor(dl_info.sample_buffer_length/(i+1))} samples.")
    
    # Configure
    dl.config.log_data = {
        "actual_velocity": dl.DataTypeAp(motor.AP.ActualVelocity),
        "actual_position": dl.DataTypeAp(motor.AP.ActualPosition),
    }
    dl.config.down_sampling_factor = 2
    dl.config.samples_per_channel = 1024

    # Do the logging
    dl.start_capture()

    # Wait for the logging to finish
    dl.wait_for_capture_completion()

    # Pull the data from the module
    while dl.download_log_step():
        print(f"Download progress: {dl.download_progress:.2f}%")
    print(f"Download progress: {dl.download_progress:.2f}%")

    # Access the logged data
    actual_velocity = dl.log.data["actual_velocity"]
    actual_position = dl.log.data["actual_position"]
