################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""Run a TMCM-123x_0_1 in "Profile Velocity Mode" using PDOs.

Includes the recording and plotting of actual velocity.

Tested with:
* Firmware version 3.26
* Using the Python canopen package version 2.0.0
"""
import time
import dataclasses
import canopen
import matplotlib.pyplot as plt
from pytrinamic.modules.canopen_node import TmcmNode


samples = []


@dataclasses.dataclass
class Sample:
    timestamp: float
    velocity: int


def tpdo4_callback(message):
    global samples
    velocity = message['Velocity Actual Value 1'].raw
    timestamp = message.timestamp
    samples.append(Sample(timestamp=timestamp, velocity=velocity))


with canopen.Network() as network:
    #network.connect(channel='PCAN_USBBUS1', bustype='pcan', bitrate=1_000_000)
    network.connect(channel=0, bustype='kvaser', bitrate=1_000_000)

    tmcm_123x_0_1 = TmcmNode(1, 'TMCM-1230.eds')
    network.add_node(tmcm_123x_0_1)

    # Reconfiguration
    tmcm_123x_0_1.sdo[0x1403][1].raw = 0x8000_0381  # disable the RPDO4
    tmcm_123x_0_1.sdo[0x1603][0].raw = 0            # write the number of entries into subindex 0
    tmcm_123x_0_1.sdo[0x1603][1].raw = 0x60400010
    tmcm_123x_0_1.sdo[0x1603][2].raw = 0x60FF0020
    tmcm_123x_0_1.sdo[0x1603][3].raw = 0x60600008
    tmcm_123x_0_1.sdo[0x1603][0].raw = 3            # write the number of entries into subindex 0
    tmcm_123x_0_1.sdo[0x1403][1].raw = 0x4000_0381  # enable the RPDO4

    tmcm_123x_0_1.load_configuration()
    tmcm_123x_0_1.nmt.state = 'OPERATIONAL'

    tmcm_123x_0_1.go_to_operation_enabled()

    tmcm_123x_0_1.tpdo[4].add_callback(tpdo4_callback)

    tmcm_123x_0_1.sdo['Absolute Max Current 1'].raw = 50
    tmcm_123x_0_1.sdo['Stop On Stall 1'].raw = 0

    target_velocity = 10000
    # Profile Velocity Mode
    tmcm_123x_0_1.rpdo[4]['Modes of Operation 1'].raw = tmcm_123x_0_1.ModeOfOperation.PROFILE_VELOCITY_MODE
    tmcm_123x_0_1.rpdo[4]['Controlword 1'].raw = tmcm_123x_0_1.Cmd.ENABLE_OPERATION
    tmcm_123x_0_1.rpdo[4]['Target Velocity 1'].raw = target_velocity
    tmcm_123x_0_1.rpdo[4].transmit()
    print("Motor rotating...")
    time.sleep(5)
    tmcm_123x_0_1.rpdo[4]['Target Velocity 1'].raw = 0
    tmcm_123x_0_1.rpdo[4].transmit()
    print("Motor stopped!")
    time.sleep(2)
    tmcm_123x_0_1.nmt.state = 'PRE-OPERATIONAL'
    tmcm_123x_0_1.shutdown()

fig, ax = plt.subplots()
t = [s.timestamp for s in samples]
v = [s.velocity for s in samples]
ax.plot(t, v)
ax.set_xlabel('Time')
ax.set_ylabel('Velocity')
plt.show()


