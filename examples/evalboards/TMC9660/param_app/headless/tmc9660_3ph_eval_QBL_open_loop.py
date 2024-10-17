################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Demo on how to operate an TMC9660-3PH-EVAL.

The TMC9660-3PH-EVAL is used in headless mode for this example.

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


with ConnectionManager("--interface serial_tmcl --port COM5").connect() as my_interface:

    tmc9660 = TMC9660(my_interface)

    tmc9660.set_axis_parameter(tmc9660.ap.MOTOR_TYPE, tmc9660.ap.MOTOR_TYPE.choice.BLDC_MOTOR)
    tmc9660.set_axis_parameter(tmc9660.ap.OPENLOOP_VOLTAGE, 1000)
    tmc9660.set_axis_parameter(tmc9660.ap.COMMUTATION_MODE, tmc9660.ap.COMMUTATION_MODE.choice.FOC_OPENLOOP_VOLTAGE_MODE)

    tmc9660.set_axis_parameter(tmc9660.ap.VELOCITY_SCALING_FACTOR, 458)
    tmc9660.set_axis_parameter(tmc9660.ap.TARGET_VELOCITY, 20)
    
    start_time_s = time.time()
    while time.time() - start_time_s < 4:
        print(f"Actual velocity: {tmc9660.get_axis_parameter(tmc9660.ap.ACTUAL_VELOCITY)}")
        time.sleep(0.1)

    tmc9660.set_axis_parameter(tmc9660.ap.TARGET_VELOCITY, 0)
    time.sleep(0.1)
    tmc9660.set_axis_parameter(tmc9660.ap.COMMUTATION_MODE, tmc9660.ap.COMMUTATION_MODE.choice.SYSTEM_OFF)
