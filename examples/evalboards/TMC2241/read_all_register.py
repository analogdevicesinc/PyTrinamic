################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to read all TMC2241 registers of TMC2241-EVAL."""

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC2241
from pytrinamic.evalboards import TMC2241_eval


with ConnectionManager().connect() as my_interface:

    tmc5241_eval = TMC2241_eval(my_interface)

    for register in TMC2241.REGMAP.registers():
        print(f"{register.name:17}: 0x{tmc5241_eval.read(register):08X}")
