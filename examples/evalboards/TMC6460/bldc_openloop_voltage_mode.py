#!/usr/bin/env python
################################################################################
# Copyright © 2026 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
This script configures and controls a motor using the TMC6460 evaluation board in voltage mode.
The script assumes that a BLDC motor is connected to the evaluation board.
"""

import time

from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import TMC6460
from pytrinamic.evalboards import TMC6460_eval
from pytrinamic.tmcl import TMCLCommand

# # Uncomment these lines to enable logging of all communication
# import logging
# import sys
# logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

### Parameters #################################################################
N_POLE_PAIRS = 4

OPENLOOP_VELOCITY = 2000
OPENLOOP_VOLTAGE  = 1500

################################################################################

with ConnectionManager().connect() as my_interface:
    tmc6460_eval = TMC6460_eval(my_interface)

    # Motor setup
    print("Configuring motor settings...")
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTOR_TYPE.choice.BLDC)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.N_POLE_PAIRS, N_POLE_PAIRS)

    # ADC and CSA setup
    tmc6460_eval.write(TMC6460.REGMAP.MCC_ADC.CSA_GAIN.CSA_GAIN.choice.X1) # (default: x1 gain)

    # Gate driver setup
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.USE_INTERNAL_R_REF, 0) # external is more precise over temperature (default: 1)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.SLEW_RATE.choice.SR_400_V_PER_US) # (default: SR_200_V_PER_US)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.LS_RES_ON.choice.RES_55_MOHM) # (default: RES_55_MOHM) allows the widest current range
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.DRV_EN_BIT, 1)

    # PWM setup
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.PWM_PERIOD.MAX_COUNT, 4800)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.PWM.SV_MODE.choice.HARMONIC)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.PWM.CHOP.choice.CENTERED)

    # Set ramper parameters for velocity movement
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_MODE.choice.RAMP_VELOCITY)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_USE_PHI_E, 1)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_EN, 1)
    tmc6460_eval.write(TMC6460.REGMAP.RAMPER.A1.A1, 100)
    tmc6460_eval.write(TMC6460.REGMAP.RAMPER.A2.A2, 200)
    tmc6460_eval.write(TMC6460.REGMAP.RAMPER.A_MAX.A_MAX, 100)

    # Enable voltage control mode
    tmc6460_eval.write(TMC6460.REGMAP.EXT_CTRL.VOLTAGE, 0)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTION_MODE.choice.VOLTAGE_EXT)

    # Start motor
    print("Turning motor...")
    tmc6460_eval.write(TMC6460.REGMAP.EXT_CTRL.VOLTAGE.UD, OPENLOOP_VOLTAGE)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_VELOCITY_TARGET.PID_VELOCITY_TARGET, OPENLOOP_VELOCITY)

    start_time = time.time()
    while (time.time() - start_time) < 5:
        time.sleep(0.1)

    # Stop motor
    print("Stopping motor...")
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_VELOCITY_TARGET.PID_VELOCITY_TARGET, 0)
    tmc6460_eval.write(TMC6460.REGMAP.EXT_CTRL.VOLTAGE, 0)
    time.sleep(1)

    print("Turning system off...")
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTION_MODE.choice.PWM_OFF)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.DRV_EN_BIT, 0)
