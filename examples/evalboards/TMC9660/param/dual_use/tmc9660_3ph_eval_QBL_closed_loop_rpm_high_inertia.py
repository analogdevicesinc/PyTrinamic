################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to use TMC9660-3PH-EVKIT to spin a BLDC motor and use brake chopper to burn kinetic energy during braking.

The brake chopper is basically used for over-voltage protection of the power supply.

The script records the curve of the supply voltage during the braking, as well as the brake chopper active flag.
Note that in cases where the brake chopper is active only for short amount of times, the brake chopper active flag is barely caught active.

A brass cylinder with a moment of inertia of 4500g*cm² is attached to the motor shaft.
The brass cylinder has a diameter of about 60mm and a length of 42mm, at a weight of 1kg.

J = m * R² / 2 = 1000g * (3cm)² / 2 = 4500g*cm²

A 100Ohm / 10W brake chopper load resistor is used.

      V ▲                                                                  
        │                                                                  
        │                                                                  
    BRAKE_CHOPPER_VOLTAGE_LIMIT                                            
   ───────────────────────────────────██────────██───────██───────────     
  ▲ │   │                           ███ ██     ████     ████               
  | │   │                          ██    █   ██   ██   ██  ██              
  | ▼ BRAKE_CHOPPER_HYSTERESIS    ██     █████     ████     ██             
  |  ────────────────────────────██──────────────────────────█────────     
  |     │                       ██                           █             
  |     │████████████████████████                            ████████████  supply_voltage
  |     │                       |◀──    brake phase     ──▶|                                       
  |     │                                                                      
  |     │                                                                  
        └──────────────────────────────────────────────────────────────────▶
                                                                          t
         
The required TMC-EvalSystem firmware is 3.10.7 or later.

The TMC9660-3PH-EVAL is supplied with 24V.

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

                            +-----+  +-------------------+       +---++--------------+ +--+            
                     USB    |     |==|                   |-------|   ||              | |  |          
                     -------|     |==|                   |-------|   ||              |=|  |           
Connected to the machine    |     |==|                   |-------|ABN||BLDC QBL4208  | |  |          
running this script.        |     |==|                   |       +---++--------------+ +--+       
                            |LB   |==|TMC9660-3PH-EVAL   |---R100  |   |              
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
        +--|----------------+       +---++--------------+ +--+        
        |  |                |-------|   ||              | |  |        
        |                   |-------|   ||              |=|  |           
        |                   |-------|ABN||BLDC QBL4208  | |  |        
        |                   |       +---++--------------+ +--+ 
        |TMC9660-3PH-EVAL   |---R100  |   |    
        +-------------------+         |   |                    
                      | |             |   | Digital hall feedback                   
                      | +-----------------+                    
                      |               | ABN encoder feedback                       
                      +---------------+        
#############################################################################################################
# Notes
#############################################################################################################

The example uses an TMCS-28-5-1K ABN encoder.

Wiring:

  Motor                         ABN encoder                      Digital hall                     OVP resistor

| Cable Color | MOTOR |       | Cable Color | ENCODER1 |       | Cable Color | HALL SENSOR |     | BRAKE CHOPPER |
|-------------|-------|       |-------------|----------|       |-------------|-------------|     |---------------|
| Black       | U     |       | Red         | +5V      |       | Red         | +5V         |     | +VM           |
| Red         | V     |       | Black       | GND      |       | Black       | GND         |     | BRAKE CH      |
| Yellow      | W     |       | Withe       | A        |       | Blue        | U           |     
                              | Green       | B        |       | Green       | V           |     
                              | Yellow      | N        |       | Withe       | W           |     
