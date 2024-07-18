################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

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

# >>> put in your code here <<<

# ========================================

# Set baud rate back to default (do not read afterwards)
my_interface.serial.write(struct.pack(">BI", TMC4671.REG.UART_BPS | 0x80, default_baud_rate))

my_interface.close()

print("\nReady.")
