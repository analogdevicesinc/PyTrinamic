################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Demo on how to read all parameters that could be stored non-volatile.

The script outputs a comma separated list for each axis parameter like this:

    MOTOR_TYPE                                    ;   0; 0
    MOTOR_POLE_PAIRS                              ;   1; 1
    MOTOR_DIRECTION                               ;   2; 0
    MOTOR_PWM_FREQUENCY                           ;   3; 25000
    OUTPUT_VOLTAGE_LIMIT                          ;   5; 8000
    MAX_TORQUE                                    ;   6; 2000
    ...
    ...
    ACTUAL_VELOCITY_BIQUAD_FILTER_BCOEFF_1        ; 328; 7329
    ACTUAL_VELOCITY_BIQUAD_FILTER_BCOEFF_2        ; 329; 3665

The script can easily be modified to create a different formatted output.
    
Use the `connection_mode` to change the hardware connection.

#############################################################################################################
# connection_mode == with_landungsbruecke
#############################################################################################################
On Windows the config upload and app start can be done with:
    python ubltools_1.0.1/ubl_evalsystem_wrapper.py <COM-PORT> write config ubltools_1.0.1/ioconfig_tmc9660-3ph-eval.toml
    python ubltools_1.0.1/ubl_evalsystem_wrapper.py <COM-PORT> start
Where <COM-PORT> needs to be replaced by the COM port of the Landungsbruecke.

Important: first connect USB and then power the TMC9660-3PH-EVAL.

                            +-----+  +-------------------+     
                     USB    |     |==|                   |     
                     -------|     |==|                   |        
Connected to the machine    |     |==|                   |     
running this script.        |LB   |==|TMC9660-3PH-EVAL   |     
                            +-----+  +-------------------+
                   

#############################################################################################################
# connection_mode == headless
#############################################################################################################
On Windows the config upload and app start can be done with:
        ubltools_1.0.1/ublcli.exe --port <COM-PORT> write config ubltools_1.0.1/ioconfig_tmc9660-3ph-eval.toml
        ubltools_1.0.1/ublcli.exe --port <COM-PORT> start
Where <COM-PORT> needs to be replaced by the COM port of the USB-UART cable.

   --------+                       
           |  USB-UART Cable - Connected to the machine running this script.                                       
        +--|----------------+
        |  |                |
        |                   |
        |                   |
        |TMC9660-3PH-EVAL   |
        +-------------------+
"""
import inspect
from typing import Literal, Union

from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import TMC9660
from pytrinamic.evalboards import TMC9660_3PH_eval
from pytrinamic.modules import Parameter
from pytrinamic.tmcl import TMCLReplyStatusError

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

    all_parameters = [member for _, member in inspect.getmembers(TMC9660.ap) if isinstance(member, Parameter)]

    # Maximum parameter name length we need to format the output nicely.
    max_name_len = max([len(parameter.name) for parameter in all_parameters])

    for parameter in sorted(all_parameters, key=lambda p: p.index):
        # Access.RWE stands for Read/Write/EEPROM - EEPROM is synonymous for: can be stored non-volatile.
        if parameter.access == Parameter.Access.RWE:
            try:
                value = tmc9660_device.get_parameter(parameter)
            except TMCLReplyStatusError:
                pass
            else:
                entry = f"{parameter.name:{max_name_len}}; {parameter.index:3}; {value}"
                print(entry)