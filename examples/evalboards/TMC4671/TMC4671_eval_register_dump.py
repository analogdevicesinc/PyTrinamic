################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Dump all register values of the TMC4671 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are used for communication with the IC.
"""
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.connections import UartIcInterface
from pytrinamic.evalboards import TMC4671_eval
from pytrinamic.ic import TMC4671

pytrinamic.show_info()
my_interface = ConnectionManager().connect()
#my_interface = ConnectionManager("--interface uart_ic --port COM14 --data-rate 9600").connect()  # Swap with previous line if you are not using the Landungsbrueck but a USB UART cable
print(my_interface)

if isinstance(my_interface, UartIcInterface):
    # Create an TMC4671 IC class which communicates directly over UART
    mc = TMC4671(my_interface)
    # Use IC like an "EVAL" to use this example for both access variants
    eval_board = mc
else:
    # Create an TMC4671 IC class which communicates over the Landungsbrücke via TMCL
    eval_board = TMC4671_eval(my_interface)
    mc = eval_board.ics[0]

print("CHIPINFO_DATA:                     0x{0:08X}".format(eval_board.read_register(mc.REG.CHIPINFO_DATA)))
print("CHIPINFO_ADDR:                     0x{0:08X}".format(eval_board.read_register(mc.REG.CHIPINFO_ADDR)))
print("ADC_RAW_DATA:                      0x{0:08X}".format(eval_board.read_register(mc.REG.ADC_RAW_DATA)))
print("ADC_RAW_ADDR:                      0x{0:08X}".format(eval_board.read_register(mc.REG.ADC_RAW_ADDR)))
print("dsADC_MCFG_B_MCFG_A:               0x{0:08X}".format(eval_board.read_register(mc.REG.dsADC_MCFG_B_MCFG_A)))
print("dsADC_MCLK_A:                      0x{0:08X}".format(eval_board.read_register(mc.REG.dsADC_MCLK_A)))
print("dsADC_MCLK_B:                      0x{0:08X}".format(eval_board.read_register(mc.REG.dsADC_MCLK_B)))
print("dsADC_MDEC_B_MDEC_A:               0x{0:08X}".format(eval_board.read_register(mc.REG.dsADC_MDEC_B_MDEC_A)))
print("ADC_I1_SCALE_OFFSET:               0x{0:08X}".format(eval_board.read_register(mc.REG.ADC_I1_SCALE_OFFSET)))
print("ADC_I0_SCALE_OFFSET:               0x{0:08X}".format(eval_board.read_register(mc.REG.ADC_I0_SCALE_OFFSET)))
print("ADC_I_SELECT:                      0x{0:08X}".format(eval_board.read_register(mc.REG.ADC_I_SELECT)))
print("ADC_I1_I0_EXT:                     0x{0:08X}".format(eval_board.read_register(mc.REG.ADC_I1_I0_EXT)))
print("DS_ANALOG_INPUT_STAGE_CFG:         0x{0:08X}".format(eval_board.read_register(mc.REG.DS_ANALOG_INPUT_STAGE_CFG)))
print("AENC_0_SCALE_OFFSET:               0x{0:08X}".format(eval_board.read_register(mc.REG.AENC_0_SCALE_OFFSET)))
print("AENC_1_SCALE_OFFSET:               0x{0:08X}".format(eval_board.read_register(mc.REG.AENC_1_SCALE_OFFSET)))
print("AENC_2_SCALE_OFFSET:               0x{0:08X}".format(eval_board.read_register(mc.REG.AENC_2_SCALE_OFFSET)))
print("AENC_SELECT:                       0x{0:08X}".format(eval_board.read_register(mc.REG.AENC_SELECT)))
print("ADC_IWY_IUX:                       0x{0:08X}".format(eval_board.read_register(mc.REG.ADC_IWY_IUX)))
print("ADC_IV:                            0x{0:08X}".format(eval_board.read_register(mc.REG.ADC_IV)))
print("AENC_WY_UX:                        0x{0:08X}".format(eval_board.read_register(mc.REG.AENC_WY_UX)))
print("AENC_VN:                           0x{0:08X}".format(eval_board.read_register(mc.REG.AENC_VN)))
print("PWM_POLARITIES:                    0x{0:08X}".format(eval_board.read_register(mc.REG.PWM_POLARITIES)))
print("PWM_MAXCNT:                        0x{0:08X}".format(eval_board.read_register(mc.REG.PWM_MAXCNT)))
print("PWM_BBM_H_BBM_L:                   0x{0:08X}".format(eval_board.read_register(mc.REG.PWM_BBM_H_BBM_L)))
print("PWM_SV_CHOP:                       0x{0:08X}".format(eval_board.read_register(mc.REG.PWM_SV_CHOP)))
print("MOTOR_TYPE_N_POLE_PAIRS:           0x{0:08X}".format(eval_board.read_register(mc.REG.MOTOR_TYPE_N_POLE_PAIRS)))
print("PHI_E_EXT:                         0x{0:08X}".format(eval_board.read_register(mc.REG.PHI_E_EXT)))
print("PHI_M_EXT:                         0x{0:08X}".format(eval_board.read_register(mc.REG.PHI_M_EXT)))
print("POSITION_EXT:                      0x{0:08X}".format(eval_board.read_register(mc.REG.POSITION_EXT)))
print("OPENLOOP_MODE:                     0x{0:08X}".format(eval_board.read_register(mc.REG.OPENLOOP_MODE)))
print("OPENLOOP_ACCELERATION:             0x{0:08X}".format(eval_board.read_register(mc.REG.OPENLOOP_ACCELERATION)))
print("OPENLOOP_VELOCITY_TARGET:          0x{0:08X}".format(eval_board.read_register(mc.REG.OPENLOOP_VELOCITY_TARGET)))
print("OPENLOOP_VELOCITY_ACTUAL:          0x{0:08X}".format(eval_board.read_register(mc.REG.OPENLOOP_VELOCITY_ACTUAL)))
print("OPENLOOP_PHI:                      0x{0:08X}".format(eval_board.read_register(mc.REG.OPENLOOP_PHI)))
print("UQ_UD_EXT:                         0x{0:08X}".format(eval_board.read_register(mc.REG.UQ_UD_EXT)))
print("ABN_DECODER_MODE:                  0x{0:08X}".format(eval_board.read_register(mc.REG.ABN_DECODER_MODE)))
print("ABN_DECODER_PPR:                   0x{0:08X}".format(eval_board.read_register(mc.REG.ABN_DECODER_PPR)))
print("ABN_DECODER_COUNT:                 0x{0:08X}".format(eval_board.read_register(mc.REG.ABN_DECODER_COUNT)))
print("ABN_DECODER_COUNT_N:               0x{0:08X}".format(eval_board.read_register(mc.REG.ABN_DECODER_COUNT_N)))
print("ABN_DECODER_PHI_E_PHI_M_OFFSET:    0x{0:08X}".format(eval_board.read_register(mc.REG.ABN_DECODER_PHI_E_PHI_M_OFFSET)))
print("ABN_DECODER_PHI_E_PHI_M:           0x{0:08X}".format(eval_board.read_register(mc.REG.ABN_DECODER_PHI_E_PHI_M)))
print("ABN_2_DECODER_MODE:                0x{0:08X}".format(eval_board.read_register(mc.REG.ABN_2_DECODER_MODE)))
print("ABN_2_DECODER_PPR:                 0x{0:08X}".format(eval_board.read_register(mc.REG.ABN_2_DECODER_PPR)))
print("ABN_2_DECODER_COUNT:               0x{0:08X}".format(eval_board.read_register(mc.REG.ABN_2_DECODER_COUNT)))
print("ABN_2_DECODER_COUNT_N:             0x{0:08X}".format(eval_board.read_register(mc.REG.ABN_2_DECODER_COUNT_N)))
print("ABN_2_DECODER_PHI_M_OFFSET:        0x{0:08X}".format(eval_board.read_register(mc.REG.ABN_2_DECODER_PHI_M_OFFSET)))
print("ABN_2_DECODER_PHI_M:               0x{0:08X}".format(eval_board.read_register(mc.REG.ABN_2_DECODER_PHI_M)))
print("HALL_MODE:                         0x{0:08X}".format(eval_board.read_register(mc.REG.HALL_MODE)))
print("HALL_POSITION_060_000:             0x{0:08X}".format(eval_board.read_register(mc.REG.HALL_POSITION_060_000)))
print("HALL_POSITION_180_120:             0x{0:08X}".format(eval_board.read_register(mc.REG.HALL_POSITION_180_120)))
print("HALL_POSITION_300_240:             0x{0:08X}".format(eval_board.read_register(mc.REG.HALL_POSITION_300_240)))
print("HALL_PHI_E_PHI_M_OFFSET:           0x{0:08X}".format(eval_board.read_register(mc.REG.HALL_PHI_E_PHI_M_OFFSET)))
print("HALL_DPHI_MAX:                     0x{0:08X}".format(eval_board.read_register(mc.REG.HALL_DPHI_MAX)))
print("HALL_PHI_E_INTERPOLATED_PHI_E:     0x{0:08X}".format(eval_board.read_register(mc.REG.HALL_PHI_E_INTERPOLATED_PHI_E)))
print("HALL_PHI_M:                        0x{0:08X}".format(eval_board.read_register(mc.REG.HALL_PHI_M)))
print("AENC_DECODER_MODE:                 0x{0:08X}".format(eval_board.read_register(mc.REG.AENC_DECODER_MODE)))
print("AENC_DECODER_N_MASK_N_THRESHOLD:   0x{0:08X}".format(eval_board.read_register(mc.REG.AENC_DECODER_N_MASK_N_THRESHOLD)))
print("AENC_DECODER_PHI_A_RAW:            0x{0:08X}".format(eval_board.read_register(mc.REG.AENC_DECODER_PHI_A_RAW)))
print("AENC_DECODER_PHI_A_OFFSET:         0x{0:08X}".format(eval_board.read_register(mc.REG.AENC_DECODER_PHI_A_OFFSET)))
print("AENC_DECODER_PHI_A:                0x{0:08X}".format(eval_board.read_register(mc.REG.AENC_DECODER_PHI_A)))
print("AENC_DECODER_PPR:                  0x{0:08X}".format(eval_board.read_register(mc.REG.AENC_DECODER_PPR)))
print("AENC_DECODER_COUNT:                0x{0:08X}".format(eval_board.read_register(mc.REG.AENC_DECODER_COUNT)))
print("AENC_DECODER_COUNT_N:              0x{0:08X}".format(eval_board.read_register(mc.REG.AENC_DECODER_COUNT_N)))
print("AENC_DECODER_PHI_E_PHI_M_OFFSET:   0x{0:08X}".format(eval_board.read_register(mc.REG.AENC_DECODER_PHI_E_PHI_M_OFFSET)))
print("AENC_DECODER_PHI_E_PHI_M:          0x{0:08X}".format(eval_board.read_register(mc.REG.AENC_DECODER_PHI_E_PHI_M)))
print("AENC_DECODER_POSITION:             0x{0:08X}".format(eval_board.read_register(mc.REG.AENC_DECODER_POSITION)))
print("PIDIN_TORQUE_TARGET_FLUX_TARGET:   0x{0:08X}".format(eval_board.read_register(mc.REG.PIDIN_TORQUE_TARGET_FLUX_TARGET)))
print("PIDIN_VELOCITY_TARGET:             0x{0:08X}".format(eval_board.read_register(mc.REG.PIDIN_VELOCITY_TARGET)))
print("PIDIN_POSITION_TARGET:             0x{0:08X}".format(eval_board.read_register(mc.REG.PIDIN_POSITION_TARGET)))
print("CONFIG_DATA:                       0x{0:08X}".format(eval_board.read_register(mc.REG.CONFIG_DATA)))
print("CONFIG_ADDR:                       0x{0:08X}".format(eval_board.read_register(mc.REG.CONFIG_ADDR)))
print("VELOCITY_SELECTION:                0x{0:08X}".format(eval_board.read_register(mc.REG.VELOCITY_SELECTION)))
print("POSITION_SELECTION:                0x{0:08X}".format(eval_board.read_register(mc.REG.POSITION_SELECTION)))
print("PHI_E_SELECTION:                   0x{0:08X}".format(eval_board.read_register(mc.REG.PHI_E_SELECTION)))
print("PHI_E:                             0x{0:08X}".format(eval_board.read_register(mc.REG.PHI_E)))
print("PID_FLUX_P_FLUX_I:                 0x{0:08X}".format(eval_board.read_register(mc.REG.PID_FLUX_P_FLUX_I)))
print("PID_TORQUE_P_TORQUE_I:             0x{0:08X}".format(eval_board.read_register(mc.REG.PID_TORQUE_P_TORQUE_I)))
print("PID_VELOCITY_P_VELOCITY_I:         0x{0:08X}".format(eval_board.read_register(mc.REG.PID_VELOCITY_P_VELOCITY_I)))
print("PID_POSITION_P_POSITION_I:         0x{0:08X}".format(eval_board.read_register(mc.REG.PID_POSITION_P_POSITION_I)))
print("PID_TORQUE_FLUX_TARGET_DDT_LIMITS: 0x{0:08X}".format(eval_board.read_register(mc.REG.PID_TORQUE_FLUX_TARGET_DDT_LIMITS)))
print("PIDOUT_UQ_UD_LIMITS:               0x{0:08X}".format(eval_board.read_register(mc.REG.PIDOUT_UQ_UD_LIMITS)))
print("PID_TORQUE_FLUX_LIMITS:            0x{0:08X}".format(eval_board.read_register(mc.REG.PID_TORQUE_FLUX_LIMITS)))
print("PID_ACCELERATION_LIMIT:            0x{0:08X}".format(eval_board.read_register(mc.REG.PID_ACCELERATION_LIMIT)))
print("PID_VELOCITY_LIMIT:                0x{0:08X}".format(eval_board.read_register(mc.REG.PID_VELOCITY_LIMIT)))
print("PID_POSITION_LIMIT_LOW:            0x{0:08X}".format(eval_board.read_register(mc.REG.PID_POSITION_LIMIT_LOW)))
print("POSITION_LIMIT_HIGH:               0x{0:08X}".format(eval_board.read_register(mc.REG.POSITION_LIMIT_HIGH)))
print("MODE_RAMP_MODE_MOTION:             0x{0:08X}".format(eval_board.read_register(mc.REG.MODE_RAMP_MODE_MOTION)))
print("PID_TORQUE_FLUX_TARGET:            0x{0:08X}".format(eval_board.read_register(mc.REG.PID_TORQUE_FLUX_TARGET)))
print("PID_TORQUE_FLUX_OFFSET:            0x{0:08X}".format(eval_board.read_register(mc.REG.PID_TORQUE_FLUX_OFFSET)))
print("PID_VELOCITY_TARGET:               0x{0:08X}".format(eval_board.read_register(mc.REG.PID_VELOCITY_TARGET)))
print("PID_VELOCITY_OFFSET:               0x{0:08X}".format(eval_board.read_register(mc.REG.PID_VELOCITY_OFFSET)))
print("PID_POSITION_TARGET:               0x{0:08X}".format(eval_board.read_register(mc.REG.PID_POSITION_TARGET)))
print("PID_TORQUE_FLUX_ACTUAL:            0x{0:08X}".format(eval_board.read_register(mc.REG.PID_TORQUE_FLUX_ACTUAL)))
print("PID_VELOCITY_ACTUAL:               0x{0:08X}".format(eval_board.read_register(mc.REG.PID_VELOCITY_ACTUAL)))
print("PID_POSITION_ACTUAL:               0x{0:08X}".format(eval_board.read_register(mc.REG.PID_POSITION_ACTUAL)))
print("PID_ERROR_DATA:                    0x{0:08X}".format(eval_board.read_register(mc.REG.PID_ERROR_DATA)))
print("PID_ERROR_ADDR:                    0x{0:08X}".format(eval_board.read_register(mc.REG.PID_ERROR_ADDR)))
print("INTERIM_DATA:                      0x{0:08X}".format(eval_board.read_register(mc.REG.INTERIM_DATA)))
print("INTERIM_ADDR:                      0x{0:08X}".format(eval_board.read_register(mc.REG.INTERIM_ADDR)))
print("WATCHDOG_CFG:                      0x{0:08X}".format(eval_board.read_register(mc.REG.WATCHDOG_CFG)))
print("ADC_VM_LIMITS:                     0x{0:08X}".format(eval_board.read_register(mc.REG.ADC_VM_LIMITS)))
print("INPUTS_RAW:                        0x{0:08X}".format(eval_board.read_register(mc.REG.INPUTS_RAW)))
print("OUTPUTS_RAW:                       0x{0:08X}".format(eval_board.read_register(mc.REG.OUTPUTS_RAW)))
print("STEP_WIDTH:                        0x{0:08X}".format(eval_board.read_register(mc.REG.STEP_WIDTH)))
print("UART_BPS:                          0x{0:08X}".format(eval_board.read_register(mc.REG.UART_BPS)))
print("UART_ADDRS:                        0x{0:08X}".format(eval_board.read_register(mc.REG.UART_ADDRS)))
print("GPIO_dsADCI_CONFIG:                0x{0:08X}".format(eval_board.read_register(mc.REG.GPIO_dsADCI_CONFIG)))
print("STATUS_FLAGS:                      0x{0:08X}".format(eval_board.read_register(mc.REG.STATUS_FLAGS)))
print("STATUS_MASK:                       0x{0:08X}".format(eval_board.read_register(mc.REG.STATUS_MASK)))

my_interface.close()
