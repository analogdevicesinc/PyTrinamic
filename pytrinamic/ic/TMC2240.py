from ..ic.tmc_ic import TMCIc


class TMC2240(TMCIc):
    """
    The TMC2240-A is a stepper motor controller and driver IC with serial communication interfaces.
    Supply voltage: 4.5-36V.
    """
    def __init__(self):
        super().__init__("TMC2240", self.__doc__)

    class REG:
        """
        Define all registers of the TMC2240.
        """
        GCONF            = 0x00
        GSTAT            = 0x01
        IFCNT            = 0x02
        SLAVECONF        = 0x03
        IOIN             = 0x04
        DRV_CONF         = 0x0A
        GLOBAL_SCALER    = 0x0B
        IHOLD_IRUN       = 0x10
        TPOWERDOWN       = 0x11
        TSTEP            = 0x12
        TPWMTHRS         = 0x13
        TCOOLTHRS        = 0x14
        THIGH            = 0x15
        DIRECT_MODE      = 0x2D
        ENCMODE          = 0x38
        X_ENC            = 0x39
        ENC_CONST        = 0x3A
        ENC_STATUS       = 0x3B
        ENC_LATCH        = 0x3C
        ADC_VSUPPLY_AIN  = 0x50
        ADC_TEMP         = 0x51
        OTW_OV_VTH       = 0x52
        MSLUT_0          = 0x60
        MSLUT_1          = 0x61
        MSLUT_2          = 0x62
        MSLUT_3          = 0x63
        MSLUT_4          = 0x64
        MSLUT_5          = 0x65
        MSLUT_6          = 0x66
        MSLUT_7          = 0x67
        MSLUTSEL         = 0x68
        MSLUTSTART       = 0x69
        MSCNT            = 0x6A
        MSCURACT         = 0x6B
        CHOPCONF         = 0x6C
        COOLCONF         = 0x6D
        DCCTRL           = 0x6E
        DRV_STATUS       = 0x6F
        PWMCONF          = 0x70
        PWM_SCALE        = 0x71
        PWM_AUTO         = 0x72
        SG4_THRS         = 0x74
        SG4_RESULT       = 0x75
        SG4_IND          = 0x76

    class FIELD:
        """
        Define all register bitfields of the TMC2240.

        Each field is defined as a tuple consisting of ( Address, Mask, Shift ).

        The name of the register is written as a comment behind each tuple. This is
        intended for IDE users viewing the definition of a field by hovering over
        it. This allows the user to see the corresponding register name of a field
        without opening this file and searching for the definition.
        """

        FAST_STANDSTILL         = ( 0x00, 0x00000002,  1 )
        EN_PWM_MODE             = ( 0x00, 0x00000004,  2 )
        MULTISTEP_FILT          = ( 0x00, 0x00000008,  3 )
        SHAFT                   = ( 0x00, 0x00000010,  4 )
        DIAG0_ERROR             = ( 0x00, 0x00000020,  5 )
        DIAG0_OTPW              = ( 0x00, 0x00000040,  6 )
        DIAG0_STALL             = ( 0x00, 0x00000080,  7 )
        DIAG1_STALL             = ( 0x00, 0x00000100,  8 )
        DIAG1_INDEX             = ( 0x00, 0x00000200,  9 )
        DIAG1_ONSTATE           = ( 0x00, 0x00000400, 10 )
        DIAG0_PUSHPULL          = ( 0x00, 0x00001000, 12 )
        DIAG1_PUSHPULL          = ( 0x00, 0x00002000, 13 )
        SMALL_HYSTERESIS        = ( 0x00, 0x00004000, 14 )
        STOP_ENABLE             = ( 0x00, 0x00008000, 15 )
        DIRECT_MODE             = ( 0x00, 0x00010000, 16 )
        RESET                   = ( 0x01, 0x00000001,  0 )
        DRV_ERR                 = ( 0x01, 0x00000002,  1 )
        UV_CP                   = ( 0x01, 0x00000004,  2 )
        REGISTER_RESET          = ( 0x01, 0x00000008,  3 )
        VM_UVLO                 = ( 0x01, 0x00000010,  4 )
        IFCNT                   = ( 0x02, 0x000000FF,  0 )
        SLAVEADDR               = ( 0x03, 0x000000FF,  0 )
        SENDDELAY               = ( 0x03, 0x00000F00,  8 )
        REFL_STEP               = ( 0x04, 0x00000001,  0 )
        REFR_DIR                = ( 0x04, 0x00000002,  1 )
        ENCB_CFG4               = ( 0x04, 0x00000004,  2 )
        ENCA_CFG5               = ( 0x04, 0x00000008,  3 )
        DRV_ENN                 = ( 0x04, 0x00000010,  4 )
        ENCN_CFG6               = ( 0x04, 0x00000020,  5 )
        UART_EN                 = ( 0x04, 0x00000040,  6 )
        RESERVED                = ( 0x04, 0x00000080,  7 )
        COMP_A                  = ( 0x04, 0x00000100,  8 )
        COMP_B                  = ( 0x04, 0x00000200,  9 )
        COMP_A1_A2              = ( 0x04, 0x00000400, 10 )
        COMP_B1_B2              = ( 0x04, 0x00000800, 11 )
        OUTPUT                  = ( 0x04, 0x00001000, 12 )
        EXT_RES_DET             = ( 0x04, 0x00002000, 13 )
        EXT_CLK                 = ( 0x04, 0x00004000, 14 )
        ADC_ERR                 = ( 0x04, 0x00008000, 15 )
        SILICON_RV              = ( 0x04, 0x00070000, 16 )
        VERSION                 = ( 0x04, 0xFF000000, 24 )
        CURRENT_RANGE           = ( 0x0A, 0x00000003,  0 )
        SLOPE_CONTROL           = ( 0x0A, 0x00000030,  4 )
        GLOBALSCALER            = ( 0x0B, 0x000000FF,  0 )
        IHOLD                   = ( 0x10, 0x0000001F,  0 )
        IRUN                    = ( 0x10, 0x00001F00,  8 )
        IHOLDDELAY              = ( 0x10, 0x000F0000, 16 )
        IRUNDELAY               = ( 0x10, 0x0F000000, 24 )
        TPOWERDOWN              = ( 0x11, 0x000000FF,  0 )
        TSTEP                   = ( 0x12, 0x000FFFFF,  0 )
        TPWMTHRS                = ( 0x13, 0x000FFFFF,  0 )
        TCOOLTHRS               = ( 0x14, 0x000FFFFF,  0 )
        THIGH                   = ( 0x15, 0x000FFFFF,  0 )
        DIRECT_COIL_A           = ( 0x2D, 0x000001FF,  0 )
        DIRECT_COIL_B           = ( 0x2D, 0x01FF0000, 16 )
        POL_A                   = ( 0x38, 0x00000001,  0 )
        POL_B                   = ( 0x38, 0x00000002,  1 )
        POL_N                   = ( 0x38, 0x00000004,  2 )
        IGNORE_AB               = ( 0x38, 0x00000008,  3 )
        CLR_CONT                = ( 0x38, 0x00000010,  4 )
        CLR_ONCE                = ( 0x38, 0x00000020,  5 )
        POS_NEG_EDGE            = ( 0x38, 0x000000C0,  6 )
        CLR_ENC_X               = ( 0x38, 0x00000100,  8 )
        LATCH_X_ACT             = ( 0x38, 0x00000200,  9 )
        ENC_SEL_DECIMAL         = ( 0x38, 0x00000400, 10 )
        X_ENC                   = ( 0x39, 0xFFFFFFFF,  0 )
        ENC_CONST               = ( 0x3A, 0xFFFFFFFF,  0 )
        N_EVENT                 = ( 0x3B, 0x00000001,  0 )
        DEVIATION_WARN          = ( 0x3B, 0x00000002,  1 )
        ENC_LATCH               = ( 0x3C, 0xFFFFFFFF,  0 )
        ADC_VSUPPLY             = ( 0x50, 0x00001FFF,  0 )
        ADC_AIN                 = ( 0x50, 0x1FFF0000, 16 )
        ADC_TEMP                = ( 0x51, 0x00001FFF,  0 )
        #RESERVED                = ( 0x51, 0x1FFF0000, 16 )
        OVERVOLTAGE_VTH         = ( 0x52, 0x00001FFF,  0 )
        OVERTEMPPREWARNING_VTH  = ( 0x52, 0x1FFF0000, 16 )
        MSLUT__                 = ( 0x60, 0xFFFFFFFF,  0 )
        #MSLUT__                 = ( 0x61, 0xFFFFFFFF,  0 )
        #MSLUT__                 = ( 0x62, 0xFFFFFFFF,  0 )
        #MSLUT__                 = ( 0x63, 0xFFFFFFFF,  0 )
        #MSLUT__                 = ( 0x64, 0xFFFFFFFF,  0 )
        #MSLUT__                 = ( 0x65, 0xFFFFFFFF,  0 )
        #MSLUT__                 = ( 0x66, 0xFFFFFFFF,  0 )
        #MSLUT__                 = ( 0x67, 0xFFFFFFFF,  0 )
        W0                      = ( 0x68, 0x00000003,  0 )
        W1                      = ( 0x68, 0x0000000C,  2 )
        W2                      = ( 0x68, 0x00000030,  4 )
        W3                      = ( 0x68, 0x000000C0,  6 )
        X1                      = ( 0x68, 0x0000FF00,  8 )
        X2                      = ( 0x68, 0x00FF0000, 16 )
        X3                      = ( 0x68, 0xFF000000, 24 )
        START_SIN               = ( 0x69, 0x000000FF,  0 )
        START_SIN90             = ( 0x69, 0x00FF0000, 16 )
        OFFSET_SIN90            = ( 0x69, 0xFF000000, 24 )
        MSCNT                   = ( 0x6A, 0x000003FF,  0 )
        CUR_B                   = ( 0x6B, 0x000001FF,  0 )
        CUR_A                   = ( 0x6B, 0x01FF0000, 16 )
        TOFF                    = ( 0x6C, 0x0000000F,  0 )
        HSTRT_TFD210            = ( 0x6C, 0x00000070,  4 )
        HEND_OFFSET             = ( 0x6C, 0x00000780,  7 )
        FD3                     = ( 0x6C, 0x00000800, 11 )
        DISFDCC                 = ( 0x6C, 0x00001000, 12 )
        CHM                     = ( 0x6C, 0x00004000, 14 )
        TBL                     = ( 0x6C, 0x00018000, 15 )
        VHIGHFS                 = ( 0x6C, 0x00040000, 18 )
        VHIGHCHM                = ( 0x6C, 0x00080000, 19 )
        TPFD                    = ( 0x6C, 0x00F00000, 20 )
        MRES                    = ( 0x6C, 0x0F000000, 24 )
        INTPOL                  = ( 0x6C, 0x10000000, 28 )
        DEDGE                   = ( 0x6C, 0x20000000, 29 )
        DISS2G                  = ( 0x6C, 0x40000000, 30 )
        DISS2VS                 = ( 0x6C, 0x80000000, 31 )
        SEMIN                   = ( 0x6D, 0x0000000F,  0 )
        SEUP                    = ( 0x6D, 0x00000060,  5 )
        SEMAX                   = ( 0x6D, 0x00000F00,  8 )
        SEDN                    = ( 0x6D, 0x00006000, 13 )
        SEIMIN                  = ( 0x6D, 0x00008000, 15 )
        SGT                     = ( 0x6D, 0x007F0000, 16 )
        SFILT                   = ( 0x6D, 0x01000000, 24 )
        DC_TIME                 = ( 0x6E, 0x000003FF,  0 )
        DC_SG                   = ( 0x6E, 0x00FF0000, 16 )
        SG_RESULT               = ( 0x6F, 0x000003FF,  0 )
        S2VSA                   = ( 0x6F, 0x00001000, 12 )
        S2VSB                   = ( 0x6F, 0x00002000, 13 )
        STEALTH                 = ( 0x6F, 0x00004000, 14 )
        FSACTIVE                = ( 0x6F, 0x00008000, 15 )
        CS_ACTUAL               = ( 0x6F, 0x001F0000, 16 )
        STALLGUARD              = ( 0x6F, 0x01000000, 24 )
        OT                      = ( 0x6F, 0x02000000, 25 )
        OTPW                    = ( 0x6F, 0x04000000, 26 )
        S2GA                    = ( 0x6F, 0x08000000, 27 )
        S2GB                    = ( 0x6F, 0x10000000, 28 )
        OLA                     = ( 0x6F, 0x20000000, 29 )
        OLB                     = ( 0x6F, 0x40000000, 30 )
        STST                    = ( 0x6F, 0x80000000, 31 )
        PWM_OFS                 = ( 0x70, 0x000000FF,  0 )
        PWM_GRAD                = ( 0x70, 0x0000FF00,  8 )
        PWM_FREQ                = ( 0x70, 0x00030000, 16 )
        PWM_AUTOSCALE           = ( 0x70, 0x00040000, 18 )
        PWM_AUTOGRAD            = ( 0x70, 0x00080000, 19 )
        FREEWHEEL               = ( 0x70, 0x00300000, 20 )
        PWM_MEAS_SD_ENABLE      = ( 0x70, 0x00400000, 22 )
        PWM_DIS_REG_STST        = ( 0x70, 0x00800000, 23 )
        PWM_REG                 = ( 0x70, 0x0F000000, 24 )
        PWM_LIM                 = ( 0x70, 0xF0000000, 28 )
        PWM_SCALE_SUM           = ( 0x71, 0x000003FF,  0 )
        PWM_SCALE_AUTO          = ( 0x71, 0x01FF0000, 16 )
        PWM_OFS_AUTO            = ( 0x72, 0x000000FF,  0 )
        PWM_GRAD_AUTO           = ( 0x72, 0x00FF0000, 16 )
        SG4_THRS                = ( 0x74, 0x000000FF,  0 )
        SG4_FILT_EN             = ( 0x74, 0x00000100,  8 )
        SG_ANGLE_OFFSET         = ( 0x74, 0x00000200,  9 )
        SG4_RESULT              = ( 0x75, 0x000003FF,  0 )
        SG4_IND_0               = ( 0x76, 0x000000FF,  0 )
        SG4_IND_1               = ( 0x76, 0x0000FF00,  8 )
        SG4_IND_2               = ( 0x76, 0x00FF0000, 16 )
        SG4_IND_3               = ( 0x76, 0xFF000000, 24 )