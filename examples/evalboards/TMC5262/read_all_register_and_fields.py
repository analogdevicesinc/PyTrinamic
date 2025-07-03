################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to read all TMC5262 registers of TMC5262-EVAL."""

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC5262
from pytrinamic.evalboards import TMC5262_eval


with ConnectionManager().connect() as my_interface:

    TMC5262_eval = TMC5262_eval(my_interface)

    for register in TMC5262.REGMAP.registers():
        register_value = TMC5262_eval.read(register)
        print(f"{register.name:17}: 0x{register_value:08X}")
        for field in register.fields():
            field_value = field.get(register_value)
            if field.choice:
                option_text = next((text for text, option in field.choice.items() if option.value == field_value), None)
                print(f"  {field.name:22}: {option_text}")
            else:
                print(f"  {field.name:22}: {field_value}")