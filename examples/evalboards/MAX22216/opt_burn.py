################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to OTP a value of 0xFF for register 0x40

Note: Supply voltage VM has to be set to 8.7V +-0.1VDC

            +------------------------+                 +-------------------+                   
            |     Landungsbrücke     |                 |     MAX22216      |                   
            |                        |                 |                   |                   
            |                       1|-----------------|15,20,21,26 VM     |                   
            |                       2|-----------------|5  GND             |                   
            |                       8|-----------------|27 ENABLE          |                   
            |                      12|-----------------|11 CRC_EN          |                   
            |                      15|-----------------|32 VCC_IO          |                   
            |                      24|-----------------|29 SPI_CS          |                   
            |                      27|-----------------|28 SPI_SCK         |                   
            |                      28|-----------------|31 MISO            |                   
            |                      29|-----------------|30 MOSI            |                   
            |                        |                 |                   |                   
            |                        |                 |                   |                   
USB --------|                        |                 |                   |                   
            +------------------------+                 +-------------------+                                                                                                     
"""

import time
from pytrinamic.connections import ConnectionManager


with ConnectionManager().connect() as my_interface:
    # enable Landungsbrücke to use MAX22216         
    my_interface.send(143, 3, 0, 0x021E0000)
    my_interface.send(143, 4, 0, 0x021E0000)
    
    # switch OFF DIO4 - CRC_EN
    my_interface.send(9, 6, 7, 1)  
    # switch ON DIO0 - ENABLE signal 
    my_interface.send(9, 6, 3, 1) 
      
    # read voltage from EVAL board
    # Pin 1 on connector J301 (44 pin connector)used for VM input
    #  voltage devider with 100k to 4k7 (~70VDC possible)
    tmp = str(my_interface.send(15, 5, 0, 0))
    tmp = tmp.split(',')
    VM = int(tmp[4], 16)/10
    print("Suppl:y " + str(VM) +" V")
    
    # check if voltage is in expected range of 8.7 +-0.1VDC
    if (VM >= 8.6) and (VM <= 8.8):  
        print(my_interface.send(172, 0, 1, 0) )    # TMCLOTP.init
        print(my_interface.send(172, 1, 1, 0x40))  # TMCLOTP.address
        print(my_interface.send(172, 2, 1, 0xFF))  # TMCLOTP.value
        print(my_interface.send(172, 3, 1, 0))     # TMCLOTP.program     
        #print(my_interface.send(172, 4, 1, 0))     # TMCLOTP.lock, use only when OTP shall be locked
        time.sleep(0.5) #wait until writing is completed
        tmp = str(my_interface.send(172, 5, 1, 0))     # TMCLOTP.status, writing completed when 0x02 is returned 
        print(tmp)
        tmp = tmp.split(',')
        if int(tmp[4]) == 2:
            print("OTP performed successfully")
        else:
            print("OTP not performed due to timeout or device is locked")
    else:
        print("please set VM to 8.7VDC +- 0.1")  
    
    # DISABLE device by setting ENABLE low
    my_interface.send(9, 6, 3, 0)
    # close USB TMCL interface