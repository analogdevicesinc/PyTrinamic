#!/usr/bin/env python
################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

'''
The LUT is applied to an analog SinCos encoder, and a ramp signal is used as the ground-truth reference.

The script first measures the encoder and ramp data for one revolution and calculates the error. In the
error signal (SINCOS − RAMP), two frequencies are observed: a lower frequency that corresponds to magnet
misalignment relative to the motor shaft, and a higher frequency that corresponds to the motor pole pairs.
The lower frequency is filtered out using an FFT-based approach before mapping the data to the LUT entries.

The script then measures the encoder data for another revolution and compares the error before and after
applying the correction LUT.
'''

import time

from matplotlib.pyplot import plot

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

SAMPLE_RATE = 200  # Hz

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
        dl.config.samples_per_channel = 1200
        dl.config.Trigger.on_data = TMC6460.REGMAP.FOC.PID_VELOCITY_TARGET.PID_VELOCITY_TARGET
        dl.config.Trigger.edge = pytrinamic.datalogger.DataLogger.TriggerEdge.RISING

        try:
            dl.config.set_sample_rate(rate_hz=SAMPLE_RATE)
        except pytrinamic.datalogger.DataLoggerConfigError:
            pass
        dl.config.log_data = [
            TMC6460.REGMAP.FEEDBACK.PHI_CONVERTED.PHI_CONVERTED_B,
            TMC6460.REGMAP.RAMPER.PHI_E.PHI_E,
            TMC6460.REGMAP.FEEDBACK.CH_B.PHI_LOOKUP_B,
        ]

        start_motor()

        time.sleep(1)

        # Log the required data
        print("Retrieving the needed data...")
        dl.start_capture()
        dl.wait_for_capture_completion()

        stop_motor()

        # Retrieve the logged data
        dl.download_log()
        phi_conv_b = dl.log.data["PHI_CONVERTED.PHI_CONVERTED_B"].samples
        ramper_phi_e = dl.log.data["PHI_E.PHI_E"].samples

        # In order to calculate the error for lookup table both signals
        # needs to be comparable. That means we need to take signals before
        # "Correction LUT" block(refer to feedback engine block diagram).
        # Ramp signal needs to be divided by 4 and unwrapped to match the 
        # 16 bit value which is comparable to SinCos encoder value. 

        ramper_phi_e_unwrap = 0
        i = 0
        # Divide the ramp signal by 4 (phi_e = corrected_output * ENC_MUL_FACTOR)
        ramper_phi_e_unwrap = [(val // 4) for val in ramper_phi_e]
        # Unwrap the ramp signal such that it only resets only when it reached 65535 (1 revolution)
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

        # Taking sincos as a reference, we only separate an array that has only one mechanical revolution
        # We search for the index when SINCOS is zero and then take second index when it reaches to 65535

        first_index = None
        second_index = None

        for i in range(1, len(phi_conv_b)):
            if phi_conv_b[i-1] > 60000 and phi_conv_b[i] < 1000:
                first_index = i
                break
        for i in range(first_index+1, len(phi_conv_b)):
            if abs(phi_conv_b[i] - phi_conv_b[i-1]) > 10000:
                second_index = i
                break
        print(f"First index: {first_index}, Second index: {second_index}")

        phiDiff = [ramper - sincos for sincos, ramper in zip(phi_conv_b, ramper_phi_e_unwrap)]
        phiDiff = [val + 65_536 if (val < -10000) else val for val in phiDiff]
        phiDiff = [val - 65_536 if (val > 10000) else val for val in phiDiff]
        dcOffset = int(statistics.mean(phiDiff))
        phiDiff = [val - dcOffset for val in phiDiff]

        # Perform FFT 
        fft_signal = np.fft.fft(phiDiff)
        frequencies = np.fft.fftfreq(len(fft_signal), d=1/SAMPLE_RATE)
        # Create mask to filter out frequencies lower than 0.272 Hz (velocity = 5000)
        low_freq_mask = np.abs(frequencies) <= 1  # Low frequency below 0.272 Hz
        high_freq_mask = np.abs(frequencies) > 1  # High frequency above 0.272 Hz
        # Apply masks
        fft_low = fft_signal * low_freq_mask
        fft_high = fft_signal * high_freq_mask
        # Inverse FFT to get the filtered signal
        signal_low = np.fft.ifft(fft_low).real
        signal_high = np.fft.ifft(fft_high).real

        #plot original and filtered signal
        plt.figure()

        plt.subplot(3,1,1)
        plt.plot(phiDiff, label='Error Signal')
        plt.legend()
        plt.xlabel('Sample count')
        plt.ylabel('Register units')

        plt.subplot(3,1,2)
        plt.plot(signal_low, label='Low-Pass Filtered Signal', linestyle='dashed')
        plt.legend()
        plt.xlabel('Sample count')
        plt.ylabel('Register units')

        plt.subplot(3,1,3)
        plt.plot(signal_high, label='High-Pass Filtered Signal', linestyle='dotted')
        plt.legend()
        plt.xlabel('Sample count')
        plt.ylabel('Register units')

        plt.show()

        # Slice out that portion for both arrays corresponding to one mechanical revolution
        phiDiff_1rev_low = signal_low[first_index:second_index]
        phiDiff_1rev_high = signal_high[first_index:second_index]

        ### Prepare the LUT data
        if LOOKUP_ENABLE:

            # Apply a moving average filter to the difference
            phiDiffAvgd = []
            window_size = 15
            i = 0

            while i < len(phiDiff_1rev_high) - window_size + 1:
                window = phiDiff_1rev_high[i:i+window_size]
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

            time.sleep(1)

            # Log the required data
            print("Retrieving the needed data...")
            dl.start_capture()
            dl.wait_for_capture_completion()

            stop_motor()

            # Retrieve the logged data
            dl.download_log()

            phi_conv_b = dl.log.data["PHI_CONVERTED.PHI_CONVERTED_B"].samples # SINCOS
            ramper_phi_e = dl.log.data["PHI_E.PHI_E"].samples # Ramper
            phi_lookup_b = dl.log.data["CH_B.PHI_LOOKUP_B"].samples # LUT output

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

            errBefore = [sincos - ramp for sincos, ramp in zip(phi_conv_b, ramper_phi_e_unwrap)]
            errBefore = [val + 65_536 if val < -10000 else val for val in errBefore]
            errBefore = [val - 65_536 if val > 10000 else val for val in errBefore]
            dcOffset = int(statistics.mean(errBefore))
            errBefore = [val - dcOffset for val in errBefore]

            errAfter = [sincos - lut for sincos, lut in zip(phi_conv_b, phi_lookup_b)]
            errAfter = [val + 65_536 if val < -10000 else val for val in errAfter]
            errAfter = [val - 65_536 if val > 10000 else val for val in errAfter]
            dcOffset = int(statistics.mean(errAfter))
            errAfter = [val - dcOffset for val in errAfter]

            plt.figure()
            plt.plot(errBefore, label="Encoder error before LUT")
            plt.plot(errAfter, label="Encoder error after LUT")
            plt.legend()
            plt.xlabel('Sample count')
            plt.ylabel('Register units')
            plt.show()

            # Disable the driver
            print()
            print("Disabling the driver...")
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
    tmc6460_eval.write(TMC6460.REGMAP.FEEDBACK.OUTPUT_CONF.PHI_E_SRC.choice.LOOKUP_B)

    # Torque and flux PI
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_CONFIG.CURRENT_NORM_P, PI_CURRENT_P_NORM)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_CONFIG.CURRENT_NORM_I, PI_CURRENT_I_NORM)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_FLUX_COEFF.FLUX_P, PI_CURRENT_P)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_FLUX_COEFF.FLUX_I, PI_CURRENT_I)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_COEFF.TORQUE_P, PI_CURRENT_P)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_COEFF.TORQUE_I, PI_CURRENT_I)

    tmc6460_eval.write(TMC6460.REGMAP.RAMPER.POSITION.POSITION, 0)
    tmc6460_eval.write(TMC6460.REGMAP.RAMPER.PHI_E.PHI_E_OFFSET, 0)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_MODE.choice.RAMP_VELOCITY)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_USE_PHI_E, 1)
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.RAMP_EN, 1)

    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_POSITION_ACTUAL.PID_POSITION_ACTUAL, 0)
    tmc6460_eval.write(TMC6460.REGMAP.FOC.PID_TORQUE_FLUX_TARGET, OPENLOOP_CURRENT)
    # Enable current control mode
    tmc6460_eval.write(TMC6460.REGMAP.MCC_CONFIG.MOTOR_MOTION.MOTION_MODE.choice.TORQUE)

    time.sleep(1)

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