'''
Created on 02.01.2019

@author: ed
'''

class TMC4671_register:

    " ===== TMC4671 register set ===== "

    CHIPINFO_DATA                       = 0x00
    CHIPINFO_ADDR                       = 0x01

    ADC_RAW_DATA                        = 0x02
    ADC_RAW_ADDR                        = 0x03

    dsADC_MCFG_B_MCFG_A                 = 0x04
    dsADC_MCLK_A                        = 0x05
    dsADC_MCLK_B                        = 0x06
    dsADC_MDEC_B_MDEC_A                 = 0x07

    ADC_I1_SCALE_OFFSET                 = 0x08
    ADC_I0_SCALE_OFFSET                 = 0x09
    ADC_I_SELECT                        = 0x0A
    ADC_I1_I0_EXT                       = 0x0B

    DS_ANALOG_INPUT_STAGE_CFG           = 0x0C

    AENC_0_SCALE_OFFSET                 = 0x0D
    AENC_1_SCALE_OFFSET                 = 0x0E
    AENC_2_SCALE_OFFSET                 = 0x0F
    AENC_SELECT                         = 0x11

    ADC_IWY_IUX                         = 0x12
    ADC_IV                              = 0x13
    AENC_WY_UX                          = 0x15
    AENC_VN                             = 0x16

    PWM_POLARITIES                      = 0x17
    PWM_MAXCNT                          = 0x18
    PWM_BBM_H_BBM_L                     = 0x19
    PWM_SV_CHOP                         = 0x1A
    MOTOR_TYPE_N_POLE_PAIRS             = 0x1B

    PHI_E_EXT                           = 0x1C
    PHI_M_EXT                           = 0x1D
    POSITION_EXT                        = 0x1E
    OPENLOOP_MODE                       = 0x1F
    OPENLOOP_ACCELERATION               = 0x20
    OPENLOOP_VELOCITY_TARGET            = 0x21
    OPENLOOP_VELOCITY_ACTUAL            = 0x22
    OPENLOOP_PHI                        = 0x23
    UQ_UD_EXT                           = 0x24

    ABN_DECODER_MODE                    = 0x25
    ABN_DECODER_PPR                     = 0x26
    ABN_DECODER_COUNT                   = 0x27
    ABN_DECODER_COUNT_N                 = 0x28
    ABN_DECODER_PHI_E_PHI_M_OFFSET      = 0x29
    ABN_DECODER_PHI_E_PHI_M             = 0x2A

    ABN_2_DECODER_MODE                  = 0x2C
    ABN_2_DECODER_PPR                   = 0x2D
    ABN_2_DECODER_COUNT                 = 0x2E
    ABN_2_DECODER_COUNT_N               = 0x2F
    ABN_2_DECODER_PHI_M_OFFSET          = 0x30
    ABN_2_DECODER_PHI_M                 = 0x31

    HALL_MODE                           = 0x33
    HALL_POSITION_060_000               = 0x34
    HALL_POSITION_180_120               = 0x35
    HALL_POSITION_300_240               = 0x36
    HALL_PHI_E_PHI_M_OFFSET             = 0x37
    HALL_DPHI_MAX                       = 0x38
    HALL_PHI_E_INTERPOLATED_PHI_E       = 0x39
    HALL_PHI_M                          = 0x3A

    AENC_DECODER_MODE                   = 0x3B
    AENC_DECODER_N_MASK_N_THRESHOLD     = 0x3C
    AENC_DECODER_PHI_A_RAW              = 0x3D
    AENC_DECODER_PHI_A_OFFSET           = 0x3E
    AENC_DECODER_PHI_A                  = 0x3F

    AENC_DECODER_PPR                    = 0x40
    AENC_DECODER_COUNT                  = 0x41
    AENC_DECODER_COUNT_N                = 0x42
    AENC_DECODER_PHI_E_PHI_M_OFFSET     = 0x45
    AENC_DECODER_PHI_E_PHI_M            = 0x46
    AENC_DECODER_POSITION               = 0x47

    PIDIN_TORQUE_TARGET_FLUX_TARGET     = 0x4A
    PIDIN_VELOCITY_TARGET               = 0x4B
    PIDIN_POSITION_TARGET               = 0x4C

    CONFIG_DATA                         = 0x4D
    CONFIG_ADDR                         = 0x4E

    VELOCITY_SELECTION                  = 0x50
    POSITION_SELECTION                  = 0x51
    PHI_E_SELECTION                     = 0x52
    PHI_E                               = 0x53

    PID_FLUX_P_FLUX_I                   = 0x54
    PID_TORQUE_P_TORQUE_I               = 0x56
    PID_VELOCITY_P_VELOCITY_I           = 0x58
    PID_POSITION_P_POSITION_I           = 0x5A
    PID_TORQUE_FLUX_TARGET_DDT_LIMITS   = 0x5C
    PIDOUT_UQ_UD_LIMITS                 = 0x5D
    PID_TORQUE_FLUX_LIMITS              = 0x5E
    PID_ACCELERATION_LIMIT              = 0x5F
    PID_VELOCITY_LIMIT                  = 0x60
    PID_POSITION_LIMIT_LOW              = 0x61
    POSITION_LIMIT_HIGH                 = 0x62

    MODE_RAMP_MODE_MOTION               = 0x63
    PID_TORQUE_FLUX_TARGET              = 0x64
    PID_TORQUE_FLUX_OFFSET              = 0x65
    PID_VELOCITY_TARGET                 = 0x66
    PID_VELOCITY_OFFSET                 = 0x67
    PID_POSITION_TARGET                 = 0x68

    PID_TORQUE_FLUX_ACTUAL              = 0x69
    PID_VELOCITY_ACTUAL                 = 0x6A
    PID_POSITION_ACTUAL                 = 0x6B

    PID_ERROR_DATA                      = 0x6C
    PID_ERROR_ADDR                      = 0x6D
    INTERIM_DATA                        = 0x6E
    INTERIM_ADDR                        = 0x6F

    WATCHDOG_CFG                        = 0x74
    ADC_VM_LIMITS                       = 0x75
    INPUTS_RAW                          = 0x76
    OUTPUTS_RAW                         = 0x77

    STEP_WIDTH                          = 0x78

    UART_BPS                            = 0x79
    UART_ADDRS                          = 0x7A

    GPIO_dsADCI_CONFIG                  = 0x7B

    STATUS_FLAGS                        = 0x7C
    STATUS_MASK                         = 0x7D

    " motion modes "
    MOTION_MODE_STOPPED     = 0
    MOTION_MODE_TORQUE      = 1
    MOTION_MODE_VELOCITY    = 2
    MOTION_MODE_POSITION    = 3
    MOTION_MODE_UQ_UD_EXT   = 8

    " phi_e selections "
    PHI_E_EXTERNAL      = 1
    PHI_E_OPEN_LOOP     = 2
    PHI_E_ABN           = 3
    PHI_E_HALL          = 5
    PHI_E_AENC          = 6
    PHI_A_AENC          = 7

    " velocity/position selection "
    VELOCITY_PHI_E_SELECTION    = 0
    VELOCITY_PHI_E_EXT          = 1
    VELOCITY_PHI_E_OPENLOOP     = 2
    VELOCITY_PHI_E_ABN          = 3

    VELOCITY_PHI_E_HAL          = 5
    VELOCITY_PHI_E_AENC         = 6
    VELOCITY_PHI_A_AENC         = 7

    VELOCITY_PHI_M_ABN          = 9
    VELOCITY_PHI_M_ABN_2        = 10
    VELOCITY_PHI_M_AENC         = 11
    VELOCITY_PHI_M_HAL          = 12
