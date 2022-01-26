#!/usr/bin/env python3
'''
Minimalistic demonstration of the stallGuard feature of the TMC5160.
To reset stall on all modules, restart then script.

Created on 20.03.2020

@author: LK
'''

################################################################################
# Configuration for all motors

CURRENT_MAX = 10
ACCELERATION = 1000
VELOCITY = 50000
THRESHOLD_SG = 3
THRESHOLD_VELOCITY = 1

################################################################################

import time

import pytrinamic
from pytrinamic.connections.connection_manager import ConnectionManager
from pytrinamic.modules.tmc_eval_shield import TmcEvalShield
from pytrinamic.evalboards.TMC5160_shield import TMC5160_shield

pytrinamic.show_info()

myInterface = ConnectionManager().connect()

shields = TmcEvalShield(myInterface, TMC5160_shield).shields

# Initialize all attached shields
for shield in shields:
    print("Rotating motor.")
    shield.set_axis_parameter(shield.AP.MaxCurrent, 0, CURRENT_MAX)
    shield.set_axis_parameter(shield.AP.MaxAcceleration, 0, ACCELERATION)
    shield.rotate(0, VELOCITY)

    shield.set_axis_parameter(shield.AP.SG2Threshold, 0, THRESHOLD_SG)
    shield.set_axis_parameter(shield.AP.smartEnergyStallVelocity, 0, 0)
    time.sleep(1)
    shield.set_axis_parameter(shield.AP.smartEnergyStallVelocity, 0, THRESHOLD_VELOCITY)

# Loop over all attached shields
while True:
    for shield in shields:
        print(f"Shield: {shield}, SGT: {shield.getAxisParameter(shield.AP.LoadValue, 0)}")
    time.sleep(0.1)

# Demo exit, stop all motors
logger.info("Stopping all motors.")
for shield in shields:
    logger.info(f"Stopping motors for shield {shield}.")
    shield.stop(0)

myInterface.close()
