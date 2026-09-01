################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

"""
Setup Example: CDR Contactor Full-Bridge. he focus of this example is to showcase the current drive 
regulation (CDR) and detection of plunger movement (DPM), and an alarm to check if the current target is reached (HHF), 
alongside other more advanced analog features. The MAX22216 is also set to use the open-load detection, as it requires 
an extra setting when used in full-bridge mode, and the global and channel PWM frequency are set to different values to 
showcase the flexibility of the part. 

The MAX22216 also has some more advanced analog and mixed features: the SlewRate of the PWM output can be 
limited to lower the EMC, and the transition periods between (RAMPs) the different levels can be controlled, which can 
lower the actual noise produced by the solenoid/contactor and limit the mechanical impact force of the plunger actuation. 
To help with opening the solenoid faster when the channel is turned OFF in full-bridge mode, the MAX22216 can create 
a reverse voltage that helps with the coil discharge (fast demagnetization – DC_H2L).

For more information refer to "Setup Example: CDR Contactor Full-Bridge" in the datasheet:
[MAX22216 evaluation kit datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/max22216evkit.pdf)

Used load: Contactor with 24V DC Coil (Non-Polarized) 
Connection: Load Between OUT2 and OUT3 
Power supply: 24V
"""

import time
from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import MAX22216
from pytrinamic.evalboards import MAX22216_eval

F_PWM_M = 40 # kHz
F_PWM_INDEX = 1 # Set the channel frequency divider as per the F_PWM_MAP below

# Global PWM master-frequency selection map: integer 0..12 maps to a different frequency (in kHz).
# Use e.g. F_PWM_M = F_PWM_M_MAP[4] for 40 kHz.
F_PWM_M_MAP = {
    0: 100,
    1: 80,
    2: 60,
    3: 50,
    4: 40,
    5: 30,
    6: 25,
    7: 20,
    8: 15,
    9: 10,
    10: 7.5,
    11: 5,
    12: 2.5,
}

F_PWM_MAP = {
    0: F_PWM_M,
    1: F_PWM_M/2,
    2: F_PWM_M/4,
    3: F_PWM_M/8,
}

F_PWM = F_PWM_MAP[F_PWM_INDEX]

GAIN = 1 # current measurement scaling factor
SNSF = 1 # Sense-scaling factor
KCDR = 1.017 # Current Drive Regulation Constant

def calc_idc_reg(idc, kcdr=KCDR, gain = GAIN, snsf = SNSF):
    """Convert a target DC output current in mA into the current-register value.
    The MAX22216 uses the relation IOUT = KCDR x GAIN x SNSF x DC_L2H[15:0]DEC.
    """
    return round(idc / kcdr / gain / snsf)  # IOUT = KCDR x GAIN x SNSF x DC_L2H[15:0]DEC               

def calc_time_l2h_reg(time_l2h, fpwm=F_PWM):
    """Convert a time value in miliseconds into the TIME_L2H register value.
    The MAX22216 uses the relation TIME_L2H = TIME_L2H[15:0]DEC / F_PWM.
    """
    return round(time_l2h * fpwm)  # TIME_L2H = TIME_L2H[15:0]DEC/F_PWM  

def get_pwm_master_index(frequency_hz):
    """Return the map key for a given PWM master frequency in Hz."""
    for key, value in F_PWM_M_MAP.items():
        if value == frequency_hz:
            return key
    raise ValueError(f"Frequency {frequency_hz} Hz is not in F_PWM_M_MAP")

def calc_dpm_start_reg(dpm_start, kcdr=KCDR, gain = GAIN, snsf = SNSF):
    """Convert a current value in mA to the DPM_START register value.
    The MAX22216 uses the relation DPM_START(mA) = 64 x KCDR x GAIN x SNSF x DPM_START[7:0]DEC.
    """
    return round(dpm_start / 64 / kcdr / gain / snsf )  # DPM_START(mA) = 64 x KCDR x GAIN x SNSF x DPM_START[7:0]DEC

def calc_dpm_thld_reg(dpm_thld, kcdr=KCDR, gain = GAIN, snsf = SNSF):
    """Convert a current value in mA to the DPM_THLD register value.
    The MAX22216 uses the relation DPM_THLD(mA) = 8 x KCDR x GAIN x SNSF x DPM_THLD[11:0]DEC.
    """
    return round(dpm_thld / 8 / kcdr / gain / snsf )  # DPM_THLD(mA) = 8 x KCDR x GAIN x SNSF x DPM_THLD[11:0]DEC

