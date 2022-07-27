from ..ic.tmc_ic import TMCIc

# features
from ..features.motor_control_ic import MotorControlIc
# from pytrinamic.features.LinearRampIC import LinearRampIC
# from pytrinamic.features.CurrentIC import CurrentIC
# from pytrinamic.features.StallGuard2IC import StallGuard2IC


class TMC5072(TMCIc):
    """
    The TMC5072 is a high-performance stepper motor controller and driver IC with serial communication interfaces.
    Supply voltage: 5-28V
    """
    def __init__(self, parent_eval):
        """
        Constructor for the TMC_IC instance.

        Parameters:
        handler: Handler object for register access operations.
        This object is expected to implement write_register and read_register functions
        to read/write registers via platform-specific communication.
        channel: Channel identifier for this IC. This will be handed to the
        write_register and read_register functions of the handler to differentiate
        between multiple ICs.
        """
        super().__init__("TMC5072", self.__doc__)
        self._parent = parent_eval
        self.motors = [self.MotorTypeA(parent_eval, self, 0), self.MotorTypeA(parent_eval, self, 1)]

    class MotorTypeA(MotorControlIc):
        """
        Motor class for the generic motor.
        """
        def __init__(self, parent_eval, ic, axis):
            MotorControlIc.__init__(self, parent_eval, ic, axis)
