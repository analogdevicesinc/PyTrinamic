#!/usr/bin/env python3
'''
Created on 02.01.2019

@author: ed
'''

if __name__ == '__main__':
    pass

import time
import PyTrinamic
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
from PyTrinamic.connections.uart_ic_interface import uart_ic_interface
from PyTrinamic.evalboards.TMC4671_eval import TMC4671_eval
from PyTrinamic.ic.TMC4671.TMC4671 import TMC4671

PyTrinamic.showInfo()
PyTrinamic.showAvailableComPorts(Serial=True)

" use evalboard via landungsbrücke or directly via UART"
USE_LANDUNGSBRUECKE = True #False #True

if USE_LANDUNGSBRUECKE:
    myInterface = serial_tmcl_interface('COM5')
    tmc4671 = TMC4671_eval(myInterface).ic()
else:
    myInterface = uart_ic_interface(PyTrinamic.firstAvailableComPort())
    tmc4671 = TMC4671(myInterface)

" get register set "
tmc4671_reg = tmc4671.register()

" read ChipInfo "
tmc4671.showChipInfo()

" configure TMC4671 for a BLDC motor with ABN-Encoder "

" Motor type &  PWM configuration "
tmc4671.writeRegister(tmc4671_reg.MOTOR_TYPE_N_POLE_PAIRS, 0x00030004)
tmc4671.writeRegister(tmc4671_reg.PWM_POLARITIES, 0x00000000)
tmc4671.writeRegister(tmc4671_reg.PWM_MAXCNT, int(0x00000F9F))
tmc4671.writeRegister(tmc4671_reg.PWM_BBM_H_BBM_L, 0x00000505) 
tmc4671.writeRegister(tmc4671_reg.PWM_SV_CHOP, 0x00000007)
 
" ADC configuration "
tmc4671.writeRegister(tmc4671_reg.ADC_I_SELECT, 0x18000100) 
tmc4671.writeRegister(tmc4671_reg.dsADC_MCFG_B_MCFG_A, 0x00100010) 
tmc4671.writeRegister(tmc4671_reg.dsADC_MCLK_A, 0x20000000) 
tmc4671.writeRegister(tmc4671_reg.dsADC_MCLK_B, 0x00000000) 
tmc4671.writeRegister(tmc4671_reg.dsADC_MDEC_B_MDEC_A, int(0x014E014E))
tmc4671.writeRegister(tmc4671_reg.ADC_I0_SCALE_OFFSET, 0x01008218) 
tmc4671.writeRegister(tmc4671_reg.ADC_I1_SCALE_OFFSET, 0x0100820A) 
 
" ABN encoder settings "
tmc4671.writeRegister(tmc4671_reg.ABN_DECODER_MODE, 0x00001000) 
tmc4671.writeRegister(tmc4671_reg.ABN_DECODER_PPR, 4000) 
tmc4671.writeRegister(tmc4671_reg.ABN_DECODER_COUNT, 0x0) 
tmc4671.writeRegister(tmc4671_reg.ABN_DECODER_PHI_E_PHI_M_OFFSET, 0x0)
                      
" Limits "
tmc4671.writeRegister(tmc4671_reg.PID_TORQUE_FLUX_LIMITS, 1000) 
 
" PI settings "
tmc4671.writeRegister(tmc4671_reg.PID_TORQUE_P_TORQUE_I, 0x01000100) 
tmc4671.writeRegister(tmc4671_reg.PID_FLUX_P_FLUX_I, 0x01000100) 
 
" ===== ABN encoder test drive ===== "
 
" Init encoder (mode 0) "
tmc4671.writeRegister(tmc4671_reg.MODE_RAMP_MODE_MOTION, 0x00000008) 
tmc4671.writeRegister(tmc4671_reg.ABN_DECODER_PHI_E_PHI_M_OFFSET, 0x00000000) 
tmc4671.writeRegister(tmc4671_reg.PHI_E_SELECTION, 0x00000001)
tmc4671.writeRegister(tmc4671_reg.PHI_E_EXT, 0x00000000)
tmc4671.writeRegister(tmc4671_reg.UQ_UD_EXT, 2000)
time.sleep(1)

" clear abn_decoder_count "
tmc4671.writeRegister(tmc4671_reg.ABN_DECODER_COUNT, 0x00000000) 
 
" Feedback selection "
tmc4671.writeRegister(tmc4671_reg.PHI_E_SELECTION, tmc4671_reg.PHI_E_ABN) 
tmc4671.writeRegister(tmc4671_reg.VELOCITY_SELECTION, tmc4671_reg.VELOCITY_PHI_M_ABN)
 
" Switch to torque mode "
tmc4671.writeRegister(tmc4671_reg.MODE_RAMP_MODE_MOTION, tmc4671_reg.MOTION_MODE_TORQUE)
                      
" Rotate right "
print("rotate right...")
tmc4671.writeRegister(tmc4671_reg.PID_TORQUE_FLUX_TARGET, 0x03E80000)
time.sleep(3)
  
" Rotate left "
print("rotate left...")
tmc4671.writeRegister(tmc4671_reg.PID_TORQUE_FLUX_TARGET, int(0xFC180000))
time.sleep(3)
 
" Stop "
print("stop...")
tmc4671.writeRegister(tmc4671_reg.PID_TORQUE_FLUX_TARGET, 0)

myInterface.close()