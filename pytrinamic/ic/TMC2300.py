from ..ic.tmc_ic import TMCIc


class TMC2300(TMCIc):
    """
    The TMC2300 is a low voltage driver for two-phase stepper motors up to 1.2A RMS. Supply voltage: 2 - 11V.
    """
    def __init__(self):
        super().__init__("TMC2300", self.__doc__)

    class REG:
        GCONF      = 0x00
        GSTAT      = 0x01
        IFCNT      = 0x02
        SLAVECONF  = 0x03
        IOIN       = 0x06
        IHOLD_IRUN = 0x10
        TPOWERDOWN = 0x11
        TSTEP      = 0x12
        TCOOLTHRS  = 0x14
        VACTUAL    = 0x22
        SGTHRS     = 0x40
        SG_VALUE   = 0x41
        COOLCONF   = 0x42
        MSCNT      = 0x6A
        MSCURACT   = 0x6B
        CHOPCONF   = 0x6C
        DRV_STATUS = 0x6F
        PWM_CONF   = 0x70
        PWM_SCALE  = 0x71
        PWM_AUTO   = 0x72

    class FIELD:
        """
        Define all register bitfields of the TMC2300.

        Each field is defined as a tuple consisting of ( Address, Mask, Shift ).

        The name of the register is written as a comment behind each tuple. This is
        intended for IDE users viewing the definition of a field by hovering over
        it. This allows the user to see the corresponding register name of a field
        without opening this file and searching for the definition.
        """

        # GCONF
        SET_TO_0           = (0x00, 0x00000001,  0)
        EXTCAP             = (0x00, 0x00000002,  1)
        SHAFT              = (0x00, 0x00000008,  3)
        DIAG_INDEX         = (0x00, 0x00000010,  4)
        DIAG_STEP          = (0x00, 0x00000020,  5)
        MULTISTEP_FILT     = (0x00, 0x00000040,  6)
        TEST_MODE          = (0x00, 0x00000080,  7)

        # GSTAT
        RESET              = (0x01, 0x00000001,  0)
        DRV_ERR            = (0x01, 0x00000002,  1)
        U3V5               = (0x01, 0x00000004,  2)

        # IFCNT
        IFCNT              = (0x02, 0x000000FF,  0)

        # SLAVECONF
        SLAVECONF          = (0x03, 0x00000F00,  8)

        # IOIN
        EN                 = (0x06, 0x00000001,  0)
        NSTDBY             = (0x06, 0x00000002,  1)
        MS1                = (0x06, 0x00000004,  2)
        MS2                = (0x06, 0x00000008,  3)
        DIAG               = (0x06, 0x00000010,  4)
        STEPPER_CLK_INPUT  = (0x06, 0x00000020,  5)
        PDN_UART           = (0x06, 0x00000040,  6)
        MODE_INPUT         = (0x06, 0x00000080,  7)
        STEP               = (0x06, 0x00000100,  8)
        DIR                = (0x06, 0x00000200,  9)
        COMP_A1A2          = (0x06, 0x00000400, 10)
        COMP_B1B2          = (0x06, 0x00000800, 11)
        VERSION            = (0x06, 0xFF000000, 24)

        # IHOLD_IRUN
        IHOLD              = (0x10, 0x0000001F,  0)
        IRUN               = (0x10, 0x00001F00,  8)
        IHOLDDELAY         = (0x10, 0x000F0000, 16)

        # TPOWERDOWN
        TPOWERDOWN         = (0x11, 0x000000FF,  0)

        # TSTEP
        TSTEP              = (0x12, 0x000FFFFF,  0)

        # TCOOLTHRS
        TCOOLTHRS          = (0x14, 0xFFFFFFFF,  0)

        # VACTUAL
        VACTUAL            = (0x22, 0x00FFFFFF,  0)

        # SGTHRS
        SGTHRS             = (0x40, 0x000000FF,  0)

        # SG_VALUE
        SG_VALUE           = (0x41, 0x000003FF,  0)

        # COOLCONF
        SEMIN              = (0x42, 0x0000000F,  0)
        SEUP               = (0x42, 0x00000060,  5)
        SEMAX              = (0x42, 0x00000F00,  8)
        SEDN               = (0x42, 0x00006000, 13)
        SEIMIN             = (0x42, 0x00008000, 15)

        # MSCNT
        MSCNT              = (0x6A, 0x000003FF,  0)

        # MSCURACT
        CUR_A              = (0x6B, 0x000001FF,  0)
        CUR_B              = (0x6B, 0x01FF0000, 16)

        # CHOPCONF
        ENABLEDRV          = (0x6C, 0x00000001,  0)
        TBL                = (0x6C, 0x00018000, 15)
        MRES               = (0x6C, 0x0F000000, 24)
        INTPOL             = (0x6C, 0x10000000, 28)
        DEDGE              = (0x6C, 0x20000000, 29)
        DISS2G             = (0x6C, 0x40000000, 30)
        DISS2VS            = (0x6C, 0x80000000, 31)

        # DRV_STATUS
        OTPW               = (0x6F, 0x00000001,  0)
        OT                 = (0x6F, 0x00000002,  1)
        S2GA               = (0x6F, 0x00000004,  2)
        S2GB               = (0x6F, 0x00000008,  3)
        S2VSA              = (0x6F, 0x00000010,  4)
        S2VSB              = (0x6F, 0x00000020,  5)
        OLA                = (0x6F, 0x00000040,  6)
        OLB                = (0x6F, 0x00000080,  7)
        T120               = (0x6F, 0x00000100,  8)
        T150               = (0x6F, 0x00000200,  9)
        CS_ACTUAL          = (0x6F, 0x001F0000, 16)
        STST               = (0x6F, 0x80000000, 31)

        # PWMCONF
        PWM_OFS            = (0x70, 0x000000FF,  0)
        PWM_GRAD           = (0x70, 0x0000FF00,  8)
        PWM_FREQ           = (0x70, 0x00030000, 16)
        PWM_AUTOSCALE      = (0x70, 0x00040000, 18)
        PWM_AUTOGRAD       = (0x70, 0x00080000, 19)
        FREEWHEEL          = (0x70, 0x00300000, 20)
        PWM_REG            = (0x70, 0x0F000000, 24)
        PWM_LIM            = (0x70, 0xF0000000, 28)

        # PWM_SCALE
        PWM_SCALE_SUM      = (0x71, 0x000000FF,  0)
        PWM_SCALE_AUTO     = (0x71, 0xFFFF0000, 16)

        # PWM_AUTO
        PWM_OFS_AUTO       = (0x72, 0x000000FF,  0)
        PWM_GRAD_AUTO      = (0x72, 0x00FF0000, 16)
