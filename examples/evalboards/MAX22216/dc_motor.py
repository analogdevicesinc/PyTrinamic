################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

"""
Example: MAX22216 controlling a brushed DC motor.

In this example setup, the MAX22216 drives a 12 V brushed DC motor. The MAX22216 has a special drive mode in which
the output is driven with a set voltage (DC_H), while a current limit is applied using DC_L2H. Brushed DC motors have
a large inrush current at startup, and their current consumption increases with motor load. The current limiter should
be set above the motor's maximum current consumption under load. The motor mode also has a brake feature (TIME_L2H):
when both channels of the full-bridge configuration are set to output, the MAX22216 forces a set current in the
opposite direction of the previous current flow, which stops the motor.

The STAT function can be set to monitor the measured current and flag when it goes above a set threshold.

For more information refer to "Setup Example: DC Motor" in the datasheet:
[MAX22216 evaluation kit datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/max22216evkit.pdf)

Used load: 12 V brushed DC motor
Setup: Load between OUT0OUT1 and OUT2OUT3
Power supply: 24 V
"""

import time
from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import MAX22216
from pytrinamic.evalboards import MAX22216_eval

KVDR = 30.518e-6 # Voltage Drive Mode Constant
F_PWM_M = 100e3 # Global PWM master frequency (100KHz)

GAIN = 1 # current measurement scaling factor
SNSF = 1 # Sense-scaling factor
KCDR = 1.017 # Current Drive Regulation Constant

def calc_vdc_reg(vdc, kvdr=KVDR):
    """Convert a target DC output voltage given in volts into the voltage-register value.
    The MAX22216 uses the relation VOUT = KVDR * 36 * DC_L2H[15:0]DEC.
    """
    return round(vdc / kvdr / 36)  # VOUT = KVDR x 36 x DC_L2H[15:0]DEC 

def calc_idc_reg(idc, kcdr=KCDR, gain = GAIN, snsf = SNSF):
    """Convert a target DC output current given in mA into the current-register value.
    The MAX22216 uses the relation IOUT = KCDR x GAIN x SNSF x DC_L2H[15:0]DEC.
    """
    return round(idc / kcdr / gain / snsf)  # IOUT = KCDR x GAIN x SNSF x DC_L2H[15:0]DEC 
    
with ConnectionManager().connect() as my_interface:

    eval = MAX22216_eval(my_interface)
    ic = eval.ics[0]
    solenoid = ic.motors[0]

    # General settings
    eval.write_register_field(MAX22216.FIELD.ACTIVE, 1) # Enable bit to activate the IC
    eval.write_register_field(MAX22216.FIELD.VDRNVDRDUTY, 1) # Internal voltage regulator for the voltage output
    eval.write_register_field(MAX22216.FIELD.CHS, 8) # Parallel full-bridge configuration

    # Solenoid sequencer channel 0
    eval.write_register_field(MAX22216.FIELD.DC_H_0, calc_vdc_reg(12)) # Sets the DC_H level to 12 V
    eval.write_register_field(MAX22216.FIELD.DC_L2H_0, calc_idc_reg(300)) # Sets the current limiter to 300 mA
    eval.write_register_field(MAX22216.FIELD.TIME_L2H_0, calc_idc_reg(100)) # Sets the brake current to 100 mA
    eval.write_register_field(MAX22216.FIELD.CTRL_MODE_0, 2) # Sets the control mode to DC motor drive

    # Setting P & I values initially to 1000, but it can be adjusted after further testing. 
    # Tuning the P_I values can be done using the "BEMF/DPM tuning tool" or the “Parameter & Register Scope” in the TMCL-IDE 
    eval.write_register_field(MAX22216.FIELD.CFG_P_0, 1000) # P value
    eval.write_register_field(MAX22216.FIELD.CFG_I_0, 1000) # I value 

    # Setting the STAT current observer
    eval.write_register_field(MAX22216.FIELD.STAT_FUN, 5) # Sets to 5:I_DC, which monitors the current and triggers an alarm if the current is higher than a set current threshold (IDC_THLD). 
    eval.write_register_field(MAX22216.FIELD.IDC_THLD_0, calc_idc_reg(295)) # IDC_THLD is compared directly to I_MONITOR. In this example, the alarm is set to 295 mA.
    eval.write_register_field(MAX22216.FIELD.IDC_THLD_1, calc_idc_reg(295)) # In full-bridge mode, the registers related to the STAT alarm configuration must be set on both channels.

    eval.write_register_field(MAX22216.FIELD.CNTL0, 1)  # Turn the solenoid on

    time.sleep(3.0)

    # Use the brake of the DC motor drive
    eval.write_register_field(MAX22216.FIELD.CNTL1, 1)  # Both channels are set to HIGH (CNTL0 and CNTL1) and the MAX22216 creates a negative 100mA output on the line to stop the motor.  

print("\nDone.")