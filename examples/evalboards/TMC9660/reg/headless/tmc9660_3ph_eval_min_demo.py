################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Minimal example on how to use PyTrinamic with TMC9660-3PH-EVAL/TMC9660-STEPPER-EVAL.

The TMC9660-3PH-EVAL/TMC9660-STEPPER-EVAL is used in headless mode for this example.

Note: To run this script the EVAL first needs an uploaded/burned configuration
and the register app must have been started.

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

    tmc9660.write(TMC9660.MCC.MOTOR_CONFIG.TYPE.choice.BLDC)
    tmc9660.write(TMC9660.MCC.MOTOR_CONFIG.N_POLE_PAIRS, 4)
    
    for _ in range(20):
        print(f"I0 = {tmc9660.read(TMC9660.MCC.ADC_I1_I0_SCALED.I0)}")
        print(f"I1 = {tmc9660.read(TMC9660.MCC.ADC_I1_I0_SCALED.I1)}")
        print(f"I2 = {tmc9660.read(TMC9660.MCC.ADC_I3_I2_SCALED.I2)}")
        time.sleep(0.2)
