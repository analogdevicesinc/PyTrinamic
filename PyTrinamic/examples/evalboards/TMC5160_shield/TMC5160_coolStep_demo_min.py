#!/usr/bin/env python3
'''
Demonstration of the stallGuard feature of the TMC5160 (minimalistic).

Created on 20.03.2020

@author: LK
'''

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

import time

import PyTrinamic
from PyTrinamic.evalboards.TMC5160_shield import TMC5160_shield
from PyTrinamic.modules.TMC_EvalShield import TMC_EvalShield

PyTrinamic.showInfo()

from PyTrinamic.connections.ConnectionManager import ConnectionManager
connectionManager = ConnectionManager()
myInterface = connectionManager.connect()

shields = TMC_EvalShield(myInterface, TMC5160_shield).shields

# Initialize all attached shields
for shield in shields:
    print("Rotating motor.")
    shield.setAxisParameter(shield.APs.MaxCurrent, 0, CURRENT_MAX)
    shield.setAxisParameter(shield.APs.MaxAcceleration, 0, ACCELERATION)
    shield.rotate(0, VELOCITY)

    # StallGuard settings
    shield.setAxisParameter(shield.APs.SG2Threshold, 0, THRESHOLD_SG)

    # CoolStep settings
    shield.setAxisParameter(shield.APs.SEIMIN, 0, CURRENT_MIN)
    shield.setAxisParameter(shield.APs.SECDS, 0, CURRENT_DOWN_STEP)
    shield.setAxisParameter(shield.APs.SECUS, 0, CURRENT_UP_STEP)
    shield.setAxisParameter(shield.APs.smartEnergyHysteresis, 0, HYSTERESIS_WIDTH)
    shield.setAxisParameter(shield.APs.smartEnergyHysteresisStart, 0, HYSTERESIS_START)
    shield.setAxisParameter(shield.APs.smartEnergyThresholdSpeed, 0, THRESHOLD_COOLSTEP)

# Loop over all attached shields
while True:
    for shield in shields:
        print(f"Shield: {shield}, SGT: {shield.getAxisParameter(shield.APs.LoadValue, 0)}, Current: {shield.getAxisParameter(shield.APs.smartEnergyActualCurrent, 0)}")
    time.sleep(0.1)

# Demo exit, stop all motors
logger.info("Stopping all motors.")
for shield in shields:
    logger.info(f"Stopping motors for shield {shield}.")
    shield.stop(0)

myInterface.close()
