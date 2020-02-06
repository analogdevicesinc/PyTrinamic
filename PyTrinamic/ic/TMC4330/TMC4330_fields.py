'''
Created on 06.02.2020

@author: JM
'''

class TMC4330_fields(object):
    """
    Define all register bitfields of the TMC4330.

    Each field is defined as a tuple consisting of ( Address, Mask, Shift ).

    The name of the register is written as a comment behind each tuple. This is
    intended for IDE users viewing the definition of a field by hovering over
    it. This allows the user to see the corresponding register name of a field
    without opening this file and searching for the definition.
    """

    # GENERAL_CONF
    USE_ASTART_AND_VSTART               = ( 0x00, 0x00000001,  0 ) # GENERAL_CONF
    DIRECT_ACC_VAL_EN                   = ( 0x00, 0x00000002,  1 ) # GENERAL_CONF
    DIRECT_BOW_VAL_EN                   = ( 0x00, 0x00000004,  2 ) # GENERAL_CONF
    STEP_INACTIVE_POL                   = ( 0x00, 0x00000008,  3 ) # GENERAL_CONF
    TOGGLE_STEP                         = ( 0x00, 0x00000010,  4 ) # GENERAL_CONF
    POL_DIR_OUT                         = ( 0x00, 0x00000020,  5 ) # GENERAL_CONF
    SDIN_MODE                           = ( 0x00, 0x000000c0,  6 ) # GENERAL_CONF
    POL_DIR_IN                          = ( 0x00, 0x00000100,  8 ) # GENERAL_CONF
    SD_INDIRECT_CONTROL                 = ( 0x00, 0x00000200,  9 ) # GENERAL_CONF
    SERIAL_ENC_IN_MODE                  = ( 0x00, 0x00000c00, 10 ) # GENERAL_CONF
    DIFF_ENC_IN_DISABLE                 = ( 0x00, 0x00001000, 12 ) # GENERAL_CONF
    INTR_POL                            = ( 0x00, 0x00008000, 15 ) # GENERAL_CONF
    INVERT_POL_TARGET_REACHED           = ( 0x00, 0x00010000, 16 ) # GENERAL_CONF
    PWM_OUT_EN                          = ( 0x00, 0x00800000, 23 ) # GENERAL_CONF
    AUTOMATIC_DIRECT_SDIN_SWITCH_OFF    = ( 0x00, 0x04000000, 26 ) # GENERAL_CONF
    CIRCULAR_CNT_AS_XLATCH              = ( 0x00, 0x08000000, 27 ) # GENERAL_CONF
    REVERSE_MOTOR_DIR                   = ( 0x00, 0x10000000, 28 ) # GENERAL_CONF
    INTR_TR_PU_PD_EN                    = ( 0x00, 0x20000000, 29 ) # GENERAL_CONF
    INTR_AS_WIRED_AND                   = ( 0x00, 0x40000000, 30 ) # GENERAL_CONF
    TR_AS_WIRED_AND                     = ( 0x00, 0x80000000, 31 ) # GENERAL_CONF

    # REFERENCE_CONF
    STOP_LEFT_EN                        = ( 0x01, 0x00000001,  0 ) # REFERENCE_CONF
    STOP_RIGHT_EN                       = ( 0x01, 0x00000002,  1 ) # REFERENCE_CONF
    POL_STOP_LEFT                       = ( 0x01, 0x00000004,  2 ) # REFERENCE_CONF
    POL_STOP_RIGHT                      = ( 0x01, 0x00000008,  3 ) # REFERENCE_CONF
    INVERT_STOP_DIRECTION               = ( 0x01, 0x00000010,  4 ) # REFERENCE_CONF
    SOFT_STOP_EN                        = ( 0x01, 0x00000020,  5 ) # REFERENCE_CONF
    VIRTUAL_LEFT_LIMIT_EN               = ( 0x01, 0x00000040,  6 ) # REFERENCE_CONF
    VIRTUAL_RIGHT_LIMIT_EN              = ( 0x01, 0x00000080,  7 ) # REFERENCE_CONF
    VIRT_STOP_MODE                      = ( 0x01, 0x00000300,  8 ) # REFERENCE_CONF
    LATCH_X_ON_INACTIVE_L               = ( 0x01, 0x00000400, 10 ) # REFERENCE_CONF
    LATCH_X_ON_ACTIVE_L                 = ( 0x01, 0x00000800, 11 ) # REFERENCE_CONF
    LATCH_X_ON_INACTIVE_R               = ( 0x01, 0x00001000, 12 ) # REFERENCE_CONF
    LATCH_X_ON_ACTIVE_R                 = ( 0x01, 0x00002000, 13 ) # REFERENCE_CONF
    STOP_LEFT_IS_HOME                   = ( 0x01, 0x00004000, 14 ) # REFERENCE_CONF
    HOME_EVENT                          = ( 0x01, 0x000f0000, 16 ) # REFERENCE_CONF
    START_HOME_TRACKING                 = ( 0x01, 0x00100000, 20 ) # REFERENCE_CONF
    CLR_POS_AT_TARGET                   = ( 0x01, 0x00200000, 21 ) # REFERENCE_CONF
    CIRCULAR_MOVEMENT_EN                = ( 0x01, 0x00400000, 22 ) # REFERENCE_CONF
    POS_COMP_OUTPUT                     = ( 0x01, 0x01800000, 23 ) # REFERENCE_CONF
    POS_COMP_SOURCE                     = ( 0x01, 0x02000000, 25 ) # REFERENCE_CONF
    MODIFIED_POS_COPARE                 = ( 0x01, 0x30000000, 28 ) # REFERENCE_CONF
    CIRCULAR_ENC_EN                     = ( 0x01, 0x80000000, 31 ) # REFERENCE_CONF

    # START_CONF
    START_EN_0_                         = ( 0x02, 0x00000001,  0 ) # START_CONF
    START_EN_1_                         = ( 0x02, 0x00000002,  1 ) # START_CONF
    START_EN_2_                         = ( 0x02, 0x00000004,  2 ) # START_CONF
    START_EN_3_                         = ( 0x02, 0x00000008,  3 ) # START_CONF
    START_EN_4_                         = ( 0x02, 0x00000010,  4 ) # START_CONF
    TRIGGER_EVENTS_0_                   = ( 0x02, 0x00000020,  5 ) # START_CONF
    TRIGGER_EVENTS_1_                   = ( 0x02, 0x00000040,  6 ) # START_CONF
    TRIGGER_EVENTS_2_                   = ( 0x02, 0x00000080,  7 ) # START_CONF
    TRIGGER_EVENTS_3_                   = ( 0x02, 0x00000100,  8 ) # START_CONF
    POL_START_SIGNAL                    = ( 0x02, 0x00000200,  9 ) # START_CONF
    IMMEDIATE_START_IN                  = ( 0x02, 0x00000400, 10 ) # START_CONF
    BUSY_STATE_EN                       = ( 0x02, 0x00000800, 11 ) # START_CONF
    PIPELINE_EN_0_                      = ( 0x02, 0x00001000, 12 ) # START_CONF
    PIPELINE_EN_1_                      = ( 0x02, 0x00002000, 13 ) # START_CONF
    PIPELINE_EN_2_                      = ( 0x02, 0x00004000, 14 ) # START_CONF
    PIPELINE_EN_3_                      = ( 0x02, 0x00008000, 15 ) # START_CONF
    SHADOW_OPTION                       = ( 0x02, 0x00030000, 16 ) # START_CONF
    CYCLIC_SHADOW_REGS                  = ( 0x02, 0x00040000, 18 ) # START_CONF
    SHADOW_MISS_CNT                     = ( 0x02, 0x00f00000, 20 ) # START_CONF
    XPIPE_REWRITE_REG_0_                = ( 0x02, 0x01000000, 24 ) # START_CONF
    XPIPE_REWRITE_REG_1_                = ( 0x02, 0x02000000, 25 ) # START_CONF
    XPIPE_REWRITE_REG_2_                = ( 0x02, 0x04000000, 26 ) # START_CONF
    XPIPE_REWRITE_REG_3_                = ( 0x02, 0x08000000, 27 ) # START_CONF
    XPIPE_REWRITE_REG_4_                = ( 0x02, 0x10000000, 28 ) # START_CONF
    XPIPE_REWRITE_REG_5_                = ( 0x02, 0x20000000, 29 ) # START_CONF
    XPIPE_REWRITE_REG_6_                = ( 0x02, 0x40000000, 30 ) # START_CONF
    XPIPE_REWRITE_REG_7_                = ( 0x02, 0x80000000, 31 ) # START_CONF

    # INPUT_FILT_CONF
    SR_ENC_IN                           = ( 0x03, 0x00000007,  0 ) # INPUT_FILT_CONF
    FILT_L_ENC_IN                       = ( 0x03, 0x00000070,  4 ) # INPUT_FILT_CONF
    SR_REF                              = ( 0x03, 0x00000700,  8 ) # INPUT_FILT_CONF
    FILT_L_REF                          = ( 0x03, 0x00007000, 12 ) # INPUT_FILT_CONF
    SR_S                                = ( 0x03, 0x00070000, 16 ) # INPUT_FILT_CONF
    FILT_L_S                            = ( 0x03, 0x00700000, 20 ) # INPUT_FILT_CONF
    SR_SD_IN                            = ( 0x03, 0x07000000, 24 ) # INPUT_FILT_CONF
    FILT_L_SD_IN                        = ( 0x03, 0x70000000, 28 ) # INPUT_FILT_CONF
    SD_FILT_ON                          = ( 0x03, 0x80000000, 31 ) # INPUT_FILT_CONF

    # SCALE_CONF
    STDBY_EN                            = ( 0x05, 0x00000001,  0 ) # SCALE_CONF
    PWM_SCALE_EN                        = ( 0x05, 0x00000100,  8 ) # SCALE_CONF
    PWM_AMPL                            = ( 0x05, 0xffff0000, 16 ) # SCALE_CONF

    # ENC_IN_CONF
    ENC_SEL_DECIMAL                     = ( 0x07, 0x00000001,  0 ) # ENC_IN_CONF
    CLEAR_ON_N                          = ( 0x07, 0x00000002,  1 ) # ENC_IN_CONF
    CLR_LATCH_CONT_ON_N                 = ( 0x07, 0x00000004,  2 ) # ENC_IN_CONF
    CLR_LATCH_ONCE_ON_N                 = ( 0x07, 0x00000008,  3 ) # ENC_IN_CONF
    POL_N                               = ( 0x07, 0x00000010,  4 ) # ENC_IN_CONF
    N_CHAN_SENSITIVITY                  = ( 0x07, 0x00000060,  5 ) # ENC_IN_CONF
    POL_A_FOR_N                         = ( 0x07, 0x00000080,  7 ) # ENC_IN_CONF
    POL_B_FOR_N                         = ( 0x07, 0x00000100,  8 ) # ENC_IN_CONF
    IGNORE_AB                           = ( 0x07, 0x00000200,  9 ) # ENC_IN_CONF
    LATCH_ENC_ON_N                      = ( 0x07, 0x00000400, 10 ) # ENC_IN_CONF
    LATCH_X_ON_N                        = ( 0x07, 0x00000800, 11 ) # ENC_IN_CONF
    MULTI_TURN_IN_EN                    = ( 0x07, 0x00001000, 12 ) # ENC_IN_CONF
    MULTI_TURN_IN_SIGNED                = ( 0x07, 0x00002000, 13 ) # ENC_IN_CONF
    USE_USTEPS_INSTEAD_OF_XRANGE        = ( 0x07, 0x00008000, 15 ) # ENC_IN_CONF
    CALC_MULTI_TURN_BEHAV               = ( 0x07, 0x00010000, 16 ) # ENC_IN_CONF
    SSI_MULTI_CYCLE_DATA                = ( 0x07, 0x00020000, 17 ) # ENC_IN_CONF
    SSI_GRAY_CODE_EN                    = ( 0x07, 0x00040000, 18 ) # ENC_IN_CONF
    LEFT_ALIGNED_DATA                   = ( 0x07, 0x00080000, 19 ) # ENC_IN_CONF
    SPI_DATA_ON_CS                      = ( 0x07, 0x00100000, 20 ) # ENC_IN_CONF
    SPI_LOW_BEFORE_CS                   = ( 0x07, 0x00200000, 21 ) # ENC_IN_CONF
    REGULATION_MODUS                    = ( 0x07, 0x00c00000, 22 ) # ENC_IN_CONF
    CL_CALIBRATION_EN                   = ( 0x07, 0x01000000, 24 ) # ENC_IN_CONF
    CL_EMF_EN                           = ( 0x07, 0x02000000, 25 ) # ENC_IN_CONF
    CL_CLR_XACT                         = ( 0x07, 0x04000000, 26 ) # ENC_IN_CONF
    CL_VLIMIT_EN                        = ( 0x07, 0x08000000, 27 ) # ENC_IN_CONF
    CL_VELOCITY_MODE_EN                 = ( 0x07, 0x10000000, 28 ) # ENC_IN_CONF
    INVERT_ENC_DIR                      = ( 0x07, 0x20000000, 29 ) # ENC_IN_CONF
    NO_ENC_VEL_PREPROC                  = ( 0x07, 0x80000000, 31 ) # ENC_IN_CONF
    SERIAL_ENC_VARIATION_LIMIT          = ( 0x07, 0x80000000, 31 ) # ENC_IN_CONF

    # ENC_IN_DATA
    SINGLE_TURN_RES                     = ( 0x08, 0x0000001f,  0 ) # ENC_IN_DATA
    MULTI_TURN_RES                      = ( 0x08, 0x000003e0,  5 ) # ENC_IN_DATA
    STATUS_BIT_CNT                      = ( 0x08, 0x00000c00, 10 ) # ENC_IN_DATA
    SERIAL_ADDR_BITS                    = ( 0x08, 0x00ff0000, 16 ) # ENC_IN_DATA
    SERIAL_DATA_BITS                    = ( 0x08, 0xff000000, 24 ) # ENC_IN_DATA

    # STEP_CONF
    MSTEP_PER_FS                        = ( 0x0A, 0x0000000f,  0 ) # STEP_CONF
    FS_PER_REV                          = ( 0x0A, 0x0000fff0,  4 ) # STEP_CONF

    # SPI_STATUS_SELECTION
    TARGET_REACHED                      = ( 0x0B, 0x00000001,  0 ) # SPI_STATUS_SELECTION
    POS_COMP_REACHED                    = ( 0x0B, 0x00000002,  1 ) # SPI_STATUS_SELECTION
    VEL_REACHED                         = ( 0x0B, 0x00000004,  2 ) # SPI_STATUS_SELECTION
    VEL_STATE_00                        = ( 0x0B, 0x00000008,  3 ) # SPI_STATUS_SELECTION
    VEL_STATE_01                        = ( 0x0B, 0x00000010,  4 ) # SPI_STATUS_SELECTION
    VEL_STATE_10                        = ( 0x0B, 0x00000020,  5 ) # SPI_STATUS_SELECTION
    RAMP_STATE_00                       = ( 0x0B, 0x00000040,  6 ) # SPI_STATUS_SELECTION
    RAMP_STATE_01                       = ( 0x0B, 0x00000080,  7 ) # SPI_STATUS_SELECTION
    RAMP_STATE_10                       = ( 0x0B, 0x00000100,  8 ) # SPI_STATUS_SELECTION
    MAX_PHASE_TRAP                      = ( 0x0B, 0x00000200,  9 ) # SPI_STATUS_SELECTION
    STOPL_EVENT                         = ( 0x0B, 0x00000800, 11 ) # SPI_STATUS_SELECTION
    STOPR_EVENT                         = ( 0x0B, 0x00001000, 12 ) # SPI_STATUS_SELECTION
    VSTOPL_ACTIVE                       = ( 0x0B, 0x00002000, 13 ) # SPI_STATUS_SELECTION
    HOME_ERROR                          = ( 0x0B, 0x00008000, 15 ) # SPI_STATUS_SELECTION
    XLATCH_DONE                         = ( 0x0B, 0x00010000, 16 ) # SPI_STATUS_SELECTION
    FS_ACTIVE                           = ( 0x0B, 0x00020000, 17 ) # SPI_STATUS_SELECTION
    ENC_FAIL                            = ( 0x0B, 0x00040000, 18 ) # SPI_STATUS_SELECTION
    N_ACTIVE                            = ( 0x0B, 0x00080000, 19 ) # SPI_STATUS_SELECTION
    ENC_DONE                            = ( 0x0B, 0x00100000, 20 ) # SPI_STATUS_SELECTION
    SER_ENC_DATA_FAIL                   = ( 0x0B, 0x00200000, 21 ) # SPI_STATUS_SELECTION
    SER_DATA_DONE                       = ( 0x0B, 0x00800000, 23 ) # SPI_STATUS_SELECTION
    SERIAL_ENC_FLAGS                    = ( 0x0B, 0x01000000, 24 ) # SPI_STATUS_SELECTION
    ENC_VEL0                            = ( 0x0B, 0x04000000, 26 ) # SPI_STATUS_SELECTION
    CL_MAX                              = ( 0x0B, 0x08000000, 27 ) # SPI_STATUS_SELECTION
    CL_FIT                              = ( 0x0B, 0x10000000, 28 ) # SPI_STATUS_SELECTION
    RST_EV                              = ( 0x0B, 0x80000000, 31 ) # SPI_STATUS_SELECTION

    # STATUS
    TARGET_REACHED_F                    = ( 0x0F, 0x00000001,  0 ) # STATUS
    POS_COMP_REACHED_F                  = ( 0x0F, 0x00000002,  1 ) # STATUS
    VEL_REACHED_F                       = ( 0x0F, 0x00000004,  2 ) # STATUS
    VEL_STATE_F                         = ( 0x0F, 0x00000018,  3 ) # STATUS
    RAMP_STATE_F                        = ( 0x0F, 0x00000060,  5 ) # STATUS
    STOPL_ACTIVE_F                      = ( 0x0F, 0x00000080,  7 ) # STATUS
    STOPR_ACTIVE_F                      = ( 0x0F, 0x00000100,  8 ) # STATUS
    VSTOPL_ACTIVE_F                     = ( 0x0F, 0x00000200,  9 ) # STATUS
    VSTOPR_ACTIVE_F                     = ( 0x0F, 0x00000400, 10 ) # STATUS
    HOME_ERROR_F                        = ( 0x0F, 0x00001000, 12 ) # STATUS
    ENC_FAIL_F                          = ( 0x0F, 0x00004000, 14 ) # STATUS
    N_ACTIVE_F                          = ( 0x0F, 0x00008000, 15 ) # STATUS
    ENC_LATCH_F                         = ( 0x0F, 0x00010000, 16 ) # STATUS
    MULTI_CYCLE_FAIL_F___SER_ENC_VAR_F  = ( 0x0F, 0x00020000, 17 ) # STATUS
    SERIAL_ENC_FLAG__                   = ( 0x0F, 0x00100000, 20 ) # STATUS

    # STP_LENGTH_ADD / DIR_SETUP_TIME
    STP_LENGTH_ADD                      = ( 0x10, 0x0000FFFF,  0 ) # STP_LENGTH_ADD / DIR_SETUP_TIME
    DIR_SETUP_TIME                      = ( 0x10, 0xFFFF0000, 16 ) # STP_LENGTH_ADD / DIR_SETUP_TIME

    # START_OUT_ADD
    START_OUT_ADD                       = ( 0x11, 0xFFFFFFFF,  0 ) # START_OUT_ADD

    # GEAR_RATIO
    GEAR_RATIO                          = ( 0x12, 0xFFFFFFFF,  0 ) # GEAR_RATIO

    # START_DELAY
    START_DELAY                         = ( 0x13, 0xFFFFFFFF,  0 ) # START_DELAY

    # CLK_GATING_DELAY
    CLK_GATING_DELAY                    = ( 0x14, 0xFFFFFFFF,  0 ) # CLK_GATING_DELAY

    # STDBY_DELAY
    STDBY_DELAY                         = ( 0x15, 0xFFFFFFFF,  0 ) # STDBY_DELAY

    # PWM_VMAX
    PWM_VMAX                            = ( 0x17, 0x00FFFFFF,  0 ) # PWM_VMAX

    # CL ANGLES
    CL_BETA                             = ( 0x1C, 0x000001FF,  0 ) # CL ANGLES
    CL_GAMMA                            = ( 0x1C, 0x00FF0000, 16 ) # CL ANGLES

    # HOME_SAFETY_MARGIN
    HOME_SAFETY_MARGIN                  = ( 0x1E, 0x0000FFFF,  0 ) # HOME_SAFETY_MARGIN

    # PWM_FREQ
    PWM_FREQ                            = ( 0x1F, 0x0000FFFF,  0 ) # PWM_FREQ

    # RAMPMODE
    OPERATION_MODE                      = ( 0x20, 0x00000004,  2 ) # RAMPMODE
    RAMP_PROFILE                        = ( 0x20, 0x00000003,  0 ) # RAMPMODE

    # XACTUAL
    XACTUAL                             = ( 0x21, 0xFFFFFFFF,  0 ) # XACTUAL

    # VACTUAL
    VACTUAL                             = ( 0x22, 0xFFFFFFFF,  0 ) # VACTUAL

    # AACTUAL
    AACTUAL                             = ( 0x23, 0xFFFFFFFF,  0 ) # AACTUAL

    # VMAX
    VMAX                                = ( 0x24, 0xFFFFFFFF,  0 ) # VMAX

    # VSTART
    VSTART                              = ( 0x25, 0x7FFFFFFF,  0 ) # VSTART

    # VSTOP
    VSTOP                               = ( 0x26, 0x7FFFFFFF,  0 ) # VSTOP

    # VBREAK
    VBREAK                              = ( 0x27, 0x7FFFFFFF,  0 ) # VBREAK

    # AMAX
    FREQUENCY_MODE                      = ( 0x28, 0x00FFFFFF,  0 ) # AMAX
    DIRECT_MODE                         = ( 0x28, 0x00FFFFFF,  0 ) # AMAX

    # ASTART
    SIGN_AACT                           = ( 0x2A, 0x80000000, 31 ) # ASTART

    # CLK_FREQ
    CLK_FREQ                            = ( 0x31, 0x01FFFFFF,  0 ) # CLK_FREQ

    # POS_COMP
    POS_COMP                            = ( 0x32, 0xFFFFFFFF,  0 ) # POS_COMP

    # VIRT_STOP_LEFT
    VIRT_STOP_LEFT                      = ( 0x33, 0xFFFFFFFF,  0 ) # VIRT_STOP_LEFT

    # VIRT_STOP_RIGHT
    VIRT_STOP_RIGHT                     = ( 0x34, 0xFFFFFFFF,  0 ) # VIRT_STOP_RIGHT

    # X_HOME
    X_HOME                              = ( 0x35, 0xFFFFFFFF,  0 ) # X_HOME

    # X_LATCH / REV_CNT / X_RANGE
    X_LATCH                             = ( 0x36, 0xFFFFFFFF,  0 ) # X_LATCH / REV_CNT / X_RANGE
    REV_CNT                             = ( 0x36, 0xFFFFFFFF,  0 ) # X_LATCH / REV_CNT / X_RANGE
    X_RANGE                             = ( 0x36, 0xFFFFFFFF,  0 ) # X_LATCH / REV_CNT / X_RANGE

    # XTARGET
    XTARGET                             = ( 0x37, 0xFFFFFFFF,  0 ) # XTARGET

    # X_PIPE0
    X_PIPE0                             = ( 0x38, 0xFFFFFFFF,  0 ) # X_PIPE0

    # X_PIPE1
    X_PIPE1                             = ( 0x39, 0xFFFFFFFF,  0 ) # X_PIPE1

    # X_PIPE2
    X_PIPE2                             = ( 0x3A, 0xFFFFFFFF,  0 ) # X_PIPE2

    # X_PIPE3
    X_PIPE3                             = ( 0x3B, 0xFFFFFFFF,  0 ) # X_PIPE3

    # X_PIPE4
    X_PIPE4                             = ( 0x3C, 0xFFFFFFFF,  0 ) # X_PIPE4

    # X_PIPE5
    X_PIPE5                             = ( 0x3D, 0xFFFFFFFF,  0 ) # X_PIPE5

    # X_PIPE6
    X_PIPE6                             = ( 0x3E, 0xFFFFFFFF,  0 ) # X_PIPE6

    # X_PIPE7
    X_PIPE7                             = ( 0x3F, 0xFFFFFFFF,  0 ) # X_PIPE7

    # SH_REG0
    SH_REG0_VMAX                        = ( 0x40, 0xFFFFFFFF,  0 ) # SH_REG0

    # SH_REG1
    SH_REG1_AMAX                        = ( 0x41, 0x00FFFFFF,  0 ) # SH_REG1

    # SH_REG2
    SH_REG2_DMAX                        = ( 0x42, 0x00FFFFFF,  0 ) # SH_REG2

    # SH_REG3
    SH_REG3_ASTART                      = ( 0x43, 0x00FFFFFF,  0 ) # SH_REG3
    SH_REG3_BOW1                        = ( 0x43, 0x00FFFFFF,  0 ) # SH_REG3

    # SH_REG4
    SH_REG4_DFINAL                      = ( 0x44, 0x00FFFFFF,  0 ) # SH_REG4
    SH_REG4_BOW2                        = ( 0x44, 0x00FFFFFF,  0 ) # SH_REG4

    # SH_REG5
    SH_REG5_VBREAK                      = ( 0x45, 0x7FFFFFFF,  0 ) # SH_REG5
    SH_REG5_BOW3                        = ( 0x45, 0x00FFFFFF,  0 ) # SH_REG5

    # SH_REG6
    SH_REG6_VSTART                      = ( 0x46, 0x7FFFFFFF,  0 ) # SH_REG6
    SH_REG6_BOW4                        = ( 0x46, 0x00FFFFFF,  0 ) # SH_REG6
    SH_REG6_VSTOP                       = ( 0x46, 0x7FFFFFFF,  0 ) # SH_REG6

    # SH_REG7
    SH_REG7_VSTOP                       = ( 0x47, 0xFFFFFFFF,  0 ) # SH_REG7
    SH_REG7_VMAX                        = ( 0x47, 0xFFFFFFFF,  0 ) # SH_REG7

    # SH_REG8
    SH_REG8_BOW1                        = ( 0x48, 0x00FFFFFF,  0 ) # SH_REG8
    SH_REG8_AMAX                        = ( 0x48, 0x00FFFFFF,  0 ) # SH_REG8

    # SH_REG9
    SH_REG9_BOW2                        = ( 0x49, 0x00FFFFFF,  0 ) # SH_REG9
    SH_REG9_DMAX                        = ( 0x49, 0x00FFFFFF,  0 ) # SH_REG9

    # SH_REG10
    SH_REG10_BOW3                       = ( 0x4A, 0x00FFFFFF,  0 ) # SH_REG10
    SH_REG10_BOW1                       = ( 0x4A, 0x00FFFFFF,  0 ) # SH_REG10
    SH_REG10_ASTART                     = ( 0x4A, 0x00FFFFFF,  0 ) # SH_REG10

    # SH_REG11
    SH_REG11_BOW4                       = ( 0x4B, 0x00FFFFFF,  0 ) # SH_REG11
    SH_REG11_BOW2                       = ( 0x4B, 0x00FFFFFF,  0 ) # SH_REG11
    SH_REG11_DFINAL                     = ( 0x4B, 0x00FFFFFF,  0 ) # SH_REG11

    # SH_REG12
    SH_REG12_BOW3                       = ( 0x4C, 0x00FFFFFF,  0 ) # SH_REG12
    SH_REG12_VBREAK                     = ( 0x4C, 0x7FFFFFFF,  0 ) # SH_REG12

    # SH_REG13
    SH_REG13_BOW4                       = ( 0x4D, 0x00FFFFFF,  0 ) # SH_REG13
    SH_REG13_VSTART                     = ( 0x4D, 0x7FFFFFFF,  0 ) # SH_REG13
    SH_REG13_VSTOP                      = ( 0x4D, 0x7FFFFFFF,  0 ) # SH_REG13

    # CLK Gating / SW Reset
    CLK_GATING_REG                      = ( 0x4F, 0x00000007,  0 ) # CLK GATING / SW RESET
    RESET_REG                           = ( 0x4F, 0xFFFFFF00,  8 ) # CLK GATING / SW RESET

    # ENC_POS
    ENC_POS                             = ( 0x50, 0xFFFFFFFF,  0 ) # ENC_POS

    # ENC_LATCH / ENC_RESET_VAL
    ENC_LATCH                           = ( 0x51, 0xFFFFFFFF,  0 ) # ENC_LATCH / ENC_RESET_VAL
    ENC_RESET_VAL                       = ( 0x51, 0xFFFFFFFF,  0 ) # ENC_LATCH / ENC_RESET_VAL

    # ENC_POS_DEV / CL_TR_TOLERANCE
    ENC_POS_DEV                         = ( 0x52, 0xFFFFFFFF,  0 ) # ENC_POS_DEV / CL_TR_TOLERANCE
    CL_TR_TOLERANCE                     = ( 0x52, 0x7FFFFFFF,  0 ) # ENC_POS_DEV / CL_TR_TOLERANCE

    # ENC_POS_DEV_TOL
    ENC_POS_DEV_TOL                     = ( 0x53, 0x7FFFFFFF,  0 ) # ENC_POS_DEV_TOL

    # ENC_IN_RES / ENC_CONST
    ENC_CONST                           = ( 0x54, 0x7FFFFFFF,  0 ) # ENC_IN_RES / ENC_CONST
    ENC_IN_RES                          = ( 0x54, 0x7FFFFFFF,  0 ) # ENC_IN_RES / ENC_CONST
    MANUAL_ENC_CONST                    = ( 0x54, 0x80000000, 31 ) # ENC_IN_RES / ENC_CONST

    # ENC_OUT_RES
    ENC_OUT_RES                         = ( 0x55, 0x7FFFFFFF,  0 ) # ENC_OUT_RES

    # SER_CLK_IN_HIGH/LOW
    SER_CLK_IN_HIGH                     = ( 0x56, 0x0000FFFF,  0 ) # SER_CLK_IN_HIGH/LOW
    SER_CLK_IN_LOW                      = ( 0x56, 0xFFFF0000, 16 ) # SER_CLK_IN_HIGH/LOW

    # SSI_IN_CLK_DELAY / SSI_IN_WTIME
    SSI_IN_CLK_DELAY                    = ( 0x57, 0x0000FFFF,  0 ) # SSI_IN_CLK_DELAY / SSI_IN_WTIME
    SSI_IN_WTIME                        = ( 0x57, 0xFFFF0000, 16 ) # SSI_IN_CLK_DELAY / SSI_IN_WTIME

    # SER_PTIME
    SER_PTIME                           = ( 0x58, 0x000FFFFF,  0 ) # SER_PTIME

    # CL_OFFSET
    CL_OFFSET                           = ( 0x59, 0xFFFFFFFF,  0 ) # CL_OFFSET

    # PID_VEL / PID_P / CL_VMAX_CALC_P
    PID_VEL                             = ( 0x5A, 0xFFFFFFFF,  0 ) # PID_VEL / PID_P / CL_VMAX_CALC_P
    CL_VMAX_CALC_P                      = ( 0x5A, 0x00FFFFFF,  0 ) # PID_VEL / PID_P / CL_VMAX_CALC_P
    PID_P                               = ( 0x5A, 0x00FFFFFF,  0 ) # PID_VEL / PID_P / CL_VMAX_CALC_P

    # PID_ISUM_RD / PID_I / CL_VMAX_CALC_I
    PID_ISUM_RD                         = ( 0x5B, 0xFFFFFFFF,  0 ) # PID_ISUM_RD / PID_I / CL_VMAX_CALC_I
    CL_VMAX_CALC_I                      = ( 0x5B, 0x00FFFFFF,  0 ) # PID_ISUM_RD / PID_I / CL_VMAX_CALC_I
    PID_I                               = ( 0x5B, 0x00FFFFFF,  0 ) # PID_ISUM_RD / PID_I / CL_VMAX_CALC_I

    # PID_D / CL_DELTA_P
    CL_DELTA_P                          = ( 0x5C, 0x00FFFFFF,  0 ) # PID_D / CL_DELTA_P
    PID_D                               = ( 0x5C, 0x00FFFFFF,  0 ) # PID_D / CL_DELTA_P

    # PID_E / PID_I_CLIP / PID_D_CLKDIV
    PID_E                               = ( 0x5D, 0xFFFFFFFF,  0 ) # PID_E / PID_I_CLIP / PID_D_CLKDIV
    PID_I_CLIP                          = ( 0x5D, 0x00007FFF,  0 ) # PID_E / PID_I_CLIP / PID_D_CLKDIV
    PID_D_CLKDIV                        = ( 0x5D, 0x00FF0000, 16 ) # PID_E / PID_I_CLIP / PID_D_CLKDIV

    # PID_DV_CLIP
    PID_DV_CLIP                         = ( 0x5E, 0x7FFFFFFF,  0 ) # PID_DV_CLIP

    # PID_TOLERANCE / CL_TOLERANCE
    CL_TOLERANCE                        = ( 0x5F, 0x000000FF,  0 ) # PID_TOLERANCE / CL_TOLERANCE
    PID_TOLERANCE                       = ( 0x5F, 0x000FFFFF,  0 ) # PID_TOLERANCE / CL_TOLERANCE

    # CL_VMIN_EMF
    CL_VMIN_EMF                         = ( 0x60, 0x00FFFFFF,  0 ) # CL_VMIN_EMF

    # CL_VADD_EMF
    CL_VADD_EMF                         = ( 0x61, 0x00FFFFFF,  0 ) # CL_VADD_EMF

    # ENC_VEL_ZERO
    ENC_VEL_ZERO                        = ( 0x62, 0x00FFFFFF,  0 ) # ENC_VEL_ZERO

    # ENC_VMEAN_... / SER_ENC_VARIATION / CL_CYCLE
    ENC_VMEAN_WAIT                      = ( 0x63, 0x000000FF,  0 ) # ENC_VMEAN_... / SER_ENC_VARIATION / CL_CYCLE
    ENC_VMEAN_FILTER                    = ( 0x63, 0x00000F00,  8 ) # ENC_VMEAN_... / SER_ENC_VARIATION / CL_CYCLE
    ENC_VMEAN_INT                       = ( 0x63, 0xFFFF0000, 16 ) # ENC_VMEAN_... / SER_ENC_VARIATION / CL_CYCLE
    SER_ENC_VARIATION                   = ( 0x63, 0x000000FF,  0 ) # ENC_VMEAN_... / SER_ENC_VARIATION / CL_CYCLE
    CL_CYCLE                            = ( 0x63, 0xFFFF0000, 16 ) # ENC_VMEAN_... / SER_ENC_VARIATION / CL_CYCLE

    # V_ENC
    V_ENC                               = ( 0x65, 0xFFFFFFFF,  0 ) # V_ENC

    # V_ENC_MEAN
    V_ENC_MEAN                          = ( 0x66, 0xFFFFFFFF,  0 ) # V_ENC_MEAN

    # ADDR_TO_ENC
    ADDR_TO_ENC                         = ( 0x68, 0xFFFFFFFF,  0 ) # ADDR_TO_ENC

    # DATA_TO_ENC
    DATA_TO_ENC                         = ( 0x69, 0xFFFFFFFF,  0 ) # DATA_TO_ENC

    # ADDR_FROM_ENC
    ADDR_FROM_ENC                       = ( 0x6A, 0xFFFFFFFF,  0 ) # ADDR_FROM_ENC

    # DATA_FROM_ENC
    DATA_FROM_ENC                       = ( 0x6B, 0xFFFFFFFF,  0 ) # DATA_FROM_ENC

    # MSLUT[0]
    MSLUT__                             = ( 0x70, 0xFFFFFFFF,  0 ) # MSLUT[0]

    # MSLUTSEL
    MSLUTSEL                            = ( 0x78, 0xFFFFFFFF,  0 ) # MSLUTSEL

    # MSCNT
    MSCNT                               = ( 0x79, 0x000003FF,  0 ) # MSCNT

    # USTEPTA/B
    CURRENTA                            = ( 0x7A, 0x000001FF,  0 ) # USTEPTA/B
    CURRENTB                            = ( 0x7A, 0x01FF0000, 16 ) # USTEPTA/B

    # USTEPA/B_SCALE
    CURRENTA_SPI                        = ( 0x7B, 0x000001FF,  0 ) # USTEPA/B_SCALE
    CURRENTB_SPI                        = ( 0x7B, 0x01FF0000, 16 ) # USTEPA/B_SCALE
    TZEROWAIT                           = ( 0x7B, 0xFFFFFFFF,  0 ) # USTEPA/B_SCALE

    # CIRCULAR_DEC
    CIRCULAR_DEC                        = ( 0x7C, 0xFFFFFFFF,  0 ) # CIRCULAR_DEC

    # ENC_COMP_...
    ENC_COMP_XOFFSET                    = ( 0x7D, 0x0000FFFF,  0 ) # ENC_COMP_...
    ENC_COMP_YOFFSET                    = ( 0x7D, 0x00FF0000, 16 ) # ENC_COMP_...

    # START_SIN...
    START_SIN                           = ( 0x7E, 0x000000FF,  0 ) # START_SIN...
    START_SIN90_120                     = ( 0x7E, 0x00FF0000, 16 ) # START_SIN...

    # VERSION_NO
    VERSION_NO                          = ( 0x7F, 0x0000000F,  0 ) # VERSION_NO
