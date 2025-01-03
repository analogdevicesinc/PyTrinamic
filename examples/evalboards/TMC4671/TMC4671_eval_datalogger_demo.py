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
    dl.log_data({
        "actual_velocity": dl.SignalTypeRegister(channel=0, address=TMC4671.REG.PID_VELOCITY_ACTUAL),
        "actual_position": dl.SignalTypeRegister(channel=0, address=TMC4671.REG.PID_POSITION_ACTUAL),
    })
    # Update the logging settings
    dl.down_sampling_factor = 2
    dl.samples_per_channel = 128
    dl.trigger_type = dl.TriggerType.TRIGGER_UNCONDITIONAL
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
    dl.download_data()
    # Access the logged data
    actual_velocity_data = dl.data["actual_velocity"]
    actual_position_data = dl.data["actual_position"]
    print(f"Actual velocity data: {actual_velocity_data}")
    print(f"Actual position data: {actual_position_data}")

    # Logging end
    ################################################################################################

    # Stop the motor
    mc_eval.write_register(TMC4671.REG.PID_VELOCITY_TARGET, 0)
    time.sleep(1)

    # Switch to stop mode
    mc_eval.write_register(TMC4671.REG.MODE_RAMP_MODE_MOTION, TMC4671.ENUM.MOTION_MODE_STOPPED)

