################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################
"""Example on how to read all TMC5221 registers of TMC5221-EVAL."""

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC5221
from pytrinamic.evalboards import TMC5221_eval


with ConnectionManager().connect() as my_interface:

    tmc5221_eval = TMC5221_eval(my_interface)

    for register in TMC5221.REGMAP.registers():
        print(f"{register.name:17}: 0x{tmc5221_eval.read(register):08X}")