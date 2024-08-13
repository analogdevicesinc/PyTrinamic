################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""This file showcases how to use multiple Eval-Systems at once.

To get the names of the COM-ports use ether the Windows "Device Manager" or
pySerial's `list_port`: https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.list_ports.
"""

import struct

from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import Landungsbruecke
from pytrinamic.tmcl import TMCLCommand


with ConnectionManager("--port=COM5").connect() as iface0, ConnectionManager("--port=COM6").connect() as iface1 :

    # Print the Landungsbruecke's firmware version
    # =============================================================================================
    for i, iface in enumerate([iface0, iface1]):
        get_fw_result = iface.send(TMCLCommand.GET_FIRMWARE_VERSION, 1, 0, 0)
        fw_version_minor, fw_version_major, module_number = struct.unpack("<BBH", get_fw_result.value.to_bytes(4, byteorder='little'))
        print(f"Board {i}: firmware {fw_version_major}.{fw_version_minor}")

    # Retrieve the connected boards at each Landungsbruecke
    # =============================================================================================
    lb0 = Landungsbruecke(iface0)
    lb1 = Landungsbruecke(iface1)
    for i, lb in enumerate([lb0, lb1]):
        print(f"Board {i}: connected eval(s): {lb.get_board_names()}")

    # Example on how to use both Landungsbruecke in case both have TMC4671 and TMC6100 connected to
    # =============================================================================================
    # mc_eval0 = TMC4671_eval(iface0)
    # drv_eval0 = TMC6100_eval(iface0)
    # mc_eval1 = TMC4671_eval(iface1)
    # drv_eval1 = TMC6100_eval(iface1)
    
    # # Initialize the driver registers
    # for drv_eval in [drv_eval0, drv_eval1]:
    #     drv_eval.write_register_field(TMC6100.FIELD.SINGLELINE, 0)

    # # Initialize the motor controller registers
    # for mc_eval in [mc_eval0, mc_eval1]:
    #     mc_eval.write_register_field(TMC4671.FIELD.MOTOR_TYPE, TMC4671.ENUM.MOTOR_TYPE_BLDC)