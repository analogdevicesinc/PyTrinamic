################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1636


connection_manager = ConnectionManager("--interface kvaser_tmcl")

with connection_manager.connect() as my_interface:
    module = TMCM1636(my_interface)
    motor = module.motors[0]

    # Add a shorter reference to the modules DataLogger.
    dl = module.datalogger

    dl_info = dl.get_info()  # This will read some information from the module.
    print(f"RAMdebug's base frequency is {dl_info.base_frequency_hz} Hz.")
    print(f"RAMdebug can sample up to {dl_info.number_of_channels} signals in parallel.")
    print(f"RAMdebug's total number of samples is {dl_info.sample_limit}")
    print(f"  If you sample 1 signal, you can have up to {dl_info.sample_limit} samples.")
    print(f"  If you sample 2 signals, you can have up to {dl_info.sample_limit // 2} samples.")
    
    # Configure
    dl.log_data({
        "actual_velocity": dl.SignalTypeAp(ap=motor.AP.ActualVelocity),
        "actual_position": dl.SignalTypeAp(ap=motor.AP.ActualPosition),
    })
    dl.down_sampling_factor = 2
    dl.samples_per_channel = 128
    dl.trigger_type = dl.TriggerType.TRIGGER_UNCONDITIONAL

    # Do the logging
    dl.activate_trigger()

    # Wait for the logging to finish
    while not dl.is_done():
        pass

    # Pull the data from the module
    dl.download_data()

    # Access the logged data
    actual_velocity = dl.data["actual_velocity"]
    actual_position = dl.data["actual_position"]



