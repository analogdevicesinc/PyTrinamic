################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

"""
Example: MAX22216 controlling a 6V solenoid. Demonstrates the
inductance measurement feautre of MAX22216.

For more information refer to "Solenoid Inductance Tool" in the datasheet:
[MAX22216 evaluation kit datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/max22216evkit.pdf)

Used load: 12V small door lock pull solenoid (non-polarized)
Connection: OUT0 to COM (VM+)
Power supply: 24V
"""

import math
import time
from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import MAX22216
from pytrinamic.evalboards import MAX22216_eval

KVDR = 30.518e-6 # Voltage Drive Mode Constant 
U_AC = 3 # Amplitude of the internally generated ac signal (3V)

F_PWM_M = 100e3 # Global PWM master frequency (100KHz)
F_AC = 1000 # Frequency of the internally generated ac signal (1000Hz)

GAIN = 1 # current measurement scaling factor
SNSF = 1 # Sense-scaling factor
KCDR = 1.017 # Current Drive Regulation Constant

def calc_u_ac_scan(u_ac, kvdr=KVDR):
    """Convert a target AC voltage into the register value used by the IC.
    The MAX22216 encodes the internally generated AC amplitude as a scaled
    digital value according to: U_AC = KVDR * 36 * U_AC_SCAN.
    """
    return round(u_ac / (36 * kvdr))  # U_AC = KVDR * 36 * U_AC_SCAN

def calc_f_ac_scan(f_ac, f_pwm_m=F_PWM_M):
    """Convert an AC signal frequency into the IC's frequency register value.
    The device stores the AC frequency as a fraction of the PWM master
    frequency: F_AC = F_PWM_M * (F_AC_SCAN / 65535).
    """
    return round((f_ac * 65535) / f_pwm_m)  # F_AC = F_PWM_M * (F_AC_SCAN/65535)

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

def calc_inductance_mh(i_ac_field, u_ac=U_AC, f_ac=F_AC, kcdr=KCDR, gain=GAIN, snsf=SNSF):
    """Estimate inductance from the measured AC current field value.
    L = U / (2*pi*f*I), expressed in mH.
    """
    i_ac = kcdr * gain * snsf * i_ac_field
    i_ac = i_ac / 1e3 # In mA
    return (u_ac / (2 * math.pi * f_ac * i_ac)) * 1e3  # mH

with ConnectionManager().connect() as my_interface:

    eval = MAX22216_eval(my_interface)
    ic = eval.ics[0]
    solenoid = ic.motors[0]

    # General settings
    eval.write_register_field(MAX22216.FIELD.ACTIVE, 1) # Enable bit to activate the IC
    eval.write_register_field(MAX22216.FIELD.VDR_NDUTY, 1) # When set Logic High, L2H, DC_H, and DC_L registers for each channel indicate a voltage level in voltage mode. 

    # Solenoid sequencer channel 0
    eval.write_register_field(MAX22216.FIELD.DC_L2H_0, calc_vdc_reg(8)) # # Sets the DC_L2H level to 8 V 
    eval.write_register_field(MAX22216.FIELD.DC_H_0, calc_vdc_reg(3)) # # Sets the DC_H level to 3 V 
    eval.write_register_field(MAX22216.FIELD.TIME_L2H_0, calc_time_l2h_reg(100)) # # Sets the TIME_L2H to 100 ms

    # Inductance measurement
    eval.write_register_field(MAX22216.FIELD.U_AC, calc_u_ac_scan(U_AC)) # Sets the amplitude of the internally generated ac signal to 3 V
    eval.write_register(MAX22216.REG.F_AC, calc_f_ac_scan(F_AC)) # Sets the frequency of the internally generated ac signal to 1000 Hz

    eval.write_register_field(MAX22216.FIELD.L_MEAS_EN_0, 1) # Inductance measurement enabled 
    eval.write_register_field(MAX22216.FIELD.L_MEAS_H_0, 1) # Enabled during hold time 

    eval.write_register_field(MAX22216.FIELD.CNTL0, 1)  # Turn the solenoid on
    time.sleep(1.0)

    I_AC_FIELD = eval.read_register_field(MAX22216.FIELD.I_AC_0)

    L = calc_inductance_mh(I_AC_FIELD)

    print(f"Inductance: {L} mH")

    time.sleep(1.0)
    eval.write_register_field(MAX22216.FIELD.CNTL0, 0)  # Turn the solenoid off

print("\nDone.")