'''
Created on 24.10.2019

@author: JM
'''

class TMC2041_register:
    """
    Define all registers of the TMC2041.
    """
    GCONF          = 0x00
    GSTAT          = 0x01
    IFCNT          = 0x02
    TEST_SEL       = 0x03
    INPUT          = 0x04
    IHOLD_IRUN_M1  = 0x30
    IHOLD_IRUN_M2  = 0x50
    MSCNT_M1       = 0x6A
    MSCURACT_M1    = 0x6B
    CHOPCONF_M1    = 0x6C
    COOLCONF_M1    = 0x6D
    DRV_STATUS_M1  = 0x6F
    MSCNT_M2       = 0x7A
    MSCURACT_M2    = 0x7B
    CHOPCONF_M2    = 0x7C
    COOLCONF_M2    = 0x7D
    DRV_STATUS_M2  = 0x7F