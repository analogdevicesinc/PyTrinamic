################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import time
import canopen
from pytrinamic.modules.canopen_node import TmcmNode

with canopen.Network() as network:
    # PEAK CAN ADAPER SETTINGS FOR CAN CONNECTION 
    network.connect(bustype='pcan', channel='PCAN_USBBUS1', bitrate=1_000_000) 
    # TMCM-1240 EDS (ELECTRONIC DATASHEET IS CALLED,CANOPEN NODE .PY PYTRINAMIC IS CALLED  )
    tmcm_1240 = TmcmNode(1, 'TMCM-1240.eds') 
  
    network.add_node(tmcm_1240)
    # LOADING CONFIGURATION FROM CANOPEN NODE FILE 
    tmcm_1240.load_configuration()
    
    tmcm_1240.nmt.state = 'OPERATIONAL'
    tmcm_1240.go_to_operation_enabled()
    tmcm_1240.shutdown()
    
    tmcm_1240.sdo['Absolute Max Current 1'].raw = 80 #CURRENT SETTINGS 
    tmcm_1240.sdo['Switch Parameters 1'].raw = 3 #DISSABLE LIMIT SWITCHES 
    tmcm_1240.go_to_operation_enabled()
    # SETTING OPERATIONAL MODE 
    tmcm_1240.sdo['Modes of Operation 1'].raw=3 #PROFILE VELOCITY MODE 

    target_velocity = 50000 #SET TARGET VELOCITY 
    print("Rotating the motor...")
  
    tmcm_1240.sdo['Target Velocity 1'].raw = target_velocity
    time.sleep(10)
  
    tmcm_1240.sdo['Target Velocity 1'].raw = 0
    print("Motor stopped!")
    # SHUTDOWN STATES 
    tmcm_1240.nmt.state = 'PRE-OPERATIONAL'

    tmcm_1240.shutdown()