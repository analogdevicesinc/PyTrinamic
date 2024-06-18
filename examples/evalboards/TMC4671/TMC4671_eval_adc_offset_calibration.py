################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import time
import numpy as np
import matplotlib.pyplot as plt

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.connections import UartIcInterface
from pytrinamic.evalboards import TMC4671_eval
from pytrinamic.ic import TMC4671

pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
#with ConnectionManager("--interface uart_ic --port COM14 --data-rate 9600").connect() as my_interface:  # Swap with previous line if you are not using the Landungsbrueck but a USB UART cable

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

    # Configure TMC4671 for a BLDC motor in open loop mode

    # Motor type &  PWM configuration
    eval_board.write_register_field(mc.FIELD.MOTOR_TYPE, mc.ENUM.MOTOR_TYPE_BLDC)
    eval_board.write_register_field(mc.FIELD.N_POLE_PAIRS, 4)
    eval_board.write_register(mc.REG.PWM_POLARITIES, 0x00000000)
    eval_board.write_register(mc.REG.PWM_MAXCNT, int(0x00000F9F))
    eval_board.write_register(mc.REG.PWM_BBM_H_BBM_L, 0x00000505)
    eval_board.write_register_field(mc.FIELD.PWM_CHOP, mc.ENUM.PWM_CENTERED_FOR_FOC)
    eval_board.write_register_field(mc.FIELD.PWM_SV, 1)

    # ADC configuration
    eval_board.write_register(mc.REG.ADC_I_SELECT, 0x18000100)
    eval_board.write_register(mc.REG.dsADC_MCFG_B_MCFG_A, 0x00100010)
    eval_board.write_register(mc.REG.dsADC_MCLK_A, 0x20000000)
    eval_board.write_register(mc.REG.dsADC_MCLK_B, 0x00000000)
    eval_board.write_register(mc.REG.dsADC_MDEC_B_MDEC_A, int(0x014E014E))
    eval_board.write_register(mc.REG.ADC_I0_SCALE_OFFSET, 0x01008218)
    eval_board.write_register(mc.REG.ADC_I1_SCALE_OFFSET, 0x0100820A)

    # Switch to stopped mode
    eval_board.write_register(mc.REG.MODE_RAMP_MODE_MOTION, mc.ENUM.MOTION_MODE_STOPPED)

    # Feedback selection
    eval_board.write_register(mc.REG.PHI_E_SELECTION, mc.ENUM.PHI_E_EXTERNAL)
    eval_board.write_register(mc.REG.PHI_E_EXT, 0)
    eval_board.write_register(mc.REG.UQ_UD_EXT, 0)

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
    eval_board.write_register(mc.REG.ADC_RAW_ADDR, 0)

    while (time.time() - startTime) <= measurementTime:
        measurements += 1

        # Read adc values
        adc_i0 = eval_board.read_register_field(mc.FIELD.ADC_I0_RAW)
        adc_i1 = eval_board.read_register_field(mc.FIELD.ADC_I1_RAW)
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
        eval_board.write_register_field(mc.FIELD.ADC_I0_OFFSET, int(adcI0Mean))
        eval_board.write_register_field(mc.FIELD.ADC_I1_OFFSET, int(adcI1Mean))
    
        " read offsets "
        lAdcI0Offset.append(eval_board.read_register_field(mc.FIELD.ADC_I0_OFFSET))
        lAdcI1Offset.append(eval_board.read_register_field(mc.FIELD.ADC_I1_OFFSET))

        print("ADC_I0_Offset: %d" % eval_board.read_register_field(mc.FIELD.ADC_I0_OFFSET))
        print("ADC_I1_Offset: %d" % eval_board.read_register_field(mc.FIELD.ADC_I1_OFFSET))

    my_interface.close()
    print("ready.")

    # plot the data
    t = np.arange(0., measurements, 1.0)
    plt.plot(t, lAdcI0Raw, 'r--', label='I0_Raw')
    plt.plot(t, lAdcI0Offset, 'r-', label='I0_Offset')
    plt.plot(t, lAdcI1Raw, 'b--', label='I1_Raw')
    plt.plot(t, lAdcI1Offset, 'b-', label='I1_Offset')
    plt.legend(loc='best')
    plt.show()
