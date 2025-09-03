################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to turn a motor in closed loop mode and where the velocity is controlled and ramped.

The example rotates the motor for some seconds while sampling the actual velocity for plotting.
Depending on the chosen `number_of_ramp_points` the actual velocity curve is supposed to look like this:

number_of_ramp_points = 4
                                                     
    RAMPER_V_TARGET ->              --------------  
                                   /              \                                      
                                  /                \                                       
                   RAMPER_A_MAX  /                  \  RAMPER_D_MAX                                    
                                /                    \                           
                               /                      \                                    
                              /                        \                                    
                          0 -/                          \----------   

#############################################################################################################
                          
number_of_ramp_points = 6
                                                                       
    RAMPER_V_TARGET ->                     -------  
                                          /       \                                      
                           RAMPER_A_MAX  /         \  RAMPER_D_MAX                                    
                                        /           \                                      
    RAMPER_V2 ->                     --/             \--                              
                       RAMPER_A2  --/                   \--  RAMPER_D2                                  
                               --/                         \--                                  
                          0 --/                               \----------   

#############################################################################################################
                        
number_of_ramp_points = 8

    RAMPER_V_TARGET ->                       -------  
                            RAMPER_A_MAX  --/       \--  RAMPER_D_MAX
    RAMPER_V1 ->                       --/             \--       
                           RAMPER_A2  /                   \  RAMPER_D2                                 
    RAMPER_V2 ->                     /                     \                                      
                       RAMPER_A1  --/                       \--  RAMPER_D1                           
                               --/                             \--                                     
                          0 --/                                   \----------   

#############################################################################################################

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
    ubltools_1.0.1/ublcli.exe --port <COM-PORT> start --mode reg
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

#############################################################################################################
# Notes
#############################################################################################################

The example uses an TMCS-28-5-1K ABN encoder.

Wiring:

  Motor                         ABN encoder                      Digital hall

| Cable Color | MOTOR |       | Cable Color | ENCODER1 |       | Cable Color | HALL SENSOR |
|-------------|-------|       |-------------|----------|       |-------------|-------------|
| Black       | U     |       | Red         | +5V      |       | Red         | +5V         |
| Red         | V     |       | Black       | GND      |       | Black       | GND         |
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

# Select the FOC feedback
commutation_feedback_select: Literal["ABN encoder", "Digital hall"] = "ABN encoder"

# Select the velocity feedback
# Idealy the "count" selection is used.
velocity_feedback_select: Literal["Same as commutation", "ABN encoder count", "Digital hall count"] = "ABN encoder count"

number_of_ramp_points: Literal[4, 6, 8] = 6

# Current scaling factor
R_SHUNT_OHM = 0.003  # TMC9660-3PH-EVAL specific shunt resistor value
CSA_GAIN = 10
current_scaling_factor = 2.5*1000/(2**16-1)/CSA_GAIN/R_SHUNT_OHM

MOTOR_POLE_PAIRS = 4
ABN_COUNTS_PER_REVOLUTION = 4096


if velocity_feedback_select == "Same as commutation":
    velocity_scaling_factor = 2**40*MOTOR_POLE_PAIRS/40e6/60
elif velocity_feedback_select == "ABN encoder count":
    velocity_scaling_factor = 2**24*ABN_COUNTS_PER_REVOLUTION/40e6/60
elif velocity_feedback_select == "Digital hall count":
    velocity_scaling_factor = 2**24*6*MOTOR_POLE_PAIRS/40e6/60

acceleration_scaling_factor = velocity_scaling_factor*2**17/40e6

target_velocity_rpm = 2000
current_limit_ma = 2000  # Closed loop maximum current in [mA]


def current_internal_to_ma(internal_value):
    return internal_value * current_scaling_factor


def current_ma_to_internal(ma_value):
    return int(ma_value / current_scaling_factor)


def velocity_internal_to_rpm(interal_value):
    return interal_value / velocity_scaling_factor


def velocity_rpm_to_internal(rpm_value):
    return int(rpm_value*velocity_scaling_factor)


