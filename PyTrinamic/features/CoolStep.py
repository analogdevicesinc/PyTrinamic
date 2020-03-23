# Created on: 23.03.2020
# Author: LK

import argparse
import logging
import time

import PyTrinamic
from PyTrinamic.features.Feature import Feature
from PyTrinamic.features.StallGuard import StallGuard

class CoolStep(Feature):

    def __init__(self, module, argList=None, logger=logging.getLogger(__name__)):
        super().__init__(module)

        self.__arglist = argList
        self.__logger = logger

        parser = argparse.ArgumentParser(description='coolStep calibration')
        parser.add_argument('-t', '--target-velocity', dest='velocity', action='store', nargs=1, type=int, default=[100000],
                            help='Target velocity for demonstration on all axes. Default: %(default)s.')
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
        parser.add_argument('-i', '--interactive', dest='interactive', action='store_true',
                            help='Interactive CoolStep hysteresis window calibration.')
        args = parser.parse_known_args(argList)[0]

        self.__threshold = args.coolstep_threshold[0]
        self.__interactive = args.interactive

        logger.debug(f"Minimum current: {args.seimin[0]}")
        logger.debug(f"Current down step: {args.down[0]}")
        logger.debug(f"Current up step: {args.up[0]}")
        logger.debug(f"Hysteresis width: {args.hwidth[0]}")
        logger.debug(f"Hysteresis start: {args.hstart[0]}")
        logger.debug(f"CoolStep threshold velocity: {self.__threshold}")
        logger.debug(f"Interactive: {self.__interactive}")

        logger.info(f"Minimum current: {args.seimin[0]} => {args.current[0] / (1 << args.seimin[0])}")
        logger.info(f"Hysteresis start: {args.hstart[0]} => {args.hstart[0] * 64}")
        logger.info(f"Hysteresis width: {args.hwidth[0]} => {args.hwidth[0] * 64}")
        logger.info(f"Hysteresis end: {args.hstart[0] + args.hwidth[0]} => {(args.hstart[0] + args.hwidth[0]) * 64}")

        self._module.setAxisParameter(self._module.APs.SEIMIN, 0, args.seimin[0])
        self._module.setAxisParameter(self._module.APs.SECDS, 0, args.down[0])
        self._module.setAxisParameter(self._module.APs.SECUS, 0, args.up[0])
        self._module.setAxisParameter(self._module.APs.smartEnergyHysteresis, 0, args.hwidth[0])
        self._module.setAxisParameter(self._module.APs.smartEnergyHysteresisStart, 0, args.hstart[0])
        self._module.setAxisParameter(self._module.APs.smartEnergyThresholdSpeed, 0, args.velocity[0] + 1)

    def calibrate(self):
        StallGuard(self._module, self.__arglist, self.__logger).calibrate_middle()

        if(self.__interactive):
            print("Now, apply some load to the motor, at which you want the current to increase automatically.")
            input("Press enter to continue ...")

            for i in range(3):
                self.__logger.info(f"Starting calibration in {3-i} seconds.")
                time.sleep(1.0)

            hstart = int(round((self._module.getAxisParameter(self._module.APs.LoadValue, 0) / 1023) * 15, 0))
            self.__logger.info(f"Hysteresis start: {hstart}")

            print("Now, release the load. Let the motor run freely.")
            input("Press enter to continue ...")

            hend = int(round((self._module.getAxisParameter(self._module.APs.LoadValue, 0) / 1023) * 15, 0))
            self.__logger.info(f"Hysteresis end: {hend}")

            hwidth = hend - hstart
            self.__logger.info(f"Hysteresis window width: {hwidth}")

            self._module.setAxisParameter(self._module.APs.smartEnergyHysteresis, 0, hwidth)
            self._module.setAxisParameter(self._module.APs.smartEnergyHysteresisStart, 0, hstart)

        self._module.setAxisParameter(self._module.APs.smartEnergyThresholdSpeed, 0, self.__threshold)
