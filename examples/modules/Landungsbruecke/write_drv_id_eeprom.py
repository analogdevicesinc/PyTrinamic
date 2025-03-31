################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Please do not use unless you know what you are doing!"""

from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import Landungsbruecke


cm = ConnectionManager()

with cm.connect() as interface:
    lb = Landungsbruecke(interface)

    lb.id_eeprom_drv.write_id_info(
        description="TMC6200",
        board_id=10, # Check out Landungsbruecke.mc_id_names for a list of IDs
        hw_major_version=1, # Board has printed version 1.1 on it
        hw_minor_version=1, # Board has printed version 1.1 on it
    )
