#!/usr/bin/env python3
'''
Created on 26.02.2019

@author: ED
'''

import time
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC4671_eval import TMC4671_eval
from PyTrinamic.ic.TMC4671.TMC4671 import TMC4671 as TMC4671_IC
from PyTrinamic.connections.uart_ic_interface import uart_ic_interface

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()

if isinstance(myInterface, uart_ic_interface):
    # Create an TMC4671 IC class which communicates directly over UART
    TMC4671 = TMC4671_IC(myInterface)
else:
    # Create an TMC4671-Eval class which communicates over the Landungsbruecke via TMCL
    TMC4671 = TMC4671_eval(myInterface)

" read ChipInfo "

TMC4671.showChipInfo

" ===== 1) base configuration ====="

polePairs = 4
enocoderResolution = 4000

" Motor type &  PWM configuration "
TMC4671.writeRegister(TMC4671.registers.MOTOR_TYPE_N_POLE_PAIRS, 0x00030000 | polePairs)
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

" ABN encoder settings "
TMC4671.writeRegister(TMC4671.registers.ABN_DECODER_MODE, 0x00001000)
TMC4671.writeRegister(TMC4671.registers.ABN_DECODER_PPR, enocoderResolution)
TMC4671.writeRegister(TMC4671.registers.ABN_DECODER_COUNT, 0x0)
TMC4671.writeRegister(TMC4671.registers.ABN_DECODER_PHI_E_PHI_M_OFFSET, 0x0)

" Open loop settings "
TMC4671.writeRegister(TMC4671.registers.OPENLOOP_MODE, 0x00000000)
TMC4671.writeRegister(TMC4671.registers.OPENLOOP_ACCELERATION, 0x0000003C)

" Limits "
TMC4671.writeRegister(TMC4671.registers.PID_TORQUE_FLUX_LIMITS, 1000)

" PI settings "
TMC4671.writeRegister(TMC4671.registers.PID_TORQUE_P_TORQUE_I, 0x01000100)
TMC4671.writeRegister(TMC4671.registers.PID_FLUX_P_FLUX_I, 0x01000100)



" ===== 2) estimate the encoder offset ====="

" Init encoder (mode 0) "
" put a voltage on the motor and wait 1 second for alignment "
TMC4671.writeRegister(TMC4671.registers.MODE_RAMP_MODE_MOTION, 0x00000008)
TMC4671.writeRegister(TMC4671.registers.ABN_DECODER_PHI_E_PHI_M_OFFSET, 0x00000000)
TMC4671.writeRegister(TMC4671.registers.PHI_E_SELECTION, TMC4671.registers.PHI_E_EXTERNAL)
TMC4671.writeRegister(TMC4671.registers.PHI_E_EXT, 0x00000000)
TMC4671.writeRegister(TMC4671.registers.UQ_UD_EXT, 2000)
time.sleep(1)

" clear abn_decoder_count "
TMC4671.writeRegister(TMC4671.registers.ABN_DECODER_COUNT, 0x00000000)

print("abn_decoder_count:" + str(TMC4671.readRegister(TMC4671.registers.ABN_DECODER_COUNT)))

" Switch to open loop velocity mode "
TMC4671.writeRegister(TMC4671.registers.PHI_E_SELECTION, TMC4671.registers.PHI_E_OPEN_LOOP)
TMC4671.writeRegister(TMC4671.registers.OPENLOOP_VELOCITY_TARGET, 60)

startTime = time.time()
while True:
    print("dec: " + str(TMC4671.readRegister(TMC4671.registers.ABN_DECODER_COUNT)) + " dec_n: " + str(TMC4671.readRegister(TMC4671.registers.ABN_DECODER_COUNT_N)))

    " stop after 3 seconds "
    if (time.time()-startTime) > 3:
        break

" read encoder offset at N channel"
decoderCountN = TMC4671.readRegister(TMC4671.registers.ABN_DECODER_COUNT_N)
decoderCountN_offset = decoderCountN % (enocoderResolution / polePairs)

print("abn_decoder_count_n:" + str(decoderCountN))
print("=> estimated encoder offset: " + str(decoderCountN_offset))



" ===== 3) use the estimated offset ====="

" write offset "
TMC4671.writeRegister(TMC4671.registers.ABN_DECODER_PHI_E_PHI_M_OFFSET, int(decoderCountN_offset))



" ===== 4) got to encoder mode ===== "

" Feedback selection "
TMC4671.writeRegister(TMC4671.registers.PHI_E_SELECTION, TMC4671.registers.PHI_E_ABN)
TMC4671.writeRegister(TMC4671.registers.VELOCITY_SELECTION, TMC4671.registers.VELOCITY_PHI_M_ABN)

" Switch to torque mode "
TMC4671.writeRegister(TMC4671.registers.MODE_RAMP_MODE_MOTION, TMC4671.registers.MOTION_MODE_TORQUE)



" ===== 5) make a testdrive ====="

maxVelocity = 0
minVelocity = 0

print("rotate right...")
TMC4671.writeRegister(TMC4671.registers.PID_TORQUE_FLUX_TARGET, 0x03E80000)

startTime = time.time()
while True:
    velocity = TMC4671.readRegister(TMC4671.registers.PID_VELOCITY_ACTUAL, signed=True)
    print("velocity: " + str(velocity))
    if velocity > maxVelocity:
        maxVelocity = velocity

    " stop after 3 seconds "
    if (time.time()-startTime) > 2:
        break

print("rotate left...")
TMC4671.writeRegister(TMC4671.registers.PID_TORQUE_FLUX_TARGET, int(0xFC180000))

startTime = time.time()
while True:
    velocity = TMC4671.readRegister(TMC4671.registers.PID_VELOCITY_ACTUAL, signed=True)
    print("velocity: " + str(velocity))
    if velocity < minVelocity:
        minVelocity = velocity

    " stop after 3 seconds "
    if (time.time()-startTime) > 2:
        break

print("stop motor")
TMC4671.writeRegister(TMC4671.registers.PID_TORQUE_FLUX_TARGET, 0)


" ===== 6) short summary ====="

print(" === summary === ")
print("abn_decoder_count_n:" + str(decoderCountN))
print("estimated encoder offset: " + str(decoderCountN_offset))
print("maxVelocity:" + str(maxVelocity))
print("minVelocity:" + str(minVelocity))

myInterface.close()