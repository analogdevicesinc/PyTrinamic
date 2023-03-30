"""Run a TMCM-1231 in "Profile Velocity Mode" using PDOs.

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
    network.connect(channel='PCAN_USBBUS1', bustype='pcan', bitrate=1_000_000)

    tmcm_1231 = TmcmNode(1, 'TMCM-1231.eds')
    network.add_node(tmcm_1231)

    # Reconfiguration
    tmcm_1231.sdo[0x1403][1].raw = 0x8000_0381  # disable the RPDO4
    tmcm_1231.sdo[0x1603][0].raw = 0            # write the number of entries into subindex 0
    tmcm_1231.sdo[0x1603][1].raw = 0x60400010
    tmcm_1231.sdo[0x1603][2].raw = 0x60FF0020
    tmcm_1231.sdo[0x1603][3].raw = 0x60600008
    tmcm_1231.sdo[0x1603][0].raw = 3            # write the number of entries into subindex 0
    tmcm_1231.sdo[0x1403][1].raw = 0x4000_0381  # enable the RPDO4

    tmcm_1231.load_configuration()
    tmcm_1231.nmt.state = 'OPERATIONAL'

    tmcm_1231.go_to_operation_enabled()

    tmcm_1231.tpdo[4].add_callback(tpdo4_callback)

    tmcm_1231.sdo['Absolute Max Current 1'].raw = 50
    tmcm_1231.sdo['Stop On Stall 1'].raw = 0

    target_velocity = 10000
    # Profile Velocity Mode
    tmcm_1231.rpdo[4]['Modes of Operation 1'].raw = tmcm_1231.ModeOfOperation.PROFILE_VELOCITY_MODE
    tmcm_1231.rpdo[4]['Controlword 1'].raw = tmcm_1231.Cmd.ENABLE_OPERATION
    tmcm_1231.rpdo[4]['Target Velocity 1'].raw = target_velocity
    tmcm_1231.rpdo[4].transmit()
    print("Motor rotating...")
    time.sleep(5)
    tmcm_1231.rpdo[4]['Target Velocity 1'].raw = 0
    tmcm_1231.rpdo[4].transmit()
    print("Motor stopped!")
    time.sleep(2)
    tmcm_1231.nmt.state = 'PRE-OPERATIONAL'
    tmcm_1231.shutdown()

fig, ax = plt.subplots()
t = [s.timestamp for s in samples]
v = [s.velocity for s in samples]
ax.plot(t, v)
ax.set_xlabel('Time')
ax.set_ylabel('Velocity')
plt.show()


