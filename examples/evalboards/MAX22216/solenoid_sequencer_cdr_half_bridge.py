################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

"""
Example: MAX22216 controlling a 6V solenoid. Demonstrates a two-level 
sequencer in Current Drive Regulation (VDR) mode. Creates a HIT period 
to open the solenoid (DC_L2H, TIME_L2H) and a HOLD period to keep it 
open (DC_H). P and I values must be set for the PI current regulator 
(if no values are set, the controller does not start). 

Used load: 12V small door lock pull solenoid (non-polarized)
Connection: OUT0 to COM (VM+)
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

    # Solenoid sequencer channel 0
    print("Testing Solenoid Sequencer...")

    eval.write_register_field(MAX22216.FIELD.CTRL_MODE, 1) # CDR mode

    eval.write_register_field(MAX22216.FIELD.DC_L2H_0, 492) # 500.36 mA
    eval.write_register_field(MAX22216.FIELD.DC_H_0, 246) # 250.18 V
    eval.write_register_field(MAX22216.FIELD.TIME_L2H_0, 10000) # 100 ms

    eval.write_register_field(MAX22216.FIELD.CFG_P_0, 800) # P value
    eval.write_register_field(MAX22216.FIELD.CFG_I_0, 20) # I value 

    eval.write_register_field(MAX22216.FIELD.CNTL0, 1)  # Turn the solenoid on
    time.sleep(1.0)
    eval.write_register_field(MAX22216.FIELD.CNTL0, 0)  # Turn the solenoid off


print("\nDone.")