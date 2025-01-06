################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to use TMC9660-3PH-EVKIT to spin a BLDC motor with SPI encoder feedback.

An AS5047 SPI encoder is used for the rotor position feedback in this example.
If you want to use VCC_IO from the board to power the encoder,
keep in mind that you first upload the config before you connect VCC_IO to the encoders 3.3V input.

The required TMC-EvalSystem firmware is 3.10.7 or later.

Note: To run this script the TMC9660-3PH-EVAL first needs an uploaded/burned configuration
and the parameter app must have been started.

If the `example_mode` is set to "check angle", the script will check if the SPI encoder angle is plausible.
If the `example_mode` is set to "move motor closed loop", the script will move the motor in closed loop mode.

Use the `connection_mode` to change the hardware connection.

#############################################################################################################
# connection_mode == with_landungsbruecke
#############################################################################################################
On Windows the config upload and app start can be done with:
    python ubltools_1.0.1/ubl_evalsystem_wrapper.py <COM-PORT> write config tmc9660_3ph_eval_QBL_spi_enc.toml
    python ubltools_1.0.1/ubl_evalsystem_wrapper.py <COM-PORT> start
Where <COM-PORT> needs to be replaced by the COM port of the Landungsbruecke.

Important: first connect USB and then power the TMC9660-3PH-EVAL.

                                           +------------------------+                     
                                           | SPI encoder feedback   |                     
                                           |                        |                     
                             +-----+  +----|--------------+       +---++--------------+   
                      USB    |     |==|                   |-------|   ||              |   
                      -------|     |==|                   |-------|SPI||              |===
 Connected to the machine    |     |==|                   |-------|ENC||BLDC QBL4208  |   
 running this script.        |LB   |==|TMC9660-3PH-EVAL   |       +---++--------------+   
                             +-----+  +-------------------+                               

#############################################################################################################
# connection_mode == headless
#############################################################################################################
On Windows the config upload and app start can be done with:
        ubltools_1.0.1/ublcli.exe --port <COM-PORT> write config tmc9660_3ph_eval_QBL_spi_enc.toml
        ubltools_1.0.1/ublcli.exe --port <COM-PORT> start
Where <COM-PORT> needs to be replaced by the COM port of the USB-UART cable.

USB-UART Cable - Connected to the machine running this script.
   -------+                                                                     
          | +-------------------------+                     
          | |  SPI encoder feedback   |                     
          | |                         |                     
        +-|-|---------------+       +---++--------------+   
        |                   |-------|   ||              |   
        |                   |-------|SPI||              |===
        |                   |-------|ENC||BLDC QBL4208  |   
        |TMC9660-3PH-EVAL   |       +---++--------------+   
        +-------------------+                               
                                                                                          
