################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to use the RAMDebug mechanism to examine different filter settings for the velocity biquad filter.

Basically the step response of the filter is evaluated.

The required TMC-EvalSystem firmware is 3.10.7 or later.

TMC9660-3PH-EVAL is powered with +24V.

Note: To run this script the TMC9660-3PH-EVAL first needs an uploaded/burned configuration
and the register app must have been started.

Use the `connection_mode` to change the hardware connection.

#############################################################################################################
# connection_mode == with_landungsbruecke
#############################################################################################################
On Windows the config upload and app start can be done with:
    python ubltools_1.0.1/ubl_evalsystem_wrapper.py <COM-PORT> write config ubltools_1.0.1/ioconfig_tmc9660-3ph-eval.toml
    python ubltools_1.0.1/ubl_evalsystem_wrapper.py <COM-PORT> start --mode reg
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
    ubltools_1.0.1/ublcli.exe --port <COM-PORT> start --mode reg
Where <COM-PORT> needs to be replaced by the COM port of the USB-UART cable.

   --------+
           | USB-UART Cable - Connected to the machine running this script.  
        +--|----------------+
        |  |                |
        |                   |
        |                   |
        |TMC9660-3PH-EVAL   |
        +-------------------+
"""

import time
from typing import Literal, Union
from dataclasses import dataclass

import matplotlib.pyplot as plt

from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import TMC9660
from pytrinamic.evalboards import TMC9660_3PH_eval
from pytrinamic.tools import calculate_biquad_filter_coefficients, LowPassFilterSpec


# Select the connection mode
connection_mode: Literal["with_landungsbruecke", "headless"] = "with_landungsbruecke"
com_port_in_headless_mode = "COM5" # Note: Change this to the com port of the USB-UART cable used.


@dataclass
class Setting:
    name: str
    filter_spec: LowPassFilterSpec


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

    tmc9660_device.write(TMC9660.MCC.VELOCITY_CONFIG.METER_TYPE.choice.VELOCITY_EXT)
    tmc9660_device.write(TMC9660.MCC.VELOCITY_EXT.VELOCITY_EXT, 0)
    time.sleep(1)

    settings = [
        Setting("LP1", LowPassFilterSpec(fc=1000)),
        Setting("LP2", LowPassFilterSpec(fc=1000, q=0.7071))
    ]

    fix, ax = plt.subplots()

    dl = tmc9660_device.datalogger

    for setting in settings:

        result = calculate_biquad_filter_coefficients(chip_type="TMC9660", filter_spec=setting.filter_spec)
        tmc9660_device.write(TMC9660.MCC.BIQUAD_V_A_1, result.normalized_coefficients.a_1)
        tmc9660_device.write(TMC9660.MCC.BIQUAD_V_A_2, result.normalized_coefficients.a_2)
        tmc9660_device.write(TMC9660.MCC.BIQUAD_V_B_0, result.normalized_coefficients.b_0)
        tmc9660_device.write(TMC9660.MCC.BIQUAD_V_B_1, result.normalized_coefficients.b_1)
        tmc9660_device.write(TMC9660.MCC.BIQUAD_V_B_2, result.normalized_coefficients.b_2)

        dl.config.samples_per_channel = 120
        dl.config.log_data = [
            TMC9660.MCC.PID_VELOCITY_ACTUAL.PID_VELOCITY_ACTUAL,
        ]
        dl.config.trigger.edge = dl.TriggerEdge.RISING
        dl.config.trigger.on_data = TMC9660.MCC.VELOCITY_EXT.VELOCITY_EXT
        dl.config.trigger.threshold = 1
        dl.config.trigger.pretrigger_samples_per_channel = 4

        dl.start_capture()

        tmc9660_device.write(TMC9660.MCC.VELOCITY_EXT.VELOCITY_EXT, 1000)

        dl.wait_for_capture_completion()

        tmc9660_device.write(TMC9660.MCC.VELOCITY_EXT.VELOCITY_EXT, 0)

        dl.download_log()

        # Plot the PID_VELOCITY_ACTUAL curve / the step response
        ax.plot(dl.log.time_vector, [x for x in dl.log.data["PID_VELOCITY_ACTUAL.PID_VELOCITY_ACTUAL"].samples] , label=f"PID_VELOCITY_ACTUAL {setting.name}")
        
        ax.legend()
        
    tmc9660_device.write(TMC9660.MCC.MOTION_CONFIG.MOTION_MODE.choice.STOPPED)
    plt.show()