################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to control the Brake(ON/OFF)."""

from pytrinamic.connections import ConnectionManager
import time

from pytrinamic.ic import MAX22215
from pytrinamic.evalboards import MAX22215_eval

with ConnectionManager().connect() as my_interface:
    max22215_eval = MAX22215_eval(my_interface)

    # Clear faults
    max22215_eval.write(MAX22215.REGMAP.CFG_2.RESET, 1)
    # Set software control mode
    max22215_eval.write(MAX22215.REGMAP.CFG_1.SW_HW, 1)
    # Set active mode
    max22215_eval.write(MAX22215.REGMAP.CFG_2.NSLEEP, 1)

    # Control the brake
    max22215_eval.write(MAX22215.REGMAP.CFG_2.RLS_BRK, 1)
    time.sleep(1.0)
    max22215_eval.write(MAX22215.REGMAP.CFG_2.RLS_BRK, 0)
