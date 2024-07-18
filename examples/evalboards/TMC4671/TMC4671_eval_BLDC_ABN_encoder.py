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

    # Configure TMC4671 for a BLDC motor with ABN-Encoder

    # Motor type & PWM configuration
    eval_board.write_register_field(mc.FIELD.MOTOR_TYPE, mc.ENUM.MOTOR_TYPE_BLDC)
    eval_board.write_register_field(mc.FIELD.N_POLE_PAIRS, 4)
    eval_board.write_register(mc.REG.PWM_POLARITIES, 0x00000000)
    eval_board.write_register(mc.REG.PWM_MAXCNT, int(0x00000F9F))
    eval_board.write_register(mc.REG.PWM_BBM_H_BBM_L, 0x00000A0A)
    eval_board.write_register_field(mc.FIELD.PWM_CHOP, mc.ENUM.PWM_CENTERED_FOR_FOC)
    eval_board.write_register_field(mc.FIELD.PWM_SV, 1)

    # ADC configuration
    eval_board.write_register(mc.REG.ADC_I_SELECT, 0x18000100)
    eval_board.write_register(mc.REG.dsADC_MCFG_B_MCFG_A, 0x00100010)
    eval_board.write_register(mc.REG.dsADC_MCLK_A, 0x20000000)
    eval_board.write_register(mc.REG.dsADC_MCLK_B, 0x00000000)
    eval_board.write_register(mc.REG.dsADC_MDEC_B_MDEC_A, int(0x014E014E))
    eval_board.write_register(mc.REG.ADC_I0_SCALE_OFFSET, 0x01008218)
    eval_board.write_register(mc.REG.ADC_I1_SCALE_OFFSET, 0x0100820A)
    # eval_board.write_register(mc.REG.ADC_I0_SCALE_OFFSET, 0x01005D87)
    # eval_board.write_register(mc.REG.ADC_I1_SCALE_OFFSET, 0x01005E0B)

    # ABN encoder settings
    eval_board.write_register(mc.REG.ABN_DECODER_MODE, 0x00001000)
    eval_board.write_register(mc.REG.ABN_DECODER_PPR, 4096)
    eval_board.write_register(mc.REG.ABN_DECODER_PHI_E_PHI_M_OFFSET, 0)

    # Limits
    eval_board.write_register(mc.REG.PID_TORQUE_FLUX_LIMITS, 1000)

    # PI settings
    eval_board.write_register(mc.REG.PID_TORQUE_P_TORQUE_I, 0x01000100)
    eval_board.write_register(mc.REG.PID_FLUX_P_FLUX_I, 0x01000100)

    # ===== ABN encoder test drive =====

    # Init encoder (mode 0)
    print("Initializing Encoder...")
    eval_board.write_register(mc.REG.MODE_RAMP_MODE_MOTION, 0x00000008)
    eval_board.write_register(mc.REG.ABN_DECODER_PHI_E_PHI_M_OFFSET, 0x00000000)
    eval_board.write_register(mc.REG.PHI_E_SELECTION, mc.ENUM.PHI_E_EXTERNAL)
    eval_board.write_register(mc.REG.PHI_E_EXT, 0x00000000)
    eval_board.write_register(mc.REG.UQ_UD_EXT, 2000)
    time.sleep(1)

    # Clear abn_decoder_count
    eval_board.write_register(mc.REG.ABN_DECODER_COUNT, 0)

    # Feedback selection
    eval_board.write_register(mc.REG.PHI_E_SELECTION, mc.ENUM.PHI_E_ABN)
    eval_board.write_register(mc.REG.VELOCITY_SELECTION, mc.ENUM.VELOCITY_PHI_M_ABN)

    # Switch to torque mode
    eval_board.write_register(mc.REG.MODE_RAMP_MODE_MOTION, mc.ENUM.MOTION_MODE_TORQUE)

    # Rotate right
    print("Rotate right...")
    eval_board.write_register_field(mc.FIELD.PID_TORQUE_TARGET, 1000)
    time.sleep(3)

    # Rotate left
    print("Rotate left...")
    eval_board.write_register_field(mc.FIELD.PID_TORQUE_TARGET, -1000)
    time.sleep(3)

    # Stop
    print("Stop...")
    eval_board.write_register(mc.REG.PID_TORQUE_FLUX_TARGET, 0)

print("\nReady.")
