class TMC5062_fields(object):
    """
    Define all register bitfields of the TMC5062.

    Each field is defined as a tuple consisting of ( Address, Mask, Shift ).
    Fields that are present multiple times in different registers (for multiple
    motors) all of the bitfield tuples are bundled together into another tuple.

    The name of the register is written as a comment behind each tuple. This is
    intended for IDE users viewing the definition of a field by hovering over
    it. This allows the user to see the corresponding register name of a field
    without opening this file and searching for the definition.
    """

    # GCONF
    POSCMP_ENABLE      = (0x00, 0x00000008,  3)  # GCONF
    ENC1_REFSEL        = (0x00, 0x00000010,  4)  # GCONF
    ENC2_ENABLE        = (0x00, 0x00000020,  5)  # GCONF
    ENC2_REFSEL        = (0x00, 0x00000040,  6)  # GCONF
    TEST_MODE          = (0x00, 0x00000080,  7)  # GCONF
    SHAFT1             = (0x00, 0x00000100,  8)  # GCONF
    SHAFT2             = (0x00, 0x00000200,  9)  # GCONF
    LOCK_GCONF         = (0x00, 0x00000400, 10)  # GCONF

    # GSTAT
    RESET              = (0x01, 0x00000001,  0)  # GSTAT
    DRV_ERR1           = (0x01, 0x00000002,  1)  # GSTAT
    DRV_ERR2           = (0x01, 0x00000004,  2)  # GSTAT
    UV_CP              = (0x01, 0x00000008,  3)  # GSTAT

    # SLAVECONF
    TEST_SEL           = (0x03, 0x0000000F,  0)  # SLAVECONF
    SENDDELAY          = (0x03, 0x000000F0,  4)  # SLAVECONF

    # INPUT / OUTPUT
    IO0_IN             = (0x04, 0x00000001,  0)  # INPUT / OUTPUT
    IO1_IN             = (0x04, 0x00000002,  1)  # INPUT / OUTPUT
    IO2_IN             = (0x04, 0x00000004,  2)  # INPUT / OUTPUT
    IO3_IN             = (0x04, 0x00000008,  3)  # INPUT / OUTPUT
    IOP_IN             = (0x04, 0x00000010,  4)  # INPUT / OUTPUT
    ION_IN             = (0x04, 0x00000020,  5)  # INPUT / OUTPUT
    DRV_ENN            = (0x04, 0x00000080,  7)  # INPUT / OUTPUT
    VERSION            = (0x04, 0xFF000000, 24)  # INPUT / OUTPUT
    IO0_OUT            = (0x04, 0x00000001,  0)  # INPUT / OUTPUT
    IO1_OUT            = (0x04, 0x00000002,  1)  # INPUT / OUTPUT
    IO2_OUT            = (0x04, 0x00000004,  2)  # INPUT / OUTPUT
    IO3_OUT            = (0x04, 0x00000008,  3)  # INPUT / OUTPUT
    IODDR0             = (0x04, 0x00000100,  8)  # INPUT / OUTPUT
    IODDR1             = (0x04, 0x00000200,  9)  # INPUT / OUTPUT
    IODDR2             = (0x04, 0x00000400, 10)  # INPUT / OUTPUT
    IODDR3             = (0x04, 0x00000800, 11)  # INPUT / OUTPUT

    # X_COMPARE
    X_COMPARE          = (0x05, 0xFFFFFFFF,  0)  # X_COMPARE


