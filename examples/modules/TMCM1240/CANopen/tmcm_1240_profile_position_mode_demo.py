################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
import time
import canopen
from pytrinamic.modules.canopen_node import TmcmNode

with canopen.Network() as network:
    # PEAK CAN ADAPER SETTINGS 
    network.connect(bustype='pcan', channel='PCAN_USBBUS1', bitrate=1_000_000)
   
    tmcm_1240 = TmcmNode(1, 'TMCM-1240.eds')# TMCM-1240 EDS (ELECTRONIC DATASHEET IS CALLED,CANOPEN NODE .PY FROM PYTRINAMIC IS CALLED  )
  
    network.add_node(tmcm_1240)

    # LOADING CONFIGURATION FOR CANOPEN NODE FILE 
    tmcm_1240.load_configuration()
    tmcm_1240.nmt.state = 'OPERATIONAL'
    tmcm_1240.go_to_operation_enabled()
    tmcm_1240.shutdown()
    tmcm_1240.sdo['Absolute Max Current 1'].raw = 80# CURRENT SETTINGS 
    tmcm_1240.sdo['Switch Parameters 1'].raw = 3# DISSABLE LIMIT SWITCHES
    tmcm_1240.sdo['Controlword 1'].raw= 6 # State transition to Shut Down
    tmcm_1240.sdo['Controlword 1'].raw= 7 # State transition to Switched On
    tmcm_1240.go_to_operation_enabled()
    # Six Point Ramp Parameters    
    tmcm_1240.sdo['Profile start velocity 1'].raw = 5000  # VSTRAT          
    tmcm_1240.sdo['Profile A1 1'].raw = 1000       # A1     
    tmcm_1240.sdo['Profile V1 1'].raw = 50000       # V1       
    tmcm_1240.sdo['Profile Velocity in pp-mode 1'].raw = 200000 #VMAX
    tmcm_1240.sdo['Profile Acceleration 1'].raw = 500   # AMAX 
    tmcm_1240.sdo['Profile Deceleration 1'].raw = 700 # DMAX                    
    tmcm_1240.sdo['Profile D1 1'].raw = 1400 #D1
    tmcm_1240.sdo['End velocity 1'].raw = 10 #VSTOP
    tmcm_1240.sdo['Ramp Wait Time 1'].raw = 255                
    tmcm_1240.go_to_operation_enabled()
    # PROFILE POSTION MODE
    
    tmcm_1240.sdo['Modes of Operation 1'].raw=1
    tmcm_1240.sdo['Target Position 1'].raw = 200000 # TARGET VELOCITY 
    tmcm_1240.sdo['Controlword 1'].raw = 31 
    print("Motor starts rotating ") 
    time.sleep(50)
    print(tmcm_1240.get_state())
    print("Motor Stoped ") 
    tmcm_1240.shutdown() # SWITCH ON DISSABLE 
    print(tmcm_1240.get_state())
