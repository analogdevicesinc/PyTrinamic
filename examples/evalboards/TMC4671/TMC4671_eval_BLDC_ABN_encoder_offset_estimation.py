################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import time
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC4671_eval
from pytrinamic.ic import TMC4671

pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
#with ConnectionManager("--interface uart_ic --port COM14 --data-rate 9600").connect() as my_interface:  # Swap with previous line if you are not using the Landungsbrueck but a USB UART cable
    print(my_interface)

    if my_interface.supports_tmcl():
        # Create an TMC4671 IC class which communicates over the Landungsbrücke via TMCL
        eval_board = TMC4671_eval(my_interface)
        mc = eval_board.ics[0]
    else:
        # Create an TMC4671 IC class which communicates directly over UART
        mc = TMC4671(my_interface)
        # Use IC like an "EVAL" to use this example for both access variants
        eval_board = mc

    # ===== 1) Base configuration =====

    pole_pairs = 4
    encoder_resolution = 4096

    # Motor type & PWM configuration
    eval_board.write_register_field(TMC4671.FIELD.MOTOR_TYPE, TMC4671.ENUM.MOTOR_TYPE_BLDC)
    eval_board.write_register_field(TMC4671.FIELD.N_POLE_PAIRS, pole_pairs)
    eval_board.write_register(TMC4671.REG.PWM_POLARITIES, 0x00000000)
    eval_board.write_register(TMC4671.REG.PWM_MAXCNT, int(0x00000F9F))
    eval_board.write_register(TMC4671.REG.PWM_BBM_H_BBM_L, 0x00000A0A)
    eval_board.write_register_field(TMC4671.FIELD.PWM_CHOP, TMC4671.ENUM.PWM_CENTERED_FOR_FOC)
    eval_board.write_register_field(TMC4671.FIELD.PWM_SV, 1)

    # ADC configuration
    eval_board.write_register(TMC4671.REG.ADC_I_SELECT, 0x18000100)
    eval_board.write_register(TMC4671.REG.dsADC_MCFG_B_MCFG_A, 0x00100010)
    eval_board.write_register(TMC4671.REG.dsADC_MCLK_A, 0x20000000)
    eval_board.write_register(TMC4671.REG.dsADC_MCLK_B, 0x00000000)
    eval_board.write_register(TMC4671.REG.dsADC_MDEC_B_MDEC_A, int(0x014E014E))
    eval_board.write_register(TMC4671.REG.ADC_I0_SCALE_OFFSET, 0x01008218)
    eval_board.write_register(TMC4671.REG.ADC_I1_SCALE_OFFSET, 0x0100820A)
    # eval_board.write_register(TMC4671.REG.ADC_I0_SCALE_OFFSET, 0x01005D87)
    # eval_board.write_register(TMC4671.REG.ADC_I1_SCALE_OFFSET, 0x01005E0B)

    # ABN encoder settings
    eval_board.write_register(TMC4671.REG.ABN_DECODER_MODE, 0x00001000)
    eval_board.write_register(TMC4671.REG.ABN_DECODER_PPR, encoder_resolution)
    eval_board.write_register(TMC4671.REG.ABN_DECODER_PHI_E_PHI_M_OFFSET, 0)

    # Open loop settings
    eval_board.write_register(TMC4671.REG.OPENLOOP_MODE, 0x00000000)
    eval_board.write_register(TMC4671.REG.OPENLOOP_ACCELERATION, 100)

    # Limits
    eval_board.write_register(TMC4671.REG.PID_TORQUE_FLUX_LIMITS, 1000)

    # PI settings
    eval_board.write_register(TMC4671.REG.PID_TORQUE_P_TORQUE_I, 0x01000100)
    eval_board.write_register(TMC4671.REG.PID_FLUX_P_FLUX_I, 0x01000100)

    # ===== 2) Estimate the encoder offset =====

    # Init encoder (mode 0)
    # Put a voltage on the motor and wait 1 second for alignment
    eval_board.write_register(TMC4671.REG.MODE_RAMP_MODE_MOTION, 0x00000008)
    eval_board.write_register(TMC4671.REG.ABN_DECODER_PHI_E_PHI_M_OFFSET, 0x00000000)
    eval_board.write_register(TMC4671.REG.PHI_E_SELECTION, TMC4671.ENUM.PHI_E_EXTERNAL)
    eval_board.write_register(TMC4671.REG.PHI_E_EXT, 0x00000000)
    eval_board.write_register(TMC4671.REG.UQ_UD_EXT, 2000)
    time.sleep(1)

    # Clear abn_decoder_count
    eval_board.write_register(TMC4671.REG.ABN_DECODER_COUNT, 0)

    print("abn_decoder_count:" + str(eval_board.read_register(TMC4671.REG.ABN_DECODER_COUNT)))

    # Switch to open loop velocity mode
    eval_board.write_register(TMC4671.REG.PHI_E_SELECTION, TMC4671.ENUM.PHI_E_OPEN_LOOP)
    eval_board.write_register(TMC4671.REG.OPENLOOP_VELOCITY_TARGET, 60)

    start_time = time.time()
    while True:
        print("dec: " + str(eval_board.read_register(TMC4671.REG.ABN_DECODER_COUNT)) +
              " dec_n: " + str(eval_board.read_register(TMC4671.REG.ABN_DECODER_COUNT_N)))

        # Stop after 3 seconds
        if (time.time() - start_time) > 3:
            break

    # Read encoder offset at N channel
    decoder_count_n = eval_board.read_register(TMC4671.REG.ABN_DECODER_COUNT_N)
    decoder_count_n_offset = decoder_count_n % (encoder_resolution / pole_pairs)

    print("abn_decoder_count_n:" + str(decoder_count_n))
    print("=> estimated encoder offset: " + str(decoder_count_n_offset))

    # ===== 3) Use the estimated offset =====

    # Write offset
    eval_board.write_register(TMC4671.REG.ABN_DECODER_PHI_E_PHI_M_OFFSET, int(decoder_count_n_offset))

    #  ===== 4) Go to encoder mode =====

    # Feedback selection
    eval_board.write_register(TMC4671.REG.PHI_E_SELECTION, TMC4671.ENUM.PHI_E_ABN)
    eval_board.write_register(TMC4671.REG.VELOCITY_SELECTION, TMC4671.ENUM.VELOCITY_PHI_M_ABN)

    # Switch to torque mode
    eval_board.write_register(TMC4671.REG.MODE_RAMP_MODE_MOTION, TMC4671.ENUM.MOTION_MODE_TORQUE)

    # ===== 5) Make a test drive =====

    max_velocity = 0
    min_velocity = 0

    print("Rotate right...")
    eval_board.write_register_field(TMC4671.FIELD.PID_TORQUE_TARGET, 1000)

    start_time = time.time()
    while True:
        velocity = eval_board.read_register(TMC4671.REG.PID_VELOCITY_ACTUAL, signed=True)
        print("velocity: " + str(velocity))
        if velocity > max_velocity:
            max_velocity = velocity

        # Stop after 3 seconds
        if (time.time() - start_time) > 2:
            break

    print("Rotate left...")
    eval_board.write_register_field(TMC4671.FIELD.PID_TORQUE_TARGET, -1000)

    start_time = time.time()
    while True:
        velocity = eval_board.read_register(TMC4671.REG.PID_VELOCITY_ACTUAL, signed=True)
        print("velocity: " + str(velocity))
        if velocity < min_velocity:
            min_velocity = velocity

        # Stop after 3 seconds
        if (time.time() - start_time) > 2:
            break

    print("Stop motor")
    eval_board.write_register(TMC4671.REG.PID_TORQUE_FLUX_TARGET, 0)

    # ===== 6) Short summary =====

    print(" === Summary === ")
    print("abn_decoder_count_n:" + str(decoder_count_n))
    print("estimated_encoder_offset: " + str(decoder_count_n_offset))
    print("max_velocity:" + str(max_velocity))
    print("min_velocity:" + str(min_velocity))

print("\nReady.")
