################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to use TMC9660-3PH-EVKIT to spin a BLDC motor with feedback.

In this example the the motors torque is regulated.
Note that the actual current will be lower than the set current if the motor has no load on it.

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

#############################################################################################################
# connection_mode == headless
#############################################################################################################
On Windows the config upload and app start can be done with:
        ubltools_1.0.1/ublcli.exe --port <COM-PORT> write config ubltools_1.0.1/ioconfig_tmc9660-3ph-eval.toml
        ubltools_1.0.1/ublcli.exe --port <COM-PORT> start
Where <COM-PORT> needs to be replaced by the COM port of the USB-UART cable.

   --------+
           | USB-UART Cable - Connected to the machine running this script.  
        +--|----------------+       +---++--------------+             
        |  |                |-------|   ||              |             
        |                   |-------|   ||              |===             
        |                   |-------|ABN||BLDC QBL4208  |             
        |TMC9660-3PH-EVAL   |       +---++--------------+             
        +-------------------+         |   |                    
                      | |             |   | Digital hall feedback                   
                      | +-----------------+                    
                      |               | ABN encoder feedback                       
                      +---------------+        
"""
import time
from typing import Literal, List
from dataclasses import dataclass

import matplotlib.pyplot as plt

from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import TMC9660
from pytrinamic.evalboards import TMC9660_3PH_eval

# Select the connection mode
connection_mode: Literal["with_landungsbruecke", "headless"] = "with_landungsbruecke"
com_port_in_headless_mode = "COM5" # Note: Change this to the com port of the USB-UART cable used.

# Select the FOC feedback
commutation_feedback_select: Literal["ABN encoder", "Digital hall"] = "ABN encoder"

# Motor specification
motor_pole_pairs = 4

# Encoder specification
encoder_resolution = 4096

# Current scaling factor
R_SHUNT = 0.003
CSA_GAIN = 10
current_scaling_factor = int(1024*2.5*1000/(2**16-1)/CSA_GAIN/R_SHUNT)


class TimeoutTimer:
    def __init__(self, timeout_in_seconds):
        self._start = time.time()
        self._timeout_in_seconds = timeout_in_seconds

    def has_expired(self):
        return time.time() - self._start > self._timeout_in_seconds


@dataclass
class Sample:
    time: int
    actual_torque: int


if connection_mode == "with_landungsbruecke":
    cm = ConnectionManager()
elif connection_mode == "headless":
    cm = ConnectionManager(f"--interface serial_tmcl --port {com_port_in_headless_mode}")

with cm.connect() as my_interface:

    if connection_mode == "with_landungsbruecke":
        tmc9660_device = TMC9660_3PH_eval(my_interface)
    elif connection_mode == "headless":
        tmc9660_device = TMC9660(my_interface)

    # Set the commutation mode to system off - in case it was on before
    tmc9660_device.set_axis_parameter(TMC9660.ap.COMMUTATION_MODE.choice.SYSTEM_OFF)

    # Increase the output voltage limit
    tmc9660_device.set_axis_parameter(TMC9660.ap.OUTPUT_VOLTAGE_LIMIT, 16000)

    # Set the motor parameters
    tmc9660_device.set_axis_parameter(TMC9660.ap.MOTOR_TYPE.choice.BLDC_MOTOR)
    tmc9660_device.set_axis_parameter(TMC9660.ap.MOTOR_POLE_PAIRS, 4)

    # Set the ABN encoder parameters
    tmc9660_device.set_axis_parameter(TMC9660.ap.ABN_1_STEPS, 4096)
    tmc9660_device.set_axis_parameter(TMC9660.ap.ABN_1_INIT_METHOD.choice.USE_HALL)

    # Set the hall sensor parameters
    tmc9660_device.set_axis_parameter(TMC9660.ap.HALL_INVERT_DIRECTION, 1)
    tmc9660_device.set_axis_parameter(TMC9660.ap.HALL_SECTOR_OFFSET.choice.DEG_240)

    # Set current related parameters
    tmc9660_device.set_axis_parameter(TMC9660.ap.CSA_GAIN_ADC_I0_TO_ADC_I2.choice.GAIN_10X)
    tmc9660_device.set_axis_parameter(TMC9660.ap.CURRENT_SCALING_FACTOR, current_scaling_factor)

    if commutation_feedback_select == "ABN encoder":
        tmc9660_device.set_axis_parameter(TMC9660.ap.COMMUTATION_MODE.choice.FOC_ABN)
    elif commutation_feedback_select == "Digital hall":
        tmc9660_device.set_axis_parameter(TMC9660.ap.COMMUTATION_MODE.choice.FOC_HALL_SENSOR)
    
    torque_ma = 1200
    # Rotate the motor and record the torque.
    # And then stop the motor but record the torque as well.
    samples: List[Sample] = []
    for target_torque, timeout in [(torque_ma, 4), (0, 3)]:
        tmc9660_device.set_axis_parameter(TMC9660.ap.TARGET_TORQUE, target_torque)
        timer = TimeoutTimer(timeout)
        while not timer.has_expired():
            samples.append(Sample(time.perf_counter(), tmc9660_device.get_axis_parameter(TMC9660.ap.ACTUAL_TORQUE)))

    tmc9660_device.set_axis_parameter(TMC9660.ap.COMMUTATION_MODE.choice.SYSTEM_OFF)

# Plot the torque curve
fig, ax = plt.subplots()
t = [sample.time-samples[0].time for sample in samples]
v = [sample.actual_torque for sample in samples]
ax.plot(t, v, label="torque")
ax.legend()
plt.show()
