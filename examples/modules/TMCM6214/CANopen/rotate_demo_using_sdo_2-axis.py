################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Uses SDO to rotate  motor1 and motor3 for 5 seconds in profile velocity mode.

Tested with:
* Firmware version 3.22
* Using the Python canopen package version 2.0.0
"""
import time
import canopen
from pytrinamic.modules.canopen_node import TmcmNode

with canopen.Network() as network:
    network.connect(channel='PCAN_USBBUS1', bustype='pcan', bitrate=1_000_000)

    tmcm_6214 = TmcmNode(1, 'TMCM-6214.eds')
    motor=[1,3]
    network.add_node(tmcm_6214)


    # Profile Velocity Mode
    if tmcm_6214.sdo['Modes of Operation {number}'.format(number=motor[0])].raw != tmcm_6214.ModeOfOperation.PROFILE_VELOCITY_MODE:
        tmcm_6214.sdo['Modes of Operation {number}'.format(number=motor[0])].raw = tmcm_6214.ModeOfOperation.PROFILE_VELOCITY_MODE
    if tmcm_6214.sdo['Modes of Operation {number}'.format(number=motor[1])].raw != tmcm_6214.ModeOfOperation.PROFILE_VELOCITY_MODE:
        tmcm_6214.sdo['Modes of Operation {number}'.format(number=motor[1])].raw = tmcm_6214.ModeOfOperation.PROFILE_VELOCITY_MODE


    tmcm_6214.load_configuration()
    tmcm_6214.nmt.state = 'OPERATIONAL'

    tmcm_6214.go_to_operation_enabled(motor[0])
    tmcm_6214.go_to_operation_enabled(motor[1])


    tmcm_6214.sdo['Absolute Max Current {number}'.format(number=motor[0])].raw = 50
    tmcm_6214.sdo['Stop On Stall {number}'.format(number=motor[0])].raw = 0
    tmcm_6214.sdo['Absolute Max Current {number}'.format(number=motor[1])].raw = 50
    tmcm_6214.sdo['Stop On Stall {number}'.format(number=motor[1])].raw = 0

    target_velocity = 51200
    print("Rotating the motor...")

    tmcm_6214.sdo['Target Velocity {number}'.format(number=motor[0])].raw = target_velocity
    tmcm_6214.sdo['Target Velocity {number}'.format(number=motor[1])].raw = target_velocity


    time.sleep(5)

    tmcm_6214.sdo['Target Velocity {number}'.format(number=motor[0])].raw = 0
    tmcm_6214.sdo['Target Velocity {number}'.format(number=motor[1])].raw = 0

    print("Motor stopped!")

    tmcm_6214.nmt.state = 'PRE-OPERATIONAL'
    tmcm_6214.shutdown(motor[0])
    tmcm_6214.shutdown(motor[1])



