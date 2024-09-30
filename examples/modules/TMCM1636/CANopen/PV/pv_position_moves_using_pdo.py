################################################################################
# Copyright © 2020 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

"""Run a TMCM-1636 in "Profile Velocity Mode" using PDOs.

Before you run the script replace <path/to/TMCM-1636.eds> with the path of the downloaded TMCM-1636's eds file.

Includes the recording and plotting of the actual velocity.

Required Python packages:
* `canopen`
* `matplotlib`

Tested with:
* Firmware version 1.13
* Using the Python canopen package version 1.2.1.
* TMCM-1636 reset to factory default
"""

import time
import statistics
import dataclasses

import canopen
import matplotlib.pyplot as plt


class Tmcm1636(canopen.RemoteNode):
    class ModeOfOperation:
        NO_MODE = 0
        PROFILE_POSITION_MODE = 1
        PROFILE_VELOCITY_MODE = 3
        HOMING_MODE = 6
        CYCLIC_SYNCHRONOUS_POSITION_MODE = 8
        CYCLIC_SYNCHRONOUS_VELOCITY_MODE = 9
        CYCLIC_SYNCHRONOUS_TORQUE_MODE = 10

    class Cmd:
        SHUTDOWN = 6
        SWITCH_ON = 7
        ENABLE_OPERATION = 15
        NEW_SET_POINT = 16
        FAULT_RESET = 128

    class CommutationMode:
        DISABLED = 0
        OPEN_LOOP = 1
        DIGITAL_HALL = 2
        ABN_ENCODER = 3

    class StateMachineFault(Exception):
        pass

    def __init__(self, *args, **kwargs):
        super(Tmcm1636, self).__init__(*args, **kwargs)

    def adc_offset_correction(self):
        @dataclasses.dataclass
        class AdcChannel:
            value_obj: int
            offset_obj: int

        channel1 = AdcChannel(self.sdo['ADC Configuration']['ADC_I0_Raw'],
                              self.sdo['ADC Configuration']['ADC_I0_Offset'])
        channel2 = AdcChannel(self.sdo['ADC Configuration']['ADC_I1_Raw'],
                              self.sdo['ADC Configuration']['ADC_I1_Offset'])
        last_commutation_mode = self.sdo['Commutation Mode'].raw
        self.sdo['Commutation Mode'].raw = 0
        for ch in [channel1, channel2]:
            adc_samples = [ch.value_obj.raw for _ in range(40)]
            adc_samples_mean = round(statistics.mean(adc_samples))
            ch.offset_obj.raw = adc_samples_mean
        self.sdo['Commutation Mode'].raw = last_commutation_mode

    def go_to_operation_enabled(self):
        # clear an eventually present fault
        state = self.get_state()
        if state == 'Fault':
            self.sdo['Controlword'].raw = self.Cmd.FAULT_RESET
            while 1:
                state = self.get_state()
                if state == 'Switch on disable':
                    break
                time.sleep(1)
        sequence_from_state = {
            'Switch on disable': [(self.Cmd.SHUTDOWN, 'Ready to switch on'),
                                  (self.Cmd.SWITCH_ON, 'Switched on'),
                                  (self.Cmd.ENABLE_OPERATION, 'Operation enabled')],
            'Ready to switch on': [(self.Cmd.SWITCH_ON, 'Switched on'),
                                   (self.Cmd.ENABLE_OPERATION, 'Operation enabled')],
            'Switched on': [(self.Cmd.ENABLE_OPERATION, 'Operation enabled')],
            'Operation enabled': [],
        }
        # go up the state machine states
        for cmd, expected_status in sequence_from_state[state]:
            self.sdo['Controlword'].raw = cmd
            time.sleep(0.1)
            while 1:
                state = self.get_state()
                if state == 'Fault':
                    raise self.StateMachineFault(f'Fault when transitioning to {expected_status}')
                if state == expected_status:
                    break

    def shutdown(self):
        if self.get_state() != 'Switch on disable':
            self.sdo['Controlword'].raw = 0
            time.sleep(0.1)

    def get_state(self):
        states = [
            ('Not ready to switch on', 0b0000_0000_0100_1111, 0b0000_0000_0000_0000),
            ('Switch on disable', 0b0000_0000_0100_1111, 0b0000_0000_0100_0000),
            ('Ready to switch on', 0b0000_0000_0110_1111, 0b0000_0000_0010_0001),
            ('Switched on', 0b0000_0000_0110_1111, 0b0000_0000_0010_0011),
            ('Operation enabled', 0b0000_0000_0110_1111, 0b0000_0000_0010_0111),
            ('Quick Stop active', 0b0000_0000_0110_1111, 0b0000_0000_0000_0111),
            ('Fault reaction active', 0b0000_0000_0100_1111, 0b0000_0000_0000_1111),
            ('Fault', 0b0000_0000_0100_1111, 0b0000_0000_0000_1000),
        ]
        statusword = self.sdo['Statusword'].raw
        for name, mask, bits in states:
            if (statusword & mask) == bits:
                return name

    def get_motor_status_flags(self):
        flags_list = {
            0x0000_0001: 'OVERCURRENT',
            0x0000_0002: 'UNDERVOLTAGE',
            0x0000_0004: 'OVERVOLTAGE',
            0x0000_0010: 'MOTORHALTED',
            0x0000_0100: 'STOPMODE',
            0x0000_0200: 'VELOCITYMODE',
            0x0000_0400: 'POSITIONMODE',
            0x0000_0800: 'TORQUEMODE',
            0x0000_8000: 'INITIALIZED',
        }
        msf = self.sdo['Motor Status Flags'].raw
        active_flags_by_name = []
        for flag_mask, flag_name in flags_list.items():
            if msf & flag_mask:
                active_flags_by_name.append(flag_name)
        return '|'.join(active_flags_by_name[::-1])


