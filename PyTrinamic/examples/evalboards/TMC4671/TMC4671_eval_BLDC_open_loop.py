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
USE_LANDUNGSBRUECKE = True #False

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

" configure TMC4671 for a BLDC motor in open loop mode"

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

" Open loop settings "
tmc4671.writeRegister(tmc4671_reg.OPENLOOP_MODE, 0x00000000) 
tmc4671.writeRegister(tmc4671_reg.OPENLOOP_ACCELERATION, 0x0000003C) 
 
" Feedback selection "
tmc4671.writeRegister(tmc4671_reg.PHI_E_SELECTION, tmc4671_reg.PHI_E_OPEN_LOOP) 
tmc4671.writeRegister(tmc4671_reg.UQ_UD_EXT, 2000) 

" ===== Open loop test drive ===== "

" Switch to open loop velocity mode "
tmc4671.writeRegister(tmc4671_reg.MODE_RAMP_MODE_MOTION, tmc4671_reg.MOTION_MODE_UQ_UD_EXT)
 
" Rotate right "
print("rotate right...")
tmc4671.writeRegister(tmc4671_reg.OPENLOOP_VELOCITY_TARGET, 120)
time.sleep(3)
  
" Rotate left "
print("rotate left...")
tmc4671.writeRegister(tmc4671_reg.OPENLOOP_VELOCITY_TARGET, -120)
time.sleep(6)
 
" Stop "
print("stop...")
tmc4671.writeRegister(tmc4671_reg.OPENLOOP_VELOCITY_TARGET, 0)
time.sleep(3) 
 
" unpower "
print("unpowered...")
tmc4671.writeRegister(tmc4671_reg.UQ_UD_EXT, 0)

myInterface.close()