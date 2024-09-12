###############################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import statistics
import time

from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC4671_eval, TMC6100_eval
from pytrinamic.ic import TMC6100


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
    tmc4671_eval.write(tmc4671_reg.PWM_SV_CHOP.PWM_CHOP.choice["centered PWM for FOC"])
    tmc4671_eval.write(tmc4671_reg.PWM_SV_CHOP.PWM_SV, 1)

    # ADC configuration
    tmc4671_eval.write(tmc4671_reg.ADC_I_SELECT, 0x24000100)  # This is actually the registers default value.
    tmc4671_eval.write(tmc4671_reg.dsADC_MCFG_B_MCFG_A, 0x00100010)
    tmc4671_eval.write(tmc4671_reg.dsADC_MCLK_A, 0x20000000)
    tmc4671_eval.write(tmc4671_reg.dsADC_MCLK_B, 0x00000000)
    tmc4671_eval.write(tmc4671_reg.dsADC_MDEC_B_MDEC_A, int(0x014E014E))

    # ADC scaling (1:1 scaling but inverted)
    tmc4671_eval.write(tmc4671_reg.ADC_I0_SCALE_OFFSET.ADC_I0_SCALE, -256)
    tmc4671_eval.write(tmc4671_reg.ADC_I1_SCALE_OFFSET.ADC_I1_SCALE, -256)

    # ADC offset compensation
    adc_i0_samples = []
    adc_i1_samples = []
    tmc4671_eval.write(tmc4671_reg.ADC_I0_SCALE_OFFSET.ADC_I0_OFFSET, 0)  # Reset offset for I0
    tmc4671_eval.write(tmc4671_reg.ADC_I1_SCALE_OFFSET.ADC_I1_OFFSET, 0)  # Reset offset for I1
    for _ in range(50):
        # Sample the raw ADC values to determine the offset error.
        raw_data_adc_i1_i0 = tmc4671_eval.read(tmc4671_reg.ADC_RAW_DATA)
        adc_i0_samples.append(tmc4671_reg.ADC_RAW_DATA.ADC_I0_RAW.get(raw_data_adc_i1_i0))
        adc_i1_samples.append(tmc4671_reg.ADC_RAW_DATA.ADC_I1_RAW.get(raw_data_adc_i1_i0))
    adc_i0_error = statistics.mean(adc_i0_samples)  # Calculate offset error for I0.
    adc_i1_error = statistics.mean(adc_i1_samples)  # Calculate offset error for I1.
    tmc4671_eval.write(tmc4671_reg.ADC_I0_SCALE_OFFSET.ADC_I0_OFFSET, int(adc_i0_error))  # Write I0 error into offset field for I0 offset compensation.
    tmc4671_eval.write(tmc4671_reg.ADC_I1_SCALE_OFFSET.ADC_I1_OFFSET, int(adc_i1_error))  # Write I1 error into offset field for I1 offset compensation.

    # Open loop settings
    tmc4671_eval.write(tmc4671_reg.OPENLOOP_MODE, 0)
    tmc4671_eval.write(tmc4671_reg.OPENLOOP_ACCELERATION, 100)

    # Feedback selection
    tmc4671_eval.write(tmc4671_reg.PHI_E_SELECTION.PHI_E_SELECTION.choice["phi_e_openloop"])
    tmc4671_eval.write(tmc4671_reg.UQ_UD_EXT, 2000)

    # ===== Open loop test drive =====

    # Switch to open loop velocity mode
    tmc4671_eval.write(tmc4671_reg.MODE_RAMP_MODE_MOTION.MODE_MOTION.choice["uq_ud_ext"])

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