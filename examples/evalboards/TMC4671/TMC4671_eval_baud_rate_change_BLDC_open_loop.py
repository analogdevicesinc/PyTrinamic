################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import time
import struct
import pytrinamic
from pytrinamic.connections import UartIcInterface
from pytrinamic.ic import TMC4671

pytrinamic.show_info()

default_data_rate = 9600
default_baud_rate = 0x00009600

new_data_rate = 115200
new_baud_rate = 0x00115200

# new_data_rate = 921600                # not working correctly with pyserial?
# new_baud_rate = 0x00921600            # not working correctly with pyserial?

# new_data_rate = 3000000
# new_baud_rate = 0x03000000

# Open connection with standard baud rate
my_interface = UartIcInterface('COM10', datarate=default_data_rate)

# Read actual baud rate
print("Actual baud rate:  \t", hex(my_interface.send(TMC4671.REG.UART_BPS, 0x0).value))

# Update baud rate (do not read afterwards)
print("Change baud rate:\t", hex(new_baud_rate))
my_interface.serial.write(struct.pack(">BI", TMC4671.REG.UART_BPS | 0x80, new_baud_rate))

my_interface.close()

# Open connection with new baud rate
my_interface = UartIcInterface('COM10', datarate=new_data_rate)
mc = TMC4671(my_interface)

# Read actual baud rate
print("New baud rate: \t\t", hex(my_interface.send(TMC4671.REG.UART_BPS, 0x0).value))

# ========================================

# Configure TMC4671 for a BLDC motor in open loop mode

# Motor type & PWM configuration
mc.write_register_field(mc.FIELD.MOTOR_TYPE, mc.ENUM.MOTOR_TYPE_BLDC)
mc.write_register_field(mc.FIELD.N_POLE_PAIRS, 4)
mc.write_register(mc.REG.PWM_POLARITIES, 0x00000000)
mc.write_register(mc.REG.PWM_MAXCNT, int(0x00000F9F))
mc.write_register(mc.REG.PWM_BBM_H_BBM_L, 0x00000A0A)
mc.write_register_field(mc.FIELD.PWM_CHOP, mc.ENUM.PWM_CENTERED_FOR_FOC)
mc.write_register_field(mc.FIELD.PWM_SV, 1)

# ADC configuration
mc.write_register(mc.REG.ADC_I_SELECT, 0x18000100)
mc.write_register(mc.REG.dsADC_MCFG_B_MCFG_A, 0x00100010)
mc.write_register(mc.REG.dsADC_MCLK_A, 0x20000000)
mc.write_register(mc.REG.dsADC_MCLK_B, 0x00000000)
mc.write_register(mc.REG.dsADC_MDEC_B_MDEC_A, int(0x014E014E))
mc.write_register(mc.REG.ADC_I0_SCALE_OFFSET, 0x01008218)
mc.write_register(mc.REG.ADC_I1_SCALE_OFFSET, 0x0100820A)
# mc.write_register(mc.REG.ADC_I0_SCALE_OFFSET, 0x01005D2B)
# mc.write_register(mc.REG.ADC_I1_SCALE_OFFSET, 0x01005C85)

# Open loop settings
mc.write_register(mc.REG.OPENLOOP_MODE, 0x00000000)
mc.write_register(mc.REG.OPENLOOP_ACCELERATION, 100)

# Feedback selection
mc.write_register(mc.REG.PHI_E_SELECTION, mc.ENUM.PHI_E_OPEN_LOOP)
mc.write_register(mc.REG.UQ_UD_EXT, 2000)

# ===== Open loop test drive =====

# Switch to open loop velocity mode
mc.write_register(mc.REG.MODE_RAMP_MODE_MOTION, mc.ENUM.MOTION_MODE_UQ_UD_EXT)

# Rotate right
print("Rotate right...")
mc.write_register(mc.REG.OPENLOOP_VELOCITY_TARGET, 200)
time.sleep(3)

# Rotate left
print("Rotate left...")
mc.write_register(mc.REG.OPENLOOP_VELOCITY_TARGET, -200)
time.sleep(6)

# Stop
print("Stop...")
mc.write_register(mc.REG.OPENLOOP_VELOCITY_TARGET, 0)
time.sleep(3)

# Unpower
print("Unpowered...")
mc.write_register(mc.REG.UQ_UD_EXT, 0)

# ========================================

# Set baud rate back to default (do not read afterwards)
my_interface.serial.write(struct.pack(">BI", TMC4671.REG.UART_BPS | 0x80, default_baud_rate))

my_interface.close()

print("\nReady.")
