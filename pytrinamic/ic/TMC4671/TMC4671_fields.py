class TMC4671_fields(object):
    """
    Defines all register bitfields of the TMC4671.

    Each field is defined as a tuple consisting of (address, mask, shift).

    The name of the register is written as a comment behind each tuple. This is
    intended for IDE users viewing the definition of a field by hovering over
    it. This allows the user to see the corresponding register name of a field
    without opening this file and searching for the definition.
    """

    # CHIPINFO_DATA
    SI_TYPE                                = (0x00, 0xFFFFFFFF,  0)  # CHIPINFO_DATA
    SI_VERSION                             = (0x00, 0xFFFFFFFF,  0)  # CHIPINFO_DATA
    SI_DATE                                = (0x00, 0xFFFFFFFF,  0)  # CHIPINFO_DATA
    SI_TIME                                = (0x00, 0xFFFFFFFF,  0)  # CHIPINFO_DATA
    SI_VARIANT                             = (0x00, 0xFFFFFFFF,  0)  # CHIPINFO_DATA
    SI_BUILD                               = (0x00, 0xFFFFFFFF,  0)  # CHIPINFO_DATA

    # CHIPINFO_ADDR
    CHIP_INFO_ADDRESS                      = (0x01, 0x000000FF,  0)  # CHIPINFO_ADDR

    # ADC_RAW_DATA
    ADC_I0_RAW                             = (0x02, 0x0000FFFF,  0)  # ADC_RAW_DATA
    ADC_I1_RAW                             = (0x02, 0xFFFF0000, 16)  # ADC_RAW_DATA
    ADC_VM_RAW                             = (0x02, 0x0000FFFF,  0)  # ADC_RAW_DATA
    ADC_AGPI_A_RAW                         = (0x02, 0xFFFF0000, 16)  # ADC_RAW_DATA
    ADC_AGPI_B_RAW                         = (0x02, 0x0000FFFF,  0)  # ADC_RAW_DATA
    ADC_AENC_UX_RAW                        = (0x02, 0xFFFF0000, 16)  # ADC_RAW_DATA
    ADC_AENC_VN_RAW                        = (0x02, 0x0000FFFF,  0)  # ADC_RAW_DATA
    ADC_AENC_WY_RAW                        = (0x02, 0xFFFF0000, 16)  # ADC_RAW_DATA

    # ADC_RAW_ADDR
    ADC_RAW_ADDR                           = (0x03, 0x000000FF,  0)  # ADC_RAW_ADDR

    # dsADC_MCFG_B_MCFG_A
    CFG_DSMODULATOR_A                      = (0x04, 0x00000003,  0)  # DSADC_MCFG_B_MCFG_A
    MCLK_POLARITY_A                        = (0x04, 0x00000004,  2)  # DSADC_MCFG_B_MCFG_A
    MDAT_POLARITY_A                        = (0x04, 0x00000008,  3)  # DSADC_MCFG_B_MCFG_A
    SEL_NCLK_MCLK_I_A                      = (0x04, 0x00000010,  4)  # DSADC_MCFG_B_MCFG_A
    BLANKING_A                             = (0x04, 0x0000FF00,  8)  # DSADC_MCFG_B_MCFG_A
    CFG_DSMODULATOR_B                      = (0x04, 0x00030000, 16)  # DSADC_MCFG_B_MCFG_A
    MCLK_POLARITY_B                        = (0x04, 0x00040000, 18)  # DSADC_MCFG_B_MCFG_A
    MDAT_POLARITY_B                        = (0x04, 0x00080000, 19)  # DSADC_MCFG_B_MCFG_A
    SEL_NCLK_MCLK_I_B                      = (0x04, 0x00100000, 20)  # DSADC_MCFG_B_MCFG_A
    BLANKING_B                             = (0x04, 0xFF000000, 24)  # DSADC_MCFG_B_MCFG_A

    # dsADC_MCLK_A
    DSADC_MCLK_A                           = (0x05, 0xFFFFFFFF,  0)  # DSADC_MCLK_A

    # dsADC_MCLK_B
    DSADC_MCLK_B                           = (0x06, 0xFFFFFFFF,  0)  # DSADC_MCLK_B

    # dsADC_MDEC_B_MDEC_A
    DSADC_MDEC_A                           = (0x07, 0x0000FFFF,  0)  # DSADC_MDEC_B_MDEC_A
    DSADC_MDEC_B                           = (0x07, 0xFFFF0000, 16)  # DSADC_MDEC_B_MDEC_A

    # ADC_I1_SCALE_OFFSET
    ADC_I1_OFFSET                          = (0x08, 0x0000FFFF,  0)  # ADC_I1_SCALE_OFFSET
    ADC_I1_SCALE                           = (0x08, 0xFFFF0000, 16)  # ADC_I1_SCALE_OFFSET

    # ADC_I0_SCALE_OFFSET
    ADC_I0_OFFSET                          = (0x09, 0x0000FFFF,  0)  # ADC_I0_SCALE_OFFSET
    ADC_I0_SCALE                           = (0x09, 0xFFFF0000, 16)  # ADC_I0_SCALE_OFFSET

    # ADC_I_SELECT
    ADC_I0_SELECT                          = (0x0a, 0x000000FF,  0)  # ADC_I_SELECT
    ADC_I1_SELECT                          = (0x0a, 0x0000FF00,  8)  # ADC_I_SELECT
    ADC_I_UX_SELECT                        = (0x0a, 0x03000000, 24)  # ADC_I_SELECT
    ADC_I_V_SELECT                         = (0x0a, 0x0C000000, 26)  # ADC_I_SELECT
    ADC_I_WY_SELECT                        = (0x0a, 0x30000000, 28)  # ADC_I_SELECT

    # ADC_I1_I0_EXT
    ADC_I0_EXT                             = (0x0b, 0x0000FFFF,  0)  # ADC_I1_I0_EXT
    ADC_I1_EXT                             = (0x0b, 0xFFFF0000, 16)  # ADC_I1_I0_EXT

    # DS_ANALOG_INPUT_STAGE_CFG
    ADC_I0                                 = (0x0c, 0x0000000F,  0)  # DS_ANALOG_INPUT_STAGE_CFG
    ADC_I1                                 = (0x0c, 0x000000F0,  4)  # DS_ANALOG_INPUT_STAGE_CFG
    ADC_VM                                 = (0x0c, 0x00000F00,  8)  # DS_ANALOG_INPUT_STAGE_CFG
    ADC_AGPI_A                             = (0x0c, 0x0000F000, 12)  # DS_ANALOG_INPUT_STAGE_CFG
    ADC_AGPI_B                             = (0x0c, 0x000F0000, 16)  # DS_ANALOG_INPUT_STAGE_CFG
    ADC_AENC_UX                            = (0x0c, 0x00F00000, 20)  # DS_ANALOG_INPUT_STAGE_CFG
    ADC_AENC_VN                            = (0x0c, 0x0F000000, 24)  # DS_ANALOG_INPUT_STAGE_CFG
    ADC_AENC_WY                            = (0x0c, 0xF0000000, 28)  # DS_ANALOG_INPUT_STAGE_CFG

    # AENC_0_SCALE_OFFSET
    AENC_0_OFFSET                          = (0x0d, 0x0000FFFF,  0)  # AENC_0_SCALE_OFFSET
    AENC_0_SCALE                           = (0x0d, 0xFFFF0000, 16)  # AENC_0_SCALE_OFFSET

    # AENC_1_SCALE_OFFSET
    AENC_1_OFFSET                          = (0x0e, 0x0000FFFF,  0)  # AENC_1_SCALE_OFFSET
    AENC_1_SCALE                           = (0x0e, 0xFFFF0000, 16)  # AENC_1_SCALE_OFFSET

    # AENC_2_SCALE_OFFSET
    AENC_2_OFFSET                          = (0x0f, 0x0000FFFF,  0)  # AENC_2_SCALE_OFFSET
    AENC_2_SCALE                           = (0x0f, 0xFFFF0000, 16)  # AENC_2_SCALE_OFFSET

    # AENC_SELECT
    AENC_0_SELECT                          = (0x11, 0x000000FF,  0)  # AENC_SELECT
    AENC_1_SELECT                          = (0x11, 0x0000FF00,  8)  # AENC_SELECT
    AENC_2_SELECT                          = (0x11, 0x00FF0000, 16)  # AENC_SELECT

    # ADC_IWY_IUX
    ADC_IUX                                = (0x12, 0x0000FFFF,  0)  # ADC_IWY_IUX
    ADC_IWY                                = (0x12, 0xFFFF0000, 16)  # ADC_IWY_IUX

    # ADC_IV
    ADC_IV                                 = (0x13, 0x0000FFFF,  0)  # ADC_IV

    # AENC_WY_UX
    AENC_UX                                = (0x15, 0x0000FFFF,  0)  # AENC_WY_UX
    AENC_WY                                = (0x15, 0xFFFF0000, 16)  # AENC_WY_UX

    # AENC_VN
    AENC_VN                                = (0x16, 0x0000FFFF,  0)  # AENC_VN

    # PWM_POLARITIES
    PWM_POLARITIES_LOW_SIDE                = (0x17, 0x00000001,  0)  # PWM_POLARITIES
    PWM_POLARITIES_HIGH_SIDE               = (0x17, 0x00000002,  1)  # PWM_POLARITIES

    # PWM_MAXCNT
    PWM_MAXCNT                             = (0x18, 0x0000FFFF,  0)  # PWM_MAXCNT

    # PWM_BBM_H_BBM_L
    PWM_BBM_L                              = (0x19, 0x000000FF,  0)  # PWM_BBM_H_BBM_L
    PWM_BBM_H                              = (0x19, 0x0000FF00,  8)  # PWM_BBM_H_BBM_L

    # PWM_SV_CHOP
    PWM_CHOP                               = (0x1a, 0x000000FF,  0)  # PWM_SV_CHOP
    PWM_SV                                 = (0x1a, 0x00000100,  8)  # PWM_SV_CHOP

    # MOTOR_TYPE_N_POLE_PAIRS
    N_POLE_PAIRS                           = (0x1b, 0x0000FFFF,  0)  # MOTOR_TYPE_N_POLE_PAIRS
    MOTOR_TYPE                             = (0x1b, 0x00FF0000, 16)  # MOTOR_TYPE_N_POLE_PAIRS

    # PHI_E_EXT
    PHI_E_EXT                              = (0x1c, 0x0000FFFF,  0)  # PHI_E_EXT

    # PHI_M_EXT
    PHI_M_EXT                              = (0x1d, 0x0000FFFF,  0)  # PHI_M_EXT

    # POSITION_EXT
    POSITION_EXT                           = (0x1e, 0xFFFFFFFF,  0)  # POSITION_EXT

    # OPENLOOP_MODE
    OPENLOOP_PHI_DIRECTION                 = (0x1f, 0x00001000, 12)  # OPENLOOP_MODE

    # OPENLOOP_ACCELERATION
    OPENLOOP_ACCELERATION                  = (0x20, 0xFFFFFFFF,  0)  # OPENLOOP_ACCELERATION

    # OPENLOOP_VELOCITY_TARGET
    OPENLOOP_VELOCITY_TARGET               = (0x21, 0xFFFFFFFF,  0)  # OPENLOOP_VELOCITY_TARGET

    # OPENLOOP_VELOCITY_ACTUAL
    OPENLOOP_VELOCITY_ACTUAL               = (0x22, 0xFFFFFFFF,  0)  # OPENLOOP_VELOCITY_ACTUAL

    # OPENLOOP_PHI
    OPENLOOP_PHI                           = (0x23, 0x0000FFFF,  0)  # OPENLOOP_PHI

    # UQ_UD_EXT
    UD_EXT                                 = (0x24, 0x0000FFFF,  0)  # UQ_UD_EXT
    UQ_EXT                                 = (0x24, 0xFFFF0000, 16)  # UQ_UD_EXT

    # ABN_DECODER_MODE
    ABN_APOL                               = (0x25, 0x00000001,  0)  # ABN_DECODER_MODE
    ABN_BPOL                               = (0x25, 0x00000002,  1)  # ABN_DECODER_MODE
    ABN_NPOL                               = (0x25, 0x00000004,  2)  # ABN_DECODER_MODE
    ABN_USE_ABN_AS_N                       = (0x25, 0x00000008,  3)  # ABN_DECODER_MODE
    ABN_CLN                                = (0x25, 0x00000100,  8)  # ABN_DECODER_MODE
    ABN_DIRECTION                          = (0x25, 0x00001000, 12)  # ABN_DECODER_MODE

    # ABN_DECODER_PPR
    ABN_DECODER_PPR                        = (0x26, 0x00FFFFFF,  0)  # ABN_DECODER_PPR

    # ABN_DECODER_COUNT
    ABN_DECODER_COUNT                      = (0x27, 0x00FFFFFF,  0)  # ABN_DECODER_COUNT

    # ABN_DECODER_COUNT_N
    ABN_DECODER_COUNT_N                    = (0x28, 0x00FFFFFF,  0)  # ABN_DECODER_COUNT_N

    # ABN_DECODER_PHI_E_PHI_M_OFFSET
    ABN_DECODER_PHI_M_OFFSET               = (0x29, 0x0000FFFF,  0)  # ABN_DECODER_PHI_E_PHI_M_OFFSET
    ABN_DECODER_PHI_E_OFFSET               = (0x29, 0xFFFF0000, 16)  # ABN_DECODER_PHI_E_PHI_M_OFFSET

    # ABN_DECODER_PHI_E_PHI_M
    ABN_DECODER_PHI_M                      = (0x2a, 0x0000FFFF,  0)  # ABN_DECODER_PHI_E_PHI_M
    ABN_DECODER_PHI_E                      = (0x2a, 0xFFFF0000, 16)  # ABN_DECODER_PHI_E_PHI_M

    # ABN_2_DECODER_MODE
    ABN_2_APOL                             = (0x2c, 0x00000001,  0)  # ABN_2_DECODER_MODE
    ABN_2_BPOL                             = (0x2c, 0x00000002,  1)  # ABN_2_DECODER_MODE
    ABN_2_NPOL                             = (0x2c, 0x00000004,  2)  # ABN_2_DECODER_MODE
    ABN_2_USE_ABN_AS_N                     = (0x2c, 0x00000008,  3)  # ABN_2_DECODER_MODE
    ABN_2_CLN                              = (0x2c, 0x00000100,  8)  # ABN_2_DECODER_MODE
    ABN_2_DIRECTION                        = (0x2c, 0x00001000, 12)  # ABN_2_DECODER_MODE

    # ABN_2_DECODER_PPR
    ABN_2_DECODER_PPR                      = (0x2d, 0x00FFFFFF,  0)  # ABN_2_DECODER_PPR

    # ABN_2_DECODER_COUNT
    ABN_2_DECODER_COUNT                    = (0x2e, 0x00FFFFFF,  0)  # ABN_2_DECODER_COUNT

    # ABN_2_DECODER_COUNT_N
    ABN_2_DECODER_COUNT_N                  = (0x2f, 0x00FFFFFF,  0)  # ABN_2_DECODER_COUNT_N

    # ABN_2_DECODER_PHI_M_OFFSET
    ABN_2_DECODER_PHI_M_OFFSET             = (0x30, 0x0000FFFF,  0)  # ABN_2_DECODER_PHI_M_OFFSET

    # ABN_2_DECODER_PHI_M
    ABN_2_DECODER_PHI_M                    = (0x31, 0x0000FFFF,  0)  # ABN_2_DECODER_PHI_M

    # HALL_MODE
    HALL_POLARITY                          = (0x33, 0x00000001,  0)  # HALL_MODE
    HALL_INTERPOLATION                     = (0x33, 0x00000100,  8)  # HALL_MODE
    HALL_DIRECTION                         = (0x33, 0x00001000, 12)  # HALL_MODE
    HALL_HALL_BLANK                        = (0x33, 0x0FFF0000, 16)  # HALL_MODE

    # HALL_POSITION_060_000
    HALL_POSITION_000                      = (0x34, 0x0000FFFF,  0)  # HALL_POSITION_060_000
    HALL_POSITION_060                      = (0x34, 0xFFFF0000, 16)  # HALL_POSITION_060_000

    # HALL_POSITION_180_120
    HALL_POSITION_120                      = (0x35, 0x0000FFFF,  0)  # HALL_POSITION_180_120
    HALL_POSITION_180                      = (0x35, 0xFFFF0000, 16)  # HALL_POSITION_180_120

    # HALL_POSITION_300_240
    HALL_POSITION_240                      = (0x36, 0x0000FFFF,  0)  # HALL_POSITION_300_240
    HALL_POSITION_300                      = (0x36, 0xFFFF0000, 16)  # HALL_POSITION_300_240

    # HALL_PHI_E_PHI_M_OFFSET
    HALL_PHI_M_OFFSET                      = (0x37, 0x0000FFFF,  0)  # HALL_PHI_E_PHI_M_OFFSET
    HALL_PHI_E_OFFSET                      = (0x37, 0xFFFF0000, 16)  # HALL_PHI_E_PHI_M_OFFSET

    # HALL_DPHI_MAX
    HALL_DPHI_MAX                          = (0x38, 0x0000FFFF,  0)  # HALL_DPHI_MAX

    # HALL_PHI_E_INTERPOLATED_PHI_E
    HALL_PHI_E                             = (0x39, 0x0000FFFF,  0)  # HALL_PHI_E_INTERPOLATED_PHI_E
    HALL_PHI_E_INTERPOLATED                = (0x39, 0xFFFF0000, 16)  # HALL_PHI_E_INTERPOLATED_PHI_E

    # HALL_PHI_M
    HALL_PHI_M                             = (0x3a, 0x0000FFFF,  0)  # HALL_PHI_M

    # AENC_DECODER_MODE
    AENC_DECODER_MODE_120DEG_N90DEG        = (0x3b, 0x00000001,  0)  # AENC_DECODER_MODE
    AENC_DECODER_MODE_DECODER_COUNT_DIR    = (0x3b, 0x00001000, 12)  # AENC_DECODER_MODE

    # AENC_DECODER_N_THRESHOLD
    AENC_DECODER_N_THRESHOLD               = (0x3c, 0x0000FFFF,  0)  # AENC_DECODER_N_THRESHOLD
    AENC_DECODER_N_MASK                    = (0x3c, 0xFFFF0000, 16)  # AENC_DECODER_N_THRESHOLD

    # AENC_DECODER_PHI_A_RAW
    AENC_DECODER_PHI_A_RAW                 = (0x3d, 0x0000FFFF,  0)  # AENC_DECODER_PHI_A_RAW

    # AENC_DECODER_PHI_A_OFFSET
    AENC_DECODER_PHI_A_OFFSET              = (0x3e, 0x0000FFFF,  0)  # AENC_DECODER_PHI_A_OFFSET

    # AENC_DECODER_PHI_A
    AENC_DECODER_PHI_A                     = (0x3f, 0x0000FFFF,  0)  # AENC_DECODER_PHI_A

    # AENC_DECODER_PPR
    AENC_DECODER_PPR                       = (0x40, 0x0000FFFF,  0)  # AENC_DECODER_PPR

    # AENC_DECODER_COUNT
    AENC_DECODER_COUNT                     = (0x41, 0xFFFFFFFF,  0)  # AENC_DECODER_COUNT

    # AENC_DECODER_COUNT_N
    AENC_DECODER_COUNT_N                   = (0x42, 0xFFFFFFFF,  0)  # AENC_DECODER_COUNT_N

    # AENC_DECODER_PHI_E_PHI_M_OFFSET
    AENC_DECODER_PHI_M_OFFSET              = (0x45, 0x0000FFFF,  0)  # AENC_DECODER_PHI_E_PHI_M_OFFSET
    AENC_DECODER_PHI_E_OFFSET              = (0x45, 0xFFFF0000, 16)  # AENC_DECODER_PHI_E_PHI_M_OFFSET

    # AENC_DECODER_PHI_E_PHI_M
    AENC_DECODER_PHI_M                     = (0x46, 0x0000FFFF,  0)  # AENC_DECODER_PHI_E_PHI_M
    AENC_DECODER_PHI_E                     = (0x46, 0xFFFF0000, 16)  # AENC_DECODER_PHI_E_PHI_M

    # AENC_DECODER_POSITION
    AENC_DECODER_POSITION                  = (0x47, 0xFFFFFFFF,  0)  # AENC_DECODER_POSITION

    # PIDIN_VELOCITY_TARGET
    PIDIN_VELOCITY_TARGET                  = (0x4b, 0xFFFFFFFF,  0)  # PIDIN_VELOCITY_TARGET

    # PIDIN_POSITION_TARGET
    PIDIN_POSITION_TARGET                  = (0x4c, 0xFFFFFFFF,  0)  # PIDIN_POSITION_TARGET

    # CONFIG_DATA
    BIQUAD_X_A_1                           = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_X_A_2                           = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_X_B_0                           = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_X_B_1                           = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_X_B_2                           = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_X_ENABLE                        = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_V_A_1                           = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_V_A_2                           = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_V_B_0                           = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_V_B_1                           = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_V_B_2                           = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_V_ENABLE                        = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_T_A_1                           = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_T_A_2                           = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_T_B_0                           = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_T_B_1                           = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_T_B_2                           = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_T_ENABLE                        = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_F_A_1                           = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_F_A_2                           = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_F_B_0                           = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_F_B_1                           = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_F_B_2                           = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    BIQUAD_F_ENABLE                        = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    PRBS_AMPLITUDE                         = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    PRBS_DOWN_SAMPLING_RATIO               = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    FEED_FORWARD_VELOCITY_GAIN             = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    FEED_FORWARD_VELICITY_FILTER_CONSTANT  = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    FEED_FORWARD_TORQUE_GAIN               = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    FEED_FORWARD_TORGUE_FILTER_CONSTANT    = (0x4d, 0xFFFFFFFF,  0)  # CONFIG_DATA
    VELOCITY_METER_PPTM_MIN_POS_DEV        = (0x4d, 0x0000FFFF,  0)  # CONFIG_DATA
    REF_SWITCH_CONFIG                      = (0x4d, 0x0000FFFF,  0)  # CONFIG_DATA
    ENCODER_INIT_HALL_ENABLE               = (0x4d, 0x00000001,  0)  # CONFIG_DATA
    SINGLE_PIN_IF_CFG                      = (0x4d, 0x000000FF,  0)  # CONFIG_DATA
    SINGLE_PIN_IF_STATUS                   = (0x4d, 0xFFFF0000, 16)  # CONFIG_DATA
    SINGLE_PIN_IF_OFFSET                   = (0x4d, 0x0000FFFF,  0)  # CONFIG_DATA
    SINGLE_PIN_IF_SCALE                    = (0x4d, 0xFFFF0000, 16)  # CONFIG_DATA

    # CONFIG_ADDR
    CONFIG_ADDR                            = (0x4e, 0xFFFFFFFF,  0)  # CONFIG_ADDR

    # VELOCITY_SELECTION
    VELOCITY_SELECTION                     = (0x50, 0x000000FF,  0)  # VELOCITY_SELECTION
    VELOCITY_METER_SELECTION               = (0x50, 0x0000FF00,  8)  # VELOCITY_SELECTION

    # POSITION_SELECTION
    POSITION_SELECTION                     = (0x51, 0x000000FF,  0)  # POSITION_SELECTION

    # PHI_E_SELECTION
    PHI_E_SELECTION                        = (0x52, 0x000000FF,  0)  # PHI_E_SELECTION

    # PHI_E
    PHI_E                                  = (0x53, 0x0000FFFF,  0)  # PHI_E

    # PID_FLUX_P_FLUX_I
    PID_FLUX_I                             = (0x54, 0x0000FFFF,  0)  # PID_FLUX_P_FLUX_I
    PID_FLUX_P                             = (0x54, 0xFFFF0000, 16)  # PID_FLUX_P_FLUX_I

    # PID_TORQUE_P_TORQUE_I
    PID_TORQUE_I                           = (0x56, 0x0000FFFF,  0)  # PID_TORQUE_P_TORQUE_I
    PID_TORQUE_P                           = (0x56, 0xFFFF0000, 16)  # PID_TORQUE_P_TORQUE_I

    # PID_VELOCITY_P_VELOCITY_I
    PID_VELOCITY_I                         = (0x58, 0x0000FFFF,  0)  # PID_VELOCITY_P_VELOCITY_I
    PID_VELOCITY_P                         = (0x58, 0xFFFF0000, 16)  # PID_VELOCITY_P_VELOCITY_I

    # PID_POSITION_P_POSITION_I
    PID_POSITION_I                         = (0x5a, 0x0000FFFF,  0)  # PID_POSITION_P_POSITION_I
    PID_POSITION_P                         = (0x5a, 0xFFFF0000, 16)  # PID_POSITION_P_POSITION_I

    # PID_TORQUE_FLUX_TARGET_DDT_LIMITS
    PID_TORQUE_FLUX_TARGET_DDT_LIMITS      = (0x5c, 0xFFFFFFFF,  0)  # PID_TORQUE_FLUX_TARGET_DDT_LIMITS

    # PIDOUT_UQ_UD_LIMITS
    PIDOUT_UQ_UD_LIMITS                    = (0x5d, 0x0000FFFF,  0)  # PIDOUT_UQ_UD_LIMITS

    # PID_TORQUE_FLUX_LIMITS
    PID_TORQUE_FLUX_LIMITS                 = (0x5e, 0x0000FFFF,  0)  # PID_TORQUE_FLUX_LIMITS

    # PID_ACCELERATION_LIMIT
    PID_ACCELERATION_LIMIT                 = (0x5f, 0xFFFFFFFF,  0)  # PID_ACCELERATION_LIMIT

    # PID_VELOCITY_LIMIT
    PID_VELOCITY_LIMIT                     = (0x60, 0xFFFFFFFF,  0)  # PID_VELOCITY_LIMIT

    # PID_POSITION_LIMIT_LOW
    PID_POSITION_LIMIT_LOW                 = (0x61, 0xFFFFFFFF,  0)  # PID_POSITION_LIMIT_LOW

    # PID_POSITION_LIMIT_HIGH
    PID_POSITION_LIMIT_HIGH                = (0x62, 0xFFFFFFFF,  0)  # PID_POSITION_LIMIT_HIGH

    # MODE_RAMP_MODE_MOTION
    MODE_MOTION                            = (0x63, 0x000000FF,  0)  # MODE_RAMP_MODE_MOTION
    MODE_RAMP                              = (0x63, 0x0000FF00,  8)  # MODE_RAMP_MODE_MOTION
    MODE_FF                                = (0x63, 0x00FF0000, 16)  # MODE_RAMP_MODE_MOTION
    MODE_PID_SMPL                          = (0x63, 0x7F000000, 24)  # MODE_RAMP_MODE_MOTION
    MODE_PID_TYPE                          = (0x63, 0x80000000, 31)  # MODE_RAMP_MODE_MOTION

    # PID_TORQUE_FLUX_TARGET
    PID_FLUX_TARGET                        = (0x64, 0x0000FFFF,  0)  # PID_TORQUE_FLUX_TARGET
    PID_TORQUE_TARGET                      = (0x64, 0xFFFF0000, 16)  # PID_TORQUE_FLUX_TARGET

    # PID_TORQUE_FLUX_OFFSET
    PID_FLUX_OFFSET                        = (0x65, 0x0000FFFF,  0)  # PID_TORQUE_FLUX_OFFSET
    PID_TORQUE_OFFSET                      = (0x65, 0xFFFF0000, 16)  # PID_TORQUE_FLUX_OFFSET

    # PID_VELOCITY_TARGET
    PID_VELOCITY_TARGET                    = (0x66, 0xFFFFFFFF,  0)  # PID_VELOCITY_TARGET

    # PID_VELOCITY_OFFSET
    PID_VELOCITY_OFFSET                    = (0x67, 0xFFFFFFFF,  0)  # PID_VELOCITY_OFFSET

    # PID_POSITION_TARGET
    PID_POSITION_TARGET                    = (0x68, 0xFFFFFFFF,  0)  # PID_POSITION_TARGET

    # PID_TORQUE_FLUX_ACTUAL
    PID_FLUX_ACTUAL                        = (0x69, 0x0000FFFF,  0)  # PID_TORQUE_FLUX_ACTUAL
    PID_TORQUE_ACTUAL                      = (0x69, 0xFFFF0000, 16)  # PID_TORQUE_FLUX_ACTUAL

    # PID_VELOCITY_ACTUAL
    PID_VELOCITY_ACTUAL                    = (0x6a, 0xFFFFFFFF,  0)  # PID_VELOCITY_ACTUAL

    # PID_POSITION_ACTUAL
    PID_POSITION_ACTUAL                    = (0x6b, 0xFFFFFFFF,  0)  # PID_POSITION_ACTUAL

    # PID_ERROR_DATA
    PID_TORQUE_ERROR                       = (0x6c, 0xFFFFFFFF,  0)  # PID_ERROR_DATA
    PID_FLUX_ERROR                         = (0x6c, 0xFFFFFFFF,  0)  # PID_ERROR_DATA
    PID_VELOCITY_ERROR                     = (0x6c, 0xFFFFFFFF,  0)  # PID_ERROR_DATA
    PID_POSITION_ERROR                     = (0x6c, 0xFFFFFFFF,  0)  # PID_ERROR_DATA
    PID_TORQUE_ERROR_SUM                   = (0x6c, 0xFFFFFFFF,  0)  # PID_ERROR_DATA
    PID_FLUX_ERROR_SUM                     = (0x6c, 0xFFFFFFFF,  0)  # PID_ERROR_DATA
    PID_VELOCITY_ERROR_SUM                 = (0x6c, 0xFFFFFFFF,  0)  # PID_ERROR_DATA
    PID_POSITION_ERROR_SUM                 = (0x6c, 0xFFFFFFFF,  0)  # PID_ERROR_DATA

    # PID_ERROR_ADDR
    PID_ERROR_ADDR                         = (0x6d, 0x000000FF,  0)  # PID_ERROR_ADDR

    # INTERIM_DATA
    PIDIN_TARGET_TORQUE                    = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    PIDIN_TARGET_FLUX                      = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    PIDIN_TARGET_VELOCITY                  = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    PIDIN_TARGET_POSITION                  = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    PIDOUT_TARGET_TORQUE                   = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    PIDOUT_TARGET_FLUX                     = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    PIDOUT_TARGET_VELOCITY                 = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    PIDOUT_TARGET_POSITION                 = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    FOC_IUX                                = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    FOC_IWY                                = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    FOC_IV                                 = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    FOC_IA                                 = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    FOC_IB                                 = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    FOC_ID                                 = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    FOC_IQ                                 = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    FOC_UD                                 = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    FOC_UQ                                 = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    FOC_UD_LIMITED                         = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    FOC_UQ_LIMITED                         = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    FOC_UA                                 = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    FOC_UB                                 = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    FOC_UUX                                = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    FOC_UWY                                = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    FOC_UV                                 = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    PWM_UX                                 = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    PWM_WY                                 = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    PWM_V                                  = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    ADC_I_0                                = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    ADC_I_1                                = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    PID_FLUX_ACTUAL_DIV256                 = (0x6e, 0x000000FF,  0)  # INTERIM_DATA
    PID_TORQUE_ACTUAL_DIV256               = (0x6e, 0x0000FF00,  8)  # INTERIM_DATA
    PID_FLUX_TARGET_DIV256                 = (0x6e, 0x00FF0000, 16)  # INTERIM_DATA
    PID_TORQUE_TARGET_DIV256               = (0x6e, 0xFF000000, 24)  # INTERIM_DATA
    PID_TORQUE_ACTUAL_INTERIM              = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    PID_TORQUE_TARGET_INTERIM              = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    PID_FLUX_ACTUAL_INTERIM                = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    PID_FLUX_TARGET_INTERIM                = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    PID_VELOCITY_ACTUAL_DIV256             = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    PID_VELOCITY_TARGET_DIV256             = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    PID_VELOCITY_ACTUAL_LSB                = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    PID_VELOCITY_TARGET_LSB                = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    PID_POSITION_ACTUAL_DIV256             = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    PID_POSITION_TARGET_DIV256             = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    PID_POSITION_ACTUAL_LSB                = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    PID_POSITION_TARGET_LSB                = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    FF_VELOCITY                            = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    FF_TORQUE                              = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    ACTUAL_VELOCITY_PPTM                   = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    REF_SWITCH_STATUS                      = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    HOME_POSITION                          = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    LEFT_POSITION                          = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    RIGHT_POSITION                         = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    ENC_INIT_HALL_STATUS                   = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    ENC_INIT_HALL_PHI_E_ABN_OFFSET         = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    ENC_INIT_HALL_PHI_E_AENC_OFFSET        = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    ENC_INIT_HALL_PHI_A_AENC_OFFSET        = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    ENC_INIT_MINI_MOVE_STATUS              = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    ENC_INIT_MINI_MOVE_U_D                 = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    ENC_INIT_MINI_MOVE_PHI_E_OFFSET        = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    ENC_INIT_MINI_MOVE_PHI_E               = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    SINGLE_PIN_IF_TARGET_TORQUE            = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    SINGLE_PIN_IF_PWM_DUTY_CYCLE           = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    SINGLE_PIN_IF_TARGET_VELOCITY          = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    SINGLE_PIN_IF_TARGET_POSITION          = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    DEBUG_VALUE_0                          = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    DEBUG_VALUE_1                          = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    DEBUG_VALUE_2                          = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    DEBUG_VALUE_3                          = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    DEBUG_VALUE_4                          = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    DEBUG_VALUE_5                          = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    DEBUG_VALUE_6                          = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    DEBUG_VALUE_7                          = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    DEBUG_VALUE_8                          = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    DEBUG_VALUE_9                          = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    DEBUG_VALUE_10                         = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    DEBUG_VALUE_11                         = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    DEBUG_VALUE_12                         = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    DEBUG_VALUE_13                         = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    DEBUG_VALUE_14                         = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    DEBUG_VALUE_15                         = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    DEBUG_VALUE_16                         = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    DEBUG_VALUE_17                         = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    DEBUG_VALUE_18                         = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    DEBUG_VALUE_19                         = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    CONFIG_REG_0                           = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    CONFIG_REG_1                           = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    CTRL_PARAM_0                           = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    CTRL_PARAM_1                           = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    CTRL_PARAM_2                           = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    CTRL_PARAM_3                           = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    STATUS_REG_0                           = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    STATUS_REG_1                           = (0x6e, 0xFFFFFFFF,  0)  # INTERIM_DATA
    STATUS_PARAM_0                         = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    STATUS_PARAM_1                         = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA
    STATUS_PARAM_2                         = (0x6e, 0x0000FFFF,  0)  # INTERIM_DATA
    STATUS_PARAM_3                         = (0x6e, 0xFFFF0000, 16)  # INTERIM_DATA

    # INTERIM_ADDR
    INTERIM_ADDR                           = (0x6f, 0x000000FF,  0)  # INTERIM_ADDR

    # WATCHDOG_CFG
    WATCHDOG_CFG                           = (0x74, 0x00000003,  0)  # WATCHDOG_CFG

    # ADC_VM_LIMITS
    ADC_VM_LIMIT_LOW                       = (0x75, 0x0000FFFF,  0)  # ADC_VM_LIMITS
    ADC_VM_LIMIT_HIGH                      = (0x75, 0xFFFF0000, 16)  # ADC_VM_LIMITS

    # TMC4671_INPUTS_RAW
    A_OF_ABN_RAW                           = (0x76, 0x00000001,  0)  # TMC4671_INPUTS_RAW
    B_OF_ABN_RAW                           = (0x76, 0x00000002,  1)  # TMC4671_INPUTS_RAW
    N_OF_ABN_RAW                           = (0x76, 0x00000004,  2)  # TMC4671_INPUTS_RAW
    A_OF_ABN_2_RAW                         = (0x76, 0x00000010,  4)  # TMC4671_INPUTS_RAW
    B_OF_ABN_2_RAW                         = (0x76, 0x00000020,  5)  # TMC4671_INPUTS_RAW
    N_OF_ABN_2_RAW                         = (0x76, 0x00000040,  6)  # TMC4671_INPUTS_RAW
    HALL_UX_OF_HALL_RAW                    = (0x76, 0x00000100,  8)  # TMC4671_INPUTS_RAW
    HALL_V_OF_HALL_RAW                     = (0x76, 0x00000200,  9)  # TMC4671_INPUTS_RAW
    HALL_WY_OF_HALL_RAW                    = (0x76, 0x00000400, 10)  # TMC4671_INPUTS_RAW
    REF_SW_R_RAW                           = (0x76, 0x00001000, 12)  # TMC4671_INPUTS_RAW
    REF_SW_H_RAW                           = (0x76, 0x00002000, 13)  # TMC4671_INPUTS_RAW
    REF_SW_L_RAW                           = (0x76, 0x00004000, 14)  # TMC4671_INPUTS_RAW
    ENABLE_IN_RAW                          = (0x76, 0x00008000, 15)  # TMC4671_INPUTS_RAW
    STP_OF_DIRSTP_RAW                      = (0x76, 0x00010000, 16)  # TMC4671_INPUTS_RAW
    DIR_OF_DIRSTP_RAW                      = (0x76, 0x00020000, 17)  # TMC4671_INPUTS_RAW
    PWM_IN_RAW                             = (0x76, 0x00040000, 18)  # TMC4671_INPUTS_RAW
    HALL_UX_FILT                           = (0x76, 0x00100000, 20)  # TMC4671_INPUTS_RAW
    HALL_V_FILT                            = (0x76, 0x00200000, 21)  # TMC4671_INPUTS_RAW
    HALL_WY_FILT                           = (0x76, 0x00400000, 22)  # TMC4671_INPUTS_RAW
    PWM_IDLE_L_RAW                         = (0x76, 0x10000000, 28)  # TMC4671_INPUTS_RAW
    PWM_IDLE_H_RAW                         = (0x76, 0x20000000, 29)  # TMC4671_INPUTS_RAW

    # TMC4671_OUTPUTS_RAW
    TMC4671_OUTPUTS_RAW_PWM_UX1_L          = (0x77, 0x00000001,  0)  # TMC4671_OUTPUTS_RAW
    TMC4671_OUTPUTS_RAW_PWM_UX1_H          = (0x77, 0x00000002,  1)  # TMC4671_OUTPUTS_RAW
    TMC4671_OUTPUTS_RAW_PWM_VX2_L          = (0x77, 0x00000004,  2)  # TMC4671_OUTPUTS_RAW
    TMC4671_OUTPUTS_RAW_PWM_VX2_H          = (0x77, 0x00000008,  3)  # TMC4671_OUTPUTS_RAW
    TMC4671_OUTPUTS_RAW_PWM_WY1_L          = (0x77, 0x00000010,  4)  # TMC4671_OUTPUTS_RAW
    TMC4671_OUTPUTS_RAW_PWM_WY1_H          = (0x77, 0x00000020,  5)  # TMC4671_OUTPUTS_RAW
    TMC4671_OUTPUTS_RAW_PWM_Y2_L           = (0x77, 0x00000040,  6)  # TMC4671_OUTPUTS_RAW
    TMC4671_OUTPUTS_RAW_PWM_Y2_H           = (0x77, 0x00000080,  7)  # TMC4671_OUTPUTS_RAW

    # STEP_WIDTH
    STEP_WIDTH                             = (0x78, 0xFFFFFFFF,  0)  # STEP_WIDTH

    # UART_BPS
    UART_BPS                               = (0x79, 0x00FFFFFF,  0)  # UART_BPS

    # UART_ADDRS
    ADDR_A                                 = (0x7A, 0x000000FF,  0)  # UART_ADDRS
    ADDR_B                                 = (0x7A, 0x0000FF00,  8)  # UART_ADDRS
    ADDR_C                                 = (0x7A, 0x00FF0000, 16)  # UART_ADDRS
    ADDR_D                                 = (0x7A, 0xFF000000, 24)  # UART_ADDRS

    # GPIO_dsADCI_CONFIG
    GPIO_DSADCI_CONFIG_0                   = (0x7B, 0x00000001,  0)  # GPIO_DSADCI_CONFIG
    GPIO_DSADCI_CONFIG_1                   = (0x7B, 0x00000002,  1)  # GPIO_DSADCI_CONFIG
    GPIO_DSADCI_CONFIG_2                   = (0x7B, 0x00000004,  2)  # GPIO_DSADCI_CONFIG
    GPIO_DSADCI_CONFIG_3                   = (0x7B, 0x00000008,  3)  # GPIO_DSADCI_CONFIG
    GPIO_DSADCI_CONFIG_4                   = (0x7B, 0x00000010,  4)  # GPIO_DSADCI_CONFIG
    GPIO_DSADCI_CONFIG_5                   = (0x7B, 0x00000020,  5)  # GPIO_DSADCI_CONFIG
    GPIO_DSADCI_CONFIG_6                   = (0x7B, 0x00000040,  6)  # GPIO_DSADCI_CONFIG
    GPO                                    = (0x7B, 0x00FF0000, 16)  # GPIO_DSADCI_CONFIG
    GPI                                    = (0x7B, 0xFF000000, 24)  # GPIO_DSADCI_CONFIG

    # STATUS_FLAGS
    STATUS_FLAG_PID_X_TARGET_LIMIT         = (0x7c, 0x00000001,  0)  # STATUS_FLAGS
    STATUS_FLAG_PID_X_TARGET_DDT_LIMIT     = (0x7c, 0x00000002,  1)  # STATUS_FLAGS
    STATUS_FLAG_PID_X_ERRSUM_LIMIT         = (0x7c, 0x00000004,  2)  # STATUS_FLAGS
    STATUS_FLAG_PID_X_OUTPUT_LIMIT         = (0x7c, 0x00000008,  3)  # STATUS_FLAGS
    STATUS_FLAG_PID_V_TARGET_LIMIT         = (0x7c, 0x00000010,  4)  # STATUS_FLAGS
    STATUS_FLAG_PID_V_TARGET_DDT_LIMIT     = (0x7c, 0x00000020,  5)  # STATUS_FLAGS
    STATUS_FLAG_PID_V_ERRSUM_LIMIT         = (0x7c, 0x00000040,  6)  # STATUS_FLAGS
    STATUS_FLAG_PID_V_OUTPUT_LIMIT         = (0x7c, 0x00000080,  7)  # STATUS_FLAGS
    STATUS_FLAG_PID_ID_TARGET_LIMIT        = (0x7c, 0x00000100,  8)  # STATUS_FLAGS
    STATUS_FLAG_PID_ID_TARGET_DDT_LIMIT    = (0x7c, 0x00000200,  9)  # STATUS_FLAGS
    STATUS_FLAG_PID_ID_ERRSUM_LIMIT        = (0x7c, 0x00000400, 10)  # STATUS_FLAGS
    STATUS_FLAG_PID_ID_OUTPUT_LIMIT        = (0x7c, 0x00000800, 11)  # STATUS_FLAGS
    STATUS_FLAG_PID_IQ_TARGET_LIMIT        = (0x7c, 0x00001000, 12)  # STATUS_FLAGS
    STATUS_FLAG_PID_IQ_TARGET_DDT_LIMIT    = (0x7c, 0x00002000, 13)  # STATUS_FLAGS
    STATUS_FLAG_PID_IQ_ERRSUM_LIMIT        = (0x7c, 0x00004000, 14)  # STATUS_FLAGS
    STATUS_FLAG_PID_IQ_OUTPUT_LIMIT        = (0x7c, 0x00008000, 15)  # STATUS_FLAGS
    STATUS_FLAG_IPARK_CIRLIM_LIMIT_U_D     = (0x7c, 0x00010000, 16)  # STATUS_FLAGS
    STATUS_FLAG_IPARK_CIRLIM_LIMIT_U_Q     = (0x7c, 0x00020000, 17)  # STATUS_FLAGS
    STATUS_FLAG_IPARK_CIRLIM_LIMIT_U_R     = (0x7c, 0x00040000, 18)  # STATUS_FLAGS
    STATUS_FLAG_NOT_PLL_LOCKED             = (0x7c, 0x00080000, 19)  # STATUS_FLAGS
    STATUS_FLAG_REF_SW_R                   = (0x7c, 0x00100000, 20)  # STATUS_FLAGS
    STATUS_FLAG_REF_SW_H                   = (0x7c, 0x00200000, 21)  # STATUS_FLAGS
    STATUS_FLAG_REF_SW_L                   = (0x7c, 0x00400000, 22)  # STATUS_FLAGS
    STATUS_FLAG___                         = (0x7c, 0x00800000, 23)  # STATUS_FLAGS
    STATUS_FLAG_PWM_MIN                    = (0x7c, 0x01000000, 24)  # STATUS_FLAGS
    STATUS_FLAG_PWM_MAX                    = (0x7c, 0x02000000, 25)  # STATUS_FLAGS
    STATUS_FLAG_ADC_I_CLIPPED              = (0x7c, 0x04000000, 26)  # STATUS_FLAGS
    STATUS_FLAG_AENC_CLIPPED               = (0x7c, 0x08000000, 27)  # STATUS_FLAGS
    STATUS_FLAG_ENC_N                      = (0x7c, 0x10000000, 28)  # STATUS_FLAGS
    STATUS_FLAG_ENC_2_N                    = (0x7c, 0x20000000, 29)  # STATUS_FLAGS
    STATUS_FLAG_AENC_N                     = (0x7c, 0x40000000, 30)  # STATUS_FLAGS
    STATUS_FLAG_WD_ERROR                   = (0x7c, 0x80000000, 31)  # STATUS_FLAGS

    # STATUS_MASK
    WARNING_MASK                           = (0x7d, 0xFFFFFFFF,  0)  # STATUS_MASK
