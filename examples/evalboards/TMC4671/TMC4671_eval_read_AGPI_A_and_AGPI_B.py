################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Demo on how to read general purpose input A (AGPI_A) and B (AGPI_B) and convert the ADC value to a voltage.

16 bits map to +-2.5V, but it is not possible to measure negative voltages.
On the Eval there is a 5/1 voltage divider. With that:
* 0 volt at the input of the eval's pin header should result in ADC value 32768 (2^15).
* 12.5 (2.5*5) volt at the input of the eval's pin header should result in ADC value 65535 (2^16 - 1).

Prior to printing the measured voltages the script does a very basic offset compensation of the analog inputs against the internal reference voltage.

Beware the ADC drift and that the ADC has more offset that cannot be compensated automatically via the below code.
And beware that the ADC should be used in its recommended operation range 50% to 75% for the single ended use case of AGPI_A and AGPI_B.
For the TMC4671-EVAL with its 5/1 voltage divider at the AGPIs the recommended operation range would be 0V to 9.375V, where 12.5V is the maximum.
"""

import time
from pytrinamic.connections import ConnectionManager
from pytrinamic.connections import UartIcInterface
from pytrinamic.evalboards import TMC4671_eval
from pytrinamic.ic import TMC4671


voltage_factor = 12.5 / 32767

with ConnectionManager().connect() as my_interface:   # Swap with the next line if you are not using the Landungsbrueck but a USB UART cable
#with ConnectionManager("--interface uart_ic --port COM14 --data-rate 9600").connect() as my_interface:

    if isinstance(my_interface, UartIcInterface):
        # Create an TMC4671 IC class which communicates directly over UART
        tmc4671_eval = TMC4671(my_interface)
    else:
        # Create an TMC4671-EVAL class which communicate over the Landungsbrücke via TMCL
        tmc4671_eval = TMC4671_eval(my_interface)
    
    tmc4671_eval.write_register(TMC4671.REG.dsADC_MCLK_B, 0x2000_0000)  # This is needed to get AGPI_B running

    # Get offset error for AGPI_A, for offset compensation.
    tmc4671_eval.write_register(TMC4671.REG.ADC_RAW_ADDR, 1) # Select "ADC_AGPI_A_RAW & ADC_VM_RAW"
    tmc4671_eval.write_register_field(TMC4671.FIELD.ADC_AGPI_A, 5) # Select V5/2 -> apply reference voltage to ADC input
    agpi_a_raw = tmc4671_eval.read_register_field(TMC4671.FIELD.ADC_AGPI_A_RAW)
    agpi_a_offset_error = agpi_a_raw  - (2**16)/2
    tmc4671_eval.write_register_field(TMC4671.FIELD.ADC_AGPI_A, 4) # INP vs. GND
    # Get offset error for AGPI_B, for offset compensation.
    tmc4671_eval.write_register(TMC4671.REG.ADC_RAW_ADDR, 2) # Select "ADC_AENC_UX_RAW & ADC_AGPI_B_RAW"
    tmc4671_eval.write_register_field(TMC4671.FIELD.ADC_AGPI_B, 5) # Select V5/2 -> apply reference voltage to ADC input
    agpi_b_raw = tmc4671_eval.read_register_field(TMC4671.FIELD.ADC_AGPI_B_RAW)
    agpi_b_offset_error = agpi_b_raw  - (2**16)/2
    tmc4671_eval.write_register_field(TMC4671.FIELD.ADC_AGPI_B, 4) # INP vs. GND

    # Continuously print measured voltages.
    while 1:
        tmc4671_eval.write_register(TMC4671.REG.ADC_RAW_ADDR, 1) # Select "ADC_AGPI_A_RAW & ADC_VM_RAW"
        agpi_a_raw = tmc4671_eval.read_register_field(TMC4671.FIELD.ADC_AGPI_A_RAW)
        agpi_a_offset_corrected = agpi_a_raw - 2**15 - agpi_a_offset_error
        agpi_a_voltage = voltage_factor*agpi_a_offset_corrected

        tmc4671_eval.write_register(TMC4671.REG.ADC_RAW_ADDR, 2) # Select "ADC_AENC_UX_RAW & ADC_AGPI_B_RAW"
        agpi_b_raw = tmc4671_eval.read_register_field(TMC4671.FIELD.ADC_AGPI_B_RAW)
        agpi_b_offset_corrected = agpi_b_raw - 2**15 - agpi_b_offset_error
        agpi_b_voltage = voltage_factor*agpi_b_offset_corrected

        print(f"AGPI_A: {agpi_a_voltage:5.2f}V | AGPI_B: {agpi_b_voltage:5.2f}V")
        time.sleep(0.2)
