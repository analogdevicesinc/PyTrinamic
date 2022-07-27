from ..ic.tmc_ic import TMCIc


class TMC5160(TMCIc):
    """
    The TMC5160-A is a high-power stepper motor controller and driver IC with serial communication interfaces.
    Supply voltage: 8-60V.
    """
    def __init__(self):
        super().__init__("TMC5160", self.__doc__)

    class REG:
        """
        Define all registers of the TMC5160.
        """
        GCONF          = 0x00
        GSTAT          = 0x01
        IFCNT          = 0x02
        SLAVECONF      = 0x03
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
        RAMPMODE       = 0x20
        XACTUAL        = 0x21
        VACTUAL        = 0x22
        VSTART         = 0x23
        A1             = 0x24
        V1             = 0x25
        AMAX           = 0x26
        VMAX           = 0x27
        DMAX           = 0x28
        D1             = 0x2A
        VSTOP          = 0x2B
        TZEROWAIT      = 0x2C
        XTARGET        = 0x2D
        VDCMIN         = 0x33
        SW_MODE        = 0x34
        RAMP_STAT      = 0x35
        XLATCH         = 0x36
        ENCMODE        = 0x38
        X_ENC          = 0x39
        ENC_CONST      = 0x3A
        ENC_STATUS     = 0x3B
        ENC_LATCH      = 0x3C
        ENC_DEVIATION  = 0x3D
        MSLUT0         = 0x60
        MSLUT1         = 0x61
        MSLUT2         = 0x62
        MSLUT3         = 0x63
        MSLUT4         = 0x64
        MSLUT5         = 0x65
        MSLUT6         = 0x66
        MSLUT7         = 0x67
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
        Define all register bitfields of the TMC5160.

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

        # IFCNT
        IFCNT                              = (0x02, 0x000000FF,  0)

        # SLAVECONF
        SLAVEADDR                          = (0x03, 0x000000FF,  0)
        SENDDELAY                          = (0x03, 0x00000F00,  8)

        # IOIN / OUTPUT
        REFL_STEP                          = (0x04, 0x00000001,  0)
        REFR_DIR                           = (0x04, 0x00000002,  1)
        ENCB_DCEN_CFG4                     = (0x04, 0x00000004,  2)
        ENCA_DCIN_CFG5                     = (0x04, 0x00000008,  3)
        DRV_ENN_CFG6                       = (0x04, 0x00000010,  4)
        ENC_N_DCO                          = (0x04, 0x00000020,  5)
        SD_MODE                            = (0x04, 0x00000040,  6)
        SWCOMP_IN                          = (0x04, 0x00000080,  7)
        VERSION                            = (0x04, 0xFF000000, 24)
        OUTPUT_PIN_POLARITY                = (0x04, 0x00000001,  0)

        # X_COMPARE
        X_COMPARE                          = (0x05, 0xFFFFFFFF,  0)

        # OTP_PROG
        OTPBIT                             = (0x06, 0x00000007,  0)
        OTPBYTE                            = (0x06, 0x00000030,  4)
        OTPMAGIC                           = (0x06, 0x0000FF00,  8)

        # OTP_READ
        OTP_TBL                            = (0x07, 0x00000080,  7)
        OTP_BBM                            = (0x07, 0x00000040,  6)
        OTP_S2_LEVEL                       = (0x07, 0x00000020,  5)
        OTP_FCLKTRIM                       = (0x07, 0x0000001F,  0)

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

        # RAMPMODE
        RAMPMODE                           = (0x20, 0x00000003,  0)

        # XACTUAL
        XACTUAL                            = (0x21, 0xFFFFFFFF,  0)

        # VACTUAL
        VACTUAL                            = (0x22, 0x00FFFFFF,  0)

        # VSTART
        VSTART                             = (0x23, 0x0003FFFF,  0)

        # A1
        A1                                 = (0x24, 0x0000FFFF,  0)

        # V1
        V1_                                = (0x25, 0x000FFFFF,  0)

        # AMAX
        AMAX                               = (0x26, 0x0000FFFF,  0)

        # VMAX
        VMAX                               = (0x27, 0x007FFFFF,  0)

        # DMAX
        DMAX                               = (0x28, 0x0000FFFF,  0)

        # D1
        D1                                 = (0x2A, 0x0000FFFF,  0)

        # VSTOP
        VSTOP                              = (0x2B, 0x0003FFFF,  0)

        # TZEROWAIT
        TZEROWAIT                          = (0x2C, 0x0000FFFF,  0)

        # XTARGET
        XTARGET                            = (0x2D, 0xFFFFFFFF,  0)

        # VDCMIN
        VDCMIN                             = (0x33, 0x007FFFFF,  0)

        # SW_MODE
        STOP_L_ENABLE                      = (0x34, 0x00000001,  0)
        STOP_R_ENABLE                      = (0x34, 0x00000002,  1)
        POL_STOP_L                         = (0x34, 0x00000004,  2)
        POL_STOP_R                         = (0x34, 0x00000008,  3)
        SWAP_LR                            = (0x34, 0x00000010,  4)
        LATCH_L_ACTIVE                     = (0x34, 0x00000020,  5)
        LATCH_L_INACTIVE                   = (0x34, 0x00000040,  6)
        LATCH_R_ACTIVE                     = (0x34, 0x00000080,  7)
        LATCH_R_INACTIVE                   = (0x34, 0x00000100,  8)
        EN_LATCH_ENCODER                   = (0x34, 0x00000200,  9)
        SG_STOP                            = (0x34, 0x00000400, 10)
        EN_SOFTSTOP                        = (0x34, 0x00000800, 11)

        # RAMP_STAT
        STATUS_STOP_L                      = (0x35, 0x00000001,  0)
        STATUS_STOP_R                      = (0x35, 0x00000002,  1)
        STATUS_LATCH_L                     = (0x35, 0x00000004,  2)
        STATUS_LATCH_R                     = (0x35, 0x00000008,  3)
        EVENT_STOP_L                       = (0x35, 0x00000010,  4)
        EVENT_STOP_R                       = (0x35, 0x00000020,  5)
        EVENT_STOP_SG                      = (0x35, 0x00000040,  6)
        EVENT_POS_REACHED                  = (0x35, 0x00000080,  7)
        VELOCITY_REACHED                   = (0x35, 0x00000100,  8)
        POSITION_REACHED                   = (0x35, 0x00000200,  9)
        VZERO                              = (0x35, 0x00000400, 10)
        T_ZEROWAIT_ACTIVE                  = (0x35, 0x00000800, 11)
        SECOND_MOVE                        = (0x35, 0x00001000, 12)
        STATUS_SG                          = (0x35, 0x00002000, 13)

        # XLATCH
        XLATCH                             = (0x36, 0xFFFFFFFF,  0)

        # ENCMODE
        POL_A                              = (0x38, 0x00000001,  0)
        POL_B                              = (0x38, 0x00000002,  1)
        POL_N                              = (0x38, 0x00000004,  2)
        IGNORE_AB                          = (0x38, 0x00000008,  3)
        CLR_CONT                           = (0x38, 0x00000010,  4)
        CLR_ONCE                           = (0x38, 0x00000020,  5)
        POS_EDGE_NEG_EDGE                  = (0x38, 0x000000C0,  6)
        CLR_ENC_X                          = (0x38, 0x00000100,  8)
        LATCH_X_ACT                        = (0x38, 0x00000200,  9)
        ENC_SEL_DECIMAL                    = (0x38, 0x00000400, 10)

        # X_ENC
        X_ENC                              = (0x39, 0xFFFFFFFF,  0)

        # ENC_CONST
        FRACTIONAL                         = (0x3A, 0x0000FFFF,  0)
        INTEGER                            = (0x3A, 0xFFFF0000, 16)

        # ENC_STATUS
        N_EVENT                            = (0x3B, 0x00000001,  0)
        DEVIATION_WARN                     = (0x3B, 0x00000002,  1)

        # ENC_LATCH
        ENC_LATCH                          = (0x3C, 0xFFFFFFFF,  0)

        # ENC_DEVIATION
        ENC_DEVIATION                      = (0x3D, 0x000FFFFF,  0)

        # MSLUT[0]
        OFS0                               = (0x60, 0x00000001,  0)
        OFS1                               = (0x60, 0x00000002,  1)
        OFS2                               = (0x60, 0x00000004,  2)
        OFS3                               = (0x60, 0x00000008,  3)
        OFS4                               = (0x60, 0x00000010,  4)
        OFS5                               = (0x60, 0x00000020,  5)
        OFS6                               = (0x60, 0x00000040,  6)
        OFS7                               = (0x60, 0x00000080,  7)
        OFS8                               = (0x60, 0x00000100,  8)
        OFS9                               = (0x60, 0x00000200,  9)
        OFS10                              = (0x60, 0x00000400, 10)
        OFS11                              = (0x60, 0x00000800, 11)
        OFS12                              = (0x60, 0x00001000, 12)
        OFS13                              = (0x60, 0x00002000, 13)
        OFS14                              = (0x60, 0x00004000, 14)
        OFS15                              = (0x60, 0x00008000, 15)
        OFS16                              = (0x60, 0x00010000, 16)
        OFS17                              = (0x60, 0x00020000, 17)
        OFS18                              = (0x60, 0x00040000, 18)
        OFS19                              = (0x60, 0x00080000, 19)
        OFS20                              = (0x60, 0x00100000, 20)
        OFS21                              = (0x60, 0x00200000, 21)
        OFS22                              = (0x60, 0x00400000, 22)
        OFS23                              = (0x60, 0x00800000, 23)
        OFS24                              = (0x60, 0x01000000, 24)
        OFS25                              = (0x60, 0x02000000, 25)
        OFS26                              = (0x60, 0x04000000, 26)
        OFS27                              = (0x60, 0x08000000, 27)
        OFS28                              = (0x60, 0x10000000, 28)
        OFS29                              = (0x60, 0x20000000, 29)
        OFS30                              = (0x60, 0x40000000, 30)
        OFS31                              = (0x60, 0x80000000, 31)

        # MSLUT[1]
        OFS32                              = (0x61, 0x00000001,  0)
        OFS33                              = (0x61, 0x00000002,  1)
        OFS34                              = (0x61, 0x00000004,  2)
        OFS35                              = (0x61, 0x00000008,  3)
        OFS36                              = (0x61, 0x00000010,  4)
        OFS37                              = (0x61, 0x00000020,  5)
        OFS38                              = (0x61, 0x00000040,  6)
        OFS39                              = (0x61, 0x00000080,  7)
        OFS40                              = (0x61, 0x00000100,  8)
        OFS41                              = (0x61, 0x00000200,  9)
        OFS42                              = (0x61, 0x00000400, 10)
        OFS43                              = (0x61, 0x00000800, 11)
        OFS44                              = (0x61, 0x00001000, 12)
        OFS45                              = (0x61, 0x00002000, 13)
        OFS46                              = (0x61, 0x00004000, 14)
        OFS47                              = (0x61, 0x00008000, 15)
        OFS48                              = (0x61, 0x00010000, 16)
        OFS49                              = (0x61, 0x00020000, 17)
        OFS50                              = (0x61, 0x00040000, 18)
        OFS51                              = (0x61, 0x00080000, 19)
        OFS52                              = (0x61, 0x00100000, 20)
        OFS53                              = (0x61, 0x00200000, 21)
        OFS54                              = (0x61, 0x00400000, 22)
        OFS55                              = (0x61, 0x00800000, 23)
        OFS56                              = (0x61, 0x01000000, 24)
        OFS57                              = (0x61, 0x02000000, 25)
        OFS58                              = (0x61, 0x04000000, 26)
        OFS59                              = (0x61, 0x08000000, 27)
        OFS60                              = (0x61, 0x10000000, 28)
        OFS61                              = (0x61, 0x20000000, 29)
        OFS62                              = (0x61, 0x40000000, 30)
        OFS63                              = (0x61, 0x80000000, 31)

        # MSLUT[2]
        OFS64                              = (0x62, 0x00000001,  0)
        OFS65                              = (0x62, 0x00000002,  1)
        OFS66                              = (0x62, 0x00000004,  2)
        OFS67                              = (0x62, 0x00000008,  3)
        OFS68                              = (0x62, 0x00000010,  4)
        OFS69                              = (0x62, 0x00000020,  5)
        OFS70                              = (0x62, 0x00000040,  6)
        OFS71                              = (0x62, 0x00000080,  7)
        OFS72                              = (0x62, 0x00000100,  8)
        OFS73                              = (0x62, 0x00000200,  9)
        OFS74                              = (0x62, 0x00000400, 10)
        OFS75                              = (0x62, 0x00000800, 11)
        OFS76                              = (0x62, 0x00001000, 12)
        OFS77                              = (0x62, 0x00002000, 13)
        OFS78                              = (0x62, 0x00004000, 14)
        OFS79                              = (0x62, 0x00008000, 15)
        OFS80                              = (0x62, 0x00010000, 16)
        OFS81                              = (0x62, 0x00020000, 17)
        OFS82                              = (0x62, 0x00040000, 18)
        OFS83                              = (0x62, 0x00080000, 19)
        OFS84                              = (0x62, 0x00100000, 20)
        OFS85                              = (0x62, 0x00200000, 21)
        OFS86                              = (0x62, 0x00400000, 22)
        OFS87                              = (0x62, 0x00800000, 23)
        OFS88                              = (0x62, 0x01000000, 24)
        OFS89                              = (0x62, 0x02000000, 25)
        OFS90                              = (0x62, 0x04000000, 26)
        OFS91                              = (0x62, 0x08000000, 27)
        OFS92                              = (0x62, 0x10000000, 28)
        OFS93                              = (0x62, 0x20000000, 29)
        OFS94                              = (0x62, 0x40000000, 30)
        OFS95                              = (0x62, 0x80000000, 31)

        # MSLUT[3]
        OFS96                              = (0x63, 0x00000001,  0)
        OFS97                              = (0x63, 0x00000002,  1)
        OFS98                              = (0x63, 0x00000004,  2)
        OFS99                              = (0x63, 0x00000008,  3)
        OFS100                             = (0x63, 0x00000010,  4)
        OFS101                             = (0x63, 0x00000020,  5)
        OFS102                             = (0x63, 0x00000040,  6)
        OFS103                             = (0x63, 0x00000080,  7)
        OFS104                             = (0x63, 0x00000100,  8)
        OFS105                             = (0x63, 0x00000200,  9)
        OFS106                             = (0x63, 0x00000400, 10)
        OFS107                             = (0x63, 0x00000800, 11)
        OFS108                             = (0x63, 0x00001000, 12)
        OFS109                             = (0x63, 0x00002000, 13)
        OFS110                             = (0x63, 0x00004000, 14)
        OFS111                             = (0x63, 0x00008000, 15)
        OFS112                             = (0x63, 0x00010000, 16)
        OFS113                             = (0x63, 0x00020000, 17)
        OFS114                             = (0x63, 0x00040000, 18)
        OFS115                             = (0x63, 0x00080000, 19)
        OFS116                             = (0x63, 0x00100000, 20)
        OFS117                             = (0x63, 0x00200000, 21)
        OFS118                             = (0x63, 0x00400000, 22)
        OFS119                             = (0x63, 0x00800000, 23)
        OFS120                             = (0x63, 0x01000000, 24)
        OFS121                             = (0x63, 0x02000000, 25)
        OFS122                             = (0x63, 0x04000000, 26)
        OFS123                             = (0x63, 0x08000000, 27)
        OFS124                             = (0x63, 0x10000000, 28)
        OFS125                             = (0x63, 0x20000000, 29)
        OFS126                             = (0x63, 0x40000000, 30)
        OFS127                             = (0x63, 0x80000000, 31)

        # MSLUT[4]
        OFS128                             = (0x64, 0x00000001,  0)
        OFS129                             = (0x64, 0x00000002,  1)
        OFS130                             = (0x64, 0x00000004,  2)
        OFS131                             = (0x64, 0x00000008,  3)
        OFS132                             = (0x64, 0x00000010,  4)
        OFS133                             = (0x64, 0x00000020,  5)
        OFS134                             = (0x64, 0x00000040,  6)
        OFS135                             = (0x64, 0x00000080,  7)
        OFS136                             = (0x64, 0x00000100,  8)
        OFS137                             = (0x64, 0x00000200,  9)
        OFS138                             = (0x64, 0x00000400, 10)
        OFS139                             = (0x64, 0x00000800, 11)
        OFS140                             = (0x64, 0x00001000, 12)
        OFS141                             = (0x64, 0x00002000, 13)
        OFS142                             = (0x64, 0x00004000, 14)
        OFS143                             = (0x64, 0x00008000, 15)
        OFS144                             = (0x64, 0x00010000, 16)
        OFS145                             = (0x64, 0x00020000, 17)
        OFS146                             = (0x64, 0x00040000, 18)
        OFS147                             = (0x64, 0x00080000, 19)
        OFS148                             = (0x64, 0x00100000, 20)
        OFS149                             = (0x64, 0x00200000, 21)
        OFS150                             = (0x64, 0x00400000, 22)
        OFS151                             = (0x64, 0x00800000, 23)
        OFS152                             = (0x64, 0x01000000, 24)
        OFS153                             = (0x64, 0x02000000, 25)
        OFS154                             = (0x64, 0x04000000, 26)
        OFS155                             = (0x64, 0x08000000, 27)
        OFS156                             = (0x64, 0x10000000, 28)
        OFS157                             = (0x64, 0x20000000, 29)
        OFS158                             = (0x64, 0x40000000, 30)
        OFS159                             = (0x64, 0x80000000, 31)

        # MSLUT[5]
        OFS160                             = (0x65, 0x00000001,  0)
        OFS161                             = (0x65, 0x00000002,  1)
        OFS162                             = (0x65, 0x00000004,  2)
        OFS163                             = (0x65, 0x00000008,  3)
        OFS164                             = (0x65, 0x00000010,  4)
        OFS165                             = (0x65, 0x00000020,  5)
        OFS166                             = (0x65, 0x00000040,  6)
        OFS167                             = (0x65, 0x00000080,  7)
        OFS168                             = (0x65, 0x00000100,  8)
        OFS169                             = (0x65, 0x00000200,  9)
        OFS170                             = (0x65, 0x00000400, 10)
        OFS171                             = (0x65, 0x00000800, 11)
        OFS172                             = (0x65, 0x00001000, 12)
        OFS173                             = (0x65, 0x00002000, 13)
        OFS174                             = (0x65, 0x00004000, 14)
        OFS175                             = (0x65, 0x00008000, 15)
        OFS176                             = (0x65, 0x00010000, 16)
        OFS177                             = (0x65, 0x00020000, 17)
        OFS178                             = (0x65, 0x00040000, 18)
        OFS179                             = (0x65, 0x00080000, 19)
        OFS180                             = (0x65, 0x00100000, 20)
        OFS181                             = (0x65, 0x00200000, 21)
        OFS182                             = (0x65, 0x00400000, 22)
        OFS183                             = (0x65, 0x00800000, 23)
        OFS184                             = (0x65, 0x01000000, 24)
        OFS185                             = (0x65, 0x02000000, 25)
        OFS186                             = (0x65, 0x04000000, 26)
        OFS187                             = (0x65, 0x08000000, 27)
        OFS188                             = (0x65, 0x10000000, 28)
        OFS189                             = (0x65, 0x20000000, 29)
        OFS190                             = (0x65, 0x40000000, 30)
        OFS191                             = (0x65, 0x80000000, 31)

        # MSLUT[6]
        OFS192                             = (0x66, 0x00000001,  0)
        OFS193                             = (0x66, 0x00000002,  1)
        OFS194                             = (0x66, 0x00000004,  2)
        OFS195                             = (0x66, 0x00000008,  3)
        OFS196                             = (0x66, 0x00000010,  4)
        OFS197                             = (0x66, 0x00000020,  5)
        OFS198                             = (0x66, 0x00000040,  6)
        OFS199                             = (0x66, 0x00000080,  7)
        OFS200                             = (0x66, 0x00000100,  8)
        OFS201                             = (0x66, 0x00000200,  9)
        OFS202                             = (0x66, 0x00000400, 10)
        OFS203                             = (0x66, 0x00000800, 11)
        OFS204                             = (0x66, 0x00001000, 12)
        OFS205                             = (0x66, 0x00002000, 13)
        OFS206                             = (0x66, 0x00004000, 14)
        OFS207                             = (0x66, 0x00008000, 15)
        OFS208                             = (0x66, 0x00010000, 16)
        OFS209                             = (0x66, 0x00020000, 17)
        OFS210                             = (0x66, 0x00040000, 18)
        OFS211                             = (0x66, 0x00080000, 19)
        OFS212                             = (0x66, 0x00100000, 20)
        OFS213                             = (0x66, 0x00200000, 21)
        OFS214                             = (0x66, 0x00400000, 22)
        OFS215                             = (0x66, 0x00800000, 23)
        OFS216                             = (0x66, 0x01000000, 24)
        OFS217                             = (0x66, 0x02000000, 25)
        OFS218                             = (0x66, 0x04000000, 26)
        OFS219                             = (0x66, 0x08000000, 27)
        OFS220                             = (0x66, 0x10000000, 28)
        OFS221                             = (0x66, 0x20000000, 29)
        OFS222                             = (0x66, 0x40000000, 30)
        OFS223                             = (0x66, 0x80000000, 31)

        # MSLUT[7]
        OFS224                             = (0x67, 0x00000001,  0)
        OFS225                             = (0x67, 0x00000002,  1)
        OFS226                             = (0x67, 0x00000004,  2)
        OFS227                             = (0x67, 0x00000008,  3)
        OFS228                             = (0x67, 0x00000010,  4)
        OFS229                             = (0x67, 0x00000020,  5)
        OFS230                             = (0x67, 0x00000040,  6)
        OFS231                             = (0x67, 0x00000080,  7)
        OFS232                             = (0x67, 0x00000100,  8)
        OFS233                             = (0x67, 0x00000200,  9)
        OFS234                             = (0x67, 0x00000400, 10)
        OFS235                             = (0x67, 0x00000800, 11)
        OFS236                             = (0x67, 0x00001000, 12)
        OFS237                             = (0x67, 0x00002000, 13)
        OFS238                             = (0x67, 0x00004000, 14)
        OFS239                             = (0x67, 0x00008000, 15)
        OFS240                             = (0x67, 0x00010000, 16)
        OFS241                             = (0x67, 0x00020000, 17)
        OFS242                             = (0x67, 0x00040000, 18)
        OFS243                             = (0x67, 0x00080000, 19)
        OFS244                             = (0x67, 0x00100000, 20)
        OFS245                             = (0x67, 0x00200000, 21)
        OFS246                             = (0x67, 0x00400000, 22)
        OFS247                             = (0x67, 0x00800000, 23)
        OFS248                             = (0x67, 0x01000000, 24)
        OFS249                             = (0x67, 0x02000000, 25)
        OFS250                             = (0x67, 0x04000000, 26)
        OFS251                             = (0x67, 0x08000000, 27)
        OFS252                             = (0x67, 0x10000000, 28)
        OFS253                             = (0x67, 0x20000000, 29)
        OFS254                             = (0x67, 0x40000000, 30)
        OFS255                             = (0x67, 0x80000000, 31)

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
