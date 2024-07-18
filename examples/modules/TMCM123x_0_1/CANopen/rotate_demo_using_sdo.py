################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Uses SDO to rotate the motor for 5 seconds in profile velocity mode.
"""
import time
import canopen
from pytrinamic.modules.canopen_node import TmcmNode

with canopen.Network() as network:
    network.connect(channel='0', bustype='kvaser', bitrate=1_000_000)

    tmcm_123x_0_1 = TmcmNode(1, 'TMCM-1230.eds')
    network.add_node(tmcm_123x_0_1)
    # Profile Velocity Mode
    tmcm_123x_0_1.sdo['Modes of Operation 1'].raw = tmcm_123x_0_1.ModeOfOperation.PROFILE_VELOCITY_MODE

    tmcm_123x_0_1.load_configuration()
    tmcm_123x_0_1.nmt.state = 'OPERATIONAL'

    tmcm_123x_0_1.go_to_operation_enabled()
    tmcm_123x_0_1.sdo['Absolute Max Current 1'].raw = 50
    tmcm_123x_0_1.sdo['Stop On Stall 1'].raw = 0


    target_velocity = 10000
    print("Rotating the motor...")
    tmcm_123x_0_1.sdo['Target Velocity 1'].raw = target_velocity
    time.sleep(5)
    tmcm_123x_0_1.sdo['Target Velocity 1'].raw = 0
    print("Motor stopped!")

    tmcm_123x_0_1.nmt.state = 'PRE-OPERATIONAL'
    tmcm_123x_0_1.shutdown()



