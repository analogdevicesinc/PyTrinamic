################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to use TMC9660-3PH-EVKIT.

Note: To run this script the TMC9660-3PH-EVAL first needs an uploaded/burned configuration
and the register app must have been started.

                            +-----+  +-------------------+
                     USB    |     |==|                   |
                     -------|     |==|                   |
Connected to the machine    |     |==|                   |
running this script.        |LB   |==|TMC9660-3PH-EVAL   |
                            +-----+  +-------------------+

"""

import time

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC9660
from pytrinamic.evalboards import TMC9660_3PH_eval


with ConnectionManager().connect() as my_interface:

    tmc9660_eval = TMC9660_3PH_eval(my_interface)

    for register in TMC9660.MCC.registers():
        register_value = tmc9660_eval.read(register)
        print(f"{register.name:17}: 0x{register_value:08X}")
        for field in register.fields():
            field_value = field.get(register_value)
            if field.choice:
                print(f"  {field.name:22}: {field.choice.get(field_value).name}")
            else:
                print(f"  {field.name:22}: {field_value}")

