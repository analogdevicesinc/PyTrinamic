#!/usr/bin/env python3
'''
Created on 26.02.2019

@author: ed
'''

import time
import PyTrinamic
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
from PyTrinamic.connections.uart_ic_interface import uart_ic_interface
from PyTrinamic.evalboards.TMC4671_eval import TMC4671_eval
from PyTrinamic.ic.TMC4671.TMC4671 import TMC4671

PyTrinamic.showInfo()
PyTrinamic.showAvailableComPorts(Serial=True)

" use evalboard via landungsbrücke or directly via UART"
USE_LANDUNGSBRUECKE = False #True

if USE_LANDUNGSBRUECKE:
    myInterface = serial_tmcl_interface('COM5')
    tmc4671 = TMC4671_eval(myInterface).ic()
else:
    myInterface = uart_ic_interface('COM6')
    tmc4671 = TMC4671(myInterface)

" get register set "
tmc4671_reg = tmc4671.register()

" get register set "
tmc4671.showChipInfo()



" ===== 1) base configuration ====="

polePairs = 4
enocoderResolution = 4000

" Motor type &  PWM configuration "
tmc4671.writeRegister(tmc4671_reg.MOTOR_TYPE_N_POLE_PAIRS, 0x00030000 | polePairs)
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
tmc4671.writeRegister(tmc4671_reg.ABN_DECODER_PPR, enocoderResolution) 
tmc4671.writeRegister(tmc4671_reg.ABN_DECODER_COUNT, 0x0) 
tmc4671.writeRegister(tmc4671_reg.ABN_DECODER_PHI_E_PHI_M_OFFSET, 0x0)

" Open loop settings "
tmc4671.writeRegister(tmc4671_reg.OPENLOOP_MODE, 0x00000000) 
tmc4671.writeRegister(tmc4671_reg.OPENLOOP_ACCELERATION, 0x0000003C) 

" Limits "
tmc4671.writeRegister(tmc4671_reg.PID_TORQUE_FLUX_LIMITS, 1000) 

" PI settings "
tmc4671.writeRegister(tmc4671_reg.PID_TORQUE_P_TORQUE_I, 0x01000100) 
tmc4671.writeRegister(tmc4671_reg.PID_FLUX_P_FLUX_I, 0x01000100) 



" ===== 2) estimate the encoder offset ====="

" Init encoder (mode 0) "
" put a voltage on the motor and wait 1 second for alignment "
tmc4671.writeRegister(tmc4671_reg.MODE_RAMP_MODE_MOTION, 0x00000008) 
tmc4671.writeRegister(tmc4671_reg.ABN_DECODER_PHI_E_PHI_M_OFFSET, 0x00000000) 
tmc4671.writeRegister(tmc4671_reg.PHI_E_SELECTION, tmc4671_reg.PHI_E_EXTERNAL)
tmc4671.writeRegister(tmc4671_reg.PHI_E_EXT, 0x00000000)
tmc4671.writeRegister(tmc4671_reg.UQ_UD_EXT, 2000)
time.sleep(1)

" clear abn_decoder_count "
tmc4671.writeRegister(tmc4671_reg.ABN_DECODER_COUNT, 0x00000000)

print("abn_decoder_count:" + str(tmc4671.readRegister(tmc4671_reg.ABN_DECODER_COUNT)))

" Switch to open loop velocity mode "
tmc4671.writeRegister(tmc4671_reg.PHI_E_SELECTION, tmc4671_reg.PHI_E_OPEN_LOOP) 
tmc4671.writeRegister(tmc4671_reg.OPENLOOP_VELOCITY_TARGET, 60)

startTime = time.time()
while True:
    print("dec: " + str(tmc4671.readRegister(tmc4671_reg.ABN_DECODER_COUNT)) + " dec_n: " + str(tmc4671.readRegister(tmc4671_reg.ABN_DECODER_COUNT_N)))
    
    " stop after 3 seconds "
    if (time.time()-startTime) > 3:
        break

" read encoder offset at N channel"    
decoderCountN = tmc4671.readRegister(tmc4671_reg.ABN_DECODER_COUNT_N)
decoderCountN_offset = decoderCountN % (enocoderResolution / polePairs)

print("abn_decoder_count_n:" + str(decoderCountN))
print("=> estimated encoder offset: " + str(decoderCountN_offset))



" ===== 3) use the estimated offset ====="

" write offset "
tmc4671.writeRegister(tmc4671_reg.ABN_DECODER_PHI_E_PHI_M_OFFSET, int(decoderCountN_offset))



" ===== 4) got to encoder mode ===== "

" Feedback selection "
tmc4671.writeRegister(tmc4671_reg.PHI_E_SELECTION, tmc4671_reg.PHI_E_ABN) 
tmc4671.writeRegister(tmc4671_reg.VELOCITY_SELECTION, tmc4671_reg.VELOCITY_PHI_M_ABN)

" Switch to torque mode "
tmc4671.writeRegister(tmc4671_reg.MODE_RAMP_MODE_MOTION, tmc4671_reg.MOTION_MODE_TORQUE)



" ===== 5) make a testdrive ====="

maxVelocity = 0
minVelocity = 0

print("rotate right...")
tmc4671.writeRegister(tmc4671_reg.PID_TORQUE_FLUX_TARGET, 0x03E80000)

startTime = time.time()
while True:
    velocity = tmc4671.actualVelocity()
    print("velocity: " + str(velocity))
    if velocity > maxVelocity:
        maxVelocity = velocity
   
    " stop after 3 seconds "
    if (time.time()-startTime) > 2:
        break

print("rotate left...")
tmc4671.writeRegister(tmc4671_reg.PID_TORQUE_FLUX_TARGET, int(0xFC180000))

startTime = time.time()
while True:
    velocity = tmc4671.actualVelocity()
    print("velocity: " + str(velocity))
    if velocity < minVelocity:
        minVelocity = velocity
    
    " stop after 3 seconds "
    if (time.time()-startTime) > 2:
        break

print("stop motor")
tmc4671.writeRegister(tmc4671_reg.PID_TORQUE_FLUX_TARGET, 0)



" ===== 6) short summary ====="

print(" === summary === ")
print("abn_decoder_count_n:" + str(decoderCountN))
print("estimated encoder offset: " + str(decoderCountN_offset))
print("maxVelocity:" + str(maxVelocity))
print("minVelocity:" + str(minVelocity))

myInterface.close()