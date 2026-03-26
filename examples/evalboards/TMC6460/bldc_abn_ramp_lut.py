#!/usr/bin/env python
################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

"""
The LUT is applied to an ABN encoder, and a ramp signal is used as the ground-truth reference.

The script first measures the encoder and ramp data for one revolution and calculates the error(ABN − RAMP).
The error is then scaled down to 256 entries and the data is written to the LUT.

The script then measures the encoder data for another revolution and compares the error before and after
applying the correction LUT.
"""

import statistics
import sys
import time

try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Error: This script requires matplotlib for visualization")
    sys.exit(1)

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import TMC6460
from pytrinamic.evalboards import TMC6460_eval

# # Uncomment these lines to enable logging of all communication
# import logging
# import sys
# logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

### Parameters #################################################################
N_POLE_PAIRS   = 4
ABN_PPR        = 1024
ABN_INVERT_DIR = False

LOOKUP_ENABLE  = True
PLOT_ENC_ERROR = True
PLOT_LUT_DATA  = True

OPENLOOP_VELOCITY = 5000
OPENLOOP_CURRENT  = 10000

# These are default PI values that are very conservative
PI_CURRENT_P      = 243
PI_CURRENT_P_NORM = 0    # 0=NO_SHIFT, 1=RSHIFT_8
PI_CURRENT_I      = 1615
PI_CURRENT_I_NORM = 1    # 0=NO_SHIFT, 1=RSHIFT_8

