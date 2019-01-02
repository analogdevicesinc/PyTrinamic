'''
Created on 02.01.2019

@author: ed
'''

if __name__ == '__main__':
    pass

import time
import PyTrinamic
from PyTrinamic.connections.SerialInterface import SerialInterface
from PyTrinamic.evalboards.TMC4671_Eval import TMC4671_Eval
from PyTrinamic.ICs.TMC4671.TMC4671_Register import TMC4671_Register
from PyTrinamic.ICs.TMC4671.TMC4671_Mask_Shift import TMC4671_Mask_Shift

PyTrinamic.showInfo()
PyTrinamic.showAvailableComPorts()

myInterface = SerialInterface('COM5')
tmc4671_eval = TMC4671_Eval(myInterface)
tmc4671_eval.showChipInfo()

tmc4671_reg = TMC4671_Register()
tmc4671_ms = TMC4671_Mask_Shift()

" configure TMC4671 for a BLDC motor with ABN-Encoder "

" Motor type &  PWM configuration "
myInterface.writeMC(tmc4671_reg.MOTOR_TYPE_N_POLE_PAIRS, 0x00030004)
myInterface.writeMC(tmc4671_reg.PWM_POLARITIES, 0x00000000)
myInterface.writeMC(tmc4671_reg.PWM_MAXCNT, int(0x00000F9F))
myInterface.writeMC(tmc4671_reg.PWM_BBM_H_BBM_L, 0x00000505) 
myInterface.writeMC(tmc4671_reg.PWM_SV_CHOP, 0x00000007)

" ADC configuration "
myInterface.writeMC(tmc4671_reg.ADC_I_SELECT, 0x18000100) 
myInterface.writeMC(tmc4671_reg.dsADC_MCFG_B_MCFG_A, 0x00100010) 
myInterface.writeMC(tmc4671_reg.dsADC_MCLK_A, 0x20000000) 
myInterface.writeMC(tmc4671_reg.dsADC_MCLK_B, 0x00000000) 
myInterface.writeMC(tmc4671_reg.dsADC_MDEC_B_MDEC_A, int(0x014E014E))
myInterface.writeMC(tmc4671_reg.ADC_I0_SCALE_OFFSET, 0x01008218) 
myInterface.writeMC(tmc4671_reg.ADC_I1_SCALE_OFFSET, 0x0100820A) 

" ABN encoder settings "
myInterface.writeMC(tmc4671_reg.ABN_DECODER_MODE, 0x00001000) 
myInterface.writeMC(tmc4671_reg.ABN_DECODER_PPR, 4000) 
myInterface.writeMC(tmc4671_reg.ABN_DECODER_COUNT, 0x0) 
myInterface.writeMC(tmc4671_reg.ABN_DECODER_PHI_E_PHI_M_OFFSET, 0x0)
                     
" Limits "
myInterface.writeMC(tmc4671_reg.PID_TORQUE_FLUX_LIMITS, 1000) 

" PI settings "
myInterface.writeMC(tmc4671_reg.PID_TORQUE_P_TORQUE_I, 0x01000100) 
myInterface.writeMC(tmc4671_reg.PID_FLUX_P_FLUX_I, 0x01000100) 

" ===== ABN encoder test drive ===== "

" Init encoder (mode 0) "
myInterface.writeMC(tmc4671_reg.MODE_RAMP_MODE_MOTION, 0x00000008) 
myInterface.writeMC(tmc4671_reg.ABN_DECODER_PHI_E_PHI_M_OFFSET, 0x00000000) 
myInterface.writeMC(tmc4671_reg.PHI_E_SELECTION, 0x00000001)
myInterface.writeMC(tmc4671_reg.PHI_E_EXT, 0x00000000)
myInterface.writeMC(tmc4671_reg.UQ_UD_EXT, 2000)
time.sleep(1)
myInterface.writeMC(tmc4671_reg.ABN_DECODER_COUNT, 0x00000000) 

" Feedback selection "
myInterface.writeMC(tmc4671_reg.PHI_E_SELECTION, 0x00000003) 
myInterface.writeMC(tmc4671_reg.VELOCITY_SELECTION, 0x00000009)

" Switch to torque mode "
myInterface.writeMC(tmc4671_reg.MODE_RAMP_MODE_MOTION, tmc4671_reg.MOTION_MODE_TORQUE)
                     
" Rotate right "
print("rotate right...")
myInterface.writeMC(tmc4671_reg.PID_TORQUE_FLUX_TARGET, 0x03E80000)
time.sleep(3)
 
" Rotate left "
print("rotate left...")
myInterface.writeMC(tmc4671_reg.PID_TORQUE_FLUX_TARGET, int(0xFC180000))
time.sleep(3)

" Stop "
print("stop...")
myInterface.writeMC(tmc4671_reg.PID_TORQUE_FLUX_TARGET, 0)
time.sleep(3) 

myInterface.close()