with ConnectionManager().connect() as my_interface:

    eval = MAX22216_eval(my_interface)
    ic = eval.ics[0]
    solenoid = ic.motors[0]

    # General settings
    eval.write_register_field(MAX22216.FIELD.ACTIVE, 1) # Enable bit to activate the IC
    eval.write_register_field(MAX22216.FIELD.VDRNVDRDUTY, 1) # When set Logic High, L2H, DC_H, and DC_L registers for each channel indicate a voltage level in voltage mode. 
    eval.write_register_field(MAX22216.FIELD.CHS, 5) # 2x independent full-bridges (CH0CH1 and CH2CH3)

    eval.write_register_field(MAX22216.FIELD.F_PWM_M, get_pwm_master_index(F_PWM_M)) # Global F_PWM is lowered to 40kHz to lower EMI.
    eval.write_register_field(MAX22216.FIELD.F_PWM_0, F_PWM_INDEX) # Set the channel frequency to PWM/2. Refer to F_PWM_MAP.  

    # Solenoid sequencer channel 0
    eval.write_register_field(MAX22216.FIELD.CTRL_MODE_0, 1) # CDR mode

    eval.write_register_field(MAX22216.FIELD.DC_L2H_0, calc_idc_reg(250)) # Sets the DC_L2H level to 250 mA 
    eval.write_register_field(MAX22216.FIELD.TIME_L2H_0, calc_time_l2h_reg(50)) # Sets the TIME_L2H to 50 ms
    eval.write_register_field(MAX22216.FIELD.DC_H_0, calc_idc_reg(100)) # Sets the DC_H level to 100 mA 
    
    eval.write_register_field(MAX22216.FIELD.RAMP_0, 1) # RAMP is set to a very low value to show the effects on the current going in this contactor
    eval.write_register_field(MAX22216.FIELD.RUPE_0, 1) # Ramp up enabled

    eval.write_register_field(MAX22216.FIELD.DC_H2L, -12) # The fast demagnetization (DC_H2L) is set to −12V
    eval.write_register_field(MAX22216.FIELD.H2L_EN_0, 1) # Enable fast demagnetization 

    # Enable open load detection
    
    # When using the open-load detection in full-bridge configuration, both channels must enable it
    eval.write_register_field(MAX22216.FIELD.OL_EN_0, 1) # Enable open-loop detection in CH0
    eval.write_register_field(MAX22216.FIELD.OL_EN_1, 1) # Enable open-loop detection in CH1

    # One of the channels must have the HSnLS bit enabled
    eval.write_register_field(MAX22216.FIELD.HSNLS_0, 1) # Output is driven using the high-side MOSFET.

    eval.write_register_field(MAX22216.FIELD.HHF_EN_0, 1) # Triggers an alarm if the channel current is not reaching the target current

    eval.write_register_field(MAX22216.FIELD.SLEW_RATE_0, 3) # Lowest slew rate for the lowest EMI

    # DPM Tool

    # Now that all the registers are set, the DPM tool can be used to both set the DPM and tune the PI values.
    eval.write_register_field(MAX22216.FIELD.CFG_P_0, 40000) # P value
    eval.write_register_field(MAX22216.FIELD.CFG_I_0, 500) # I value

    eval.write_register_field(MAX22216.FIELD.DPM_EN_0, 1) # Enable DPM 
    eval.write_register_field(MAX22216.FIELD.DPM_START_0, calc_dpm_start_reg(65.09)) # Sets DPM_START to 65.09 mA 
    eval.write_register_field(MAX22216.FIELD.DPM_THLD_0, calc_dpm_thld_reg(73.22)) # Sets DPM_THLD to 73.22 mA

    eval.write_register_field(MAX22216.FIELD.CNTL0, 1)  # Turn the solenoid on
    time.sleep(2.0)
    eval.write_register_field(MAX22216.FIELD.CNTL0, 0)  # Turn the solenoid off

    eval.write_register_field(MAX22216.FIELD.DPM0, 1) # Clear DPM flag

    # Read the flag status
    DPM0_FAULT = eval.read_register_field(MAX22216.FIELD.DPM0)
    print(f"DPM0_FAULT: {DPM0_FAULT}") # This should read zero

    time.sleep(2.0)

    # Creating a DPM fault to activate the flag
    eval.write_register_field(MAX22216.FIELD.DC_L2H_0, calc_idc_reg(150)) # Lower the DC_L2H level to 150 mA, which is very low for this contactor. The DPM flag should turn on.

    eval.write_register_field(MAX22216.FIELD.CNTL0, 1)  # Turn the solenoid on
    time.sleep(2.0)
    eval.write_register_field(MAX22216.FIELD.CNTL0, 0)  # Turn the solenoid off

    # Read the flag status again after the DPM fault is generated
    DPM0_FAULT = eval.read_register_field(MAX22216.FIELD.DPM0)
    print(f"DPM0_FAULT: {DPM0_FAULT}") # This should read one

print("\nDone.")