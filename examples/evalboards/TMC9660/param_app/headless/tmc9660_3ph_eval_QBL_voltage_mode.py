################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Demo on how to operate an TMC9660-3PH-EVAL.

The TMC9660-3PH-EVAL is used in headless mode for this example.

Note: To run this script the TMC9660-3PH-EVAL first needs an uploaded/burned configuration
and the parameter app must have been started.
On Windows this can be done with:
        ubltools_1.0.1/ublcli.exe --port <COM-PORT> write config ubltools_1.0.1/ioconfig_tmc9660-3ph-eval.toml
        ubltools_1.0.1/ublcli.exe --port <COM-PORT> start
Where <COM-PORT> needs to be replaced by the COM port of the USB-UART cable.

   --------+                       
           |  USB-UART Cable - Connected to the machine running this script.                                       
        +--|----------------+       +--------------+             
        |  |                |-------|              |             
        |                   |-------|              |===             
        |                   |-------|BLDC QBL4208  |             
        |TMC9660-3PH-EVAL   |       +--------------+             
        +-------------------+                             
"""

import time

from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import TMC9660


com_port = "COM5"  # Note: Change this to the com port of the USB-UART cable used.

with ConnectionManager(f"--interface serial_tmcl --port {com_port}").connect() as my_interface:

    tmc9660 = TMC9660(my_interface)

    tmc9660.set_axis_parameter(tmc9660.ap.MOTOR_TYPE.choice.BLDC_MOTOR)
    tmc9660.set_axis_parameter(tmc9660.ap.OPENLOOP_VOLTAGE, 1000)
    tmc9660.set_axis_parameter(tmc9660.ap.COMMUTATION_MODE.choice.FOC_OPENLOOP_VOLTAGE_MODE)

    tmc9660.set_axis_parameter(tmc9660.ap.TARGET_VELOCITY, 10_000)
    
    start_time_s = time.time()
    while time.time() - start_time_s < 4:
        print(f"Actual velocity: {tmc9660.get_axis_parameter(tmc9660.ap.ACTUAL_VELOCITY)}")
        time.sleep(0.1)

    tmc9660.set_axis_parameter(tmc9660.ap.TARGET_VELOCITY, 0)
    time.sleep(0.1)
    tmc9660.set_axis_parameter(tmc9660.ap.COMMUTATION_MODE.choice.SYSTEM_OFF)
