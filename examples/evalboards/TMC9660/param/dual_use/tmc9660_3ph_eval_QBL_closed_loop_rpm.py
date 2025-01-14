################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to use TMC9660-3PH-EVKIT to spin a BLDC motor with feedback.

It demonstrates the use of TMC9660 in velocity mode.
Velocity is given in RPM and the read velocity is returned in RPM as well.
To keep the example as simple as possible, we use only 4 point ramp mode.
This is what the actual velocity curve is supposed to look like.

                  target_velocity_rpm                                                     
                                  ----------------                                        
                                 /                \                                       
                                /                  \                                      
          acceleration_rpm_s   /                    \                                     
                              /                      \                                    
                             /                        \                                    
                          0 -                          ----------    

The required TMC-EvalSystem firmware is 3.10.7 or later.

Note: To run this script the TMC9660-3PH-EVAL first needs an uploaded/burned configuration
and the parameter app must have been started.
Note: With a change in feedback selection, the velocity PI regulator P and I parameters must be tuned again,
because of the change in internal scaling.

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
# Select the velocity feedback
velocity_feedback_select: Literal["Same as commutation", "ABN encoder", "Digital hall"] = "Same as commutation"

# Motor specification
motor_pole_pairs = 4

# Encoder specification
encoder_resolution = 4096

# Calculate the velocity scaling factor
kv_same = (2**16*motor_pole_pairs)*2**24/40e6/60
kv_abn = (encoder_resolution)*2**24/40e6/60
kv_hall = (6*motor_pole_pairs)*2**24/40e6/60


class TimeoutTimer:
    def __init__(self, timeout_in_seconds):
        self._start = time.time()
        self._timeout_in_seconds = timeout_in_seconds

    def has_expired(self):
        return time.time() - self._start > self._timeout_in_seconds


@dataclass
class Sample:
    time: int
    actual_velocity_internal: int


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

    # Set the velocity controller parameters
    tmc9660_device.set_axis_parameter(TMC9660.ap.VELOCITY_NORM_P.choice.SHIFT_8_BIT)
    tmc9660_device.set_axis_parameter(TMC9660.ap.VELOCITY_P, 500)
    tmc9660_device.set_axis_parameter(TMC9660.ap.VELOCITY_I, 5000)

    # Set the ABN encoder parameters
    tmc9660_device.set_axis_parameter(TMC9660.ap.ABN_1_STEPS, 4096)

    # Set the hall sensor parameters
    tmc9660_device.set_axis_parameter(TMC9660.ap.HALL_INVERT_DIRECTION, 1)
    tmc9660_device.set_axis_parameter(TMC9660.ap.HALL_SECTOR_OFFSET.choice.DEG_240)

    if commutation_feedback_select == "ABN encoder":
        tmc9660_device.set_axis_parameter(TMC9660.ap.COMMUTATION_MODE.choice.FOC_ABN)
    elif commutation_feedback_select == "Digital hall":
        tmc9660_device.set_axis_parameter(TMC9660.ap.COMMUTATION_MODE.choice.FOC_HALL_SENSOR)
    
    if velocity_feedback_select == "Same as commutation":
        kv = kv_same
        tmc9660_device.set_axis_parameter(TMC9660.ap.VELOCITY_SENSOR_SELECTION.choice.SAME_AS_COMMUTATION)
    elif velocity_feedback_select == "ABN encoder":
        kv = kv_abn
        tmc9660_device.set_axis_parameter(TMC9660.ap.VELOCITY_SENSOR_SELECTION.choice.ABN1_ENCODER)
    elif velocity_feedback_select == "Digital hall":
        kv = kv_hall
        tmc9660_device.set_axis_parameter(TMC9660.ap.VELOCITY_SENSOR_SELECTION.choice.DIGITAL_HALL)

    # Calculate the acceleration scaling factor
    ka = kv*2**17/40e6
    print(f"kv: {kv}")
    print(f"ka: {ka}")

    target_velocity_rpm = 4000
    target_velocity_internal = int(target_velocity_rpm*kv)
    acceleration_rpm_s = 2000  # [rpm/s]
    acceleration_internal =  int(acceleration_rpm_s*ka)
    
    tmc9660_device.set_axis_parameter(TMC9660.ap.RAMP_ENABLE, 1)
    # Enable 4 point ramp mode by disabling 6/8 point ramp mode.
    tmc9660_device.set_axis_parameter(TMC9660.ap.RAMP_V1, 0)
    tmc9660_device.set_axis_parameter(TMC9660.ap.RAMP_V2, 0)
    # Set the 4 point ramp parameters
    tmc9660_device.set_axis_parameter(TMC9660.ap.RAMP_AMAX, acceleration_internal)
    tmc9660_device.set_axis_parameter(TMC9660.ap.RAMP_DMAX, acceleration_internal)
    tmc9660_device.set_axis_parameter(TMC9660.ap.RAMP_VMAX, target_velocity_internal)
    print(f"RAMP_AMAX/RAMP_DMAX: {acceleration_internal}")
    print(f"RAMP_VMAX: {target_velocity_internal}")
    
    # Rotate the motor and record the velocity.
    # And then stop the motor but record the velocity as well.
    samples: List[Sample] = []
    for target_velocity, timeout in [(target_velocity_internal, 4), (0, 3)]:
        tmc9660_device.set_axis_parameter(TMC9660.ap.TARGET_VELOCITY, target_velocity)
        timer = TimeoutTimer(timeout)
        while not timer.has_expired():
            samples.append(Sample(time.perf_counter(), tmc9660_device.get_axis_parameter(TMC9660.ap.ACTUAL_VELOCITY)))

    tmc9660_device.set_axis_parameter(TMC9660.ap.COMMUTATION_MODE.choice.SYSTEM_OFF)

# Plot the velocity curve
fig, ax = plt.subplots()
t = [sample.time-samples[0].time for sample in samples]
v = [sample.actual_velocity_internal/kv for sample in samples]
ax.plot(t, v, label="velocity")
ax.legend()
plt.show()
