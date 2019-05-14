#!/usr/bin/env python3
'''
Created on 13 May 2019

@author: LH
'''
import sys
import time
import math
import re
import struct

import PyTrinamic
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
from PyTrinamic.TMCL import TMCL_Command
from serial import SerialException

# Timeout in seconds for reconnecting to the module after sending the TMCL_BOOT
# command.
SERIAL_BOOT_TIMEOUT = 10
################################# Preparation ##################################
PyTrinamic.showInfo()

if len(sys.argv) < 2:
    print("Usage: FirmwareUpdate.py HexFilePath")
    exit(1)

print("Opening hex file (" + sys.argv[1] + ")")

try:
    f = open(sys.argv[1], "rt")
except FileNotFoundError:
    print("Error: Hex file not found")
    exit(1)

############################### Hex file parsing ###############################
print("Parsing hex file")

data = []
extendedAddress = 0
segmentAddress  = 0
for lineNumber, line in enumerate(f, 1):
    ### Parse a hex file line
    # Check for RECORD MARK
    if line[0] != ':':
        continue

    # CHKSUM validation
    # All Bytes summed together modulo 256 have to be 0
    checksum = 0
    for i in range(1, len(line)-1, 2):
        checksum = checksum + int(line[i:i+2], 16)
    if checksum % 256 != 0:
        print("Error: Invalid Checksum in line " + str(lineNumber))
        exit(1)

    # Read the fields of the entry
    rec_len      = int(line[1:3], 16)
    rec_address  = int(line[3:7], 16)
    rec_type     = int(line[7:9], 16)
    rec_data     = line[9:rec_len*2+9]

    # RECLEN validation
    # Total characters:
    #     1: RECORD MARK
    #     2: RECLEN
    #     4: LOAD OFFSET
    #     2: RECTYPE
    #     RECLEN*2: DATA / INFO
    #     2: CHKSUM
    #     1: \n
    if 1 + 2 + 4 + 2 + (rec_len*2) + 2 + 1 != len(line):
        print("Error: Invalid record length in line " + str(lineNumber))

    ### Record type distinction
    if rec_type == 0:
        # Type: Data Record
        address = extendedAddress + segmentAddress + rec_address
        if address % 4 != 0:
            print("Error: Address is not 4-Byte aligned (Line " + str(lineNumber) +")")
            exit(1)

        data.append((address, rec_len, rec_data))

    if rec_type == 1:
        # Type: End of File Record
        break

    if rec_type == 2:
        # Type: Extended Segment Address Record
        segmentAddress = int(rec_data, 16) * 0x10

        if extendedAddress != 0:
            print("Warning: Hex file uses both Type 2 and Type 4 records!")

    if rec_type == 3:
        # Type: Start Segment Address Record
        # Ignore this record
        pass

    if rec_type == 4:
        # Type: Extended Linear Address Record
        extendedAddress = int(rec_data, 16) * 0x10000
        print("Extended Address: " + hex(extendedAddress))

        if segmentAddress != 0:
            print("Warning: Hex file uses both Type 2 and Type 4 records!")

    if rec_type == 5:
        # Type: Start Linear Address Record
        # Ignore this record
        pass

print("Parsed " + str(lineNumber) + " lines containing " + str(len(data)) + " data records")

# Make sure that the data is sorted by address
data.sort(key=lambda x:x[0])

f.close()

print()

########################### Binary data preparation ############################

# Get the boundaries and size of the data
start_address = data[0][0]
end_address   = data[-1][0] + data[-1][1]
length = end_address - start_address

# Extract the parsed hex data into a bytearray
byteData = bytearray(length)
checksum = 0
for entry in data:
    address = entry[0]

    for i in range(0, entry[1]):
        value = int(entry[2][i*2:(i+1)*2], 16)
        checksum  = (checksum + value) & 0xFFFFFFFF
        byteData[address-start_address + i] = value

print("Start address: 0x{0:08X}".format(start_address))
print("End address:   0x{0:08X}".format(end_address))
print("Length:        0x{0:08X}".format(length))
print("Checksum:      0x{0:08X}".format(checksum))

print()

############################## Bootloader entry ################################ 
# Connect to the evaluation board
print("Connecting")
myInterface = serial_tmcl_interface(PyTrinamic.firstAvailableComPort(USB=True))

# Send the boot command
print("Switching to bootloader mode")
myInterface.sendBoot(1)
myInterface.close()

