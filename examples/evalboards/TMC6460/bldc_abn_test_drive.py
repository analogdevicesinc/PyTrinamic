#!/usr/bin/env python
################################################################################
# Copyright © 2026 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
This script configures the TMC6460 to run a test drive in torque mode (closed loop).
An ABN encoder is initialized and used to generate Phi E feedback.

This example assumes the use of the TMC6460-EVAL board and an ABN encoder
connected to the ENC_A, ENC_B, ENC_N pins.
Default torque and flux PI coefficients are also set in the script,
these should also be changed according to the used motor.

Some commented out examples to configure the use of the second encoder interface
are also included.
"""

import time

from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import TMC6460
from pytrinamic.evalboards import TMC6460_eval

# # Uncomment these lines to enable logging of all communication
# import logging
# import sys
# logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

### Parameters #################################################################
N_POLE_PAIRS = 4

# ABN sensor pulses-per-rotation (PPR).
# Note that the TMC6460 uses counts-per-rotation (CPR = PPR*4) internally.
ABN_PPR = 1024

INITIALIZATION_CURRENT = 5000 # Used during initial alignment
TARGET_CURRENT         = 2000 # Used during test drive

# These are default PI values that are very conservative
PI_CURRENT_P      = 200
PI_CURRENT_P_NORM = 1    # 0=NO_SHIFT, 1=RSHIFT_8
PI_CURRENT_I      = 250
PI_CURRENT_I_NORM = 1    # 0=NO_SHIFT, 1=RSHIFT_8

################################################################################
with ConnectionManager().connect() as my_interface:
    tmc6460_eval = TMC6460_eval(my_interface)

    print()
    print("Configuring the TMC6460...")

    # ADC AND CSA SETUP
    tmc6460_eval.write(TMC6460.REGMAP.MCC_ADC.CSA_GAIN.CSA_GAIN.choice.X1) # (default: x1 gain)

    # GATE DRIVER SETUP
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.USE_INTERNAL_R_REF, 0) # external is more precise over temperature (default: 1)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.SLEW_RATE.choice.SR_400_V_PER_US) # (default: SR_200_V_PER_US)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.LS_RES_ON.choice.RES_55_MOHM) # (default: RES_55_MOHM) allows the widest current range
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.DRV_EN_BIT, 1)

    # PWM SETUP
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.PWM_PERIOD.MAX_COUNT, 4800) # f_pwm = 120MHz/max_count; 4800 -> 25kHz
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.PWM.SV_MODE.choice.HARMONIC) # (default: HARMONIC)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.PWM.CHOP.choice.CENTERED) # (default: CENTERED)

    # MOTOR SETUP
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTOR_TYPE.choice.BLDC)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.N_POLE_PAIRS, N_POLE_PAIRS)

    # IO MATRIX SETUP
    # Depending on which pins are used for the ABN encoder(s), the IO matrix has to be set.

    # Using pins ENC_A, ENC_B, ENC_N (14, 15, 16, resp.):
    # This is strictly not needed if IC has been reset, as these are the default values.
    tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_MATRIX.PIN_ENC_A.choice.ENC_A)
    tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_MATRIX.PIN_ENC_B.choice.ENC_B)
    tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_MATRIX.PIN_ENC_N.choice.ENC_N)

    # Example when connecting an ABN encoder to pins HALL_U, HALL_V, HALL_W (17, 18, 19, resp.):
    #tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_MATRIX.PIN_HALL_U.choice.ENC2_A)
    #tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_MATRIX.PIN_HALL_V.choice.ENC2_B)
    #tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_MATRIX.PIN_HALL_W.choice.ENC2_N)

    # ABN ENCODER SETUP

    # The 'ABN' register block should be used when connecting
    # an encoder to the ABN main pins, i.e., ENC_A, ENC_B, ENC_N.
    tmc6460_eval.write(TMC6460.REGMAP.ABN.CONFIG.CPR, (ABN_PPR*4) - 1) # should be the encoder's CPR minus one
    tmc6460_eval.write(TMC6460.REGMAP.ABN.CONFIG.INV_DIR, 0) # use if encoder's direction is inverted
    tmc6460_eval.write(TMC6460.REGMAP.ABN.CONFIG.COMBINED_N.choice.ALL) # allows more precise N pulse detection
    tmc6460_eval.write(TMC6460.REGMAP.ABN.CONFIG.CLN.choice.OFF)

    # The 'ABN2' register block should be used when connecting
    # an encoder to pins HALL_U, HALL_V, HALL_W, however.
    #tmc6460_eval.write(TMC6460.REGMAP.ABN2.CONFIG.CPR, (ABN_PPR*4) - 1)
    #tmc6460_eval.write(TMC6460.REGMAP.ABN2.CONFIG.INV_DIR, 0)
    #tmc6460_eval.write(TMC6460.REGMAP.ABN2.CONFIG.COMBINED_N.choice.ALL)
    #tmc6460_eval.write(TMC6460.REGMAP.ABN2.CONFIG.CLN.choice.OFF)

    # FEEDBACK INPUT SETUP
    # Depending on the used feedback inputs, channel A and B of the feedback engine have to be set.
    # This only sets which feedback input to use for each of the channels; the output of the channels
    # will be routed to the Phi E generator, velocity meter and/or position decoder at a later step.

    ### When using a single ABN encoder:
    # Channel A will be used for Phi E feedback
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_A.SRC_SEL_A.choice.ABN_1)
    #tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_A.SRC_SEL_A.choice.ABN_2)
        # ABN_1 option makes use of value in register 'ABN.COUNT' as
        # feedback source, this option should be used for Phi E generation
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_A.CPR_INV_A, 2**24 // (ABN_PPR*4))
        # cpr_inv = 2^24 / cpr_encoder, this is valid when using ABN for Phi E generation
    # Channel B will be used for velocity and position feedback
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_B.SRC_SEL_B.choice.ABN_1_FREE)
    #tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_B.SRC_SEL_B.choice.ABN_2_FREE)
        # ABN_1_FREE option makes use of an internal 'ABN_FREE' value (not available as
        # a register), this option should be used for velocity and position feedback
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_B.CPR_INV_B, 256)
        # cpr_inv = some power of 2 >= 256, this is valid when using the *_FREE source options.
        # To understand the logic behind this, consider that 'ABN_FREE' counts the encoder's
        # pulses without resetting the count on every revolution (as 'ABN.COUNT' does);
        # Then consider what the 16-bit conversion block does: it multiplies the output of the
        # chosen source by cpr_inv and right shifts the result by 8 (effectively dividing by 256).
        # Thus, if we want to keep the ABN_FREE count transparent, we need a cpr_inv of 256.
        # Using 256 has the advantage of reflecting the 'truest' resolution of the
        # encoder in the velocity and position values.
        # Using bigger powers of 2 can be useful when the resulting velocity (or position)
        # values are too small, which could lead to problems with the ramper.

    ### When using two ABN encoders:
    # Example when using two separate ABN encoders e.g. first one in channel A for
    # Phi E generation, second one after a gearbox in channel B for velocity and position
    # tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_A.SRC_SEL_A.choice.ABN_1)
    # tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_A.CPR_INV_A, (ABN_PPR*4) - 1)
    # tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_B.SRC_SEL_B.choice.ABN_2_FREE)
    # tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_B.CPR_INV_B, 256)

    # PHI E, VELOCITY AND POSITION FEEDBACK SETUP
    # The input for the Phi E generator, the velocity meter and the position decoder
    # can be set to track the lookup table (LUT) channel A or B, which accordingly
    # come from the previously configured feedback channels A and B.
    # The LUT is deactivated by default, which results in the feedback channels
    # going through unmodified.
    # An additional input option is available for the Phi E generator, which takes
    # the output of the LUT and creates extrapolated values from it. This would
    # generally be used for very low line count encoders or Hall sensors.

    # Make sure the LUT is disabled
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.LUT.LOOKUP_A_EN, 0)
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.LUT.LOOKUP_B_EN, 0)

    # Phi E generator
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.OUTPUT_CONF.PHI_E_SRC.choice.LOOKUP_A)
        # Phi E generator to use the LUT channel A, as mentioned before the LUT
        # itself is not enabled, so this effectively uses feedback channel A,
        # which was previously configured with the source of ABN_1.
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.OUTPUT_CONF.PHI_E_MUL_FACTOR, N_POLE_PAIRS)
        # mul_factor = phi encoder to phi e ratio,
        # for ABN encoders this is equal to the pole pair number

    # Velocity Meter(s)
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.OUTPUT_CONF.POSITION_SRC.choice.LOOKUP_B)
        # Both velocity meters share the same input; in this case make use of the LUT
        # channel B, which was previously configured with the source of ABN_1_FREE
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.VELOCITY_FRQ_CONF.VELOCITY_SAMPLING, 0)
        # Downsampling by skipping every X PWM cycles (default=0)
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.VELOCITY_FRQ_CONF.VELOCITY_SCALING, 6991)
        # vel_scaling = 2^24/60000000 * f_PWM/(VEL_SAMPLING+1),
        # f_PWM should be calculated accoriding to the value set in MCC_CONFIG.PWM_PERIOD.MAX_COUNT
        # This value is used so that the output of both velocity meters have the same resulting scale
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.VELOCITY_FRQ_CONF.VELOCITY_SYNC_SRC.choice.PWM_Z) # (default: PWM_Z)
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.VELOCITY_PER_CONF.POS_DEV_TIMER, 0xFFF0) # (default=0xFFF0)
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.VELOCITY_PER_CONF.POS_DEV_MIN, 1) # (default=1)
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.VELOCITY_PER_FILTER.FILTER_WIDTH, 3) # moving average filter window width (default=0)
        # The three writes above are used to configure the period velocity meter
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.OUTPUT_CONF.VELOCITY_SELECTION.choice.VELOCITY_PER)
        # Only one velocity meter can be used as an input for the FOC controller,
        # however, by configuring both meters already we allow to change
        # which meter is used at a later point, even on-the-fly 

    # Position decoder
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.OUTPUT_CONF.VELOCITY_SRC.choice.LOOKUP_B)
        # Position decoder to use LUT channel B, thus the ABN_1_FREE

    # PI CONTROLLER SETUP
    # The coefficients for the PI controller will vary from motor to motor and from
    # setup to setup; ideally they should be tuned on the final mechanical setup.
    # The values provided here are specific to the motor I'm using

    # Torque and flux PI
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_CONFIG.CURRENT_NORM_P, PI_CURRENT_P_NORM)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_CONFIG.CURRENT_NORM_I, PI_CURRENT_I_NORM)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_FLUX_COEFF.FLUX_P, PI_CURRENT_P)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_FLUX_COEFF.FLUX_I, PI_CURRENT_I)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_COEFF.TORQUE_P, PI_CURRENT_P)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_COEFF.TORQUE_I, PI_CURRENT_I)

    # End of configuration

    # INITIALIZE THE ABN ENCODER
    # Initialization means to align the Phi E that comes from the encoder with
    # the motor's Phi E; this is needed for the FOC to work in closed loop

    print()
    print("Initializing the ABN encoder via count reset (no absolute position obtained)...")
    # Reset the ramper position and make sure the ramper's Phi E offset has no offset relative to it
    tmc6460_eval.write(TMC6460.REGMAP.RAMPER.POSITION.POSITION, 0)
    tmc6460_eval.write(TMC6460.REGMAP.RAMPER.PHI_E.PHI_E_OFFSET, 0)

    # Set ramper for position mode and use it to generate a Phi E
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_MODE.choice.RAMP_POSITION)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_EN, True)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_USE_PHI_E, True)

    # Enable torque control mode (current open loop) and set a fixed flux without any torque
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET.PID_TORQUE_TARGET, 0)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTION_MODE.choice.TORQUE)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET.PID_FLUX_TARGET, INITIALIZATION_CURRENT)

    # Wait for motor to settle
    time.sleep(1)

    # At this point the motor will be in a known position, electrically speaking at least;
    # This is not an absolute position, however, as there are N electrical revolutions for
    # every mechanical revolution of the motor (with N equal to the motor's pole pair count)

    # Clear the ABN count, this ensures the encoder and the motor's Phi E are in sync
    tmc6460_eval.write(TMC6460.REGMAP.ABN.COUNT.COUNT, 0)
    #tmc6460_eval.write(TMC6460.REGMAP.ABN2.COUNT.COUNT, 0)

    # Clear the controller's actual position too;
    # this is strictly not necessary at this point but nice to also have in sync
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_POSITION_ACTUAL.PID_POSITION_ACTUAL, 0)

    # Turn down the set flux
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET.PID_FLUX_TARGET, 0)

    print("Encoder initialized")
    time.sleep(1)

    # PERFORM THE TEST DRIVE
    # When turning the motor in torque mode with a set torque, 
    # the motor will simply spin as fast as possible;
    # we do this for some seconds here to show that the ABN was correctly
    # initialized and it is correctly being used as a Phi E source

    print()
    print("Turning the motor in torque mode (current closed loop)...")
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_USE_PHI_E, False)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET.PID_TORQUE_TARGET, TARGET_CURRENT)
    for i in reversed(range(5)):
        print(f"{i+1} s remaining", flush=True)
        time.sleep(1)

    print("Stopping motor...")
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET.PID_TORQUE_TARGET, 0)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTION_MODE.choice.PWM_OFF)
