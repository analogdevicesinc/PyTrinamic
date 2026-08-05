################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

"""
Example: MAX22216 controlling a 6V solenoid. Demonstrates detection of plunger movement
(DPM) with automatic transition to HOLD current while operating in Voltage Drive
Regulation (VDR) mode. It also demonstrates internal selectable STAT alarms that can be set to output 
a digital signal on the STAT1 pin.

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

    # DPM 
    print("Testing DPM in normal state...")
    eval.write_register_field(MAX22216.FIELD.DPM0, 1) # Clear flag
    eval.write_register_field(MAX22216.FIELD.DC_L2H_0, 10922) # 12 V
    eval.write_register_field(MAX22216.FIELD.DC_H_0, 7282) # 8 V
    eval.write_register_field(MAX22216.FIELD.TIME_L2H_0, 10000) # 100 ms

    # Configuring DPM Settings
    eval.write_register_field(MAX22216.FIELD.DPM_EN_0, 1) # Enable DPM 
    eval.write_register_field(MAX22216.FIELD.DPM_MIN_CURRENT_0, 4) # 260.35 mA
    eval.write_register_field(MAX22216.FIELD.DPM_THLD_0, 50) # 406.8 mA

    eval.write_register_field(MAX22216.FIELD.CNTL0, 1) # Turn the solenoid on
    time.sleep(1.0)
    eval.write_register_field(MAX22216.FIELD.CNTL0, 0) # Turn the solenoid off

    # Read the flag status
    DPM0_FAULT = eval.read_register_field(MAX22216.FIELD.DPM0)
    print(f"DPM0_FAULT: {DPM0_FAULT}") # This should read zero

    time.sleep(2.0)

    print("Enabling END_HIT_AUTO")
    eval.write_register_field(MAX22216.FIELD.END_HIT_AUTO_0, 1)

    # Setting STAT0 pin as DPM alarm. When the DPM is detected, the STAT0 pin is LOW. 
    eval.write_register_field(MAX22216.FIELD.STAT_FUN, 3) # Set the STAT function to DPM
    eval.write_register_field(MAX22216.FIELD.STAT_SEL0, 1) # Connects the STAT0 pin to the internal STAT1 function
    eval.write_register_field(MAX22216.FIELD.STAT_POL, 1) # STAT pin outputs LOW when the function is triggered

    # Creating a DPM fault to activate the flag
    print("Testing DPM in error state...")
    eval.write_register_field(MAX22216.FIELD.DC_L2H_0, 7282) # 8 V
    eval.write_register_field(MAX22216.FIELD.DC_H_0, 1820) # 2 V
    eval.write_register_field(MAX22216.FIELD.TIME_L2H_0, 5000) # This has no effect as it is overwritten by END_HIT_AUTO

    eval.write_register_field(MAX22216.FIELD.CNTL0, 1)
    time.sleep(1.0)
    eval.write_register_field(MAX22216.FIELD.CNTL0, 0)

    # Read the flag status
    DPM0_FAULT = eval.read_register_field(MAX22216.FIELD.DPM0)
    print(f"DPM0_FAULT: {DPM0_FAULT}") # This should read one
    
print("\nDone.")