from ..ic.tmc_ic import TMCIc


class TMC6200(TMCIc):
    """
    The TMC6200 is a high-power gate-driver for PMSM servo or BLDC motors. Supply voltage: 8 - 60V
    """
    def __init__(self):
        super().__init__("TMC6200", self.__doc__)

    class REG:

        GCONF           = 0x00
        GSTAT           = 0x01
        IOIN_OUTPUT     = 0x04
        OTP_PROG        = 0x06
        OTP_READ        = 0x07
        FACTORY_CONF    = 0x08
        SHORT_CONF      = 0x09
        DRV_CONF        = 0x0A

    class FIELD:

        # GCONF
        DISABLE           = (0x00, 0x00000001, 0)
        SINGLELINE        = (0x00, 0x00000002, 1)
        FAULTDIRECT       = (0x00, 0x00000004, 2)
        UNUSED            = (0x00, 0x00000008, 3)
        AMPLIFICATION     = (0x00, 0x00000030, 4)
        AMPLIFIER_OFF     = (0x00, 0x00000040, 6)
        TEST_MODE         = (0x00, 0x00000080, 7)

        # GSTAT
        RESET             = (0x01, 0x00000001, 0)
        DRV_OTPW          = (0x01, 0x00000002, 1)
        DRV_OT            = (0x01, 0x00000004, 2)
        UV_CP             = (0x01, 0x00000008, 3)
        SHORTDET_U        = (0x01, 0x00000010, 4)
        S2GU              = (0x01, 0x00000020, 5)
        S2VSU             = (0x01, 0x00000040, 6)
        SHORTDET_V        = (0x01, 0x00000100, 8)
        S2GV              = (0x01, 0x00000200, 9)
        S2VSV             = (0x01, 0x00000400, 10)
        SHORTDET_W        = (0x01, 0x00001000, 12)
        S2GW              = (0x01, 0x00002000, 13)
        S2VSW             = (0x01, 0x00004000, 14)

        # IOIN / OUTPUT
        UL                = (0x04, 0x00000001, 0)
        UH                = (0x04, 0x00000002, 1)
        VL                = (0x04, 0x00000004, 2)
        VH                = (0x04, 0x00000008, 3)
        WL                = (0x04, 0x00000010, 4)
        WH                = (0x04, 0x00000020, 5)
        DRV_EN            = (0x04, 0x00000040, 6)
        OTPW              = (0x04, 0x00000100, 8)
        OT136_C           = (0x04, 0x00000200, 9)
        OT143_C           = (0x04, 0x00000400, 10)
        OT150_C           = (0x04, 0x00000800, 11)
        VERSION           = (0x04, 0xFF000000, 24)

        # OTP_PROG
        OTPBIT            = (0x06, 0x00000007, 0)
        OTPBYTE           = (0x06, 0x00000030, 4)
        OTPMAGIC          = (0x06, 0x0000FF00, 8)

        # OTP_READ
        OTP_FCLKTRIM      = (0x07, 0x0000001F, 0)
        OTP_S2_LEVEL      = (0x07, 0x00000020, 5)
        OTP_BBM           = (0x07, 0x000000C0, 6)

        # FACTORY_CONF
        FACTORY_CONF      = (0x08, 0x0000001F, 0)

        # SHORT_CONF
        S2VS_LEVEL        = (0x09, 0x0000000F, 0)
        S2G_LEVEL         = (0x09, 0x00000F00, 8)
        SHORTFILTER       = (0x09, 0x00030000, 16)
        SHORTDELAY        = (0x09, 0x00100000, 20)
        RETRY             = (0x09, 0x03000000, 24)
        PROTECT_PARALLEL  = (0x09, 0x10000000, 28)
        DISABLE_S2G       = (0x09, 0x20000000, 29)
        DISABLE_S2VS      = (0x09, 0x40000000, 30)

        # DRV_CONF
        BBMCLKS           = (0x0A, 0x0000000F, 0)
        OTSELECT          = (0x0A, 0x00030000, 16)
        DRVSTRENGTH       = (0x0A, 0x000C0000, 18)
