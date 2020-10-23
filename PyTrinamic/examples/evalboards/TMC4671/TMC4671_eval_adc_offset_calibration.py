#!/usr/bin/env python3
'''
Created on 22.07.2020

@author: ED
'''
if __name__ == '__main__':
    pass

import time
import numpy as np
import matplotlib.pyplot as plt

from PyTrinamic.connections.ConnectionManagerPC import ConnectionManagerPC
from PyTrinamic.evalboards.TMC4671_eval import TMC4671_eval
from PyTrinamic.ic.TMC4671.TMC4671 import TMC4671 as TMC4671_IC

myInterface = ConnectionManagerPC(interfaces=["usb_tmcl"]).connect()[0]

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

" Switch to stopped mode "
TMC4671.writeRegister(TMC4671.registers.MODE_RAMP_MODE_MOTION, TMC4671.registers.MOTION_MODE_STOPPED)

" Feedback selection "
TMC4671.writeRegister(TMC4671.registers.PHI_E_SELECTION, TMC4671.registers.PHI_E_EXTERNAL)
TMC4671.writeRegister(TMC4671.registers.PHI_E_EXT, 0)
TMC4671.writeRegister(TMC4671.registers.UQ_UD_EXT, 0)

print("start calibration...")

" calibrate_adc_offsets "
measurementTime = 2.0
measurements = 0

lAdcI0Raw = list()
lAdcI0Filt = list()
lAdcI0Offset = list()

lAdcI1Raw = list()
lAdcI1Filt = list()
lAdcI1Offset = list()

startTime = time.time()
TMC4671.writeRegister(TMC4671.registers.ADC_RAW_ADDR, 0)

while ((time.time() - startTime) <= measurementTime):
    measurements += 1

    " read adc values "
    adc_i0 = TMC4671.readRegisterField(TMC4671.fields.ADC_I0_RAW)
    adc_i1 = TMC4671.readRegisterField(TMC4671.fields.ADC_I1_RAW)
    #print("ADC_I0_Value: %d" % adc_i0)
    #print("ADC_I1_Value: %d" % adc_i1)
    lAdcI0Raw.append(adc_i0)
    lAdcI1Raw.append(adc_i1)

    " filter offsets "
    adcI0Mean = np.mean(lAdcI0Raw)
    lAdcI0Filt.append(adcI0Mean)
    adcI1Mean = np.mean(lAdcI1Raw)
    lAdcI1Filt.append(adcI1Mean)

    " update offsets "
    TMC4671.writeRegisterField(TMC4671.fields.ADC_I0_OFFSET, int(adcI0Mean))
    TMC4671.writeRegisterField(TMC4671.fields.ADC_I1_OFFSET, int(adcI1Mean))

    " read offsets "
    lAdcI0Offset.append(TMC4671.readRegisterField(TMC4671.fields.ADC_I0_OFFSET))
    lAdcI1Offset.append(TMC4671.readRegisterField(TMC4671.fields.ADC_I1_OFFSET))

print("ADC_I0_Offset: %d" % TMC4671.readRegisterField(TMC4671.fields.ADC_I0_OFFSET))
print("ADC_I1_Offset: %d" % TMC4671.readRegisterField(TMC4671.fields.ADC_I1_OFFSET))

myInterface.close()
print("ready.")

" plot the data "
t = np.arange(0., measurements, 1.0)
plt.plot(t, lAdcI0Raw, 'r--', label='I0_Raw')
plt.plot(t, lAdcI0Offset, 'r-', label='I0_Offset')
plt.plot(t, lAdcI1Raw, 'b--', label='I1_Raw')
plt.plot(t, lAdcI1Offset, 'b-', label='I1_Offset')
plt.legend(loc='best')
plt.show()
