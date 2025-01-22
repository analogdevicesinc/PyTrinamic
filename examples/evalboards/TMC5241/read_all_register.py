################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to read all TMC5241 registers of TMC5241-EVAL."""

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC5241
from pytrinamic.evalboards import TMC5241_eval


with ConnectionManager().connect() as my_interface:

    tmc5241_eval = TMC5241_eval(my_interface)

    for register in TMC5241.REGMAP.registers():
        print(f"{register.name:17}: 0x{tmc5241_eval.read(register):08X}")
