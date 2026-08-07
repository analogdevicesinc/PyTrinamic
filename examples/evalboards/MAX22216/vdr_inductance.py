################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

"""
Example: MAX22216 controlling a 6V solenoid. Demonstrates the
inductance measurement feautre of MAX22216.

Used load: 12V small door lock pull solenoid (non-polarized)
Connection: OUT0 to COM (VM+)
Power supply: 24V
"""

import logging
import math
import time

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import MAX22216
from pytrinamic.evalboards import MAX22216_eval

pytrinamic.show_info()

KVDR = 30.518e-6
U_AC = 3
U_AC_SCAN = round( U_AC / (36 * KVDR) ) # U_AC = KVDR * 36 * U_AC_SCAN

F_PWM_M = 100e3 # 100KHz
F_AC = 1000 # Hz
F_AC_SCAN = round(( F_AC * 65535 ) / F_PWM_M) # F_AC = F_PWM_M * (F_AC_SCAN/65535)

GAIN = 1
SNSF = 1
KCDR = 1.017


with ConnectionManager().connect() as my_interface:
    print(my_interface)

    eval = MAX22216_eval(my_interface)
    ic = eval.ics[0]
    solenoid = ic.motors[0]

    # General settings
    eval.write_register_field(MAX22216.FIELD.ACTIVE, 1)
    eval.write_register_field(MAX22216.FIELD.VDR_NDUTY, 1)

    # Solenoid sequencer channel 0
    eval.write_register_field(MAX22216.FIELD.DC_L2H_0, 7282) # 8 V
    eval.write_register_field(MAX22216.FIELD.DC_H_0, 2731) # 3 V
    eval.write_register_field(MAX22216.FIELD.TIME_L2H_0, 10000) # 100 ms

    # Inductance measurement
    eval.write_register_field(MAX22216.FIELD.U_AC, U_AC_SCAN) # 3 
    eval.write_register(MAX22216.REG.F_AC, F_AC_SCAN) # 1000 Hz

    eval.write_register_field(MAX22216.FIELD.L_MEAS_EN_0, 1)
    eval.write_register_field(MAX22216.FIELD.L_MEAS_H_0, 1)

    eval.write_register_field(MAX22216.FIELD.CNTL0, 1)  # Turn the solenoid on
    time.sleep(1.0)

    I_AC_FIELD = eval.read_register_field(MAX22216.FIELD.I_AC_0)
    I_AC = KCDR * GAIN * SNSF * I_AC_FIELD
    print(f"I_AC: {I_AC:.2f} mA")
    L = (U_AC * 1e3) / (2 * math.pi * F_AC * I_AC)
    L = L * 1e3 # Convert into mH
    print(f"Inductance: {L} mH")

    time.sleep(1.0)
    eval.write_register_field(MAX22216.FIELD.CNTL0, 0)  # Turn the solenoid off


print("\nDone.")