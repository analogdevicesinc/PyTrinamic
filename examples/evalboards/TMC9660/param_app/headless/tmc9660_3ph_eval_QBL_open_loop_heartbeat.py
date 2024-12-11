################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Demo on how global parameters are used.

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

    # Rotate the motor.
    tmc9660.set_axis_parameter(tmc9660.ap.TARGET_VELOCITY, 10_000)
    
    # Set the heartbeat monitoring timeout to 3s and enable it.
    tmc9660.set_global_parameter(tmc9660.gp_bank0.HEARTBEAT_MONITORING_TIMEOUT, 0, 3000)
    tmc9660.set_global_parameter(tmc9660.gp_bank0.HEARTBEAT_MONITORING_CONFIG.choice.TMCL_UART_INTERFACE, 0)
    
    # Initially all should be fine. The motor should be rotating.
    print(f"Actual velocity: {tmc9660.get_axis_parameter(tmc9660.ap.ACTUAL_VELOCITY)}")
    print(f"Commutation Mode: {tmc9660.get_axis_parameter(tmc9660.ap.COMMUTATION_MODE.choice).name}")
    print(f"HEARTBEAT_STOPPED: {bool(tmc9660.get_axis_parameter(tmc9660.ap.GENERAL_ERROR_FLAGS) & 0x04000000)}")

    time.sleep(4)

    # At this point the motor should have stopped due to the heartbeat timeout.
    # Meaning:
    # * velocity should be zero,
    # * commutation mode should be in SYSTEM_OFF,
    # * and the heartbeat error flag should be set.

    print(f"Actual velocity: {tmc9660.get_axis_parameter(tmc9660.ap.ACTUAL_VELOCITY)}")
    print(f"Commutation Mode: {tmc9660.get_axis_parameter(tmc9660.ap.COMMUTATION_MODE.choice).name}")
    print(f"HEARTBEAT_STOPPED: {bool(tmc9660.get_axis_parameter(tmc9660.ap.GENERAL_ERROR_FLAGS) & 0x04000000)}")

    tmc9660.set_global_parameter(tmc9660.gp_bank0.HEARTBEAT_MONITORING_CONFIG.choice.DISABLED, 0)
    tmc9660.set_axis_parameter(tmc9660.ap.GENERAL_ERROR_FLAGS, 0x04000000) # Clear heartbeat error flag, otherwise you cannot move the motor again.