################################################################################
def main():
    with ConnectionManager().connect() as my_interface:
        global tmc6460_eval
        tmc6460_eval = TMC6460_eval(my_interface)

        tmc6460_init()

        # Configure the datalogger
        dl = tmc6460_eval.datalogger
        dl.config.samples_per_channel = 2000
        dl.config.Trigger.on_data = TMC6460.REGMAP.FOC.PID_VELOCITY_TARGET.PID_VELOCITY_TARGET
        dl.config.Trigger.edge = pytrinamic.datalogger.DataLogger.TriggerEdge.RISING
        try:
            dl.config.set_sample_rate(rate_hz=200)
        except pytrinamic.datalogger.DataLoggerConfigError:
            pass
        dl.config.log_data = [
            TMC6460.REGMAP.FEEDBACK.PHI_CONVERTED.PHI_CONVERTED_A,
            TMC6460.REGMAP.FEEDBACK.CH_A.PHI_LOOKUP_A,
            TMC6460.REGMAP.RAMPER.PHI_E.PHI_E,
        ]

        start_motor()

        # Log the required data
        print("Retrieving the needed data...")
        dl.start_capture()
        dl.wait_for_capture_completion()

        # Stop motor
        stop_motor()
        time.sleep(1)

        # Retrieve the logged data
        dl.download_log()
        phi_conv_a = dl.log.data["PHI_CONVERTED.PHI_CONVERTED_A"].samples
        ramper_phi_e = dl.log.data["PHI_E.PHI_E"].samples

        # In order to calculate the error for lookup table both signals
        # needs to be comparable. That means we need to take signals before
        # "Correction LUT" block(refer to feedback engine block diagram).
        # Ramp signal needs to be divided by 4 and unwrapped to match the 
        # 16 bit value which is comparable to ABN encoder value. 

        i = 0
        ramper_phi_e_unwrap = [(val // 4) for val in ramper_phi_e]
        if len(ramper_phi_e_unwrap) > 1:
            offset = 0
            unwrapped = [ramper_phi_e_unwrap[0]]
            prev = ramper_phi_e_unwrap[0]
            for val in ramper_phi_e_unwrap[1:]:
                if val < prev:
                    offset += (65536 // 4)
                    i = (i + 1)
                    if i==4:
                        offset = 0
                        i=0
                unwrapped.append(val + offset)
                prev = val

            ramper_phi_e_unwrap = unwrapped

        plt.figure()
        plt.plot(phi_conv_a, label='ABN 1 rev')
        plt.plot(ramper_phi_e_unwrap, label='Ramper 1 rev')
        plt.legend()
        plt.title("Full uncompensated ABN measurement")
        plt.show()

        # Taking ABN as a reference, we only separate an array that has only one mechanical revolution
        # We search for the index when ABN is zero and then take second index when it reaches to 65535
        # we then slice out that portion for both arrays
        first_index = None
        second_index = None

        for i in range(1, len(phi_conv_a)):
            if phi_conv_a[i-1] > 60000 and phi_conv_a[i] < 1000:
                first_index = i
                break
        for i in range(first_index+1, len(phi_conv_a)):
            if phi_conv_a[i-1] > 60000 and phi_conv_a[i] < 1000:
                second_index = i
                break

        print(f"First index: {first_index}, Second index: {second_index}")
        phi_conv_a_1rev = phi_conv_a[first_index:second_index]
        ramper_phi_e_unwrap_1rev = ramper_phi_e_unwrap[first_index:second_index]

        plt.figure()
        plt.plot(phi_conv_a_1rev, label='ABN 1 rev')
        plt.plot(ramper_phi_e_unwrap_1rev, label='Ramper 1 rev')
        plt.legend()
        plt.title("Single rotation uncompensated ABN measurement")
        plt.show()

        ### Prepare the LUT data
        if LOOKUP_ENABLE:

            # Feedback LUT setup
            print("Configuring (some) feedback LUT settings...")
            tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.LUT.SPLIT_MODE_EN, 0)
            tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.LUT.LOOKUP_A_EN, 1)
            tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.LUT.LOOKUP_B_EN, 0)

            # Get the difference between the two encoders' phi, removing any 'DC' offset
            print()
            print("Calculating the ABN encoder's error...")
            phiDiff = [ramper - abn for ramper, abn in zip(ramper_phi_e_unwrap_1rev, phi_conv_a_1rev)]
            phiDiff = [val + 65_536 if (val < -10000) else val for val in phiDiff]
            phiDiff = [val - 65_536 if (val > 10000) else val for val in phiDiff]
            dcOffset = int(statistics.mean(phiDiff))
            phiDiff = [val - dcOffset for val in phiDiff]

            # Apply a moving average filter to the difference
            phiDiffAvgd = []
            window_size = 15
            i = 0

            while i < len(phiDiff) - window_size + 1:
                window = phiDiff[i:i+window_size]
                window_average = sum(window) / window_size
                phiDiffAvgd.append(window_average)
                i += 1

            # Reduce the number of samples to 256
            stepSize = len(phiDiffAvgd) / 256
            indices = [int(round(idx * stepSize, 0)) for idx in range(256)]
            phiDiffAvgd256 = [phiDiffAvgd[idx] for idx in indices]

            # Get the minimum and maximum difference to determine the required gain
            requiredGain = max([abs(x) for x in phiDiffAvgd256]) / 128
            print(f"Max and min error value: {max(phiDiffAvgd256):0.2f}, {min(phiDiffAvgd256):0.2f}")

            if requiredGain > 16.0:
                tmc6460_eval.write(TMC6460.REGMAP.EXT_CTRL.VOLTAGE.UD, 0)
                tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTION_MODE.choice.PWM_OFF)
                tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.DRV_EN_BIT, 0)
                print("Error: Compensation required is too big for representation in the LUT (gain exceeding 16)")
                sys.exit(1)
            elif requiredGain > 8.0:
                requiredGainCfg = 4
            elif requiredGain > 4.0:
                requiredGainCfg = 3
            elif requiredGain > 2.0:
                requiredGainCfg = 2
            elif requiredGain > 1.0:
                requiredGainCfg = 1
            else:
                requiredGainCfg = 0
            gain = 2 ** requiredGainCfg
            # Generate the values for the LUT
            phiDiffLut = [int(val / gain) for val in phiDiffAvgd256]

            ### Configure the LUT

            # Clear the LUT
            print()
            print("Configuring the LUT...")
            print("Clearing any existing LUT data...")
            clear_lut_data()
            print("Writing the LUT data and gain...")
            tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.LUT.LOOKUP_A_GAIN, requiredGainCfg)
            print(requiredGainCfg)
            write_lut_data(phiDiffLut)
            currentLut = read_lut_data()

            if PLOT_ENC_ERROR:
                plt.plot(phiDiff, label="Calculated encoder error")
                plt.plot(list([x + window_size//2 for x in range(len(phiDiffAvgd))]), phiDiffAvgd, label=f"Filtered encoder error (moving average n={window_size})")
                plt.legend()
                plt.title("Encoder error")
                plt.xlabel('Sample count')
                plt.ylabel('Register units')
                plt.show()

            if PLOT_LUT_DATA:
                plt.plot(phiDiffAvgd256, label="Downsampled encoded error (256 entries)")
                plt.plot([x*gain for x in phiDiffLut], linestyle='dashed', label="Value written to LUT")
                plt.plot([x*gain for x in currentLut], linestyle='dotted', label="Value read back from LUT")
                plt.legend()
                plt.title("Calculated LUT settings")
                plt.xlabel('Sample count')
                plt.ylabel('Register units')
                plt.show()

        ### After applying the LUT

            start_motor()

            # Log the required data
            print("Retrieving the needed data...")
            dl.start_capture()
            dl.wait_for_capture_completion()

            # Stop motor
            stop_motor()
            time.sleep(1)

            # Retrieve the logged data
            dl.download_log()

            # Process the logged data; this implies getting the average difference
            # between the ramper's Phi E and the ABN sensor's Phi E

            phi_conv_a = dl.log.data["PHI_CONVERTED.PHI_CONVERTED_A"].samples # ABN
            phi_lookup_a = dl.log.data["CH_A.PHI_LOOKUP_A"].samples
            ramper_phi_e = dl.log.data["PHI_E.PHI_E"].samples

        # Detect and correct wrap-around in ramper_phi_e_unwrap (unwrap)
        ramper_phi_e_unwrap = 0
        i = 0
        ramper_phi_e_unwrap = [(val // 4) for val in ramper_phi_e]
        if len(ramper_phi_e_unwrap) > 1:
            offset = 0
            unwrapped = [ramper_phi_e_unwrap[0]]
            prev = ramper_phi_e_unwrap[0]
            for val in ramper_phi_e_unwrap[1:]:
                if val < prev:
                    offset += (65536 // 4)
                    i = (i + 1)
                    if i==4:
                        offset = 0
                        i=0
                unwrapped.append(val + offset)
                prev = val

            ramper_phi_e_unwrap = unwrapped

            errBefore = [abn - ramp for abn, ramp in zip(phi_conv_a, ramper_phi_e_unwrap)]
            errBefore = [val + 65_536 if val < -10000 else val for val in errBefore]
            errBefore = [val - 65_536 if val > 10000 else val for val in errBefore]
            dcOffset = int(statistics.mean(errBefore))
            errBefore = [val - dcOffset for val in errBefore]

            errAfter = [abn - lut for abn, lut in zip(phi_conv_a, phi_lookup_a)]
            errAfter = [val + 65_536 if val < -10000 else val for val in errAfter]
            errAfter = [val - 65_536 if val > 10000 else val for val in errAfter]
            dcOffset = int(statistics.mean(errAfter))
            errAfter = [val - dcOffset for val in errAfter]

            plt.figure()
            plt.plot(errBefore, label="Encoder error before LUT")
            plt.plot(errAfter, label="Encoder error after LUT")
            plt.legend()
            plt.title("Encoder error comparison")
            plt.xlabel('Sample count')
            plt.ylabel('Register units')
            plt.show()


def clear_lut_data():
    for addr in range(0, 256, 4):
        tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.LUT.ADDR, addr)
        tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.LUT_WDATA.WDATA, 0)


def write_lut_data(phiList: list[int]):
    # Ensure all values fit
    assert all([x < 256 for x in phiList]), "Something wen't wrong calculating LUT entries. Not all values fit within 8 bit"
    assert len(phiList) == 256

    # The LUT has 256 entries, each one consisting of a 8-bit signed integer.
    # Data can only be populated four entries at a time, which means a package
    # of four entries has to be combined into a single 32-bit wide value,
    # and then written while chosing addresses which are multiples of four.
    for idx in range(0, 256, 4):
        wData =  (phiList[idx]   & 0xFF)        \
              | ((phiList[idx+1] & 0xFF) << 8)  \
              | ((phiList[idx+2] & 0xFF) << 16) \
              | ((phiList[idx+3] & 0xFF) << 24)
        tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.LUT.ADDR, idx)
        tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.LUT_WDATA.WDATA, wData)


def read_lut_data():
    # In contrast to writing, the LUT's 256 entries can all be individually read.
    # This is acchieved by writing the address to be read and then by
    # reading the value in the LUT.RDATA field (an 8-bit wide field).
    lut = []
    for addr in range(256):
        tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.LUT.ADDR, addr)
        lut.append(tmc6460_eval.read(TMC6460.REGMAP.FEEDBACK.LUT.RDATA))
    return lut.copy()


def tmc6460_init():
    # Motor setup
    print("Configuring motor settings...")
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTOR_TYPE.choice.BLDC)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.N_POLE_PAIRS, N_POLE_PAIRS)

    # Depending on which pins are used for the ABN encoder(s), the IO matrix has to be set.

    # Using pins ENC_A, ENC_B, ENC_N (14, 15, 16, resp.):
    # This is strictly not needed if IC has been reset, as these are the default values.
    tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_MATRIX.PIN_ENC_A.choice.ENC_A)
    tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_MATRIX.PIN_ENC_B.choice.ENC_B)
    tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_MATRIX.PIN_ENC_N.choice.ENC_N)

    # The 'ABN' register block should be used when connecting
    # an encoder to the ABN main pins, i.e., ENC_A, ENC_B, ENC_N.
    tmc6460_eval.write(TMC6460.REGMAP.ABN.CONFIG.CPR, (ABN_PPR*4) - 1) # should be the encoder's CPR minus one
    tmc6460_eval.write(TMC6460.REGMAP.ABN.CONFIG.INV_DIR, ABN_INVERT_DIR) # use if encoder's direction is inverted
    tmc6460_eval.write(TMC6460.REGMAP.ABN.CONFIG.COMBINED_N.choice.ALL) # allows more precise N pulse detection
    tmc6460_eval.write(TMC6460.REGMAP.ABN.CONFIG.CLN.choice.OFF)
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_A.SRC_SEL_A.choice.ABN_1)
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_A.CPR_INV_A, 2**24 // (ABN_PPR*4))
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.OUTPUT_CONF.PHI_E_SRC.choice.LOOKUP_A)
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.OUTPUT_CONF.PHI_E_MUL_FACTOR, N_POLE_PAIRS)

    # PWM setup
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.PWM_PERIOD.MAX_COUNT, 4800)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.PWM.SV_MODE.choice.HARMONIC)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.PWM.CHOP.choice.CENTERED)

    # ADC and CSA setup
    tmc6460_eval.write(TMC6460.REGMAP.MCC_ADC.CSA_GAIN.CSA_GAIN.choice.X1) # (default: x1 gain)

    # Gate driver setup
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.USE_INTERNAL_R_REF, 0) # external is more precise over temperature (default: 1)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.SLEW_RATE.choice.SR_400_V_PER_US) # (default: SR_200_V_PER_US)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.LS_RES_ON.choice.RES_55_MOHM) # (default: RES_55_MOHM) allows the widest current range
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.DRV_EN_BIT, 1)

    # Torque and flux PI
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_CONFIG.CURRENT_NORM_P, PI_CURRENT_P_NORM)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_CONFIG.CURRENT_NORM_I, PI_CURRENT_I_NORM)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_FLUX_COEFF.FLUX_P, PI_CURRENT_P)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_FLUX_COEFF.FLUX_I, PI_CURRENT_I)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_COEFF.TORQUE_P, PI_CURRENT_P)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_COEFF.TORQUE_I, PI_CURRENT_I)

    # Reset the ramper position and make sure the ramper's Phi E offset has no offset relative to it
    tmc6460_eval.write(TMC6460.REGMAP.RAMPER.POSITION.POSITION, 0)
    tmc6460_eval.write(TMC6460.REGMAP.RAMPER.PHI_E.PHI_E_OFFSET, 0)

    # Set ramper parameters for velocity movement
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_MODE.choice.RAMP_VELOCITY)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_USE_PHI_E, 1)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_EN, 1)
    # tmc6460_eval.write(TMC6460.REGMAP.RAMPER.A1.A1, 100)
    # tmc6460_eval.write(TMC6460.REGMAP.RAMPER.A2.A2, 200)
    # tmc6460_eval.write(TMC6460.REGMAP.RAMPER.A_MAX.A_MAX, 250)

    # Clear the ABN count, this ensures the encoder and the motor's Phi E are in sync
    tmc6460_eval.write(TMC6460.REGMAP.ABN.COUNT.COUNT, 0)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_POSITION_ACTUAL.PID_POSITION_ACTUAL, 0)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET, OPENLOOP_CURRENT)

    # Enable current control mode
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTION_MODE.choice.TORQUE)
    time.sleep(1)

    tmc6460_eval.write(TMC6460.REGMAP.ABN.COUNT.COUNT, 0)

    print("Encoder initialized")


def start_motor():
    print("Turning motor...")
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET.PID_FLUX_TARGET, OPENLOOP_CURRENT)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_VELOCITY_TARGET.PID_VELOCITY_TARGET, OPENLOOP_VELOCITY)


def stop_motor():
    print("Stopping motor...")
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_VELOCITY_TARGET.PID_VELOCITY_TARGET, 0)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET, 0)


if __name__ == "__main__":
    main()