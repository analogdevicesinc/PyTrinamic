################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

"""
Example: MAX22216 controlling a 6V solenoid. CH0CH1 Full-Bridge/CDR/One-Level Control. 
In this example, a solenoid is connected between Channel 0 and Channel 1, and it is 
controlled using a constant current. 

Used load: 12V small door lock pull solenoid (non-polarized)
Connection: OUT0 --- Solenoid --- OUT1
Power supply: 24V
"""

import logging
import time

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import MAX22216
from pytrinamic.evalboards import MAX22216_eval

pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
    print(my_interface)

    eval = MAX22216_eval(my_interface)
    ic = eval.ics[0]
    solenoid = ic.motors[0]

    # General settings
    eval.write_register_field(MAX22216.FIELD.ACTIVE, 1)
    eval.write_register_field(MAX22216.FIELD.VDR_NDUTY, 1)
    eval.write_register_field(MAX22216.FIELD.CHS, 5) # 2x independent full-bridges (CH0CH1 and CH2CH3)

    # Solenoid sequencer channel 0
    print("Testing Solenoid Sequencer...")

    eval.write_register_field(MAX22216.FIELD.CTRL_MODE, 1) # CDR mode

    eval.write_register_field(MAX22216.FIELD.DC_L2H_0, 492) # 500.36 mA

    eval.write_register_field(MAX22216.FIELD.CFG_P_0, 2000) # P value
    eval.write_register_field(MAX22216.FIELD.CFG_I_0, 10) # I value 

    eval.write_register_field(MAX22216.FIELD.CNTL0, 1)  # Turn the solenoid on
    time.sleep(2.0)
    eval.write_register_field(MAX22216.FIELD.CNTL0, 0)  # Turn the solenoid off


print("\nDone.")