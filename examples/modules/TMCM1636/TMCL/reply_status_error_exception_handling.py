################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""This example demonstrates how to handle TMCLReplyStatusErrors when communicating with the TMCM-1636 module."""

from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1636
from pytrinamic.tmcl import TMCLReplyStatusError


with ConnectionManager("--interface kvaser_tmcl").connect() as my_interface:
    module = TMCM1636(my_interface)

    try:
        module.get_axis_parameter(ap_type=255, axis=0)
    except TMCLReplyStatusError as e:
        print(f"TMCL status code: {e.status_code}")
        print(f"Error occurred: {e}")
