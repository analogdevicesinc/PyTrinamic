################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import Landungsbruecke


cm = ConnectionManager()

with cm.connect() as interface:
    lb = Landungsbruecke(interface)

    print("ID EEPROM content:")
    print("Mc: ", lb.eeprom_drv.read_id_info())
    print("Drv:", lb.eeprom_mc.read_id_info())

    print("Board IDs:")
    print(lb.get_board_ids())

    print("Board Names:")
    print(lb.get_board_names())