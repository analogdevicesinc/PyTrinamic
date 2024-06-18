################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Demonstration of the stallGuard feature of the TMC5160 (minimalistic).
"""

import time
import pytrinamic
from pytrinamic.connections.connection_manager import ConnectionManager
from pytrinamic.modules.tmc_eval_shield import TmcEvalShield
from pytrinamic.evalboards.TMC5160_shield import TMC5160_shield

################################################################################
# Configuration for all motors

# General
CURRENT_MAX = 10
ACCELERATION = 1000
VELOCITY = 50000

# StallGuard
THRESHOLD_SG = 3

# CoolStep
CURRENT_MIN = 0 # 0: CURRENT_MAX / 2, 1: CURRENT_MAX / 4
CURRENT_DOWN_STEP = 2 # 0 : Slow, 3: Instant
CURRENT_UP_STEP = 2 # 0 : Slow, 3: Instant
HYSTERESIS_WIDTH = 4
HYSTERESIS_START = 9
THRESHOLD_COOLSTEP = 0

################################################################################

pytrinamic.show_info()
connection_manager = ConnectionManager()
my_interface = connection_manager.connect()

shields = TmcEvalShield(my_interface, TMC5160_shield).shields

# Initialize all attached shields
for shield in shields:
    print("Rotating motor.")
    shield.set_axis_parameter(shield.AP.MaxCurrent, 0, CURRENT_MAX)
    shield.set_axis_parameter(shield.AP.MaxAcceleration, 0, ACCELERATION)
    shield.rotate(0, VELOCITY)

    # StallGuard settings
    shield.set_axis_parameter(shield.AP.SG2Threshold, 0, THRESHOLD_SG)

    # CoolStep settings
    shield.set_axis_parameter(shield.AP.SEIMIN, 0, CURRENT_MIN)
    shield.set_axis_parameter(shield.AP.SECDS, 0, CURRENT_DOWN_STEP)
    shield.set_axis_parameter(shield.AP.SECUS, 0, CURRENT_UP_STEP)
    shield.set_axis_parameter(shield.AP.smartEnergyHysteresis, 0, HYSTERESIS_WIDTH)
    shield.set_axis_parameter(shield.AP.smartEnergyHysteresisStart, 0, HYSTERESIS_START)
    shield.set_axis_parameter(shield.AP.smartEnergyThresholdSpeed, 0, THRESHOLD_COOLSTEP)

# Loop over all attached shields
while True:
    for shield in shields:
        print(f"Shield: {shield}, SGT: {shield.getAxisParameter(shield.AP.LoadValue, 0)}, Current: {shield.getAxisParameter(shield.AP.smartEnergyActualCurrent, 0)}")
    time.sleep(0.1)

# Demo exit, stop all motors
logger.info("Stopping all motors.")
for shield in shields:
    logger.info(f"Stopping motors for shield {shield}.")
    shield.stop(0)

my_interface.close()
