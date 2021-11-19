#!/usr/bin/env python3
'''
Created on 02.01.2019

@author: ED
'''
if __name__ == '__main__':
    pass

import time
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC4671_eval import TMC4671_eval
from PyTrinamic.ic.TMC4671.TMC4671 import TMC4671 as TMC4671_IC

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()

if myInterface.supportsTMCL():
    # Create an TMC4671-Eval class which communicates over the Landungsbruecke via TMCL
    TMC4671 = TMC4671_eval(myInterface)
else:
    # Create an TMC4671 IC class which communicates directly over UART
    TMC4671 = TMC4671_IC(myInterface)

" read ChipInfo "

TMC4671.showChipInfo

" configure TMC4671 for a BLDC motor in open loop mode"

" Motor type &  PWM configuration "
TMC4671.writeRegister(TMC4671.registers.MOTOR_TYPE_N_POLE_PAIRS, 0x00030004)
TMC4671.writeRegister(TMC4671.registers.PWM_POLARITIES, 0x00000000)
TMC4671.writeRegister(TMC4671.registers.PWM_MAXCNT, int(0x00000F9F))
TMC4671.writeRegister(TMC4671.registers.PWM_BBM_H_BBM_L, 0x00000505)
TMC4671.writeRegister(TMC4671.registers.PWM_SV_CHOP, 0x00000007)

" ADC configuration "
TMC4671.writeRegister(TMC4671.registers.ADC_I_SELECT, 0x18000100)
TMC4671.writeRegister(TMC4671.registers.dsADC_MCFG_B_MCFG_A, 0x00100010)
TMC4671.writeRegister(TMC4671.registers.dsADC_MCLK_A, 0x20000000)
TMC4671.writeRegister(TMC4671.registers.dsADC_MCLK_B, 0x00000000)
TMC4671.writeRegister(TMC4671.registers.dsADC_MDEC_B_MDEC_A, int(0x014E014E))
TMC4671.writeRegister(TMC4671.registers.ADC_I0_SCALE_OFFSET, 0x01008218)
TMC4671.writeRegister(TMC4671.registers.ADC_I1_SCALE_OFFSET, 0x0100820A)

" Open loop settings "
TMC4671.writeRegister(TMC4671.registers.OPENLOOP_MODE, 0x00000000)
TMC4671.writeRegister(TMC4671.registers.OPENLOOP_ACCELERATION, 0x0000003C)

" Feedback selection "
TMC4671.writeRegister(TMC4671.registers.PHI_E_SELECTION, TMC4671.registers.PHI_E_OPEN_LOOP)
TMC4671.writeRegister(TMC4671.registers.UQ_UD_EXT, 2000)

" ===== Open loop test drive ===== "

" Switch to open loop velocity mode "
TMC4671.writeRegister(TMC4671.registers.MODE_RAMP_MODE_MOTION, TMC4671.registers.MOTION_MODE_UQ_UD_EXT)

" Rotate right "
print("rotate right...")
TMC4671.writeRegister(TMC4671.registers.OPENLOOP_VELOCITY_TARGET, 2000)
time.sleep(3)

" Rotate left "
print("rotate left...")
TMC4671.writeRegister(TMC4671.registers.OPENLOOP_VELOCITY_TARGET, -2000)
time.sleep(6)

" Stop "
print("stop...")
TMC4671.writeRegister(TMC4671.registers.OPENLOOP_VELOCITY_TARGET, 0)
time.sleep(3)

" unpower "
print("unpowered...")
TMC4671.writeRegister(TMC4671.registers.UQ_UD_EXT, 0)

myInterface.close()