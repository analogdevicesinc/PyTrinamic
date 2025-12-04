################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to read all TMC5262 registers of TMC5262-EVAL."""

import ctypes

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC5262
from pytrinamic.evalboards import TMC5262_eval


with ConnectionManager().connect() as my_interface:
    tmc5262_eval = TMC5262_eval(my_interface)

    for register in TMC5262.REGMAP.registers():
        register_value = tmc5262_eval.read(register)
        # Convert to unsigned for the hex print not to be negative
        register_value = ctypes.c_uint32(register_value).value
        print(f"{register.name:17}: 0x{register_value:08X}")
        if len(register.fields()) == 1 and register.fields()[0].name == register.name:
            # Do not print the field value if the field is the same as the register
            continue
        for field in register.fields():
            field_value = field.get(register_value)
            if field.choice:
                # Print text representation of the field value if its an enumeration
                print(f"  {field.name:24}: {field.choice.get(field_value).name}")
            else:
                # Just print the field value decimal
                print(f"  {field.name:24}: {field_value}")
