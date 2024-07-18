################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import logging
import time

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import MAX22216
from pytrinamic.evalboards import MAX22216_eval


logging.basicConfig(level=logging.DEBUG)

pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
    print(my_interface)

    eval = MAX22216_eval(my_interface)
    ic = eval.ics[0]
    solenoid = ic.motors[0]

    solenoid.u_supply = 24.0 # V

    solenoid.u_dc_h = 10.0 # V
    solenoid.u_dc_l = 0.0 # V
    solenoid.u_dc_l2h = 10.0 # V 
    solenoid.u_dc_h2l = 0.0 # V
    solenoid.u_ac = 1.0 # V ampl
    solenoid.f_ac = 50.0 # Hz

    solenoid.set_high()
    time.sleep(1.0)
    solenoid.set_low()
    time.sleep(1.0)
    

print("\nDone.")