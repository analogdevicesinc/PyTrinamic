################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import time
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC4671_eval
from pytrinamic.ic import TMC4671


with ConnectionManager().connect() as my_interface:

    mc_eval = TMC4671_eval(my_interface)

    # Rotate the motor
    mc_eval.write_register(TMC4671.REG.PID_VELOCITY_TARGET, 500)
    time.sleep(3)

    ################################################################################################
    # Logging begin

    # Get a reference to the eval's DataLogger instance
    dl = mc_eval.datalogger
    # Configure the data to be logged
    dl.config.log_data = {
        "actual_velocity": dl.DataTypeRegister(channel=0, address=TMC4671.REG.PID_VELOCITY_ACTUAL),
        "actual_position": dl.DataTypeRegister(channel=0, address=TMC4671.REG.PID_POSITION_ACTUAL),
    }
    # Update the logging settings
    dl.config.down_sampling_factor = 2
    dl.config.samples_per_channel = 128
    dl.config.trigger_type = dl.TriggerType.UNCONDITIONAL
    # Start the logging
    dl.activate_trigger()
    # Wait until the logging is triggered
    while not dl.got_triggered():
        pass
    print("Logging triggered.")
    # Wait for the logging to finish
    while not dl.is_done():
        pass
    print("Logging done.")
    # Pull the data from the eval
    dl.download_logs()
    # Access the logged data
    actual_velocity_samples = dl.log["actual_velocity"].samples
    actual_position_samples = dl.log["actual_position"].samples
    print(f"Actual velocity data: {actual_velocity_samples}")
    print(f"Actual position data: {actual_position_samples}")

    # Logging end
    ################################################################################################

    # Stop the motor
    mc_eval.write_register(TMC4671.REG.PID_VELOCITY_TARGET, 0)
    time.sleep(1)

    # Switch to stop mode
    mc_eval.write_register(TMC4671.REG.MODE_RAMP_MODE_MOTION, TMC4671.ENUM.MOTION_MODE_STOPPED)

