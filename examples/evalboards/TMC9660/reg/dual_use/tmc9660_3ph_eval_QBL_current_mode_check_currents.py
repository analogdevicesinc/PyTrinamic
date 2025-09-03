################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to turn a motor in closed loop in torque controlled mode.

The example rotates the motor for 10 seconds.
The ramp generator is used to ramp up and down the velocity.

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
from dataclasses import dataclass
from typing import Literal, Union

from matplotlib import pyplot as plt

from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import TMC9660
from pytrinamic.evalboards import TMC9660_3PH_eval


# Select the connection mode
connection_mode: Literal["with_landungsbruecke", "headless"] = "with_landungsbruecke"
com_port_in_headless_mode = "COM5" # Note: Change this to the com port of the USB-UART cable used.

# Current scaling factor
R_SHUNT_OHM = 0.003  # TMC9660-3PH-EVAL specific shunt resistor value
CSA_GAIN: Literal[5, 10, 20, 40] = 10  # 10 is a good tradeoff
current_scaling_factor = 2.5*1000/(2**16-1)/CSA_GAIN/R_SHUNT_OHM
adc_clipping_current_ampere = 2.5/CSA_GAIN/R_SHUNT_OHM
print(f"ADC clipping current: {adc_clipping_current_ampere:.3}A")  # The maximum current that can be measured by the ADCs

velocity_scaling_factor = 2**40/40e6/60
acceleration_scaling_factor = velocity_scaling_factor*2**17/40e6

csa_gain_to_choice = {
    5: TMC9660.ADC.CSA_SETUP.CSA012_GAIN.choice.CSA012_GAIN_x5,
    10: TMC9660.ADC.CSA_SETUP.CSA012_GAIN.choice.CSA012_GAIN_x10,
    20: TMC9660.ADC.CSA_SETUP.CSA012_GAIN.choice.CSA012_GAIN_x20,
    40: TMC9660.ADC.CSA_SETUP.CSA012_GAIN.choice.CSA012_GAIN_x40,
}

target_current_ma = 2000  # 2000mA Open loop current


def current_internal_to_ma(internal_value):
    return internal_value * current_scaling_factor


def current_ma_to_internal(ma_value):
    return int(ma_value / current_scaling_factor)


def velocity_rpm_to_internal(rpm_value):
    return int(rpm_value*velocity_scaling_factor)


def acceleration_rpms_to_internal(rpms_value):
    return int(rpms_value*acceleration_scaling_factor)
    

@dataclass
class Phase:
    voltage_internal: int
    current_ma: float

@dataclass
class Sample:
    phase_u: Phase
    phase_v: Phase
    phase_w: Phase


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
    tmc9660_device.write(csa_gain_to_choice[CSA_GAIN])

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
    tmc9660_device.write(TMC9660.MCC.PID_VELOCITY_LIMIT, 2000000)

    # Set PID coefficients
    tmc9660_device.write(TMC9660.MCC.PID_CONFIG.CURRENT_NORM_P.choice.SHIFT_8)
    tmc9660_device.write(TMC9660.MCC.PID_CONFIG.CURRENT_NORM_I.choice.SHIFT_16)
    tmc9660_device.write(TMC9660.MCC.PID_TORQUE_COEFF.P, 600)
    tmc9660_device.write(TMC9660.MCC.PID_TORQUE_COEFF.I, 600)
    tmc9660_device.write(TMC9660.MCC.PID_FLUX_COEFF.P, 600)
    tmc9660_device.write(TMC9660.MCC.PID_FLUX_COEFF.I, 600)

    # Configure the ramp generator
    tmc9660_device.write(TMC9660.MCC.MOTION_CONFIG.RAMP_ENABLE, 1)
    tmc9660_device.write(TMC9660.MCC.MOTION_CONFIG.RAMP_MODE.choice.VELOCITY)
    tmc9660_device.write(TMC9660.MCC.RAMPER_A_MAX, acceleration_rpms_to_internal(60))  # Acceleration 60 RPM per second
    tmc9660_device.write(TMC9660.MCC.RAMPER_D_MAX, acceleration_rpms_to_internal(60))  # Deceleration 60 RPM per second

    # Configure phi_e source and motion mode
    tmc9660_device.write(TMC9660.MCC.PHI_E_SELECTION.PHI_E_SELECTION.choice.PHI_E_RAMP)
    tmc9660_device.write(TMC9660.MCC.MOTION_CONFIG.MOTION_MODE.choice.TORQUE)

    # Apply flux
    tmc9660_device.write(TMC9660.MCC.PID_TORQUE_FLUX_TARGET.PID_FLUX_TARGET, current_ma_to_internal(target_current_ma))

    # Do the velocity move
    tmc9660_device.write(TMC9660.MCC.RAMPER_V_TARGET, velocity_rpm_to_internal(60))

    samples = []
    start_time = time.time()
    while time.time() - start_time < 2:
        samples.append(Sample(
            phase_u=Phase(voltage_internal=tmc9660_device.read(TMC9660.MCC.FOC_UWY_UUX.UUX),
                          current_ma=current_internal_to_ma(tmc9660_device.read(TMC9660.MCC.ADC_IWY_IUX.IUX)),
            ),
            phase_v=Phase(voltage_internal=tmc9660_device.read(TMC9660.MCC.FOC_UWY_UUX.UWY),
                          current_ma=current_internal_to_ma(tmc9660_device.read(TMC9660.MCC.ADC_IWY_IUX.IWY)),
            ),
            phase_w=Phase(voltage_internal=tmc9660_device.read(TMC9660.MCC.FOC_UV.UV),
                          current_ma=current_internal_to_ma(tmc9660_device.read(TMC9660.MCC.ADC_IV.IV)),
            ),
        ))

    # Teardown/Stop
    tmc9660_device.write(TMC9660.MCC.RAMPER_V_TARGET, 0)
    time.sleep(1)
    tmc9660_device.write(TMC9660.MCC.PID_TORQUE_FLUX_TARGET.PID_FLUX_TARGET, 0)
    tmc9660_device.write(TMC9660.MCC.MOTION_CONFIG.MOTION_MODE.choice.STOPPED)

fig, axs = plt.subplots(3, 1, layout="constrained")
for ax, name in zip(axs, ["u", "v", "w"]):
    ax.plot([getattr(sample, f"phase_{name}").voltage_internal for sample in samples], "b-", label="Voltage[internal]")
    ax.set_title(f"Phase {name.upper()}")
    ax.set_ylabel("Voltage[internal]", color="b")
    ax.legend(loc="upper right")
    ax_sec = ax.twinx()
    ax_sec.plot([getattr(sample, f"phase_{name}").current_ma for sample in samples], "g-", label="Current[mA]")
    ax_sec.set_ylabel("Current[mA]", color="g")
    ax_sec.legend(loc="lower right")
plt.show()