reset_module_at_start = False

samples = []


@dataclasses.dataclass
class Sample:
    timestamp: float
    velocity: int


def tpdo4_callback(message):
    global samples
    velocity = message["Velocity Actual Value"].raw
    timestamp = message.timestamp
    samples.append(Sample(timestamp=timestamp, velocity=velocity))


with canopen.Network() as network:
    network.connect(bustype="kvaser", channel=0, bitrate=1_000_000)

    tmcm_1636 = Tmcm1636(1, "<path/to/TMCM-1636.eds>")
    network.add_node(tmcm_1636)

    if reset_module_at_start:
        tmcm_1636.nmt.send_command(0x81)   #Reset
        tmcm_1636.nmt.wait_for_bootup()

    tmcm_1636.adc_offset_correction()

    # The settings that depend on your hardware setup
    # PROBABLY NEEDS TO BE EDITED!
    tmcm_1636.sdo["ABN Encoder Settings"]["Direction"].raw = 1
    tmcm_1636.sdo["ABN Encoder Settings"]["Steps"].raw = 4096

    # Settings you might want to change
    tmcm_1636.sdo["Profile Acceleration"].raw = 2_000
    tmcm_1636.sdo["Profile Velocity in pp-mode"].raw = 4_000
    tmcm_1636.sdo["Position Scaler"].raw = tmcm_1636.sdo["ABN Encoder Settings"]["Steps"].raw
    tmcm_1636.sdo["Position Window"].raw = tmcm_1636.sdo["ABN Encoder Settings"]["Steps"].raw / 8
    tmcm_1636.sdo["Position Window Time"].raw = 100  # ms

    # Commutation based on ABN encoder feedback
    tmcm_1636.sdo["Commutation Mode"].raw = tmcm_1636.CommutationMode.ABN_ENCODER

    # Profile Velocity Mode
    tmcm_1636.sdo["Modes of Operation"].raw = tmcm_1636.ModeOfOperation.PROFILE_VELOCITY_MODE

    tmcm_1636.load_configuration()
    tmcm_1636.nmt.state = "OPERATIONAL"

    tmcm_1636.go_to_operation_enabled()

    tmcm_1636.tpdo[4].add_callback(tpdo4_callback)

    target_velocity = 500

    tmcm_1636.rpdo[4]["Controlword"].raw = 15
    tmcm_1636.rpdo[4]["Target Velocity"].raw = target_velocity
    tmcm_1636.rpdo[4].transmit()
    time.sleep(5)
    tmcm_1636.rpdo[4]["Target Velocity"].raw = 0
    tmcm_1636.rpdo[4].transmit()
    time.sleep(2)

    tmcm_1636.nmt.state = "PRE-OPERATIONAL"

fig, ax = plt.subplots()
t = [s.timestamp for s in samples]
v = [s.velocity for s in samples]
ax.plot(t, v)
plt.show()


