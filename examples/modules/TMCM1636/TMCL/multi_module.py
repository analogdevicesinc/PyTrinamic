################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""Example script for the TMCM-1636-TMCL that shows how to access two modules within one CAN network."""

from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1636


connection_manager = ConnectionManager("--interface kvaser_tmcl")

with connection_manager.connect() as my_interface:

    modules = [
        TMCM1636(my_interface, module_id=1),
        TMCM1636(my_interface, module_id=3),
    ]

    for module in modules:
        motor = module.motors[0]
        print(motor.get_axis_parameter(motor.AP.AdcOffsetPhaseA))

