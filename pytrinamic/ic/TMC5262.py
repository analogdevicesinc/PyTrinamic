################################################################################
# Copyright © 2023 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

from ..ic.tmc_ic import TMCIc
from ..features.motor_control_ic import MotorControlIc


class TMC5262(TMCIc):
    """
        The TMC5262 is a smart high-power single axis stepper motor controller and driver IC with SPI communication interface.
        Supply voltage: 4,5-65V DC
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
        Define all registers of the TMC5262.

        Each register is defined either as an integer or as a tuple of integers.
        Each integer represents a register address. Tuples of addresses are used to
        represent a register that exists multiple times for multiple motors.
        """
        GCONF = 0x00
        GSTAT = 0x01
        DIAG_CONF = 0x02
        DIAG_DAC_CONF = 0x03
        IOIN = 0x04
        X_COMPARE = 0x05
        X_COMPARE_REPEAT = 0x06
        DRV_CONF = 0x0A
        PLL = 0x0B
        IHOLD_IRUN = 0x10
        TPOWERDOWN = 0x11
        TSTEP = 0x12
        TPWMTHRS = 0x13
        TCOOLTHRS = 0x14
        THIGH = 0x15
        TSGP_LOW_VEL_THRS = 0x16
        T_RCOIL_MEAS = 0x17
        TUDCSTEP = 0x18
        UDC_CONF = 0x19
        STEPS_LOST = 0x1A
        RAMPMODE = 0x20
        XACTUAL = 0x21
        VACTUAL = 0x22
        VSTART = 0x23
        A1 = 0x24
        V1 = 0x25
        AMAX = 0x26
        VMAX = 0x27
        DMAX = 0x28
        TVMAX = 0x29
        D1 = 0x2A
        VSTOP = 0x2B
        TZEROWAIT = 0x2C
        XTARGET = 0x2D
        V2 = 0x2E
        A2 = 0x2F
        D2 = 0x30
        AACTUAL = 0x31
        SW_MODE = 0x34
        RAMP_STAT = 0x35
        XLATCH = 0x36
        ENCMODE = 0x38
        X_ENC = 0x39
        ENC_CONST = 0x3A
        ENC_STATUS = 0x3B
        ENC_LATCH = 0x3C
        ENC_DEVIATION = 0x3D
        VIRTUAL_STOP_L = 0x3E
        VIRTUAL_STOP_R = 0x3F
        CURRENT_PI_REG = 0x40
        ANGLE_PI_REG = 0x41
        CUR_ANGLE_LIMIT = 0x42
        ANGLE_LOWER_LIMIT = 0x43
        CUR_ANGLE_MEAS = 0x44
        PI_RESULTS = 0x45
        COIL_INDUCT = 0x46
        R_COIL = 0x47
        R_COIL_USER = 0x48
        SGP_CONF = 0x49
        SGP_IND_2_3 = 0x4A
        SGP_IND_0_1 = 0x4B
        INDUCTANCE_VOLTAGE = 0x4C
        SGP_BEMF = 0x4D
        COOLSTEPPLUS_CONF = 0x4E
        COOLSTEPPLUS_PI_REG = 0x4F
        COOLSTEPPLUS_PI_DOWN = 0x50
        COOLSTEPPLUS_RESERVE_CONF = 0x51
        COOLSTEPPLUS_LOAD_RESERVE = 0x52
        TSTEP_VELOCITY = 0x53
        ADC_VSUPPLY_TEMP = 0x58
        ADC_I = 0x59
        OTW_OV_VTH = 0x5A
        MSLUT_0 = 0x60
        MSLUT_1 = 0x61
        MSLUT_2 = 0x62
        MSLUT_3 = 0x63
        MSLUT_4 = 0x64
        MSLUT_5 = 0x65
        MSLUT_6 = 0x66
        MSLUT_7 = 0x67
        MSLUTSEL = 0x68
        MSLUTSTART = 0x69
        MSCNT = 0x6A
        MSCURACT = 0x6B
        CHOPCONF = 0x6C
        COOLCONF = 0x6D
        DRV_STATUS = 0x6F
        PWMCONF = 0x70

    class FIELD:
        """
        Define all register bitfields of the TMC5262.

        Each field is defined as a tuple consisting of ( Address, Mask, Shift ).

        The name of the register is written as a comment behind each tuple. This is
        intended for IDE users viewing the definition of a field by hovering over
        it. This allows the user to see the corresponding register name of a field
        without opening this file and searching for the definition.
        """

        FAST_STANDSTILL = (0x00, 0x00000001, 0)
        EN_STEALTHCHOP = (0x00, 0x00000002, 1)
        MULTISTEP_FILT = (0x00, 0x00000004, 2)
        SHAFT = (0x00, 0x00000008, 3)
        SMALL_HYSTERESIS = (0x00, 0x00000010, 4)
        STOP_ENABLE = (0x00, 0x00000020, 5)
        DIRECT_MODE = (0x00, 0x00000040, 6)
        LENGTH_STEPPULSE = (0x00, 0x00000F00, 8)
        OV_NN = (0x00, 0x00001000, 12)
        THREEPHASE_MCC = (0x00, 0x40000000, 30)
        STEP_DIR = (0x00, 0x80000000, 31)
        RESET = (0x01, 0x00000001, 0)
        DRV_ERR = (0x01, 0x00000002, 1)
        UV_CP = (0x01, 0x00000004, 2)
        REGISTER_RESET = (0x01, 0x00000008, 3)
        VM_UVLO = (0x01, 0x00000010, 4)
        VCCIO_UV = (0x01, 0x00000020, 5)
        DIAG0_ERROR = (0x02, 0x00000001, 0)
        DIAG0_OTPW = (0x02, 0x00000002, 1)
        DIAG0_STALL = (0x02, 0x00000004, 2)
        DIAG0_INDEX = (0x02, 0x00000008, 3)
        DIAG0_STEP = (0x02, 0x00000010, 4)
        DIAG0_DIR = (0x02, 0x00000020, 5)
        DIAG0_XCOMP = (0x02, 0x00000040, 6)
        DIAG0_OV = (0x02, 0x00000080, 7)
        DIAG0_DCUSTEP = (0x02, 0x00000100, 8)
        DIAG0_EV_STOP_REF = (0x02, 0x00000200, 9)
        DIAG0_EV_STOP_SG = (0x02, 0x00000400, 10)
        DIAG0_EV_POS_REACHED = (0x02, 0x00000800, 11)
        DIAG0_EV_N_DEVIATION = (0x02, 0x00001000, 12)
        DIAG1_ERROR = (0x02, 0x00002000, 13)
        DIAG1_OTPW = (0x02, 0x00004000, 14)
        DIAG1_STALL = (0x02, 0x00008000, 15)
        DIAG1_INDEX = (0x02, 0x00010000, 16)
        DIAG1_STEP = (0x02, 0x00020000, 17)
        DIAG1_DIR = (0x02, 0x00040000, 18)
        DIAG1_XCOMP = (0x02, 0x00080000, 19)
        DIAG1_OV = (0x02, 0x00100000, 20)
        DIAG1_UDCSTEP = (0x02, 0x00200000, 21)
        DIAG1_EV_STOP_REF = (0x02, 0x00400000, 22)
        DIAG1_EV_STOP_SG = (0x02, 0x00800000, 23)
        DIAG1_EV_POS_REACHED = (0x02, 0x01000000, 24)
        DIAG1_EV_N_DEVIATION = (0x02, 0x02000000, 25)
        DIAG0_NOD_PP = (0x02, 0x10000000, 28)
        DIAG0_INVPP = (0x02, 0x20000000, 29)
        DIAG1_NOD_PP = (0x02, 0x40000000, 30)
        DIAG1_INVPP = (0x02, 0x80000000, 31)
        DIAG0_DAC_EN = (0x03, 0x00000001, 0)
        DIAG0_DAC_SEL = (0x03, 0x000001F0, 4)
        DIAG1_DAC_EN = (0x03, 0x00001000, 12)
        DIAG1_DAC_SEL = (0x03, 0x001F0000, 16)
        REFL = (0x04, 0x00000001, 0)
        REFR = (0x04, 0x00000002, 1)
        ENCB = (0x04, 0x00000004, 2)
        ENCA = (0x04, 0x00000008, 3)
        DRV_ENN = (0x04, 0x00000010, 4)
        ENCN = (0x04, 0x00000020, 5)
        RESERVED = (0x04, 0x00000080, 7)
        EXT_RES_DET = (0x04, 0x00002000, 13)
        EXT_CLK = (0x04, 0x00004000, 14)
        SILICON_RV = (0x04, 0x00070000, 16)
        VERSION = (0x04, 0xFF000000, 24)
        X_COMPARE = (0x05, 0xFFFFFFFF, 0)
        X_COMPARE_REPEAT = (0x06, 0x00FFFFFF, 0)
        CURRENT_RANGE = (0x0A, 0x00000003, 0)
        CURRENT_RANGE_SCALE = (0x0A, 0x0000000C, 2)
        SLOPE_CONTROL = (0x0A, 0x00000030, 4)
        COMMIT = (0x0B, 0x00000001, 0)
        EXT_NOT_INT = (0x0B, 0x00000002, 1)
        CLK_SYS_SEL = (0x0B, 0x00000004, 2)
        ADC_CLK_ENA = (0x0B, 0x00000008, 3)
        PWM_CLK_ENA = (0x0B, 0x00000010, 4)
        CLOCK_DIVIDER = (0x0B, 0x000003E0, 5)
        CLK_FSM_ENA = (0x0B, 0x00000400, 10)
        CLK_1MO_TMO = (0x0B, 0x00001000, 12)
        CLK_LOSS = (0x0B, 0x00002000, 13)
        CLK_IS_STUCK = (0x0B, 0x00004000, 14)
        PLL_LOCK_LOSS = (0x0B, 0x00008000, 15)
        IHOLD = (0x10, 0x000000FF, 0)
        IRUN = (0x10, 0x0000FF00, 8)
        IHOLDDELAY = (0x10, 0x00FF0000, 16)
        IRUNDELAY = (0x10, 0x0F000000, 24)
        TPOWERDOWN = (0x11, 0x000000FF, 0)
        TSTEP = (0x12, 0x000FFFFF, 0)
        TPWMTHRS = (0x13, 0x000FFFFF, 0)
        TCOOLTHRS = (0x14, 0x000FFFFF, 0)
        THIGH = (0x15, 0x000FFFFF, 0)
        TSGP_LOW_VEL_THRS = (0x16, 0x000FFFFF, 0)
        T_RCOIL_MEAS = (0x17, 0x000FFFFF, 0)
        TUDCSTEP = (0x18, 0x000FFFFF, 0)
        DECEL_THRS = (0x19, 0x0000000F, 0)
        ACCEL_THRS = (0x19, 0x000000F0, 4)
        UDC_ENABLE = (0x19, 0x00000100, 8)
        STEPS_LOST = (0x1A, 0x000FFFFF, 0)
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
        HARD_STOP_CLR_CUR_INT = (0x34, 0x00008000, 15)
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
        NBEMF_ABN_SEL = (0x38, 0x00000800, 11)
        BEMF_HYST = (0x38, 0x00007000, 12)
        BEMF_BLANK_TIME = (0x38, 0x00FF0000, 16)
        BEMF_FILTER_SEL = (0x38, 0x30000000, 28)
        X_ENC = (0x39, 0xFFFFFFFF, 0)
        ENC_CONST = (0x3A, 0xFFFFFFFF, 0)
        N_EVENT = (0x3B, 0x00000001, 0)
        DEVIATION_WARN = (0x3B, 0x00000002, 1)
        ENC_LATCH = (0x3C, 0xFFFFFFFF, 0)
        ENC_DEVIATION = (0x3D, 0x000FFFFF, 0)
        VIRTUAL_STOP_L = (0x3E, 0xFFFFFFFF, 0)
        VIRTUAL_STOP_R = (0x3F, 0xFFFFFFFF, 0)
        CUR_P = (0x40, 0x00000FFF, 0)
        CUR_I = (0x40, 0x03FF0000, 16)
        ANGLE_P = (0x41, 0x00000FFF, 0)
        ANGLE_I = (0x41, 0x03FF0000, 16)
        ANGLE_PI_LIMIT = (0x42, 0x000003FF, 0)
        ANGLE_PI_INT_POS_CLIP = (0x42, 0x00001000, 12)
        ANGLE_PI_INT_NEG_CLIP = (0x42, 0x00002000, 13)
        ANGLE_PI_POS_CLIP = (0x42, 0x00004000, 14)
        ANGLE_PI_NEG_CLIP = (0x42, 0x00008000, 15)
        CUR_PI_LIMIT = (0x42, 0x0FFF0000, 16)
        CUR_PI_INT_POS_CLIP = (0x42, 0x10000000, 28)
        CUR_PI_INT_NEG_CLIP = (0x42, 0x20000000, 29)
        CUR_PI_POS_CLIP = (0x42, 0x40000000, 30)
        CUR_PI_NEG_CLIP = (0x42, 0x80000000, 31)
        ANGLE_LOWER_I_LIMIT = (0x43, 0x000003FF, 0)
        ANGLE_ERROR = (0x43, 0x03FF0000, 16)
        AMPL_MEAS = (0x44, 0x00000FFF, 0)
        ANGLE_MEAS = (0x44, 0x03FF0000, 16)
        PWM_CALC = (0x45, 0x00001FFF, 0)
        ANGLE_CORR_CALC = (0x45, 0x03FF0000, 16)
        COIL_INDUCT = (0x46, 0x00007FFF, 0)
        RCOIL_MANUAL = (0x46, 0x00010000, 16)
        RCOIL_THERMAL_COUPLING = (0x46, 0x00020000, 17)
        R_COIL_AUTO_B = (0x47, 0x00000FFF, 0)
        R_COIL_AUTO_A = (0x47, 0x0FFF0000, 16)
        R_COIL_USER_B = (0x48, 0x00000FFF, 0)
        R_COIL_USER_A = (0x48, 0x0FFF0000, 16)
        SGP_THRS = (0x49, 0x000001FF, 0)
        SGP_FILT_EN = (0x49, 0x00001000, 12)
        SGP_LOW_VEL_FREEZE = (0x49, 0x00002000, 13)
        SGP_CLEAR_CUR_PI = (0x49, 0x00004000, 14)
        SGP_LOW_VEL_SLOPE = (0x49, 0x00FF0000, 16)
        SGP_LOW_VEL_CNTS = (0x49, 0x30000000, 28)
        SGP_IND_2 = (0x4A, 0x000003FF, 0)
        SGP_IND_3 = (0x4A, 0x03FF0000, 16)
        SGP_IND_0 = (0x4B, 0x000003FF, 0)
        SGP_IND_1 = (0x4B, 0x03FF0000, 16)
        UL_B = (0x4C, 0x00000FFF, 0)
        UL_A = (0x4C, 0x0FFF0000, 16)
        SGP_RAW = (0x4D, 0x000003FF, 0)
        UBEMF_ABS = (0x4D, 0x0FFF0000, 16)
        COOL_CUR_DIV = (0x4E, 0x0000000F, 0)
        LOAD_FILT_EN = (0x4E, 0x00000010, 4)
        COOLSTEP_P = (0x4F, 0x00000FFF, 0)
        COOLSTEP_I = (0x4F, 0x03FF0000, 16)
        COOL_PI_DOWN_LIMIT = (0x50, 0x00000FFF, 0)
        COOL_PI_OFF_SPEED = (0x50, 0x0FFF0000, 16)
        COOL_LOW_LOAD_RESERVE = (0x51, 0x000000FF, 0)
        COOL_HI_LOAD_RESERVE = (0x51, 0x0000FF00, 8)
        COOL_LOW_GENERATORIC_RESERVE = (0x51, 0x00FF0000, 16)
        COOL_HI_GENERATORIC_RESERVE = (0x51, 0xFF000000, 24)
        SGP_RESULT = (0x52, 0x000003FF, 0)
        COOLSTEP_LOAD_RESERVE = (0x52, 0x01FF0000, 16)
        TSTEP_VELOCITY = (0x53, 0x007FFFFF, 0)
        ADC_VSUPPLY = (0x58, 0x000001FF, 0)
        ADC_TEMP = (0x58, 0x01FF0000, 16)
        ADC_I_A = (0x59, 0x00000FFF, 0)
        ADC_I_B = (0x59, 0x0FFF0000, 16)
        OVERVOLTAGE_VTH = (0x5A, 0x000001FF, 0)
        OVERTEMPPREWARNING_VTH = (0x5A, 0x01FF0000, 16)
        MSLUT_0 = (0x60, 0xFFFFFFFF, 0)
        MSLUT_1 = (0x61, 0xFFFFFFFF, 0)
        MSLUT_2 = (0x62, 0xFFFFFFFF, 0)
        MSLUT_3 = (0x63, 0xFFFFFFFF, 0)
        MSLUT_4 = (0x64, 0xFFFFFFFF, 0)
        MSLUT_5 = (0x65, 0xFFFFFFFF, 0)
        MSLUT_6 = (0x66, 0xFFFFFFFF, 0)
        MSLUT_7 = (0x67, 0xFFFFFFFF, 0)
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
        TPFD = (0x6C, 0x00F00000, 20)
        MRES = (0x6C, 0x0F000000, 24)
        INTPOL = (0x6C, 0x10000000, 28)
        DEDGE = (0x6C, 0x20000000, 29)
        SEMIN = (0x6D, 0x0000000F, 0)
        SEUP = (0x6D, 0x00000060, 5)
        SEMAX = (0x6D, 0x00000F00, 8)
        SEDN = (0x6D, 0x00007000, 12)
        SEIMIN = (0x6D, 0x00008000, 15)
        SGT = (0x6D, 0x007F0000, 16)
        THIGH_SG_OFF = (0x6D, 0x00800000, 23)
        SFILT = (0x6D, 0x01000000, 24)
        SG_RESULT = (0x6F, 0x000003FF, 0)
        SEQ_STOPPED = (0x6F, 0x00000400, 10)
        OV = (0x6F, 0x00000800, 11)
        S2VSA = (0x6F, 0x00001000, 12)
        S2VSB = (0x6F, 0x00002000, 13)
        STEALTH = (0x6F, 0x00004000, 14)
        CS_ACTUAL = (0x6F, 0x00FF0000, 16)
        STALLGUARD = (0x6F, 0x01000000, 24)
        OT = (0x6F, 0x02000000, 25)
        OTPW = (0x6F, 0x04000000, 26)
        S2GA = (0x6F, 0x08000000, 27)
        S2GB = (0x6F, 0x10000000, 28)
        OLA = (0x6F, 0x20000000, 29)
        OLB = (0x6F, 0x40000000, 30)
        STST = (0x6F, 0x80000000, 31)
        PWM_FREQ = (0x70, 0x0000000F, 0)
        FREEWHEEL = (0x70, 0x00000030, 4)
        OL_THRSH = (0x70, 0x000000C0, 6)
        SD_ON_MEAS_LO = (0x70, 0x0000F000, 12)
        SD_ON_MEAS_HI = (0x70, 0x000F0000, 16)
