#!/usr/bin/env python3
'''
Demonstration of the stallGuard feature of the TMC5160.
The sensorless stallGaurd technology calculates the remaining available load for
a motor and detects incoming stalls. If such a stall is detected, the motor
driver will automatically stop to prevent damage and miscalculations.

This demo performs an interactive stallGuard initialization to set up the
sensitivity and thresholds. After that you are free to play around with this
feature.

All actions will be performed on all attached shields simultaneously, so you can
try it with multiple axes aswell.

Created on 20.03.2020

@author: LK
'''

import argparse
import os
import logging
import time
import sys

import msvcrt

from threading import Thread

import PyTrinamic
from PyTrinamic.evalboards.TMC5160_shield import TMC5160_shield
from PyTrinamic.modules.TMC_EvalShield import TMC_EvalShield

parser = argparse.ArgumentParser(description='stallGuard demo')
parser.add_argument('-t', '--target-velocity', dest='velocity', action='store', nargs=1, type=int, default=50000,
                    help='Target velocity for demonstration on all axes. Default: %(default)s.')
parser.add_argument('-a', '--acceleration', dest='acceleration', action='store', nargs=1, type=int, default=1000,
                    help='Acceleration used for ramping to target velocity. Default: %(default)s.')
parser.add_argument('-c', '--current', dest='current', action='store', nargs=1, type=int, default=5,
                    help='Current Scaler value while motor is running. Default: %(default)s.')
parser.add_argument('-e', '--threshold-velocity', dest='threshold', action='store', nargs=1, type=int, default=1,
                    help='Velocity threshold, above which stallGuard is enabled. Default: %(default)s.')
parser.add_argument('-v', '--verbosity', dest='verbosity', action='store', nargs=1, type=int, choices=[logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL], default=[logging.INFO],
                    help=f'Verbosity level (default: %(default)s, {logging.DEBUG}: DEBUG, {logging.INFO}: INFO, {logging.WARNING}: WARNING, {logging.ERROR}: ERROR, {logging.CRITICAL}: CRITICAL)')

args = parser.parse_args()
verbosity = args.verbosity[0]

logger = logging.getLogger(__name__)
logger.setLevel(verbosity)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(verbosity)
formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s")
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)

PyTrinamic.showInfo()

from PyTrinamic.connections.ConnectionManager import ConnectionManager
connectionManager = ConnectionManager()
myInterface = connectionManager.connect()

shields = TMC_EvalShield(myInterface, TMC5160_shield).shields

# Initialize all attached shields
for shield in shields:
    logger.info(f"Initializing motor at shield {shield}.")

    logger.info("Rotating motor.")
    shield.setAxisParameter(shield.APs.MaxCurrent, 0, args.current)
    shield.setAxisParameter(shield.APs.MaxAcceleration, 0, args.acceleration)
    shield.setAxisParameter(shield.APs.smartEnergyStallVelocity, 0, 0)
    shield.rotate(0, args.velocity)

    print("Now, do apply some load to the motor, at which you want it to stop automatically.")
    input("Press any key to continue ...")

    for i in range(3):
        logger.info(f"Starting calibration in {3-i} seconds.")
        time.sleep(1.0)

    logger.info(f"Calibrating SGT.")
    sgthresh = 0
    sgt = 0
    while((sgt == 0) and (sgthresh < 64)):
        logger.info(f"SGT too low, increasing threshold to {sgthresh}.")
        shield.setAxisParameter(shield.APs.SG2Threshold, 0, sgthresh)
        sgthresh = sgthresh + 1
        time.sleep(0.1)
        sgt = shield.getAxisParameter(shield.APs.LoadValue, 0)
        logger.info(f"SGT load: {sgt}")
    shield.setAxisParameter(shield.APs.SG2Threshold, 0, sgthresh - 1)
    logger.info(f"Calibration done. Now release the load.")

    input("Press any key to continue ...")

    shield.setAxisParameter(shield.APs.smartEnergyStallVelocity, 0, args.threshold)

logger.info("Initialization is done. You can now play around with applying loads and see if the motor stops.")

def handle_key():
    while True:
        ch = msvcrt.getch()
        if ch == b'r':
            logger.info("Resetting stall for all shields.")
            for shield in shields:
                logger.info(f"Resetting stall for {shield}.")
                shield.setAxisParameter(shield.APs.smartEnergyStallVelocity, 0, 0)
                time.sleep(1)
                shield.setAxisParameter(shield.APs.smartEnergyStallVelocity, 0, args.threshold)
        elif ch == b'e':
            exit()

t = Thread(target=handle_key)
t.start()

# Loop over all attached shields
while True:
    status = ""
    for shield in shields:
        sgt = shield.getAxisParameter(shield.APs.LoadValue, 0)
        status = status + f"Shield: {shield}, SGT: {sgt}\n"
    status = status + """
    Keyboard shortcuts:
    'r': Reset stall on all motors.
    'e': Exit the demo."""
    os.system('cls' if os.name=='nt' else 'clear')
    print(status)
    time.sleep(0.1)
    if not t.isAlive():
        break

# Demo exit, stop all motors
logger.info("Stopping all motors.")
for shield in shields:
    logger.info(f"Stopping motors for shield {shield}.")
    shield.stop(0)

myInterface.close()