class TMC5062_fields_m1(object):

    # RAMPMODE_M1
    RAMPMODE           = (0x20, 0x00000003,  0)  # RAMPMODE_M1

    # XACTUAL_M1
    XACTUAL            = (0x21, 0xFFFFFFFF,  0)  # XACTUAL_M1

    # VACTUAL_M1
    VACTUAL            = (0x22, 0x00FFFFFF,  0)  # VACTUAL_M1

    # VSTART_M1
    VSTART             = (0x23, 0x0003FFFF,  0)  # VSTART_M1

    # A1_M1
    A1                 = (0x24, 0x0000FFFF,  0)  # A1_M1

    # V1_M1
    V1                 = (0x25, 0x000FFFFF,  0)  # V1_M1

    # AMAX_M1
    AMAX               = (0x26, 0x0000FFFF,  0)  # AMAX_M1

    # VMAX_M1
    VMAX               = (0x27, 0x007FFFFF,  0)  # VMAX_M1

    # DMAX_M1
    DMAX               = (0x28, 0x0000FFFF,  0)  # DMAX_M1

    # D1_M1
    D1                 = (0x2A, 0x0000FFFF,  0)  # D1_M1

    # VSTOP_M1
    VSTOP              = (0x2B, 0x0003FFFF,  0)  # VSTOP_M1

    # TZEROWAIT_M1
    TZEROWAIT          = (0x2C, 0x0000FFFF,  0)  # TZEROWAIT_M1

    # XTARGET_M1
    XTARGET            = (0x2D, 0xFFFFFFFF,  0)  # XTARGET_M1

    # IHOLD_IRUN_M1
    IHOLD              = (0x30, 0x0000001F,  0)  # IHOLD_IRUN_M1
    IRUN               = (0x30, 0x00001F00,  8)  # IHOLD_IRUN_M1
    IHOLDDELAY         = (0x30, 0x000F0000, 16)  # IHOLD_IRUN_M1

    # VCOOLTHRS_M1
    VCOOLTHRS          = (0x31, 0x007FFFFF,  0)  # VCOOLTHRS_M1

    # VHIGH_M1
    VHIGH              = (0x32, 0x007FFFFF,  0)  # VHIGH_M1

    # VDCMIN_M1
    VDCMIN             = (0x33, 0x007FFFFF,  0)  # VDCMIN_M1

    # SW_MODE_M1
    STOP_L_ENABLE      = (0x34, 0x00000001,  0)  # SW_MODE_M1
    STOP_R_ENABLE      = (0x34, 0x00000002,  1)  # SW_MODE_M1
    POL_STOP_L         = (0x34, 0x00000004,  2)  # SW_MODE_M1
    POL_STOP_R         = (0x34, 0x00000008,  3)  # SW_MODE_M1
    SWAP_LR            = (0x34, 0x00000010,  4)  # SW_MODE_M1
    LATCH_L_ACTIVE     = (0x34, 0x00000020,  5)  # SW_MODE_M1
    LATCH_L_INACTIVE   = (0x34, 0x00000040,  6)  # SW_MODE_M1
    LATCH_R_ACTIVE     = (0x34, 0x00000080,  7)  # SW_MODE_M1
    LATCH_R_INACTIVE   = (0x34, 0x00000100,  8)  # SW_MODE_M1
    EN_LATCH_ENCODER   = (0x34, 0x00000200,  9)  # SW_MODE_M1
    SG_STOP            = (0x34, 0x00000400, 10)  # SW_MODE_M1
    EN_SOFTSTOP        = (0x34, 0x00000800, 11)  # SW_MODE_M1

    # RAMP_STAT_M1
    STATUS_STOP_L      = (0x35, 0x00000001,  0)  # RAMP_STAT_M1
    STATUS_STOP_R      = (0x35, 0x00000002,  1)  # RAMP_STAT_M1
    STATUS_LATCH_L     = (0x35, 0x00000004,  2)  # RAMP_STAT_M1
    STATUS_LATCH_R     = (0x35, 0x00000008,  3)  # RAMP_STAT_M1
    EVENT_STOP_L       = (0x35, 0x00000010,  4)  # RAMP_STAT_M1
    EVENT_STOP_R       = (0x35, 0x00000020,  5)  # RAMP_STAT_M1
    EVENT_STOP_SG      = (0x35, 0x00000040,  6)  # RAMP_STAT_M1
    EVENT_POS_REACHED  = (0x35, 0x00000080,  7)  # RAMP_STAT_M1
    VELOCITY_REACHED   = (0x35, 0x00000100,  8)  # RAMP_STAT_M1
    POSITION_REACHED   = (0x35, 0x00000200,  9)  # RAMP_STAT_M1
    VZERO              = (0x35, 0x00000400, 10)  # RAMP_STAT_M1
    T_ZEROWAIT_ACTIVE  = (0x35, 0x00000800, 11)  # RAMP_STAT_M1
    SECOND_MOVE        = (0x35, 0x00001000, 12)  # RAMP_STAT_M1
    STATUS_SG          = (0x35, 0x00002000, 13)  # RAMP_STAT_M1

    # XLATCH_M1
    XLATCH             = (0x36, 0xFFFFFFFF,  0)  # XLATCH_M1

    # ENCMODE_M1
    POL_A              = (0x38, 0x00000001,  0)  # ENCMODE_M1
    POL_B              = (0x38, 0x00000002,  1)  # ENCMODE_M1
    POL_N              = (0x38, 0x00000004,  2)  # ENCMODE_M1
    IGNORE_AB          = (0x38, 0x00000008,  3)  # ENCMODE_M1
    CLR_CONT           = (0x38, 0x00000010,  4)  # ENCMODE_M1
    CLR_ONCE           = (0x38, 0x00000020,  5)  # ENCMODE_M1
    POS_EDGE_NEG_EDGE  = (0x38, 0x000000C0,  6)  # ENCMODE_M1
    CLR_ENC_X          = (0x38, 0x00000100,  8)  # ENCMODE_M1
    LATCH_X_ACT        = (0x38, 0x00000200,  9)  # ENCMODE_M1
    ENC_SEL_DECIMAL    = (0x38, 0x00000400, 10)  # ENCMODE_M1

    # X_ENC_M1
    X_ENC              = (0x39, 0xFFFFFFFF,  0)  # X_ENC_M1

    # ENC_CONST_M1
    INTEGER            = (0x3A, 0xFFFF0000, 16)  # ENC_CONST_M1
    FRACTIONAL         = (0x3A, 0x0000FFFF,  0)  # ENC_CONST_M1

    # ENC_STATUS_M1
    ENC_STATUS         = (0x3B, 0x00000001,  0)  # ENC_STATUS_M1

    # ENC_LATCH_M1
    ENC_LATCH          = (0x3C, 0xFFFFFFFF,  0)  # ENC_LATCH_M1

    # MSLUTSEL_M1
    W0                 = (0x68, 0x00000003,  0)  # MSLUTSEL_M1
    W1                 = (0x68, 0x0000000C,  2)  # MSLUTSEL_M1
    W2                 = (0x68, 0x00000030,  4)  # MSLUTSEL_M1
    W3                 = (0x68, 0x000000C0,  6)  # MSLUTSEL_M1
    X1                 = (0x68, 0x0000FF00,  8)  # MSLUTSEL_M1
    X2                 = (0x68, 0x00FF0000, 16)  # MSLUTSEL_M1
    X3                 = (0x68, 0xFF000000, 24)  # MSLUTSEL_M1

    # MSLUTSTART_M1
    START_SIN          = (0x69, 0x000000FF,  0)  # MSLUTSTART_M1
    START_SIN90        = (0x69, 0x00FF0000, 16)  # MSLUTSTART_M1

    # MSCNT_M1
    MSCNT              = (0x6A, 0x000003FF,  0)  # MSCNT_M1

    # MSCURACT_M1
    CUR_A              = (0x6B, 0x000001FF,  0)  # MSCURACT_M1
    CUR_B              = (0x6B, 0x01FF0000, 16)  # MSCURACT_M1

    # CHOPCONF_M1
    TOFF               = (0x6C, 0x0000000F,  0)  # CHOPCONF_M1
    TFD_2__0_          = (0x6C, 0x00000070,  4)  # CHOPCONF_M1
    OFFSET             = (0x6C, 0x00000780,  7)  # CHOPCONF_M1
    TFD__              = (0x6C, 0x00000800, 11)  # CHOPCONF_M1
    DISFDCC            = (0x6C, 0x00001000, 12)  # CHOPCONF_M1
    RNDTF              = (0x6C, 0x00002000, 13)  # CHOPCONF_M1
    CHM                = (0x6C, 0x00004000, 14)  # CHOPCONF_M1
    TBL                = (0x6C, 0x00018000, 15)  # CHOPCONF_M1
    VSENSE             = (0x6C, 0x00020000, 17)  # CHOPCONF_M1
    VHIGHFS            = (0x6C, 0x00040000, 18)  # CHOPCONF_M1
    VHIGHCHM           = (0x6C, 0x00080000, 19)  # CHOPCONF_M1
    SYNC               = (0x6C, 0x00F00000, 20)  # CHOPCONF_M1
    DISS2G             = (0x6C, 0x40000000, 30)  # CHOPCONF_M1

    # COOLCONF_M1
    SEMIN              = (0x6D, 0x0000000F,  0)  # COOLCONF_M1
    SEUP               = (0x6D, 0x00000060,  5)  # COOLCONF_M1
    SEMAX              = (0x6D, 0x00000F00,  8)  # COOLCONF_M1
    SEDN               = (0x6D, 0x00006000, 13)  # COOLCONF_M1
    SEIMIN             = (0x6D, 0x00008000, 15)  # COOLCONF_M1
    SGT                = (0x6D, 0x007F0000, 16)  # COOLCONF_M1
    SFILT              = (0x6D, 0x01000000, 24)  # COOLCONF_M1

    # DRV_STATUS_M1
    SG_RESULT          = (0x6F, 0x000003FF,  0)  # DRV_STATUS_M1
    FSACTIVE           = (0x6F, 0x00008000, 15)  # DRV_STATUS_M1
    CS_ACTUAL          = (0x6F, 0x001F0000, 16)  # DRV_STATUS_M1
    STALLGUARD         = (0x6F, 0x01000000, 24)  # DRV_STATUS_M1
    OT                 = (0x6F, 0x02000000, 25)  # DRV_STATUS_M1
    OTPW               = (0x6F, 0x04000000, 26)  # DRV_STATUS_M1
    S2GA               = (0x6F, 0x08000000, 27)  # DRV_STATUS_M1
    S2GB               = (0x6F, 0x10000000, 28)  # DRV_STATUS_M1
    OLA                = (0x6F, 0x20000000, 29)  # DRV_STATUS_M1
    OLB                = (0x6F, 0x40000000, 30)  # DRV_STATUS_M1
    STST               = (0x6F, 0x80000000, 31)  # DRV_STATUS_M1


