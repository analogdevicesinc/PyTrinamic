#!/usr/bin/env python
################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################
"""
This example script reads all registers and their fields from a TMC6460
evaluation board and exports the values to a text file or prints them to the console.
"""

from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import TMC6460, Choice, Access

from pytrinamic.evalboards import TMC6460_eval
from datetime import datetime

EXCLUDE_READ_ONLY = False  # Set to True to only show read/write registers

# Set target output file. None means printing to stdout
FILE_NAME = None
FILE_NAME = "TMC6460_register_export.txt"

with ConnectionManager().connect() as my_interface:
    tmc6460_eval = TMC6460_eval(my_interface)

    output_lines = []
    output_lines.append("TMC6460 Register Export")
    output_lines.append(f"Date/Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    output_lines.append(f"Read only registers excluded") if EXCLUDE_READ_ONLY else None
    output_lines.append("===============================================================\n")

    # Iterate over all registers and their fields in the register map
    for group in TMC6460.REGMAP.groups():
        for register in group.registers():
            if EXCLUDE_READ_ONLY and not register.access.is_writable():
                continue

            value = tmc6460_eval.read(register)

            output_lines.append(f"{group.name}.{register.name} = 0x{value:08X}")

            for field in register.fields():
                if EXCLUDE_READ_ONLY and field.access == Access.R:
                    continue

                field_value = tmc6460_eval.read(field)
                if field.choice is not None:
                    choices: Choice = field.choice
                    field_choice = choices.get(field_value)
                    output_lines.append(f"    {field.name} = {field_choice.name} ({field_value})")
                else:
                    output_lines.append(f"    {field.name} = {field_value}")

    if FILE_NAME != None:
        with open(FILE_NAME, "w") as f:
            for line in output_lines:
                f.write(line + "\n")
        print(f"Register output stored in {FILE_NAME}")
    else:
        for line in output_lines:
            print(line)
