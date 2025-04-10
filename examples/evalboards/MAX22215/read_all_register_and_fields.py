################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to read all MAX22215 registers of MAX22215-EVAL."""

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import MAX22215
from pytrinamic.evalboards import MAX22215_eval


with ConnectionManager().connect() as my_interface:

    max22215_eval = MAX22215_eval(my_interface)

    for register in MAX22215.REGMAP.registers():
        register_value = max22215_eval.read(register)
        print(f"{register.name:17}: 0x{register_value:08X}")
        for field in register.fields():
            field_value = field.get(register_value)
            if field.choice:
                option_text = next((text for text, option in field.choice.items() if option.value == field_value), None)
                print(f"  {field.name:22}: {option_text}")
            else:
                print(f"  {field.name:22}: {field_value}")