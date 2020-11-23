#!/usr/bin/env python3
'''
Created on 07.03.2019

@author: ED
'''

if __name__ == '__main__':
    pass

import time
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC4671_eval import TMC4671_eval
from PyTrinamic.evalboards.TMC6200_eval import TMC6200_eval
from PyTrinamic.ic.TMC4671.TMC4671 import TMC4671 as TMC4671_IC
from PyTrinamic.ic.TMC6200.TMC6200 import TMC6200 as TMC6200_IC
from PyTrinamic.connections.uart_ic_interface import uart_ic_interface

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()

if isinstance(myInterface, uart_ic_interface):
    # Create an TMC4671 IC class which communicates directly over UART
    TMC4671 = TMC4671_IC(myInterface)
else:
    # Create an TMC4671-Eval class which communicates over the Landungsbruecke via TMCL
    TMC4671 = TMC4671_eval(myInterface)

if isinstance(myInterface, uart_ic_interface):
    # Create an TMC4671 IC class which communicates directly over UART
    TMC6200 = TMC6200_IC(myInterface)
else:
    # Create an TMC4671-Eval class which communicates over the Landungsbruecke via TMCL
    TMC6200 = TMC6200_eval(myInterface)

" read ChipInfo "

TMC4671.showChipInfo
TMC6200.showChipInfo

" configure TMC6200 pwm for use with TMC4671 (disable singleline)"
TMC6200.writeRegister(TMC6200.registers.GCONF, 0x0)

" configure TMC4671 for a BLDC motor with ABN-Encoder "

" Motor type &  PWM configuration "
TMC4671.writeRegister(TMC4671.registers.MOTOR_TYPE_N_POLE_PAIRS, 0x00030004)
TMC4671.writeRegister(TMC4671.registers.PWM_POLARITIES, 0x00000000)
TMC4671.writeRegister(TMC4671.registers.PWM_MAXCNT, int(0x00000F9F))
TMC4671.writeRegister(TMC4671.registers.PWM_BBM_H_BBM_L, 0x00001414)
TMC4671.writeRegister(TMC4671.registers.PWM_SV_CHOP, 0x00000007)

" ADC configuration "
TMC4671.writeRegister(TMC4671.registers.ADC_I_SELECT, 0x24000100)
TMC4671.writeRegister(TMC4671.registers.dsADC_MCFG_B_MCFG_A, 0x00100010)
TMC4671.writeRegister(TMC4671.registers.dsADC_MCLK_A, 0x20000000)
TMC4671.writeRegister(TMC4671.registers.dsADC_MCLK_B, 0x00000000)
TMC4671.writeRegister(TMC4671.registers.dsADC_MDEC_B_MDEC_A, int(0x014E014E))
TMC4671.writeRegister(TMC4671.registers.ADC_I0_SCALE_OFFSET, 0xFF00826D)
TMC4671.writeRegister(TMC4671.registers.ADC_I1_SCALE_OFFSET, 0xFF0081F8)

" ABN encoder settings "
TMC4671.writeRegister(TMC4671.registers.ABN_DECODER_MODE, 0x00000000)
TMC4671.writeRegister(TMC4671.registers.ABN_DECODER_PPR, 4096)
TMC4671.writeRegister(TMC4671.registers.ABN_DECODER_COUNT, 0x0)
TMC4671.writeRegister(TMC4671.registers.ABN_DECODER_PHI_E_PHI_M_OFFSET, 0x0)

" Limits "
TMC4671.writeRegister(TMC4671.registers.PID_TORQUE_FLUX_LIMITS, 1000)

" PI settings "
TMC4671.writeRegister(TMC4671.registers.PID_TORQUE_P_TORQUE_I, 0x01000100)
TMC4671.writeRegister(TMC4671.registers.PID_FLUX_P_FLUX_I, 0x01000100)

" ===== ABN encoder test drive ===== "

" Init encoder (mode 0) "
TMC4671.writeRegister(TMC4671.registers.MODE_RAMP_MODE_MOTION, 0x00000008)
TMC4671.writeRegister(TMC4671.registers.ABN_DECODER_PHI_E_PHI_M_OFFSET, 0x00000000)
TMC4671.writeRegister(TMC4671.registers.PHI_E_SELECTION, TMC4671.registers.PHI_E_EXTERNAL)
TMC4671.writeRegister(TMC4671.registers.PHI_E_EXT, 0x00000000)
TMC4671.writeRegister(TMC4671.registers.UQ_UD_EXT, 2000)
time.sleep(1)

" clear abn_decoder_count "
TMC4671.writeRegister(TMC4671.registers.ABN_DECODER_COUNT, 0x00000000)

" Feedback selection "
TMC4671.writeRegister(TMC4671.registers.PHI_E_SELECTION, TMC4671.registers.PHI_E_ABN)
TMC4671.writeRegister(TMC4671.registers.VELOCITY_SELECTION, TMC4671.registers.VELOCITY_PHI_M_ABN)

" Switch to torque mode "
TMC4671.writeRegister(TMC4671.registers.MODE_RAMP_MODE_MOTION, TMC4671.registers.MOTION_MODE_TORQUE)

" Rotate right "
print("rotate right...")
TMC4671.writeRegister(TMC4671.registers.PID_TORQUE_FLUX_TARGET, 0x03E80000)
time.sleep(3)

" Rotate left "
print("rotate left...")
TMC4671.writeRegister(TMC4671.registers.PID_TORQUE_FLUX_TARGET, int(0xFC180000))
time.sleep(3)

" Stop "
print("stop...")
TMC4671.writeRegister(TMC4671.registers.PID_TORQUE_FLUX_TARGET, 0)

myInterface.close()