#!/usr/bin/env python
################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################
"""
This example showcases the basic usage of the new datalogger interface.
It allows a more streamlined data acquisition based on mechanisms such as
RAMDebug.

Note that this interface is still in active development and may change by the
time the TMC6460 is fully released!
"""
from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import TMC6460
from pytrinamic.evalboards import TMC6460_eval

# # Uncomment these lines to enable logging of all communication
# import logging
# import sys
# logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

with ConnectionManager().connect() as my_interface:

    tmc6460_eval = TMC6460_eval(my_interface)

    dl = tmc6460_eval.datalogger

    ############################################################################
    print("Example 1: Capture without trigger")

    # Set up the datalogger to capture two channels
    dl.config.samples_per_channel = 10
    dl.config.log_data = [
        TMC6460.REGMAP.CHIP.ID,
        TMC6460.REGMAP.MCC_ADC.IW_IU.IU,
    ]

    # Start the capture without any trigger
    # This will immediately start capturing data
    dl.start_capture()

    # Wait until the data capture is completed
    dl.wait_for_capture_completion()

    # Download the capture data. Note that for bigger captures this can take
    # a few seconds
    dl.download_log()

    # Print the captured data
    print(dl.log.data["ID"].samples)
    print(dl.log.data["IW_IU.IU"].samples)
    print()

    ############################################################################
    print("Example 2: Capture with trigger")
    # Setting up the ramper to spin. We don't actually turn the motor, just
    # the internal ramp generator.
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.N_POLE_PAIRS, 4)
    tmc6460_eval.write(TMC6460.REGMAP.RAMPER.A_MAX.A_MAX, 25000)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_MODE.choice.RAMP_VELOCITY)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_EN, 1)
    tmc6460_eval.write(TMC6460.REGMAP.RAMPER.POSITION.POSITION, 0)
    tmc6460_eval.write(TMC6460.REGMAP.RAMPER.PHI_E.PHI_E_OFFSET, 0)

    # Set up the data logger to capture the ramper angle
    dl.config.samples_per_channel = 10
    dl.config.log_data = [
        TMC6460.REGMAP.RAMPER.PHI_E.PHI_E,
    ]

    # Configure the data logger with a configured trigger on the ramper angle
    # A trigger threshold of 0 and a rising edge trigger means we trigger
    # once the trigger value becomes greater than 0.
    dl.config.trigger.on_data = TMC6460.REGMAP.RAMPER.PHI_E.PHI_E
    dl.config.trigger.threshold = 0
    dl.config.trigger.edge = dl.TriggerEdge.RISING
    dl.config.trigger.pretrigger_samples_per_channel=5
    
    dl.start_capture()


    # Wait until the requested amount of pretrigger samples were captured
    dl.wait_for_pretrigger_completion()

    # At this point the measurement is waiting for the trigger to occur

    # Give the ramper a target velocity, causing it to start rotating the angle
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_VELOCITY_TARGET.PID_VELOCITY_TARGET, 100_000)

    # Wait for the capture to complete
    dl.wait_for_capture_completion()

    # Turn off the target value.
    # We suggest doing this before downloading - especially with larger captures
    # and a target value that actually energizes the system such as a current
    # step.
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_VELOCITY_TARGET.PID_VELOCITY_TARGET, 0)

    # Download the data
    dl.download_log()

    # Show the data
    print(dl.log.data["PHI_E.PHI_E"].samples)
