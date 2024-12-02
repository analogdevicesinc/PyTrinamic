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
    # Configure the signals to be logged
    dl.signals = {
        "actual_velocity": dl.SignalTypeRegister(address=TMC4671.REG.PID_VELOCITY_ACTUAL),
        "actual_position": dl.SignalTypeRegister(address=TMC4671.REG.PID_POSITION_ACTUAL),
    }
    # Update the logging settings
    dl.prescaler = 2
    dl.number_of_samples = 128
    dl.trigger_type = dl.TriggerType.TRIGGER_UNCONDITIONAL
    # Start the logging
    dl.start()
    # Wait for the logging to stop
    while not dl.has_stopped():
        pass
    # Access the logged signal
    actual_velocity_samples = dl.result["actual_velocity"]
    actual_position_samples = dl.result["actual_position"]

    # Logging end
    ################################################################################################

    # Stop the motor
    mc_eval.write_register(TMC4671.REG.PID_VELOCITY_TARGET, 0)
    time.sleep(1)

    # Switch to stop mode
    mc_eval.write_register(TMC4671.REG.MODE_RAMP_MODE_MOTION, TMC4671.ENUM.MOTION_MODE_STOPPED)

