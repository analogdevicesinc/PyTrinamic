import time
import numpy as np
import matplotlib.pyplot as plt

import pytrinamic2
from pytrinamic2.connections.connection_manager import ConnectionManager
from pytrinamic2.evalboards import TMC4671_eval
from pytrinamic2.ic import TMC4671 as TMC4671_IC

pytrinamic2.show_info()

myInterface = ConnectionManager().connect()
print(myInterface)

if myInterface.supports_tmcl():
    # Create an TMC4671-Eval class which communicates over the Landungsbrücke via TMCL
    TMC4671 = TMC4671_eval(myInterface)
else:
    # Create an TMC4671 IC class which communicates directly with the IC over UART
    TMC4671 = TMC4671_IC(myInterface)

with myInterface:

    # Configure TMC4671 for a BLDC motor in open loop mode

    # Motor type &  PWM configuration
    TMC4671.write_register_field(TMC4671.fields.MOTOR_TYPE, TMC4671.ENUMs.MOTOR_TYPE_BLDC)
    TMC4671.write_register_field(TMC4671.fields.N_POLE_PAIRS, 4)
    TMC4671.write_register(TMC4671.registers.PWM_POLARITIES, 0x00000000)
    TMC4671.write_register(TMC4671.registers.PWM_MAXCNT, int(0x00000F9F))
    TMC4671.write_register(TMC4671.registers.PWM_BBM_H_BBM_L, 0x00000505)
    TMC4671.write_register_field(TMC4671.fields.PWM_CHOP, TMC4671.ENUMs.PWM_CENTERED_FOR_FOC)
    TMC4671.write_register_field(TMC4671.fields.PWM_SV, 1)

    # ADC configuration
    TMC4671.write_register(TMC4671.registers.ADC_I_SELECT, 0x18000100)
    TMC4671.write_register(TMC4671.registers.dsADC_MCFG_B_MCFG_A, 0x00100010)
    TMC4671.write_register(TMC4671.registers.dsADC_MCLK_A, 0x20000000)
    TMC4671.write_register(TMC4671.registers.dsADC_MCLK_B, 0x00000000)
    TMC4671.write_register(TMC4671.registers.dsADC_MDEC_B_MDEC_A, int(0x014E014E))
    TMC4671.write_register(TMC4671.registers.ADC_I0_SCALE_OFFSET, 0x01008218)
    TMC4671.write_register(TMC4671.registers.ADC_I1_SCALE_OFFSET, 0x0100820A)

    # Switch to stopped mode
    TMC4671.write_register(TMC4671.registers.MODE_RAMP_MODE_MOTION, TMC4671.ENUMs.MOTION_MODE_STOPPED)

    # Feedback selection
    TMC4671.write_register(TMC4671.registers.PHI_E_SELECTION, TMC4671.ENUMs.PHI_E_EXTERNAL)
    TMC4671.write_register(TMC4671.registers.PHI_E_EXT, 0)
    TMC4671.write_register(TMC4671.registers.UQ_UD_EXT, 0)

    print("Start calibration...")

    # calibrate_adc_offsets
    measurementTime = 2.0
    measurements = 0

    lAdcI0Raw = list()
    lAdcI0Filt = list()
    lAdcI0Offset = list()

    lAdcI1Raw = list()
    lAdcI1Filt = list()
    lAdcI1Offset = list()

    startTime = time.time()

    # select the use of ADC_RAW in ADC_RAW_DATA
    TMC4671.write_register(TMC4671.registers.ADC_RAW_ADDR, 0)

    while (time.time() - startTime) <= measurementTime:
        measurements += 1

        # Read adc values
        adc_i0 = TMC4671.read_register_field(TMC4671.fields.ADC_I0_RAW)
        adc_i1 = TMC4671.read_register_field(TMC4671.fields.ADC_I1_RAW)
        print("ADC_I0_Value: %d" % adc_i0)
        print("ADC_I1_Value: %d" % adc_i1)
        lAdcI0Raw.append(adc_i0)
        lAdcI1Raw.append(adc_i1)
    
        # filter offsets
        adcI0Mean = np.mean(lAdcI0Raw)
        lAdcI0Filt.append(adcI0Mean)
        adcI1Mean = np.mean(lAdcI1Raw)
        lAdcI1Filt.append(adcI1Mean)

        # update offsets
        TMC4671.write_register_field(TMC4671.fields.ADC_I0_OFFSET, int(adcI0Mean))
        TMC4671.write_register_field(TMC4671.fields.ADC_I1_OFFSET, int(adcI1Mean))
    
        " read offsets "
        lAdcI0Offset.append(TMC4671.read_register_field(TMC4671.fields.ADC_I0_OFFSET))
        lAdcI1Offset.append(TMC4671.read_register_field(TMC4671.fields.ADC_I1_OFFSET))

        print("ADC_I0_Offset: %d" % TMC4671.read_register_field(TMC4671.fields.ADC_I0_OFFSET))
        print("ADC_I1_Offset: %d" % TMC4671.read_register_field(TMC4671.fields.ADC_I1_OFFSET))

    myInterface.close()
    print("ready.")

    # plot the data
    t = np.arange(0., measurements, 1.0)
    plt.plot(t, lAdcI0Raw, 'r--', label='I0_Raw')
    plt.plot(t, lAdcI0Offset, 'r-', label='I0_Offset')
    plt.plot(t, lAdcI1Raw, 'b--', label='I1_Raw')
    plt.plot(t, lAdcI1Offset, 'b-', label='I1_Offset')
    plt.legend(loc='best')
    plt.show()
