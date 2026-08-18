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

import time
from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import MAX22216
from pytrinamic.evalboards import MAX22216_eval

F_PWM_M = 100e3 # Global PWM master frequency (100KHz)
GAIN = 1 # current measurement scaling factor
SNSF = 1 # Sense-scaling factor
KCDR = 1.017 # Current Drive Regulation Constant

def calc_idc_reg(idc, kcdr=KCDR, gain = GAIN, snsf = SNSF):
    """Convert a target DC output current into the current-register value.
    The MAX22216 uses the relation IOUT = KCDR x GAIN x SNSF x DC_L2H[15:0]DEC
    for the output waveform level.
    """
    return round(idc / kcdr / gain / snsf)  # IOUT = KCDR x GAIN x SNSF x DC_L2H[15:0]DEC 

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

    # Solenoid sequencer channel 0
    print("Testing Solenoid Sequencer...")

    eval.write_register_field(MAX22216.FIELD.CTRL_MODE_0, 1) # CDR mode

    eval.write_register_field(MAX22216.FIELD.DC_L2H_0, calc_idc_reg(500)) # Sets the DC_L2H level to 500 mA
    eval.write_register_field(MAX22216.FIELD.DC_H_0, calc_idc_reg(250)) # Sets the DC_H level to 250 mA
    eval.write_register_field(MAX22216.FIELD.TIME_L2H_0, calc_time_l2h_reg(100)) # Sets the TIME_L2H to 100 ms

    eval.write_register_field(MAX22216.FIELD.CFG_P_0, 800) # P value
    eval.write_register_field(MAX22216.FIELD.CFG_I_0, 20) # I value 

    eval.write_register_field(MAX22216.FIELD.CNTL0, 1)  # Turn the solenoid on
    time.sleep(1.0)
    eval.write_register_field(MAX22216.FIELD.CNTL0, 0)  # Turn the solenoid off

print("\nDone.")