#!/usr/bin/env python
################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

"""
This script configures the TMC6460 to run a test drive in torque mode (closed loop).
A Hall sensor is used to generate Phi E feedback; by default, a Hall sensor Phi E
offset will be estimated for the connected motor; once an offset is found, the
script can be modified to make use of such offset and skip the estimation step.

The Hall sensor is assumed to be connected to the Hall connector of the eval.
Torque and flux PI coefficients are also set in the script,
these should also be changed according to the used motor.
"""

import time

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import TMC6460
from pytrinamic.evalboards import TMC6460_eval

# # Uncomment these lines to enable logging of all communication
# import logging
# import sys
# logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
# # matplotlib and its dependencies can be noisy at the DEBUG level
# # Turn them down to not pollute our logging output
# logging.getLogger("matplotlib").setLevel(logging.WARN)
# logging.getLogger("PIL").setLevel(logging.WARN)

### Parameters #################################################################

FIND_NEW_HALL_OFFSET = True
SHOW_HALL_OFFSET_PLOTS = True
PRESET_HALL_OFFSET = 0
PERFORM_TEST_DRIVE = False

HALL_IO_INVERSION = False
# 0-5 : HALL.HALL_CONFIG.HALL_MAP
# For a correctly wired hall sensor, the correct mapping value is 3
# If the wiring is wrong, it can be compensated using this setting.
HALL_MAPPING_VALUE = 3

N_POLE_PAIRS = 4

# Used during hall offset identification
OPENLOOP_VELOCITY = 100_000 # Should be at least 50000 so extrapolation happens
OPENLOOP_CURRENT  = 10000

# Used during hall test drive
TARGET_CURRENT    = 10000

# These are default PI values that are very conservative
PI_CURRENT_P      = 200
PI_CURRENT_P_NORM = 1    # 0=NO_SHIFT, 1=RSHIFT_8
PI_CURRENT_I      = 250
PI_CURRENT_I_NORM = 1    # 0=NO_SHIFT, 1=RSHIFT_8

################################################################################

if not PERFORM_TEST_DRIVE and not FIND_NEW_HALL_OFFSET:
    print("Invalid configuration")
    exit(1)

