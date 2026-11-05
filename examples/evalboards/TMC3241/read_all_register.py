################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################
"""Example on how to read all TMC3241 registers of TMC3241-EVAL."""

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC3241
from pytrinamic.evalboards import TMC3241_eval


with ConnectionManager().connect() as my_interface:
    tmc3241_eval = TMC3241_eval(my_interface)

    for register in TMC3241.REGMAP.registers():
        print(f"{register.name:17}: 0x{tmc3241_eval.read(register):08X}")
