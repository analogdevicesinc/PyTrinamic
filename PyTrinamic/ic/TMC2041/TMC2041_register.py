'''
Created on 24.10.2019

@author: JM
'''

class TMC2041_register:
    """
    Define all registers of the TMC2041.
    """
    GCONF         = 0x00
    GSTAT         = 0x01
    IFCNT         = 0x02
    TEST_SEL      = 0x03
    INPUT         = 0x04
    IHOLD_IRUN_M1 = 0x30
    MSCNT_M1      = 0x6A
    MSCURACT_M1   = 0x6B
    CHOPCONF_M1   = 0x6C
    COOLCONF_M1   = 0x6D
    DRV_STATUS_M1 = 0x6F
    
    list = [
        GCONF         ,
        GSTAT         ,
        IFCNT         ,
        TEST_SEL      ,
        INPUT         ,
        IHOLD_IRUN_M1 ,
        MSCNT_M1      ,
        MSCURACT_M1   ,
        CHOPCONF_M1   ,
        COOLCONF_M1   ,
        DRV_STATUS_M1 ,
    ]