if SHOW_HALL_OFFSET_PLOTS and not plt:
    print("Script is set to show plots but Matplotlib library was not found.")
    print("Either disable showing the plots or install the needed library.")
    exit()

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
    # Depending on which pins are used for the Hall sensor, the IO matrix has to be set.
    # Unlike the case of ABN encoders, only a single Hall sensor can be used at a time.

    # Using pins HALL_U, HALL_V, HALL_W (17, 18, 19, resp.):
    # This is strictly not needed if IC has been reset, as these are the default values.
    tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_MATRIX.PIN_HALL_U.choice.HALL_U)
    tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_MATRIX.PIN_HALL_V.choice.HALL_V)
    tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_MATRIX.PIN_HALL_W.choice.HALL_W)

    # Example when connecting the Hall sensor to pins ENC_A, ENC_B, ENC_N (14, 15, 16, resp.):
    #tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_MATRIX.PIN_ENC_A.choice.HALL_U)
    #tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_MATRIX.PIN_ENC_B.choice.HALL_V)
    #tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_MATRIX.PIN_ENC_N.choice.HALL_W)

    # HALL SENSOR SETUP
    # For digital Hall sensors, only the mapping of the UVW inputs can be set,
    # the mapping can be changed to correct for signals connected in the
    # wrong order or to reverse the direction of the detected count.
    tmc6460_eval.write(TMC6460.REGMAP.HALL.MAP_CONFIG.HALL_MAP, HALL_MAPPING_VALUE)

    # Set the IO inversion of the hall inputs
    tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_CONFIG.INV_PIN_HALL_U, HALL_IO_INVERSION)
    tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_CONFIG.INV_PIN_HALL_V, HALL_IO_INVERSION)
    tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_CONFIG.INV_PIN_HALL_W, HALL_IO_INVERSION)

    # FEEDBACK INPUT SETUP
    # When the Hall sensor is the only feedback available, one of the feedback channels has
    # to be used for Phi E generation, and the other for velocity and position feedback.
    # This step only configures each of the feedback channels; the output of the channels will
    # be routed to the Phi E generator, velocity meter and/or position decoder at a later step.

    # Channel A will be used for Phi E feedback
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_A.SRC_SEL_A.choice.HALL)
        # HALL option makes use of value in the field 'HALL.DIG_COUNT.COUNT' as
        # feedback source, this option should be used for Phi E generation
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_A.CPR_INV_A, 2_796_203)
        # cpr_inv = 2^24 / 6, this is valid when using Hall for Phi E generation
    # Channel B will be used for velocity and position feedback
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_B.SRC_SEL_B.choice.HALL_FREE)
        # HALL_FREE option makes use of an internal 'HALL_FREE' value (not available as
        # a register), this option should be used for velocity and position feedback
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_B.CPR_INV_B, 65_536)
        # cpr_inv = some power of 2 >= 256, this is valid when using the *_FREE source options.
        # To understand the logic behind this, consider that 'HALL_FREE' counts the encoder's
        # pulses without resetting the count on every revolution (as 'HALL.DIG_COUNT.COUNT' does);
        # Then cosider what the 16-bit conversion block does: it multiplies the output of the
        # chosen source by cpr_inv and right shifts the result by 8 (effectively dividing by 256).
        # Thus, if we want to keep the HALL_FREE count transparent, we need a cpr_inv of 256.
        # Using 256 has the advantage of reflecting the 'truest' resolution of the
        # encoder in the velocity and position values.
        # If 256 is used for a Hall sensor, however, the resulting measured velocity
        # values will be too small, which can lead to problems when using the ramper,
        # as even an acceleration value of 1 will result in high accelerations.
        # The cpr_inv of 2^16 used in this example shows a better balance.

    # PHI E, VELOCITY AND POSITION FEEDBACK SETUP
    # The input for the Phi E generator, the velocity meter and the position decoder
    # can be set to track the lookup table (LUT) channel A or B, which accordingly
    # come from the previously configured feedback channels A and B.
    # The LUT is deactivated by default, which results in the
    # feedback channels going through unmodified.
    # An additional input option is available for the Phi E generator, which takes
    # the output of the LUT and creates extrapolated values from it. This would
    # generally be used for very low line count encoders or Hall sensors.

    # Make sure the LUT is disabled
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.LUT.LOOKUP_A_EN, 0)
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.LUT.LOOKUP_B_EN, 0)

    # Phi E generator
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.OUTPUT_CONF.PHI_E_SRC.choice.EXTRAPOLATOR_A)
        # Phi E generator to use the extrapolator channel A,
        # which comes from feedback channel A, which in turn
        # was previously configured with the source of HALL.
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.OUTPUT_CONF.PHI_E_MUL_FACTOR, 1)
        # mul_factor = phi encoder to phi e ratio,
        # for Hall sensors this should be 1
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.PHI_E_OFFSET.PHI_E_OFFSET, PRESET_HALL_OFFSET)
        # For absolute (or quasi-absolute such a Hall sensor) feedback
        # sources an appropriate Phi E offset must be specified to
        # align the motor's Phi E with the sensor's Phi E

    # Velocity Meter(s)
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.OUTPUT_CONF.POSITION_SRC.choice.LOOKUP_B)
        # Both velocity meters share the same input; in this case make use the LUT
        # channel B, which was previously configured with the source of HALL_FREE
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
        # Position decoder to use LUT channel B, thus HALL_FREE

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

    # FIND AN APPROPRIATE HALL SENSOR OFFSET IF INDICATED

    if FIND_NEW_HALL_OFFSET:
        print()
        print("Finding a suitable Hall sensor Phi E offset...")

        # Reset the ramper position and make sure the ramper's Phi E offset has no offset relative to it
        tmc6460_eval.write(TMC6460.REGMAP.RAMPER.POSITION.POSITION, 0)
        tmc6460_eval.write(TMC6460.REGMAP.RAMPER.PHI_E.PHI_E_OFFSET, 0)
        tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.PHI_E_OFFSET.PHI_E_OFFSET, 0)

        # Set ramper for velocity mode and use it to generate a Phi E
        tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_MODE.choice.RAMP_VELOCITY)
        tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_EN, True)
        tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_USE_PHI_E, True)

        offsets = []
        directions_valid = []
        for invert_direction in [False, True]:
            print(f"Starting test run: {'Backwards' if invert_direction else 'Forwards'} direction")

            # Enable torque control mode (current open loop)
            tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTION_MODE.choice.TORQUE)
            # Set a fixed flux by ramping the value up
            target_flux = OPENLOOP_CURRENT
            target_step = OPENLOOP_CURRENT // 10
            for flux in range(target_step, target_flux, target_step):
                tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET.PID_FLUX_TARGET, flux)
                time.sleep(0.2)
            time.sleep(1)

            # At this point the motor will be in a known position, electrically speaking
            # at least; from here, an offset can be found by extracting the difference
            # from the Hall sensor's Phi E and the ramper's Phi E while the motor turns

            # Configure the datalogger
            dl = tmc6460_eval.datalogger
            dl.config.samples_per_channel = 1024
            try:
                dl.config.set_sample_rate(rate_hz=5000)
            except pytrinamic.datalogger.DataLoggerConfigError:
                pass
            dl.config.log_data = [
                TMC6460.REGMAP.RAMPER.PHI_E.PHI_E,
                TMC6460.REGMAP.FEEDBACK.PHI_E.PHI_E_FOC,
                TMC6460.REGMAP.HALL.DIG_COUNT.COUNT,
            ]

            # Start turning the motor and wait a bit until the velocity is reached
            print("Turning the motor...")
            tmc6460_eval.write(TMC6460.REGMAP.RAMPER.A_MAX.A_MAX, 250)
            tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_VELOCITY_TARGET.PID_VELOCITY_TARGET, OPENLOOP_VELOCITY * (-1 if not invert_direction else 1))
                # The extrapolator block needs to have a minimum update frequency on its input
                # to start extrapolating, therefore we set a velocity of at least 60,000 here.
                # Using lower velocity values might lead to an incorrect offset estimation.
            while not tmc6460_eval.read(TMC6460.REGMAP.RAMPER.STATUS.V_REACHED_STATUS):
                time.sleep(0.2)
            time.sleep(0.2)

            # Log the required data
            print("Retrieving the needed data...")
            dl.start_capture()
            dl.wait_for_capture_completion()

            # Stop the motor and turn down the set flux
            tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_VELOCITY_TARGET.PID_VELOCITY_TARGET, 0)
            tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET.PID_FLUX_TARGET, 0)

            # Retrieve the logged data
            dl.download_log()

            # Process the logged data; this implies getting the average difference
            # between the ramper's Phi E and the Hall sensor's Phi E
            ramper_phi_e = dl.log.data["PHI_E.PHI_E"].samples
            hall_phi_e = dl.log.data["PHI_E.PHI_E_FOC"].samples
            hall_count = dl.log.data["DIG_COUNT.COUNT"].samples

            phi_e_diff = [(ramper - hall) & 0xFFFF for ramper, hall in zip(ramper_phi_e, hall_phi_e)]
            # & 0xFFFF is used here to effectively add 2^16 to difference values which
            # have a negative sign, since the offset value must always be positive
            phi_e_offset = sum(phi_e_diff) // len(phi_e_diff)
            offsets.append(phi_e_offset)
            phi_e_deviation = [(((val - phi_e_offset) & 0xFFFF) ^ 0x8000) - 0x8000 for val in phi_e_diff]
            phi_e_deviation_min = min(phi_e_deviation)
            phi_e_deviation_max = max(phi_e_deviation)
            print(f"Deviation range: [{phi_e_deviation_min} ; {phi_e_deviation_max}]")
            hall_direction_is_correct = (phi_e_deviation_max - phi_e_deviation_min) <= 32768
            directions_valid.append(hall_direction_is_correct)
            if hall_direction_is_correct:
                print("Hall direction is correct!")
            else:
                print("Hall direction is wrong!")

            # Apply the estimated offset
            print(f"Estimated offset: {phi_e_offset}")

            # Show plots if indicated, useful for debugging
            if SHOW_HALL_OFFSET_PLOTS:
                plt.figure()
                plt.plot(hall_phi_e, label='Hall Phi E')
                plt.plot(ramper_phi_e, label='Ramper Phi E')
                plt.plot(phi_e_diff, label='Phi E Offset')
                plt.plot([x*65536/6 for x in hall_count], label='Hall count (scaled up)')
                plt.title(f"Hall mapping: {HALL_MAPPING_VALUE}, Mean Offset: {phi_e_offset}, Direction {'matches' if hall_direction_is_correct else 'doesnt match'}")
                plt.legend()

        print("Offsets:", offsets)
        tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.PHI_E_OFFSET.PHI_E_OFFSET, (sum(offsets) // len(offsets)) & 0xFFFF)

        # Show the plots after the two test runs
        if SHOW_HALL_OFFSET_PLOTS:
            if not PERFORM_TEST_DRIVE:
                # Close the port early
                my_interface.close()
            plt.show()

        if not all(directions_valid):
            print("Hall direction detected to be incorrect. Test drive is skipped")
            exit(1)
    else:
        print()
        print(f"Using a preset Hall Phi E offset of {PRESET_HALL_OFFSET:,}...")

    if not PERFORM_TEST_DRIVE:
        exit(0)

    time.sleep(1)

    # ALIGN THE MOTOR AND THE CONTROLLER'S PHI E
    # This is needed ro reliably start moving the motor later

    # Reset the ramper position
    tmc6460_eval.write(TMC6460.REGMAP.RAMPER.POSITION.POSITION, 0)

    # Set ramper for position mode and use it to generate a Phi E
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_MODE.choice.RAMP_POSITION)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_EN, 1)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_USE_PHI_E, 1)

    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTION_MODE.choice.TORQUE)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET.PID_TORQUE_TARGET, 5000)
    time.sleep(1)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET.PID_TORQUE_TARGET, 0)

    # PERFORM THE TEST DRIVE
    # When turning the motor in torque mode with a set torque, 
    # the motor will simply spin as fast as possible;
    # we do this for some seconds here to show that the Hall sensor has
    # the right offset and it is correctly being used as a Phi E source

    print()
    print("Turning the motor in torque mode (current closed loop)...")
    # Enable torque control mode (current open loop)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_EN, 0)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_USE_PHI_E, 0)
    target_torque = TARGET_CURRENT
    target_step = TARGET_CURRENT // 10
    print("Turning forwards...")
    for torque in range(target_step, target_torque, target_step):
        tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET.PID_TORQUE_TARGET, torque)
        time.sleep(0.1)
    for i in range(3):
        print(f"{3-i} s remaining", flush=True)
        time.sleep(1)

    print("\rStopping motor...")
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET.PID_TORQUE_TARGET, 0)
    time.sleep(1)

    print("Turning backwards...")
    for torque in range(target_step, target_torque, target_step):
        tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET.PID_TORQUE_TARGET, -torque)
        time.sleep(0.1)
    for i in range(3):
        print(f"{3-i} s remaining", flush=True)
        time.sleep(1)

    print("\rStopping motor...")
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET, 0)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTION_MODE.choice.PWM_OFF)
