"""
Uses SDO to rotate the motor for 5 seconds in profile velocity mode.
"""
import time
import canopen
from pytrinamic.modules.canopen_node import TmcmNode

with canopen.Network() as network:
    network.connect(channel='PCAN_USBBUS1', bustype='pcan', bitrate=1_000_000)

    tmcm_1231 = TmcmNode(1, 'TMCM-1231.eds')
    network.add_node(tmcm_1231)
    # Profile Velocity Mode
    tmcm_1231.sdo['Modes of Operation 1'].raw = tmcm_1231.ModeOfOperation.PROFILE_VELOCITY_MODE

    tmcm_1231.load_configuration()
    tmcm_1231.nmt.state = 'OPERATIONAL'

    tmcm_1231.go_to_operation_enabled()
    tmcm_1231.sdo['Absolute Max Current 1'].raw = 50
    tmcm_1231.sdo['Stop On Stall 1'].raw = 0


    target_velocity = 10000
    print("Rotating the motor...")
    tmcm_1231.sdo['Target Velocity 1'].raw = target_velocity
    time.sleep(5)
    tmcm_1231.sdo['Target Velocity 1'].raw = 0
    print("Motor stopped!")

    tmcm_1231.nmt.state = 'PRE-OPERATIONAL'
    tmcm_1231.shutdown()



