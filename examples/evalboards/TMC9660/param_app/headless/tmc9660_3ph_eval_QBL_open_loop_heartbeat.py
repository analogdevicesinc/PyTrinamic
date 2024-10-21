################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Demo on how global parameters are used.

The TMC9660-3PH-EVAL is used in headless mode for this example.

Note: To run this script the TMC9660-3PH-EVAL first needs an uploaded/burned configuration
and the parameter app must have been started.

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
    
    tmc9660.set_global_parameter(tmc9660.gp_bank0.HEARTBEAT_MONITORING_TIMEOUT, 0, 3000)
    tmc9660.set_global_parameter(tmc9660.gp_bank0.HEARTBEAT_MONITORING_CONFIG, 0, tmc9660.gp_bank0.HEARTBEAT_MONITORING_CONFIG.choice.TMCL_UART_INTERFACE)
    
    print(f"Actual velocity: {tmc9660.get_axis_parameter(tmc9660.ap.ACTUAL_VELOCITY)}")
    print(f"Commutation Mode: {tmc9660.get_axis_parameter(tmc9660.ap.COMMUTATION_MODE)}")
    print(f"HEARTBEAT_STOPPED: {bool(tmc9660.get_axis_parameter(tmc9660.ap.GENERAL_ERROR_FLAGS) & 0x04000000)}")

    time.sleep(4)

    print(f"Actual velocity: {tmc9660.get_axis_parameter(tmc9660.ap.ACTUAL_VELOCITY)}")
    print(f"Commutation Mode: {tmc9660.get_axis_parameter(tmc9660.ap.COMMUTATION_MODE)}")
    print(f"HEARTBEAT_STOPPED: {bool(tmc9660.get_axis_parameter(tmc9660.ap.GENERAL_ERROR_FLAGS) & 0x04000000)}")

    tmc9660.set_global_parameter(tmc9660.gp_bank0.HEARTBEAT_MONITORING_CONFIG, 0, tmc9660.gp_bank0.HEARTBEAT_MONITORING_CONFIG.choice.DISABLED)
    tmc9660.set_axis_parameter(tmc9660.ap.GENERAL_ERROR_FLAGS, 0x04000000) # Clear heartbeat error flag, otherwise you cannot move the motor again.