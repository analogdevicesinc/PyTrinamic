################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to use TMC9660-3PH-EVKIT to spin a BLDC motor with feedback.

The required TMC-EvalSystem firmware is 3.10.7 or later.

Note: To run this script the TMC9660-3PH-EVAL first needs an uploaded/burned configuration
and the parameter app must have been started.
On Windows this can be done with:
    python ubltools_1.0.1/ubl_evalsystem_wrapper.py <COM-PORT> write config ubltools_1.0.1/ioconfig_tmc9660-3ph-eval.toml
    python ubltools_1.0.1/ubl_evalsystem_wrapper.py <COM-PORT> start
Where <COM-PORT> needs to be replaced by the COM port of the Landungsbruecke.

                            +-----+  +-------------------+       +---++--------------+             
                     USB    |     |==|                   |-------|   ||              |             
                     -------|     |==|                   |-------|   ||              |===             
Connected to the machine    |     |==|                   |-------|ABN||BLDC QBL4208  |             
running this script.        |LB   |==|TMC9660-3PH-EVAL   |       +---++--------------+             
                            +-----+  +-------------------+         |   |                    
                                                   | |             |   | Digital hall feedback                   
                                                   | +-----------------+                    
                                                   |               | ABN encoder feedback                       
                                                   +---------------+                      
"""

import time
from typing import Literal

from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import TMC9660
from pytrinamic.evalboards import TMC9660_3PH_eval


# Select the feedback type
feedback_select: Literal["ABN encoder", "Digital hall"] = "ABN encoder"

with ConnectionManager().connect() as my_interface:

    tmc9660_eval = TMC9660_3PH_eval(my_interface)

    tmc9660_eval.set_axis_parameter(TMC9660.ap.COMMUTATION_MODE.choice.SYSTEM_OFF)
    tmc9660_eval.set_axis_parameter(TMC9660.ap.MOTOR_TYPE.choice.BLDC_MOTOR)
    tmc9660_eval.set_axis_parameter(TMC9660.ap.MOTOR_POLE_PAIRS, 4)

    tmc9660_eval.set_axis_parameter(TMC9660.ap.VELOCITY_NORM_P.choice.SHIFT_8_BIT)
    tmc9660_eval.set_axis_parameter(TMC9660.ap.VELOCITY_P, 500)
    tmc9660_eval.set_axis_parameter(TMC9660.ap.VELOCITY_I, 5000)

    if feedback_select == "ABN encoder":
        tmc9660_eval.set_axis_parameter(TMC9660.ap.ABN_1_STEPS, 4096)
        tmc9660_eval.set_axis_parameter(TMC9660.ap.COMMUTATION_MODE.choice.FOC_ABN)
    elif feedback_select == "Digital hall":
        tmc9660_eval.set_axis_parameter(TMC9660.ap.HALL_INVERT_DIRECTION, 1)
        tmc9660_eval.set_axis_parameter(TMC9660.ap.HALL_SECTOR_OFFSET.choice.DEG_240)
        tmc9660_eval.set_axis_parameter(TMC9660.ap.COMMUTATION_MODE.choice.FOC_HALL_SENSOR)

    tmc9660_eval.set_axis_parameter(TMC9660.ap.TARGET_VELOCITY, 2_000_000)
    
    start_time_s = time.time()
    while time.time() - start_time_s < 4:
        print(f"Actual velocity: {tmc9660_eval.get_axis_parameter(TMC9660.ap.ACTUAL_VELOCITY)}")
        time.sleep(0.1)

    tmc9660_eval.set_axis_parameter(TMC9660.ap.TARGET_VELOCITY, 0)
    time.sleep(0.1)
    tmc9660_eval.set_axis_parameter(TMC9660.ap.COMMUTATION_MODE.choice.SYSTEM_OFF)
