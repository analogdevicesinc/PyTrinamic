################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
    This example demonstrates the prototyping of the OTP (One-Time Programmable) feature of the TMC5222. 
    Prototyping is reversible with a power cycle, allowing for experimentation with OTP settings without 
    permanently altering the OTP. The changes made during prototyping take effect immediately, but only 
    until the IC is reset.

    In this example, values are written to the USER_DATA registers, although any other register can also 
    be utilized. Some registers are written with write protection enabled, while others are modified with 
    the write protection bit disabled. The impact of overwriting the values in the registers is observed
    in each case.
"""

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC5222, Register, Access
from pytrinamic.evalboards import TMC5222_eval

TMC5222.REGMAP.MTP_CONTROL = Register(name="MTP_CONTROL", parent=TMC5222.REGMAP, access=Access.RW, address=0x0010, signed=False)
TMC5222.REGMAP.MTP_PROT_ADDR = Register(name="MTP_PROT_ADDR", parent=TMC5222.REGMAP, access=Access.RW, address=0x0012, signed=False)
TMC5222.REGMAP.MTP_PROT_WDATA = Register(name="MTP_PROT_WDATA", parent=TMC5222.REGMAP, access=Access.RW, address=0x0013, signed=False)

WRITEABLE = 0
WRITE_PROTECT = 1

def prototype_register_start_address(address, write_protect):
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_ADDR, 0x0)
    write_value = address | (write_protect << 7)
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_WDATA, write_value)
    return

def prototype_register_value(value):
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_ADDR, 0x4)
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_WDATA, value)
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_ADDR, 0x5)
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_WDATA, value >> 8)
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_ADDR, 0x6)
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_WDATA, value >> 16)
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_ADDR, 0x7)
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_WDATA, value >> 24)
    return

def prototype_register_lock_value(value):
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_ADDR, 0x8)
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_WDATA, value)
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_ADDR, 0x9)
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_WDATA, value >> 8)
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_ADDR, 0xA)
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_WDATA, value >> 16)
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_ADDR, 0xB)
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_WDATA, value >> 24)
    return

def prototype_block_otp(block_mtp_access):
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_ADDR, 0xF)
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_WDATA, block_mtp_access << 7)
    return

def set_i2c_addr(i2c_addr, disable_iref_fault):
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_ADDR, 0xC)
    tmc5222_eval.write(TMC5222.REGMAP.MTP_PROT_WDATA, i2c_addr | (disable_iref_fault << 3))
    return

def lb_i2c_address(my_interface, i2c_addr):
    # Change the I2C communication address of the connected Landungsbrücke.
    my_interface.send(144, 10, 0, i2c_addr)
    return

with ConnectionManager().connect() as my_interface:

    lb_i2c_address(my_interface, 0b1100000)

    tmc5222_eval = TMC5222_eval(my_interface)

    # Disable the driver before entering the OTP mode
    tmc5222_eval.write(TMC5222.REGMAP.GCR_GCONF.DRV_EN_SW, 0x00)

    # Enter OTP Mode
    tmc5222_eval.write(TMC5222.REGMAP.OTP_MODE_OTP_MODE, 0x12A7)

    # Set prototyping mode
    tmc5222_eval.write(TMC5222.REGMAP.MTP_CONTROL, 0x10)

    # Set Address to write MTP_REGISTER_ADDRESS record.
    prototype_register_start_address(0x46, WRITEABLE) # Set address to USER_DATA_0 (0x46)
    prototype_register_value(0x76543210)              # Write data to USER_DATA_0
    prototype_register_value(0xFEDCBA98)              # Write data to USER_DATA_1 (0x47), no need to write the register address again if it comes next in the sequence 0x46, 0x47,..

    prototype_register_start_address(0x48, WRITE_PROTECT) # Set address to USER_DATA_2 (0x48). Although 0x48 comes after 0x47, we write the address to enable write_protect this time
    prototype_register_value(0x01234567)                  # Write data to USER_DATA_2 
    prototype_register_value(0x89ABCDEF)                  # Write data to USER_DATA_3 (0x49)

    # This block will change the i2c address and lock the whole OTP, so after this no new entry will be possible anymore.
    i2c_addr = 0b001 # Set the i2c device address bits 4..2
    if i2c_addr > 7 :
        print(f"This i2c address setting {i2c_addr} is not a valid setting.")
    disable_iref_fault = False
    block_mtp_access = True

    set_i2c_addr(i2c_addr, disable_iref_fault) # This change will be immediately visible in the i2c traffic, therefore the Landungsbrücke needs to be set to the new address.
    lb_i2c_address(my_interface, 0b1100100) # Set Landungsbrücke to the new i2C address to be able to continue communication after changing the i2C address in the OTP prototyping.
    
    prototype_block_otp(block_mtp_access) # Lock the whole otp --> after this no new entry will be usable

    # As the OTP was locked before this will not have any effect anymore.
    # The set register values will not be present in the first readout.
    prototype_register_start_address(0x48, WRITEABLE) # this does nothing now
    prototype_register_value(0xCAFEBEEF)              # this does nothing now
    prototype_register_value(0xBABEBABE)              # this does nothing now

    # Leave otp mode
    tmc5222_eval.write(TMC5222.REGMAP.OTP_MODE_OTP_MODE, 0x12A0)

    # Read registers
    print("-----------")
    print("Reading registers:")
    print(f"0x46: 0x{tmc5222_eval.read(TMC5222.REGMAP.USER_DATA_USER_DATA_0):08X}")
    print(f"0x47: 0x{tmc5222_eval.read(TMC5222.REGMAP.USER_DATA_USER_DATA_1):08X}")
    print(f"0x48: 0x{tmc5222_eval.read(TMC5222.REGMAP.USER_DATA_USER_DATA_2):08X}")
    print(f"0x49: 0x{tmc5222_eval.read(TMC5222.REGMAP.USER_DATA_USER_DATA_3):08X}")

    print("-----------")
    print("Overwrite registers to zero")
    # Try to overwrite
    tmc5222_eval.write(TMC5222.REGMAP.USER_DATA_USER_DATA_0, 0)
    tmc5222_eval.write(TMC5222.REGMAP.USER_DATA_USER_DATA_1, 0)
    tmc5222_eval.write(TMC5222.REGMAP.USER_DATA_USER_DATA_2, 0)
    tmc5222_eval.write(TMC5222.REGMAP.USER_DATA_USER_DATA_3, 0)

    print("-----------")
    print("Reading registers again:")
    print("Note: Write protected registers won't be overwritten. 0x48 and 0x49 should still contain the old value.")
    # Read again to verify
    print(f"0x46: 0x{tmc5222_eval.read(TMC5222.REGMAP.USER_DATA_USER_DATA_0):08X}")
    print(f"0x47: 0x{tmc5222_eval.read(TMC5222.REGMAP.USER_DATA_USER_DATA_1):08X}")
    print(f"0x48: 0x{tmc5222_eval.read(TMC5222.REGMAP.USER_DATA_USER_DATA_2):08X}")
    print(f"0x49: 0x{tmc5222_eval.read(TMC5222.REGMAP.USER_DATA_USER_DATA_3):08X}")