"""
import time
from typing import Literal, List, Union
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

# Calculate the velocity scaling factor
kv = (encoder_resolution)*2**24/40e6/60
# Calculate the acceleration scaling factor
ka = kv*2**17/40e6


class TimeoutTimer:
    def __init__(self, timeout_in_seconds):
        self._start = time.time()
        self._timeout_in_seconds = timeout_in_seconds

    def has_expired(self):
        return time.time() - self._start > self._timeout_in_seconds


@dataclass
class Sample:
    time_stamp: float
    value: int


@dataclass
class Record:
    supply_voltage: Sample
    brake_chopper_active: Sample


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

    tmc9660_device.set_parameter(TMC9660.ap.COMMUTATION_MODE.choice.SYSTEM_OFF)

    # Adapt the over voltage protection to the actual supply voltage.
    bc_hysteresis = 5 # 0.5 Volts -> let the voltage bounce in this range
    bc_hysteresis_stop = 2 # 0.2 Volts -> bounce area should start at supply voltage plus this value
    supply_voltage = tmc9660_device.get_parameter(TMC9660.ap.SUPPLY_VOLTAGE)
    tmc9660_device.set_parameter(TMC9660.ap.BRAKE_CHOPPER_HYSTERESIS, bc_hysteresis)
    tmc9660_device.set_parameter(TMC9660.ap.BRAKE_CHOPPER_VOLTAGE_LIMIT, supply_voltage + bc_hysteresis + bc_hysteresis_stop)
    tmc9660_device.set_parameter(TMC9660.ap.BRAKE_CHOPPER_ENABLE.choice.ENABLED)

    # Set the commutation mode to system off - in case it was on before
    tmc9660_device.set_parameter(TMC9660.ap.COMMUTATION_MODE.choice.SYSTEM_OFF)

    # Increase the output voltage limit
    tmc9660_device.set_parameter(TMC9660.ap.OUTPUT_VOLTAGE_LIMIT, 16000)

    # Set the motor parameters
    tmc9660_device.set_parameter(TMC9660.ap.MOTOR_TYPE.choice.BLDC_MOTOR)
    tmc9660_device.set_parameter(TMC9660.ap.MOTOR_POLE_PAIRS, motor_pole_pairs)

    # Set the velocity controller parameters
    tmc9660_device.set_parameter(TMC9660.ap.VELOCITY_NORM_P.choice.NO_SHIFT)
    tmc9660_device.set_parameter(TMC9660.ap.VELOCITY_NORM_I.choice.SHIFT_8_BIT)
    tmc9660_device.set_parameter(TMC9660.ap.VELOCITY_P, 100)
    tmc9660_device.set_parameter(TMC9660.ap.VELOCITY_I, 2)

    # Set the ABN encoder parameters
    tmc9660_device.set_parameter(TMC9660.ap.ABN_1_STEPS, encoder_resolution)

    # Set the hall sensor parameters
    tmc9660_device.set_parameter(TMC9660.ap.HALL_INVERT_DIRECTION, 1)
    tmc9660_device.set_parameter(TMC9660.ap.HALL_SECTOR_OFFSET.choice.DEG_240)

    # Set current related parameters
    tmc9660_device.set_parameter(TMC9660.ap.CSA_GAIN_ADC_I0_TO_ADC_I2.choice.GAIN_10X)
    tmc9660_device.set_parameter(TMC9660.ap.CURRENT_SCALING_FACTOR, current_scaling_factor)

    # Use hall sensor as source for commutation
    # This is not ideal for smooth commutation but we circumvent issues with ABN init / ABN alignment.
    tmc9660_device.set_parameter(TMC9660.ap.COMMUTATION_MODE.choice.FOC_HALL_SENSOR)

    # For velocity feedback use ABN1, for this ABN init is not needed.
    tmc9660_device.set_parameter(TMC9660.ap.VELOCITY_SENSOR_SELECTION.choice.ABN1_ENCODER)

    target_velocity_rpm = 2000
    target_velocity_internal = int(target_velocity_rpm*kv)
    acceleration_rpm_s = 1000  # [rpm/s]
    acceleration_internal =  int(acceleration_rpm_s*ka)
    
    tmc9660_device.set_parameter(TMC9660.ap.RAMP_ENABLE, 1)
    # Enable 4 point ramp mode by disabling 6/8 point ramp mode.
    tmc9660_device.set_parameter(TMC9660.ap.RAMP_V1, 0)
    tmc9660_device.set_parameter(TMC9660.ap.RAMP_V2, 0)
    # Set the 4 point ramp parameters
    tmc9660_device.set_parameter(TMC9660.ap.RAMP_AMAX, acceleration_internal)
    tmc9660_device.set_parameter(TMC9660.ap.RAMP_DMAX, acceleration_internal)
    tmc9660_device.set_parameter(TMC9660.ap.RAMP_VMAX, target_velocity_internal)
    
    # Rotate the motor and then stop the motor.
    # During the deceleration (target_velocity == 0) sample the supply voltage and the BRAKE_CHOPPER_ACTIVE flag.
    samples: List[Record] = []
    start_time = time.perf_counter()
    for target_velocity, timeout in [(target_velocity_internal, 5), (0, 5)]:
        tmc9660_device.set_parameter(TMC9660.ap.TARGET_VELOCITY, target_velocity)
        timer = TimeoutTimer(timeout)
        while not timer.has_expired():
            if target_velocity == 0:
                supply_voltage = Sample(time.perf_counter(), tmc9660_device.get_parameter(TMC9660.ap.SUPPLY_VOLTAGE))
                brake_chopper_active = Sample(time.perf_counter(), TMC9660.ap.GENERAL_STATUS_FLAGS.BRAKE_CHOPPER_ACTIVE.get(tmc9660_device.get_parameter(TMC9660.ap.GENERAL_STATUS_FLAGS)))
                samples.append(Record(supply_voltage, brake_chopper_active))

    tmc9660_device.set_parameter(TMC9660.ap.COMMUTATION_MODE.choice.SYSTEM_OFF)

fig, (ax0, ax1) = plt.subplots(2)
t_sv = [record.supply_voltage.time_stamp - start_time for record in samples]
sv = [record.supply_voltage.value for record in samples]
ax0.plot(t_sv, sv, "r-", label="supply_voltage")
t_bca = [record.brake_chopper_active.time_stamp - start_time for record in samples]
bca = [record.brake_chopper_active.value*100 for record in samples]
ax1.plot(t_bca, bca, "b-", label="brake_chopper_active")
fig.legend()
plt.show()