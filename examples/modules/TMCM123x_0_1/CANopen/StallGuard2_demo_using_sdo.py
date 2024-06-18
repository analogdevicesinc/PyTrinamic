################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Sets the StallGuard2 threshold such that the stall guard value (i.e SG value) is zero
when the motor comes close to stall and also sets the stop on stall velocity to a value
one less than the actual velocity of the motor
"""
import time
import canopen
from pytrinamic.modules.canopen_node import TmcmNode

def stallguard2_init(init_velocity):
    # Resetting SG2 threshold and stop on stall velocity to zero
    tmcm_123x_0_1.sdo['Stall Guard2 Threshold 1'].raw = 0
    tmcm_123x_0_1.sdo['Stop On Stall 1'].raw = 0
    print("Rotating...")
    tmcm_123x_0_1.sdo['Target Velocity 1'].raw = init_velocity
    sgthresh = 0
    sgt = 0
    load_samples = []
    while (sgt == 0) and (sgthresh < 64):
        load_samples = []
        tmcm_123x_0_1.sdo['Stall Guard2 Threshold 1'].raw = sgthresh
        time.sleep(0.2)
        sgthresh += 1
        for i in range(50):
            load_samples.append(tmcm_123x_0_1.sdo['Actual Load Value 1'].raw )
        if not any(load_samples):
            sgt = 0
        else:
            sgt = max(load_samples)
    while 1:
        load_samples = []
        for i in range(50):
            load_samples.append(tmcm_123x_0_1.sdo['Actual Load Value 1'].raw )
        if 0 in load_samples:
            tmcm_123x_0_1.sdo['Absolute Max Current 1'].raw = tmcm_123x_0_1.sdo['Absolute Max Current 1'].raw - 1
        else:
            break

    tmcm_123x_0_1.sdo['Stop On Stall 1'].raw = tmcm_123x_0_1.sdo['Velocity Actual Value 1'].raw - 1

def main():
    with canopen.Network() as network:
        network.connect(channel='0', bustype='kvaser', bitrate=1_000_000)

        global tmcm_123x_0_1
        tmcm_123x_0_1 = TmcmNode(1, 'TMCM-1230.eds')
        network.add_node(tmcm_123x_0_1)
        tmcm_123x_0_1.sdo['Modes of Operation 1'].raw = tmcm_123x_0_1.ModeOfOperation.PROFILE_VELOCITY_MODE

        tmcm_123x_0_1.load_configuration()
        tmcm_123x_0_1.nmt.state = 'OPERATIONAL'

        tmcm_123x_0_1.go_to_operation_enabled()
        tmcm_123x_0_1.sdo['Absolute Max Current 1'].raw = 20
        tmcm_123x_0_1.sdo['Standby Current 1'].raw = 8
        tmcm_123x_0_1.sdo['Microstep Resolution 1'].raw = 8

        # set up StallGuard2
        print("Configuring StallGuard2 parameters...")
        stallguard2_init(init_velocity = 10000)
        print("Apply load and try to stall the motor...")
        motor_activity_flag_mask = 0x4000
        while tmcm_123x_0_1.sdo['Statusword 1'].raw & motor_activity_flag_mask != 0:
            pass
        print("Motor stopped by StallGuard2!")

        tmcm_123x_0_1.nmt.state = 'PRE-OPERATIONAL'
        tmcm_123x_0_1.shutdown()

if __name__ == "__main__":
        main()