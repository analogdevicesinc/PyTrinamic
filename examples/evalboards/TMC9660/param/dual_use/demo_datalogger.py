################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Demo on how to read and write flags.

Use the `connection_mode` to change the hardware connection.

#############################################################################################################
# connection_mode == with_landungsbruecke
#############################################################################################################
On Windows the config upload and app start can be done with:
    python ubltools_1.0.1/ubl_evalsystem_wrapper.py <COM-PORT> write config ubltools_1.0.1/ioconfig_tmc9660-3ph-eval.toml
    python ubltools_1.0.1/ubl_evalsystem_wrapper.py <COM-PORT> start
Where <COM-PORT> needs to be replaced by the COM port of the Landungsbruecke.

Important: first connect USB and then power the TMC9660-3PH-EVAL.

                            +-----+  +-------------------+     
                     USB    |     |==|                   |     
                     -------|     |==|                   |        
Connected to the machine    |     |==|                   |     
running this script.        |LB   |==|TMC9660-3PH-EVAL   |     
                            +-----+  +-------------------+
                   

#############################################################################################################
# connection_mode == headless
#############################################################################################################
On Windows the config upload and app start can be done with:
        ubltools_1.0.1/ublcli.exe --port <COM-PORT> write config ubltools_1.0.1/ioconfig_tmc9660-3ph-eval.toml
        ubltools_1.0.1/ublcli.exe --port <COM-PORT> start
Where <COM-PORT> needs to be replaced by the COM port of the USB-UART cable.

   --------+                       
           |  USB-UART Cable - Connected to the machine running this script.                                       
        +--|----------------+
        |  |                |
        |                   |
        |                   |
        |TMC9660-3PH-EVAL   |
        +-------------------+
"""

from typing import Literal

from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import TMC9660
from pytrinamic.evalboards import TMC9660_3PH_eval


# Select the connection mode
connection_mode: Literal["with_landungsbruecke", "headless"] = "with_landungsbruecke"
com_port_in_headless_mode = "COM5" # Note: Change this to the com port of the USB-UART cable used.


if connection_mode == "with_landungsbruecke":
    cm = ConnectionManager()
elif connection_mode == "headless":
    cm = ConnectionManager(f"--interface serial_tmcl --port {com_port_in_headless_mode}")

with cm.connect() as my_interface:

    if connection_mode == "with_landungsbruecke":
        tmc9660_device = TMC9660_3PH_eval(my_interface)
    elif connection_mode == "headless":
        tmc9660_device = TMC9660(my_interface)

    dl = tmc9660_device.datalogger
    print(dl.get_info())

    dl.config.samples_per_channel = 16
    dl.config.down_sampling_factor = 2
    dl.config.log_data = [
        TMC9660.ap.ADC_I0,
        TMC9660.ap.ADC_I1,
        TMC9660.ap.ADC_I2,
    ]

    dl.start_capture()

    dl.wait_for_capture_completion()

    dl.download_log()

    print(dl.log.data["ADC_I0"])
    print(dl.log.data["ADC_I1"])
    print(dl.log.data["ADC_I2"])

    print(f"Logged data sample rate: {dl.log.rate_hz} Hz")

    for name, log in dl.log.data.items():
        print(f"Log {name}:")
        print(f"  Samples: {log.samples}")
        print(f"  Parameter: {type(log.request_object)}")
