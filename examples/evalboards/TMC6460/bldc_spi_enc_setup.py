#!/usr/bin/env python
################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

"""
This script configures the TMC6460 to run a test drive in torque mode (closed loop)
using an SPI encoder accessed by the TMC6460 IO controller.

The SPI encoder is polled to generate PHI_E feedback for the motor.

To set up the SPI encoder, the script features a setup mode to allow
identification and configuration of motor and encoder parameters.
The default values set are for an ADMT4000 SPI encoder.
"""

import logging
import time
import sys

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import TMC6460
from pytrinamic.evalboards import TMC6460_eval

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger("matplotlib").setLevel(logging.WARN)
logging.getLogger("PIL").setLevel(logging.WARN)

### System parameters ##########################################################
# The pole pair count of the connected motor
POLE_PAIRS = 4

# Current to use for openloop operation
# ToDo: Unit scaling
OPENLOOP_CURRENT = 10000 # [internal] unit

# Velocity to use for openloop operation
OPENLOOP_VELOCITY = 60000 # [internal] unit

# Used during torque test drive
TARGET_CURRENT    = 10000 # [internal] unit

# These are default PI values that are very conservative
PI_CURRENT_P      = 200
PI_CURRENT_P_NORM = 1    # 0=NO_SHIFT, 1=RSHIFT_8
PI_CURRENT_I      = 250
PI_CURRENT_I_NORM = 1    # 0=NO_SHIFT, 1=RSHIFT_8

### SPI Encoder parameters #####################################################
# Comment in the respective encoder you are using
### ADMT4000 SPI encoder settings ###
# The encoder steps of the connected SPI encoder
SPI_ENCODER_STEPS = 16384
# Whether to invert the connected SPI encoder direction
SPI_ENCODER_INVERT_DIRECTION = False
# What offset to apply to the SPI encoder electrical angle
SPI_ENCODER_OFFSET_PHI_E = 0

# The SPI mode of the connected SPI encoder
# - 0: CPOL=0, CPHA=0
# - 1: CPOL=0, CPHA=1
# - 2: CPOL=1, CPHA=0
# - 3: CPOL=1, CPHA=1
SPI_BUS_MODE = 0

# Select the SPI frequency: 3MHz - 117187 Hz
# If the exact frequency cannot be represented, this script will round down.
SPI_FREQUENCY_SELECTION = 3_000_000 # Hz

# SPI data bits for the angle polling datagram
SPI_BITS = 32

# Bits of the reply datagram containing the angle data
# The set bits must be in order for the reference IO controller program,
# but may have gaps.
SPI_DATA_MASK = 0x00FFFC00 # ADMT4000: Register 5 reports 14 angle bits

# Bits to send for angle polling datagrams
# These bits are sent MSB-to-LSB, starting at the 32-bit MSB
# For data lengths less than 32, lowest bits are not sent.
SPI_SEND_DATA = 0x05000000 # ADMT4000: Read register 5

# Idle time between datagrams where chip select is deasserted
SPI_IDLE_TIME = 16


### AS5047 SPI encoder settings ###
# # The encoder steps of the connected SPI encoder
# SPI_ENCODER_STEPS = 16384
# # Whether to invert the connected SPI encoder direction
# SPI_ENCODER_INVERT_DIRECTION = False
# # What offset to apply to the SPI encoder electrical angle
# SPI_ENCODER_OFFSET_PHI_E = 0
#
# # The SPI mode of the connected SPI encoder
# # - 0: CPOL=0, CPHA=0
# # - 1: CPOL=0, CPHA=1
# # - 2: CPOL=1, CPHA=0
# # - 3: CPOL=1, CPHA=1
# SPI_BUS_MODE = 1
#
# # Select the SPI frequency: 3MHz - 117187 Hz
# # If the exact frequency cannot be represented, this script will round down.
# SPI_FREQUENCY_SELECTION = 3_000_000 # Hz
#
# # SPI data bits for the angle polling datagram
# SPI_BITS = 16
#
# # Bits of the reply datagram containing the angle data
# # The set bits must be in order for the reference IO controller program,
# # but may have gaps.
# SPI_DATA_MASK = 0x00003FFF # AS5047: Bits 13:0 report the angle
#
# # Bits to send for angle polling datagrams
# # These bits are sent MSB-to-LSB, starting at the 32-bit MSB
# # For data lengths less than 32, lowest bits are not sent.
# SPI_SEND_DATA = 0xFFFFFFFF # AS5047
#
# # Idle time between datagrams where chip select is deasserted
# SPI_IDLE_TIME = 16

