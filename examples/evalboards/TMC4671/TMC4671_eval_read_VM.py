################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Demo on how to read VM and convert the ADC value to a voltage.

16 bits map to +-2.5V, but it is not possible to measure negative voltages.
On the Eval there is a 1015/15 voltage divider. With that:
* 0 volt at the input of the eval's pin header should result in ADC value 32768 (2^15).
* ~169.17 (2.5*1015/15) volt at the input of the eval's pin header should result in ADC value 65535 (2^16 - 1).

Prior to printing the measured voltages the script does a very basic offset compensation of the analog inputs against the internal reference voltage.

Beware the ADC drift and that the ADC has more offset that cannot be compensated automatically via the below code.
And beware that the ADC should be used in its recommended operation range 50% to 75% for the single ended use case of VM.
For the TMC4671-EVAL the recommended operation range is not exceeded if voltage is kept below 80V.
"""

import time
from pytrinamic.connections import ConnectionManager
from pytrinamic.connections import UartIcInterface
from pytrinamic.evalboards import TMC4671_eval
from pytrinamic.ic import TMC4671


voltage_factor = (2.5*1015/15) / 32767

with ConnectionManager().connect() as my_interface:   # Swap with the next line if you are not using the Landungsbrueck but a USB UART cable
#with ConnectionManager("--interface uart_ic --port COM14 --data-rate 9600").connect() as my_interface:

    if isinstance(my_interface, UartIcInterface):
        # Create an TMC4671 IC class which communicates directly over UART
        tmc4671_eval = TMC4671(my_interface)
    else:
        # Create an TMC4671-EVAL class which communicate over the Landungsbrücke via TMCL
        tmc4671_eval = TMC4671_eval(my_interface)

    # Get offset error for AGPI_A, for offset compensation.
    tmc4671_eval.write_register(TMC4671.REG.ADC_RAW_ADDR, 1) # Select "ADC_AGPI_A_RAW & ADC_VM_RAW"
    tmc4671_eval.write_register_field(TMC4671.FIELD.ADC_VM, 5) # Select V5/2 -> apply reference voltage to ADC input
    vm_raw = tmc4671_eval.read_register_field(TMC4671.FIELD.ADC_VM_RAW)
    vm_offset_error = vm_raw  - (2**16)/2
    tmc4671_eval.write_register_field(TMC4671.FIELD.ADC_VM, 4) # INP vs. GND

    # Continuously print measured voltage.
    while 1:
        tmc4671_eval.write_register(TMC4671.REG.ADC_RAW_ADDR, 1) # Select "ADC_AGPI_A_RAW & ADC_VM_RAW"
        vm_raw = tmc4671_eval.read_register_field(TMC4671.FIELD.ADC_VM_RAW)
        vm_offset_corrected = vm_raw - 2**15 - vm_offset_error
        vm_voltage = voltage_factor*vm_offset_corrected

        print(f"VM: {vm_voltage:5.2f}V")
        time.sleep(0.2)
