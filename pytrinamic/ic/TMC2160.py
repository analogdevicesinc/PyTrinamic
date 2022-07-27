from ..ic.tmc_ic import TMCIc


class TMC2160(TMCIc):
    """
    The TMC2160 is a high-power stepper motor driver IC with SPI interface. Supply voltage: 8-60V.
    """
    def __init__(self):
        super().__init__("TMC2160", self.__doc__)

    class REG:
        """
        Define all registers of the TMC2160.
        """
        GCONF          = 0x00
        GSTAT          = 0x01
        IOIN_OUTPUT    = 0x04
        X_COMPARE      = 0x05
        OTP_PROG       = 0x06
        OTP_READ       = 0x07
        FACTORY_CONF   = 0x08
        SHORT_CONF     = 0x09
        DRV_CONF       = 0x0A
        GLOBAL_SCALER  = 0x0B
        OFFSET_READ    = 0x0C
        IHOLD_IRUN     = 0x10
        TPOWERDOWN     = 0x11
        TSTEP          = 0x12
        TPWMTHRS       = 0x13
        TCOOLTHRS      = 0x14
        THIGH          = 0x15
        XDIRECT        = 0x2D
        VDCMIN         = 0x33
        MSLUT__        = 0x60
        MSLUTSEL       = 0x68
        MSLUTSTART     = 0x69
        MSCNT          = 0x6A
        MSCURACT       = 0x6B
        CHOPCONF       = 0x6C
        COOLCONF       = 0x6D
        DCCTRL         = 0x6E
        DRV_STATUS     = 0x6F
        PWM_CONF       = 0x70
        PWM_SCALE      = 0x71
        PWM_AUTO       = 0x72
        LOST_STEPS     = 0x73

    class FIELD:
        """
        Define all register bitfields of the TMC2160.

        Each field is defined as a tuple consisting of ( Address, Mask, Shift ).

        The name of the register is written as a comment behind each tuple. This is
        intended for IDE users viewing the definition of a field by hovering over
        it. This allows the user to see the corresponding register name of a field
        without opening this file and searching for the definition.
        """

        # GCONF
        RECALIBRATE                        = (0x00, 0x00000001,  0)
        FASTSTANDSTILL                     = (0x00, 0x00000002,  1)
        EN_PWM_MODE                        = (0x00, 0x00000004,  2)
        MULTISTEP_FILT                     = (0x00, 0x00000008,  3)
        SHAFT                              = (0x00, 0x00000010,  4)
        DIAG0_ERROR__ONLY_WITH_SD_MODE_1_  = (0x00, 0x00000020,  5)
        DIAG0_OTPW__ONLY_WITH_SD_MODE_1_   = (0x00, 0x00000040,  6)

        DIAG0_STALL                        = (0x00, 0x00000080,  7)
        DIAG1_STALL                        = (0x00, 0x00000100,  8)

        DIAG0_STEP                         = (0x00, 0x00000080,  7)
        DIAG1_DIR                          = (0x00, 0x00000100,  8)

        DIAG1_INDEX                        = (0x00, 0x00000200,  9)
        DIAG1_ONSTATE                      = (0x00, 0x00000400, 10)
        DIAG1_STEPS_SKIPPED                = (0x00, 0x00000800, 11)
        DIAG0_INT_PUSHPULL                 = (0x00, 0x00001000, 12)
        DIAG1_POSCOMP_PUSHPULL             = (0x00, 0x00002000, 13)
        SMALL_HYSTERESIS                   = (0x00, 0x00004000, 14)
        STOP_ENABLE                        = (0x00, 0x00008000, 15)
        DIRECT_MODE                        = (0x00, 0x00010000, 16)
        TEST_MODE                          = (0x00, 0x00020000, 17)

        # GSTAT
        RESET                              = (0x01, 0x00000001,  0)
        DRV_ERR                            = (0x01, 0x00000002,  1)
        UV_CP                              = (0x01, 0x00000004,  2)

        # IOIN / OUTPUT
        STEP                               = (0x04, 0x00000001,  0)
        DIR                                = (0x04, 0x00000002,  1)
        DCEN_CFG4                          = (0x04, 0x00000004,  2)
        DCIN_CFG5                          = (0x04, 0x00000008,  3)
        DRV_ENN                            = (0x04, 0x00000010,  4)
        DCO_CFG6                           = (0x04, 0x00000020,  5)
        VERSION                            = (0x04, 0xFF000000, 24)
        OUTPUT_PIN_POLARITY                = (0x04, 0x00000001,  0)

        # X_COMPARE
        X_COMPARE                          = (0x05, 0xFFFFFFFF,  0)

        # OTP_PROG
        OTPBIT                             = (0x06, 0x00000007,  0)
        OTPBYTE                            = (0x06, 0x00000030,  4)
        OTPMAGIC                           = (0x06, 0x0000FF00,  8)

        # OTP_READ
        OTP_FCLKTRIM                       = (0x07, 0x0000001F,  0)
        OTP_S2_LEVEL                       = (0x07, 0x00000020,  5)
        OTP_BBM                            = (0x07, 0x00000040,  6)
        OTP_TBL                            = (0x07, 0x00000080,  7)

        # FACTORY_CONF
        FCLKTRIM                           = (0x08, 0x0000001F,  0)

        # SHORT_CONF
        S2VS_LEVEL                         = (0x09, 0x0000000F,  0)
        S2GND_LEVEL                        = (0x09, 0x00000F00,  8)
        SHORTFILTER                        = (0x09, 0x00030000, 16)
        SHORTDELAY                         = (0x09, 0x00040000, 18)

        # DRV_CONF
        BBMTIME                            = (0x0A, 0x0000001F,  0)
        BBMCLKS                            = (0x0A, 0x00000F00,  8)
        OTSELECT                           = (0x0A, 0x00030000, 16)
        DRVSTRENGTH                        = (0x0A, 0x000C0000, 18)
        FILT_ISENSE                        = (0x0A, 0x00300000, 20)

        # GLOBAL_SCALER
        GLOBAL_SCALER                      = (0x0B, 0x000000FF,  0)

        # OFFSET_READ
        OFFSET_READ_A                      = (0x0C, 0x0000FF00,  8)
        OFFSET_READ_B                      = (0x0C, 0x000000FF,  0)

        # IHOLD_IRUN
        IHOLD                              = (0x10, 0x0000001F,  0)
        IRUN                               = (0x10, 0x00001F00,  8)
        IHOLDDELAY                         = (0x10, 0x000F0000, 16)

        # TPOWERDOWN
        TPOWERDOWN                         = (0x11, 0x000000FF,  0)

        # TSTEP
        TSTEP                              = (0x12, 0x000FFFFF,  0)

        # TPWMTHRS
        TPWMTHRS                           = (0x13, 0x000FFFFF,  0)

        # TCOOLTHRS
        TCOOLTHRS                          = (0x14, 0x000FFFFF,  0)

        # THIGH
        THIGH                              = (0x15, 0x000FFFFF,  0)

        # XDIRECT
        XDIRECT                            = (0x2D, 0xFFFFFFFF,  0)

        # VDCMIN
        VDCMIN                             = (0x33, 0x007FFFFF,  0)

        # MSLUTSEL
        W0                                 = (0x68, 0x00000003,  0)
        W1                                 = (0x68, 0x0000000C,  2)
        W2                                 = (0x68, 0x00000030,  4)
        W3                                 = (0x68, 0x000000C0,  6)
        X1                                 = (0x68, 0x0000FF00,  8)
        X2                                 = (0x68, 0x00FF0000, 16)
        X3                                 = (0x68, 0xFF000000, 24)

        # MSLUTSTART
        START_SIN                          = (0x69, 0x000000FF,  0)
        START_SIN90                        = (0x69, 0x00FF0000, 16)

        # MSCNT
        MSCNT                              = (0x6A, 0x000003FF,  0)

        # MSCURACT
        CUR_A                              = (0x6B, 0x000001FF,  0)
        CUR_B                              = (0x6B, 0x01FF0000, 16)

        # CHOPCONF
        TOFF                               = (0x6C, 0x0000000F,  0)

        TFD_2__0_                          = (0x6C, 0x00000070,  4)
        OFFSET                             = (0x6C, 0x00000780,  7)

        HSTRT                              = (0x6C, 0x00000070,  4)
        HEND                               = (0x6C, 0x00000780,  7)

        TFD__                              = (0x6C, 0x00000800, 11)
        DISFDCC                            = (0x6C, 0x00001000, 12)
        RNDTF                              = (0x6C, 0x00002000, 13)
        CHM                                = (0x6C, 0x00004000, 14)
        TBL                                = (0x6C, 0x00018000, 15)
        VSENSE                             = (0x6C, 0x00020000, 17)
        VHIGHFS                            = (0x6C, 0x00040000, 18)
        VHIGHCHM                           = (0x6C, 0x00080000, 19)
        TPFD                               = (0x6C, 0x00F00000, 20)
        MRES                               = (0x6C, 0x0F000000, 24)
        INTPOL                             = (0x6C, 0x10000000, 28)
        DEDGE                              = (0x6C, 0x20000000, 29)
        DISS2G                             = (0x6C, 0x40000000, 30)
        DISS2VS                            = (0x6C, 0x80000000, 31)

        # COOLCONF
        SEMIN                              = (0x6D, 0x0000000F,  0)
        SEUP                               = (0x6D, 0x00000060,  5)
        SEMAX                              = (0x6D, 0x00000F00,  8)
        SEDN                               = (0x6D, 0x00006000, 13)
        SEIMIN                             = (0x6D, 0x00008000, 15)
        SGT                                = (0x6D, 0x007F0000, 16)
        SFILT                              = (0x6D, 0x01000000, 24)

        # DCCTRL
        DC_TIME                            = (0x6E, 0x000003FF,  0)
        DC_SG                              = (0x6E, 0x00FF0000, 16)

        # DRV_STATUS
        SG_RESULT                          = (0x6F, 0x000003FF,  0)
        S2VSA                              = (0x6F, 0x00001000, 12)
        S2VSB                              = (0x6F, 0x00002000, 13)
        STEALTH                            = (0x6F, 0x00004000, 14)
        FSACTIVE                           = (0x6F, 0x00008000, 15)
        CS_ACTUAL                          = (0x6F, 0x001F0000, 16)
        STALLGUARD                         = (0x6F, 0x01000000, 24)
        OT                                 = (0x6F, 0x02000000, 25)
        OTPW                               = (0x6F, 0x04000000, 26)
        S2GA                               = (0x6F, 0x08000000, 27)
        S2GB                               = (0x6F, 0x10000000, 28)
        OLA                                = (0x6F, 0x20000000, 29)
        OLB                                = (0x6F, 0x40000000, 30)
        STST                               = (0x6F, 0x80000000, 31)

        # PWMCONF
        PWM_OFS                            = (0x70, 0x000000FF,  0)
        PWM_GRAD                           = (0x70, 0x0000FF00,  8)
        PWM_FREQ                           = (0x70, 0x00030000, 16)
        PWM_AUTOSCALE                      = (0x70, 0x00040000, 18)
        PWM_AUTOGRAD                       = (0x70, 0x00080000, 19)
        FREEWHEEL                          = (0x70, 0x00300000, 20)
        PWM_REG                            = (0x70, 0x0F000000, 24)
        PWM_LIM                            = (0x70, 0xF0000000, 28)

        # PWM_SCALE
        PWM_SCALE_SUM                      = (0x71, 0x000000FF,  0)
        PWM_SCALE_AUTO                     = (0x71, 0x01FF0000, 16)

        # PWM_AUTO
        PWM_OFS_AUTO                       = (0x72, 0x000000FF,  0)
        PWM_GRAD_AUTO                      = (0x72, 0x00FF0000, 16)

        # LOST_STEPS
        LOST_STEPS                         = (0x73, 0x000FFFFF,  0)
