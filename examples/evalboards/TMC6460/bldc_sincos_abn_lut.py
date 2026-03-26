#!/usr/bin/env python
################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

'''
The LUT is applied to an analog sincos encoder, and an
ABN encoder is used as a ground truth reference; both
encoders are attached to the same motor shaft.

The script first measures both of the encoder's data for one
revolution, calculating the error, processing it and writing
the data to the LUT entries.

Then the script measures the encoder's data for yet another
revolution and compares the error of the data before and
after the correction LUT.
'''

import time

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

import statistics
import numpy as np

import pytrinamic
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
ABN_PPR = 1024
LOOKUP_ENABLE = True
PLOT_ENC_ERROR = False
PLOT_LUT_DATA = False

OPENLOOP_VELOCITY = 1850

################################################################################
def main():
    with ConnectionManager().connect() as my_interface:
        global tmc6460_eval
        tmc6460_eval = TMC6460_eval(my_interface)

        tmc6460_init()

        tmc6460_eval.write(TMC6460.REGMAP.RAMPER.POSITION.POSITION, 0)
        tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_MODE.choice.RAMP_POSITION)
        tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_USE_PHI_E, 1)
        tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_EN, 1)
        tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTION_MODE.choice.VOLTAGE_EXT)
        tmc6460_eval.write(TMC6460.REGMAP.EXT_CTRL.VOLTAGE.UD, 2000)
        time.sleep(1)
        #tmc6460_eval.write(TMC6460.REGMAP.ABN.COUNT.COUNT, 0)
        tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_POSITION_ACTUAL.PID_POSITION_ACTUAL, 0)
        tmc6460_eval.write(TMC6460.REGMAP.RAMPER.POSITION.POSITION, 0)
        tmc6460_eval.write(TMC6460.REGMAP.EXT_CTRL.VOLTAGE.UD, 0)
        tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_MODE.choice.RAMP_VELOCITY)
        tmc6460_eval.write(TMC6460.REGMAP.EXT_CTRL.VOLTAGE.UD, 2000)

        # Configure the datalogger
        dl = tmc6460_eval.datalogger
        dl.config.samples_per_channel = 2024
        dl.config.Trigger.on_data = TMC6460.REGMAP.FOC.PID_VELOCITY_TARGET.PID_VELOCITY_TARGET
        dl.config.Trigger.edge = pytrinamic.datalogger.DataLogger.TriggerEdge.RISING

        try:
            dl.config.set_sample_rate(rate_hz=200)
        except pytrinamic.datalogger.DataLoggerConfigError:
            pass
        dl.config.log_data = [
            TMC6460.REGMAP.FEEDBACK.PHI_CONVERTED.PHI_CONVERTED_B,
            TMC6460.REGMAP.FEEDBACK.PHI_CONVERTED.PHI_CONVERTED_A,
            TMC6460.REGMAP.FEEDBACK.CH_B.PHI_LOOKUP_B,
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

        # Process the logged data; this implies getting the average difference
        # between the ramper's Phi E and the ABN sensor's Phi E
        phi_conv_b = dl.log.data["PHI_CONVERTED.PHI_CONVERTED_B"].samples
        phi_conv_a = dl.log.data["PHI_CONVERTED.PHI_CONVERTED_A"].samples

        plt.figure()
        plt.plot(phi_conv_a, label='ABN')
        plt.plot(phi_conv_b, label='SINCOS')
        plt.legend()
        plt.show()

        # Taking sincos as a reference, we only separate an array that has only one mechanical revolution
        # We search for the index when SINCOS is zero and then take second index when it reaches to 65535
        # we then slice out that portion for both arrays
        first_index = None
        second_index = None

        for i in range(1, len(phi_conv_b)):
            if phi_conv_b[i-1] > 60000 and phi_conv_b[i] < 1000:
                first_index = i
                break
        for i in range(first_index+1, len(phi_conv_b)):
            if phi_conv_b[i-1] > 60000 and phi_conv_b[i] < 1000:
                second_index = i
                break

        print(f"First index: {first_index}, Second index: {second_index}")
        phi_conv_a_1rev = phi_conv_a[first_index:second_index]
        phi_conv_b_1rev = phi_conv_b[first_index:second_index]

        plt.figure()
        plt.plot(phi_conv_a_1rev, label='ABN 1 rev')
        plt.plot(phi_conv_b_1rev, label='SINCOS 1 rev')
        plt.legend()
        plt.show()

        ### Prepare the LUT data
        if LOOKUP_ENABLE:

            # Get the difference between the two encoders' phi, removing any 'DC' offset
            print()
            print("Calculating the SINCOS encoder's error...")
            phiDiff = [abn - sincos for sincos, abn in zip(phi_conv_b_1rev, phi_conv_a_1rev)]
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
            # print(f"Required LUT gain factor: {2 ** requiredGainCfg}")

            if requiredGain > 16.0:
                tmc6460_eval.write(TMC6460.REGMAP.EXT_CTRL.VOLTAGE.UD, 0)
                tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTION_MODE.choice.PWM_OFF)
                tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.DRV_EN_BIT, 0)
                assert False, "Aborting, the used encoder requires a gain bigger than 16"
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

            # Generate the values for the LUT
            phiDiffLut = [int(val / (2 ** requiredGainCfg)) for val in phiDiffAvgd256]
            phiDiffLut = np.array(phiDiffLut, dtype=np.int8)

            ### Configure the LUT

            # Clear the LUT
            print()
            print("Configuring the LUT...")
            print("Clearing any existing LUT data...")
            clear_lut_data()
            print("Writing the LUT data and gain...")
            tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.LUT.LOOKUP_B_GAIN, requiredGainCfg)
            print(requiredGainCfg)
            write_lut_data(phiDiffLut)
            currentLut = read_lut_data()

            if PLOT_ENC_ERROR:
                plt.plot(phiDiff, label="Calculated encoder error")
                plt.plot(phiDiffAvgd, label=f"Filtered encoder error (moving average n={window_size})")
                plt.legend()
                plt.xlabel('Sample count')
                plt.ylabel('Register units')
                plt.show()

            if PLOT_LUT_DATA:
                plt.plot(phiDiffAvgd256, label="Downsampled encoded error (256 entries)")
                plt.plot(phiDiffLut, linestyle='dashed', label="Value written to LUT (error/gain)")
                plt.plot(currentLut, linestyle='dotted', label="Value read back from LUT")
                plt.legend()
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

            phi_conv_b = dl.log.data["PHI_CONVERTED.PHI_CONVERTED_B"].samples # SINCOS
            phi_conv_a = dl.log.data["PHI_CONVERTED.PHI_CONVERTED_A"].samples # ABN
            phi_lookup_b = dl.log.data["CH_B.PHI_LOOKUP_B"].samples

            errBefore = [abn - sincos for abn, sincos in zip(phi_conv_a, phi_conv_b)]
            errBefore = [val + 65_536 if val < -10000 else val for val in errBefore]
            errBefore = [val - 65_536 if val > 10000 else val for val in errBefore]
            dcOffset = int(statistics.mean(errBefore))
            errBefore = [val - dcOffset for val in errBefore]

            errAfter = [abn - lut for abn, lut in zip(phi_conv_a, phi_lookup_b)]
            errAfter = [val + 65_536 if val < -10000 else val for val in errAfter]
            errAfter = [val - 65_536 if val > 10000 else val for val in errAfter]
            dcOffset = int(statistics.mean(errAfter))
            errAfter = [val - dcOffset for val in errAfter]

            plt.plot(errBefore, label="Encoder error before LUT")
            plt.plot(errAfter, label="Encoder error after LUT")
            plt.legend()
            plt.xlabel('Sample count')
            plt.ylabel('Register units')
            plt.show()

            # Disable the driver
            print()
            print("Disabling the driver...")
            tmc6460_eval.write(TMC6460.REGMAP.EXT_CTRL.VOLTAGE.UD, 0)
            tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTION_MODE.choice.PWM_OFF)
            tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.GDRV.DRV_EN_BIT, 0)


