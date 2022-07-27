from ..ic.tmc_ic import TMCIc

# features
from ..features.motor_control_ic import MotorControlIc
# from pytrinamic.features.linear_ramp_ic import LinearRampIC
# from pytrinamic.features.current_ic import CurrentIC
# from pytrinamic.features.stallguard2_ic import StallGuard2IC


class TMC5130(TMCIc):
    """
    The TMC5130 is a high-performance stepper motor controller and driver IC with serial communication interfaces.
    Supply voltage: 4,75-46V
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
        super().__init__("TMC5130", self.__doc__)
        self._parent = parent_eval
        self.motors = [self.MotorTypeA(parent_eval, self, 0)]

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
        Define all registers of the TMC5130.

        Each register is defined either as an integer or as a tuple of integers.
        Each integer represents a register address. Tuples of addresses are used to
        represent a register that exists multiple times for multiple motors.
        """
        GCONF          = 0x00
        GSTAT          = 0x01
        IFCNT          = 0x02
        SLAVECONF      = 0x03
        IOIN_OUTPUT    = 0x04
        X_COMPARE      = 0x05
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
        MSLUT_0        = 0x60
        MSLUT_1        = 0x61
        MSLUT_2        = 0x62
        MSLUT_3        = 0x63
        MSLUT_4        = 0x64
        MSLUT_5        = 0x65
        MSLUT_6        = 0x66
        MSLUT_7        = 0x67
        MSLUTSEL       = 0x68
        MSLUTSTART     = 0x69
        MSCNT          = 0x6A
        MSCURACT       = 0x6B
        CHOPCONF       = 0x6C
        COOLCONF       = 0x6D
        DCCTRL         = 0x6E
        DRV_STATUS     = 0x6F
        PWMCONF        = 0x70
        PWM_SCALE      = 0x71
        ENCM_CTRL      = 0x72
        LOST_STEPS     = 0x73

    class FIELD:
        """
        Define all register bitfields of the TMC5130.

        Each field is defined as a tuple consisting of ( Address, Mask, Shift ).

        The name of the register is written as a comment behind each tuple. This is
        intended for IDE users viewing the definition of a field by hovering over
        it. This allows the user to see the corresponding register name of a field
        without opening this file and searching for the definition.
        """

        # GCONF
        I_SCALE_ANALOG                     = (0x00, 0x00000001,  0)
        INTERNAL_RSENSE                    = (0x00, 0x00000002,  1)
        EN_PWM_MODE                        = (0x00, 0x00000004,  2)
        ENC_COMMUTATION                    = (0x00, 0x00000008,  3)
        SHAFT                              = (0x00, 0x00000010,  4)
        DIAG0_ERROR__ONLY_WITH_SD_MODE_1_  = (0x00, 0x00000020,  5)
        DIAG0_OTPW__ONLY_WITH_SD_MODE_1_   = (0x00, 0x00000040,  6)
        DIAG0_STALL                        = (0x00, 0x00000080,  7)
        DIAG0_STEP                         = (0x00, 0x00000080,  7)
        DIAG1_STALL                        = (0x00, 0x00000100,  8)
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

        # IFCNT
        IFCNT                              = (0x02, 0x000000FF,  0)

        # SLAVECONF
        SLAVEADDR                          = (0x03, 0x000000FF,  0)
        SENDDELAY                          = (0x03, 0x00000F00,  8)

        # IOIN / OUTPUT
        REFL_STEP                          = (0x04, 0x00000001,  0)
        OUTPUT_PIN_POLARITY                = (0x04, 0x00000001,  0)
        REFR_DIR                           = (0x04, 0x00000002,  1)
        ENCB_DCEN_CFG4                     = (0x04, 0x00000004,  2)
        ENCA_DCIN_CFG5                     = (0x04, 0x00000008,  3)
        DRV_ENN_CFG6                       = (0x04, 0x00000010,  4)
        ENC_N_DCO                          = (0x04, 0x00000020,  5)
        SD_MODE                            = (0x04, 0x00000040,  6)
        SWCOMP_IN                          = (0x04, 0x00000080,  7)
        VERSION                            = (0x04, 0xFF000000, 24)

        # X_COMPARE
        X_COMPARE                          = (0x05, 0xFFFFFFFF,  0)

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
        V1                                 = (0x25, 0x000FFFFF,  0)

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
        INTEGER                            = (0x3A, 0xFFFF0000, 16)
        FRACTIONAL                         = (0x3A, 0x0000FFFF,  0)

        # ENC_STATUS
        ENC_STATUS                         = (0x3B, 0x00000001,  0)

        # ENC_LATCH
        ENC_LATCH                          = (0x3C, 0xFFFFFFFF,  0)

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
        HSTRT                              = (0x6C, 0x00000070,  4)
        OFFSET                             = (0x6C, 0x00000780,  7)
        HEND                               = (0x6C, 0x00000780,  7)
        TFD__                              = (0x6C, 0x00000800, 11)
        DISFDCC                            = (0x6C, 0x00001000, 12)
        RNDTF                              = (0x6C, 0x00002000, 13)
        CHM                                = (0x6C, 0x00004000, 14)
        TBL                                = (0x6C, 0x00018000, 15)
        VSENSE                             = (0x6C, 0x00020000, 17)
        VHIGHFS                            = (0x6C, 0x00040000, 18)
        VHIGHCHM                           = (0x6C, 0x00080000, 19)
        SYNC                               = (0x6C, 0x00F00000, 20)
        MRES                               = (0x6C, 0x0F000000, 24)
        INTPOL                             = (0x6C, 0x10000000, 28)
        DEDGE                              = (0x6C, 0x20000000, 29)
        DISS2G                             = (0x6C, 0x40000000, 30)

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
        PWM_AMPL                           = (0x70, 0x000000FF,  0)
        PWM_GRAD                           = (0x70, 0x0000FF00,  8)
        PWM_FREQ                           = (0x70, 0x00030000, 16)
        PWM_AUTOSCALE                      = (0x70, 0x00040000, 18)
        PWM_SYMMETRIC                      = (0x70, 0x00080000, 19)
        FREEWHEEL                          = (0x70, 0x00300000, 20)

        # PWM_SCALE
        PWM_SCALE                          = (0x71, 0x000000FF,  0)

        # ENCM_CTRL
        INV                                = (0x72, 0x00000001,  0)
        MAXSPEED                           = (0x72, 0x00000002,  1)

        # LOST_STEPS
        LOST_STEPS                         = (0x73, 0x000FFFFF,  0)
