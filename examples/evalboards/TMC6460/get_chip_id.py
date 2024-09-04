#!/usr/bin/env python
################################################################################
# Copyright © 2026 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import TMC6460
from pytrinamic.evalboards import TMC6460_eval

# # Uncomment these lines to enable logging of all communication
# import logging
# import sys
# logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


with ConnectionManager().connect() as my_interface:
    tmc6460_eval = TMC6460_eval(my_interface)
    # Read the chip revision from the "Chip" register group
    rev = tmc6460_eval.read(TMC6460.REGMAP.CHIP.ID)
    print(f"Chip ID: 0x{rev:08X}")
