################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

"""
Example: MAX22216 controlling a 6V solenoid. Demonstrates the Open load
detection feature.

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

    # Solenoid Sequencer Settings
    eval.write_register_field(MAX22216.FIELD.DC_L2H_0, 10922) # 12 V
    eval.write_register_field(MAX22216.FIELD.DC_H_0, 7282) # 8 V
    eval.write_register_field(MAX22216.FIELD.TIME_L2H_0, 10000) # 100 ms

    eval.write_register_field(MAX22216.FIELD.CNTL0, 1) # Turn the solenoid on
    time.sleep(1.0)
    eval.write_register_field(MAX22216.FIELD.CNTL0, 0) # Turn the solenoid off

    # Open-load detection
    eval.write_register_field(MAX22216.FIELD.OL_EN_0, 1) # Enable open load detection

    print("Remove the solenoid and then press enter!")

    input()
    eval.write_register_field(MAX22216.FIELD.CNTL0, 1)
    time.sleep(1.0)
    eval.write_register_field(MAX22216.FIELD.CNTL0, 0)
    
    # Read the flag status
    OLF0_FAULT = eval.read_register_field(MAX22216.FIELD.OLF0)
    print(f"OLF0_FAULT: {OLF0_FAULT}") # This should read one
    
print("\nDone.")