def acceleration_rpms_to_internal(rpms_value):
    return int(rpms_value*acceleration_scaling_factor)


@dataclass
class Sample:
    time: float
    actual_velocity_rpm: int


class TimeoutTimer:
    def __init__(self, timeout_in_seconds):
        self._start = time.time()
        self._timeout_in_seconds = timeout_in_seconds

    def has_expired(self):
        return time.time() - self._start > self._timeout_in_seconds


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

    # Update the current shunt amplifier gain for phase U, V, W.
    tmc9660_device.write(TMC9660.ADC.CSA_SETUP.CSA012_GAIN.choice.CSA012_GAIN_x10)

    # PWM off
    tmc9660_device.write(TMC9660.MCC.PWM_CONFIG.CHOP, 0)

    # Enable bridges
    tmc9660_device.write(TMC9660.MCC.GDRV_HW.BRIDGE_ENABLE_U, 1)
    tmc9660_device.write(TMC9660.MCC.GDRV_HW.BRIDGE_ENABLE_V, 1)
    tmc9660_device.write(TMC9660.MCC.GDRV_HW.BRIDGE_ENABLE_W, 1)

    # Activate bias, charge pump and BST_SW_CP
    tmc9660_device.write(TMC9660.MCC.GDRV_HW.BIAS_EN, 1)
    tmc9660_device.write(TMC9660.MCC.GDRV_HW.CHARGEPUMP_EN, 1)
    tmc9660_device.write(TMC9660.MCC.GDRV_HW.BST_SW_CP_EN, 1)

    # Set gate driver currents and timings
    tmc9660_device.write(TMC9660.MCC.GDRV_CFG.IGATE_SINK_UVW.choice.SINK_270MA)
    tmc9660_device.write(TMC9660.MCC.GDRV_CFG.IGATE_SOURCE_UVW.choice.SOURCE_135MA)
    tmc9660_device.write(TMC9660.MCC.GDRV_CFG.ADAPTIVE_MODE_UVW, 1)
    tmc9660_device.write(TMC9660.MCC.GDRV_TIMING.T_DRIVE_SINK_UVW, 3)
    tmc9660_device.write(TMC9660.MCC.GDRV_TIMING.T_DRIVE_SOURCE_UVW, 3)
    tmc9660_device.write(TMC9660.MCC.GDRV_BBM, 0)
    
    # Set the PWM frequency and other PWM settings
    tmc9660_device.write(TMC9660.MCC.PWM_MAXCNT, 4799)  # Default for 25KHz
    tmc9660_device.write(TMC9660.MCC.PWM_CONFIG.SV_MODE.choice.BOTTOM_OFFSET)
    tmc9660_device.write(TMC9660.MCC.PWM_CONFIG.DUTY_CYCLE_OFFSET, 0)
    tmc9660_device.write(TMC9660.MCC.PWM_SWITCH_LIMIT, int(0xFFFF * 0.8)) # 80% of the max
    tmc9660_device.write(TMC9660.MCC.PWM_CONFIG.CHOP.choice.OFF_LSON)
    time.sleep(0.001) # Wait for bst caps to charge
    tmc9660_device.write(TMC9660.MCC.PWM_CONFIG.CHOP.choice.CENTERED)

    # Enable PWM channels
    tmc9660_device.write(TMC9660.MCC.PWM_CONFIG.ENABLE_UX1, 1)
    tmc9660_device.write(TMC9660.MCC.PWM_CONFIG.ENABLE_VX2, 1)
    tmc9660_device.write(TMC9660.MCC.PWM_CONFIG.ENABLE_WY1, 1)

    # Motor setting
    tmc9660_device.write(TMC9660.MCC.MOTOR_CONFIG.N_POLE_PAIRS, MOTOR_POLE_PAIRS)
    tmc9660_device.write(TMC9660.MCC.MOTOR_CONFIG.TYPE.choice.BLDC)

    # Set limits
    tmc9660_device.write(TMC9660.MCC.PID_UQ_UD_LIMITS, 20000) # Enough headroom
    tmc9660_device.write(TMC9660.MCC.PID_TORQUE_FLUX_LIMITS.PID_FLUX_LIMIT, current_ma_to_internal(current_limit_ma))
    tmc9660_device.write(TMC9660.MCC.PID_TORQUE_FLUX_LIMITS.PID_TORQUE_LIMIT, current_ma_to_internal(current_limit_ma))
    # Allow a little bit of overshoot for the velocity
    tmc9660_device.write(TMC9660.MCC.PID_VELOCITY_LIMIT, velocity_rpm_to_internal(target_velocity_rpm*1.2))

    # Set PID coefficients
    tmc9660_device.write(TMC9660.MCC.PID_CONFIG.CURRENT_NORM_P.choice.SHIFT_8)
    tmc9660_device.write(TMC9660.MCC.PID_CONFIG.CURRENT_NORM_I.choice.SHIFT_16)
    tmc9660_device.write(TMC9660.MCC.PID_TORQUE_COEFF.P, 600)
    tmc9660_device.write(TMC9660.MCC.PID_TORQUE_COEFF.I, 600)
    tmc9660_device.write(TMC9660.MCC.PID_FLUX_COEFF.P, 600)
    tmc9660_device.write(TMC9660.MCC.PID_FLUX_COEFF.I, 600)
    # Check out the tmc9660_3ph_eval_QBL_closed_loop_velocity_mode.py example for better velocity PI values depending on feeback selection.
    tmc9660_device.write(TMC9660.MCC.PID_CONFIG.VELOCITY_NORM_P.choice.SHIFT_0)
    tmc9660_device.write(TMC9660.MCC.PID_CONFIG.VELOCITY_NORM_I.choice.SHIFT_8)
    tmc9660_device.write(TMC9660.MCC.PID_VELOCITY_COEFF.P, 100)
    tmc9660_device.write(TMC9660.MCC.PID_VELOCITY_COEFF.I, 2)

    # Configure hall settings
    tmc9660_device.write(TMC9660.MCC.HALL_MODE.POLARITY.choice.NORMAL)
    tmc9660_device.write(TMC9660.MCC.HALL_MODE.ORDER.choice.VUW)

    # Configure ABN settings
    tmc9660_device.write(TMC9660.MCC.ABN_MODE.DIRECTION.choice.POS)
    tmc9660_device.write(TMC9660.MCC.ABN_CPR, ABN_COUNTS_PER_REVOLUTION)
    tmc9660_device.write(TMC9660.MCC.ABN_CPR_INV, 2**32//ABN_COUNTS_PER_REVOLUTION)
    # Take over hall phi_e for rough encoder alignment
    tmc9660_device.write(TMC9660.MCC.ABN_COUNT, 0)
    tmc9660_device.write(TMC9660.MCC.ABN_PHI_E_OFFSET, tmc9660_device.read(TMC9660.MCC.HALL_PHI_E_EXTRAPOLATED_PHI_E.PHI_E))

    # Configure phi_e source and motion mode
    if commutation_feedback_select == "ABN encoder":
        tmc9660_device.write(TMC9660.MCC.PHI_E_SELECTION.PHI_E_SELECTION.choice.PHI_E_ABN)
    elif commutation_feedback_select == "Digital hall":
        tmc9660_device.write(TMC9660.MCC.PHI_E_SELECTION.PHI_E_SELECTION.choice.PHI_E_HAL)

    if velocity_feedback_select == "Same as commutation":
        tmc9660_device.write(TMC9660.MCC.VELOCITY_CONFIG.SELECTION.choice.PHI_E)
    elif velocity_feedback_select == "ABN encoder count":
        tmc9660_device.write(TMC9660.MCC.VELOCITY_CONFIG.SELECTION.choice.ABN_COUNT)
    elif velocity_feedback_select == "Digital hall count":
        tmc9660_device.write(TMC9660.MCC.VELOCITY_CONFIG.SELECTION.choice.HALL_COUNT)
    
    # Configure the ramp generator
    tmc9660_device.write(TMC9660.MCC.MOTION_CONFIG.RAMP_ENABLE, 1)
    tmc9660_device.write(TMC9660.MCC.MOTION_CONFIG.RAMP_MODE.choice.VELOCITY)
    if number_of_ramp_points == 4:
        tmc9660_device.write(TMC9660.MCC.RAMPER_A_MAX, acceleration_rpms_to_internal(1000))  # Acceleration 1000 RPM per second
        tmc9660_device.write(TMC9660.MCC.RAMPER_D_MAX, acceleration_rpms_to_internal(1000))  # Deceleration 1000 RPM per second
        tmc9660_device.write(TMC9660.MCC.RAMPER_V2, 0)
        tmc9660_device.write(TMC9660.MCC.RAMPER_V1, 0)
    elif number_of_ramp_points == 6:
        tmc9660_device.write(TMC9660.MCC.RAMPER_A_MAX, acceleration_rpms_to_internal(1000))  # Acceleration 1000 RPM per second
        tmc9660_device.write(TMC9660.MCC.RAMPER_D_MAX, acceleration_rpms_to_internal(1000))  # Deceleration 1000 RPM per second
        tmc9660_device.write(TMC9660.MCC.RAMPER_V2, velocity_rpm_to_internal(1000))
        tmc9660_device.write(TMC9660.MCC.RAMPER_A2, acceleration_rpms_to_internal(500))  # Acceleration 500 RPM per second
        tmc9660_device.write(TMC9660.MCC.RAMPER_D2, acceleration_rpms_to_internal(500))  # Deceleration 500 RPM per second
        tmc9660_device.write(TMC9660.MCC.RAMPER_V1, velocity_rpm_to_internal(0))
    elif number_of_ramp_points == 8:
        tmc9660_device.write(TMC9660.MCC.RAMPER_A_MAX, acceleration_rpms_to_internal(500))  # Acceleration 500 RPM per second
        tmc9660_device.write(TMC9660.MCC.RAMPER_D_MAX, acceleration_rpms_to_internal(500))  # Deceleration 500 RPM per second
        tmc9660_device.write(TMC9660.MCC.RAMPER_V2, velocity_rpm_to_internal(1600))
        tmc9660_device.write(TMC9660.MCC.RAMPER_A2, acceleration_rpms_to_internal(1000))  # Acceleration 1000 RPM per second
        tmc9660_device.write(TMC9660.MCC.RAMPER_D2, acceleration_rpms_to_internal(1000))  # Deceleration 1000 RPM per second
        tmc9660_device.write(TMC9660.MCC.RAMPER_V1, velocity_rpm_to_internal(400))
        tmc9660_device.write(TMC9660.MCC.RAMPER_A1, acceleration_rpms_to_internal(500))  # Acceleration 500 RPM per second
        tmc9660_device.write(TMC9660.MCC.RAMPER_D1, acceleration_rpms_to_internal(500))  # Deceleration 500 RPM per second

    tmc9660_device.write(TMC9660.MCC.MOTION_CONFIG.MOTION_MODE.choice.VELOCITY)
    
    # Rotate the motor and record the velocity.
    # And then stop the motor but record the velocity as well.
    samples: List[Sample] = []
    for target_velocity, timeout in [(target_velocity_rpm, 4), (0, 3)]:
        tmc9660_device.write(TMC9660.MCC.RAMPER_V_TARGET, velocity_rpm_to_internal(target_velocity))
        timer = TimeoutTimer(timeout)
        while not timer.has_expired():
            samples.append(Sample(time.perf_counter(), velocity_internal_to_rpm(tmc9660_device.read(TMC9660.MCC.PID_VELOCITY_ACTUAL))))

    tmc9660_device.write(TMC9660.MCC.MOTION_CONFIG.MOTION_MODE.choice.STOPPED)

# Plot the velocity curve
fig, ax = plt.subplots()
t = [sample.time-samples[0].time for sample in samples]
v = [sample.actual_velocity_rpm for sample in samples]
ax.plot(t, v, label="velocity")
ax.legend()
plt.show()
