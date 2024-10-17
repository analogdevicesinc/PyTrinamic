################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Minimal example on how to use PyTrinamic with TMC9660-3PH-EVAL/TMC9660-STEPPER-EVAL.

The TMC9660-3PH-EVAL/TMC9660-STEPPER-EVAL is used in headless mode for this example.

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


with ConnectionManager("--interface serial_tmcl --port COM5").connect() as my_interface:

    tmc9660 = TMC9660(my_interface)

    for _ in range(10):
        voltage_v = tmc9660.get_axis_parameter(tmc9660.ap.SUPPLY_VOLTAGE) / 10
        print(f"Supply voltage: {voltage_v:.2f} V")
        time.sleep(0.2)
