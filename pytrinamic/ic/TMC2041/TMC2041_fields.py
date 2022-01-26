'''
Created on 24.10.2019

@author: JM
'''

class TMC2041_fields(object):
    """
    Define all register bitfields of the TMC2041.

    Each field is defined as a tuple consisting of ( Address, Mask, Shift ).

    The name of the register is written as a comment behind each tuple. This is
    intended for IDE users viewing the definition of a field by hovering over
    it. This allows the user to see the corresponding register name of a field
    without opening this file and searching for the definition.
    """

    # GCONF
    TEST_MODE   = ( 0x00, 0x00000080,  7 ) # GCONF
    SHAFT1      = ( 0x00, 0x00000100,  8 ) # GCONF
    SHAFT2      = ( 0x00, 0x00000200,  9 ) # GCONF
    LOCK_GCONF  = ( 0x00, 0x00000400, 10 ) # GCONF

    # GSTAT
    RESET       = ( 0x01, 0x00000001,  0 ) # GSTAT
    DRV_ERR1    = ( 0x01, 0x00000002,  1 ) # GSTAT
    DRV_ERR2    = ( 0x01, 0x00000004,  2 ) # GSTAT
    UV_CP       = ( 0x01, 0x00000008,  3 ) # GSTAT

    # IFCNT
    IFCNT       = ( 0x02, 0x000000FF,  0 ) # IFCNT

    # TEST_SEL
    TEST_SEL    = ( 0x03, 0x0000000F,  0 ) # TEST_SEL

    # INPUT
    DRV_ENN     = ( 0x04, 0x00000080,  7 ) # INPUT
    VERSION     = ( 0x04, 0xFF000000, 24 ) # INPUT

    # IHOLD_IRUN_M1
    IHOLD       = ( 0x30, 0x0000001F,  0 ) # IHOLD_IRUN_M1
    IRUN        = ( 0x30, 0x00001F00,  8 ) # IHOLD_IRUN_M1
    IHOLDDELAY  = ( 0x30, 0x000F0000, 16 ) # IHOLD_IRUN_M1

    # IHOLD_IRUN_M2
    IHOLD       = ( 0x50, 0x0000001F,  0 ) # IHOLD_IRUN_M2
    IRUN        = ( 0x50, 0x00001F00,  8 ) # IHOLD_IRUN_M2
    IHOLDDELAY  = ( 0x50, 0x000F0000, 16 ) # IHOLD_IRUN_M2

    # MSCNT_M1
    MSCNT       = ( 0x6A, 0x000003FF,  0 ) # MSCNT_M1

    # MSCURACT_M1
    CUR_A       = ( 0x6B, 0x000001FF,  0 ) # MSCURACT_M1
    CUR_B       = ( 0x6B, 0x01FF0000, 16 ) # MSCURACT_M1

    # CHOPCONF_M1
    TOFF        = ( 0x6C, 0x0000000F,  0 ) # CHOPCONF_M1
    TFD_2__0_   = ( 0x6C, 0x00000070,  4 ) # CHOPCONF_M1
    OFFSET      = ( 0x6C, 0x00000780,  7 ) # CHOPCONF_M1
    TFD__       = ( 0x6C, 0x00000800, 11 ) # CHOPCONF_M1
    DISFDCC     = ( 0x6C, 0x00001000, 12 ) # CHOPCONF_M1
    RNDTF       = ( 0x6C, 0x00002000, 13 ) # CHOPCONF_M1
    CHM         = ( 0x6C, 0x00004000, 14 ) # CHOPCONF_M1
    TBL         = ( 0x6C, 0x00018000, 15 ) # CHOPCONF_M1
    VSENSE      = ( 0x6C, 0x00020000, 17 ) # CHOPCONF_M1
    VHIGHFS     = ( 0x6C, 0x00040000, 18 ) # CHOPCONF_M1
    VHIGHCHM    = ( 0x6C, 0x00080000, 19 ) # CHOPCONF_M1
    SYNC        = ( 0x6C, 0x00F00000, 20 ) # CHOPCONF_M1
    MRES        = ( 0x6C, 0x0F000000, 24 ) # CHOPCONF_M1
    INTPOL16    = ( 0x6C, 0x10000000, 28 ) # CHOPCONF_M1
    DEDGE       = ( 0x6C, 0x20000000, 29 ) # CHOPCONF_M1
    DISS2G      = ( 0x6C, 0x40000000, 30 ) # CHOPCONF_M1
    TOFF        = ( 0x6C, 0x0000000F,  0 ) # CHOPCONF_M1
    TFD_2__0_   = ( 0x6C, 0x00000070,  4 ) # CHOPCONF_M1
    OFFSET      = ( 0x6C, 0x00000780,  7 ) # CHOPCONF_M1
    TFD__       = ( 0x6C, 0x00000800, 11 ) # CHOPCONF_M1
    DISFDCC     = ( 0x6C, 0x00001000, 12 ) # CHOPCONF_M1
    RNDTF       = ( 0x6C, 0x00002000, 13 ) # CHOPCONF_M1
    CHM         = ( 0x6C, 0x00004000, 14 ) # CHOPCONF_M1
    TBL         = ( 0x6C, 0x00018000, 15 ) # CHOPCONF_M1
    VSENSE      = ( 0x6C, 0x00020000, 17 ) # CHOPCONF_M1
    VHIGHFS     = ( 0x6C, 0x00040000, 18 ) # CHOPCONF_M1
    VHIGHCHM    = ( 0x6C, 0x00080000, 19 ) # CHOPCONF_M1
    SYNC        = ( 0x6C, 0x00F00000, 20 ) # CHOPCONF_M1
    MRES        = ( 0x6C, 0x0F000000, 24 ) # CHOPCONF_M1
    INTPOL16    = ( 0x6C, 0x10000000, 28 ) # CHOPCONF_M1
    DEDGE       = ( 0x6C, 0x20000000, 29 ) # CHOPCONF_M1
    DISS2G      = ( 0x6C, 0x40000000, 30 ) # CHOPCONF_M1
    TOFF        = ( 0x6C, 0x0000000F,  0 ) # CHOPCONF_M1
    HSTRT       = ( 0x6C, 0x00000070,  4 ) # CHOPCONF_M1
    HEND        = ( 0x6C, 0x00000780,  7 ) # CHOPCONF_M1
    RNDTF       = ( 0x6C, 0x00002000, 13 ) # CHOPCONF_M1
    CHM         = ( 0x6C, 0x00004000, 14 ) # CHOPCONF_M1
    TBL         = ( 0x6C, 0x00018000, 15 ) # CHOPCONF_M1
    VSENSE      = ( 0x6C, 0x00020000, 17 ) # CHOPCONF_M1
    VHIGHFS     = ( 0x6C, 0x00040000, 18 ) # CHOPCONF_M1
    VHIGHCHM    = ( 0x6C, 0x00080000, 19 ) # CHOPCONF_M1
    SYNC        = ( 0x6C, 0x00F00000, 20 ) # CHOPCONF_M1
    MRES        = ( 0x6C, 0x0F000000, 24 ) # CHOPCONF_M1
    INTPOL16    = ( 0x6C, 0x10000000, 28 ) # CHOPCONF_M1
    DEDGE       = ( 0x6C, 0x20000000, 29 ) # CHOPCONF_M1
    DISS2G      = ( 0x6C, 0x40000000, 30 ) # CHOPCONF_M1

    # COOLCONF_M1
    SEMIN       = ( 0x6D, 0x0000000F,  0 ) # COOLCONF_M1
    SEUP        = ( 0x6D, 0x00000060,  5 ) # COOLCONF_M1
    SEMAX       = ( 0x6D, 0x00000F00,  8 ) # COOLCONF_M1
    SEDN        = ( 0x6D, 0x00006000, 13 ) # COOLCONF_M1
    SEIMIN      = ( 0x6D, 0x00008000, 15 ) # COOLCONF_M1
    SGT         = ( 0x6D, 0x007F0000, 16 ) # COOLCONF_M1
    SFILT       = ( 0x6D, 0x01000000, 24 ) # COOLCONF_M1

    # DRV_STATUS_M1
    SG_RESULT   = ( 0x6F, 0x000003FF,  0 ) # DRV_STATUS_M1
    FSACTIVE    = ( 0x6F, 0x00008000, 15 ) # DRV_STATUS_M1
    CS_ACTUAL   = ( 0x6F, 0x001F0000, 16 ) # DRV_STATUS_M1
    STALLGUARD  = ( 0x6F, 0x01000000, 24 ) # DRV_STATUS_M1
    OT          = ( 0x6F, 0x02000000, 25 ) # DRV_STATUS_M1
    OTPW        = ( 0x6F, 0x04000000, 26 ) # DRV_STATUS_M1
    S2GA        = ( 0x6F, 0x08000000, 27 ) # DRV_STATUS_M1
    S2GB        = ( 0x6F, 0x10000000, 28 ) # DRV_STATUS_M1
    OLA         = ( 0x6F, 0x20000000, 29 ) # DRV_STATUS_M1
    OLB         = ( 0x6F, 0x40000000, 30 ) # DRV_STATUS_M1
    STST        = ( 0x6F, 0x80000000, 31 ) # DRV_STATUS_M1

    # MSCNT_M2
    MSCNT       = ( 0x7A, 0x000003FF,  0 ) # MSCNT_M2

    # MSCURACT_M2
    CUR_A       = ( 0x7B, 0x000001FF,  0 ) # MSCURACT_M2
    CUR_B       = ( 0x7B, 0x01FF0000, 16 ) # MSCURACT_M2

    # CHOPCONF_M2
    TOFF        = ( 0x7C, 0x0000000F,  0 ) # CHOPCONF_M2
    TFD_2__0_   = ( 0x7C, 0x00000070,  4 ) # CHOPCONF_M2
    OFFSET      = ( 0x7C, 0x00000780,  7 ) # CHOPCONF_M2
    TFD__       = ( 0x7C, 0x00000800, 11 ) # CHOPCONF_M2
    DISFDCC     = ( 0x7C, 0x00001000, 12 ) # CHOPCONF_M2
    RNDTF       = ( 0x7C, 0x00002000, 13 ) # CHOPCONF_M2
    CHM         = ( 0x7C, 0x00004000, 14 ) # CHOPCONF_M2
    TBL         = ( 0x7C, 0x00018000, 15 ) # CHOPCONF_M2
    VSENSE      = ( 0x7C, 0x00020000, 17 ) # CHOPCONF_M2
    VHIGHFS     = ( 0x7C, 0x00040000, 18 ) # CHOPCONF_M2
    VHIGHCHM    = ( 0x7C, 0x00080000, 19 ) # CHOPCONF_M2
    SYNC        = ( 0x7C, 0x00F00000, 20 ) # CHOPCONF_M2
    DISS2G      = ( 0x7C, 0x40000000, 30 ) # CHOPCONF_M2
    TOFF        = ( 0x7C, 0x0000000F,  0 ) # CHOPCONF_M2
    TFD_2__0_   = ( 0x7C, 0x00000070,  4 ) # CHOPCONF_M2
    OFFSET      = ( 0x7C, 0x00000780,  7 ) # CHOPCONF_M2
    TFD__       = ( 0x7C, 0x00000800, 11 ) # CHOPCONF_M2
    DISFDCC     = ( 0x7C, 0x00001000, 12 ) # CHOPCONF_M2
    RNDTF       = ( 0x7C, 0x00002000, 13 ) # CHOPCONF_M2
    CHM         = ( 0x7C, 0x00004000, 14 ) # CHOPCONF_M2
    TBL         = ( 0x7C, 0x00018000, 15 ) # CHOPCONF_M2
    VSENSE      = ( 0x7C, 0x00020000, 17 ) # CHOPCONF_M2
    VHIGHFS     = ( 0x7C, 0x00040000, 18 ) # CHOPCONF_M2
    VHIGHCHM    = ( 0x7C, 0x00080000, 19 ) # CHOPCONF_M2
    SYNC        = ( 0x7C, 0x00F00000, 20 ) # CHOPCONF_M2
    DISS2G      = ( 0x7C, 0x40000000, 30 ) # CHOPCONF_M2
    TOFF        = ( 0x7C, 0x0000000F,  0 ) # CHOPCONF_M2
    HSTRT       = ( 0x7C, 0x00000070,  4 ) # CHOPCONF_M2
    HEND        = ( 0x7C, 0x00000780,  7 ) # CHOPCONF_M2
    RNDTF       = ( 0x7C, 0x00002000, 13 ) # CHOPCONF_M2
    CHM         = ( 0x7C, 0x00004000, 14 ) # CHOPCONF_M2
    TBL         = ( 0x7C, 0x00018000, 15 ) # CHOPCONF_M2
    VSENSE      = ( 0x7C, 0x00020000, 17 ) # CHOPCONF_M2
    VHIGHFS     = ( 0x7C, 0x00040000, 18 ) # CHOPCONF_M2
    VHIGHCHM    = ( 0x7C, 0x00080000, 19 ) # CHOPCONF_M2
    SYNC        = ( 0x7C, 0x00F00000, 20 ) # CHOPCONF_M2
    DISS2G      = ( 0x7C, 0x40000000, 30 ) # CHOPCONF_M2

    # COOLCONF_M2
    SEMIN       = ( 0x7D, 0x0000000F,  0 ) # COOLCONF_M2
    SEUP        = ( 0x7D, 0x00000060,  5 ) # COOLCONF_M2
    SEMAX       = ( 0x7D, 0x00000F00,  8 ) # COOLCONF_M2
    SEDN        = ( 0x7D, 0x00006000, 13 ) # COOLCONF_M2
    SEIMIN      = ( 0x7D, 0x00008000, 15 ) # COOLCONF_M2
    SGT         = ( 0x7D, 0x007F0000, 16 ) # COOLCONF_M2
    SFILT       = ( 0x7D, 0x01000000, 24 ) # COOLCONF_M2

    # DRV_STATUS_M2
    SG_RESULT   = ( 0x7F, 0x000003FF,  0 ) # DRV_STATUS_M2
    FSACTIVE    = ( 0x7F, 0x00008000, 15 ) # DRV_STATUS_M2
    CS_ACTUAL   = ( 0x7F, 0x001F0000, 16 ) # DRV_STATUS_M2
    STALLGUARD  = ( 0x7F, 0x01000000, 24 ) # DRV_STATUS_M2
    OT          = ( 0x7F, 0x02000000, 25 ) # DRV_STATUS_M2
    OTPW        = ( 0x7F, 0x04000000, 26 ) # DRV_STATUS_M2
    S2GA        = ( 0x7F, 0x08000000, 27 ) # DRV_STATUS_M2
    S2GB        = ( 0x7F, 0x10000000, 28 ) # DRV_STATUS_M2
    OLA         = ( 0x7F, 0x20000000, 29 ) # DRV_STATUS_M2
    OLB         = ( 0x7F, 0x40000000, 30 ) # DRV_STATUS_M2
    STST        = ( 0x7F, 0x80000000, 31 ) # DRV_STATUS_M2
