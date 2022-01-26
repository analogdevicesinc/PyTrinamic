'''
Created on 27.03.2020

@author: JM
'''

class TMC2300_fields(object):
    """
    Define all register bitfields of the TMC2300.

    Each field is defined as a tuple consisting of ( Address, Mask, Shift ).

    The name of the register is written as a comment behind each tuple. This is
    intended for IDE users viewing the definition of a field by hovering over
    it. This allows the user to see the corresponding register name of a field
    without opening this file and searching for the definition.
    """

    # GCONF
    SET_TO_0           = ( 0x00, 0x00000001,  0 ) # GCONF
    EXTCAP             = ( 0x00, 0x00000002,  1 ) # GCONF
    SHAFT              = ( 0x00, 0x00000008,  3 ) # GCONF
    DIAG_INDEX         = ( 0x00, 0x00000010,  4 ) # GCONF
    DIAG_STEP          = ( 0x00, 0x00000020,  5 ) # GCONF
    MULTISTEP_FILT     = ( 0x00, 0x00000040,  6 ) # GCONF
    TEST_MODE          = ( 0x00, 0x00000080,  7 ) # GCONF

    # GSTAT
    RESET              = ( 0x01, 0x00000001,  0 ) # GSTAT
    DRV_ERR            = ( 0x01, 0x00000002,  1 ) # GSTAT
    U3V5               = ( 0x01, 0x00000004,  2 ) # GSTAT

    # IFCNT
    IFCNT              = ( 0x02, 0x000000FF,  0 ) # IFCNT

    # SLAVECONF
    SLAVECONF          = ( 0x03, 0x00000F00,  8 ) # SLAVECONF

    # IOIN
    EN                 = ( 0x06, 0x00000001,  0 ) # IOIN
    NSTDBY             = ( 0x06, 0x00000002,  1 ) # IOIN
    MS1                = ( 0x06, 0x00000004,  2 ) # IOIN
    MS2                = ( 0x06, 0x00000008,  3 ) # IOIN
    DIAG               = ( 0x06, 0x00000010,  4 ) # IOIN
    STEPPER_CLK_INPUT  = ( 0x06, 0x00000020,  5 ) # IOIN
    PDN_UART           = ( 0x06, 0x00000040,  6 ) # IOIN
    MODE_INPUT         = ( 0x06, 0x00000080,  7 ) # IOIN
    STEP               = ( 0x06, 0x00000100,  8 ) # IOIN
    DIR                = ( 0x06, 0x00000200,  9 ) # IOIN
    COMP_A1A2          = ( 0x06, 0x00000400, 10 ) # IOIN
    COMP_B1B2          = ( 0x06, 0x00000800, 11 ) # IOIN
    VERSION            = ( 0x06, 0xFF000000, 24 ) # IOIN

    # IHOLD_IRUN
    IHOLD              = ( 0x10, 0x0000001F,  0 ) # IHOLD_IRUN
    IRUN               = ( 0x10, 0x00001F00,  8 ) # IHOLD_IRUN
    IHOLDDELAY         = ( 0x10, 0x000F0000, 16 ) # IHOLD_IRUN

    # TPOWERDOWN
    TPOWERDOWN         = ( 0x11, 0x000000FF,  0 ) # TPOWERDOWN

    # TSTEP
    TSTEP              = ( 0x12, 0x000FFFFF,  0 ) # TSTEP

    # TCOOLTHRS
    TCOOLTHRS          = ( 0x14, 0xFFFFFFFF,  0 ) # TCOOLTHRS

    # VACTUAL
    VACTUAL            = ( 0x22, 0x00FFFFFF,  0 ) # VACTUAL

    # SGTHRS
    SGTHRS             = ( 0x40, 0x000000FF,  0 ) # SGTHRS

    # SG_VALUE
    SG_VALUE           = ( 0x41, 0x000003FF,  0 ) # SG_VALUE

    # COOLCONF
    SEMIN              = ( 0x42, 0x0000000F,  0 ) # COOLCONF
    SEUP               = ( 0x42, 0x00000060,  5 ) # COOLCONF
    SEMAX              = ( 0x42, 0x00000F00,  8 ) # COOLCONF
    SEDN               = ( 0x42, 0x00006000, 13 ) # COOLCONF
    SEIMIN             = ( 0x42, 0x00008000, 15 ) # COOLCONF

    # MSCNT
    MSCNT              = ( 0x6A, 0x000003FF,  0 ) # MSCNT

    # MSCURACT
    CUR_A              = ( 0x6B, 0x000001FF,  0 ) # MSCURACT
    CUR_B              = ( 0x6B, 0x01FF0000, 16 ) # MSCURACT

    # CHOPCONF
    ENABLEDRV          = ( 0x6C, 0x00000001,  0 ) # CHOPCONF
    TBL                = ( 0x6C, 0x00018000, 15 ) # CHOPCONF
    MRES               = ( 0x6C, 0x0F000000, 24 ) # CHOPCONF
    INTPOL             = ( 0x6C, 0x10000000, 28 ) # CHOPCONF
    DEDGE              = ( 0x6C, 0x20000000, 29 ) # CHOPCONF
    DISS2G             = ( 0x6C, 0x40000000, 30 ) # CHOPCONF
    DISS2VS            = ( 0x6C, 0x80000000, 31 ) # CHOPCONF

    # DRV_STATUS
    OTPW               = ( 0x6F, 0x00000001,  0 ) # DRV_STATUS
    OT                 = ( 0x6F, 0x00000002,  1 ) # DRV_STATUS
    S2GA               = ( 0x6F, 0x00000004,  2 ) # DRV_STATUS
    S2GB               = ( 0x6F, 0x00000008,  3 ) # DRV_STATUS
    S2VSA              = ( 0x6F, 0x00000010,  4 ) # DRV_STATUS
    S2VSB              = ( 0x6F, 0x00000020,  5 ) # DRV_STATUS
    OLA                = ( 0x6F, 0x00000040,  6 ) # DRV_STATUS
    OLB                = ( 0x6F, 0x00000080,  7 ) # DRV_STATUS
    T120               = ( 0x6F, 0x00000100,  8 ) # DRV_STATUS
    T150               = ( 0x6F, 0x00000200,  9 ) # DRV_STATUS
    CS_ACTUAL          = ( 0x6F, 0x001F0000, 16 ) # DRV_STATUS
    STST               = ( 0x6F, 0x80000000, 31 ) # DRV_STATUS

    # PWMCONF
    PWM_OFS            = ( 0x70, 0x000000FF,  0 ) # PWMCONF
    PWM_GRAD           = ( 0x70, 0x0000FF00,  8 ) # PWMCONF
    PWM_FREQ           = ( 0x70, 0x00030000, 16 ) # PWMCONF
    PWM_AUTOSCALE      = ( 0x70, 0x00040000, 18 ) # PWMCONF
    PWM_AUTOGRAD       = ( 0x70, 0x00080000, 19 ) # PWMCONF
    FREEWHEEL          = ( 0x70, 0x00300000, 20 ) # PWMCONF
    PWM_REG            = ( 0x70, 0x0F000000, 24 ) # PWMCONF
    PWM_LIM            = ( 0x70, 0xF0000000, 28 ) # PWMCONF

    # PWM_SCALE
    PWM_SCALE_SUM      = ( 0x71, 0x000000FF,  0 ) # PWM_SCALE
    PWM_SCALE_AUTO     = ( 0x71, 0xFFFF0000, 16 ) # PWM_SCALE

    # PWM_AUTO
    PWM_OFS_AUTO       = ( 0x72, 0x000000FF,  0 ) # PWM_AUTO
    PWM_GRAD_AUTO      = ( 0x72, 0x00FF0000, 16 ) # PWM_AUTO
