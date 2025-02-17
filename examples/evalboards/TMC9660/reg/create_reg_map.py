################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example script that showcases how to create a register map for the TMC9660."""

from pytrinamic.ic import TMC9660


max_name_length = max([len(register.name) for register in TMC9660.MCC.registers()])
for register in TMC9660.MCC.registers():
    print(f"#define {register.name:{max_name_length}} 0x{register.address:04x}")