### Script sequence control ####################################################
### Openloop detection sequence: Turn the motor, poll SPI encoder
# Enable this sequence
RUN_OPENLOOP_DETECTION = True
# Show graphs of the detection
SHOW_OPENLOOP_PLOTS = True

# Whether to do just a forwards rotation, or both a forwards and a backwards
# rotation.
OPENLOOP_SECOND_ROTATION=False

### Test drive: Turn the motor in torque mode based on SPI encoder
# Enable this section
# !!! Only turn this on after configuring all the above settings !!!
RUN_TEST_DRIVE = False

################################################################################

### Sanity-check parameters
assert SPI_FREQUENCY_SELECTION <= 3_000_000, "Maximum SPI frequency is 3MHz"

SPI_FREQUENCY_CONFIG = 0 # <- IO controller SPI frequency of 3MHz
if SPI_FREQUENCY_SELECTION != 3_000_000:
    for i in range(10, 256):
        frequency = 60e6 // ((i+1) * 2)
        if frequency <= SPI_FREQUENCY_SELECTION:
            SPI_FREQUENCY_CONFIG = i
            if frequency < SPI_FREQUENCY_SELECTION:
                print(f"Requested SPI frequency of {SPI_FREQUENCY_SELECTION} Hz cannot be produced exactly. Rounding down to {frequency} Hz")
            break
    else:
        print("Invalid frequency selection! Select a frequency between 3MHz and 117187Hz")
        sys.exit(1)