# Reconnect after a small delay
print("Reconnecting")
timestamp = time.time()
while (time.time() - timestamp) < SERIAL_BOOT_TIMEOUT:
    try:
        # Attempt to connect
        myInterface = serial_tmcl_interface(PyTrinamic.firstAvailableComPort(USB=True))
        # If no exception occured, exit the retry loop
        break
    except SerialException:
        myInterface = None

if not(myInterface):
    print("Error: Timeout when attempting to reconnect to bootloader")
    exit(1)

# Retrieve the bootloader version
bootloaderVersion = myInterface.getVersionString(1)
found = re.search("\d\d\d\dB\d\d\d", bootloaderVersion)
if found:
    pattern = found.group(0)[0:4] + "V\d\d\d"
    print("Scanning new firmware data for correct module string (" + found.group(0)[0:4] + "V###)")
else:
    found = re.search("\d\d\dB\d\.\d\d", bootloaderVersion)
    if found:
        pattern = found.group(0)[0:3] + "V\d\.\d\d"
        print("Scanning new firmware data for correct module string (" + found.group(0)[0:3] + "V#.##)")
    else:
        print("Error: GetVersion returned invalid answer (" + bootloaderVersion + ")")
        exit(1)

# Scan for the module string
firmwareString = str(byteData, encoding="ascii", errors="ignore")
found = re.search(pattern, firmwareString)
if not(found):
    print("Error: No matching version string found in firmware image")
    exit(1)

print("Bootloader version: " + bootloaderVersion)
print("Firmware version:   " + found.group(0))

print()

# Get the memory parameters
reply = myInterface.send(1, TMCL_Command.BOOT_GET_INFO, 0, 0, 0)
mem_page_size = reply.value
reply = myInterface.send(1, TMCL_Command.BOOT_GET_INFO, 1, 0, 0)
mem_start_address = reply.value
reply = myInterface.send(1, TMCL_Command.BOOT_GET_INFO, 2, 0, 0)
mem_size = reply.value

# Check if the page size is a power of two
if not(((mem_page_size & (mem_page_size - 1)) == 0) and mem_page_size != 0):
    print("Error: Page size of module is not a power of two")
    exit(1)

# Check if the start addresses match
if start_address != mem_start_address:
    print("Error: Start address of firmware does not match start address of bootloader")
    exit(1)

############################### Firmware upload ################################

# Erase the old firmware
print("Erasing the old firmware")
reply = myInterface.send(1, TMCL_Command.BOOT_ERASE_ALL, 0, 0, 0)

# Calculate the starting page
current_page        = math.floor(start_address/mem_page_size) * mem_page_size
# Store the internal page buffer state
current_page_dirty  = False

# Helper function: BOOT_WRITE_PAGE safety wrapper
def writePage(page):
    if page == 0:
        raise ValueError

    print("Writing page 0x{0:08X}".format(page))
    myInterface.send(1, TMCL_Command.BOOT_WRITE_PAGE, 0, 0, current_page)

# Helper function: Write a 32 bit data block
def write32Bit(address, writeData):
    global current_page
    global current_page_dirty

    # Split the address of the entry into page/offset values
    page    = math.floor(address/mem_page_size) * mem_page_size
    offset  = address - page

    if page != current_page:
        writePage(current_page)
        current_page = page
        current_page_dirty = False

    #print("Writing {0:08X} to offset {1:04X} on page {2:08X}".format(writeData, offset, page))
    myInterface.send(1, TMCL_Command.BOOT_WRITE_BUFFER, math.floor(offset/4) % 256, math.floor(math.floor(offset/4) / 256), writeData)
    current_page_dirty = True

for i in range(0, len(byteData), 4):
    address = i + start_address
    value = struct.unpack("<I", byteData[i:i+4])[0]
    write32Bit(address, value)

# If the last page didn't get written yet, write it
if current_page_dirty:
    writePage(current_page)

print()

# Checksum verification
reply = myInterface.send(1, TMCL_Command.BOOT_GET_CHECKSUM, 0, 0, end_address-1)
if reply.value != checksum:
    print("Error: Checksums dont match! (Checksum: 0x{0:08X}, received: 0x{1:08X}".format(checksum, reply.value))
    exit(1)

print("Checksum of the uploaded firmware matches")
print("Finalizing upload (Writing length and checksum)")
# Write firmware length
myInterface.send(1, TMCL_Command.BOOT_WRITE_LENGTH, 0, 0, length)
# Write firmware checksum
myInterface.send(1, TMCL_Command.BOOT_WRITE_LENGTH, 1, 0, checksum)

# Restart the firmware
print("Starting the firmware")
myInterface.send(1, TMCL_Command.BOOT_START_APPL, 0, 0, 0)
