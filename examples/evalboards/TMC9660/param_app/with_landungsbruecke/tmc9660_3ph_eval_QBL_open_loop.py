################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to use TMC9660-3PH-EVKIT to spin a BLDC motor in open loop voltage mode.

Note: To run this script the TMC9660-3PH-EVAL first needs an uploaded/burned configuration
and the the app must have been started.

                            +-----+  +-------------------+       +--------------+             
                     USB    |     |==|                   |-------|              |             
                     -------|     |==|                   |-------|              |===             
Connected to the machine    |     |==|                   |-------|BLDC QBL4208  |             
running this script.        |LB   |==|TMC9660-3PH-EVAL   |       +--------------+             
                            +-----+  +-------------------+                             

"""

import time

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC9660
from pytrinamic.evalboards import TMC9660_3PH_eval


with ConnectionManager().connect() as my_interface:

    tmc9660_eval = TMC9660_3PH_eval(my_interface)

    tmc9660_eval.set_axis_parameter(TMC9660.ap.MOTOR_TYPE, TMC9660.ap.MOTOR_TYPE.choice.BLDC_MOTOR)
    tmc9660_eval.set_axis_parameter(TMC9660.ap.OPENLOOP_VOLTAGE, 1000)
    tmc9660_eval.set_axis_parameter(TMC9660.ap.COMMUTATION_MODE, TMC9660.ap.COMMUTATION_MODE.choice.FOC_OPENLOOP_VOLTAGE_MODE)

    tmc9660_eval.set_axis_parameter(TMC9660.ap.VELOCITY_SCALING_FACTOR, 458)
    tmc9660_eval.set_axis_parameter(TMC9660.ap.TARGET_VELOCITY, 20)
    
    start_time_s = time.time()
    while time.time() - start_time_s < 4:
        print(f"Actual velocity: {tmc9660_eval.get_axis_parameter(TMC9660.ap.ACTUAL_VELOCITY)}")
        time.sleep(0.1)

    tmc9660_eval.set_axis_parameter(TMC9660.ap.TARGET_VELOCITY, 0)
    time.sleep(0.1)
    tmc9660_eval.set_axis_parameter(TMC9660.ap.COMMUTATION_MODE, TMC9660.ap.COMMUTATION_MODE.choice.SYSTEM_OFF)