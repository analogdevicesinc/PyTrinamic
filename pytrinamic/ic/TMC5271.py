################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from ..ic.tmc_ic import TMCIc
from ..features.motor_control_ic import MotorControlIc


class TMC5271(TMCIc):
    """
    The TMC5271 is a smart high-performance single-axis stepper motor controller and driver IC
    with serial communication interfaces (SPI and UART). Supply voltage: 2.1-20V DC.
    """
    def __init__(self, parent_eval):
        super().__init__(self.__class__.__name__, self.__doc__)
        self._parent = parent_eval
        self.motors = [self.MotorTypeA(parent_eval, self, 0)]

    class MotorTypeA(MotorControlIc):
        """
        Motor class for the generic motor.
        """
        def __init__(self, parent_eval, ic, axis):
            MotorControlIc.__init__(self, parent_eval, ic, axis)

    class REG:
        """
        Define all registers of the TMC5271.
        """
        GCONF             = 0x00
        GSTAT             = 0x01
        IFCNT             = 0x02
        SLAVECONF         = 0x03
        IOIN              = 0x04
        DRV_CONF          = 0x05
        GLOBAL_SCALER     = 0x06
        RAMPMODE          = 0x07
        MSLUT_ADDR        = 0x08
        MSLUT_DATA        = 0x09
        X_COMPARE         = 0x10
        X_COMPARE_REPEAT  = 0x11
        IHOLD_IRUN        = 0x12
        TPOWERDOWN        = 0x13
        TSTEP             = 0x14
        TPWMTHRS          = 0x15
        TCOOLTHRS         = 0x16
        THIGH             = 0x17
        XACTUAL           = 0x18
        VACTUAL           = 0x19
        AACTUAL           = 0x1A
        VSTART            = 0x1B
        A1                = 0x1C
        V1                = 0x1D
        A2                = 0x1E
        V2                = 0x1F
        AMAX              = 0x20
        VMAX              = 0x21
        DMAX              = 0x22
        D2                = 0x23
        D1                = 0x24
        VSTOP             = 0x25
        TVMAX             = 0x26
        TZEROWAIT         = 0x27
        XTARGET           = 0x28
        VDCMIN            = 0x29
        SW_MODE           = 0x2A
        RAMP_STAT         = 0x2B
        XLATCH            = 0x2C
        POSITION_PI_CTRL  = 0x2D
        X_ENC             = 0x2E
        ENCMODE           = 0x2F
        ENC_CONST         = 0x30
        ENC_STATUS        = 0x31
        ENC_LATCH         = 0x32
        ENC_DEVIATION     = 0x33
        VIRTUAL_STOP_L    = 0x34
        VIRTUAL_STOP_R    = 0x35
        MSCNT             = 0x36
        MSCURACT          = 0x37
        CHOPCONF          = 0x38
        COOLCONF          = 0x39
        DCCTRL            = 0x3A
        DRV_STATUS        = 0x3B
        PWMCONF           = 0x3C
        PWM_SCALE         = 0x3D
        PWM_AUTO          = 0x3E
        SG4_THRS          = 0x3F
        SG4_RESULT        = 0x40
        SG4_IND           = 0x41

    class FIELD:
        """
        Define all register bitfields of the TMC5271.

        Each field is defined as a tuple consisting of ( Address, Mask, Shift ).

        The name of the register is written as a comment behind each tuple. This is
        intended for IDE users viewing the definition of a field by hovering over
        it. This allows the user to see the corresponding register name of a field
        without opening this file and searching for the definition.
        """
        EN_PWM_MODE                = ( 0x00, 0x00000001,  0 )
        MULTISTEP_FILT             = ( 0x00, 0x00000002,  1 )
        SHAFT                      = ( 0x00, 0x00000004,  2 )
        DIAG0_ERROR                = ( 0x00, 0x00000008,  3 )
        DIAG0_OTPW                 = ( 0x00, 0x00000010,  4 )
        DIAG0_STALL_STEP           = ( 0x00, 0x00000020,  5 )
        DIAG1_STALL_DIR            = ( 0x00, 0x00000040,  6 )
        DIAG1_INDEX                = ( 0x00, 0x00000080,  7 )
        DIAG0_INT_PUSHPULL         = ( 0x00, 0x00000100,  8 )
        DIAG1_POSCOMP_PUSHPULL     = ( 0x00, 0x00000200,  9 )
        SMALL_HYSTERESIS           = ( 0x00, 0x00000400, 10 )
        STOP_ENABLE                = ( 0x00, 0x00000800, 11 )
        DIRECT_MODE                = ( 0x00, 0x00001000, 12 )
        SD                         = ( 0x00, 0x00002000, 13 )
        DRV_ENN                    = ( 0x00, 0x00004000, 14 )
        QSC_STS_ENA                = ( 0x00, 0x00008000, 15 )
        DIAG0_SEL_nERROR_RAMP      = ( 0x00, 0x20000000, 29 )
        RESET                      = ( 0x01, 0x00000001,  0 )
        DRV_ERR                    = ( 0x01, 0x00000002,  1 )
        UV_LDO                     = ( 0x01, 0x00000004,  2 )
        REGISTER_RESET             = ( 0x01, 0x00000008,  3 )
        VM_UVLO                    = ( 0x01, 0x00000010,  4 )
        IFCNT                      = ( 0x02, 0x000000FF,  0 )
        SLAVEADDR                  = ( 0x03, 0x000000FF,  0 )
        SENDDELAY                  = ( 0x03, 0x00000F00,  8 )
        ADC_TEMPERATURE            = ( 0x04, 0x000001FE,  1 )
        ADC_EN                     = ( 0x04, 0x00000200,  9 )
        SEL_OSCILLATOR             = ( 0x04, 0x00000800, 11 )
        EXT_RES_DET                = ( 0x04, 0x00001000, 12 )
        OUTPUT                     = ( 0x04, 0x00002000, 13 )
        QSC_STATUS                 = ( 0x04, 0x00008000, 15 )
        SILICON_RV                 = ( 0x04, 0x00070000, 16 )
        VERSION                    = ( 0x04, 0xFF000000, 24 )
        FSR                        = ( 0x05, 0x00000003,  0 )
        FSR_IREF                   = ( 0x05, 0x0000000C,  2 )
        EN_EMERGENCY_DISABLE       = ( 0x05, 0x00000010,  4 )
        STANDSTILL_TIME            = ( 0x05, 0x00070000, 16 )
        GLOBALSCALER_A             = ( 0x06, 0x000000FF,  0 )
        GLOBALSCALER_B             = ( 0x06, 0x0000FF00,  8 )
        RAMPMODE                   = ( 0x07, 0x00000003,  0 )
        MSLUT_ADDR                 = ( 0x08, 0x0000001F,  0 )
        MSLUT_DATA                 = ( 0x09, 0xFFFFFFFF,  0 )
        X_COMPARE                  = ( 0x10, 0xFFFFFFFF,  0 )
        X_COMPARE_REPEAT           = ( 0x11, 0x00FFFFFF,  0 )
        IHOLD                      = ( 0x12, 0x0000001F,  0 )
        IRUN                       = ( 0x12, 0x00001F00,  8 )
        IHOLDDELAY                 = ( 0x12, 0x000F0000, 16 )
        IRUNDELAY                  = ( 0x12, 0x0F000000, 24 )
        TPOWERDOWN                 = ( 0x13, 0x000000FF,  0 )
        TSTEP                      = ( 0x14, 0x000FFFFF,  0 )
        TPWMTHRS                   = ( 0x15, 0x000FFFFF,  0 )
        TCOOLTHRS                  = ( 0x16, 0x000FFFFF,  0 )
        THIGH                      = ( 0x17, 0x000FFFFF,  0 )
        XACTUAL                    = ( 0x18, 0xFFFFFFFF,  0 )
        VACTUAL                    = ( 0x19, 0x00FFFFFF,  0 )
        AACTUAL                    = ( 0x1A, 0x00FFFFFF,  0 )
        VSTART                     = ( 0x1B, 0x0003FFFF,  0 )
        A1                         = ( 0x1C, 0x0003FFFF,  0 )
        V1                         = ( 0x1D, 0x000FFFFF,  0 )
        A2                         = ( 0x1E, 0x0003FFFF,  0 )
        V2                         = ( 0x1F, 0x000FFFFF,  0 )
        AMAX                       = ( 0x20, 0x0003FFFF,  0 )
        VMAX                       = ( 0x21, 0x007FFFFF,  0 )
        DMAX                       = ( 0x22, 0x0003FFFF,  0 )
        D2                         = ( 0x23, 0x0003FFFF,  0 )
        D1                         = ( 0x24, 0x0003FFFF,  0 )
        VSTOP                      = ( 0x25, 0x0003FFFF,  0 )
        TVMAX                      = ( 0x26, 0x0000FFFF,  0 )
        TZEROWAIT                  = ( 0x27, 0x0000FFFF,  0 )
        XTARGET                    = ( 0x28, 0xFFFFFFFF,  0 )
        VDCMIN_RESERVED            = ( 0x29, 0x000000FF,  0 )
        VDCMIN_VDCMIN              = ( 0x29, 0x007FFF00,  8 )
        SW_MODE_STOP_L_ENABLE      = ( 0x2A, 0x00000001,  0 )
        SW_MODE_STOP_R_ENABLE      = ( 0x2A, 0x00000002,  1 )
        SW_MODE_POL_STOP_L         = ( 0x2A, 0x00000004,  2 )
        SW_MODE_POL_STOP_R         = ( 0x2A, 0x00000008,  3 )
        SW_MODE_SWAP_LR            = ( 0x2A, 0x00000010,  4 )
        SW_MODE_LATCH_L_ACTIVE     = ( 0x2A, 0x00000020,  5 )
        SW_MODE_LATCH_L_INACTIVE   = ( 0x2A, 0x00000040,  6 )
        SW_MODE_LATCH_R_ACTIVE     = ( 0x2A, 0x00000080,  7 )
        SW_MODE_LATCH_R_INACTIVE   = ( 0x2A, 0x00000100,  8 )
        SW_MODE_EN_LATCH_ENCODER   = ( 0x2A, 0x00000200,  9 )
        SG_STOP                    = ( 0x2A, 0x00000400, 10 )
        SW_MODE_EN_SOFTSTOP        = ( 0x2A, 0x00000800, 11 )
        SW_MODE_EN_VIRTUAL_STOP_L  = ( 0x2A, 0x00001000, 12 )
        SW_MODE_EN_VIRTUAL_STOP_R  = ( 0x2A, 0x00002000, 13 )
        SW_MODE_VIRTUAL_STEP_ENC   = ( 0x2A, 0x00004000, 14 )
        STATUS_STOP_L              = ( 0x2B, 0x00000001,  0 )
        STATUS_STOP_R              = ( 0x2B, 0x00000002,  1 )
        STATUS_LATCH_L             = ( 0x2B, 0x00000004,  2 )
        STATUS_LATCH_R             = ( 0x2B, 0x00000008,  3 )
        EVENT_STOP_L               = ( 0x2B, 0x00000010,  4 )
        EVENT_STOP_R               = ( 0x2B, 0x00000020,  5 )
        EVENT_STOP_SG              = ( 0x2B, 0x00000040,  6 )
        EVENT_POS_REACHED          = ( 0x2B, 0x00000080,  7 )
        VELOCITY_REACHED           = ( 0x2B, 0x00000100,  8 )
        POSITION_REACHED           = ( 0x2B, 0x00000200,  9 )
        VZERO                      = ( 0x2B, 0x00000400, 10 )
        T_ZEROWAIT_ACTIVE          = ( 0x2B, 0x00000800, 11 )
        SECOND_MOVE                = ( 0x2B, 0x00001000, 12 )
        STATUS_SG                  = ( 0x2B, 0x00002000, 13 )
        STATUS_VIRTUAL_STOP_L      = ( 0x2B, 0x00004000, 14 )
        STATUS_VIRTUAL_STOP_R      = ( 0x2B, 0x00008000, 15 )
        XLATCH                     = ( 0x2C, 0xFFFFFFFF,  0 )
        P_POSITION                 = ( 0x2D, 0x000003FF,  0 )
        TOLERANCE                  = ( 0x2D, 0x00FF0000, 16 )
        TOL_ON_POS_REACHED         = ( 0x2D, 0x10000000, 28 )
        X_ENC                      = ( 0x2E, 0xFFFFFFFF,  0 )
        POL_A                      = ( 0x2F, 0x00000001,  0 )
        POL_B                      = ( 0x2F, 0x00000002,  1 )
        POL_N                      = ( 0x2F, 0x00000004,  2 )
        IGNORE_AB                  = ( 0x2F, 0x00000008,  3 )
        CLR_CONT                   = ( 0x2F, 0x00000010,  4 )
        CLR_ONCE                   = ( 0x2F, 0x00000020,  5 )
        POS_NEG_EDGE               = ( 0x2F, 0x000000C0,  6 )
        CLR_ENC_X                  = ( 0x2F, 0x00000100,  8 )
        LATCH_X_ACT                = ( 0x2F, 0x00000200,  9 )
        ENC_SEL_DECIMAL            = ( 0x2F, 0x00000400, 10 )
        NBEMF_ABN_SEL              = ( 0x2F, 0x00000800, 11 )
        BEMF_HYST                  = ( 0x2F, 0x00007000, 12 )
        qsc_enc_en                 = ( 0x2F, 0x00008000, 15 )
        BEMF_BLANK_TIME            = ( 0x2F, 0x00FF0000, 16 )
        BEMF_FILTER_SEL            = ( 0x2F, 0x30000000, 28 )
        ENC_CONST                  = ( 0x30, 0xFFFFFFFF,  0 )
        N_EVENT                    = ( 0x31, 0x00000001,  0 )
        DEVIATION_WARN             = ( 0x31, 0x00000002,  1 )
        ENC_LATCH                  = ( 0x32, 0xFFFFFFFF,  0 )
        ENC_DEVIATION              = ( 0x33, 0x000FFFFF,  0 )
        VIRTUAL_STOP_L             = ( 0x34, 0xFFFFFFFF,  0 )
        VIRTUAL_STOP_R             = ( 0x35, 0xFFFFFFFF,  0 )
        MSCNT                      = ( 0x36, 0x000003FF,  0 )
        CUR_A                      = ( 0x37, 0x000001FF,  0 )
        CUR_B                      = ( 0x37, 0x01FF0000, 16 )
        TOFF                       = ( 0x38, 0x0000000F,  0 )
        HSTRT_TFD210               = ( 0x38, 0x00000070,  4 )
        HEND_OFFSET                = ( 0x38, 0x00000780,  7 )
        FD3                        = ( 0x38, 0x00000800, 11 )
        DISFDCC                    = ( 0x38, 0x00001000, 12 )
        CHM                        = ( 0x38, 0x00004000, 14 )
        TBL                        = ( 0x38, 0x00018000, 15 )
        VHIGHFS                    = ( 0x38, 0x00040000, 18 )
        VHIGHCHM                   = ( 0x38, 0x00080000, 19 )
        TPFD                       = ( 0x38, 0x00F00000, 20 )
        MRES                       = ( 0x38, 0x0F000000, 24 )
        INTPOL                     = ( 0x38, 0x10000000, 28 )
        DEDGE                      = ( 0x38, 0x20000000, 29 )
        DISS2G                     = ( 0x38, 0x40000000, 30 )
        DISS2VS                    = ( 0x38, 0x80000000, 31 )
        SEMIN                      = ( 0x39, 0x0000000F,  0 )
        SEUP                       = ( 0x39, 0x00000060,  5 )
        SEMAX                      = ( 0x39, 0x00000F00,  8 )
        SEDN                       = ( 0x39, 0x00006000, 13 )
        SEIMIN                     = ( 0x39, 0x00008000, 15 )
        SGT                        = ( 0x39, 0x007F0000, 16 )
        SFILT                      = ( 0x39, 0x01000000, 24 )
        DC_TIME                    = ( 0x3A, 0x000003FF,  0 )
        DC_SG                      = ( 0x3A, 0x00FF0000, 16 )
        SG_RESULT                  = ( 0x3B, 0x000003FF,  0 )
        S2VSA                      = ( 0x3B, 0x00001000, 12 )
        S2VSB                      = ( 0x3B, 0x00002000, 13 )
        STEALTH                    = ( 0x3B, 0x00004000, 14 )
        FSACTIVE                   = ( 0x3B, 0x00008000, 15 )
        CS_ACTUAL                  = ( 0x3B, 0x001F0000, 16 )
        STALLGUARD                 = ( 0x3B, 0x01000000, 24 )
        OT                         = ( 0x3B, 0x02000000, 25 )
        OTPW                       = ( 0x3B, 0x04000000, 26 )
        S2GA                       = ( 0x3B, 0x08000000, 27 )
        S2GB                       = ( 0x3B, 0x10000000, 28 )
        OLA                        = ( 0x3B, 0x20000000, 29 )
        OLB                        = ( 0x3B, 0x40000000, 30 )
        STST                       = ( 0x3B, 0x80000000, 31 )
        PWM_OFS                    = ( 0x3C, 0x000000FF,  0 )
        PWM_GRAD                   = ( 0x3C, 0x0000FF00,  8 )
        PWM_FREQ                   = ( 0x3C, 0x00030000, 16 )
        PWM_AUTOSCALE              = ( 0x3C, 0x00040000, 18 )
        PWM_AUTOGRAD               = ( 0x3C, 0x00080000, 19 )
        FREEWHEEL                  = ( 0x3C, 0x00300000, 20 )
        PWM_MEAS_SD_ENABLE         = ( 0x3C, 0x00400000, 22 )
        PWM_DIS_REG_STST           = ( 0x3C, 0x00800000, 23 )
        PWM_REG                    = ( 0x3C, 0x0F000000, 24 )
        PWM_LIM                    = ( 0x3C, 0xF0000000, 28 )
        PWM_SCALE_SUM              = ( 0x3D, 0x000003FF,  0 )
        PWM_SCALE_AUTO             = ( 0x3D, 0x01FF0000, 16 )
        PWM_OFS_AUTO               = ( 0x3E, 0x000000FF,  0 )
        PWM_GRAD_AUTO              = ( 0x3E, 0x00FF0000, 16 )
        SG4_THRS                   = ( 0x3F, 0x000000FF,  0 )
        SG4_FILT_EN                = ( 0x3F, 0x00000100,  8 )
        SG_ANGLE_OFFSET            = ( 0x3F, 0x00000200,  9 )
        SG4_RESULT_SG_RESULT       = ( 0x40, 0x000003FF,  0 )
        IND_0                      = ( 0x41, 0x000000FF,  0 )
        IND_1                      = ( 0x41, 0x0000FF00,  8 )
        IND_2                      = ( 0x41, 0x00FF0000, 16 )
        IND_3                      = ( 0x41, 0xFF000000, 24 )