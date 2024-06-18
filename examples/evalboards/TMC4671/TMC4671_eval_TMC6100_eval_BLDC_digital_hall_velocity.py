################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import time
import statistics
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC4671_eval, TMC6100_eval
from pytrinamic.ic import TMC4671, TMC6100


with ConnectionManager().connect() as my_interface:

    # Create TMC4671-EVAL and TMC6100-EVAL class which communicate over the Landungsbrücke via TMCL
    mc_eval = TMC4671_eval(my_interface)
    drv_eval = TMC6100_eval(my_interface)

    # Configure TMC6100 pwm for use with TMC4671 (disable singleline)
    drv_eval.write_register_field(TMC6100.FIELD.SINGLELINE, 0)

    # Configure TMC4671 for a BLDC motor with digital hall

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
    mc_eval.write_register(TMC4671.REG.ADC_I0_SCALE_OFFSET, 0xFF000000)
    mc_eval.write_register(TMC4671.REG.ADC_I1_SCALE_OFFSET, 0xFF000000)
    for _ in range(50):
        adc_i0_samples.append(mc_eval.read_register_field(TMC4671.FIELD.ADC_I0_RAW))
        adc_i1_samples.append(mc_eval.read_register_field(TMC4671.FIELD.ADC_I0_RAW))
    adc_i0_offset = statistics.mean(adc_i0_samples)
    adc_i1_offset = statistics.mean(adc_i1_samples)
    mc_eval.write_register(TMC4671.REG.ADC_I0_SCALE_OFFSET, 0xFF000000 + int(adc_i0_offset))
    mc_eval.write_register(TMC4671.REG.ADC_I1_SCALE_OFFSET, 0xFF000000 + int(adc_i1_offset))

    # Limits
    mc_eval.write_register(TMC4671.REG.PID_TORQUE_FLUX_LIMITS, 1000)

    # PI settings for Torque/Flux regulator
    mc_eval.write_register(TMC4671.REG.PID_TORQUE_P_TORQUE_I, 0x01000100)
    mc_eval.write_register(TMC4671.REG.PID_FLUX_P_FLUX_I, 0x01000100)

    # hall settings
    mc_eval.write_register_field(TMC4671.FIELD.HALL_DIRECTION, 1)
    mc_eval.write_register_field(TMC4671.FIELD.HALL_PHI_E_OFFSET, 9500)

    # Commutation Feedback selection
    mc_eval.write_register(TMC4671.REG.PHI_E_SELECTION, TMC4671.ENUM.PHI_E_HALL)

    # ===== Digital hall test drive =====

    # Limits
    mc_eval.write_register(TMC4671.REG.PID_TORQUE_FLUX_LIMITS, 2000)

    # PI settings for velocity regulator
    mc_eval.write_register(TMC4671.REG.PID_VELOCITY_P_VELOCITY_I, 400 << 16 | 100 << 0)

    # Velocity Feedback selection
    mc_eval.write_register(TMC4671.REG.VELOCITY_SELECTION, TMC4671.ENUM.VELOCITY_PHI_M_HAL)

    # Switch to velocity mode
    mc_eval.write_register(TMC4671.REG.MODE_RAMP_MODE_MOTION, TMC4671.ENUM.MOTION_MODE_VELOCITY)

    # Rotate right
    print("Rotate right!")
    mc_eval.write_register(TMC4671.REG.PID_VELOCITY_TARGET, 500)
    time.sleep(3)

    # Stop
    print("Stop!")
    mc_eval.write_register(TMC4671.REG.PID_VELOCITY_TARGET, 0)
    time.sleep(1)

    # Switch to stop mode
    mc_eval.write_register(TMC4671.REG.MODE_RAMP_MODE_MOTION, TMC4671.ENUM.MOTION_MODE_STOPPED)
