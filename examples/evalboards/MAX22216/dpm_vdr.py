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

import time
from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import MAX22216
from pytrinamic.evalboards import MAX22216_eval

KVDR = 30.518e-6 # Voltage Drive Mode Constant
F_PWM_M = 100e3 # Global PWM master frequency (100KHz)

def calc_vdc_reg(vdc, kvdr=KVDR):
    """Convert a target DC output voltage into the voltage-register value.
    The MAX22216 uses the relation VOUT = KVDR * 36 * DC_L2H[15:0]DEC for the
    output waveform level.
    """
    return round(vdc / kvdr / 36)  # VOUT = KVDR x 36 x DC_L2H[15:0]DEC 

def calc_time_l2h_reg(time_l2h, fpwm=F_PWM_M):
    """Convert a time value into the TIME_L2H register value.
    The register value is defined as TIME_L2H = TIME_L2H[15:0]DEC / F_PWM.
    """
    return round(time_l2h * fpwm)  # TIME_L2H = TIME_L2H[15:0]DEC/F_PWM  

with ConnectionManager().connect() as my_interface:

    eval = MAX22216_eval(my_interface)
    ic = eval.ics[0]
    solenoid = ic.motors[0]

    # General settings
    eval.write_register_field(MAX22216.FIELD.ACTIVE, 1) # Enable bit to activate the IC
    eval.write_register_field(MAX22216.FIELD.VDR_NDUTY, 1) # When set Logic High, L2H, DC_H, and DC_L registers for each channel indicate a voltage level in voltage mode. 

    # DPM 
    print("Testing DPM in normal state...")
    eval.write_register_field(MAX22216.FIELD.DPM0, 1) # Clear flag
    eval.write_register_field(MAX22216.FIELD.DC_L2H_0, calc_vdc_reg(12)) # Sets the DC_L2H level to 12 V 
    eval.write_register_field(MAX22216.FIELD.DC_H_0, calc_vdc_reg(8)) # Sets the DC_H level to 8 V 
    eval.write_register_field(MAX22216.FIELD.TIME_L2H_0, calc_time_l2h_reg(100)) # Sets the TIME_L2H to 100 ms 

    # Configuring DPM Settings
    eval.write_register_field(MAX22216.FIELD.DPM_EN_0, 1) # Enable DPM 
    eval.write_register_field(MAX22216.FIELD.DPM_MIN_CURRENT_0, 4) # Sets DPM_START to 260.35 mA (Register Value: 4)
    eval.write_register_field(MAX22216.FIELD.DPM_THLD_0, 50) # Sets DPM_THLD to 406.8 mA (Register Value: 50)

    eval.write_register_field(MAX22216.FIELD.CNTL0, 1) # Turn the solenoid on
    time.sleep(1.0)
    eval.write_register_field(MAX22216.FIELD.CNTL0, 0) # Turn the solenoid off

    # Read the flag status
    DPM0_FAULT = eval.read_register_field(MAX22216.FIELD.DPM0)
    print(f"DPM0_FAULT: {DPM0_FAULT}") # This should read zero

    time.sleep(2.0)

    print("Enabling END_HIT_AUTO")
    eval.write_register_field(MAX22216.FIELD.END_HIT_AUTO_0, 1) # Enable END_HIT_AUTO

    # Setting STAT0 pin as DPM alarm. When the DPM is detected, the STAT0 pin is LOW. 
    eval.write_register_field(MAX22216.FIELD.STAT_FUN, 3) # Set the STAT function to DPM
    eval.write_register_field(MAX22216.FIELD.STAT_SEL0, 1) # Connects the STAT0 pin to the internal STAT1 function
    eval.write_register_field(MAX22216.FIELD.STAT_POL, 1) # STAT pin outputs LOW when the function is triggered

    # Creating a DPM fault to activate the flag
    print("Testing DPM in error state...")
    eval.write_register_field(MAX22216.FIELD.DC_L2H_0, calc_vdc_reg(8)) # Sets the DC_L2H level to 8 V (Register Value: 7282)
    eval.write_register_field(MAX22216.FIELD.DC_H_0, calc_vdc_reg(2)) # Sets the DC_H level to 2 V. This voltage is not high enough to hold the solenoid, and it will activate the DPM fault flag.
    eval.write_register_field(MAX22216.FIELD.TIME_L2H_0, calc_time_l2h_reg(50)) # This has no effect as it is overwritten by END_HIT_AUTO

    eval.write_register_field(MAX22216.FIELD.CNTL0, 1)
    time.sleep(1.0)
    eval.write_register_field(MAX22216.FIELD.CNTL0, 0)

    # Read the flag status
    DPM0_FAULT = eval.read_register_field(MAX22216.FIELD.DPM0)
    print(f"DPM0_FAULT: {DPM0_FAULT}") # This should read one
    
print("\nDone.")