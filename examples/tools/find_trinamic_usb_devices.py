################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import struct
from pytrinamic.connections import UsbTmclInterface
from pytrinamic.tmcl import TMCLCommand

com_ports = UsbTmclInterface.list()

for com_port in com_ports:
    with UsbTmclInterface(com_port) as connection:
        get_fw_result = connection.send(TMCLCommand.GET_FIRMWARE_VERSION, 1, 0, 0)
        fw_version_minor, fw_version_major, module_number = struct.unpack("<BBH", get_fw_result.value.to_bytes(4, byteorder='little'))
        print(f"Port {com_port}:")
        print(f"   Module number: {module_number}")
        print(f"   Firmware version: {fw_version_major}.{fw_version_minor}")