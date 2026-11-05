################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################
"""Example on how to use TMC3241-EVAL."""

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC3241
from pytrinamic.evalboards import TMC3241_eval


ext_not_int_map = {
    0: "The internal clock is used",
    1: "The Landungsbruecke provides an external clock signal",
}

with ConnectionManager().connect() as my_interface:
    tmc3241_eval = TMC3241_eval(my_interface)

    ext_not_int = tmc3241_eval.read(TMC3241.REGMAP.PLL.EXT_NOT_INT)
    print(f"EXT_NOT_INT: {ext_not_int} ({ext_not_int_map[ext_not_int]})")

    clock_divider = tmc3241_eval.read(TMC3241.REGMAP.PLL.CLOCK_DIVIDER)
    print(f"CLOCK_DIVIDER: {TMC3241.REGMAP.PLL.CLOCK_DIVIDER.choice.get(clock_divider).name}")
