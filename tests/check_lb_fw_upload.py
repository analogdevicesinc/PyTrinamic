################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""This script checks the firmware upload CLI tool tmclfwupload.

A standard Landungsbruecke is used for this check, please connect one via USB.
The hex files are downloaded from the internet, so you need internet connection to run this script.
"""

import time
import urllib
import struct
import subprocess
import urllib.request

from pytrinamic.connections import ConnectionManager
from pytrinamic.tmcl import TMCLCommand


lb_fw_3_10_1_hex = urllib.request.urlretrieve("https://github.com/analogdevicesinc/TMC-EvalSystem/releases/download/3.10.1/Landungsbruecke_v3.10.1_BL.hex")[0]
lb_fw_3_10_2_hex = urllib.request.urlretrieve("https://github.com/analogdevicesinc/TMC-EvalSystem/releases/download/3.10.2/Landungsbruecke_v3.10.2_BL.hex")[0]

for hex, expected_build_version in [(lb_fw_3_10_1_hex, 3101), (lb_fw_3_10_2_hex, 3102)]:

    subprocess.run(["tmclfwupload", hex])

    time.sleep(5)

    cm = ConnectionManager()

    with cm.connect() as interface:

        get_fw_result = interface.send(TMCLCommand.GET_FIRMWARE_VERSION, 1, 0, 0)
        fw_version_minor, fw_version_major, module_number = struct.unpack("<BBH", get_fw_result.value.to_bytes(4, byteorder='little'))
        assert module_number == 12
        assert fw_version_major == 3
        assert fw_version_minor == 10
        get_fw_result = interface.send(TMCLCommand.GET_FIRMWARE_VERSION, 5, 0, 0)
        assert get_fw_result.value == expected_build_version
