from ..ic.tmc_ic import TMCIc
from ..features.motor_control_ic import MotorControlIc



class TMC5240(TMCIc):
    """
        The TMC5240 is a smart high-performance stepper motor controller and driver IC with serial communication interfaces (SPI, UART).
        Supply voltage: 4,5-36V
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
        Define all registers of the TMC5240.

        Each register is defined either as an integer or as a tuple of integers.
        Each integer represents a register address. Tuples of addresses are used to
        represent a register that exists multiple times for multiple motors.
        """
        GCONF          = 0x00
        GSTAT          = 0x01
        IFCNT          = 0x02
        SLAVECONF      = 0x03
        INP_OUT        = 0x04
        X_COMPARE      = 0x05
        OTP_PROG       = 0x06
        DRV_CONF       = 0x0A
        GLOBAL_SCALER  = 0x0B
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
        TVMAX          = 0x29
        D1             = 0x2A
        VSTOP          = 0x2B
        TZEROWAIT      = 0x2C
        XTARGET        = 0x2D
        V2	           = 0x2E
        A2             = 0x2F
        D2     		   = 0x30
        AACTUAL        = 0x31
        VDCMIN         = 0x33
        SWMODE         = 0x34
        RAMPSTAT       = 0x35
        XLATCH         = 0x36
        ENCMODE        = 0x38
        XENC           = 0x39
        ENC_CONST      = 0x3A
        ENC_STATUS     = 0x3B
        ENC_LATCH      = 0x3C
        ENC_DEVIATION  = 0x3D
        ADC_VSUPPLY_AIN= 0x50
        ADC_TEMP       = 0x51
        OTW_OV_VTH     = 0x52
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
        DRVSTATUS      = 0x6F
        PWMCONF        = 0x70
        PWMSCALE       = 0x71
        PWM_AUTO       = 0x72
        SG4_THRS       = 0x74
        SG4_RESULT	   = 0x75
        SG4_IND        = 0x76

    class FIELD:
        """
        Define all register bitfields of the TMC5240.

        Each field is defined as a tuple consisting of ( Address, Mask, Shift ).

        The name of the register is written as a comment behind each tuple. This is
        intended for IDE users viewing the definition of a field by hovering over
        it. This allows the user to see the corresponding register name of a field
        without opening this file and searching for the definition.
        """

        FAST_STANDSTILL = (0x00, 0x00000002, 1)
        EN_PWM_MODE = (0x00, 0x00000004, 2)
        MULTISTEP_FILT = (0x00, 0x00000008, 3)
        SHAFT = (0x00, 0x00000010, 4)
        DIAG0_NINT_STEP = (0x00, 0x00000080, 7)
        DIAG1_NPOSCOMP_DIR = (0x00, 0x00000100, 8)
        DIAG0_INT_PUSHPULL = (0x00, 0x00001000, 12)
        DIAG1_POSCOMP_PUSHPULL = (0x00, 0x00002000, 13)
        SMALL_HYSTERESIS = (0x00, 0x00004000, 14)
        STOP_ENABLE = (0x00, 0x00008000, 15)
        DIRECT_MODE = (0x00, 0x00010000, 16)
        LENGTH_STEP_PULSE = (0x00, 0x001E0000, 17)
        RESET = (0x01, 0x00000001, 0)
        DRV_ERR = (0x01, 0x00000002, 1)
        UV_CP = (0x01, 0x00000004, 2)
        REGISTER_RESET = (0x01, 0x00000008, 3)
        VM_UVLO = (0x01, 0x00000010, 4)
        IFCNT = (0x02, 0x000000FF, 0)
        SLAVEADDR = (0x03, 0x000000FF, 0)
        SENDDELAY = (0x03, 0x00000F00, 8)
        REFL = (0x04, 0x00000001, 0)
        REFR = (0x04, 0x00000002, 1)
        ENCB = (0x04, 0x00000004, 2)
        ENCA = (0x04, 0x00000008, 3)
        DRV_ENN = (0x04, 0x00000010, 4)
        ENCN = (0x04, 0x00000020, 5)
        UART_EN = (0x04, 0x00000040, 6)
        RESERVED = (0x04, 0x00000080, 7)
        COMP_A = (0x04, 0x00000100, 8)
        COMP_B = (0x04, 0x00000200, 9)
        COMP_A1_A2 = (0x04, 0x00000400, 10)
        COMP_B1_B2 = (0x04, 0x00000800, 11)
        OUTPUT = (0x04, 0x00001000, 12)
        EXT_RES_DET = (0x04, 0x00002000, 13)
        EXT_CLK = (0x04, 0x00004000, 14)
        ADC_ERR = (0x04, 0x00008000, 15)
        SILICON_RV = (0x04, 0x00070000, 16)
        VERSION = (0x04, 0xFF000000, 24)
        X_COMPARE = (0x05, 0xFFFFFFFF, 0)
        X_COMPARE_REPEAT = (0x06, 0x00FFFFFF, 0)
        CURRENT_RANGE = (0x0A, 0x00000003, 0)
        SLOPE_CONTROL = (0x0A, 0x00000030, 4)
        GLOBALSCALER = (0x0B, 0x000000FF, 0)
        IHOLD = (0x10, 0x0000001F, 0)
        IRUN = (0x10, 0x00001F00, 8)
        IHOLDDELAY = (0x10, 0x000F0000, 16)
        IRUNDELAY = (0x10, 0x0F000000, 24)
        TPOWERDOWN = (0x11, 0x000000FF, 0)
        TSTEP = (0x12, 0x000FFFFF, 0)
        TPWMTHRS = (0x13, 0x000FFFFF, 0)
        TCOOLTHRS = (0x14, 0x000FFFFF, 0)
        THIGH = (0x15, 0x000FFFFF, 0)
        RAMPMODE = (0x20, 0x00000003, 0)
        XACTUAL = (0x21, 0xFFFFFFFF, 0)
        VACTUAL = (0x22, 0x00FFFFFF, 0)
        VSTART = (0x23, 0x0003FFFF, 0)
        A1 = (0x24, 0x0003FFFF, 0)
        V1 = (0x25, 0x000FFFFF, 0)
        AMAX = (0x26, 0x0003FFFF, 0)
        VMAX = (0x27, 0x007FFFFF, 0)
        DMAX = (0x28, 0x0003FFFF, 0)
        TVMAX = (0x29, 0x0000FFFF, 0)
        D1 = (0x2A, 0x0003FFFF, 0)
        VSTOP = (0x2B, 0x0003FFFF, 0)
        TZEROWAIT = (0x2C, 0x0000FFFF, 0)
        XTARGET = (0x2D, 0xFFFFFFFF, 0)
        V2 = (0x2E, 0x000FFFFF, 0)
        A2 = (0x2F, 0x0003FFFF, 0)
        D2 = (0x30, 0x0003FFFF, 0)
        AACTUAL = (0x31, 0x00FFFFFF, 0)
        # RESERVED                = ( 0x33, 0x000000FF,  0 )
        VDCMIN = (0x33, 0x007FFF00, 8)
        STOP_L_ENABLE = (0x34, 0x00000001, 0)
        STOP_R_ENABLE = (0x34, 0x00000002, 1)
        POL_STOP_L = (0x34, 0x00000004, 2)
        POL_STOP_R = (0x34, 0x00000008, 3)
        SWAP_LR = (0x34, 0x00000010, 4)
        LATCH_L_ACTIVE = (0x34, 0x00000020, 5)
        LATCH_L_INACTIVE = (0x34, 0x00000040, 6)
        LATCH_R_ACTIVE = (0x34, 0x00000080, 7)
        LATCH_R_INACTIVE = (0x34, 0x00000100, 8)
        EN_LATCH_ENCODER = (0x34, 0x00000200, 9)
        SG_STOP = (0x34, 0x00000400, 10)
        EN_SOFTSTOP = (0x34, 0x00000800, 11)
        EN_VIRTUAL_STOP_L = (0x34, 0x00001000, 12)
        EN_VIRTUAL_STOP_R = (0x34, 0x00002000, 13)
        VIRTUAL_STOP_ENC = (0x34, 0x00004000, 14)
        STATUS_STOP_L = (0x35, 0x00000001, 0)
        STATUS_STOP_R = (0x35, 0x00000002, 1)
        STATUS_LATCH_L = (0x35, 0x00000004, 2)
        STATUS_LATCH_R = (0x35, 0x00000008, 3)
        EVENT_STOP_L = (0x35, 0x00000010, 4)
        EVENT_STOP_R = (0x35, 0x00000020, 5)
        EVENT_STOP_SG = (0x35, 0x00000040, 6)
        EVENT_POS_REACHED = (0x35, 0x00000080, 7)
        VELOCITY_REACHED = (0x35, 0x00000100, 8)
        POSITION_REACHED = (0x35, 0x00000200, 9)
        VZERO = (0x35, 0x00000400, 10)
        T_ZEROWAIT_ACTIVE = (0x35, 0x00000800, 11)
        SECOND_MOVE = (0x35, 0x00001000, 12)
        STATUS_SG = (0x35, 0x00002000, 13)
        STATUS_VIRTUAL_STOP_L = (0x35, 0x00004000, 14)
        STATUS_VIRTUAL_STOP_R = (0x35, 0x00008000, 15)
        XLATCH = (0x36, 0xFFFFFFFF, 0)
        POL_A = (0x38, 0x00000001, 0)
        POL_B = (0x38, 0x00000002, 1)
        POL_N = (0x38, 0x00000004, 2)
        IGNORE_AB = (0x38, 0x00000008, 3)
        CLR_CONT = (0x38, 0x00000010, 4)
        CLR_ONCE = (0x38, 0x00000020, 5)
        POS_NEG_EDGE = (0x38, 0x000000C0, 6)
        CLR_ENC_X = (0x38, 0x00000100, 8)
        LATCH_X_ACT = (0x38, 0x00000200, 9)
        ENC_SEL_DECIMAL = (0x38, 0x00000400, 10)
        X_ENC = (0x39, 0xFFFFFFFF, 0)
        ENC_CONST = (0x3A, 0xFFFFFFFF, 0)
        N_EVENT = (0x3B, 0x00000001, 0)
        DEVIATION_WARN = (0x3B, 0x00000002, 1)
        ENC_LATCH = (0x3C, 0xFFFFFFFF, 0)
        ENC_DEVIATION = (0x3D, 0x000FFFFF, 0)
        VIRTUAL_STOP_L = (0x3E, 0xFFFFFFFF, 0)
        VIRTUAL_STOP_R = (0x3F, 0xFFFFFFFF, 0)
        ADC_VSUPPLY = (0x50, 0x00001FFF, 0)
        ADC_AIN = (0x50, 0x1FFF0000, 16)
        ADC_TEMP = (0x51, 0x00001FFF, 0)
        # RESERVED                = ( 0x51, 0x1FFF0000, 16 )
        OVERVOLTAGE_VTH = (0x52, 0x00001FFF, 0)
        OVERTEMPPREWARNING_VTH = (0x52, 0x1FFF0000, 16)
        MSLUT__ = (0x60, 0xFFFFFFFF, 0)
        # MSLUT__                 = ( 0x61, 0xFFFFFFFF,  0 )
        # MSLUT__                 = ( 0x62, 0xFFFFFFFF,  0 )
        # MSLUT__                 = ( 0x63, 0xFFFFFFFF,  0 )
        # MSLUT__                 = ( 0x64, 0xFFFFFFFF,  0 )
        # MSLUT__                 = ( 0x65, 0xFFFFFFFF,  0 )
        # MSLUT__                 = ( 0x66, 0xFFFFFFFF,  0 )
        # MSLUT__                 = ( 0x67, 0xFFFFFFFF,  0 )
        W0 = (0x68, 0x00000003, 0)
        W1 = (0x68, 0x0000000C, 2)
        W2 = (0x68, 0x00000030, 4)
        W3 = (0x68, 0x000000C0, 6)
        X1 = (0x68, 0x0000FF00, 8)
        X2 = (0x68, 0x00FF0000, 16)
        X3 = (0x68, 0xFF000000, 24)
        START_SIN = (0x69, 0x000000FF, 0)
        START_SIN90 = (0x69, 0x00FF0000, 16)
        OFFSET_SIN90 = (0x69, 0xFF000000, 24)
        MSCNT = (0x6A, 0x000003FF, 0)
        CUR_B = (0x6B, 0x000001FF, 0)
        CUR_A = (0x6B, 0x01FF0000, 16)
        TOFF = (0x6C, 0x0000000F, 0)
        HSTRT_TFD210 = (0x6C, 0x00000070, 4)
        HEND_OFFSET = (0x6C, 0x00000780, 7)
        FD3 = (0x6C, 0x00000800, 11)
        DISFDCC = (0x6C, 0x00001000, 12)
        CHM = (0x6C, 0x00004000, 14)
        TBL = (0x6C, 0x00018000, 15)
        VHIGHFS = (0x6C, 0x00040000, 18)
        VHIGHCHM = (0x6C, 0x00080000, 19)
        TPFD = (0x6C, 0x00F00000, 20)
        MRES = (0x6C, 0x0F000000, 24)
        INTPOL = (0x6C, 0x10000000, 28)
        DEDGE = (0x6C, 0x20000000, 29)
        DISS2G = (0x6C, 0x40000000, 30)
        DISS2VS = (0x6C, 0x80000000, 31)
        SEMIN = (0x6D, 0x0000000F, 0)
        SEUP = (0x6D, 0x00000060, 5)
        SEMAX = (0x6D, 0x00000F00, 8)
        SEDN = (0x6D, 0x00006000, 13)
        SEIMIN = (0x6D, 0x00008000, 15)
        SGT = (0x6D, 0x007F0000, 16)
        SFILT = (0x6D, 0x01000000, 24)
        DC_TIME = (0x6E, 0x000003FF, 0)
        DC_SG = (0x6E, 0x00FF0000, 16)
        SG_RESULT = (0x6F, 0x000003FF, 0)
        S2VSA = (0x6F, 0x00001000, 12)
        S2VSB = (0x6F, 0x00002000, 13)
        STEALTH = (0x6F, 0x00004000, 14)
        FSACTIVE = (0x6F, 0x00008000, 15)
        CS_ACTUAL = (0x6F, 0x001F0000, 16)
        STALLGUARD = (0x6F, 0x01000000, 24)
        OT = (0x6F, 0x02000000, 25)
        OTPW = (0x6F, 0x04000000, 26)
        S2GA = (0x6F, 0x08000000, 27)
        S2GB = (0x6F, 0x10000000, 28)
        OLA = (0x6F, 0x20000000, 29)
        OLB = (0x6F, 0x40000000, 30)
        STST = (0x6F, 0x80000000, 31)
        PWM_OFS = (0x70, 0x000000FF, 0)
        PWM_GRAD = (0x70, 0x0000FF00, 8)
        PWM_FREQ = (0x70, 0x00030000, 16)
        PWM_AUTOSCALE = (0x70, 0x00040000, 18)
        PWM_AUTOGRAD = (0x70, 0x00080000, 19)
        FREEWHEEL = (0x70, 0x00300000, 20)
        PWM_MEAS_SD_ENABLE = (0x70, 0x00400000, 22)
        PWM_DIS_REG_STST = (0x70, 0x00800000, 23)
        PWM_REG = (0x70, 0x0F000000, 24)
        PWM_LIM = (0x70, 0xF0000000, 28)
        PWM_SCALE_SUM = (0x71, 0x000003FF, 0)
        PWM_SCALE_AUTO = (0x71, 0x01FF0000, 16)
        PWM_OFS_AUTO = (0x72, 0x000000FF, 0)
        PWM_GRAD_AUTO = (0x72, 0x00FF0000, 16)
        SG4_THRS = (0x74, 0x000000FF, 0)
        SG4_FILT_EN = (0x74, 0x00000100, 8)
        SG_ANGLE_OFFSET = (0x74, 0x00000200, 9)
        SG4_RESULT = (0x75, 0x000003FF, 0)
        SG4_IND_0 = (0x76, 0x000000FF, 0)
        SG4_IND_1 = (0x76, 0x0000FF00, 8)
        SG4_IND_2 = (0x76, 0x00FF0000, 16)
        SG4_IND_3 = (0x76, 0xFF000000, 24)