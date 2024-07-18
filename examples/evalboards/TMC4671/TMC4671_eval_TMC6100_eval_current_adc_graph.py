################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""
This code measures the phase currents and convert them to ampere reading
Note: There might be an offset compared to the actual reading and that can be compensated in
    io_raw_to_current_conversion() function
"""

import time
import dataclasses
import statistics
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC4671_eval, TMC6100_eval
from pytrinamic.ic import TMC4671, TMC6100
import matplotlib.pyplot as plt


@dataclasses.dataclass
class Sample:
    timestamp: float
    ADC_I0_RAW: int


def io_raw_to_current_conversion(mc_eval):

    adc_raw = mc_eval.read_register_field(TMC4671.FIELD.ADC_I0_RAW)
    sys_volt = 5  # system voltage is 5V
    bits = 16  # 16 bit ADC
    r_shunt = 0.003  # shunt resistance 3 milliohm
    volt_amp = (adc_raw * sys_volt) / ((2 ** bits) - 1)  # Amplified_Voltage output of AD8418
    volt = (volt_amp - 2.5) / 20  # AD8418_Offset=2.5 & Gain=20 , voltage before amplification
    current = volt / r_shunt  # Offset can be adjusted at this step
    return current


pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
    print(my_interface)

    # Create a TMC4671-EVAL and TMC6100-EVAL which communicates over the Landungsbrücke via TMCL
    mc_eval = TMC4671_eval(my_interface)
    drv_eval = TMC6100_eval(my_interface)
    motor = mc_eval.motors[0]
    # Convert ADC_I0_RAW value to the corresponding current

    # Configure TMC6100 pwm for use with TMC4671 (disable singleline)
    drv_eval.write_register_field(TMC6100.FIELD.SINGLELINE, 0)

    # Configure TMC4671 for a BLDC motor in open loop mode

    # Motor type & PWM configuration
    mc_eval.write_register_field(TMC4671.FIELD.MOTOR_TYPE, TMC4671.ENUM.MOTOR_TYPE_BLDC)
    mc_eval.write_register_field(TMC4671.FIELD.N_POLE_PAIRS, 4)
    mc_eval.write_register(TMC4671.REG.PWM_POLARITIES, 0x00000000)
    mc_eval.write_register(TMC4671.REG.PWM_MAXCNT, int(0x00000F9F))
    mc_eval.write_register(TMC4671.REG.PWM_BBM_H_BBM_L, 0x00001414)
    mc_eval.write_register_field(TMC4671.FIELD.PWM_CHOP, TMC4671.ENUM.PWM_CENTERED_FOR_FOC)
    mc_eval.write_register_field(TMC4671.FIELD.PWM_SV, 1)

    # ADC configuration
    mc_eval.write_register(TMC4671.REG.ADC_I_SELECT, 0x24000100)
    mc_eval.write_register(TMC4671.REG.dsADC_MCFG_B_MCFG_A, 0x00100010)
    mc_eval.write_register(TMC4671.REG.dsADC_MCLK_A, 0x20000000)
    mc_eval.write_register(TMC4671.REG.dsADC_MCLK_B, 0x00000000)
    mc_eval.write_register(TMC4671.REG.dsADC_MDEC_B_MDEC_A, int(0x014E014E))
    # ADC offset compensation
    adc_i0_samples = []
    adc_i1_samples = []
    for _ in range(50):
        adc_i0_samples.append(mc_eval.read_register_field(TMC4671.FIELD.ADC_I0_RAW))
        adc_i1_samples.append(mc_eval.read_register_field(TMC4671.FIELD.ADC_I1_RAW))
    adc_i0_offset = statistics.mean(adc_i0_samples)
    adc_i1_offset = statistics.mean(adc_i1_samples)
    # Set scaling to -256 and apply the calculated offset
    mc_eval.write_register(TMC4671.REG.ADC_I0_SCALE_OFFSET, 0xFF000000 + int(adc_i0_offset))
    mc_eval.write_register(TMC4671.REG.ADC_I1_SCALE_OFFSET, 0xFF000000 + int(adc_i1_offset))

    # Open loop settings
    mc_eval.write_register(TMC4671.REG.OPENLOOP_MODE, 0x00000000)
    mc_eval.write_register(TMC4671.REG.OPENLOOP_ACCELERATION, 100)

    # Feedback selection
    mc_eval.write_register(TMC4671.REG.PHI_E_SELECTION, TMC4671.ENUM.PHI_E_OPEN_LOOP)
    mc_eval.write_register(TMC4671.REG.UQ_UD_EXT, 2000)

    # Switch to open loop velocity mode
    mc_eval.write_register(TMC4671.REG.MODE_RAMP_MODE_MOTION, TMC4671.ENUM.MOTION_MODE_UQ_UD_EXT)

    samples = []

    # Rotate right
    print("Rotate right...")
    mc_eval.write_register(TMC4671.REG.OPENLOOP_VELOCITY_TARGET, 5)
    start_time = time.time()
    while time.time() - start_time < 5:
        samples.append(Sample(time.perf_counter(), io_raw_to_current_conversion(mc_eval)))
    time.sleep(3)

    fig, ax = plt.subplots()
    t = [s.timestamp - samples[0].timestamp for s in samples]
    rawadc = [s.ADC_I0_RAW for s in samples]
    ax.set_xlabel('time(sec)')
    ax.set_ylabel('I(amps)')
    ax.plot(t, rawadc, label='Current(amps)')
    ax.legend()
    plt.show()

    # Stop
    print("Stop...")
    mc_eval.write_register(TMC4671.REG.OPENLOOP_VELOCITY_TARGET, 0)
    time.sleep(3)

    # Unpower
    print("Unpowered...")
    mc_eval.write_register(TMC4671.REG.UQ_UD_EXT, 0)

print("\nReady.")
