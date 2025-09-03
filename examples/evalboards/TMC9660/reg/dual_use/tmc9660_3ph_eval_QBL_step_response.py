################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to use the RAMDebug mechanism to create a current step response plot.

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
    ubltools_1.0.1/ublcli.exe --port <COM-PORT> start --mode reg
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
from typing import Literal, Union

import matplotlib.pyplot as plt

from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import TMC9660
from pytrinamic.evalboards import TMC9660_3PH_eval


# Select the connection mode
connection_mode: Literal["with_landungsbruecke", "headless"] = "with_landungsbruecke"
com_port_in_headless_mode = "COM5" # Note: Change this to the com port of the USB-UART cable used.

# Current scaling factor
R_SHUNT_OHM = 0.003  # TMC9660-3PH-EVAL specific shunt resistor value
CSA_GAIN = 10
current_scaling_factor = 2.5*1000/(2**16-1)/CSA_GAIN/R_SHUNT_OHM

target_current_ma = 2000  # 2000mA Open loop current


def current_internal_to_ma(internal_value):
    return internal_value * current_scaling_factor


def current_ma_to_internal(ma_value):
    return int(ma_value / current_scaling_factor)


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
    tmc9660_device.write(TMC9660.MCC.MOTOR_CONFIG.N_POLE_PAIRS, 4)
    tmc9660_device.write(TMC9660.MCC.MOTOR_CONFIG.TYPE.choice.BLDC)

    # Set limits
    tmc9660_device.write(TMC9660.MCC.PID_UQ_UD_LIMITS, 6000)
    tmc9660_device.write(TMC9660.MCC.PID_TORQUE_FLUX_LIMITS.PID_FLUX_LIMIT, current_ma_to_internal(target_current_ma*1.2))
    tmc9660_device.write(TMC9660.MCC.PID_TORQUE_FLUX_LIMITS.PID_TORQUE_LIMIT, current_ma_to_internal(target_current_ma*1.2))

    # Set PID coefficients
    tmc9660_device.write(TMC9660.MCC.PID_CONFIG.CURRENT_NORM_P.choice.SHIFT_8)
    tmc9660_device.write(TMC9660.MCC.PID_CONFIG.CURRENT_NORM_I.choice.SHIFT_16)
    tmc9660_device.write(TMC9660.MCC.PID_TORQUE_COEFF.P, 0)
    tmc9660_device.write(TMC9660.MCC.PID_TORQUE_COEFF.I, 0)

    # Configure phi_e source and motion mode
    tmc9660_device.write(TMC9660.MCC.PHI_E_SELECTION.PHI_E_SELECTION.choice.PHI_E_EXT)
    tmc9660_device.write(TMC9660.MCC.PHI_EXT.PHI_E_EXT, 0)
    tmc9660_device.write(TMC9660.MCC.MOTION_CONFIG.MOTION_MODE.choice.TORQUE)

    settings_a = {
        TMC9660.MCC.PID_FLUX_COEFF.P: 600,
        TMC9660.MCC.PID_FLUX_COEFF.I: 600,
    }
    settings_b = {
        TMC9660.MCC.PID_FLUX_COEFF.P: 50,
        TMC9660.MCC.PID_FLUX_COEFF.I: 100,
    }

    fig, (ax_a, ax_b) = plt.subplots(2, 1, layout="constrained")

    dl = tmc9660_device.datalogger

    for settings, ax in [(settings_b, ax_b), (settings_a, ax_a)]:
        for field, value in settings.items():
            tmc9660_device.write(field, value)

        dl.config.samples_per_channel = 256
        dl.config.log_data = [
            TMC9660.MCC.PID_TORQUE_FLUX_TARGET.PID_FLUX_TARGET,
            TMC9660.MCC.PID_TORQUE_FLUX_ACTUAL.PID_FLUX_ACTUAL,
        ]
        dl.config.trigger.edge = dl.TriggerEdge.RISING
        dl.config.trigger.on_data = TMC9660.MCC.PID_TORQUE_FLUX_TARGET.PID_FLUX_TARGET
        dl.config.trigger.threshold = current_ma_to_internal(target_current_ma//4)
        dl.config.trigger.pretrigger_samples_per_channel = 32

        dl.start_capture()

        # Apply flux
        tmc9660_device.write(TMC9660.MCC.PID_TORQUE_FLUX_TARGET.PID_FLUX_TARGET, current_ma_to_internal(target_current_ma))

        dl.wait_for_capture_completion()

        dl.download_log()

        tmc9660_device.write(TMC9660.MCC.PID_TORQUE_FLUX_TARGET.PID_FLUX_TARGET, 0)

        # Plot the current curve
        ax.plot(dl.log.time_vector, [current_internal_to_ma(x) for x in dl.log.data["PID_TORQUE_FLUX_TARGET.PID_FLUX_TARGET"].samples] , label="Target Current")
        ax.plot(dl.log.time_vector, [current_internal_to_ma(x) for x in dl.log.data["PID_TORQUE_FLUX_ACTUAL.PID_FLUX_ACTUAL"].samples] , label="Actual Current")
        ax.set_title(f"FLUX.P = {settings[TMC9660.MCC.PID_FLUX_COEFF.P]}; FLUX.I = {settings[TMC9660.MCC.PID_FLUX_COEFF.I]}")
        ax.legend()
        
    tmc9660_device.write(TMC9660.MCC.MOTION_CONFIG.MOTION_MODE.choice.STOPPED)
    plt.show()