#            LinearRampIC.__init__(self)
#            CurrentIC.__init__(self)
#            StallGuard2IC.__init__(self)

    class REG:
        """
        Define all registers of the TMC5072.

        Each register is defined either as an integer or as a tuple of integers.
        Each integer represents a register address. Tuples of addresses are used to
        represent a register that exists multiple times for multiple motors.
        """
        GCONF           = 0x00
        GSTAT           = 0x01
        IFCNT           = 0x02
        SLAVECONF       = 0x03
        INPUT___OUTPUT  = 0x04
        X_COMPARE       = 0x05
        PWMCONF_M1      = 0x10
        PWM_STATUS_M1   = 0x11
        PWMCONF_M2      = 0x18
        PWM_STATUS_M2   = 0x19
        RAMPMODE_M1     = 0x20
        XACTUAL_M1      = 0x21
        VACTUAL_M1      = 0x22
        VSTART_M1       = 0x23
        A1_M1           = 0x24
        V1_M1           = 0x25
        AMAX_M1         = 0x26
        VMAX_M1         = 0x27
        DMAX_M1         = 0x28
        D1_M1           = 0x2A
        VSTOP_M1        = 0x2B
        TZEROWAIT_M1    = 0x2C
        XTARGET_M1      = 0x2D
        RAMPMODE_M2     = 0x40
        XACTUAL_M2      = 0x41
        VACTUAL_M2      = 0x42
        VSTART_M2       = 0x43
        A1_M2           = 0x44
        V1_M2           = 0x45
        AMAX_M2         = 0x46
        VMAX_M2         = 0x47
        DMAX_M2         = 0x48
        D1_M2           = 0x4A
        VSTOP_M2        = 0x4B
        TZEROWAIT_M2    = 0x4C
        XTARGET_M2      = 0x4D
        IHOLD_IRUN_M1   = 0x30
        VCOOLTHRS_M1    = 0x31
        VHIGH_M1        = 0x32
        VDCMIN_M1       = 0x33
        SW_MODE_M1      = 0x34
        RAMP_STAT_M1    = 0x35
        XLATCH_M1       = 0x36
        IHOLD_IRUN_M2   = 0x50
        VCOOLTHRS_M2    = 0x51
        VHIGH_M2        = 0x52
        VDCMIN_M2       = 0x53
        SW_MODE_M2      = 0x54
        RAMP_STAT_M2    = 0x55
        XLATCH_M2       = 0x56
        ENCMODE_M1      = 0x38
        X_ENC_M1        = 0x39
        ENC_CONST_M1    = 0x3A
        ENC_STATUS_M1   = 0x3B
        ENC_LATCH_M1    = 0x3C
        ENCMODE_M2      = 0x58
        X_ENC_M2        = 0x59
        ENC_CONST_M2    = 0x5A
        ENC_STATUS_M2   = 0x5B
        ENC_LATCH_M2    = 0x5C
        MSLUT_0         = 0x60
        MSLUT_1         = 0x61
        MSLUT_2         = 0x62
        MSLUT_3         = 0x63
        MSLUT_4         = 0x64
        MSLUT_5         = 0x65
        MSLUT_6         = 0x66
        MSLUT_7         = 0x67
        MSLUTSEL        = 0x68
        MSLUTSTART      = 0x69
        MSCNT_M1        = 0x6A
        MSCURACT_M1     = 0x6B
        CHOPCONF_M1     = 0x6C
        COOLCONF_M1     = 0x6D
        DCCTRL_M1       = 0x6E
        DRV_STATUS_M1   = 0x6F
        MSCNT_M2        = 0x7A
        MSCURACT_M2     = 0x7B
        CHOPCONF_M2     = 0x7C
        COOLCONF_M2     = 0x7D
        DCCTRL_M2       = 0x7E
        DRV_STATUS_M2   = 0x7F

    class FIELD(object):
        """
        Define all register bitfields of the TMC5072.

        Each field is defined as a tuple consisting of ( Address, Mask, Shift ).
        Fields that are present multiple times in different registers (for multiple
        motors) all of the bitfield tuples are bundled together into another tuple.

        The name of the register is written as a comment behind each tuple. This is
        intended for IDE users viewing the definition of a field by hovering over
        it. This allows the user to see the corresponding register name of a field
        without opening this file and searching for the definition.
        """

        # GCONF
        SINGLE_DRIVER      = (0x00, 0x00000001,  0)
        STEPDIR1_ENABLE    = (0x00, 0x00000002,  1)
        STEPDIR2_ENABLE    = (0x00, 0x00000004,  2)
        POSCMP_ENABLE      = (0x00, 0x00000008,  3)
        ENC1_REFSEL        = (0x00, 0x00000010,  4)
        ENC2_ENABLE        = (0x00, 0x00000020,  5)
        ENC2_REFSEL        = (0x00, 0x00000040,  6)
        TEST_MODE          = (0x00, 0x00000080,  7)
        SHAFT1             = (0x00, 0x00000100,  8)
        SHAFT2             = (0x00, 0x00000200,  9)
        LOCK_GCONF         = (0x00, 0x00000400, 10)
        DC_SYNC            = (0x00, 0x00000800, 11)

        # GSTAT
        RESET              = (0x01, 0x00000001,  0)
        DRV_ERR1           = (0x01, 0x00000002,  1)
        DRV_ERR2           = (0x01, 0x00000004,  2)
        UV_CP              = (0x01, 0x00000008,  3)

        # IFCNT
        IFCNT              = (0x02, 0x000000FF,  0)

        # SLAVECONF
        SLAVEADDR          = (0x03, 0x0000000F,  0)
        SENDDELAY          = (0x03, 0x000000F0,  4)

        # INPUT / OUTPUT
        IO0_IN             = (0x04, 0x00000001,  0)
        IO1_IN             = (0x04, 0x00000002,  1)
        IO2_IN             = (0x04, 0x00000004,  2)
        IO3_IN             = (0x04, 0x00000008,  3)
        IOP_IN             = (0x04, 0x00000010,  4)
        ION_IN             = (0x04, 0x00000020,  5)
        NEXTADDR_IN        = (0x04, 0x00000040,  6)
        DRV_ENN            = (0x04, 0x00000080,  7)
        SW_COMP_IN         = (0x04, 0x00000100,  8)
        VERSION            = (0x04, 0xFF000000, 24)

        IO0_OUT            = (0x04, 0x00000001,  0)
        IO1_OUT            = (0x04, 0x00000002,  1)
        IO2_OUT            = (0x04, 0x00000004,  2)
        IODDR0             = (0x04, 0x00000100,  8)
        IODDR1             = (0x04, 0x00000200,  9)
        IODDR2             = (0x04, 0x00000400, 10)

        # X_COMPARE
        X_COMPARE          = (0x05, 0xFFFFFFFF,  0)

        # PWMCONF_M1
        PWM_AMPL_M1        = (0x10, 0x000000FF,  0)
        PWM_GRAD_M1        = (0x10, 0x0000FF00,  8)
        PWM_FREQ_M1        = (0x10, 0x00030000, 16)
        PWM_AUTOSCALE_M1   = (0x10, 0x00040000, 18)
        PWM_SYMMETRIC_M1   = (0x10, 0x00080000, 19)
        FREEWHEEL_M1       = (0x10, 0x00300000, 20)

        # PWM_STATUS_M1
        PWM_STATUS_M1         = (0x11, 0x000000FF,  0)

        # PWMCONF_M2
        PWM_AMPL_M2           = (0x18, 0x000000FF,  0)
        PWM_GRAD_M2           = (0x18, 0x0000FF00,  8)
        PWM_FREQ_M2           = (0x18, 0x00030000, 16)
        PWM_AUTOSCALE_M2      = (0x18, 0x00040000, 18)
        PWM_SYMMETRIC_M2      = (0x18, 0x00080000, 19)
        FREEWHEEL_M2          = (0x18, 0x00300000, 20)

        # PWM_STATUS_M2
        PWM_STATUS_M2         = (0x19, 0x000000FF,  0)

        # RAMPMODE_M1
        RAMPMODE_M1           = (0x20, 0x00000003,  0)

        # XACTUAL_M1
        XACTUAL_M1            = (0x21, 0xFFFFFFFF,  0)

        # VACTUAL_M1
        VACTUAL_M1            = (0x22, 0x00FFFFFF,  0)

        # VSTART_M1
        VSTART_M1             = (0x23, 0x0003FFFF,  0)

        # A1_M1
        A1_M1                 = (0x24, 0x0000FFFF,  0)

        # V1_M1
        V1_M1                = (0x25, 0x000FFFFF,  0)

        # AMAX_M1
        AMAX_M1               = (0x26, 0x0000FFFF,  0)

        # VMAX_M1
        VMAX_M1               = (0x27, 0x007FFFFF,  0)

        # DMAX_M1
        DMAX_M1               = (0x28, 0x0000FFFF,  0)

        # D1_M1
        D1_M1                 = (0x2A, 0x0000FFFF,  0)

        # VSTOP_M1
        VSTOP_M1              = (0x2B, 0x0003FFFF,  0)

        # TZEROWAIT_M1
        TZEROWAIT_M1          = (0x2C, 0x0000FFFF,  0)

        # XTARGET_M1
        XTARGET_M1            = (0x2D, 0xFFFFFFFF,  0)

        # RAMPMODE_M2
        RAMPMODE_M2           = (0x40, 0x00000003,  0)

        # XACTUAL_M2
        XACTUAL_M2            = (0x41, 0xFFFFFFFF,  0)

        # VACTUAL_M2
        VACTUAL_M2            = (0x42, 0x00FFFFFF,  0)

        # VSTART_M2
        VSTART_M2             = (0x43, 0x0003FFFF,  0)

        # A1_M2
        A1_M2                 = (0x44, 0x0000FFFF,  0)

        # V1_M2
        V1_M2                = (0x45, 0x000FFFFF,  0)

        # AMAX_M2
        AMAX_M2               = (0x46, 0x0000FFFF,  0)

        # VMAX_M2
        VMAX_M2               = (0x47, 0x007FFFFF,  0)

        # DMAX_M2
        DMAX_M2               = (0x48, 0x0000FFFF,  0)

        # D1_M2
        D1_M2                 = (0x4A, 0x0000FFFF,  0)

        # VSTOP_M2
        VSTOP_M2              = (0x4B, 0x0003FFFF,  0)

        # TZEROWAIT_M2
        TZEROWAIT_M2          = (0x4C, 0x0000FFFF,  0)

        # XTARGET_M2
        XTARGET_M2            = (0x4D, 0xFFFFFFFF,  0)

        # IHOLD_IRUN_M1
        IHOLD_M1              = (0x30, 0x0000001F,  0)
        IRUN_M1               = (0x30, 0x00001F00,  8)
        IHOLDDELAY_M1         = (0x30, 0x000F0000, 16)

        # VCOOLTHRS_M1
        VCOOLTHRS_M1          = (0x31, 0x007FFFFF,  0)

        # VHIGH_M1
        VHIGH_M1              = (0x32, 0x007FFFFF,  0)

        # VDCMIN_M1
        VDCMIN_M1             = (0x33, 0x007FFFFF,  0)

        # SW_MODE_M1
        STOP_L_ENABLE_M1      = (0x34, 0x00000001,  0)
        STOP_R_ENABLE_M1      = (0x34, 0x00000002,  1)
        POL_STOP_L_M1         = (0x34, 0x00000004,  2)
        POL_STOP_R_M1         = (0x34, 0x00000008,  3)
        SWAP_LR_M1            = (0x34, 0x00000010,  4)
        LATCH_L_ACTIVE_M1     = (0x34, 0x00000020,  5)
        LATCH_L_INACTIVE_M1   = (0x34, 0x00000040,  6)
        LATCH_R_ACTIVE_M1     = (0x34, 0x00000080,  7)
        LATCH_R_INACTIVE_M1   = (0x34, 0x00000100,  8)
        EN_LATCH_ENCODER_M1   = (0x34, 0x00000200,  9)
        SG_STOP_M1            = (0x34, 0x00000400, 10)
        EN_SOFTSTOP_M1        = (0x34, 0x00000800, 11)

        # RAMP_STAT_M1
        STATUS_STOP_L_M1      = (0x35, 0x00000001,  0)
        STATUS_STOP_R_M1      = (0x35, 0x00000002,  1)
        STATUS_LATCH_L_M1     = (0x35, 0x00000004,  2)
        STATUS_LATCH_R_M1     = (0x35, 0x00000008,  3)
        EVENT_STOP_L_M1       = (0x35, 0x00000010,  4)
        EVENT_STOP_R_M1       = (0x35, 0x00000020,  5)
        EVENT_STOP_SG_M1      = (0x35, 0x00000040,  6)
        EVENT_POS_REACHED_M1  = (0x35, 0x00000080,  7)
        VELOCITY_REACHED_M1   = (0x35, 0x00000100,  8)
        POSITION_REACHED_M1   = (0x35, 0x00000200,  9)
        VZERO_M1              = (0x35, 0x00000400, 10)
        T_ZEROWAIT_ACTIVE_M1  = (0x35, 0x00000800, 11)
        SECOND_MOVE_M1        = (0x35, 0x00001000, 12)
        STATUS_SG_M1          = (0x35, 0x00002000, 13)

        # XLATCH_M1
        XLATCH_M1             = (0x36, 0xFFFFFFFF,  0)

        # IHOLD_IRUN_M2
        IHOLD_M2              = (0x50, 0x0000001F,  0)
        IRUN_M2               = (0x50, 0x00001F00,  8)
        IHOLDDELAY_M2         = (0x50, 0x000F0000, 16)

        # VCOOLTHRS_M2
        VCOOLTHRS_M2          = (0x51, 0x007FFFFF,  0)

        # VHIGH_M2
        VHIGH_M2              = (0x52, 0x007FFFFF,  0)

        # VDCMIN_M2
        VDCMIN_M2             = (0x53, 0x007FFFFF,  0)

        # SW_MODE_M2
        STOP_L_ENABLE_M2      = (0x54, 0x00000001,  0)
        STOP_R_ENABLE_M2      = (0x54, 0x00000002,  1)
        POL_STOP_L_M2         = (0x54, 0x00000004,  2)
        POL_STOP_R_M2         = (0x54, 0x00000008,  3)
        SWAP_LR_M2            = (0x54, 0x00000010,  4)
        LATCH_L_ACTIVE_M2     = (0x54, 0x00000020,  5)
        LATCH_L_INACTIVE_M2   = (0x54, 0x00000040,  6)
        LATCH_R_ACTIVE_M2     = (0x54, 0x00000080,  7)
        LATCH_R_INACTIVE_M2   = (0x54, 0x00000100,  8)
        EN_LATCH_ENCODER_M2   = (0x54, 0x00000200,  9)
        SG_STOP_M2            = (0x54, 0x00000400, 10)
        EN_SOFTSTOP_M2        = (0x54, 0x00000800, 11)

        # RAMP_STAT_M2
        STATUS_STOP_L_M2      = (0x55, 0x00000001,  0)
        STATUS_STOP_R_M2      = (0x55, 0x00000002,  1)
        STATUS_LATCH_L_M2     = (0x55, 0x00000004,  2)
        STATUS_LATCH_R_M2     = (0x55, 0x00000008,  3)
        EVENT_STOP_L_M2       = (0x55, 0x00000010,  4)
        EVENT_STOP_R_M2       = (0x55, 0x00000020,  5)
        EVENT_STOP_SG_M2      = (0x55, 0x00000040,  6)
        EVENT_POS_REACHED_M2  = (0x55, 0x00000080,  7)
        VELOCITY_REACHED_M2   = (0x55, 0x00000100,  8)
        POSITION_REACHED_M2   = (0x55, 0x00000200,  9)
        VZERO_M2              = (0x55, 0x00000400, 10)
        T_ZEROWAIT_ACTIVE_M2  = (0x55, 0x00000800, 11)
        SECOND_MOVE_M2        = (0x55, 0x00001000, 12)
        STATUS_SG_M2          = (0x55, 0x00002000, 13)

        # XLATCH_M2
        XLATCH_M2             = (0x56, 0xFFFFFFFF,  0)

        # ENCMODE_M1
        POL_A_M1              = (0x38, 0x00000001,  0)
        POL_B_M1              = (0x38, 0x00000002,  1)
        POL_N_M1              = (0x38, 0x00000004,  2)
        IGNORE_AB_M1          = (0x38, 0x00000008,  3)
        CLR_CONT_M1           = (0x38, 0x00000010,  4)
        CLR_ONCE_M1           = (0x38, 0x00000020,  5)
        POS_EDGE_NEG_EDGE_M1  = (0x38, 0x000000C0,  6)
        CLR_ENC_X_M1          = (0x38, 0x00000100,  8)
        LATCH_X_ACT_M1        = (0x38, 0x00000200,  9)
        ENC_SEL_DECIMAL_M1    = (0x38, 0x00000400, 10)
        LATCH_NOW_M1          = (0x38, 0x00000800, 11)

        # X_ENC_M1
        X_ENC_M1              = (0x39, 0xFFFFFFFF,  0)

        # ENC_CONST_M1
        INTEGER_M1            = (0x3A, 0xFFFF0000, 16)
        FRACTIONAL_M1         = (0x3A, 0x0000FFFF,  0)

        # ENC_STATUS_M1
        ENC_STATUS_M1         = (0x3B, 0x00000001,  0)

        # ENC_LATCH_M1
        ENC_LATCH_M1          = (0x3C, 0xFFFFFFFF,  0)

        # ENCMODE_M2
        POL_A_M2              = (0x58, 0x00000001,  0)
        POL_B_M2              = (0x58, 0x00000002,  1)
        POL_N_M2              = (0x58, 0x00000004,  2)
        IGNORE_AB_M2          = (0x58, 0x00000008,  3)
        CLR_CONT_M2           = (0x58, 0x00000010,  4)
        CLR_ONCE_M2           = (0x58, 0x00000020,  5)
        POS_EDGE_NEG_EDGE_M2  = (0x58, 0x000000C0,  6)
        CLR_ENC_X_M2          = (0x58, 0x00000100,  8)
        LATCH_X_ACT_M2        = (0x58, 0x00000200,  9)
        ENC_SEL_DECIMAL_M2    = (0x58, 0x00000400, 10)
        LATCH_NOW_M2          = (0x58, 0x00000800, 11)

        # X_ENC_M2
        X_ENC_M2              = (0x59, 0xFFFFFFFF,  0)

        # ENC_CONST_M2
        FRACTIONAL_M2         = (0x5A, 0x0000FFFF,  0)
        INTEGER_M2            = (0x5A, 0xFFFF0000, 16)

        # ENC_STATUS_M2
        ENC_STATUS_M2         = (0x5B, 0x00000001,  0)

        # ENC_LATCH_M2
        ENC_LATCH_M2          = (0x5C, 0xFFFFFFFF,  0)

        # MSLUTSEL
        W0                    = (0x68, 0x00000003,  0)
        W1                    = (0x68, 0x0000000C,  2)
        W2                    = (0x68, 0x00000030,  4)
        W3                    = (0x68, 0x000000C0,  6)
        X1                    = (0x68, 0x0000FF00,  8)
        X2                    = (0x68, 0x00FF0000, 16)
        X3                    = (0x68, 0xFF000000, 24)

        # MSLUTSTART
        START_SIN             = (0x69, 0x000000FF,  0)
        START_SIN90           = (0x69, 0x00FF0000, 16)

        # MSCNT_M1
        MSCNT_M1              = (0x6A, 0x000003FF,  0)

        # MSCURACT_M1
        CUR_A_M1              = (0x6B, 0x000001FF,  0)
        CUR_B_M1              = (0x6B, 0x01FF0000, 16)

        # CHOPCONF_M1
        TOFF_M1               = (0x6C, 0x0000000F,  0)
        TFD_2_0_M1            = (0x6C, 0x00000070,  4)
        OFFSET_M1             = (0x6C, 0x00000780,  7)
        TFD_M1                = (0x6C, 0x00000800, 11)
        DISFDCC_M1            = (0x6C, 0x00001000, 12)
        RNDTF_M1              = (0x6C, 0x00002000, 13)
        CHM_M1                = (0x6C, 0x00004000, 14)
        TBL_M1                = (0x6C, 0x00018000, 15)
        VSENSE_M1             = (0x6C, 0x00020000, 17)
        VHIGHFS_M1            = (0x6C, 0x00040000, 18)
        VHIGHCHM_M1           = (0x6C, 0x00080000, 19)
        MRES_M1               = (0x6C, 0x0F000000, 24)
        INTPOL_M1             = (0x6C, 0x10000000, 28)
        DEDGE_M1              = (0x6C, 0x20000000, 29)
        DISS2G_M1             = (0x6C, 0x40000000, 30)

        # COOLCONF_M1
        SEMIN_M1              = (0x6D, 0x0000000F,  0)
        SEUP_M1               = (0x6D, 0x00000060,  5)
        SEMAX_M1              = (0x6D, 0x00000F00,  8)
        SEDN_M1               = (0x6D, 0x00006000, 13)
        SEIMIN_M1             = (0x6D, 0x00008000, 15)
        SGT_M1                = (0x6D, 0x007F0000, 16)
        SFILT_M1              = (0x6D, 0x01000000, 24)

        # DCCTRL_M1
        DC_TIME_M1            = (0x6E, 0x000003FF,  0)
        DC_SG_M1              = (0x6E, 0x00FF0000, 16)

        # DRV_STATUS_M1
        SG_RESULT_M1          = (0x6F, 0x000003FF,  0)
        FSACTIVE_M1           = (0x6F, 0x00008000, 15)
        CS_ACTUAL_M1          = (0x6F, 0x001F0000, 16)
        STALLGUARD_M1         = (0x6F, 0x01000000, 24)
        OT_M1                 = (0x6F, 0x02000000, 25)
        OTPW_M1               = (0x6F, 0x04000000, 26)
        S2GA_M1               = (0x6F, 0x08000000, 27)
        S2GB_M1               = (0x6F, 0x10000000, 28)
        OLA_M1                = (0x6F, 0x20000000, 29)
        OLB_M1                = (0x6F, 0x40000000, 30)
        STST_M1               = (0x6F, 0x80000000, 31)

        # MSCNT_M2
        MSCNT_M2              = (0x7A, 0x000003FF,  0)

        # MSCURACT_M2
        CUR_A_M2              = (0x7B, 0x000001FF,  0)
        CUR_B_M2              = (0x7B, 0x01FF0000, 16)

        # CHOPCONF_M2
        TOFF_M2               = (0x7C, 0x0000000F,  0)
        TFD_2_0_M2            = (0x7C, 0x00000070,  4)
        OFFSET_M2             = (0x7C, 0x00000780,  7)
        TFD_M2                = (0x7C, 0x00000800, 11)
        DISFDCC_M2            = (0x7C, 0x00001000, 12)
        RNDTF_M2              = (0x7C, 0x00002000, 13)
        CHM_M2                = (0x7C, 0x00004000, 14)
        TBL_M2                = (0x7C, 0x00018000, 15)
        VSENSE_M2             = (0x7C, 0x00020000, 17)
        VHIGHFS_M2            = (0x7C, 0x00040000, 18)
        VHIGHCHM_M2           = (0x7C, 0x00080000, 19)
        MRES_M2               = (0x7C, 0x0F000000, 24)
        INTPOL_M2             = (0x7C, 0x10000000, 28)
        DEDGE_M2              = (0x7C, 0x20000000, 29)
        DISS2G_M2             = (0x7C, 0x40000000, 30)

        # COOLCONF_M2
        SEMIN_M2              = (0x7D, 0x0000000F,  0)
        SEUP_M2               = (0x7D, 0x00000060,  5)
        SEMAX_M2              = (0x7D, 0x00000F00,  8)
        SEDN_M2               = (0x7D, 0x00006000, 13)
        SEIMIN_M2             = (0x7D, 0x00008000, 15)
        SGT_M2                = (0x7D, 0x007F0000, 16)
        SFILT_M2              = (0x7D, 0x01000000, 24)

        # DCCTRL_M2
        DC_TIME_M2            = (0x7E, 0x000003FF,  0)
        DC_SG_M2              = (0x7E, 0x00FF0000, 16)

        # DRV_STATUS_M2
        SG_RESULT_M2          = (0x7F, 0x000003FF,  0)
        FSACTIVE_M2           = (0x7F, 0x00008000, 15)
        CS_ACTUAL_M2          = (0x7F, 0x001F0000, 16)
        STALLGUARD_M2         = (0x7F, 0x01000000, 24)
        OT_M2                 = (0x7F, 0x02000000, 25)
        OTPW_M2               = (0x7F, 0x04000000, 26)
        S2GA_M2               = (0x7F, 0x08000000, 27)
        S2GB_M2               = (0x7F, 0x10000000, 28)
        OLA_M2                = (0x7F, 0x20000000, 29)
        OLB_M2                = (0x7F, 0x40000000, 30)
        STST_M2               = (0x7F, 0x80000000, 31)

        PWM_AMPL = [PWM_AMPL_M1, PWM_AMPL_M2]
        PWM_GRAD = [PWM_GRAD_M1, PWM_GRAD_M2]
        PWM_FREQ = [PWM_FREQ_M1, PWM_FREQ_M2]
        PWM_AUTOSCALE = [PWM_AUTOSCALE_M1, PWM_AUTOSCALE_M2]
        PWM_SYMMETRIC = [PWM_SYMMETRIC_M1, PWM_SYMMETRIC_M2]
        FREEWHEEL = [FREEWHEEL_M1, FREEWHEEL_M2]
        PWM_STATUS = [PWM_STATUS_M1, PWM_STATUS_M2]
        RAMPMODE = [RAMPMODE_M1, RAMPMODE_M2]
        XACTUAL = [XACTUAL_M1, XACTUAL_M2]
        VACTUAL = [VACTUAL_M1, VACTUAL_M2]
        VSTART = [VSTART_M1, VSTART_M2]
        A1 = [A1_M1, A1_M2]
        V1 = [V1_M1, V1_M2]
        AMAX = [AMAX_M1, AMAX_M2]
        VMAX = [VMAX_M1, VMAX_M2]
        DMAX = [DMAX_M1, DMAX_M2]
        D1 = [D1_M1, D1_M2]
        VSTOP = [VSTOP_M1, VSTOP_M2]
        TZEROWAIT = [TZEROWAIT_M1, TZEROWAIT_M2]
        XTARGET = [XTARGET_M1, XTARGET_M2]
        IHOLD = [IHOLD_M1, IHOLD_M2]
        IRUN = [IRUN_M1, IRUN_M2]
        IHOLDDELAY = [IHOLDDELAY_M1, IHOLDDELAY_M2]
        VCOOLTHRS = [VCOOLTHRS_M1, VCOOLTHRS_M2]
        VHIGH = [VHIGH_M1, VHIGH_M2]
        VDCMIN = [VDCMIN_M1, VDCMIN_M2]
        STOP_L_ENABLE = [STOP_L_ENABLE_M1, STOP_L_ENABLE_M2]
        STOP_R_ENABLE = [STOP_R_ENABLE_M1, STOP_R_ENABLE_M2]
        POL_STOP_L = [POL_STOP_L_M1, POL_STOP_L_M2]
        POL_STOP_R = [POL_STOP_R_M1, POL_STOP_R_M2]
        SWAP_LR = [SWAP_LR_M1, SWAP_LR_M2]
        LATCH_L_ACTIVE = [LATCH_L_ACTIVE_M1, LATCH_L_ACTIVE_M2]
        LATCH_L_INACTIVE = [LATCH_L_INACTIVE_M1, LATCH_L_INACTIVE_M2]
        LATCH_R_ACTIVE = [LATCH_R_ACTIVE_M1, LATCH_R_ACTIVE_M2]
        LATCH_R_INACTIVE = [LATCH_R_INACTIVE_M1, LATCH_R_INACTIVE_M2]
        EN_LATCH_ENCODER = [EN_LATCH_ENCODER_M1, EN_LATCH_ENCODER_M2]
        SG_STOP = [SG_STOP_M1, SG_STOP_M2]
        EN_SOFTSTOP = [EN_SOFTSTOP_M1, EN_SOFTSTOP_M2]
        STATUS_STOP_L = [STATUS_STOP_L_M1, STATUS_STOP_L_M2]
        STATUS_STOP_R = [STATUS_STOP_R_M1, STATUS_STOP_R_M2]
        STATUS_LATCH_L = [STATUS_LATCH_L_M1, STATUS_LATCH_L_M2]
        STATUS_LATCH_R = [STATUS_LATCH_R_M1, STATUS_LATCH_R_M2]
        EVENT_STOP_L = [EVENT_STOP_L_M1, EVENT_STOP_L_M2]
        EVENT_STOP_R = [EVENT_STOP_R_M1, EVENT_STOP_R_M2]
        EVENT_STOP_SG = [EVENT_STOP_SG_M1, EVENT_STOP_SG_M2]
        EVENT_POS_REACHED = [EVENT_POS_REACHED_M1, EVENT_POS_REACHED_M2]
        VELOCITY_REACHED = [VELOCITY_REACHED_M1, VELOCITY_REACHED_M2]
        POSITION_REACHED = [POSITION_REACHED_M1, POSITION_REACHED_M2]
        VZERO = [VZERO_M1, VZERO_M2]
        T_ZEROWAIT_ACTIVE = [T_ZEROWAIT_ACTIVE_M1, T_ZEROWAIT_ACTIVE_M2]
        SECOND_MOVE = [SECOND_MOVE_M1, SECOND_MOVE_M2]
        STATUS_SG = [STATUS_SG_M1, STATUS_SG_M2]
        XLATCH = [XLATCH_M1, XLATCH_M2]
        POL_A = [POL_A_M1, POL_A_M2]
        POL_B = [POL_B_M1, POL_B_M2]
        POL_N = [POL_N_M1, POL_N_M2]
        IGNORE_AB = [IGNORE_AB_M1, IGNORE_AB_M2]
        CLR_CONT = [CLR_CONT_M1, CLR_CONT_M2]
        CLR_ONCE = [CLR_ONCE_M1, CLR_ONCE_M2]
        POS_EDGE_NEG_EDGE = [POS_EDGE_NEG_EDGE_M1, POS_EDGE_NEG_EDGE_M2]
        CLR_ENC_X = [CLR_ENC_X_M1, CLR_ENC_X_M2]
        LATCH_X_ACT = [LATCH_X_ACT_M1, LATCH_X_ACT_M2]
        ENC_SEL_DECIMAL = [ENC_SEL_DECIMAL_M1, ENC_SEL_DECIMAL_M2]
        LATCH_NOW = [LATCH_NOW_M1, LATCH_NOW_M2]
        X_ENC = [X_ENC_M1, X_ENC_M2]
        INTEGER = [INTEGER_M1, INTEGER_M2]
        FRACTIONAL = [FRACTIONAL_M1, FRACTIONAL_M2]
        ENC_STATUS = [ENC_STATUS_M1, ENC_STATUS_M2]
        ENC_LATCH = [ENC_LATCH_M1, ENC_LATCH_M2]
        MSCNT = [MSCNT_M1, MSCNT_M2]
        CUR_A = [CUR_A_M1, CUR_A_M2]
        CUR_B = [CUR_B_M1, CUR_B_M2]
        TOFF = [TOFF_M1, TOFF_M2]
        TFD_2_0 = [TFD_2_0_M1, TFD_2_0_M2]
        OFFSET = [OFFSET_M1, OFFSET_M2]
        TFD = [TFD_M1, TFD_M2]
        DISFDCC = [DISFDCC_M1, DISFDCC_M2]
        RNDTF = [RNDTF_M1, RNDTF_M2]
        CHM = [CHM_M1, CHM_M2]
        TBL = [TBL_M1, TBL_M2]
        VSENSE = [VSENSE_M1, VSENSE_M2]
        VHIGHFS = [VHIGHFS_M1, VHIGHFS_M2]
        VHIGHCHM = [VHIGHCHM_M1, VHIGHCHM_M2]
        MRES = [MRES_M1, MRES_M2]
        INTPOL = [INTPOL_M1, INTPOL_M2]
        DEDGE = [DEDGE_M1, DEDGE_M2]
        DISS2G = [DISS2G_M1, DISS2G_M2]
        SEMIN = [SEMIN_M1, SEMIN_M2]
        SEUP = [SEUP_M1, SEUP_M2]
        SEMAX = [SEMAX_M1, SEMAX_M2]
        SEDN = [SEDN_M1, SEDN_M2]
        SEIMIN = [SEIMIN_M1, SEIMIN_M2]
        SGT = [SGT_M1, SGT_M2]
        SFILT = [SFILT_M1, SFILT_M2]
        DC_TIME = [DC_TIME_M1, DC_TIME_M2]
        DC_SG = [DC_SG_M1, DC_SG_M2]
        SG_RESULT = [SG_RESULT_M1, SG_RESULT_M2]
        FSACTIVE = [FSACTIVE_M1, FSACTIVE_M2]
        CS_ACTUAL = [CS_ACTUAL_M1, CS_ACTUAL_M2]
        STALLGUARD = [STALLGUARD_M1, STALLGUARD_M2]
        OT = [OT_M1, OT_M2]
        OTPW = [OTPW_M1, OTPW_M2]
        S2GA = [S2GA_M1, S2GA_M2]
        S2GB = [S2GB_M1, S2GB_M2]
        OLA = [OLA_M1, OLA_M2]
        OLB = [OLB_M1, OLB_M2]
        STST = [STST_M1, STST_M2]
