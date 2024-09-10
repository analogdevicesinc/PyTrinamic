###############################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import statistics
import time

from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC4671_eval



with ConnectionManager().connect() as my_interface:
    tmc4671_eval = TMC4671_eval(my_interface)

    tmc4671_reg = tmc4671_eval.ics[0].register

    for register in tmc4671_reg.registers():
        print(f"Register: {register.name}")
        for field in register.fields():
            print(f"\tField: {field.name}: {tmc4671_eval.read(field)}")

