################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC4671_eval
from pytrinamic.ic import TMC4671


with ConnectionManager().connect() as my_interface:

    mc_eval = TMC4671_eval(my_interface)

    ################################################################################################
    # Logging begin

    # Get a reference to the eval's DataLogger instance
    dl = mc_eval.datalogger
    # Configure the data to be logged
    dl.config.log_data = {
        "actual_velocity": dl.DataTypeRegister(block=0, channel=0, address=TMC4671.REG.PID_VELOCITY_ACTUAL),
        "actual_position": dl.DataTypeRegister(block=0, channel=0, address=TMC4671.REG.PID_POSITION_ACTUAL),
    }
    # Update the logging settings
    dl.config.down_sampling_factor = 2
    dl.config.samples_per_channel = 128
    # Start the logging
    dl.start_capture()
    # Wait for the logging to finish
    dl.wait_for_capture_completion()
    print("Logging done.")
    # Pull the data from the eval
    dl.download_log()
    # Access the logged data
    actual_velocity_samples = dl.log.data["actual_velocity"].samples
    actual_position_samples = dl.log.data["actual_position"].samples
    print(f"Actual velocity data: {actual_velocity_samples}")
    print(f"Actual position data: {actual_position_samples}")

    # Logging end
    ################################################################################################