def main():
    with ConnectionManager().connect() as my_interface:
        tmc6460_eval = TMC6460_eval(my_interface)

        print()
        print("Configuring the TMC6460...")

        ### IO MATRIX SETUP
        # Setup the SPI pins connecting to the IO controller:
        # - CSN:  Pin 19: HALL_W
        # - SCK:  Pin 14: ENC_A
        # - MISO: Pin 15: ENC_B
        # - MOSI: Pin 16: ENC_N
        tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_MATRIX.PIN_ENC_A.choice.DIRECT_OUT0)
        tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_MATRIX.PIN_ENC_B.choice.DIRECT_IN0)
        tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_MATRIX.PIN_ENC_N.choice.DIRECT_IN1_OUT1)
        tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_MATRIX.PIN_HALL_W.choice.DIRECT_OUT2)

        ### IO controller setup for SPI encoder operation
        # Ensure the IO controller is off before using it
        tmc6460_eval.write(TMC6460.REGMAP.IO_CONTROLLER.COMMAND, 0)
        # Reset RESPONSE_0
        tmc6460_eval.write(TMC6460.REGMAP.IO_CONTROLLER.RESPONSE_0, 0)
        time.sleep(0.1)

        # Check the running program version
        tmc6460_eval.write(TMC6460.REGMAP.IO_CONTROLLER.COMMAND, 0xaa000000)
        fw_version = tmc6460_eval.read(TMC6460.REGMAP.IO_CONTROLLER.RESPONSE_1)
        tmc6460_eval.write(TMC6460.REGMAP.IO_CONTROLLER.COMMAND, 0)
        print(f"IO Controller firmware version: 0x{fw_version:08X}")

        firmware_type = fw_version >> 8
        # Upper 3 bytes contain the program type
        if firmware_type not in [0x00544D10, 0x0052414D]:
            print("Error: Unknown IO controller program")
            sys.exit(1)

        # Ensure we're running the right program
        if firmware_type != 0x0052414D:
            print("Error: The IO controller is not running the correct program")
            print("Upload the correct program using io_controller_upload.py before running this script!")
            sys.exit(1)

        # IO controller SPI encoder mode:
        # - RESPONSE_2 register contains the data mask indicating which bits to
        #   forward to the decoder engine
        # - RESPONSE_1 register contains the data to send. This data starts with
        #   the register MSB
        tmc6460_eval.write(TMC6460.REGMAP.IO_CONTROLLER.RESPONSE_2, SPI_DATA_MASK)
        tmc6460_eval.write(TMC6460.REGMAP.IO_CONTROLLER.RESPONSE_1, SPI_SEND_DATA)

        # IO controller setup for SPI operation
        operation = 2 # Poll repeatedly and store in FEEDBACK.PHI_EXT_A
        command = 0xF0000000                             # IO controller command: SPI operation
        command |= (SPI_FREQUENCY_CONFIG)  & 0x0000_00FF # SPI frequency
        command |= ((SPI_BITS-1) << 8)     & 0x0000_1F00 # SPI bits to send
        command |= ((SPI_IDLE_TIME) << 16) & 0x00FF_0000 # Idle time between datagram pairs
        command |= ((operation) << 24)     & 0x0300_0000 # Configure IO controller to poll repeatedly and write to FEEDBACK.PHI_EXT_A
        command |= ((SPI_BUS_MODE) << 26)  & 0x0C00_0000 # SPI bus mode to use

        tmc6460_eval.write(TMC6460.REGMAP.IO_CONTROLLER.COMMAND, command)

        ### ADC AND CSA SETUP
        tmc6460_eval.write(TMC6460.REGMAP.MCC_ADC.CSA_GAIN.CSA_GAIN.choice.X1) # (default: x1 gain)

        ### GATE DRIVER SETUP
        tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.USE_INTERNAL_R_REF, 0) # external is more precise over temperature (default: 1)
        tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.SLEW_RATE.choice.SR_400_V_PER_US) # (default: SR_200_V_PER_US)
        tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.LS_RES_ON.choice.RES_55_MOHM) # (default: RES_55_MOHM) allows the widest current range
        tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.DRV_EN_BIT, 1) # Turn on the drive

        ### PWM SETUP
        # Select 25 kHz PWM: f_pwm = 120MHz/MAX_COUNT
        tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.PWM_PERIOD.MAX_COUNT, 4800)
        # Default: HARMONIC
        tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.PWM.SV_MODE.choice.HARMONIC)
        # Default: CENTERED PWM
        tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.PWM.CHOP.choice.CENTERED)

        ### MOTOR SETUP
        # Select BLDC motor type
        tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTOR_TYPE.choice.BLDC)
        # Set the pole pair count
        tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.N_POLE_PAIRS, POLE_PAIRS)

        ### FEEDBACK INPUT SETUP
        # We configure the SPI encoder to give us commutation angle feedback on
        # decoder engine channel A

        # Channel A will be used for Phi E feedback
        tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_A.SRC_SEL_A.choice.PHI_EXT_A)
        # CPR_INV: 2^24 divided by the amount of steps of the input
        cpr_inv = 2**24 // SPI_ENCODER_STEPS
        if SPI_ENCODER_INVERT_DIRECTION == True:
            cpr_inv = 2**24 - cpr_inv
        tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_A.CPR_INV_A, cpr_inv)

        ### Electrical angle setup
        # The electrical angle input from channel A can be corrected using an
        # optional Lookup table, and can be further extrapolated.
        # For the SPI encoder we use neither of these options

        # Acquire PHI_E directly from the (deactivated) LUT output on channel A
        tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.OUTPUT_CONF.PHI_E_SRC.choice.LOOKUP_A)
        # To translate the incoming mechanical angle to an electrical angle,
        # we multiply by the motor pole pair count
        tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.OUTPUT_CONF.PHI_E_MUL_FACTOR, POLE_PAIRS)
        # PHI_E offset to add to the feedback system output
        # For an absolute encoder such as the SPI encoder, we can either configure
        # the SPI encoder to apply offsets if it is capable of that, or we can
        # add the offset here.
        tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.PHI_E_OFFSET.PHI_E_OFFSET, SPI_ENCODER_OFFSET_PHI_E)

        ### PI CONTROLLER SETUP
        # The coefficients for the PI controller will vary from motor to motor and from
        # setup to setup; ideally they should be tuned on the final mechanical setup.
        # The values provided here are appropriate to the QBL4208 motor series.
        # Torque and flux PI
        tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_CONFIG.CURRENT_NORM_P, PI_CURRENT_P_NORM)
        tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_CONFIG.CURRENT_NORM_I, PI_CURRENT_I_NORM)
        tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_FLUX_COEFF.FLUX_P, PI_CURRENT_P)
        tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_FLUX_COEFF.FLUX_I, PI_CURRENT_I)
        tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_COEFF.TORQUE_P, PI_CURRENT_P)
        tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_COEFF.TORQUE_I, PI_CURRENT_I)

        # End of configuration

        ### Encoder setup step 1: Rotate in openloop control
        if RUN_OPENLOOP_DETECTION:
            # Openloop control is done using the built-in ramper to provide a
            # continuously rotating PHI_E angle.

            ### Ramper setup
            # Reset the ramper position
            tmc6460_eval.write(TMC6460.REGMAP.RAMPER.POSITION.POSITION, 0)
            # Make sure the ramper does not apply any PHI_E offset
            tmc6460_eval.write(TMC6460.REGMAP.RAMPER.PHI_E.PHI_E_OFFSET, 0)

            # Set ramper to velocity mode
            tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_MODE.choice.RAMP_VELOCITY)
            # Enable ramp operation
            tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_EN, 1)
            # Use the ramper PHI_E for motor control
            tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_USE_PHI_E, 1)

            for invert_direction in ([False, True] if OPENLOOP_SECOND_ROTATION else [False]):
                print(f"Starting test run: {'Backwards' if invert_direction else 'Forwards'} direction")

                # Enable torque control mode (current controlled open loop operation)
                tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET, 0)
                tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTION_MODE.choice.TORQUE)

                # Set a fixed flux by ramping the value up
                # This dampens the jump of the motor if its at a different angle initially
                target_flux = OPENLOOP_CURRENT
                target_step = OPENLOOP_CURRENT // 10
                for flux in range(target_step, target_flux, target_step):
                    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET.PID_FLUX_TARGET, flux)
                    time.sleep(0.2)
                tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET.PID_FLUX_TARGET, OPENLOOP_CURRENT)
                time.sleep(1)

                # Configure the datalogger
                dl = tmc6460_eval.datalogger
                dl.config.samples_per_channel = 512
                try:
                    dl.config.set_sample_rate(rate_hz=1000)
                except pytrinamic.datalogger.DataLoggerConfigError:
                    pass
                dl.config.log_data = [
                    # Openloop commanded angle by ramper
                    TMC6460.REGMAP.RAMPER.PHI_E.PHI_E,
                    # SPI encoder PHI_M angle after scaling, before LUT
                    TMC6460.REGMAP.FEEDBACK.PHI_CONVERTED.PHI_CONVERTED_A,
                    # SPI encoder PHI_E angle
                    TMC6460.REGMAP.FEEDBACK.PHI_E.PHI_E_FOC,
                ]

                # Start turning the motor and wait a bit until the velocity is reached
                print("Turning the motor...")
                tmc6460_eval.write(TMC6460.REGMAP.RAMPER.A_MAX.A_MAX, 250)
                tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_VELOCITY_TARGET.PID_VELOCITY_TARGET, (-OPENLOOP_VELOCITY if not invert_direction else OPENLOOP_VELOCITY))

                while not tmc6460_eval.read(TMC6460.REGMAP.RAMPER.STATUS.V_REACHED_STATUS):
                    time.sleep(1)#0.2)

                # Log the required data
                print("Retrieving the needed data...")
                dl.start_logging()
                dl.wait_till_done()

                # Stop the motor and turn down the set flux
                tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_VELOCITY_TARGET.PID_VELOCITY_TARGET, 0)
                tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET.PID_FLUX_TARGET, 0)

                # Retrieve the logged data
                dl.download_log()
                ramper_phi_e = dl.log.data["PHI_E.PHI_E"].samples
                spi_encoder_phi_m = dl.log.data["PHI_CONVERTED.PHI_CONVERTED_A"].samples
                spi_encoder_phi_e = dl.log.data["PHI_E.PHI_E_FOC"].samples

                # Calculate the difference
                phi_e_diff = calculate_nonwrapping_rotation(
                    [(a-b)&0xFFFF for a, b in zip(ramper_phi_e, spi_encoder_phi_e)],
                    bit_count=16
                    )

                # Calculate the estimated offset
                offset_estimate = sum(phi_e_diff) // len(phi_e_diff)
                offset_estimate += SPI_ENCODER_OFFSET_PHI_E
                offset_estimate &= 0xFFFF
                print("Estimated PHI_E_OFFSET:", offset_estimate)

                # Apply the offset
                tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.PHI_E_OFFSET.PHI_E_OFFSET, offset_estimate)

                # Show plots if indicated, useful for debugging
                if SHOW_OPENLOOP_PLOTS:
                    plt.figure()
                    plt.plot(ramper_phi_e, label='Ramper Phi E')
                    plt.plot(spi_encoder_phi_m, label='SPI encoder PHI_M')
                    plt.plot(spi_encoder_phi_e, label='SPI encoder PHI_E')
                    plt.plot(phi_e_diff, label="Difference in PHI_E")
                    direction_text = "Backwards" if invert_direction else "Forwards"
                    plt.title(f"SPI encoder openloop operation ({direction_text} direction)")

                    # Graph bounds:
                    # Show 16 bit unsigned PHI range plus a bit of margin
                    ymin = 0     - 1024
                    ymax = 2**16 + 1024
                    plt.ylim(ymin, ymax)
                    plt.legend()

            # Show the plots after the test run(s)
            if SHOW_OPENLOOP_PLOTS:
                if not RUN_TEST_DRIVE:
                    # Close the port early
                    my_interface.close()
                plt.show()

        else:
            print()
            print(f"Using a preset Hall Phi E offset of {SPI_ENCODER_OFFSET_PHI_E:}...")

        if not RUN_TEST_DRIVE:
            exit(0)

        # PERFORM THE TEST DRIVE
        # When turning the motor in torque mode with a set torque,
        # the motor will simply spin as fast as possible;
        # we do this for some seconds here to show that SPI encoder is correctly
        # configured.

        print()
        print("Turning the motor in torque mode (current closed loop)...")
        # Enable torque control mode (current open loop)
        tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_EN, 0)
        tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_USE_PHI_E, 0)
        tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET, 0)
        tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTION_MODE.choice.TORQUE)
        target_torque = TARGET_CURRENT
        target_step = TARGET_CURRENT // 10
        print("Turning forwards...")
        for torque in range(target_step, target_torque, target_step):
            tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET.PID_TORQUE_TARGET, torque)
            time.sleep(0.1)

        for i in range(3):
            print(f"{3-i} s remaining", flush=True)
            time.sleep(1)

        print("Stopping motor...")
        tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET.PID_TORQUE_TARGET, 0)
        time.sleep(1)

        print("Turning backwards...")
        for torque in range(target_step, target_torque, target_step):
            tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET.PID_TORQUE_TARGET, -torque)
            time.sleep(0.1)
        for i in range(3):
            print(f"{3-i} s remaining", flush=True)
            time.sleep(1)

        print("Stopping motor...")
        tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET.PID_TORQUE_TARGET, 0)
        tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTION_MODE.choice.PWM_OFF)

        print("Shutting off IO controller")
        tmc6460_eval.write(TMC6460.REGMAP.IO_CONTROLLER.COMMAND, 0)
        # Reset RESPONSE_0
        tmc6460_eval.write(TMC6460.REGMAP.IO_CONTROLLER.RESPONSE_0, 0)

def calculate_nonwrapping_rotation(data, bit_count):
    """
    This helper function takes the angle data with wrapping and creates
    a continuous non-wrapping sequence from it.

    It works by ensuring the data never jumps more than half of 2**bit_count.
    """
    # Copy the first element as-is
    result = [data[0]]

    # Subsequent elements: Compensate for sudden jumps indicative of wrapping
    for value in data[1:]:
        while value - result[-1] >= 2**(bit_count-1):
            value -= 2**bit_count
        while value - result[-1] <= -(2**(bit_count-1)):
            value += 2**bit_count

        result.append(value)

    return result

if __name__ == "__main__":
    main()