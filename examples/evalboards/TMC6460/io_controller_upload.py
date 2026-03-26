#!/usr/bin/env python
################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

"""
Upload a hex file program to the TMC6460 IOController SRAM
"""

import argparse
import logging
import time
import os
import sys

import intelhex
from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import TMC6460
from pytrinamic.evalboards import TMC6460_eval


with ConnectionManager().connect() as my_interface:
    tmc6460_eval = TMC6460_eval(my_interface)

    parser = argparse.ArgumentParser()
    parser.add_argument("hexfile", type=argparse.FileType("r"), help="Hex file that needs to be uploaded")
    parser.add_argument('--verify', action=argparse.BooleanOptionalAction, default=True, help="To verify that contents "
                                                                                            "of program memory and "
                                                                                            "hex-file are equal")
    parser.add_argument('-v', '--verbose', action="count", default=0, help="Verbosity level")
    args = parser.parse_args()

    if args.verbose == 0:
        log_level = logging.ERROR
    elif args.verbose == 1:
        log_level = logging.WARNING
    elif args.verbose == 2:
        log_level = logging.INFO
    elif args.verbose >= 3:
        log_level = logging.DEBUG

    # Create local logger
    logging.basicConfig(stream=sys.stdout, level=log_level)

    # Check the input file type
    if os.path.splitext(args.hexfile.name)[1] != ".hex":
        print(f"Input file is not a hex file ({args.hexfile})")
        exit(1)

    # Turn the IOController off
    tmc6460_eval.write(TMC6460.REGMAP.IO_CONTROLLER.COMMAND, 0x00000000)
    tmc6460_eval.write(TMC6460.REGMAP.IO_CONTROLLER.RESPONSE_0, 0x00000000)

    # Read out the running version
    tmc6460_eval.write(TMC6460.REGMAP.IO_CONTROLLER.COMMAND, 0xAA000000)
    bl_version = tmc6460_eval.read(TMC6460.REGMAP.IO_CONTROLLER.RESPONSE_1)
    print(f"Version: 0x{bl_version:08X}")

    def is_unprogrammed(program_version):
        # Upper 3 bytes contain the program type
        # Ensure that we are currently not running a program

        # P1 ROM code
        if program_version & 0xFFFFFF00 == 0x544D1000:
            return True

        # P2 & P3 ROM code
        if program_version & 0xFFFFFF00 == 0x64600000:
            return True

        return False

    if not is_unprogrammed(bl_version):
        print("Error: IO controller is already running a program")
        sys.exit(1)

    # load file
    hex_file = intelhex.IntelHex(args.hexfile)
    hex_file.padding = 0x00
    start_addr = hex_file.minaddr()
    end_addr   = hex_file.maxaddr()

    assert start_addr == 0, "Expected starting address is 0"
    assert end_addr < 0x2000

    # Download to TMC6460
    print("Loading Hex File into TMC6460...")
    for index in range(start_addr, end_addr, 2):
        command  = 0xB0000000 # Write RAM. Bits 27:16 address, bits 15:0 data
        command |= 0x0FFF0000 & ((index // 2) << 16)
        command |= 0x0000FF00 & (hex_file[index+1] << 8)
        command |= 0x000000FF & (hex_file[index])

        tmc6460_eval.write(TMC6460.REGMAP.IO_CONTROLLER.COMMAND, command)

    if args.verify:
        print("Verifying upload...")
        for index in range(start_addr, end_addr, 2):
            command  = 0xC0000000 # Command: Read RAM. Bits 27:16 address
            command |= 0x0FFF0000 & ((index // 2) << 16)
            tmc6460_eval.write(TMC6460.REGMAP.IO_CONTROLLER.COMMAND, command)
            value = tmc6460_eval.read(TMC6460.REGMAP.IO_CONTROLLER.RESPONSE_1)

            read_data = value & 0xFFFF
            file_data = (hex_file[index+1] << 8) | hex_file[index]
            if read_data != file_data:
                print("Error: Verification failed - content does not match!")
                sys.exit(1)

        print("Verification successful: contents of program memory and hex-file are equal!")

    print("Starting program in TMC6460 program memory ...")

    # Start program in TMC6460 memory
    tmc6460_eval.write(TMC6460.REGMAP.IO_CONTROLLER.COMMAND, 0xFFFFFFFF)
    time.sleep(0.05)

    # Turn the IOController off
    tmc6460_eval.write(TMC6460.REGMAP.IO_CONTROLLER.COMMAND, 0x00000000)
    tmc6460_eval.write(TMC6460.REGMAP.IO_CONTROLLER.RESPONSE_0, 0x00000000)

    # Get bootloader version
    tmc6460_eval.write(TMC6460.REGMAP.IO_CONTROLLER.COMMAND, 0xAA000000)
    time.sleep(0.05)
    version = tmc6460_eval.read(TMC6460.REGMAP.IO_CONTROLLER.RESPONSE_1)
    print(f"Running version: 0x{version:08X}")