class TMC5062_fields_m2(object):

    # RAMPMODE_M2
    RAMPMODE           = (0x40, 0x00000003,  0)  # RAMPMODE_M2

    # XACTUAL_M2
    XACTUAL            = (0x41, 0xFFFFFFFF,  0)  # XACTUAL_M2

    # VACTUAL_M2
    VACTUAL            = (0x42, 0x00FFFFFF,  0)  # VACTUAL_M2

    # VSTART_M2
    VSTART             = (0x43, 0x0003FFFF,  0)  # VSTART_M2

    # A1_M2
    A1                 = (0x44, 0x0000FFFF,  0)  # A1_M2

    # V1_M2
    V1_                = (0x45, 0x000FFFFF,  0)  # V1_M2

    # AMAX_M2
    AMAX               = (0x46, 0x0000FFFF,  0)  # AMAX_M2

    # VMAX_M2
    VMAX               = (0x47, 0x007FFFFF,  0)  # VMAX_M2

    # DMAX_M2
    DMAX               = (0x48, 0x0000FFFF,  0)  # DMAX_M2

    # D1_M2
    D1                 = (0x4A, 0x0000FFFF,  0)  # D1_M2

    # VSTOP_M2
    VSTOP              = (0x4B, 0x0003FFFF,  0)  # VSTOP_M2

    # TZEROWAIT_M2
    TZEROWAIT          = (0x4C, 0x0000FFFF,  0)   # TZEROWAIT_M2

    # XTARGET_M2
    XTARGET            = (0x4D, 0xFFFFFFFF,  0)   # XTARGET_M2

    # IHOLD_IRUN_M2
    IHOLD              = (0x50, 0x0000001F,  0)  # IHOLD_IRUN_M2
    IRUN               = (0x50, 0x00001F00,  8)  # IHOLD_IRUN_M2
    IHOLDDELAY         = (0x50, 0x000F0000, 16)  # IHOLD_IRUN_M2

    # VCOOLTHRS_M2
    VCOOLTHRS          = (0x51, 0x007FFFFF,  0)  # VCOOLTHRS_M2

    # VHIGH_M2
    VHIGH              = (0x52, 0x007FFFFF,  0)  # VHIGH_M2

    # VDCMIN_M2
    VDCMIN             = (0x53, 0x007FFFFF,  0)  # VDCMIN_M2

    # SW_MODE_M2
    STOP_L_ENABLE      = (0x54, 0x00000001,  0)  # SW_MODE_M2
    STOP_R_ENABLE      = (0x54, 0x00000002,  1)  # SW_MODE_M2
    POL_STOP_L         = (0x54, 0x00000004,  2)  # SW_MODE_M2
    POL_STOP_R         = (0x54, 0x00000008,  3)  # SW_MODE_M2
    SWAP_LR            = (0x54, 0x00000010,  4)  # SW_MODE_M2
    LATCH_L_ACTIVE     = (0x54, 0x00000020,  5)  # SW_MODE_M2
    LATCH_L_INACTIVE   = (0x54, 0x00000040,  6)  # SW_MODE_M2
    LATCH_R_ACTIVE     = (0x54, 0x00000080,  7)  # SW_MODE_M2
    LATCH_R_INACTIVE   = (0x54, 0x00000100,  8)  # SW_MODE_M2
    EN_LATCH_ENCODER   = (0x54, 0x00000200,  9)  # SW_MODE_M2
    SG_STOP            = (0x54, 0x00000400, 10)  # SW_MODE_M2
    EN_SOFTSTOP        = (0x54, 0x00000800, 11)  # SW_MODE_M2

    # RAMP_STAT_M2
    STATUS_STOP_L      = (0x55, 0x00000001,  0)  # RAMP_STAT_M2
    STATUS_STOP_R      = (0x55, 0x00000002,  1)  # RAMP_STAT_M2
    STATUS_LATCH_L     = (0x55, 0x00000004,  2)  # RAMP_STAT_M2
    STATUS_LATCH_R     = (0x55, 0x00000008,  3)  # RAMP_STAT_M2
    EVENT_STOP_L       = (0x55, 0x00000010,  4)  # RAMP_STAT_M2
    EVENT_STOP_R       = (0x55, 0x00000020,  5)  # RAMP_STAT_M2
    EVENT_STOP_SG      = (0x55, 0x00000040,  6)  # RAMP_STAT_M2
    EVENT_POS_REACHED  = (0x55, 0x00000080,  7)  # RAMP_STAT_M2
    VELOCITY_REACHED   = (0x55, 0x00000100,  8)  # RAMP_STAT_M2
    POSITION_REACHED   = (0x55, 0x00000200,  9)  # RAMP_STAT_M2
    VZERO              = (0x55, 0x00000400, 10)  # RAMP_STAT_M2
    T_ZEROWAIT_ACTIVE  = (0x55, 0x00000800, 11)  # RAMP_STAT_M2
    SECOND_MOVE        = (0x55, 0x00001000, 12)  # RAMP_STAT_M2
    STATUS_SG          = (0x55, 0x00002000, 13)  # RAMP_STAT_M2

    # XLATCH_M2
    XLATCH             = (0x56, 0xFFFFFFFF,  0)  # XLATCH_M2


    # ENCMODE_M2
    POL_A              = (0x58, 0x00000001,  0)  # ENCMODE_M2
    POL_B              = (0x58, 0x00000002,  1)  # ENCMODE_M2
    POL_N              = (0x58, 0x00000004,  2)  # ENCMODE_M2
    IGNORE_AB          = (0x58, 0x00000008,  3)  # ENCMODE_M2
    CLR_CONT           = (0x58, 0x00000010,  4)  # ENCMODE_M2
    CLR_ONCE           = (0x58, 0x00000020,  5)  # ENCMODE_M2
    POS_EDGE_NEG_EDGE  = (0x58, 0x000000C0,  6)  # ENCMODE_M2
    CLR_ENC_X          = (0x58, 0x00000100,  8)  # ENCMODE_M2
    LATCH_X_ACT        = (0x58, 0x00000200,  9)  # ENCMODE_M2
    ENC_SEL_DECIMAL    = (0x58, 0x00000400, 10)  # ENCMODE_M2

    # X_ENC_M2
    X_ENC              = (0x59, 0xFFFFFFFF,  0)  # X_ENC_M2

    # ENC_CONST_M2
    INTEGER            = (0x5A, 0xFFFF0000, 16)  # ENC_CONST_M2
    FRACTIONAL         = (0x5A, 0x0000FFFF,  0)  # ENC_CONST_M2

    # ENC_STATUS_M2
    ENC_STATUS         = (0x5B, 0x00000001,  0)  # ENC_STATUS_M2

    # ENC_LATCH_M2
    ENC_LATCH          = (0x5C, 0xFFFFFFFF,  0)  # ENC_LATCH_M2

    # MSLUTSEL_M2
    W0                 = (0x78, 0x00000003,  0)  # MSLUTSEL_M2
    W1                 = (0x78, 0x0000000C,  2)  # MSLUTSEL_M2
    W2                 = (0x78, 0x00000030,  4)  # MSLUTSEL_M2
    W3                 = (0x78, 0x000000C0,  6)  # MSLUTSEL_M2
    X1                 = (0x78, 0x0000FF00,  8)  # MSLUTSEL_M2
    X2                 = (0x78, 0x00FF0000, 16)  # MSLUTSEL_M2
    X3                 = (0x78, 0xFF000000, 24)  # MSLUTSEL_M2

    # MSLUTSTART_M2
    START_SIN          = (0x79, 0x000000FF,  0)  # MSLUTSTART_M2
    START_SIN90        = (0x79, 0x00FF0000, 16)  # MSLUTSTART_M2

    # MSCNT_M2
    MSCNT              = (0x7A, 0x000003FF,  0)  # MSCNT_M2

    # MSCURACT_M2
    CUR_A              = (0x7B, 0x000001FF,  0)  # MSCURACT_M2
    CUR_B              = (0x7B, 0x01FF0000, 16)  # MSCURACT_M2

    # CHOPCONF_M2
    TOFF               = (0x7C, 0x0000000F,  0)  # CHOPCONF_M2
    TFD_2__0_          = (0x7C, 0x00000070,  4)  # CHOPCONF_M2
    OFFSET             = (0x7C, 0x00000780,  7)  # CHOPCONF_M2
    TFD__              = (0x7C, 0x00000800, 11)  # CHOPCONF_M2
    DISFDCC            = (0x7C, 0x00001000, 12)  # CHOPCONF_M2
    RNDTF              = (0x7C, 0x00002000, 13)  # CHOPCONF_M2
    CHM                = (0x7C, 0x00004000, 14)  # CHOPCONF_M2
    TBL                = (0x7C, 0x00018000, 15)  # CHOPCONF_M2
    VSENSE             = (0x7C, 0x00020000, 17)  # CHOPCONF_M2
    VHIGHFS            = (0x7C, 0x00040000, 18)  # CHOPCONF_M2
    VHIGHCHM           = (0x7C, 0x00080000, 19)  # CHOPCONF_M2
    SYNC               = (0x7C, 0x00F00000, 20)  # CHOPCONF_M2
    DISS2G             = (0x7C, 0x40000000, 30)  # CHOPCONF_M2

    # COOLCONF_M2
    SEMIN              = (0x7D, 0x0000000F,  0)  # COOLCONF_M2
    SEUP               = (0x7D, 0x00000060,  5)  # COOLCONF_M2
    SEMAX              = (0x7D, 0x00000F00,  8)  # COOLCONF_M2
    SEDN               = (0x7D, 0x00006000, 13)  # COOLCONF_M2
    SEIMIN             = (0x7D, 0x00008000, 15)  # COOLCONF_M2
    SGT                = (0x7D, 0x007F0000, 16)  # COOLCONF_M2
    SFILT              = (0x7D, 0x01000000, 24)  # COOLCONF_M2

    # DRV_STATUS_M2
    SG_RESULT          = (0x7F, 0x000003FF,  0)  # DRV_STATUS_M2
    FSACTIVE           = (0x7F, 0x00008000, 15)  # DRV_STATUS_M2
    CS_ACTUAL          = (0x7F, 0x001F0000, 16)  # DRV_STATUS_M2
    STALLGUARD         = (0x7F, 0x01000000, 24)  # DRV_STATUS_M2
    OT                 = (0x7F, 0x02000000, 25)  # DRV_STATUS_M2
    OTPW               = (0x7F, 0x04000000, 26)  # DRV_STATUS_M2
    S2GA               = (0x7F, 0x08000000, 27)  # DRV_STATUS_M2
    S2GB               = (0x7F, 0x10000000, 28)  # DRV_STATUS_M2
    OLA                = (0x7F, 0x20000000, 29)  # DRV_STATUS_M2
    OLB                = (0x7F, 0x40000000, 30)  # DRV_STATUS_M2
    STST               = (0x7F, 0x80000000, 31)  # DRV_STATUS_M2
