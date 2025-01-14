################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Minimal example on how to use PyTrinamic with TMC9660-3PH-EVAL/TMC9660-STEPPER-EVAL.

The script will read the supply voltage ten times from the TMC9660 and print it to the console.

The TMC9660-3PH-EVAL/TMC9660-STEPPER-EVAL is used in headless mode for this example.

Note: To run this script the EVAL first needs an uploaded/burned configuration
and the parameter app must have been started.
On Windows this can be done with:
        ubltools_1.0.1/ublcli.exe --port <COM-PORT> write config ubltools_1.0.1/ioconfig_tmc9660-3ph-eval.toml
        ubltools_1.0.1/ublcli.exe --port <COM-PORT> start
Where <COM-PORT> needs to be replaced by the COM port of the USB-UART cable.

   --------+                       
           |  USB-UART Cable - Connected to the machine running this script.                                       
        +--|-----------------+
        |  |                 |
        |                    |
        |TMC9660-3PH-EVAL or |
        |TMC9660-STEPPER-EVAL|
        +--------------------+
"""

import time

from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import TMC9660


com_port = "COM5"  # Note: Change this to the com port of the USB-UART cable used.

with ConnectionManager(f"--interface serial_tmcl --port {com_port}").connect() as my_interface:

    tmc9660 = TMC9660(my_interface)

    for _ in range(10):
        voltage_v = tmc9660.get_axis_parameter(tmc9660.ap.SUPPLY_VOLTAGE) / 10
        print(f"Supply voltage: {voltage_v:.2f} V")
        time.sleep(0.2)
