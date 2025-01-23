################################################################################
# Copyright © 2026 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""
    Example of burning the OTP with TMC5221.
    It is highly recommended to prototype the desired OTP settings before actual burning.
    Prototyping can be done with the script "mtp_prototype.py" in this folder.
    
    The IC has the ability to burn 80 records in total.
    Exceeding this limit will not damage the device, but the burn procedure will be aborted and no changes will be made to the OTP.

    A record with the same RECORD_TYPE (and REGISTER_ADDRESS, depending on the Type) will overwrite a previous one,
    giving the ability to easily correct mistakes while burning.
    Only when BLOCK_MTP_ACCESS is set to "True", the OTP will be locked and no further changes are possible anymore, not even overwriting existing records.

    OTP burning needs a stable Supply Voltage of 8.7V ± 0.13V (1.5%).
    Do not program while the motor is in operation.
"""

import time

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC5221, Register, Access
from pytrinamic.evalboards import TMC5221_eval


TMC5221.REGMAP.MTP_CONTROL = Register(name="MTP_CONTROL", parent=TMC5221.REGMAP, access=Access.RW, address=0x0010, signed=False)
TMC5221.REGMAP.MTP_STATUS = Register(name="MTP_STATUS", parent=TMC5221.REGMAP, access=Access.RW, address=0x0011, signed=False)
TMC5221.REGMAP.MTP_CP_CONTROL2 = Register(name="MTP_CP_CONTROL2", parent=TMC5221.REGMAP, access=Access.RW, address=0x0021, signed=False)
TMC5221.REGMAP.MTP_CP_STATUS = Register(name="MTP_CP_STATUS", parent=TMC5221.REGMAP, access=Access.RW, address=0x0022, signed=False)
TMC5221.REGMAP.MTP_DATA0 = Register(name="MTP_DATA0", parent=TMC5221.REGMAP, access=Access.RW, address=0x0030, signed=False)
TMC5221.REGMAP.MTP_DATA1 = Register(name="MTP_DATA1", parent=TMC5221.REGMAP, access=Access.RW, address=0x0031, signed=False)
TMC5221.REGMAP.MTP_DATA2 = Register(name="MTP_DATA2", parent=TMC5221.REGMAP, access=Access.RW, address=0x0032, signed=False)
TMC5221.REGMAP.MTP_DATA3 = Register(name="MTP_DATA3", parent=TMC5221.REGMAP, access=Access.RW, address=0x0033, signed=False)
TMC5221.REGMAP.MTP_ADDR = Register(name="MTP_ADDR", parent=TMC5221.REGMAP, access=Access.RW, address=0x0034, signed=False)

INTERNAL_CLOCK = 0x0
VOLTAGE_IN_RANGE = 3
VOLTAGE_TOO_SMALL = 0
VOLTAGE_TOO_HIGH = 7

# Table 23 "MTP Record Types" in the datasheet 
RECORD_TYPE_0 = 0x0  # REGISTER_WRITE_LOCK [7], REGISTER_ADDRESS [6:0]
RECORD_TYPE_1 = 0x1  # REGISTER_DATA [31:0]
RECORD_TYPE_2 = 0x2  # REGISTER_LOCK_BITS [31:0]
RECORD_TYPE_3 = 0x3  # BLOCK_MTP_ACCESS [31], DISABLE_IREF_FAULT [3], I2C_NODE_ADDRESS [2:0]


def check_burning_voltage():
    # Check if the burning voltage is within range
    for x in range(0, 3):
        comparator_value = tmc5221_eval.read(TMC5221.REGMAP.MTP_CP_STATUS) & 0x7
        if comparator_value == VOLTAGE_IN_RANGE:
            return True
        if comparator_value == VOLTAGE_TOO_SMALL:
            print("voltage for burning is too low")
        if comparator_value == VOLTAGE_TOO_HIGH:
            print("voltage for burning is too high")
        time.sleep(1)
        print(f"trial number: {x}")
    return False


def set_data_to_burn(record_type, data_to_program):
    # We are writing 8 bit registers here
    tmc5221_eval.write(TMC5221.REGMAP.MTP_DATA0, data_to_program)
    data_to_program = data_to_program >> 8
    tmc5221_eval.write(TMC5221.REGMAP.MTP_DATA1, data_to_program)
    data_to_program = data_to_program >> 8
    tmc5221_eval.write(TMC5221.REGMAP.MTP_DATA2, data_to_program)
    data_to_program = data_to_program >> 8
    tmc5221_eval.write(TMC5221.REGMAP.MTP_DATA3, data_to_program)

    tmc5221_eval.write(TMC5221.REGMAP.MTP_ADDR, record_type)

def burn_data():
    # Check if there is space left in otp
    mtp_status = tmc5221_eval.read(TMC5221.REGMAP.MTP_STATUS)
    mtp_full = (mtp_status & 0x4) >> 2
    if not mtp_full:
        tmc5221_eval.write(TMC5221.REGMAP.MTP_CONTROL, 0x1)
        done_burning = 0
        vpp_init_fail = 0
        while (not done_burning) or (mtp_full) or (vpp_init_fail):
            # Poll the done bit or error flags
            mtp_status = tmc5221_eval.read(TMC5221.REGMAP.MTP_STATUS)
            veri_fail = (mtp_status & 0x02) >> 1
            mtp_full = (mtp_status & 0x04) >> 2
            vpp_init_fail = (mtp_status & 0x08) >> 3
            ov_during_burn_pulse = (mtp_status & 0x10) >> 4
            ecc_err_1_bit = (mtp_status & 0x20) >> 5
            ecc_err_2_bit = (mtp_status & 0x40) >> 6
            done_burning = (mtp_status & 0x80) >> 7
        if veri_fail:
            print("VERI_FAIL: burning the otp 3 times did not produce a valid result")
        if mtp_full:
            print("MTP_FULL: all records are already burnt. burn procedure will not be started and aborted.")
        if vpp_init_fail:
            print("VPP_INIT_FAIL: programming voltage did not reach desired value. Burn abandoned")
        if ov_during_burn_pulse:
            print("OV_DURING_BURN_PULSE: programming voltage exceeded limits. Safe operation not guaranteed!!")
        if ecc_err_1_bit:
            print("ECC_ERR_1BIT: loaded record contains an ECC error that was corrected")
        if ecc_err_2_bit:
            print("ECC_ERR_2BIT: loaded record contains an ECC error could not be corrected")
    else:
        print("all records are already burnt. burn procedure will not be started and aborted.")


def restore_otp():
    # After burning this will load the otp values without the need of a powercycle
    tmc5221_eval.write(TMC5221.REGMAP.MTP_CONTROL, 0x80)


with ConnectionManager().connect() as my_interface:

    tmc5221_eval = TMC5221_eval(my_interface)

    # Check for internal oscillator
    oscillator = tmc5221_eval.read(TMC5221.REGMAP.GCR_IOIN.EXT_CLK)

    # Disable the driver before entering the OTP mode
    tmc5221_eval.write(TMC5221.REGMAP.GCR_GCONF.DRV_EN_SW, 0x00)

    # Enter OTP Mode
    tmc5221_eval.write(TMC5221.REGMAP.OTP_MODE_OTP_MODE, 0x12A7)

    # Enable the window comparator
    tmc5221_eval.write(TMC5221.REGMAP.MTP_CP_CONTROL2, 0x1B)

    voltage_in_range = check_burning_voltage()

    # This example will write the registers 0x46 ... 0x4D with the respective values
    if voltage_in_range & (oscillator == INTERNAL_CLOCK):
        print("Voltage ok")

        # Set to "True" to burn the value of the registers in OTP
        # For prototyping/testing it's recommended to only burn registers that are not needed for motor operation.
        # E.g. the USER_DATA registers.
        LIMIT_VALUES = False
        VMAX_LIMIT = False
        USER_DATA_0 = False
        USER_DATA = False

        # Caution! Every further record becoming burned to the OTP is ignored if BLOCK_MTP = True.
        # This will effectively locks the whole OTP.
        BLOCK_MTP = False

        if LIMIT_VALUES:
            # This example burns the the maximum current limits.
            # The value can be obtained by the TMCL-IDE register browser.
            # Usually it is useful to set the write protection for these registers to avoid accidental overwriting of these limiting values.
            start_address = 0x45    # 0x45 -> LIMIT_VALUES
            write_protect = 1
            data = (write_protect << 7) + start_address
            set_data_to_burn(RECORD_TYPE_0, data)
            burn_data()
            set_data_to_burn(RECORD_TYPE_1, 0x0A1F0E64)
            burn_data()
            print("Limit burned")

        if VMAX_LIMIT:
            # This example burns the maximum velocity limits with write protection enabled.
            start_address = 0x44    # 0x44 -> VMAX_LIMIT
            write_protect = 1
            data = (write_protect << 7) + start_address
            set_data_to_burn(RECORD_TYPE_0, data)
            burn_data()
            set_data_to_burn(RECORD_TYPE_1, 0x000186A0)
            burn_data()
            print("VMAX_LIMIT burned")

        if USER_DATA_0:
            # This example burns one USER_DATA register with write protection enabled.
            start_address = 0x46    # 0x46 -> USER_DATA_0
            write_protect = 1
            data = (write_protect << 7) + start_address
            set_data_to_burn(RECORD_TYPE_0, data)
            burn_data()
            set_data_to_burn(RECORD_TYPE_1, 0xF1F1F1F1)
            burn_data()
            print("USER_DATA_0 burned")

        if USER_DATA:
            # Compared to USER_DATA_0, this will efficiently burn a sequence of USER_DATA registers.
            # This example could be used to burn a unique serial number or application relevant data to the device.
            # Again, write protection is enabled in this example.
            write_protect = 1
            start_address = 0x46 
            data = (write_protect << 7) + start_address
            set_data_to_burn(RECORD_TYPE_0, data) # write the address of the register to be burned i.e. 0x46
            burn_data()
            set_data_to_burn(RECORD_TYPE_1, 0x5A5A5A5A) # write the data to 0x46
            burn_data()
            set_data_to_burn(RECORD_TYPE_1, 0xA5A5A5A5) # No need to write the address 0x47 again, as it is automatically incremented with successive writes to the data register
            burn_data()
            set_data_to_burn(RECORD_TYPE_1, 0xBEEFBEEF) # write the data to 0x48
            burn_data()
            set_data_to_burn(RECORD_TYPE_1, 0xCAFEBABE) # write the data to 0x49
            burn_data()
            set_data_to_burn(RECORD_TYPE_1, 0xBABEBEEF) # write the data to 0x4A
            burn_data()
            set_data_to_burn(RECORD_TYPE_1, 0xDEADBEEF) # write the data to 0x4B
            burn_data()
            set_data_to_burn(RECORD_TYPE_1, 0x11111111) # write the data to 0x4C
            burn_data()
            set_data_to_burn(RECORD_TYPE_1, 0xFFFFFFFF) # write the data to 0x4D
            burn_data()
            print("User-Data burned")

        # Caution! every further record becoming burned to the OTP is ignored if BLOCK_MTP = True
        if BLOCK_MTP:
            i2c_node_address = 0b000   # Don't use 110 or 111!
            disable_iref_fault = 0x0
            block_mtp_access = 0x1
            data = (block_mtp_access << 31) + (disable_iref_fault << 3) + i2c_node_address
            set_data_to_burn(RECORD_TYPE_3, data)
            burn_data()

        print("program ended.")

    else:
        print("program ended without burning as voltage is not within range.")

    restore_otp()

    # Leave OTP_MODE
    tmc5221_eval.write(TMC5221.REGMAP.MTP_CP_CONTROL2, 0x0)
    tmc5221_eval.write(TMC5221.REGMAP.OTP_MODE_OTP_MODE, 0x12A0)
