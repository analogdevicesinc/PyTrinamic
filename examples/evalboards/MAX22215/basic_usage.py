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

    print(f"Chip revision {max22215_eval.read(MAX22215.REGMAP.CHIP_REV.CHIP_REV)}")

    max22215_eval.write(MAX22215.REGMAP.ACTION_ENABLE.ENABLE1, 1)
    max22215_eval.write(MAX22215.REGMAP.CFG_1.SR.choice["25 V/µs"])
    max22215_eval.write(MAX22215.REGMAP.CFG_1.GAIN.choice["100"])