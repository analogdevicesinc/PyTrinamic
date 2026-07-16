################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################
"""
    This example demonstrates the prototyping of the OTP (One-Time Programmable) feature of the TMC5221. 
    Prototyping is reversible with a power cycle, allowing for experimentation with OTP settings without 
    permanently altering the OTP. The changes made during prototyping take effect immediately, but only 
    until the IC is reset.

    In this example, values are written to the USER_DATA registers, although any other register can also 
    be utilized. Some registers are written with write protection enabled, while others are modified with 
    the write protection bit disabled. The impact of overwriting the values in the registers is observed
    in each case.
"""

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC5221, Register, Access
from pytrinamic.evalboards import TMC5221_eval


TMC5221.REGMAP.MTP_CONTROL = Register(name="MTP_CONTROL", parent=TMC5221.REGMAP, access=Access.RW, address=0x0010, signed=False)
TMC5221.REGMAP.MTP_PROT_ADDR = Register(name="MTP_PROT_ADDR", parent=TMC5221.REGMAP, access=Access.RW, address=0x0012, signed=False)
TMC5221.REGMAP.MTP_PROT_WDATA = Register(name="MTP_PROT_WDATA", parent=TMC5221.REGMAP, access=Access.RW, address=0x0013, signed=False)

WRITEABLE = 0
WRITE_PROTECT = 1

def prototype_register_start_address(address, write_protect):
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_ADDR, 0x0)
    write_value = address | (write_protect << 7)
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_WDATA, write_value)

def prototype_register_value(value):
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_ADDR, 0x4)
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_WDATA, value)
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_ADDR, 0x5)
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_WDATA, value >> 8)
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_ADDR, 0x6)
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_WDATA, value >> 16)
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_ADDR, 0x7)
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_WDATA, value >> 24)

def prototype_register_lock_value(value):
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_ADDR, 0x8)
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_WDATA, value)
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_ADDR, 0x9)
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_WDATA, value >> 8)
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_ADDR, 0xA)
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_WDATA, value >> 16)
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_ADDR, 0xB)
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_WDATA, value >> 24)

def prototype_lock_otp(disable_iref_fault, block_mtp):
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_ADDR, 0xC)
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_WDATA, disable_iref_fault << 3)
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_ADDR, 0xF)
    tmc5221_eval.write(TMC5221.REGMAP.MTP_PROT_WDATA, block_mtp << 7)


with ConnectionManager().connect() as my_interface:

    tmc5221_eval = TMC5221_eval(my_interface)

    # Disable the driver before entering the OTP mode
    tmc5221_eval.write(TMC5221.REGMAP.GCR_GCONF.DRV_EN_SW, 0x00)

    # Enter OTP Mode
    tmc5221_eval.write(TMC5221.REGMAP.OTP_MODE_OTP_MODE, 0x12A7)
    
    # Set prototyping mode
    tmc5221_eval.write(TMC5221.REGMAP.MTP_CONTROL, 0x10)

    # Set Address to write MTP_REG_ADDR record
    prototype_register_start_address(0x49, WRITEABLE) # Set address to USER_DATA_3(0x49)
    prototype_register_value(0x76543210)              # Write data to USER_DATA_3
    prototype_register_value(0xFEDCBA98)              # Write data to USER_DATA_4 (0x4A), no need to write the register address again if it comes next in the sequence 0x49, 0x4A,..

    prototype_register_start_address(0x4B, WRITE_PROTECT) # Set address to USER_DATA_5 (0x4B). Although 0x4B comes after 0x4A, we write the address to enable write_protect this time
    prototype_register_value(0x01234567)                  # Write data to USER_DATA_5 
    prototype_register_value(0x89ABCDEF)                  # Write data to USER_DATA_6 (0x4C)

    disable_iref_fault = False
    lock_otp = True
    
    prototype_lock_otp(disable_iref_fault, lock_otp) # Lock the whole otp --> after this no new entry will be usable

    # As the OTP was locked before this will not have any effect anymore.
    prototype_register_start_address(0x4B, WRITEABLE) # This does nothing now
    prototype_register_value(0xCAFEBEEF) # This does nothing now
    prototype_register_value(0xBABEBABE) # This does nothing now

    # Leave otp mode
    tmc5221_eval.write(TMC5221.REGMAP.OTP_MODE_OTP_MODE, 0x12A0)

    # Read stuff back
    print("Reading registers:")
    print(f"0x49: 0x{tmc5221_eval.read(TMC5221.REGMAP.USER_DATA_USER_DATA_3):08X}")
    print(f"0x4A: 0x{tmc5221_eval.read(TMC5221.REGMAP.USER_DATA_USER_DATA_4):08X}")
    print(f"0x4B: 0x{tmc5221_eval.read(TMC5221.REGMAP.USER_DATA_USER_DATA_5):08X}")
    print(f"0x4C: 0x{tmc5221_eval.read(TMC5221.REGMAP.USER_DATA_USER_DATA_6):08X}")

    print("-----------")
    print("Overwrite registers")
    # Try to overwrite
    tmc5221_eval.write(TMC5221.REGMAP.USER_DATA_USER_DATA_3, 0)
    tmc5221_eval.write(TMC5221.REGMAP.USER_DATA_USER_DATA_4, 0)
    tmc5221_eval.write(TMC5221.REGMAP.USER_DATA_USER_DATA_5, 0)
    tmc5221_eval.write(TMC5221.REGMAP.USER_DATA_USER_DATA_6, 0)

    print("-----------")
    print("Reading registers again:")
    # Read again and verify
    print(f"0x49: 0x{tmc5221_eval.read(TMC5221.REGMAP.USER_DATA_USER_DATA_3):08X}")
    print(f"0x4A: 0x{tmc5221_eval.read(TMC5221.REGMAP.USER_DATA_USER_DATA_4):08X}")
    print(f"0x4B: 0x{tmc5221_eval.read(TMC5221.REGMAP.USER_DATA_USER_DATA_5):08X}")
    print(f"0x4C: 0x{tmc5221_eval.read(TMC5221.REGMAP.USER_DATA_USER_DATA_6):08X}")