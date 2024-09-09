###############################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import statistics
import time

from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC4671_eval, TMC6100_eval
from pytrinamic.ic import TMC6100

from pytrinamic.ic import TMC4671


with ConnectionManager().connect() as my_interface:
    tmc4671_eval = TMC4671_eval(my_interface)
    tmc6100_eval = TMC6100_eval(my_interface)

    tmc4671_reg = tmc4671_eval.ics[0].register

    # Configure TMC6100 pwm for use with TMC4671 (disable singleline)
    tmc6100_eval.write_register_field(TMC6100.FIELD.SINGLELINE, 0) # Still use the old API for this
    
    # Configure TMC4671 for a BLDC motor in open loop mode

    # Motor type & PWM configuration
    tmc4671_eval.write(tmc4671_reg.MOTOR_TYPE_N_POLE_PAIRS.MOTOR_TYPE, 3)
    tmc4671_eval.write(tmc4671_reg.MOTOR_TYPE_N_POLE_PAIRS.N_POLE_PAIRS, 4)
    tmc4671_eval.write(tmc4671_reg.PWM_POLARITIES, 0x00000000)
    tmc4671_eval.write(tmc4671_reg.PWM_MAXCNT, int(0x00000F9F))
    tmc4671_eval.write(tmc4671_reg.PWM_BBM_H_BBM_L, 0x00001414)
    tmc4671_eval.write(tmc4671_reg.PWM_SV_CHOP.PWM_CHOP, 7)
    tmc4671_eval.write(tmc4671_reg.PWM_SV_CHOP.PWM_SV, 1)

    # ADC configuration
    tmc4671_eval.write(tmc4671_reg.ADC_I_SELECT, 0x24000100)
    tmc4671_eval.write(tmc4671_reg.dsADC_MCFG_B_MCFG_A, 0x00100010)
    tmc4671_eval.write(tmc4671_reg.dsADC_MCLK_A, 0x20000000)
    tmc4671_eval.write(tmc4671_reg.dsADC_MCLK_B, 0x00000000)
    tmc4671_eval.write(tmc4671_reg.dsADC_MDEC_B_MDEC_A, int(0x014E014E))

    adc_i0_samples = []
    adc_i1_samples = []
    tmc4671_eval.write(tmc4671_reg.ADC_I0_SCALE_OFFSET, 0xFF000000)
    tmc4671_eval.write(tmc4671_reg.ADC_I1_SCALE_OFFSET, 0xFF000000)
    for _ in range(50):
        raw_data_adc_i1_i0 = tmc4671_eval.read(tmc4671_reg.ADC_RAW_DATA)
        adc_i0_sample = (raw_data_adc_i1_i0 & 0x0000FFFF) >> 0
        adc_i1_sample = (raw_data_adc_i1_i0 & 0xFFFF0000) >> 16
        adc_i0_samples.append(adc_i0_sample)
        adc_i1_samples.append(adc_i1_sample)
    adc_i0_offset = statistics.mean(adc_i0_samples)
    adc_i1_offset = statistics.mean(adc_i1_samples)
    tmc4671_eval.write(tmc4671_reg.ADC_I0_SCALE_OFFSET, 0xFF000000 + int(adc_i0_offset))
    tmc4671_eval.write(tmc4671_reg.ADC_I1_SCALE_OFFSET, 0xFF000000 + int(adc_i1_offset))


        # Open loop settings
    tmc4671_eval.write(tmc4671_reg.OPENLOOP_MODE, 0x00000000)
    tmc4671_eval.write(tmc4671_reg.OPENLOOP_ACCELERATION, 100)

    # Feedback selection
    tmc4671_eval.write(tmc4671_reg.PHI_E_SELECTION, 2)
    tmc4671_eval.write(tmc4671_reg.UQ_UD_EXT, 2000)

    # ===== Open loop test drive =====

    # Switch to open loop velocity mode
    tmc4671_eval.write(tmc4671_reg.MODE_RAMP_MODE_MOTION, 8)

    # Rotate right
    print("Rotate right...")
    tmc4671_eval.write(tmc4671_reg.OPENLOOP_VELOCITY_TARGET, 200)
    time.sleep(3)

    # Rotate left
    print("Rotate left...")
    tmc4671_eval.write(tmc4671_reg.OPENLOOP_VELOCITY_TARGET, -200)
    time.sleep(6)

    # Stop
    print("Stop...")
    tmc4671_eval.write(tmc4671_reg.OPENLOOP_VELOCITY_TARGET, 0)
    time.sleep(3)

    # Unpower
    print("Unpowered...")
    tmc4671_eval.write(tmc4671_reg.UQ_UD_EXT, 0)


print("\nReady.")