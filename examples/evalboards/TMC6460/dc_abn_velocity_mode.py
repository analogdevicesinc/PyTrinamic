#!/usr/bin/env python
################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

"""
This script configures the TMC6460 to run a test drive for a DC motor in
velocity mode (closed loop).
An ABN encoder used to generate angle feedback.

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

### Parameters #################################################################
# ABN sensor pulses-per-rotation (PPR).
# Note that the TMC6460 uses counts-per-rotation (CPR = PPR*4) internally.
ABN_PPR = 1024

# Note that only torque (and not flux) is used for DC motors
PI_CURRENT_P      = 125
PI_CURRENT_P_NORM = 0    # 0=NO_SHIFT, 1=RSHIFT_8
PI_CURRENT_I      = 250
PI_CURRENT_I_NORM = 1    # 0=NO_SHIFT, 1=RSHIFT_8

PI_VELOCITY_P_NORM = 0
PI_VELOCITY_I_NORM = 2

PI_VELOCITY_P = 300
PI_VELOCITY_I = 3000

TARGET_VELOCITY = 30_000

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
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.LS_RES_ON.choice.RES_112_MOHM) # (default: RES_55_MOHM) allows the widest current range
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.DRV_EN_BIT, 1)

    # PWM SETUP
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.PWM_PERIOD.MAX_COUNT, 600) # f_pwm = 120MHz/max_count; 600 -> 200kHz
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.PWM_PERIOD.AUTO_KIRCHHOFF_LIM, 32_768)
        # Auto Kirchhoff limit must be set to 50% duty cycle for DC motors.
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.PWM.SV_MODE.choice.HARMONIC) # (default: HARMONIC)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.PWM.CHOP.choice.CENTERED) # (default: CENTERED)

    # MOTOR SETUP
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTOR_TYPE.choice.DC)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.N_POLE_PAIRS, 1)
        # For DC motors pole pairs must be set to 1.

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
    tmc6460_eval.write(TMC6460.REGMAP.ABN.CONFIG.INV_DIR, 1) # use if encoder's direction is inverted
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
    # will be routed to the velocity meter and/or position decoder at a later step.

    # Channel A will be used for velocity and position feedback
    # (Phi E feedback is not needed for DC motors)
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_A.SRC_SEL_A.choice.ABN_1_FREE)
    #tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_A.SRC_SEL_A.choice.ABN_2_FREE)
        # ABN_1_FREE option makes use of an internal 'ABN_FREE' value (not available as
        # a register), this option should be used for velocity and position feedback
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_A.CPR_INV_A, 256)
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

    # VELOCITY AND POSITION FEEDBACK SETUP
    # The input for the velocity meter and the position decoder can be set to
    # track the lookup table (LUT) channel A or B, which accordingly come from
    # the previously configured feedback channels A and B.  The LUT is
    # deactivated by default, which results in the feedback channels going
    # through unmodified.

    # Make sure the LUT is disabled
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.LUT.LOOKUP_A_EN, 0)

    # Velocity Meter(s)
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.OUTPUT_CONF.POSITION_SRC.choice.LOOKUP_A)
        # Both velocity meters share the same input; in this case make use the LUT
        # channel A, which was previously configured with the source of ABN_1_FREE
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.VELOCITY_FRQ_CONF.VELOCITY_SAMPLING, 0)
        # Downsampling by skipping every X PWM cycles (default=0)
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.VELOCITY_FRQ_CONF.VELOCITY_SCALING, 6991)
        # vel_scaling = 2^24/60,000,000 * f_PWM/(VEL_SAMPLING+1),
        # f_PWM should be calculated according to the value set in MCC_CONFIG.PWM_PERIOD.MAX_COUNT
        # This value is used so that the output of both velocity meters have the same resulting scale
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.VELOCITY_FRQ_CONF.VELOCITY_SYNC_SRC.choice.PWM_Z) # (default: PWM_Z)
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.VELOCITY_PER_CONF.POS_DEV_TIMER, 0xFFF0) # (default=0xFFF0)
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.VELOCITY_PER_CONF.POS_DEV_MIN, 1) # (default=1)
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.VELOCITY_PER_FILTER.FILTER_WIDTH, 3) # moving average filter window width (default=0)
        # The three writes above are used to configure the slow velocity meter
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.OUTPUT_CONF.VELOCITY_SELECTION.choice.VELOCITY_PER)
        # Only one velocity meter can be used as an input for the FOC controller,
        # however, by configuring both meters already we allow to change
        # which meter is used at a later point, even on-the-fly 

    # Position decoder
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.OUTPUT_CONF.VELOCITY_SRC.choice.LOOKUP_A)
        # Position decoder to use LUT channel A, thus the ABN_1_FREE

    # PI CONTROLLER SETUP
    # The coefficients for the PI controller will vary from motor to motor and from
    # setup to setup; ideally they should be tuned on the final mechanical setup.
    # The values provided here are specific to the motor I'm using

    # Torque and flux PI
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_CONFIG.CURRENT_NORM_P, PI_CURRENT_P_NORM)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_CONFIG.CURRENT_NORM_I, PI_CURRENT_I_NORM)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_COEFF.TORQUE_P, PI_CURRENT_P)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_COEFF.TORQUE_I, PI_CURRENT_I)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_FLUX_COEFF.FLUX_P, 0)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_FLUX_COEFF.FLUX_I, 0)

    # Velocity PI
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_CONFIG.VELOCITY_NORM_P, PI_VELOCITY_P_NORM)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_CONFIG.VELOCITY_NORM_I, PI_VELOCITY_I_NORM)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_VELOCITY_COEFF.VELOCITY_P, PI_VELOCITY_P)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_VELOCITY_COEFF.VELOCITY_I, PI_VELOCITY_I)

    # Set the ramper generator values
    tmc6460_eval.write(TMC6460.REGMAP.RAMPER.V1.V1, 0)
    tmc6460_eval.write(TMC6460.REGMAP.RAMPER.V2.V2, 0)
    tmc6460_eval.write(TMC6460.REGMAP.RAMPER.A_MAX.A_MAX, 100)

    # End of configuration

    # INITIALIZE THE ABN ENCODER
    # Unlike BLDC motors, DC motors don't need this alignment step, as
    # the concept of an electrical angle does not really apply to them

    # PERFORM THE TEST DRIVE
    print()
    print("Setting velocity mode with ramper enabled...")
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_USE_PHI_E, 0)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTION_MODE.choice.VELOCITY)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_MODE.choice.RAMP_VELOCITY)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_EN, 1)

    # Move the motor in velocity mode in both directions for a few seconds
    print("Turning the motor in velocity mode (closed loop)...")
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_VELOCITY_TARGET.PID_VELOCITY_TARGET, TARGET_VELOCITY)
    for i in reversed(range(5)):
        print(f"{i+1} s remaining", flush=True)
        time.sleep(1)

    print("Turning the motor in the opposite direction...")
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_VELOCITY_TARGET.PID_VELOCITY_TARGET, -TARGET_VELOCITY)
    for i in reversed(range(5)):
        print(f"{i+1} s remaining", flush=True)
        time.sleep(1)

    print("Stopping motor...")
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_VELOCITY_TARGET.PID_VELOCITY_TARGET, 0)
    time.sleep(2)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTION_MODE.choice.PWM_OFF)
