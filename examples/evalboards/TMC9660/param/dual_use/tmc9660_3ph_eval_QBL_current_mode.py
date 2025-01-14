################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to use TMC9660-3PH-EVKIT to turn a BLDC motor in open loop current mode.

Slowly turn the motor in open loop current mode, while recording the ADC values of the phase currents measurement ADCs.


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

# Motor specification
motor_pole_pairs = 4

# Encoder specification
encoder_resolution = 4096

# Current scaling factor
R_SHUNT_OHM = 0.003  # TMC9660-3PH-EVAL specific shunt resistor value
CSA_GAIN = 10
current_scaling_factor = int(1024*2.5*1000/(2**16-1)/CSA_GAIN/R_SHUNT_OHM)
adc_clipping_current_ampere = 2.5/CSA_GAIN/R_SHUNT_OHM
print(f"ADC clipping current: {adc_clipping_current_ampere:.3}A")  # The maximum current that can be measured by the ADCs


class TimeoutTimer:
    def __init__(self, timeout_in_seconds):
        self._start = time.time()
        self._timeout_in_seconds = timeout_in_seconds

    def has_expired(self):
        return time.time() - self._start > self._timeout_in_seconds


@dataclass
class Sample:
    time: int
    x: int


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

    # Set current related parameters
    tmc9660_device.set_axis_parameter(TMC9660.ap.CSA_GAIN_ADC_I0_TO_ADC_I2.choice.GAIN_10X)
    print(f"CURRENT_SCALING_FACTOR: {current_scaling_factor}")
    tmc9660_device.set_axis_parameter(TMC9660.ap.CURRENT_SCALING_FACTOR, current_scaling_factor)
    tmc9660_device.set_axis_parameter(TMC9660.ap.MAX_FLUX, 2000)
    tmc9660_device.set_axis_parameter(TMC9660.ap.OPENLOOP_CURRENT, 2000)
    tmc9660_device.set_axis_parameter(TMC9660.ap.COMMUTATION_MODE.choice.FOC_OPENLOOP_CURRENT_MODE)
    
    # Move the motor in open loop current mode, while recording the ADC values of the phase currents measurement ADCs.
    # Note that the ADC values are not the actual phase currents, but the raw ADC values!
    samples_i0: List[Sample] = []
    samples_i1: List[Sample] = []
    samples_i2: List[Sample] = []
    samples_current: List[Sample] = []
    for target_velocity, timeout in [(10000, 4), (0, 1)]:
        tmc9660_device.set_axis_parameter(TMC9660.ap.TARGET_VELOCITY, target_velocity)
        timer = TimeoutTimer(timeout)
        while not timer.has_expired():
            samples_i0.append(Sample(time.perf_counter(), tmc9660_device.get_axis_parameter(TMC9660.ap.ADC_I0)))
            samples_i1.append(Sample(time.perf_counter(), tmc9660_device.get_axis_parameter(TMC9660.ap.ADC_I1)))
            samples_i2.append(Sample(time.perf_counter(), tmc9660_device.get_axis_parameter(TMC9660.ap.ADC_I2)))
            samples_current.append(Sample(time.perf_counter(), tmc9660_device.get_axis_parameter(TMC9660.ap.ACTUAL_TOTAL_MOTOR_CURRENT)))

    # Remove power from the motor
    tmc9660_device.set_axis_parameter(TMC9660.ap.COMMUTATION_MODE.choice.SYSTEM_OFF)

# Plot the phase currents and the actual total motor current
fig, ax = plt.subplots()
for i, samples in enumerate([samples_i0, samples_i1, samples_i2]):
    t = [sample.time-samples[0].time for sample in samples]
    # We reusing the current_scaling_factor to scale the ADC values to the actual phase currents.
    phase_current_ma = [sample.x*current_scaling_factor/1024 for sample in samples]
    ax.plot(t, phase_current_ma, label=f"I{i}")
    ax.legend()
t = [sample.time-samples[0].time for sample in samples_current]
ax.plot(t, [sample.x for sample in samples_current], label=f"Current")
ax.legend()
plt.show()
