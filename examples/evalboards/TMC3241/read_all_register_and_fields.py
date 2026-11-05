################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################
"""Example on how to read all TMC3241 registers of TMC3241-EVAL.

Prints all registers and their fields of the TMC3241-EVAL board.
If the field has an enumeration, its text representation will be printed.
"""

import ctypes

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC3241
from pytrinamic.evalboards import TMC3241_eval


with ConnectionManager().connect() as my_interface:
    tmc3241_eval = TMC3241_eval(my_interface)

    for register in TMC3241.REGMAP.registers():
        register_value = tmc3241_eval.read(register)
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
