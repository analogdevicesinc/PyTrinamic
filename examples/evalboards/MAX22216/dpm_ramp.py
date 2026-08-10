################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

"""
Example: MAX22216 controlling a 6V solenoid. Demonstrates Ramp control in VDR mode.
The MAX22216 is capable of limiting the transition between different DC_levels.
This functionality is mostly used to lower the acoustic noise of the solenoid, 
and it is intended in applications where the solenoid is near humans.

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

    # DPM with ramp disabled
    print("Testing DPM with Ramp disabled...")
    
    eval.write_register_field(MAX22216.FIELD.DC_L2H_0, 10922) # 12 V
    eval.write_register_field(MAX22216.FIELD.DC_H_0, 7282) # 8 V
    eval.write_register_field(MAX22216.FIELD.TIME_L2H_0, 10000) # 100 ms

    eval.write_register_field(MAX22216.FIELD.CNTL0, 1) # Turn the solenoid on
    time.sleep(1.0)
    eval.write_register_field(MAX22216.FIELD.CNTL0, 0) # Turn the solenoid off

    time.sleep(3.0)

    print("Testing DPM with Ramp enabled...")

    # DPM with ramp enabled
    eval.write_register_field(MAX22216.FIELD.RUPE_0, 1) # Ramp up
    eval.write_register_field(MAX22216.FIELD.RMDE_0, 1) # Ramp mid
    eval.write_register_field(MAX22216.FIELD.RDWE_0, 1) # Ramp down

    eval.write_register_field(MAX22216.FIELD.CNTL0, 1) # Turn the solenoid on
    time.sleep(1.0)
    eval.write_register_field(MAX22216.FIELD.CNTL0, 0) # Turn the solenoid off

    
print("\nDone.")