"""
import time
import statistics
from dataclasses import dataclass
from typing import Literal, List
from ctypes import c_int16

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import TMC9660
from pytrinamic.evalboards import TMC9660_3PH_eval


example_mode: Literal["check angle", "move motor closed loop"] = "check angle"
connection_mode: Literal["with_landungsbruecke", "headless"] = "with_landungsbruecke"
com_port_in_headless_mode = "COM5" # Note: Change this to the com port of the USB-UART cable used.

if connection_mode == "with_landungsbruecke":
    cm = ConnectionManager()
elif connection_mode == "headless":
    cm = ConnectionManager(f"--interface serial_tmcl --port {com_port_in_headless_mode}")

with cm.connect() as my_interface:

    if connection_mode == "with_landungsbruecke":
        tmc9660_device = TMC9660_3PH_eval(my_interface)
    elif connection_mode == "headless":
        tmc9660_device = TMC9660(my_interface)

    # Motor settings
    tmc9660_device.set_axis_parameter(TMC9660.ap.MOTOR_TYPE.choice.BLDC_MOTOR)
    tmc9660_device.set_axis_parameter(TMC9660.ap.MOTOR_POLE_PAIRS, 4)

    # SPI encoder settings
    tmc9660_device.set_axis_parameter(TMC9660.ap.SPI_ENCODER_TRANSFER_DATA_3_0, 0x0000_FFFF)
    tmc9660_device.set_axis_parameter(TMC9660.ap.SPI_ENCODER_MAIN_TRANSFER_CMD_SIZE, 2)
    tmc9660_device.set_axis_parameter(TMC9660.ap.SPI_ENCODER_POSITION_COUNTER_MASK, 2**14 - 1)
    tmc9660_device.set_axis_parameter(TMC9660.ap.SPI_ENCODER_POSITION_COUNTER_SHIFT, 0)
    tmc9660_device.set_axis_parameter(TMC9660.ap.SPI_ENCODER_TRANSFER.choice.CONTINUOUS_POSITION_COUNTER_READ)
    tmc9660_device.set_axis_parameter(TMC9660.ap.SPI_ENCODER_DIRECTION, 1)

    if example_mode == "check angle":
        @dataclass
        class Sample:
            open_loop_position: int
            spi_enc_position: int

        # Configure the open loop mode
        tmc9660_device.set_axis_parameter(TMC9660.ap.OPENLOOP_VOLTAGE, 1000)
        tmc9660_device.set_axis_parameter(TMC9660.ap.COMMUTATION_MODE.choice.FOC_OPENLOOP_VOLTAGE_MODE)
        # Rotate the motor for 4 seconds
        tmc9660_device.set_axis_parameter(TMC9660.ap.TARGET_VELOCITY, 10_000)
        time.sleep(0.1)
        start_time_s = time.time()
        samples: List[Sample] = []
        samples_per_s: int = 10
        # .. and record the open loop angle and the SPI encoder angle
        while time.time() - start_time_s < 4:
            samples.append(Sample(tmc9660_device.get_axis_parameter(TMC9660.ap.OPENLOOP_ANGLE),
                                  tmc9660_device.get_axis_parameter(TMC9660.ap.SPI_ENCODER_COMMUTATION_ANGLE)))
            time.sleep(1/samples_per_s)
        # Stop the motor
        tmc9660_device.set_axis_parameter(TMC9660.ap.TARGET_VELOCITY, 0)
        time.sleep(0.1)
        tmc9660_device.set_axis_parameter(TMC9660.ap.COMMUTATION_MODE.choice.SYSTEM_OFF)
        # Do some checks
        slope_open_loop_angle = statistics.mean([c_int16(samples[i+1].open_loop_position - samples[i].open_loop_position).value for i in range(len(samples) - 1)]) * samples_per_s
        slope_spi_enc_angle = statistics.mean([c_int16(samples[i+1].spi_enc_position - samples[i].spi_enc_position).value for i in range(len(samples) - 1)]) * samples_per_s
        slope_error = abs(slope_spi_enc_angle - slope_open_loop_angle) / 2**16
        if abs(slope_spi_enc_angle) / 2**16 < 0.1:
            print("The SPI encoder angle does not or just barely change. Check the SPI encoder connection! Or maybe the open loop voltage is not high enough.")
        elif slope_open_loop_angle * slope_spi_enc_angle < 0:
            print("The the SPI encoder seems to be inverted. Try to invert the SPI_ENCODER_DIRECTION setting to fix this!")
        elif slope_error > 0.01:
            print(f"The SPI encoder angle slope is not parallel to the open-loop angle slope! The error is {slope_error:.3}.")
        else:
            print("The SPI encoder angle looks plausible.")
        # Plot the angles if matplotlib is installed
        if plt:
            fix, ax = plt.subplots()
            ax.plot([s.open_loop_position for s in samples], label="OPENLOOP_ANGLE")
            ax.plot([s.spi_enc_position for s in samples], label="SPI_ENCODER_COMMUTATION_ANGLE")
            ax.legend()
            plt.show()
        else:
            print("matplotlib is not installed. Install it with 'pip install matplotlib' to see the plot.")
    elif example_mode == "move motor closed loop":
        # Apply some PI controller settings, known to be good for the QBL4208.
        tmc9660_device.set_axis_parameter(TMC9660.ap.VELOCITY_NORM_P.choice.SHIFT_8_BIT)
        tmc9660_device.set_axis_parameter(TMC9660.ap.VELOCITY_P, 500)
        tmc9660_device.set_axis_parameter(TMC9660.ap.VELOCITY_I, 5000)
        # Configure SPI encoder based feedback
        tmc9660_device.set_axis_parameter(TMC9660.ap.COMMUTATION_MODE.choice.FOC_SPI_ENC)
        # Rotate the motor for 5 seconds
        tmc9660_device.set_axis_parameter(TMC9660.ap.TARGET_VELOCITY, 400_000)
        time.sleep(5)
        # Stop the motor
        tmc9660_device.set_axis_parameter(TMC9660.ap.TARGET_VELOCITY, 0)
        time.sleep(1)
        tmc9660_device.set_axis_parameter(TMC9660.ap.COMMUTATION_MODE.choice.SYSTEM_OFF)
