################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Demo on how global parameters are used.

The required TMC-EvalSystem firmware is 3.10.7 or later.

Note: To run this script the TMC9660-3PH-EVAL first needs an uploaded/burned configuration
and the parameter app must have been started.

Use the `connection_mode` to change the hardware connection.

#############################################################################################################
# connection_mode == with_landungsbruecke
#############################################################################################################
On Windows the config upload and app start can be done with:
    python ubltools_1.0.1/ubl_evalsystem_wrapper.py <COM-PORT> write config ubltools_1.0.1/ioconfig_tmc9660-3ph-eval.toml
    python ubltools_1.0.1/ubl_evalsystem_wrapper.py <COM-PORT> start
Where <COM-PORT> needs to be replaced by the COM port of the Landungsbruecke.

Important: first connect USB and then power the TMC9660-3PH-EVAL.

                            +-----+  +-------------------+       +--------------+             
                     USB    |     |==|                   |-------|              |             
                     -------|     |==|                   |-------|              |===             
Connected to the machine    |     |==|                   |-------|BLDC QBL4208  |             
running this script.        |LB   |==|TMC9660-3PH-EVAL   |       +--------------+             
                            +-----+  +-------------------+                         
                    

#############################################################################################################
# connection_mode == headless
#############################################################################################################
On Windows the config upload and app start can be done with:
        ubltools_1.0.1/ublcli.exe --port <COM-PORT> write config ubltools_1.0.1/ioconfig_tmc9660-3ph-eval.toml
        ubltools_1.0.1/ublcli.exe --port <COM-PORT> start
Where <COM-PORT> needs to be replaced by the COM port of the USB-UART cable.

   --------+
           | USB-UART Cable - Connected to the machine running this script.  
        +--|----------------+       +--------------+             
        |  |                |-------|              |             
        |                   |-------|              |===             
        |                   |-------|BLDC QBL4208  |             
        |TMC9660-3PH-EVAL   |       +--------------+             
        +-------------------+                  
                             
"""

from typing import Literal, Union
import time

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

    tmc9660_device: Union[TMC9660_3PH_eval, TMC9660]
    
    if connection_mode == "with_landungsbruecke":
        tmc9660_device = TMC9660_3PH_eval(my_interface)
    elif connection_mode == "headless":
        tmc9660_device = TMC9660(my_interface)

    tmc9660_device.set_parameter(TMC9660.ap.MOTOR_TYPE.choice.BLDC_MOTOR)
    tmc9660_device.set_parameter(TMC9660.ap.OPENLOOP_VOLTAGE, 1000)
    tmc9660_device.set_parameter(TMC9660.ap.COMMUTATION_MODE.choice.FOC_OPENLOOP_VOLTAGE_MODE)

    # Rotate the motor.
    tmc9660_device.set_parameter(TMC9660.ap.TARGET_VELOCITY, 10_000)
    
    # Set the heartbeat monitoring timeout to 3s and enable it.
    tmc9660_device.set_parameter(TMC9660.gp_bank0.HEARTBEAT_MONITORING_TIMEOUT, 3000)
    tmc9660_device.set_parameter(TMC9660.gp_bank0.HEARTBEAT_MONITORING_CONFIG.choice.TMCL_UART_INTERFACE)
    
    # Initially all should be fine. The motor should be rotating.
    print(f"Actual velocity: {tmc9660_device.get_parameter(TMC9660.ap.ACTUAL_VELOCITY)}")
    print(f"Commutation Mode: {TMC9660.ap.COMMUTATION_MODE.choice.get(tmc9660_device.get_parameter(TMC9660.ap.COMMUTATION_MODE)).name}")
    print(f"HEARTBEAT_STOPPED: {TMC9660.ap.GENERAL_ERROR_FLAGS.HEARTBEAT_STOPPED.get(tmc9660_device.get_parameter(TMC9660.ap.GENERAL_ERROR_FLAGS))}")

    time.sleep(4)

    # At this point the motor should have stopped due to the heartbeat timeout.
    # Meaning:
    # * velocity should be zero,
    # * commutation mode should be in SYSTEM_OFF,
    # * and the heartbeat error flag should be set.

    print(f"Actual velocity: {tmc9660_device.get_parameter(TMC9660.ap.ACTUAL_VELOCITY)}")
    print(f"Commutation Mode: {TMC9660.ap.COMMUTATION_MODE.choice.get(tmc9660_device.get_parameter(TMC9660.ap.COMMUTATION_MODE)).name}")
    print(f"HEARTBEAT_STOPPED: {TMC9660.ap.GENERAL_ERROR_FLAGS.HEARTBEAT_STOPPED.get(tmc9660_device.get_parameter(TMC9660.ap.GENERAL_ERROR_FLAGS))}")

    tmc9660_device.set_parameter(TMC9660.gp_bank0.HEARTBEAT_MONITORING_CONFIG.choice.DISABLED)
    tmc9660_device.set_parameter(TMC9660.ap.GENERAL_ERROR_FLAGS, 0x04000000) # Clear heartbeat error flag, otherwise you cannot move the motor again.