def clear_lut_data():
    for addr in range(0, 256, 4):
        tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.LUT.ADDR, addr)
        tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.LUT_WDATA.WDATA, 0)


def write_lut_data(phiList):
    # The LUT has 256 entries, each one consisting of a 8-bit signed integer.
    # Data can only be populated four entries at a time, which means a package
    # of four entries has to be combined into a single 32-bit wide value,
    # and then written while chosing addresses which are multiples of four.
    for idx in range(0, 256, 4):
        wData = ((int(phiList[idx]) & 0xFF) | ((int(phiList[idx+1]) & 0xFF) << 8) | ((int(phiList[idx+2]) & 0xFF) << 16) | ((int(phiList[idx+3]) & 0xFF) << 24))
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

    # SINCOS setup
    #tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_CONFIG.ANA_DIV_VCCIOF, 0) # 0=DIV_BY_4P5(default), 1=DIV_BY_3P0, 2=DIV_BY_2P2, 3=DIV_BY_1P0
    tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_MATRIX.PIN_HALL_U, 1) # 0=HALL_U(default), 1=AINP_U, 2=ENC2A, ...
    tmc6460_eval.write(TMC6460.REGMAP.CHIP.IO_MATRIX.PIN_HALL_W, 1) # 0=HALL_W(default), 1=AINP_W, 2=ENC2N, ...
    tmc6460_eval.write(TMC6460.REGMAP.HALL.ANA_CONFIG, 0) # default pin mapping
    tmc6460_eval.write(TMC6460.REGMAP.HALL.ANA_CONFIG.ANA_MODE.choice.XY) # 0=XY_MODE(default), 1=UVW_MODE
    tmc6460_eval.write(TMC6460.REGMAP.HALL.ANA_CONFIG.TWO_CYCLE_MODE_EN, 1) # Enable for encoders that output two cycles per rev
    tmc6460_eval.write(TMC6460.REGMAP.HALL.ANA_UX_CONFIG.UX_OFFSET, 15000) # Subtracted from raw value before scaling
    tmc6460_eval.write(TMC6460.REGMAP.HALL.ANA_UX_CONFIG.UX_SCALE, 1024) # 1024 -> scale of 1
    tmc6460_eval.write(TMC6460.REGMAP.HALL.ANA_WY_CONFIG.WY_OFFSET, 15000) # Subtracted from raw value before scaling
    tmc6460_eval.write(TMC6460.REGMAP.HALL.ANA_WY_CONFIG.WY_SCALE, 1024) # 1024 -> scale of 1
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_B.SRC_SEL_B, 4) # 4=ANALOG_HALL
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_B.CPR_INV_B, 256) # 16777216/pulses_per_rotation
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.PHI_E_OFFSET.PHI_E_OFFSET, 6000)
    # tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.LUT.LOOKUP_B_EN, 0)

    # The 'ABN' register block should be used when connecting
    # an encoder to the ABN main pins, i.e., ENC_A, ENC_B, ENC_N.
    tmc6460_eval.write(TMC6460.REGMAP.ABN.CONFIG.CPR, (ABN_PPR*4) - 0) # should be the encoder's CPR minus one
    tmc6460_eval.write(TMC6460.REGMAP.ABN.CONFIG.INV_DIR, 1) # use if encoder's direction is inverted
    tmc6460_eval.write(TMC6460.REGMAP.ABN.CONFIG.COMBINED_N.choice.ALL) # allows more precise N pulse detection
    tmc6460_eval.write(TMC6460.REGMAP.ABN.CONFIG.CLN.choice.OFF)
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_A.SRC_SEL_A.choice.ABN_1)
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.CONF_CH_A.CPR_INV_A, 2**24 // (ABN_PPR*4))
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.OUTPUT_CONF.PHI_E_SRC.choice.LOOKUP_B)
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

    # Feedback LUT setup
    print("Configuring (some) feedback LUT settings...")
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.LUT.SPLIT_MODE_EN, 0)
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.LUT.LOOKUP_A_EN, 0)
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.LUT.LOOKUP_B_EN, 1)

    time.sleep(1)

    print("Encoder initialized")


def start_motor():
    print("Turning motor...")
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_VELOCITY_TARGET.PID_VELOCITY_TARGET, OPENLOOP_VELOCITY)


def stop_motor():
    print("Stopping motor...")
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_VELOCITY_TARGET.PID_VELOCITY_TARGET, 0)


if __name__ == "__main__":
    main()