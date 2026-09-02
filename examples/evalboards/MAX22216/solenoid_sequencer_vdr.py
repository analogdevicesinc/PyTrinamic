################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

"""
Example: MAX22216 controlling a 6V solenoid. Demonstrates a two-level 
sequencer in Voltage Drive Regulation (VDR) mode. Creates a HIT period 
to open the solenoid (DC_L2H, TIME_L2H) and a HOLD period to keep it 
open (DC_H).

For more information refer to "Solenoid Sequencer Tool" in the datasheet:
[MAX22216 evaluation kit datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/max22216evkit.pdf)

Used load: 12V small door lock pull solenoid (non-polarized)
Connection: OUT0 to COM (VM+)
Power supply: 24V
"""

import time
from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import MAX22216
from pytrinamic.evalboards import MAX22216_eval

KVDR = 30.518e-6 # Voltage Drive Mode Constant
F_PWM_M = 100 # Global PWM master frequency in KHz (100KHz by default)

def calc_vdc_reg(vdc, kvdr=KVDR):
    """Convert a target DC output voltage in volts into the voltage-register value.
    The MAX22216 uses the relation VOUT = KVDR * 36 * DC_L2H[15:0]DEC.
    """
    return round(vdc / kvdr / 36)  # VOUT = KVDR x 36 x DC_L2H[15:0]DEC 

def calc_time_l2h_reg(time_l2h, fpwm=F_PWM_M):
    """Convert a time value in milliseconds into the TIME_L2H register value.
    The MAX22216 uses the relation TIME_L2H = TIME_L2H[15:0]DEC / F_PWM.
    """
    return round(time_l2h * fpwm)  # TIME_L2H = TIME_L2H[15:0]DEC/F_PWM  
    
with ConnectionManager().connect() as my_interface:

    eval = MAX22216_eval(my_interface)
    ic = eval.ics[0]
    solenoid = ic.motors[0]

    # General settings
    eval.write_register_field(MAX22216.FIELD.ACTIVE, 1) # Enable bit to activate the IC
    eval.write_register_field(MAX22216.FIELD.VDRNVDRDUTY, 1) # When set Logic High, L2H, DC_H, and DC_L registers for each channel indicate a voltage level in voltage mode.

    # Solenoid sequencer channel 0
    print("Testing Solenoid Sequencer...")
    
    eval.write_register_field(MAX22216.FIELD.DC_L2H_0, calc_vdc_reg(12)) # Sets the DC_L2H level to 12 V 
    eval.write_register_field(MAX22216.FIELD.DC_H_0, calc_vdc_reg(8)) # Sets the DC_H level to 8 V 
    eval.write_register_field(MAX22216.FIELD.TIME_L2H_0, calc_time_l2h_reg(100)) # Sets the TIME_L2H to 100 ms 

    eval.write_register_field(MAX22216.FIELD.CNTL0, 1)  # Turn the solenoid on
    time.sleep(1.0)
    eval.write_register_field(MAX22216.FIELD.CNTL0, 0)  # Turn the solenoid off

print("\nDone.")