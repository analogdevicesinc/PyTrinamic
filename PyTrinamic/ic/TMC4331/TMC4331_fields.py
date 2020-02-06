'''
Created on 06.02.2020

@author: JM
'''

class TMC4331_fields(object):
    """
    Define all register bitfields of the TMC4331.

    Each field is defined as a tuple consisting of ( Address, Mask, Shift ).

    The name of the register is written as a comment behind each tuple. This is
    intended for IDE users viewing the definition of a field by hovering over
    it. This allows the user to see the corresponding register name of a field
    without opening this file and searching for the definition.
    """

    # GENERAL_CONF
    USE_ASTART_AND_VSTART             = ( 0x00, 0x00000001,  0 ) # GENERAL_CONF
    DIRECT_ACC_VAL_EN                 = ( 0x00, 0x00000002,  1 ) # GENERAL_CONF
    DIRECT_BOW_VAL_EN                 = ( 0x00, 0x00000004,  2 ) # GENERAL_CONF
    STEP_INACTIVE_POL                 = ( 0x00, 0x00000008,  3 ) # GENERAL_CONF
    TOGGLE_STEP                       = ( 0x00, 0x00000010,  4 ) # GENERAL_CONF
    POL_DIR_OUT                       = ( 0x00, 0x00000020,  5 ) # GENERAL_CONF
    SDIN_MODE                         = ( 0x00, 0x000000c0,  6 ) # GENERAL_CONF
    POL_DIR_IN                        = ( 0x00, 0x00000100,  8 ) # GENERAL_CONF
    SD_INDIRECT_CONTROL               = ( 0x00, 0x00000200,  9 ) # GENERAL_CONF
    STDBY_CLK_PIN_ASSIGNMENT          = ( 0x00, 0x00006000, 13 ) # GENERAL_CONF
    INTR_POL                          = ( 0x00, 0x00008000, 15 ) # GENERAL_CONF
    INVERT_POL_TARGET_REACHED         = ( 0x00, 0x00010000, 16 ) # GENERAL_CONF
    FS_EN                             = ( 0x00, 0x00080000, 19 ) # GENERAL_CONF
    FS_SDOUT                          = ( 0x00, 0x00100000, 20 ) # GENERAL_CONF
    DCSTEP_MODE                       = ( 0x00, 0x00600000, 21 ) # GENERAL_CONF
    PWM_OUT_EN                        = ( 0x00, 0x00800000, 23 ) # GENERAL_CONF
    AUTOMATIC_DIRECT_SDIN_SWITCH_OFF  = ( 0x00, 0x04000000, 26 ) # GENERAL_CONF
    CIRCULAR_CNT_AS_XLATCH            = ( 0x00, 0x08000000, 27 ) # GENERAL_CONF
    REVERSE_MOTOR_DIR                 = ( 0x00, 0x10000000, 28 ) # GENERAL_CONF
    INTR_TR_PU_PD_EN                  = ( 0x00, 0x20000000, 29 ) # GENERAL_CONF
    INTR_AS_WIRED_AND                 = ( 0x00, 0x40000000, 30 ) # GENERAL_CONF
    TR_AS_WIRED_AND                   = ( 0x00, 0x80000000, 31 ) # GENERAL_CONF

    # REFERENCE_CONF
    STOP_LEFT_EN                      = ( 0x01, 0x00000001,  0 ) # REFERENCE_CONF
    STOP_RIGHT_EN                     = ( 0x01, 0x00000002,  1 ) # REFERENCE_CONF
    POL_STOP_LEFT                     = ( 0x01, 0x00000004,  2 ) # REFERENCE_CONF
    POL_STOP_RIGHT                    = ( 0x01, 0x00000008,  3 ) # REFERENCE_CONF
    INVERT_STOP_DIRECTION             = ( 0x01, 0x00000010,  4 ) # REFERENCE_CONF
    SOFT_STOP_EN                      = ( 0x01, 0x00000020,  5 ) # REFERENCE_CONF
    VIRTUAL_LEFT_LIMIT_EN             = ( 0x01, 0x00000040,  6 ) # REFERENCE_CONF
    VIRTUAL_RIGHT_LIMIT_EN            = ( 0x01, 0x00000080,  7 ) # REFERENCE_CONF
    VIRT_STOP_MODE                    = ( 0x01, 0x00000300,  8 ) # REFERENCE_CONF
    LATCH_X_ON_INACTIVE_L             = ( 0x01, 0x00000400, 10 ) # REFERENCE_CONF
    LATCH_X_ON_ACTIVE_L               = ( 0x01, 0x00000800, 11 ) # REFERENCE_CONF
    LATCH_X_ON_INACTIVE_R             = ( 0x01, 0x00001000, 12 ) # REFERENCE_CONF
    LATCH_X_ON_ACTIVE_R               = ( 0x01, 0x00002000, 13 ) # REFERENCE_CONF
    STOP_LEFT_IS_HOME                 = ( 0x01, 0x00004000, 14 ) # REFERENCE_CONF
    HOME_EVENT                        = ( 0x01, 0x000f0000, 16 ) # REFERENCE_CONF
    START_HOME_TRACKING               = ( 0x01, 0x00100000, 20 ) # REFERENCE_CONF
    CLR_POS_AT_TARGET                 = ( 0x01, 0x00200000, 21 ) # REFERENCE_CONF
    CIRCULAR_MOVEMENT_EN              = ( 0x01, 0x00400000, 22 ) # REFERENCE_CONF
    POS_COMP_OUTPUT                   = ( 0x01, 0x01800000, 23 ) # REFERENCE_CONF
    STOP_ON_STALL                     = ( 0x01, 0x04000000, 26 ) # REFERENCE_CONF
    DRV_AFTER_STALL                   = ( 0x01, 0x08000000, 27 ) # REFERENCE_CONF
    MODIFIED_POS_COPARE               = ( 0x01, 0x30000000, 28 ) # REFERENCE_CONF
    AUTOMATIC_COVER                   = ( 0x01, 0x40000000, 30 ) # REFERENCE_CONF
    CIRCULAR_ENC_EN                   = ( 0x01, 0x80000000, 31 ) # REFERENCE_CONF

    # START_CONF
    START_EN_0_                       = ( 0x02, 0x00000001,  0 ) # START_CONF
    START_EN_1_                       = ( 0x02, 0x00000002,  1 ) # START_CONF
    START_EN_2_                       = ( 0x02, 0x00000004,  2 ) # START_CONF
    START_EN_3_                       = ( 0x02, 0x00000008,  3 ) # START_CONF
    START_EN_4_                       = ( 0x02, 0x00000010,  4 ) # START_CONF
    TRIGGER_EVENTS_0_                 = ( 0x02, 0x00000020,  5 ) # START_CONF
    TRIGGER_EVENTS_1_                 = ( 0x02, 0x00000040,  6 ) # START_CONF
    TRIGGER_EVENTS_2_                 = ( 0x02, 0x00000080,  7 ) # START_CONF
    TRIGGER_EVENTS_3_                 = ( 0x02, 0x00000100,  8 ) # START_CONF
    POL_START_SIGNAL                  = ( 0x02, 0x00000200,  9 ) # START_CONF
    IMMEDIATE_START_IN                = ( 0x02, 0x00000400, 10 ) # START_CONF
    BUSY_STATE_EN                     = ( 0x02, 0x00000800, 11 ) # START_CONF
    PIPELINE_EN_0_                    = ( 0x02, 0x00001000, 12 ) # START_CONF
    PIPELINE_EN_1_                    = ( 0x02, 0x00002000, 13 ) # START_CONF
    PIPELINE_EN_2_                    = ( 0x02, 0x00004000, 14 ) # START_CONF
    PIPELINE_EN_3_                    = ( 0x02, 0x00008000, 15 ) # START_CONF
    SHADOW_OPTION                     = ( 0x02, 0x00030000, 16 ) # START_CONF
    CYCLIC_SHADOW_REGS                = ( 0x02, 0x00040000, 18 ) # START_CONF
    SHADOW_MISS_CNT                   = ( 0x02, 0x00f00000, 20 ) # START_CONF
    XPIPE_REWRITE_REG_0_              = ( 0x02, 0x01000000, 24 ) # START_CONF
    XPIPE_REWRITE_REG_1_              = ( 0x02, 0x02000000, 25 ) # START_CONF
    XPIPE_REWRITE_REG_2_              = ( 0x02, 0x04000000, 26 ) # START_CONF
    XPIPE_REWRITE_REG_3_              = ( 0x02, 0x08000000, 27 ) # START_CONF
    XPIPE_REWRITE_REG_4_              = ( 0x02, 0x10000000, 28 ) # START_CONF
    XPIPE_REWRITE_REG_5_              = ( 0x02, 0x20000000, 29 ) # START_CONF
    XPIPE_REWRITE_REG_6_              = ( 0x02, 0x40000000, 30 ) # START_CONF
    XPIPE_REWRITE_REG_7_              = ( 0x02, 0x80000000, 31 ) # START_CONF

    # INPUT_FILT_CONF
    SR_SD_IN                          = ( 0x03, 0x00000007,  0 ) # INPUT_FILT_CONF
    FILT_L_SD_IN                      = ( 0x03, 0x00000070,  4 ) # INPUT_FILT_CONF
    SR_REF                            = ( 0x03, 0x00000700,  8 ) # INPUT_FILT_CONF
    FILT_L_REF                        = ( 0x03, 0x00007000, 12 ) # INPUT_FILT_CONF
    SR_S                              = ( 0x03, 0x00070000, 16 ) # INPUT_FILT_CONF
    FILT_L_S                          = ( 0x03, 0x00700000, 20 ) # INPUT_FILT_CONF

    # SPI_OUT_CONF
    SPI_OUTPUT_FORMAT                 = ( 0x04, 0x0000000f,  0 ) # SPI_OUT_CONF
    MIXED_DECAY                       = ( 0x04, 0x00000030,  4 ) # SPI_OUT_CONF
    AUTO_DOUBLE_CHOPSYNC              = ( 0x04, 0x00001000, 12 ) # SPI_OUT_CONF
    STDBY_ON_STALL_FOR_24X            = ( 0x04, 0x00000040,  6 ) # SPI_OUT_CONF
    STALL_FLAG_INSTEAD_OF_UV_EN       = ( 0x04, 0x00000080,  7 ) # SPI_OUT_CONF
    STALL_LOAD_LIMIT                  = ( 0x04, 0x00000700,  8 ) # SPI_OUT_CONF
    PWM_PHASE_SHFT_EN                 = ( 0x04, 0x00000800, 11 ) # SPI_OUT_CONF
    THREE_PHASE_STEPPER_EN            = ( 0x04, 0x00000010,  4 ) # SPI_OUT_CONF
    AUTOREPEAT_COVER_EN               = ( 0x04, 0x00000080,  7 ) # SPI_OUT_CONF
    COVER_DONE_ONLY_FOR_COVER         = ( 0x04, 0x00001000, 12 ) # SPI_OUT_CONF
    SCALE_VALE_TRANSFER_EN            = ( 0x04, 0x00000020,  5 ) # SPI_OUT_CONF
    DISABLE_POLLING                   = ( 0x04, 0x00000040,  6 ) # SPI_OUT_CONF
    POLL_BLOCK_EXP                    = ( 0x04, 0x00000f00,  8 ) # SPI_OUT_CONF
    SCK_LOW_BEFORE_CSN                = ( 0x04, 0x00000010,  4 ) # SPI_OUT_CONF
    NEW_OUT_BIT_AT_RISE               = ( 0x04, 0x00000020,  5 ) # SPI_OUT_CONF
    DAC_CMD_LENGTH                    = ( 0x04, 0x00000f80,  7 ) # SPI_OUT_CONF
    COVER_DATA_LENGTH                 = ( 0x04, 0x000fe000, 13 ) # SPI_OUT_CONF
    SPI_OUT_LOW_TIME                  = ( 0x04, 0x00f00000, 20 ) # SPI_OUT_CONF
    SPI_OUT_HIGH_TIME                 = ( 0x04, 0x0f000000, 24 ) # SPI_OUT_CONF

    # CURRENT_CONF
    HOLD_CURRENT_SCALE_EN             = ( 0x05, 0x00000001,  0 ) # CURRENT_CONF
    DRIVE_CURRENT_SCALE_EN            = ( 0x05, 0x00000002,  1 ) # CURRENT_CONF
    BOOST_CURRENT_ON_ACC_EN           = ( 0x05, 0x00000004,  2 ) # CURRENT_CONF
    BOOST_CURRENT_ON_DEC_EN           = ( 0x05, 0x00000008,  3 ) # CURRENT_CONF
    BOOST_CURRENT_AFTER_START_EN      = ( 0x05, 0x00000010,  4 ) # CURRENT_CONF
    SEC_DRIVE_CURRENT_SCALE_EN        = ( 0x05, 0x00000020,  5 ) # CURRENT_CONF
    FREEWHEELING_EN                   = ( 0x05, 0x00000040,  6 ) # CURRENT_CONF
    PWM_SCALE_EN                      = ( 0x05, 0x00000100,  8 ) # CURRENT_CONF
    PWM_AMPL                          = ( 0x05, 0xffff0000, 16 ) # CURRENT_CONF

    # SCALE_VALUES
    BOOST_SCALE_VAL                   = ( 0x06, 0x000000ff,  0 ) # SCALE_VALUES
    DRV1_SCALE_VAL                    = ( 0x06, 0x0000ff00,  8 ) # SCALE_VALUES
    DRV2_SCALE_VAL                    = ( 0x06, 0x00ff0000, 16 ) # SCALE_VALUES
    HOLD_SCALE_VAL                    = ( 0x06, 0xff000000, 24 ) # SCALE_VALUES

    # STEP_CONF
    MSTEP_PER_FS                      = ( 0x0A, 0x0000000f,  0 ) # STEP_CONF
    FS_PER_REV                        = ( 0x0A, 0x0000fff0,  4 ) # STEP_CONF
    SG                                = ( 0x0A, 0x00010000, 16 ) # STEP_CONF
    OT                                = ( 0x0A, 0x00020000, 17 ) # STEP_CONF
    OTPW                              = ( 0x0A, 0x00040000, 18 ) # STEP_CONF
    S2GA                              = ( 0x0A, 0x00080000, 19 ) # STEP_CONF
    S2GB                              = ( 0x0A, 0x00100000, 20 ) # STEP_CONF
    OLA                               = ( 0x0A, 0x00200000, 21 ) # STEP_CONF
    OLB                               = ( 0x0A, 0x00400000, 22 ) # STEP_CONF
    STST                              = ( 0x0A, 0x00800000, 23 ) # STEP_CONF
    UV_SF                             = ( 0x0A, 0x00010000, 16 ) # STEP_CONF
    OCA                               = ( 0x0A, 0x00080000, 19 ) # STEP_CONF
    OCB                               = ( 0x0A, 0x00100000, 20 ) # STEP_CONF
    OCHS                              = ( 0x0A, 0x00800000, 23 ) # STEP_CONF

    # SPI_STATUS_SELECTION
    TARGET_REACHED                    = ( 0x0B, 0x00000001,  0 ) # SPI_STATUS_SELECTION
    POS_COMP_REACHED                  = ( 0x0B, 0x00000002,  1 ) # SPI_STATUS_SELECTION
    VEL_REACHED                       = ( 0x0B, 0x00000004,  2 ) # SPI_STATUS_SELECTION
    VEL_STATE_00                      = ( 0x0B, 0x00000008,  3 ) # SPI_STATUS_SELECTION
    VEL_STATE_01                      = ( 0x0B, 0x00000010,  4 ) # SPI_STATUS_SELECTION
    VEL_STATE_10                      = ( 0x0B, 0x00000020,  5 ) # SPI_STATUS_SELECTION
    RAMP_STATE_00                     = ( 0x0B, 0x00000040,  6 ) # SPI_STATUS_SELECTION
    RAMP_STATE_01                     = ( 0x0B, 0x00000080,  7 ) # SPI_STATUS_SELECTION
    RAMP_STATE_10                     = ( 0x0B, 0x00000100,  8 ) # SPI_STATUS_SELECTION
    MAX_PHASE_TRAP                    = ( 0x0B, 0x00000200,  9 ) # SPI_STATUS_SELECTION
    STOPL_EVENT                       = ( 0x0B, 0x00000800, 11 ) # SPI_STATUS_SELECTION
    STOPR_EVENT                       = ( 0x0B, 0x00001000, 12 ) # SPI_STATUS_SELECTION
    VSTOPL_ACTIVE                     = ( 0x0B, 0x00002000, 13 ) # SPI_STATUS_SELECTION
    HOME_ERROR                        = ( 0x0B, 0x00008000, 15 ) # SPI_STATUS_SELECTION
    XLATCH_DONE                       = ( 0x0B, 0x00010000, 16 ) # SPI_STATUS_SELECTION
    FS_ACTIVE                         = ( 0x0B, 0x00020000, 17 ) # SPI_STATUS_SELECTION
    COVER_DONE                        = ( 0x0B, 0x02000000, 25 ) # SPI_STATUS_SELECTION
    STOP_ON_STALL                     = ( 0x0B, 0x20000000, 29 ) # SPI_STATUS_SELECTION
    MOTOR_EV                          = ( 0x0B, 0x40000000, 30 ) # SPI_STATUS_SELECTION
    RST_EV                            = ( 0x0B, 0x80000000, 31 ) # SPI_STATUS_SELECTION

    # STATUS
    TARGET_REACHED_F                  = ( 0x0F, 0x00000001,  0 ) # STATUS
    POS_COMP_REACHED_F                = ( 0x0F, 0x00000002,  1 ) # STATUS
    VEL_REACHED_F                     = ( 0x0F, 0x00000004,  2 ) # STATUS
    VEL_STATE_F                       = ( 0x0F, 0x00000018,  3 ) # STATUS
    RAMP_STATE_F                      = ( 0x0F, 0x00000060,  5 ) # STATUS
    STOPL_ACTIVE_F                    = ( 0x0F, 0x00000080,  7 ) # STATUS
    STOPR_ACTIVE_F                    = ( 0x0F, 0x00000100,  8 ) # STATUS
    VSTOPL_ACTIVE_F                   = ( 0x0F, 0x00000200,  9 ) # STATUS
    VSTOPR_ACTIVE_F                   = ( 0x0F, 0x00000400, 10 ) # STATUS
    ACTIVE_STALL_F                    = ( 0x0F, 0x00000800, 11 ) # STATUS
    HOME_ERROR_F                      = ( 0x0F, 0x00001000, 12 ) # STATUS
    FS_ACTIVE_F                       = ( 0x0F, 0x00002000, 13 ) # STATUS

    # STP_LENGTH_ADD / DIR_SETUP_TIME
    STP_LENGTH_ADD                    = ( 0x10, 0x0000FFFF,  0 ) # STP_LENGTH_ADD / DIR_SETUP_TIME
    DIR_SETUP_TIME                    = ( 0x10, 0xFFFF0000, 16 ) # STP_LENGTH_ADD / DIR_SETUP_TIME

    # START_OUT_ADD
    START_OUT_ADD                     = ( 0x11, 0xFFFFFFFF,  0 ) # START_OUT_ADD

    # GEAR_RATIO
    GEAR_RATIO                        = ( 0x12, 0xFFFFFFFF,  0 ) # GEAR_RATIO

    # START_DELAY
    START_DELAY                       = ( 0x13, 0xFFFFFFFF,  0 ) # START_DELAY

    # CLK_GATING_DELAY
    CLK_GATING_DELAY                  = ( 0x14, 0xFFFFFFFF,  0 ) # CLK_GATING_DELAY

    # STDBY_DELAY
    STDBY_DELAY                       = ( 0x15, 0xFFFFFFFF,  0 ) # STDBY_DELAY

    # FREEWHEEL_DELAY
    FREEWHEEL_DELAY                   = ( 0x16, 0xFFFFFFFF,  0 ) # FREEWHEEL_DELAY

    # VDRV_SCALE_LIMIT / PWM_VMAX
    VDRV_SCALE_LIMIT                  = ( 0x17, 0x00FFFFFF,  0 ) # VDRV_SCALE_LIMIT / PWM_VMAX
    PWM_VMAX                          = ( 0x17, 0x00FFFFFF,  0 ) # VDRV_SCALE_LIMIT / PWM_VMAX

    # UP_SCALE_DELAY
    UP_SCALE_DELAY                    = ( 0x18, 0x00FFFFFF,  0 ) # UP_SCALE_DELAY

    # HOLD_SCALE_DELAY
    HOLD_SCALE_DELAY                  = ( 0x19, 0x00FFFFFF,  0 ) # HOLD_SCALE_DELAY

    # DRV_SCALE_DELAY
    DRV_SCALE_DELAY                   = ( 0x1A, 0x00FFFFFF,  0 ) # DRV_SCALE_DELAY

    # BOOST_TIME
    BOOST_TIME                        = ( 0x1B, 0x00FFFFFF,  0 ) # BOOST_TIME

    # SPI_SWITCH_VEL / DAC ADDR
    SPI_SWITCH_VEL                    = ( 0x1D, 0x00FFFFFF,  0 ) # SPI_SWITCH_VEL / DAC ADDR
    DAC_ADDR_A                        = ( 0x1D, 0x0000FFFF,  0 ) # SPI_SWITCH_VEL / DAC ADDR
    DAC_ADDR_B                        = ( 0x1D, 0xFFFF0000, 16 ) # SPI_SWITCH_VEL / DAC ADDR

    # HOME_SAFETY_MARGIN
    HOME_SAFETY_MARGIN                = ( 0x1E, 0x0000FFFF,  0 ) # HOME_SAFETY_MARGIN

    # PWM_FREQ / CHOPSYNC_DIV
    PWM_FREQ                          = ( 0x1F, 0x0000FFFF,  0 ) # PWM_FREQ / CHOPSYNC_DIV
    CHOPSYNC_DIV                      = ( 0x1F, 0x00000FFF,  0 ) # PWM_FREQ / CHOPSYNC_DIV

    # RAMPMODE
    OPERATION_MODE                    = ( 0x20, 0x00000004,  2 ) # RAMPMODE
    RAMP_PROFILE                      = ( 0x20, 0x00000003,  0 ) # RAMPMODE

    # XACTUAL
    XACTUAL                           = ( 0x21, 0xFFFFFFFF,  0 ) # XACTUAL

    # VACTUAL
    VACTUAL                           = ( 0x22, 0xFFFFFFFF,  0 ) # VACTUAL

    # AACTUAL
    AACTUAL                           = ( 0x23, 0xFFFFFFFF,  0 ) # AACTUAL

    # VMAX
    VMAX                              = ( 0x24, 0xFFFFFFFF,  0 ) # VMAX

    # VSTART
    VSTART                            = ( 0x25, 0x7FFFFFFF,  0 ) # VSTART

    # VSTOP
    VSTOP                             = ( 0x26, 0x7FFFFFFF,  0 ) # VSTOP

    # VBREAK
    VBREAK                            = ( 0x27, 0x7FFFFFFF,  0 ) # VBREAK

    # AMAX
    FREQUENCY_MODE                    = ( 0x28, 0x00FFFFFF,  0 ) # AMAX
    DIRECT_MODE                       = ( 0x28, 0x00FFFFFF,  0 ) # AMAX

    # ASTART
    SIGN_AACT                         = ( 0x2A, 0x80000000, 31 ) # ASTART

    # CLK_FREQ
    CLK_FREQ                          = ( 0x31, 0x01FFFFFF,  0 ) # CLK_FREQ

    # POS_COMP
    POS_COMP                          = ( 0x32, 0xFFFFFFFF,  0 ) # POS_COMP

    # VIRT_STOP_LEFT
    VIRT_STOP_LEFT                    = ( 0x33, 0xFFFFFFFF,  0 ) # VIRT_STOP_LEFT

    # VIRT_STOP_RIGHT
    VIRT_STOP_RIGHT                   = ( 0x34, 0xFFFFFFFF,  0 ) # VIRT_STOP_RIGHT

    # X_HOME
    X_HOME                            = ( 0x35, 0xFFFFFFFF,  0 ) # X_HOME

    # X_LATCH / REV_CNT / X_RANGE
    X_LATCH                           = ( 0x36, 0xFFFFFFFF,  0 ) # X_LATCH / REV_CNT / X_RANGE
    REV_CNT                           = ( 0x36, 0xFFFFFFFF,  0 ) # X_LATCH / REV_CNT / X_RANGE
    X_RANGE                           = ( 0x36, 0xFFFFFFFF,  0 ) # X_LATCH / REV_CNT / X_RANGE

    # XTARGET
    XTARGET                           = ( 0x37, 0xFFFFFFFF,  0 ) # XTARGET

    # X_PIPE0
    X_PIPE0                           = ( 0x38, 0xFFFFFFFF,  0 ) # X_PIPE0

    # X_PIPE1
    X_PIPE1                           = ( 0x39, 0xFFFFFFFF,  0 ) # X_PIPE1

    # X_PIPE2
    X_PIPE2                           = ( 0x3A, 0xFFFFFFFF,  0 ) # X_PIPE2

    # X_PIPE3
    X_PIPE3                           = ( 0x3B, 0xFFFFFFFF,  0 ) # X_PIPE3

    # X_PIPE4
    X_PIPE4                           = ( 0x3C, 0xFFFFFFFF,  0 ) # X_PIPE4

    # X_PIPE5
    X_PIPE5                           = ( 0x3D, 0xFFFFFFFF,  0 ) # X_PIPE5

    # X_PIPE6
    X_PIPE6                           = ( 0x3E, 0xFFFFFFFF,  0 ) # X_PIPE6

    # X_PIPE7
    X_PIPE7                           = ( 0x3F, 0xFFFFFFFF,  0 ) # X_PIPE7

    # SH_REG0
    SH_REG0_VMAX                      = ( 0x40, 0xFFFFFFFF,  0 ) # SH_REG0

    # SH_REG1
    SH_REG1_AMAX                      = ( 0x41, 0x00FFFFFF,  0 ) # SH_REG1

    # SH_REG2
    SH_REG2_DMAX                      = ( 0x42, 0x00FFFFFF,  0 ) # SH_REG2

    # SH_REG3
    SH_REG3_ASTART                    = ( 0x43, 0x00FFFFFF,  0 ) # SH_REG3
    SH_REG3_BOW1                      = ( 0x43, 0x00FFFFFF,  0 ) # SH_REG3

    # SH_REG4
    SH_REG4_DFINAL                    = ( 0x44, 0x00FFFFFF,  0 ) # SH_REG4
    SH_REG4_BOW2                      = ( 0x44, 0x00FFFFFF,  0 ) # SH_REG4

    # SH_REG5
    SH_REG5_VBREAK                    = ( 0x45, 0x7FFFFFFF,  0 ) # SH_REG5
    SH_REG5_BOW3                      = ( 0x45, 0x00FFFFFF,  0 ) # SH_REG5

    # SH_REG6
    SH_REG6_VSTART                    = ( 0x46, 0x7FFFFFFF,  0 ) # SH_REG6
    SH_REG6_BOW4                      = ( 0x46, 0x00FFFFFF,  0 ) # SH_REG6
    SH_REG6_VSTOP                     = ( 0x46, 0x7FFFFFFF,  0 ) # SH_REG6

    # SH_REG7
    SH_REG7_VSTOP                     = ( 0x47, 0xFFFFFFFF,  0 ) # SH_REG7
    SH_REG7_VMAX                      = ( 0x47, 0xFFFFFFFF,  0 ) # SH_REG7

    # SH_REG8
    SH_REG8_BOW1                      = ( 0x48, 0x00FFFFFF,  0 ) # SH_REG8
    SH_REG8_AMAX                      = ( 0x48, 0x00FFFFFF,  0 ) # SH_REG8

    # SH_REG9
    SH_REG9_BOW2                      = ( 0x49, 0x00FFFFFF,  0 ) # SH_REG9
    SH_REG9_DMAX                      = ( 0x49, 0x00FFFFFF,  0 ) # SH_REG9

    # SH_REG10
    SH_REG10_BOW3                     = ( 0x4A, 0x00FFFFFF,  0 ) # SH_REG10
    SH_REG10_BOW1                     = ( 0x4A, 0x00FFFFFF,  0 ) # SH_REG10
    SH_REG10_ASTART                   = ( 0x4A, 0x00FFFFFF,  0 ) # SH_REG10

    # SH_REG11
    SH_REG11_BOW4                     = ( 0x4B, 0x00FFFFFF,  0 ) # SH_REG11
    SH_REG11_BOW2                     = ( 0x4B, 0x00FFFFFF,  0 ) # SH_REG11
    SH_REG11_DFINAL                   = ( 0x4B, 0x00FFFFFF,  0 ) # SH_REG11

    # SH_REG12
    SH_REG12_BOW3                     = ( 0x4C, 0x00FFFFFF,  0 ) # SH_REG12
    SH_REG12_VBREAK                   = ( 0x4C, 0x7FFFFFFF,  0 ) # SH_REG12

    # SH_REG13
    SH_REG13_BOW4                     = ( 0x4D, 0x00FFFFFF,  0 ) # SH_REG13
    SH_REG13_VSTART                   = ( 0x4D, 0x7FFFFFFF,  0 ) # SH_REG13
    SH_REG13_VSTOP                    = ( 0x4D, 0x7FFFFFFF,  0 ) # SH_REG13

    # CLK Gating / SW Reset
    CLK_GATING_REG                    = ( 0x4F, 0x00000007,  0 ) # CLK GATING / SW RESET
    RESET_REG                         = ( 0x4F, 0xFFFFFF00,  8 ) # CLK GATING / SW RESET

    # FS_VEL / DC_VEL
    FS_VEL                            = ( 0x60, 0x00FFFFFF,  0 ) # FS_VEL / DC_VEL
    DC_VEL                            = ( 0x60, 0x00FFFFFF,  0 ) # FS_VEL / DC_VEL

    # DC_TIME / DC_SG / DC_BLKTIME
    DC_TIME                           = ( 0x61, 0x000000FF,  0 ) # DC_TIME / DC_SG / DC_BLKTIME
    DC_SG                             = ( 0x61, 0x0000FF00,  8 ) # DC_TIME / DC_SG / DC_BLKTIME
    DC_BLKTIME                        = ( 0x61, 0xFFFF0000, 16 ) # DC_TIME / DC_SG / DC_BLKTIME

    # DC_LSPTM
    DC_LSPTM                          = ( 0x62, 0xFFFFFFFF,  0 ) # DC_LSPTM

    # VSTALL_LIMIT
    VSTALL_LIMIT                      = ( 0x67, 0x00FFFFFF,  0 ) # VSTALL_LIMIT

    # COVER_LOW / POLLING_STATUS
    POLLING_STATUS                    = ( 0x6C, 0xFFFFFFFF,  0 ) # COVER_LOW / POLLING_STATUS
    COVER_LOW                         = ( 0x6C, 0xFFFFFFFF,  0 ) # COVER_LOW / POLLING_STATUS

    # COVER_HIGH / POLLING_REG
    POLLING_REG_GSTAT                 = ( 0x6D, 0xF0000000, 28 ) # COVER_HIGH / POLLING_REG
    POLLING_REG_PWM_SCALE             = ( 0x6D, 0x0FF00000, 20 ) # COVER_HIGH / POLLING_REG
    POLLING_REG_LOST_STEPS            = ( 0x6D, 0xFFFFFFFF,  0 ) # COVER_HIGH / POLLING_REG
    COVER_HIGH                        = ( 0x6D, 0xFFFFFFFF,  0 ) # COVER_HIGH / POLLING_REG

    # COVER_DRV_LOW
    COVER_DRV_LOW                     = ( 0x6E, 0xFFFFFFFF,  0 ) # COVER_DRV_LOW

    # COVER_DRV_HIGH
    COVER_DRV_HIGH                    = ( 0x6F, 0xFFFFFFFF,  0 ) # COVER_DRV_HIGH

    # MSLUT[0]
    MSLUT__                           = ( 0x70, 0xFFFFFFFF,  0 ) # MSLUT[0]

    # MSLUTSEL
    MSLUTSEL                          = ( 0x78, 0xFFFFFFFF,  0 ) # MSLUTSEL

    # MSCNT / MSOFFSET
    MSCNT                             = ( 0x79, 0x000003FF,  0 ) # MSCNT / MSOFFSET
    MSOFFSET                          = ( 0x79, 0x000003FF,  0 ) # MSCNT / MSOFFSET

    # CURRENTA/B
    CURRENTA                          = ( 0x7A, 0x000001FF,  0 ) # CURRENTA/B
    CURRENTB                          = ( 0x7A, 0x01FF0000, 16 ) # CURRENTA/B

    # CURRENTA/B_SPI / TZEROWAIT
    CURRENTA_SPI                      = ( 0x7B, 0x000001FF,  0 ) # CURRENTA/B_SPI / TZEROWAIT
    CURRENTB_SPI                      = ( 0x7B, 0x01FF0000, 16 ) # CURRENTA/B_SPI / TZEROWAIT
    TZEROWAIT                         = ( 0x7B, 0xFFFFFFFF,  0 ) # CURRENTA/B_SPI / TZEROWAIT

    # SCALE_PARAM / CIRCULAR_DEC
    SCALE_PARAM                       = ( 0x7C, 0x000001FF,  0 ) # SCALE_PARAM / CIRCULAR_DEC
    CIRCULAR_DEC                      = ( 0x7C, 0xFFFFFFFF,  0 ) # SCALE_PARAM / CIRCULAR_DEC

    # START_SIN... / DAC_OFFSET
    START_SIN                         = ( 0x7E, 0x000000FF,  0 ) # START_SIN... / DAC_OFFSET
    START_SIN90_120                   = ( 0x7E, 0x00FF0000, 16 ) # START_SIN... / DAC_OFFSET
    DAC_OFFSET                        = ( 0x7E, 0xFF000000, 24 ) # START_SIN... / DAC_OFFSET

    # VERSION_NO
    VERSION_NO                        = ( 0x7F, 0x0000000F,  0 ) # VERSION_NO
