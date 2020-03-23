#!/usr/bin/env python3
'''
Demonstration of the cooolStep feature of the TMC5160.
The sensorless stallGaurd technology calculates the remaining available load for
a motor. If that remaining load exceeds a specified value (i.e. load decreases),
coolStep will automatically decrease the motor current to save energy.
If the remaining load undercuts a specified value, coolStep will
automatically increase the motor current to prevent step loss.

This demo performs an interactive stallGuard initialization to set up the
sensitivity and thresholds. After that you are free to play around with this
feature.

All actions will be performed on all attached shields simultaneously, so you can
try it with multiple axes aswell.

Created on 23.03.2020

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
from PyTrinamic.features.StallGuard import StallGuard

parser = argparse.ArgumentParser(description='coolStep demo')
parser.add_argument('-t', '--target-velocity', dest='velocity', action='store', nargs=1, type=int, default=[100000],
                    help='Target velocity for demonstration on all axes. Default: %(default)s.')
parser.add_argument('-a', '--acceleration', dest='acceleration', action='store', nargs=1, type=int, default=[1000],
                    help='Acceleration used for ramping to target velocity. Default: %(default)s.')
parser.add_argument('-c', '--current', dest='current', action='store', nargs=1, type=int, default=[16],
                    help='Current Scaler value while motor is running. Default: %(default)s.')
parser.add_argument('--current-minimum', dest='seimin', action='store', nargs=1, type=int, default=[1], choices=range(0, 1),
                    help='Minimal current after decreasing. 0: maximum_current / 2, 1: maximum_current / 4. Default: %(default)s.')
parser.add_argument('--current-down-step', dest='down', action='store', nargs=1, type=int, default=[2], choices=range(0, 3),
                    help='Reaction speed for decreasing. 0: React slowly with ramping, 3: React instantly. Default: %(default)s.')
parser.add_argument('--current-up-step', dest='up', action='store', nargs=1, type=int, default=[2], choices=range(0, 3),
                    help='Reaction speed for increasing. 0: React slowly with ramping, 3: React instantly. Default: %(default)s.')
parser.add_argument('--hysteresis-width', dest='hwidth', action='store', nargs=1, type=int, default=[4], choices=range(0, 15),
                    help='CoolStep hysteresis window width in [1/16 SGT_MAX]. Default: %(default)s.')
parser.add_argument('--hysteresis-start', dest='hstart', action='store', nargs=1, type=int, default=[9], choices=range(0, 15),
                    help='CoolStep hysteresis window start in [1/16 SGT_MAX]. Default: %(default)s.')
parser.add_argument('--coolstep-threshold', dest='coolstep_threshold', action='store', nargs=1, type=int, default=[0],
                    help='Velocity threshold, above which CoolStep becomes active. Default: %(default)s.')
parser.add_argument('-v', '--verbosity', dest='verbosity', action='store', nargs=1, type=int, choices=[logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL], default=[logging.INFO],
                    help=f'Verbosity level (default: %(default)s, {logging.DEBUG}: DEBUG, {logging.INFO}: INFO, {logging.WARNING}: WARNING, {logging.ERROR}: ERROR, {logging.CRITICAL}: CRITICAL)')

args = parser.parse_known_args()[0]
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
    shield.setAxisParameter(shield.APs.MaxCurrent, 0, args.current[0])
    shield.setAxisParameter(shield.APs.MaxAcceleration, 0, args.acceleration[0])
    shield.rotate(0, args.velocity[0])

    StallGuard(shield, sys.argv, logger).calibrate_middle()

    shield.setAxisParameter(shield.APs.SEIMIN, 0, args.seimin[0])
    shield.setAxisParameter(shield.APs.SECDS, 0, args.down[0])
    shield.setAxisParameter(shield.APs.SECUS, 0, args.up[0])
    shield.setAxisParameter(shield.APs.smartEnergyHysteresis, 0, args.hwidth[0])
    shield.setAxisParameter(shield.APs.smartEnergyHysteresisStart, 0, args.hstart[0])
    shield.setAxisParameter(shield.APs.smartEnergyThresholdSpeed, 0, args.coolstep_threshold[0])

print("Initialization is done. You can now play around with applying and releasing loads and see how the current gets adjusted.")
input("Press enter to continue ...")

def handle_key():
    while True:
        ch = msvcrt.getch()
        if ch == b'e':
            exit()

t = Thread(target=handle_key)
t.start()

# Loop over all attached shields
while True:
    status = ""
    for shield in shields:
        sgt = shield.getAxisParameter(shield.APs.LoadValue, 0)
        status = status + f"Shield: {shield}, SGT: {sgt}, Current: {shield.getAxisParameter(shield.APs.smartEnergyActualCurrent, 0)}\n"
    status = status + """
    Keyboard shortcuts:
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
