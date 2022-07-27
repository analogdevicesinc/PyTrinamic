from ..ic.tmc_ic import TMCIc


class TMC4361(TMCIc):
    """
    The TMC4361 is a miniaturized high-performance motion controller for stepper motor drivers.
    """
    def __init__(self):
        super().__init__("TMC4361", self.__doc__)

    class REG:
        """
        Define all registers of the TMC4361.
        """
        GENERAL_CONF                                  = 0x00
        REFERENCE_CONF                                = 0x01
        START_CONF                                    = 0x02
        INPUT_FILT_CONF                               = 0x03
        SPI_OUT_CONF                                  = 0x04
        CURRENT_CONF                                  = 0x05
        SCALE_VALUES                                  = 0x06
        ENC_IN_CONF                                   = 0x07
        ENC_IN_DATA                                   = 0x08
        ENC_OUT_DATA                                  = 0x09
        STEP_CONF                                     = 0x0A
        SPI_STATUS_SELECTION                          = 0x0B
        EVENT_CLEAR_CONF                              = 0x0C
        INTR_CONF                                     = 0x0D
        EVENTS                                        = 0x0E
        STATUS                                        = 0x0F
        STP_LENGTH_ADD___DIR_SETUP_TIME               = 0x10
        START_OUT_ADD                                 = 0x11
        GEAR_RATIO                                    = 0x12
        START_DELAY                                   = 0x13
        CLK_GATING_DELAY                              = 0x14
        STDBY_DELAY                                   = 0x15
        FREEWHEEL_DELAY                               = 0x16
        VDRV_SCALE_LIMIT___PWM_VMAX                   = 0x17
        UP_SCALE_DELAY___CL_UPSCALE_DELAY             = 0x18
        HOLD_SCALE_DELAY___CL_DNSCALE_DELAY           = 0x19
        DRV_SCALE_DELAY                               = 0x1A
        BOOST_TIME                                    = 0x1B
        CL_ANGLES                                     = 0x1C
        SPI_SWITCH_VEL___DAC_ADDR                     = 0x1D
        HOME_SAFETY_MARGIN                            = 0x1E
        PWM_FREQ___CHOPSYNC_DIV                       = 0x1F
        RAMPMODE                                      = 0x20
        XACTUAL                                       = 0x21
        VACTUAL                                       = 0x22
        AACTUAL                                       = 0x23
        VMAX                                          = 0x24
        VSTART                                        = 0x25
        VSTOP                                         = 0x26
        VBREAK                                        = 0x27
        AMAX                                          = 0x28
        DMAX                                          = 0x29
        ASTART                                        = 0x2A
        DFINAL                                        = 0x2B
        DSTOP                                         = 0x2C
        BOW1                                          = 0x2D
        BOW2                                          = 0x2E
        BOW3                                          = 0x2F
        BOW4                                          = 0x30
        CLK_FREQ                                      = 0x31
        POS_COMP                                      = 0x32
        VIRT_STOP_LEFT                                = 0x33
        VIRT_STOP_RIGHT                               = 0x34
        X_HOME                                        = 0x35
        X_LATCH___REV_CNT___X_RANGE                   = 0x36
        XTARGET                                       = 0x37
        X_PIPE0                                       = 0x38
        X_PIPE1                                       = 0x39
        X_PIPE2                                       = 0x3A
        X_PIPE3                                       = 0x3B
        X_PIPE4                                       = 0x3C
        X_PIPE5                                       = 0x3D
        X_PIPE6                                       = 0x3E
        X_PIPE7                                       = 0x3F
        SH_REG0                                       = 0x40
        SH_REG1                                       = 0x41
        SH_REG2                                       = 0x42
        SH_REG3                                       = 0x43
        SH_REG4                                       = 0x44
        SH_REG5                                       = 0x45
        SH_REG6                                       = 0x46
        SH_REG7                                       = 0x47
        SH_REG8                                       = 0x48
        SH_REG9                                       = 0x49
        SH_REG10                                      = 0x4A
        SH_REG11                                      = 0x4B
        SH_REG12                                      = 0x4C
        SH_REG13                                      = 0x4D
        Freeze_Registers                              = 0x4E
        ENC_POS                                       = 0x50
        ENC_LATCH___ENC_RESET_VAL                     = 0x51
        ENC_POS_DEV___CL_TR_TOLERANCE                 = 0x52
        ENC_POS_DEV_TOL                               = 0x53
        ENC_IN_RES___ENC_CONST                        = 0x54
        ENC_OUT_RES                                   = 0x55
        SER_CLK_IN_HIGH_LOW                           = 0x56
        SSI_IN_CLK_DELAY___SSI_IN_WTIME               = 0x57
        SER_PTIME                                     = 0x58
        CL_OFFSET                                     = 0x59
        PID_VEL___PID_P___CL_VMAX_CALC_P              = 0x5A
        PID_ISUM_RD___PID_I___CL_VMAX_CALC_I          = 0x5B
        PID_D___CL_DELTA_P                            = 0x5C
        PID_E___PID_I_CLIP___PID_D_CLKDIV             = 0x5D
        PID_DV_CLIP                                   = 0x5E
        PID_TOLERANCE___CL_TOLERANCE                  = 0x5F
        FS_VEL___DC_VEL___CL_VMIN_EMF                 = 0x60
        DC_TIME___DC_SG___DC_BLKTIME___CL_VADD_EMF    = 0x61
        DC_LSPTM___ENC_VEL_ZERO                       = 0x62
        ENC_VMEAN_______SER_ENC_VARIATION___CL_CYCLE  = 0x63
        V_ENC                                         = 0x65
        V_ENC_MEAN                                    = 0x66
        VSTALL_LIMIT                                  = 0x67
        ADDR_TO_ENC                                   = 0x68
        DATA_TO_ENC                                   = 0x69
        ADDR_FROM_ENC                                 = 0x6A
        DATA_FROM_ENC                                 = 0x6B
        COVER_LOW                                     = 0x6C
        COVER_HIGH___POLLING_REG                      = 0x6D
        COVER_DRV_LOW                                 = 0x6E
        COVER_DRV_HIGH                                = 0x6F
        MSLUT__                                       = 0x70
        MSLUTSEL                                      = 0x78
        MSCNT                                         = 0x79
        CURRENTA_B                                    = 0x7A
        CURRENTA_B_SPI                                = 0x7B
        SCALE_PARAM___CIRCULAR_DEC                    = 0x7C
        ENC_COMP____                                  = 0x7D
        START_SIN______DAC_OFFSET                     = 0x7E
        VERSION_NO                                    = 0x7F

    class FIELD:
        """
        Define all register bitfields of the TMC4361.

        Each field is defined as a tuple consisting of (Address, Mask, Shift).

        The name of the register is written as a comment behind each tuple. This is
        intended for IDE users viewing the definition of a field by hovering over
        it. This allows the user to see the corresponding register name of a field
        without opening this file and searching for the definition.
        """

        # GENERAL_CONF
        USE_ASTART_AND_VSTART               = (0x00, 0x00000001,  0)
        DIRECT_ACC_VAL_EN                   = (0x00, 0x00000002,  1)
        DIRECT_BOW_VAL_EN                   = (0x00, 0x00000004,  2)
        STEP_INACTIVE_POL                   = (0x00, 0x00000008,  3)
        TOGGLE_STEP                         = (0x00, 0x00000010,  4)
        POL_DIR_OUT                         = (0x00, 0x00000020,  5)
        SDIN_MODE                           = (0x00, 0x000000c0,  6)
        POL_DIR_IN                          = (0x00, 0x00000100,  8)
        SD_INDIRECT_CONTROL                 = (0x00, 0x00000200,  9)
        SERIAL_ENC_IN_MODE                  = (0x00, 0x00000c00, 10)
        DIFF_ENC_IN_DISABLE                 = (0x00, 0x00001000, 12)
        STDBY_CLK_PIN_ASSIGNMENT            = (0x00, 0x00006000, 13)
        INTR_POL                            = (0x00, 0x00008000, 15)
        INVERT_POL_TARGET_REACHED           = (0x00, 0x00010000, 16)
        FS_EN                               = (0x00, 0x00080000, 19)
        FS_SDOUT                            = (0x00, 0x00100000, 20)
        DCSTEP_MODE                         = (0x00, 0x00600000, 21)
        PWM_OUT_EN                          = (0x00, 0x00800000, 23)
        SERIAL_ENC_OUT_ENABLE               = (0x00, 0x01000000, 24)
        SERIAL_ENC_OUT_DIFF_DISABLE         = (0x00, 0x02000000, 25)
        AUTOMATIC_DIRECT_SDIN_SWITCH_OFF    = (0x00, 0x04000000, 26)
        CIRCULAR_CNT_AS_XLATCH              = (0x00, 0x08000000, 27)
        REVERSE_MOTOR_DIR                   = (0x00, 0x10000000, 28)
        INTR_TR_PU_PD_EN                    = (0x00, 0x20000000, 29)
        INTR_AS_WIRED_AND                   = (0x00, 0x40000000, 30)
        TR_AS_WIRED_AND                     = (0x00, 0x80000000, 31)

        # REFERENCE_CONF
        STOP_LEFT_EN                        = (0x01, 0x00000001,  0)
        STOP_RIGHT_EN                       = (0x01, 0x00000002,  1)
        POL_STOP_LEFT                       = (0x01, 0x00000004,  2)
        POL_STOP_RIGHT                      = (0x01, 0x00000008,  3)
        INVERT_STOP_DIRECTION               = (0x01, 0x00000010,  4)
        SOFT_STOP_EN                        = (0x01, 0x00000020,  5)
        VIRTUAL_LEFT_LIMIT_EN               = (0x01, 0x00000040,  6)
        VIRTUAL_RIGHT_LIMIT_EN              = (0x01, 0x00000080,  7)
        VIRT_STOP_MODE                      = (0x01, 0x00000300,  8)
        LATCH_X_ON_INACTIVE_L               = (0x01, 0x00000400, 10)
        LATCH_X_ON_ACTIVE_L                 = (0x01, 0x00000800, 11)
        LATCH_X_ON_INACTIVE_R               = (0x01, 0x00001000, 12)
        LATCH_X_ON_ACTIVE_R                 = (0x01, 0x00002000, 13)
        STOP_LEFT_IS_HOME                   = (0x01, 0x00004000, 14)
        STOP_RIGHT_IS_HOME                  = (0x01, 0x00008000, 15)
        HOME_EVENT                          = (0x01, 0x000f0000, 16)
        START_HOME_TRACKING                 = (0x01, 0x00100000, 20)
        CLR_POS_AT_TARGET                   = (0x01, 0x00200000, 21)
        CIRCULAR_MOVEMENT_EN                = (0x01, 0x00400000, 22)
        POS_COMP_OUTPUT                     = (0x01, 0x01800000, 23)
        POS_COMP_SOURCE                     = (0x01, 0x02000000, 25)
        STOP_ON_STALL                       = (0x01, 0x04000000, 26)
        DRV_AFTER_STALL                     = (0x01, 0x08000000, 27)
        MODIFIED_POS_COPARE                 = (0x01, 0x30000000, 28)
        AUTOMATIC_COVER                     = (0x01, 0x40000000, 30)
        CIRCULAR_ENC_EN                     = (0x01, 0x80000000, 31)

        # START_CONF
        START_EN_0_                         = (0x02, 0x00000001,  0)
        START_EN_1_                         = (0x02, 0x00000002,  1)
        START_EN_2_                         = (0x02, 0x00000004,  2)
        START_EN_3_                         = (0x02, 0x00000008,  3)
        START_EN_4_                         = (0x02, 0x00000010,  4)
        TRIGGER_EVENTS_0_                   = (0x02, 0x00000020,  5)
        TRIGGER_EVENTS_1_                   = (0x02, 0x00000040,  6)
        TRIGGER_EVENTS_2_                   = (0x02, 0x00000080,  7)
        TRIGGER_EVENTS_3_                   = (0x02, 0x00000100,  8)
        POL_START_SIGNAL                    = (0x02, 0x00000200,  9)
        IMMEDIATE_START_IN                  = (0x02, 0x00000400, 10)
        BUSY_STATE_EN                       = (0x02, 0x00000800, 11)
        PIPELINE_EN_0_                      = (0x02, 0x00001000, 12)
        PIPELINE_EN_1_                      = (0x02, 0x00002000, 13)
        PIPELINE_EN_2_                      = (0x02, 0x00004000, 14)
        PIPELINE_EN_3_                      = (0x02, 0x00008000, 15)
        SHADOW_OPTION                       = (0x02, 0x00030000, 16)
        CYCLIC_SHADOW_REGS                  = (0x02, 0x00040000, 18)
        SHADOW_MISS_CNT                     = (0x02, 0x00f00000, 20)
        XPIPE_REWRITE_REG_0_                = (0x02, 0x01000000, 24)
        XPIPE_REWRITE_REG_1_                = (0x02, 0x02000000, 25)
        XPIPE_REWRITE_REG_2_                = (0x02, 0x04000000, 26)
        XPIPE_REWRITE_REG_3_                = (0x02, 0x08000000, 27)
        XPIPE_REWRITE_REG_4_                = (0x02, 0x10000000, 28)
        XPIPE_REWRITE_REG_5_                = (0x02, 0x20000000, 29)
        XPIPE_REWRITE_REG_6_                = (0x02, 0x40000000, 30)
        XPIPE_REWRITE_REG_7_                = (0x02, 0x80000000, 31)

        # INPUT_FILT_CONF
        SR_ENC_IN                           = (0x03, 0x00000007,  0)
        FILT_L_ENC_IN                       = (0x03, 0x00000070,  4)
        SD_FILT0                            = (0x03, 0x00000080,  7)
        SR_REF                              = (0x03, 0x00000700,  8)
        FILT_L_REF                          = (0x03, 0x00007000, 12)
        SD_FILT1                            = (0x03, 0x00008000, 15)
        SR_S                                = (0x03, 0x00070000, 16)
        FILT_L_S                            = (0x03, 0x00700000, 20)
        SD_FILT2                            = (0x03, 0x00800000, 23)
        SR_ENC_OUT                          = (0x03, 0x07000000, 24)
        FILT_L_ENC_OUT                      = (0x03, 0x70000000, 28)
        SD_FILT3                            = (0x03, 0x80000000, 31)

        # SPI_OUT_CONF
        SPI_OUTPUT_FORMAT                   = (0x04, 0x0000000f,  0)
        SSI_OUT_MTIME                       = (0x04, 0x00fffff0,  4)
        MIXED_DECAY                         = (0x04, 0x00000030,  4)
        AUTO_DOUBLE_CHOPSYNC                = (0x04, 0x00001000, 12)
        STDBY_ON_STALL_FOR_24X              = (0x04, 0x00000040,  6)
        STALL_FLAG_INSTEAD_OF_UV_EN         = (0x04, 0x00000080,  7)
        STALL_LOAD_LIMIT                    = (0x04, 0x00000700,  8)
        PWM_PHASE_SHFT_EN                   = (0x04, 0x00000800, 11)
        THREE_PHASE_STEPPER_EN              = (0x04, 0x00000010,  4)
        SCALE_VAL_TRANSFER_EN               = (0x04, 0x00000020,  5)
        DISABLE_POLLING                     = (0x04, 0x00000040,  6)
        POLL_BLOCK_MULT                     = (0x04, 0x00001f80,  7)
        SCALE_VALE_TRANSFER_EN              = (0x04, 0x00000020,  5)
        SCK_LOW_BEFORE_CSN                  = (0x04, 0x00000010,  4)
        NEW_OUT_BIT_AT_RISE                 = (0x04, 0x00000020,  5)
        DAC_CMD_LENGTH                      = (0x04, 0x0000f800,  7)
        COVER_DATA_LENGTH                   = (0x04, 0x000fe000, 13)
        SPI_OUT_LOW_TIME                    = (0x04, 0x00f00000, 20)
        SPI_OUT_HIGH_TIME                   = (0x04, 0x0f000000, 24)
        SPI_OUT_IDLE_TIME                   = (0x04, 0xf0000000, 28)

        # CURRENT_CONF
        HOLD_CURRENT_SCALE_EN               = (0x05, 0x00000001,  0)
        DRIVE_CURRENT_SCALE_EN              = (0x05, 0x00000002,  1)
        BOOST_CURRENT_ON_ACC_EN             = (0x05, 0x00000004,  2)
        BOOST_CURRENT_ON_DEC_EN             = (0x05, 0x00000008,  3)
        BOOST_CURRENT_AFTER_START_EN        = (0x05, 0x00000010,  4)
        SEC_DRIVE_CURRENT_SCALE_EN          = (0x05, 0x00000020,  5)
        FREEWHEELING_EN                     = (0x05, 0x00000040,  6)
        CLOSED_LOOP_SCALE_EN                = (0x05, 0x00000080,  7)
        PWM_SCALE_EN                        = (0x05, 0x00000100,  8)
        PWM_AMPL                            = (0x05, 0xffff0000, 16)

        # SCALE_VALUES
        BOOST_SCALE_VAL                     = (0x06, 0x000000ff,  0)
        DRV1_SCALE_VAL                      = (0x06, 0x0000ff00,  8)
        DRV2_SCALE_VAL                      = (0x06, 0x00ff0000, 16)
        HOLD_SCALE_VAL                      = (0x06, 0xff000000, 24)
        CL_IMIN                             = (0x06, 0x000000ff,  0)
        CL_IMAX                             = (0x06, 0x0000ff00,  8)
        CL_START_UP                         = (0x06, 0x00ff0000, 16)
        CL_START_DN                         = (0x06, 0xff000000, 24)

        # ENC_IN_CONF
        ENC_SEL_DECIMAL                     = (0x07, 0x00000001,  0)
        CLEAR_ON_N                          = (0x07, 0x00000002,  1)
        CLR_LATCH_CONT_ON_N                 = (0x07, 0x00000004,  2)
        CLR_LATCH_ONCE_ON_N                 = (0x07, 0x00000008,  3)
        POL_N                               = (0x07, 0x00000010,  4)
        N_CHAN_SENSITIVITY                  = (0x07, 0x00000060,  5)
        POL_A_FOR_N                         = (0x07, 0x00000080,  7)
        POL_B_FOR_N                         = (0x07, 0x00000100,  8)
        IGNORE_AB                           = (0x07, 0x00000200,  9)
        LATCH_ENC_ON_N                      = (0x07, 0x00000400, 10)
        LATCH_X_ON_N                        = (0x07, 0x00000800, 11)
        MULTI_TURN_IN_EN                    = (0x07, 0x00001000, 12)
        MULTI_TURN_IN_SIGNED                = (0x07, 0x00002000, 13)
        MULTI_TURN_OUT_EN                   = (0x07, 0x00004000, 14)
        USE_USTEPS_INSTEAD_OF_XRANGE        = (0x07, 0x00008000, 15)
        CALC_MULTI_TURN_BEHAV               = (0x07, 0x00010000, 16)
        SSI_MULTI_CYCLE_DATA                = (0x07, 0x00020000, 17)
        SSI_GRAY_CODE_EN                    = (0x07, 0x00040000, 18)
        LEFT_ALIGNED_DATA                   = (0x07, 0x00080000, 19)
        SPI_DATA_ON_CS                      = (0x07, 0x00100000, 20)
        SPI_LOW_BEFORE_CS                   = (0x07, 0x00200000, 21)
        REGULATION_MODUS                    = (0x07, 0x00c00000, 22)
        CL_CALIBRATION_EN                   = (0x07, 0x01000000, 24)
        CL_EMF_EN                           = (0x07, 0x02000000, 25)
        CL_CLR_XACT                         = (0x07, 0x04000000, 26)
        CL_VLIMIT_EN                        = (0x07, 0x08000000, 27)
        CL_VELOCITY_MODE_EN                 = (0x07, 0x10000000, 28)
        INVERT_ENC_DIR                      = (0x07, 0x20000000, 29)
        ENC_OUT_GRAY                        = (0x07, 0x40000000, 30)
        NO_ENC_VEL_PREPROC                  = (0x07, 0x80000000, 31)
        SERIAL_ENC_VARIATION_LIMIT          = (0x07, 0x80000000, 31)

        # ENC_IN_DATA
        SINGLE_TURN_RES                     = (0x08, 0x0000001f,  0)
        MULTI_TURN_RES                      = (0x08, 0x000003e0,  5)
        STATUS_BIT_CNT                      = (0x08, 0x00000c00, 10)
        SERIAL_ADDR_BITS                    = (0x08, 0x00ff0000, 16)
        SERIAL_DATA_BITS                    = (0x08, 0xff000000, 24)

        # ENC_OUT_DATA
        SINGLE_TURN_RES_OUT                 = (0x09, 0x0000001f,  0)
        MULTI_TURN_RES_OUT                  = (0x09, 0x000003e0,  5)

        # STEP_CONF
        MSTEP_PER_FS                        = (0x0A, 0x0000000f,  0)
        FS_PER_REV                          = (0x0A, 0x0000fff0,  4)
        SG                                  = (0x0A, 0x00010000, 16)
        OT                                  = (0x0A, 0x00020000, 17)
        OTPW                                = (0x0A, 0x00040000, 18)
        S2GA                                = (0x0A, 0x00080000, 19)
        S2GB                                = (0x0A, 0x00100000, 20)
        OLA                                 = (0x0A, 0x00200000, 21)
        OLB                                 = (0x0A, 0x00400000, 22)
        STST                                = (0x0A, 0x00800000, 23)
        UV_SF                               = (0x0A, 0x00010000, 16)
        OCA                                 = (0x0A, 0x00080000, 19)
        OCB                                 = (0x0A, 0x00100000, 20)
        OCHS                                = (0x0A, 0x00800000, 23)

        # SPI_STATUS_SELECTION
        TARGET_REACHED                      = (0x0B, 0x00000001,  0)
        POS_COMP_REACHED                    = (0x0B, 0x00000002,  1)
        VEL_REACHED                         = (0x0B, 0x00000004,  2)
        VEL_STATE_00                        = (0x0B, 0x00000008,  3)
        VEL_STATE_01                        = (0x0B, 0x00000010,  4)
        VEL_STATE_10                        = (0x0B, 0x00000020,  5)
        RAMP_STATE_00                       = (0x0B, 0x00000040,  6)
        RAMP_STATE_01                       = (0x0B, 0x00000080,  7)
        RAMP_STATE_10                       = (0x0B, 0x00000100,  8)
        MAX_PHASE_TRAP                      = (0x0B, 0x00000200,  9)
        FROZEN                              = (0x0B, 0x00000400, 10)
        STOPL_EVENT                         = (0x0B, 0x00000800, 11)
        STOPR_EVENT                         = (0x0B, 0x00001000, 12)
        VSTOPL_ACTIVE                       = (0x0B, 0x00002000, 13)
        VSTOPR_ACTIVE                       = (0x0B, 0x00004000, 14)
        HOME_ERROR                          = (0x0B, 0x00008000, 15)
        XLATCH_DONE                         = (0x0B, 0x00010000, 16)
        FS_ACTIVE                           = (0x0B, 0x00020000, 17)
        ENC_FAIL                            = (0x0B, 0x00040000, 18)
        N_ACTIVE                            = (0x0B, 0x00080000, 19)
        ENC_DONE                            = (0x0B, 0x00100000, 20)
        SER_ENC_DATA_FAIL                   = (0x0B, 0x00200000, 21)
        SER_DATA_DONE                       = (0x0B, 0x00800000, 23)
        SERIAL_ENC_FLAGS                    = (0x0B, 0x01000000, 24)
        COVER_DONE                          = (0x0B, 0x02000000, 25)
        ENC_VEL0                            = (0x0B, 0x04000000, 26)
        CL_MAX                              = (0x0B, 0x08000000, 27)
        CL_FIT                              = (0x0B, 0x10000000, 28)
        STOP_ON_STALL_STATE                 = (0x0B, 0x20000000, 29)
        MOTOR_EV                            = (0x0B, 0x40000000, 30)
        RST_EV                              = (0x0B, 0x80000000, 31)

        # STATUS
        TARGET_REACHED_F                    = (0x0F, 0x00000001,  0)
        POS_COMP_REACHED_F                  = (0x0F, 0x00000002,  1)
        VEL_REACHED_F                       = (0x0F, 0x00000004,  2)
        VEL_STATE_F                         = (0x0F, 0x00000018,  3)
        RAMP_STATE_F                        = (0x0F, 0x00000060,  5)
        STOPL_ACTIVE_F                      = (0x0F, 0x00000080,  7)
        STOPR_ACTIVE_F                      = (0x0F, 0x00000100,  8)
        VSTOPL_ACTIVE_F                     = (0x0F, 0x00000200,  9)
        VSTOPR_ACTIVE_F                     = (0x0F, 0x00000400, 10)
        ACTIVE_STALL_F                      = (0x0F, 0x00000800, 11)
        HOME_ERROR_F                        = (0x0F, 0x00001000, 12)
        FS_ACTIVE_F                         = (0x0F, 0x00002000, 13)
        ENC_FAIL_F                          = (0x0F, 0x00004000, 14)
        N_ACTIVE_F                          = (0x0F, 0x00008000, 15)
        ENC_LATCH_F                         = (0x0F, 0x00010000, 16)
        MULTI_CYCLE_FAIL_F___SER_ENC_VAR_F  = (0x0F, 0x00020000, 17)
        SERIAL_ENC_FLAG_0                   = (0x0F, 0x00100000, 20)
        SERIAL_ENC_FLAG_1                   = (0x0F, 0x00200000, 21)
        SERIAL_ENC_FLAG_2                   = (0x0F, 0x00400000, 22)
        SERIAL_ENC_FLAG_3                   = (0x0F, 0x00800000, 23)

        # STP_LENGTH_ADD / DIR_SETUP_TIME
        STP_LENGTH_ADD                      = (0x10, 0x0000FFFF,  0)
        DIR_SETUP_TIME                      = (0x10, 0xFFFF0000, 16)

        # START_OUT_ADD
        START_OUT_ADD                       = (0x11, 0xFFFFFFFF,  0)

        # GEAR_RATIO
        GEAR_RATIO                          = (0x12, 0xFFFFFFFF,  0)

        # START_DELAY
        START_DELAY                         = (0x13, 0xFFFFFFFF,  0)

        # CLK_GATING_DELAY
        CLK_GATING_DELAY                    = (0x14, 0xFFFFFFFF,  0)

        # STDBY_DELAY
        STDBY_DELAY                         = (0x15, 0xFFFFFFFF,  0)

        # FREEWHEEL_DELAY
        FREEWHEEL_DELAY                     = (0x16, 0xFFFFFFFF,  0)

        # VDRV_SCALE_LIMIT / PWM_VMAX
        VDRV_SCALE_LIMIT                    = (0x17, 0x00FFFFFF,  0)
        PWM_VMAX                            = (0x17, 0x00FFFFFF,  0)

        # UP_SCALE_DELAY / CL_UPSCALE_DELAY
        UP_SCALE_DELAY                      = (0x18, 0x00FFFFFF,  0)
        CL_UPSCALE_DELAY                    = (0x18, 0x00FFFFFF,  0)

        # HOLD_SCALE_DELAY / CL_DNSCALE_DELAY
        HOLD_SCALE_DELAY                    = (0x19, 0x00FFFFFF,  0)
        CL_DNSCALE_DELAY                    = (0x19, 0x00FFFFFF,  0)

        # DRV_SCALE_DELAY
        DRV_SCALE_DELAY                     = (0x1A, 0x00FFFFFF,  0)

        # BOOST_TIME
        BOOST_TIME                          = (0x1B, 0x00FFFFFF,  0)

        # CL ANGLES
        CL_BETA                             = (0x1C, 0x000001FF,  0)
        CL_GAMMA                            = (0x1C, 0x00FF0000, 16)

        # SPI_SWITCH_VEL / DAC ADDR
        SPI_SWITCH_VEL                      = (0x1D, 0x00FFFFFF,  0)
        DAC_ADDR_A                          = (0x1D, 0x0000FFFF,  0)
        DAC_ADDR_B                          = (0x1D, 0xFFFF0000, 16)

        # HOME_SAFETY_MARGIN
        HOME_SAFETY_MARGIN                  = (0x1E, 0x0000FFFF,  0)

        # PWM_FREQ / CHOPSYNC_DIV
        PWM_FREQ                            = (0x1F, 0x0000FFFF,  0)
        CHOPSYNC_DIV                        = (0x1F, 0x00000FFF,  0)

        # RAMPMODE
        OPERATION_MODE                      = (0x20, 0x00000004,  2)
        RAMP_PROFILE                        = (0x20, 0x00000003,  0)

        # XACTUAL
        XACTUAL                             = (0x21, 0xFFFFFFFF,  0)

        # VACTUAL
        VACTUAL                             = (0x22, 0xFFFFFFFF,  0)

        # AACTUAL
        AACTUAL                             = (0x23, 0xFFFFFFFF,  0)

        # VMAX
        VMAX                                = (0x24, 0xFFFFFFFF,  0)

        # VSTART
        VSTART                              = (0x25, 0x7FFFFFFF,  0)

        # VSTOP
        VSTOP                               = (0x26, 0x7FFFFFFF,  0)

        # VBREAK
        VBREAK                              = (0x27, 0x7FFFFFFF,  0)

        # AMAX
        AMAX                                = (0x28, 0x00FFFFFF,  0)

        # DMAX
        DMAX                                = (0x29, 0x00FFFFFF,  0)

        # ASTART
        ASTART                              = (0x2A, 0x00FFFFFF,  0)
        SIGN_AACT                           = (0x2A, 0x80000000, 31)

        # DFINAL
        DFINAL                              = (0x2B, 0x00FFFFFF,  0)

        # DSTOP
        DSTOP                               = (0x2C, 0x00FFFFFF,  0)

        # BOW1
        BOW1                                = (0x2D, 0x00FFFFFF,  0)

        # BOW2
        BOW2                                = (0x2E, 0x00FFFFFF,  0)

        # BOW3
        BOW3                                = (0x2F, 0x00FFFFFF,  0)

        # BOW4
        BOW4                                = (0x30, 0x00FFFFFF,  0)

        # CLK_FREQ
        CLK_FREQ                            = (0x31, 0x01FFFFFF,  0)

        # POS_COMP
        POS_COMP                            = (0x32, 0xFFFFFFFF,  0)

        # VIRT_STOP_LEFT
        VIRT_STOP_LEFT                      = (0x33, 0xFFFFFFFF,  0)

        # VIRT_STOP_RIGHT
        VIRT_STOP_RIGHT                     = (0x34, 0xFFFFFFFF,  0)

        # X_HOME
        X_HOME                              = (0x35, 0xFFFFFFFF,  0)

        # X_LATCH / REV_CNT / X_RANGE
        X_LATCH                             = (0x36, 0xFFFFFFFF,  0)
        X_RANGE                             = (0x36, 0xFFFFFFFF,  0)

        # XTARGET
        XTARGET                             = (0x37, 0xFFFFFFFF,  0)

        # X_PIPE0
        X_PIPE0                             = (0x38, 0xFFFFFFFF,  0)

        # X_PIPE1
        X_PIPE1                             = (0x39, 0xFFFFFFFF,  0)

        # X_PIPE2
        X_PIPE2                             = (0x3A, 0xFFFFFFFF,  0)

        # X_PIPE3
        X_PIPE3                             = (0x3B, 0xFFFFFFFF,  0)

        # X_PIPE4
        X_PIPE4                             = (0x3C, 0xFFFFFFFF,  0)

        # X_PIPE5
        X_PIPE5                             = (0x3D, 0xFFFFFFFF,  0)

        # X_PIPE6
        X_PIPE6                             = (0x3E, 0xFFFFFFFF,  0)

        # X_PIPE7
        X_PIPE7                             = (0x3F, 0xFFFFFFFF,  0)

        # SH_REG0
        SH_REG0_VMAX                        = (0x40, 0xFFFFFFFF,  0)

        # SH_REG1
        SH_REG1_AMAX                        = (0x41, 0x00FFFFFF,  0)

        # SH_REG2
        SH_REG2_DMAX                        = (0x42, 0x00FFFFFF,  0)

        # SH_REG3
        SH_REG3_ASTART                      = (0x43, 0x00FFFFFF,  0)
        SH_REG3_BOW1                        = (0x43, 0x00FFFFFF,  0)

        # SH_REG4
        SH_REG4_DFINAL                      = (0x44, 0x00FFFFFF,  0)
        SH_REG4_BOW2                        = (0x44, 0x00FFFFFF,  0)

        # SH_REG5
        SH_REG5_VBREAK                      = (0x45, 0x7FFFFFFF,  0)
        SH_REG5_BOW3                        = (0x45, 0x00FFFFFF,  0)

        # SH_REG6
        SH_REG6_VSTART                      = (0x46, 0x7FFFFFFF,  0)
        SH_REG6_BOW4                        = (0x46, 0x00FFFFFF,  0)
        SH_REG6_VSTOP                       = (0x46, 0x7FFFFFFF,  0)

        # SH_REG7
        SH_REG7_VSTOP                       = (0x47, 0xFFFFFFFF,  0)
        SH_REG7_VMAX                        = (0x47, 0xFFFFFFFF,  0)

        # SH_REG8
        SH_REG8_BOW1                        = (0x48, 0x00FFFFFF,  0)
        SH_REG8_AMAX                        = (0x48, 0x00FFFFFF,  0)

        # SH_REG9
        SH_REG9_BOW2                        = (0x49, 0x00FFFFFF,  0)
        SH_REG9_DMAX                        = (0x49, 0x00FFFFFF,  0)

        # SH_REG10
        SH_REG10_BOW3                       = (0x4A, 0x00FFFFFF,  0)
        SH_REG10_BOW1                       = (0x4A, 0x00FFFFFF,  0)
        SH_REG10_ASTART                     = (0x4A, 0x00FFFFFF,  0)

        # SH_REG11
        SH_REG11_BOW4                       = (0x4B, 0x00FFFFFF,  0)
        SH_REG11_BOW2                       = (0x4B, 0x00FFFFFF,  0)
        SH_REG11_DFINAL                     = (0x4B, 0x00FFFFFF,  0)

        # SH_REG12
        SH_REG12_BOW3                       = (0x4C, 0x00FFFFFF,  0)
        SH_REG12_VBREAK                     = (0x4C, 0x7FFFFFFF,  0)

        # SH_REG13
        SH_REG13_BOW4                       = (0x4D, 0x00FFFFFF,  0)
        SH_REG13_VSTART                     = (0x4D, 0x7FFFFFFF,  0)
        SH_REG13_VSTOP                      = (0x4D, 0x7FFFFFFF,  0)

        # Freeze Registers
        DFREEZE                             = (0x4E, 0x00FFFFFF,  0)
        IFREEZE                             = (0x4E, 0xFF000000, 24)

        # ENC_POS
        ENC_POS                             = (0x50, 0xFFFFFFFF,  0)

        # ENC_LATCH / ENC_RESET_VAL
        ENC_LATCH                           = (0x51, 0xFFFFFFFF,  0)
        ENC_RESET_VAL                       = (0x51, 0xFFFFFFFF,  0)

        # ENC_POS_DEV / CL_TR_TOLERANCE
        ENC_POS_DEV                         = (0x52, 0xFFFFFFFF,  0)
        CL_TR_TOLERANCE                     = (0x52, 0x7FFFFFFF,  0)

        # ENC_POS_DEV_TOL
        ENC_POS_DEV_TOL                     = (0x53, 0x7FFFFFFF,  0)

        # ENC_IN_RES / ENC_CONST
        ENC_CONST                           = (0x54, 0x7FFFFFFF,  0)
        ENC_IN_RES                          = (0x54, 0x7FFFFFFF,  0)
        MANUAL_ENC_CONST                    = (0x54, 0x80000000, 31)

        # ENC_OUT_RES
        ENC_OUT_RES                         = (0x55, 0x7FFFFFFF,  0)

        # SER_CLK_IN_HIGH/LOW
        SER_CLK_IN_HIGH                     = (0x56, 0x0000FFFF,  0)
        SER_CLK_IN_LOW                      = (0x56, 0xFFFF0000, 16)

        # SSI_IN_CLK_DELAY / SSI_IN_WTIME
        SSI_IN_CLK_DELAY                    = (0x57, 0x0000FFFF,  0)
        SSI_IN_WTIME                        = (0x57, 0xFFFF0000, 16)

        # SER_PTIME
        SER_PTIME                           = (0x58, 0x000FFFFF,  0)

        # CL_OFFSET
        CL_OFFSET                           = (0x59, 0xFFFFFFFF,  0)

        # PID_VEL / PID_P / CL_VMAX_CALC_P
        PID_VEL                             = (0x5A, 0xFFFFFFFF,  0)
        CL_VMAX_CALC_P                      = (0x5A, 0x00FFFFFF,  0)
        PID_P                               = (0x5A, 0x00FFFFFF,  0)

        # PID_ISUM_RD / PID_I / CL_VMAX_CALC_I
        PID_ISUM_RD                         = (0x5B, 0xFFFFFFFF,  0)
        CL_VMAX_CALC_I                      = (0x5B, 0x00FFFFFF,  0)
        PID_I                               = (0x5B, 0x00FFFFFF,  0)

        # PID_D / CL_DELTA_P
        CL_DELTA_P                          = (0x5C, 0x00FFFFFF,  0)
        PID_D                               = (0x5C, 0x00FFFFFF,  0)

        # PID_E / PID_I_CLIP / PID_D_CLKDIV
        PID_E                               = (0x5D, 0xFFFFFFFF,  0)
        PID_I_CLIP                          = (0x5D, 0x00007FFF,  0)
        PID_D_CLKDIV                        = (0x5D, 0x00FF0000, 16)

        # PID_DV_CLIP
        PID_DV_CLIP                         = (0x5E, 0x7FFFFFFF,  0)

        # PID_TOLERANCE / CL_TOLERANCE
        CL_TOLERANCE                        = (0x5F, 0x000000FF,  0)
        PID_TOLERANCE                       = (0x5F, 0x000FFFFF,  0)

        # FS_VEL / DC_VEL / CL_VMIN_EMF
        FS_VEL                              = (0x60, 0x00FFFFFF,  0)
        DC_VEL                              = (0x60, 0x00FFFFFF,  0)
        CL_VMIN_EMF                         = (0x60, 0x00FFFFFF,  0)

        # DC_TIME / DC_SG / DC_BLKTIME / CL_VADD_EMF
        DC_TIME                             = (0x61, 0x000000FF,  0)
        DC_SG                               = (0x61, 0x0000FF00,  8)
        DC_BLKTIME                          = (0x61, 0xFFFF0000, 16)
        CL_VADD_EMF                         = (0x61, 0x00FFFFFF,  0)

        # DC_LSPTM / ENC_VEL_ZERO
        DC_LSPTM                            = (0x62, 0xFFFFFFFF,  0)
        ENC_VEL_ZERO                        = (0x62, 0x00FFFFFF,  0)

        # ENC_VMEAN_... / SER_ENC_VARIATION / CL_CYCLE
        ENC_VMEAN_WAIT                      = (0x63, 0x000000FF,  0)
        ENC_VMEAN_FILTER                    = (0x63, 0x00000F00,  8)
        ENC_VMEAN_INT                       = (0x63, 0xFFFF0000, 16)
        SER_ENC_VARIATION                   = (0x63, 0x000000FF,  0)
        CL_CYCLE                            = (0x63, 0xFFFF0000, 16)

        # V_ENC
        V_ENC                               = (0x65, 0xFFFFFFFF,  0)

        # V_ENC_MEAN
        V_ENC_MEAN                          = (0x66, 0xFFFFFFFF,  0)

        # VSTALL_LIMIT
        VSTALL_LIMIT                        = (0x67, 0x00FFFFFF,  0)

        # ADDR_TO_ENC
        ADDR_TO_ENC                         = (0x68, 0xFFFFFFFF,  0)

        # DATA_TO_ENC
        DATA_TO_ENC                         = (0x69, 0xFFFFFFFF,  0)

        # ADDR_FROM_ENC
        ADDR_FROM_ENC                       = (0x6A, 0xFFFFFFFF,  0)

        # DATA_FROM_ENC
        DATA_FROM_ENC                       = (0x6B, 0xFFFFFFFF,  0)

        # COVER_LOW
        COVER_LOW                           = (0x6C, 0xFFFFFFFF,  0)

        # COVER_HIGH / POLLING_REG
        COVER_HIGH                          = (0x6D, 0xFFFFFFFF,  0)

        # COVER_DRV_LOW
        COVER_DRV_LOW                       = (0x6E, 0xFFFFFFFF,  0)

        # COVER_DRV_HIGH
        COVER_DRV_HIGH                      = (0x6F, 0xFFFFFFFF,  0)

        # MSLUT[0]
        MSLUT__                             = (0x70, 0xFFFFFFFF,  0)

        # MSLUTSEL
        MSLUTSEL                            = (0x78, 0xFFFFFFFF,  0)

        # MSCNT
        MSCNT                               = (0x79, 0x000003FF,  0)
        MSOFFSET                            = (0x79, 0x000003FF,  0)

        # CURRENTA/B
        CURRENTA                            = (0x7A, 0x000001FF,  0)
        CURRENTB                            = (0x7A, 0x01FF0000, 16)

        # CURRENTA/B_SPI
        CURRENTA_SPI                        = (0x7B, 0x000001FF,  0)
        CURRENTB_SPI                        = (0x7B, 0x01FF0000, 16)
        TZEROWAIT                           = (0x7B, 0xFFFFFFFF,  0)

        # SCALE_PARAM / CIRCULAR_DEC
        SCALE_PARAM                         = (0x7C, 0x000001FF,  0)
        CIRCULAR_DEC                        = (0x7C, 0xFFFFFFFF,  0)

        # ENC_COMP_...
        ENC_COMP_XOFFSET                    = (0x7D, 0x0000FFFF,  0)
        ENC_COMP_YOFFSET                    = (0x7D, 0x00FF0000, 16)

        # START_SIN... / DAC_OFFSET
        START_SIN                           = (0x7E, 0x000000FF,  0)
        START_SIN90_120                     = (0x7E, 0x00FF0000, 16)
        DAC_OFFSET                          = (0x7E, 0xFF000000, 24)

        # VERSION_NO
        VERSION_NO                          = (0x7F, 0x0000000F,  0)
