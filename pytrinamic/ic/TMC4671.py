import struct
from ..ic.tmc_ic import TMCIc
from ..helpers import TMC_helpers

DATAGRAM_FORMAT = ">BI"
DATAGRAM_LENGTH = 5


class TMC4671(TMCIc):
    """
    The TMC4671 is a fully integrated servo controller, providing Field Oriented Control for BLDC/PMSM
    and 2-phase Stepper motors as well as DC motor support.
    """
    def __init__(self, connection=None):
        super().__init__("TMC4671", self.__doc__)
        self._connection = connection

    # Only used for direct UART access without EvalSystem
    def write_register(self, register_address, value):
        datagram = struct.pack(DATAGRAM_FORMAT, register_address | 0x80, value & 0xFFFFFFFF)
        self._connection.send_datagram(datagram, DATAGRAM_LENGTH)

    # Only used for direct UART access without EvalSystem
    def read_register(self, register_address, signed=False):
        datagram = struct.pack(DATAGRAM_FORMAT, register_address, 0)
        reply = self._connection.send_datagram(datagram, DATAGRAM_LENGTH)
        values = struct.unpack(DATAGRAM_FORMAT, reply)
        value = values[1]
        return TMC_helpers.to_signed_32(value) if signed else value

    def write_register_field(self, field, value):
        return self.write_register(field[0], TMC_helpers.field_set(self.read_register(field[0]),
                                   field[1], field[2], value))

    def read_register_field(self, field):
        return TMC_helpers.field_get(self.read_register(field[0]), field[1], field[2])

    class REG:
        """
        Define all register of the TMC4671.
        """
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

    class FIELD:
        """
        Defines all register bitfields of the TMC4671.

        Each field is defined as a tuple consisting of (address, mask, shift).

        The name of the register is written as a comment behind each tuple. This is
        intended for IDE users viewing the definition of a field by hovering over
        it. This allows the user to see the corresponding register name of a field
        without opening this file and searching for the definition.
        """

        # CHIPINFO_DATA
        SI_TYPE                                = (0x00, 0xFFFFFFFF,  0)
        SI_VERSION                             = (0x00, 0xFFFFFFFF,  0)
        SI_DATE                                = (0x00, 0xFFFFFFFF,  0)
        SI_TIME                                = (0x00, 0xFFFFFFFF,  0)
        SI_VARIANT                             = (0x00, 0xFFFFFFFF,  0)
        SI_BUILD                               = (0x00, 0xFFFFFFFF,  0)

        # CHIPINFO_ADDR
        CHIP_INFO_ADDRESS                      = (0x01, 0x000000FF,  0)

        # ADC_RAW_DATA
        ADC_I0_RAW                             = (0x02, 0x0000FFFF,  0)
        ADC_I1_RAW                             = (0x02, 0xFFFF0000, 16)
        ADC_VM_RAW                             = (0x02, 0x0000FFFF,  0)
        ADC_AGPI_A_RAW                         = (0x02, 0xFFFF0000, 16)
        ADC_AGPI_B_RAW                         = (0x02, 0x0000FFFF,  0)
        ADC_AENC_UX_RAW                        = (0x02, 0xFFFF0000, 16)
        ADC_AENC_VN_RAW                        = (0x02, 0x0000FFFF,  0)
        ADC_AENC_WY_RAW                        = (0x02, 0xFFFF0000, 16)

        # ADC_RAW_ADDR
        ADC_RAW_ADDR                           = (0x03, 0x000000FF,  0)

        # dsADC_MCFG_B_MCFG_A
        CFG_DSMODULATOR_A                      = (0x04, 0x00000003,  0)
        MCLK_POLARITY_A                        = (0x04, 0x00000004,  2)
        MDAT_POLARITY_A                        = (0x04, 0x00000008,  3)
        SEL_NCLK_MCLK_I_A                      = (0x04, 0x00000010,  4)
        BLANKING_A                             = (0x04, 0x0000FF00,  8)
        CFG_DSMODULATOR_B                      = (0x04, 0x00030000, 16)
        MCLK_POLARITY_B                        = (0x04, 0x00040000, 18)
        MDAT_POLARITY_B                        = (0x04, 0x00080000, 19)
        SEL_NCLK_MCLK_I_B                      = (0x04, 0x00100000, 20)
        BLANKING_B                             = (0x04, 0xFF000000, 24)

        # dsADC_MCLK_A
        DSADC_MCLK_A                           = (0x05, 0xFFFFFFFF,  0)

        # dsADC_MCLK_B
        DSADC_MCLK_B                           = (0x06, 0xFFFFFFFF,  0)

        # dsADC_MDEC_B_MDEC_A
        DSADC_MDEC_A                           = (0x07, 0x0000FFFF,  0)
        DSADC_MDEC_B                           = (0x07, 0xFFFF0000, 16)

        # ADC_I1_SCALE_OFFSET
        ADC_I1_OFFSET                          = (0x08, 0x0000FFFF,  0)
        ADC_I1_SCALE                           = (0x08, 0xFFFF0000, 16)

        # ADC_I0_SCALE_OFFSET
        ADC_I0_OFFSET                          = (0x09, 0x0000FFFF,  0)
        ADC_I0_SCALE                           = (0x09, 0xFFFF0000, 16)

        # ADC_I_SELECT
        ADC_I0_SELECT                          = (0x0a, 0x000000FF,  0)
        ADC_I1_SELECT                          = (0x0a, 0x0000FF00,  8)
        ADC_I_UX_SELECT                        = (0x0a, 0x03000000, 24)
        ADC_I_V_SELECT                         = (0x0a, 0x0C000000, 26)
        ADC_I_WY_SELECT                        = (0x0a, 0x30000000, 28)

        # ADC_I1_I0_EXT
        ADC_I0_EXT                             = (0x0b, 0x0000FFFF,  0)
        ADC_I1_EXT                             = (0x0b, 0xFFFF0000, 16)

        # DS_ANALOG_INPUT_STAGE_CFG
        ADC_I0                                 = (0x0c, 0x0000000F,  0)
        ADC_I1                                 = (0x0c, 0x000000F0,  4)
        ADC_VM                                 = (0x0c, 0x00000F00,  8)
        ADC_AGPI_A                             = (0x0c, 0x0000F000, 12)
        ADC_AGPI_B                             = (0x0c, 0x000F0000, 16)
        ADC_AENC_UX                            = (0x0c, 0x00F00000, 20)
        ADC_AENC_VN                            = (0x0c, 0x0F000000, 24)
        ADC_AENC_WY                            = (0x0c, 0xF0000000, 28)

        # AENC_0_SCALE_OFFSET
        AENC_0_OFFSET                          = (0x0d, 0x0000FFFF,  0)
        AENC_0_SCALE                           = (0x0d, 0xFFFF0000, 16)

        # AENC_1_SCALE_OFFSET
        AENC_1_OFFSET                          = (0x0e, 0x0000FFFF,  0)
        AENC_1_SCALE                           = (0x0e, 0xFFFF0000, 16)

        # AENC_2_SCALE_OFFSET
        AENC_2_OFFSET                          = (0x0f, 0x0000FFFF,  0)
        AENC_2_SCALE                           = (0x0f, 0xFFFF0000, 16)

        # AENC_SELECT
        AENC_0_SELECT                          = (0x11, 0x000000FF,  0)
        AENC_1_SELECT                          = (0x11, 0x0000FF00,  8)
        AENC_2_SELECT                          = (0x11, 0x00FF0000, 16)

        # ADC_IWY_IUX
        ADC_IUX                                = (0x12, 0x0000FFFF,  0)
        ADC_IWY                                = (0x12, 0xFFFF0000, 16)

        # ADC_IV
        ADC_IV                                 = (0x13, 0x0000FFFF,  0)

        # AENC_WY_UX
        AENC_UX                                = (0x15, 0x0000FFFF,  0)
        AENC_WY                                = (0x15, 0xFFFF0000, 16)

        # AENC_VN
        AENC_VN                                = (0x16, 0x0000FFFF,  0)

        # PWM_POLARITIES
        PWM_POLARITIES_LOW_SIDE                = (0x17, 0x00000001,  0)
        PWM_POLARITIES_HIGH_SIDE               = (0x17, 0x00000002,  1)

        # PWM_MAXCNT
        PWM_MAXCNT                             = (0x18, 0x0000FFFF,  0)

        # PWM_BBM_H_BBM_L
        PWM_BBM_L                              = (0x19, 0x000000FF,  0)
        PWM_BBM_H                              = (0x19, 0x0000FF00,  8)

        # PWM_SV_CHOP
        PWM_CHOP                               = (0x1a, 0x000000FF,  0)
        PWM_SV                                 = (0x1a, 0x00000100,  8)

        # MOTOR_TYPE_N_POLE_PAIRS
        N_POLE_PAIRS                           = (0x1b, 0x0000FFFF,  0)
        MOTOR_TYPE                             = (0x1b, 0x00FF0000, 16)

        # PHI_E_EXT
        PHI_E_EXT                              = (0x1c, 0x0000FFFF,  0)

        # PHI_M_EXT
        PHI_M_EXT                              = (0x1d, 0x0000FFFF,  0)

        # POSITION_EXT
        POSITION_EXT                           = (0x1e, 0xFFFFFFFF,  0)

        # OPENLOOP_MODE
        OPENLOOP_PHI_DIRECTION                 = (0x1f, 0x00001000, 12)

        # OPENLOOP_ACCELERATION
        OPENLOOP_ACCELERATION                  = (0x20, 0xFFFFFFFF,  0)

        # OPENLOOP_VELOCITY_TARGET
        OPENLOOP_VELOCITY_TARGET               = (0x21, 0xFFFFFFFF,  0)

        # OPENLOOP_VELOCITY_ACTUAL
        OPENLOOP_VELOCITY_ACTUAL               = (0x22, 0xFFFFFFFF,  0)

        # OPENLOOP_PHI
        OPENLOOP_PHI                           = (0x23, 0x0000FFFF,  0)

        # UQ_UD_EXT
        UD_EXT                                 = (0x24, 0x0000FFFF,  0)
        UQ_EXT                                 = (0x24, 0xFFFF0000, 16)

        # ABN_DECODER_MODE
        ABN_APOL                               = (0x25, 0x00000001,  0)
        ABN_BPOL                               = (0x25, 0x00000002,  1)
        ABN_NPOL                               = (0x25, 0x00000004,  2)
        ABN_USE_ABN_AS_N                       = (0x25, 0x00000008,  3)
        ABN_CLN                                = (0x25, 0x00000100,  8)
        ABN_DIRECTION                          = (0x25, 0x00001000, 12)

        # ABN_DECODER_PPR
        ABN_DECODER_PPR                        = (0x26, 0x00FFFFFF,  0)

        # ABN_DECODER_COUNT
        ABN_DECODER_COUNT                      = (0x27, 0x00FFFFFF,  0)

        # ABN_DECODER_COUNT_N
        ABN_DECODER_COUNT_N                    = (0x28, 0x00FFFFFF,  0)

        # ABN_DECODER_PHI_E_PHI_M_OFFSET
        ABN_DECODER_PHI_M_OFFSET               = (0x29, 0x0000FFFF,  0)
        ABN_DECODER_PHI_E_OFFSET               = (0x29, 0xFFFF0000, 16)

        # ABN_DECODER_PHI_E_PHI_M
        ABN_DECODER_PHI_M                      = (0x2a, 0x0000FFFF,  0)
        ABN_DECODER_PHI_E                      = (0x2a, 0xFFFF0000, 16)

        # ABN_2_DECODER_MODE
        ABN_2_APOL                             = (0x2c, 0x00000001,  0)
        ABN_2_BPOL                             = (0x2c, 0x00000002,  1)
        ABN_2_NPOL                             = (0x2c, 0x00000004,  2)
        ABN_2_USE_ABN_AS_N                     = (0x2c, 0x00000008,  3)
        ABN_2_CLN                              = (0x2c, 0x00000100,  8)
        ABN_2_DIRECTION                        = (0x2c, 0x00001000, 12)

        # ABN_2_DECODER_PPR
        ABN_2_DECODER_PPR                      = (0x2d, 0x00FFFFFF,  0)

        # ABN_2_DECODER_COUNT
        ABN_2_DECODER_COUNT                    = (0x2e, 0x00FFFFFF,  0)

        # ABN_2_DECODER_COUNT_N
        ABN_2_DECODER_COUNT_N                  = (0x2f, 0x00FFFFFF,  0)

        # ABN_2_DECODER_PHI_M_OFFSET
        ABN_2_DECODER_PHI_M_OFFSET             = (0x30, 0x0000FFFF,  0)

        # ABN_2_DECODER_PHI_M
        ABN_2_DECODER_PHI_M                    = (0x31, 0x0000FFFF,  0)

        # HALL_MODE
        HALL_POLARITY                          = (0x33, 0x00000001,  0)
        HALL_INTERPOLATION                     = (0x33, 0x00000100,  8)
        HALL_DIRECTION                         = (0x33, 0x00001000, 12)
        HALL_HALL_BLANK                        = (0x33, 0x0FFF0000, 16)

        # HALL_POSITION_060_000
        HALL_POSITION_000                      = (0x34, 0x0000FFFF,  0)
        HALL_POSITION_060                      = (0x34, 0xFFFF0000, 16)

        # HALL_POSITION_180_120
        HALL_POSITION_120                      = (0x35, 0x0000FFFF,  0)
        HALL_POSITION_180                      = (0x35, 0xFFFF0000, 16)

        # HALL_POSITION_300_240
        HALL_POSITION_240                      = (0x36, 0x0000FFFF,  0)
        HALL_POSITION_300                      = (0x36, 0xFFFF0000, 16)

        # HALL_PHI_E_PHI_M_OFFSET
        HALL_PHI_M_OFFSET                      = (0x37, 0x0000FFFF,  0)
        HALL_PHI_E_OFFSET                      = (0x37, 0xFFFF0000, 16)

        # HALL_DPHI_MAX
        HALL_DPHI_MAX                          = (0x38, 0x0000FFFF,  0)

        # HALL_PHI_E_INTERPOLATED_PHI_E
        HALL_PHI_E                             = (0x39, 0x0000FFFF,  0)
        HALL_PHI_E_INTERPOLATED                = (0x39, 0xFFFF0000, 16)

        # HALL_PHI_M
        HALL_PHI_M                             = (0x3a, 0x0000FFFF,  0)

        # AENC_DECODER_MODE
        AENC_DECODER_MODE_120DEG_N90DEG        = (0x3b, 0x00000001,  0)
        AENC_DECODER_MODE_DECODER_COUNT_DIR    = (0x3b, 0x00001000, 12)

        # AENC_DECODER_N_THRESHOLD
        AENC_DECODER_N_THRESHOLD               = (0x3c, 0x0000FFFF,  0)
        AENC_DECODER_N_MASK                    = (0x3c, 0xFFFF0000, 16)

        # AENC_DECODER_PHI_A_RAW
        AENC_DECODER_PHI_A_RAW                 = (0x3d, 0x0000FFFF,  0)

        # AENC_DECODER_PHI_A_OFFSET
        AENC_DECODER_PHI_A_OFFSET              = (0x3e, 0x0000FFFF,  0)

        # AENC_DECODER_PHI_A
        AENC_DECODER_PHI_A                     = (0x3f, 0x0000FFFF,  0)

        # AENC_DECODER_PPR
        AENC_DECODER_PPR                       = (0x40, 0x0000FFFF,  0)

        # AENC_DECODER_COUNT
        AENC_DECODER_COUNT                     = (0x41, 0xFFFFFFFF,  0)

        # AENC_DECODER_COUNT_N
        AENC_DECODER_COUNT_N                   = (0x42, 0xFFFFFFFF,  0)

        # AENC_DECODER_PHI_E_PHI_M_OFFSET
        AENC_DECODER_PHI_M_OFFSET              = (0x45, 0x0000FFFF,  0)
        AENC_DECODER_PHI_E_OFFSET              = (0x45, 0xFFFF0000, 16)

        # AENC_DECODER_PHI_E_PHI_M
        AENC_DECODER_PHI_M                     = (0x46, 0x0000FFFF,  0)
        AENC_DECODER_PHI_E                     = (0x46, 0xFFFF0000, 16)

        # AENC_DECODER_POSITION
        AENC_DECODER_POSITION                  = (0x47, 0xFFFFFFFF,  0)

        # PIDIN_VELOCITY_TARGET
        PIDIN_VELOCITY_TARGET                  = (0x4b, 0xFFFFFFFF,  0)

        # PIDIN_POSITION_TARGET
        PIDIN_POSITION_TARGET                  = (0x4c, 0xFFFFFFFF,  0)

        # CONFIG_DATA
        BIQUAD_X_A_1                           = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_X_A_2                           = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_X_B_0                           = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_X_B_1                           = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_X_B_2                           = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_X_ENABLE                        = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_V_A_1                           = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_V_A_2                           = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_V_B_0                           = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_V_B_1                           = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_V_B_2                           = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_V_ENABLE                        = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_T_A_1                           = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_T_A_2                           = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_T_B_0                           = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_T_B_1                           = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_T_B_2                           = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_T_ENABLE                        = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_F_A_1                           = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_F_A_2                           = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_F_B_0                           = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_F_B_1                           = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_F_B_2                           = (0x4d, 0xFFFFFFFF,  0)
        BIQUAD_F_ENABLE                        = (0x4d, 0xFFFFFFFF,  0)
        PRBS_AMPLITUDE                         = (0x4d, 0xFFFFFFFF,  0)
        PRBS_DOWN_SAMPLING_RATIO               = (0x4d, 0xFFFFFFFF,  0)
        FEED_FORWARD_VELOCITY_GAIN             = (0x4d, 0xFFFFFFFF,  0)
        FEED_FORWARD_VELICITY_FILTER_CONSTANT  = (0x4d, 0xFFFFFFFF,  0)
        FEED_FORWARD_TORQUE_GAIN               = (0x4d, 0xFFFFFFFF,  0)
        FEED_FORWARD_TORGUE_FILTER_CONSTANT    = (0x4d, 0xFFFFFFFF,  0)
        VELOCITY_METER_PPTM_MIN_POS_DEV        = (0x4d, 0x0000FFFF,  0)
        REF_SWITCH_CONFIG                      = (0x4d, 0x0000FFFF,  0)
        ENCODER_INIT_HALL_ENABLE               = (0x4d, 0x00000001,  0)
        SINGLE_PIN_IF_CFG                      = (0x4d, 0x000000FF,  0)
        SINGLE_PIN_IF_STATUS                   = (0x4d, 0xFFFF0000, 16)
        SINGLE_PIN_IF_OFFSET                   = (0x4d, 0x0000FFFF,  0)
        SINGLE_PIN_IF_SCALE                    = (0x4d, 0xFFFF0000, 16)

        # CONFIG_ADDR
        CONFIG_ADDR                            = (0x4e, 0xFFFFFFFF,  0)

        # VELOCITY_SELECTION
        VELOCITY_SELECTION                     = (0x50, 0x000000FF,  0)
        VELOCITY_METER_SELECTION               = (0x50, 0x0000FF00,  8)

        # POSITION_SELECTION
        POSITION_SELECTION                     = (0x51, 0x000000FF,  0)

        # PHI_E_SELECTION
        PHI_E_SELECTION                        = (0x52, 0x000000FF,  0)

        # PHI_E
        PHI_E                                  = (0x53, 0x0000FFFF,  0)

        # PID_FLUX_P_FLUX_I
        PID_FLUX_I                             = (0x54, 0x0000FFFF,  0)
        PID_FLUX_P                             = (0x54, 0xFFFF0000, 16)

        # PID_TORQUE_P_TORQUE_I
        PID_TORQUE_I                           = (0x56, 0x0000FFFF,  0)
        PID_TORQUE_P                           = (0x56, 0xFFFF0000, 16)

        # PID_VELOCITY_P_VELOCITY_I
        PID_VELOCITY_I                         = (0x58, 0x0000FFFF,  0)
        PID_VELOCITY_P                         = (0x58, 0xFFFF0000, 16)

        # PID_POSITION_P_POSITION_I
        PID_POSITION_I                         = (0x5a, 0x0000FFFF,  0)
        PID_POSITION_P                         = (0x5a, 0xFFFF0000, 16)

        # PID_TORQUE_FLUX_TARGET_DDT_LIMITS
        PID_TORQUE_FLUX_TARGET_DDT_LIMITS      = (0x5c, 0xFFFFFFFF,  0)

        # PIDOUT_UQ_UD_LIMITS
        PIDOUT_UQ_UD_LIMITS                    = (0x5d, 0x0000FFFF,  0)

        # PID_TORQUE_FLUX_LIMITS
        PID_TORQUE_FLUX_LIMITS                 = (0x5e, 0x0000FFFF,  0)

        # PID_ACCELERATION_LIMIT
        PID_ACCELERATION_LIMIT                 = (0x5f, 0xFFFFFFFF,  0)

        # PID_VELOCITY_LIMIT
        PID_VELOCITY_LIMIT                     = (0x60, 0xFFFFFFFF,  0)

        # PID_POSITION_LIMIT_LOW
        PID_POSITION_LIMIT_LOW                 = (0x61, 0xFFFFFFFF,  0)

        # PID_POSITION_LIMIT_HIGH
        PID_POSITION_LIMIT_HIGH                = (0x62, 0xFFFFFFFF,  0)

        # MODE_RAMP_MODE_MOTION
        MODE_MOTION                            = (0x63, 0x000000FF,  0)
        MODE_RAMP                              = (0x63, 0x0000FF00,  8)
        MODE_FF                                = (0x63, 0x00FF0000, 16)
        MODE_PID_SMPL                          = (0x63, 0x7F000000, 24)
        MODE_PID_TYPE                          = (0x63, 0x80000000, 31)

        # PID_TORQUE_FLUX_TARGET
        PID_FLUX_TARGET                        = (0x64, 0x0000FFFF,  0)
        PID_TORQUE_TARGET                      = (0x64, 0xFFFF0000, 16)

        # PID_TORQUE_FLUX_OFFSET
        PID_FLUX_OFFSET                        = (0x65, 0x0000FFFF,  0)
        PID_TORQUE_OFFSET                      = (0x65, 0xFFFF0000, 16)

        # PID_VELOCITY_TARGET
        PID_VELOCITY_TARGET                    = (0x66, 0xFFFFFFFF,  0)

        # PID_VELOCITY_OFFSET
        PID_VELOCITY_OFFSET                    = (0x67, 0xFFFFFFFF,  0)

        # PID_POSITION_TARGET
        PID_POSITION_TARGET                    = (0x68, 0xFFFFFFFF,  0)

        # PID_TORQUE_FLUX_ACTUAL
        PID_FLUX_ACTUAL                        = (0x69, 0x0000FFFF,  0)
        PID_TORQUE_ACTUAL                      = (0x69, 0xFFFF0000, 16)

        # PID_VELOCITY_ACTUAL
        PID_VELOCITY_ACTUAL                    = (0x6a, 0xFFFFFFFF,  0)

        # PID_POSITION_ACTUAL
        PID_POSITION_ACTUAL                    = (0x6b, 0xFFFFFFFF,  0)

        # PID_ERROR_DATA
        PID_TORQUE_ERROR                       = (0x6c, 0xFFFFFFFF,  0)
        PID_FLUX_ERROR                         = (0x6c, 0xFFFFFFFF,  0)
        PID_VELOCITY_ERROR                     = (0x6c, 0xFFFFFFFF,  0)
        PID_POSITION_ERROR                     = (0x6c, 0xFFFFFFFF,  0)
        PID_TORQUE_ERROR_SUM                   = (0x6c, 0xFFFFFFFF,  0)
        PID_FLUX_ERROR_SUM                     = (0x6c, 0xFFFFFFFF,  0)
        PID_VELOCITY_ERROR_SUM                 = (0x6c, 0xFFFFFFFF,  0)
        PID_POSITION_ERROR_SUM                 = (0x6c, 0xFFFFFFFF,  0)

        # PID_ERROR_ADDR
        PID_ERROR_ADDR                         = (0x6d, 0x000000FF,  0)

        # INTERIM_DATA
        PIDIN_TARGET_TORQUE                    = (0x6e, 0xFFFFFFFF,  0)
        PIDIN_TARGET_FLUX                      = (0x6e, 0xFFFFFFFF,  0)
        PIDIN_TARGET_VELOCITY                  = (0x6e, 0xFFFFFFFF,  0)
        PIDIN_TARGET_POSITION                  = (0x6e, 0xFFFFFFFF,  0)
        PIDOUT_TARGET_TORQUE                   = (0x6e, 0xFFFFFFFF,  0)
        PIDOUT_TARGET_FLUX                     = (0x6e, 0xFFFFFFFF,  0)
        PIDOUT_TARGET_VELOCITY                 = (0x6e, 0xFFFFFFFF,  0)
        PIDOUT_TARGET_POSITION                 = (0x6e, 0xFFFFFFFF,  0)
        FOC_IUX                                = (0x6e, 0x0000FFFF,  0)
        FOC_IWY                                = (0x6e, 0xFFFF0000, 16)
        FOC_IV                                 = (0x6e, 0x0000FFFF,  0)
        FOC_IA                                 = (0x6e, 0x0000FFFF,  0)
        FOC_IB                                 = (0x6e, 0xFFFF0000, 16)
        FOC_ID                                 = (0x6e, 0x0000FFFF,  0)
        FOC_IQ                                 = (0x6e, 0xFFFF0000, 16)
        FOC_UD                                 = (0x6e, 0x0000FFFF,  0)
        FOC_UQ                                 = (0x6e, 0xFFFF0000, 16)
        FOC_UD_LIMITED                         = (0x6e, 0x0000FFFF,  0)
        FOC_UQ_LIMITED                         = (0x6e, 0xFFFF0000, 16)
        FOC_UA                                 = (0x6e, 0x0000FFFF,  0)
        FOC_UB                                 = (0x6e, 0xFFFF0000, 16)
        FOC_UUX                                = (0x6e, 0x0000FFFF,  0)
        FOC_UWY                                = (0x6e, 0xFFFF0000, 16)
        FOC_UV                                 = (0x6e, 0x0000FFFF,  0)
        PWM_UX                                 = (0x6e, 0x0000FFFF,  0)
        PWM_WY                                 = (0x6e, 0xFFFF0000, 16)
        PWM_V                                  = (0x6e, 0x0000FFFF,  0)
        ADC_I_0                                = (0x6e, 0x0000FFFF,  0)
        ADC_I_1                                = (0x6e, 0xFFFF0000, 16)
        PID_FLUX_ACTUAL_DIV256                 = (0x6e, 0x000000FF,  0)
        PID_TORQUE_ACTUAL_DIV256               = (0x6e, 0x0000FF00,  8)
        PID_FLUX_TARGET_DIV256                 = (0x6e, 0x00FF0000, 16)
        PID_TORQUE_TARGET_DIV256               = (0x6e, 0xFF000000, 24)
        PID_TORQUE_ACTUAL_INTERIM              = (0x6e, 0x0000FFFF,  0)
        PID_TORQUE_TARGET_INTERIM              = (0x6e, 0xFFFF0000, 16)
        PID_FLUX_ACTUAL_INTERIM                = (0x6e, 0x0000FFFF,  0)
        PID_FLUX_TARGET_INTERIM                = (0x6e, 0xFFFF0000, 16)
        PID_VELOCITY_ACTUAL_DIV256             = (0x6e, 0x0000FFFF,  0)
        PID_VELOCITY_TARGET_DIV256             = (0x6e, 0xFFFF0000, 16)
        PID_VELOCITY_ACTUAL_LSB                = (0x6e, 0x0000FFFF,  0)
        PID_VELOCITY_TARGET_LSB                = (0x6e, 0xFFFF0000, 16)
        PID_POSITION_ACTUAL_DIV256             = (0x6e, 0x0000FFFF,  0)
        PID_POSITION_TARGET_DIV256             = (0x6e, 0xFFFF0000, 16)
        PID_POSITION_ACTUAL_LSB                = (0x6e, 0x0000FFFF,  0)
        PID_POSITION_TARGET_LSB                = (0x6e, 0xFFFF0000, 16)
        FF_VELOCITY                            = (0x6e, 0xFFFFFFFF,  0)
        FF_TORQUE                              = (0x6e, 0x0000FFFF,  0)
        ACTUAL_VELOCITY_PPTM                   = (0x6e, 0xFFFFFFFF,  0)
        REF_SWITCH_STATUS                      = (0x6e, 0x0000FFFF,  0)
        HOME_POSITION                          = (0x6e, 0xFFFFFFFF,  0)
        LEFT_POSITION                          = (0x6e, 0xFFFFFFFF,  0)
        RIGHT_POSITION                         = (0x6e, 0xFFFFFFFF,  0)
        ENC_INIT_HALL_STATUS                   = (0x6e, 0x0000FFFF,  0)
        ENC_INIT_HALL_PHI_E_ABN_OFFSET         = (0x6e, 0x0000FFFF,  0)
        ENC_INIT_HALL_PHI_E_AENC_OFFSET        = (0x6e, 0x0000FFFF,  0)
        ENC_INIT_HALL_PHI_A_AENC_OFFSET        = (0x6e, 0x0000FFFF,  0)
        ENC_INIT_MINI_MOVE_STATUS              = (0x6e, 0x0000FFFF,  0)
        ENC_INIT_MINI_MOVE_U_D                 = (0x6e, 0xFFFF0000, 16)
        ENC_INIT_MINI_MOVE_PHI_E_OFFSET        = (0x6e, 0x0000FFFF,  0)
        ENC_INIT_MINI_MOVE_PHI_E               = (0x6e, 0xFFFF0000, 16)
        SINGLE_PIN_IF_TARGET_TORQUE            = (0x6e, 0x0000FFFF,  0)
        SINGLE_PIN_IF_PWM_DUTY_CYCLE           = (0x6e, 0xFFFF0000, 16)
        SINGLE_PIN_IF_TARGET_VELOCITY          = (0x6e, 0xFFFFFFFF,  0)
        SINGLE_PIN_IF_TARGET_POSITION          = (0x6e, 0xFFFFFFFF,  0)
        DEBUG_VALUE_0                          = (0x6e, 0x0000FFFF,  0)
        DEBUG_VALUE_1                          = (0x6e, 0xFFFF0000, 16)
        DEBUG_VALUE_2                          = (0x6e, 0x0000FFFF,  0)
        DEBUG_VALUE_3                          = (0x6e, 0xFFFF0000, 16)
        DEBUG_VALUE_4                          = (0x6e, 0x0000FFFF,  0)
        DEBUG_VALUE_5                          = (0x6e, 0xFFFF0000, 16)
        DEBUG_VALUE_6                          = (0x6e, 0x0000FFFF,  0)
        DEBUG_VALUE_7                          = (0x6e, 0xFFFF0000, 16)
        DEBUG_VALUE_8                          = (0x6e, 0x0000FFFF,  0)
        DEBUG_VALUE_9                          = (0x6e, 0xFFFF0000, 16)
        DEBUG_VALUE_10                         = (0x6e, 0x0000FFFF,  0)
        DEBUG_VALUE_11                         = (0x6e, 0xFFFF0000, 16)
        DEBUG_VALUE_12                         = (0x6e, 0x0000FFFF,  0)
        DEBUG_VALUE_13                         = (0x6e, 0xFFFF0000, 16)
        DEBUG_VALUE_14                         = (0x6e, 0x0000FFFF,  0)
        DEBUG_VALUE_15                         = (0x6e, 0xFFFF0000, 16)
        DEBUG_VALUE_16                         = (0x6e, 0xFFFFFFFF,  0)
        DEBUG_VALUE_17                         = (0x6e, 0xFFFFFFFF,  0)
        DEBUG_VALUE_18                         = (0x6e, 0xFFFFFFFF,  0)
        DEBUG_VALUE_19                         = (0x6e, 0xFFFFFFFF,  0)
        CONFIG_REG_0                           = (0x6e, 0xFFFFFFFF,  0)
        CONFIG_REG_1                           = (0x6e, 0xFFFFFFFF,  0)
        CTRL_PARAM_0                           = (0x6e, 0x0000FFFF,  0)
        CTRL_PARAM_1                           = (0x6e, 0xFFFF0000, 16)
        CTRL_PARAM_2                           = (0x6e, 0x0000FFFF,  0)
        CTRL_PARAM_3                           = (0x6e, 0xFFFF0000, 16)
        STATUS_REG_0                           = (0x6e, 0xFFFFFFFF,  0)
        STATUS_REG_1                           = (0x6e, 0xFFFFFFFF,  0)
        STATUS_PARAM_0                         = (0x6e, 0x0000FFFF,  0)
        STATUS_PARAM_1                         = (0x6e, 0xFFFF0000, 16)
        STATUS_PARAM_2                         = (0x6e, 0x0000FFFF,  0)
        STATUS_PARAM_3                         = (0x6e, 0xFFFF0000, 16)

        # INTERIM_ADDR
        INTERIM_ADDR                           = (0x6f, 0x000000FF,  0)

        # WATCHDOG_CFG
        WATCHDOG_CFG                           = (0x74, 0x00000003,  0)

        # ADC_VM_LIMITS
        ADC_VM_LIMIT_LOW                       = (0x75, 0x0000FFFF,  0)
        ADC_VM_LIMIT_HIGH                      = (0x75, 0xFFFF0000, 16)

        # TMC4671_INPUTS_RAW
        A_OF_ABN_RAW                           = (0x76, 0x00000001,  0)
        B_OF_ABN_RAW                           = (0x76, 0x00000002,  1)
        N_OF_ABN_RAW                           = (0x76, 0x00000004,  2)
        A_OF_ABN_2_RAW                         = (0x76, 0x00000010,  4)
        B_OF_ABN_2_RAW                         = (0x76, 0x00000020,  5)
        N_OF_ABN_2_RAW                         = (0x76, 0x00000040,  6)
        HALL_UX_OF_HALL_RAW                    = (0x76, 0x00000100,  8)
        HALL_V_OF_HALL_RAW                     = (0x76, 0x00000200,  9)
        HALL_WY_OF_HALL_RAW                    = (0x76, 0x00000400, 10)
        REF_SW_R_RAW                           = (0x76, 0x00001000, 12)
        REF_SW_H_RAW                           = (0x76, 0x00002000, 13)
        REF_SW_L_RAW                           = (0x76, 0x00004000, 14)
        ENABLE_IN_RAW                          = (0x76, 0x00008000, 15)
        STP_OF_DIRSTP_RAW                      = (0x76, 0x00010000, 16)
        DIR_OF_DIRSTP_RAW                      = (0x76, 0x00020000, 17)
        PWM_IN_RAW                             = (0x76, 0x00040000, 18)
        HALL_UX_FILT                           = (0x76, 0x00100000, 20)
        HALL_V_FILT                            = (0x76, 0x00200000, 21)
        HALL_WY_FILT                           = (0x76, 0x00400000, 22)
        PWM_IDLE_L_RAW                         = (0x76, 0x10000000, 28)
        PWM_IDLE_H_RAW                         = (0x76, 0x20000000, 29)

        # TMC4671_OUTPUTS_RAW
        TMC4671_OUTPUTS_RAW_PWM_UX1_L          = (0x77, 0x00000001,  0)
        TMC4671_OUTPUTS_RAW_PWM_UX1_H          = (0x77, 0x00000002,  1)
        TMC4671_OUTPUTS_RAW_PWM_VX2_L          = (0x77, 0x00000004,  2)
        TMC4671_OUTPUTS_RAW_PWM_VX2_H          = (0x77, 0x00000008,  3)
        TMC4671_OUTPUTS_RAW_PWM_WY1_L          = (0x77, 0x00000010,  4)
        TMC4671_OUTPUTS_RAW_PWM_WY1_H          = (0x77, 0x00000020,  5)
        TMC4671_OUTPUTS_RAW_PWM_Y2_L           = (0x77, 0x00000040,  6)
        TMC4671_OUTPUTS_RAW_PWM_Y2_H           = (0x77, 0x00000080,  7)

        # STEP_WIDTH
        STEP_WIDTH                             = (0x78, 0xFFFFFFFF,  0)

        # UART_BPS
        UART_BPS                               = (0x79, 0x00FFFFFF,  0)

        # UART_ADDRS
        ADDR_A                                 = (0x7A, 0x000000FF,  0)
        ADDR_B                                 = (0x7A, 0x0000FF00,  8)
        ADDR_C                                 = (0x7A, 0x00FF0000, 16)
        ADDR_D                                 = (0x7A, 0xFF000000, 24)

        # GPIO_dsADCI_CONFIG
        GPIO_DSADCI_CONFIG_0                   = (0x7B, 0x00000001,  0)
        GPIO_DSADCI_CONFIG_1                   = (0x7B, 0x00000002,  1)
        GPIO_DSADCI_CONFIG_2                   = (0x7B, 0x00000004,  2)
        GPIO_DSADCI_CONFIG_3                   = (0x7B, 0x00000008,  3)
        GPIO_DSADCI_CONFIG_4                   = (0x7B, 0x00000010,  4)
        GPIO_DSADCI_CONFIG_5                   = (0x7B, 0x00000020,  5)
        GPIO_DSADCI_CONFIG_6                   = (0x7B, 0x00000040,  6)
        GPO                                    = (0x7B, 0x00FF0000, 16)
        GPI                                    = (0x7B, 0xFF000000, 24)

        # STATUS_FLAGS
        STATUS_FLAG_PID_X_TARGET_LIMIT         = (0x7c, 0x00000001,  0)
        STATUS_FLAG_PID_X_TARGET_DDT_LIMIT     = (0x7c, 0x00000002,  1)
        STATUS_FLAG_PID_X_ERRSUM_LIMIT         = (0x7c, 0x00000004,  2)
        STATUS_FLAG_PID_X_OUTPUT_LIMIT         = (0x7c, 0x00000008,  3)
        STATUS_FLAG_PID_V_TARGET_LIMIT         = (0x7c, 0x00000010,  4)
        STATUS_FLAG_PID_V_TARGET_DDT_LIMIT     = (0x7c, 0x00000020,  5)
        STATUS_FLAG_PID_V_ERRSUM_LIMIT         = (0x7c, 0x00000040,  6)
        STATUS_FLAG_PID_V_OUTPUT_LIMIT         = (0x7c, 0x00000080,  7)
        STATUS_FLAG_PID_ID_TARGET_LIMIT        = (0x7c, 0x00000100,  8)
        STATUS_FLAG_PID_ID_TARGET_DDT_LIMIT    = (0x7c, 0x00000200,  9)
        STATUS_FLAG_PID_ID_ERRSUM_LIMIT        = (0x7c, 0x00000400, 10)
        STATUS_FLAG_PID_ID_OUTPUT_LIMIT        = (0x7c, 0x00000800, 11)
        STATUS_FLAG_PID_IQ_TARGET_LIMIT        = (0x7c, 0x00001000, 12)
        STATUS_FLAG_PID_IQ_TARGET_DDT_LIMIT    = (0x7c, 0x00002000, 13)
        STATUS_FLAG_PID_IQ_ERRSUM_LIMIT        = (0x7c, 0x00004000, 14)
        STATUS_FLAG_PID_IQ_OUTPUT_LIMIT        = (0x7c, 0x00008000, 15)
        STATUS_FLAG_IPARK_CIRLIM_LIMIT_U_D     = (0x7c, 0x00010000, 16)
        STATUS_FLAG_IPARK_CIRLIM_LIMIT_U_Q     = (0x7c, 0x00020000, 17)
        STATUS_FLAG_IPARK_CIRLIM_LIMIT_U_R     = (0x7c, 0x00040000, 18)
        STATUS_FLAG_NOT_PLL_LOCKED             = (0x7c, 0x00080000, 19)
        STATUS_FLAG_REF_SW_R                   = (0x7c, 0x00100000, 20)
        STATUS_FLAG_REF_SW_H                   = (0x7c, 0x00200000, 21)
        STATUS_FLAG_REF_SW_L                   = (0x7c, 0x00400000, 22)
        STATUS_FLAG___                         = (0x7c, 0x00800000, 23)
        STATUS_FLAG_PWM_MIN                    = (0x7c, 0x01000000, 24)
        STATUS_FLAG_PWM_MAX                    = (0x7c, 0x02000000, 25)
        STATUS_FLAG_ADC_I_CLIPPED              = (0x7c, 0x04000000, 26)
        STATUS_FLAG_AENC_CLIPPED               = (0x7c, 0x08000000, 27)
        STATUS_FLAG_ENC_N                      = (0x7c, 0x10000000, 28)
        STATUS_FLAG_ENC_2_N                    = (0x7c, 0x20000000, 29)
        STATUS_FLAG_AENC_N                     = (0x7c, 0x40000000, 30)
        STATUS_FLAG_WD_ERROR                   = (0x7c, 0x80000000, 31)

        # STATUS_MASK
        WARNING_MASK                           = (0x7d, 0xFFFFFFFF,  0)

    class VARIANT:
        """
        TMC4671 register variants.
        """
        CHIPINFO_ADDR_SI_TYPE                                   = 0
        CHIPINFO_ADDR_SI_VERSION                                = 1
        CHIPINFO_ADDR_SI_DATE                                   = 2
        CHIPINFO_ADDR_SI_TIME                                   = 3
        CHIPINFO_ADDR_SI_VARIANT                                = 4
        CHIPINFO_ADDR_SI_BUILD                                  = 5

        ADC_RAW_ADDR_ADC_I1_RAW_ADC_I0_RAW                      = 0
        ADC_RAW_ADDR_ADC_AGPI_A_RAW_ADC_VM_RAW                  = 1
        ADC_RAW_ADDR_ADC_AENC_UX_RAW_ADC_AGPI_B_RAW             = 2
        ADC_RAW_ADDR_ADC_AENC_WY_RAW_ADC_AENC_VN_RAW            = 3

        CONFIG_ADDR_biquad_x_a_1                                = 1
        CONFIG_ADDR_biquad_x_a_2                                = 2
        CONFIG_ADDR_biquad_x_b_0                                = 4
        CONFIG_ADDR_biquad_x_b_1                                = 5
        CONFIG_ADDR_biquad_x_b_2                                = 6
        CONFIG_ADDR_biquad_x_enable                             = 7
        CONFIG_ADDR_biquad_v_a_1                                = 9
        CONFIG_ADDR_biquad_v_a_2                                = 10
        CONFIG_ADDR_biquad_v_b_0                                = 12
        CONFIG_ADDR_biquad_v_b_1                                = 13
        CONFIG_ADDR_biquad_v_b_2                                = 14
        CONFIG_ADDR_biquad_v_enable                             = 15
        CONFIG_ADDR_biquad_t_a_1                                = 17
        CONFIG_ADDR_biquad_t_a_2                                = 18
        CONFIG_ADDR_biquad_t_b_0                                = 20
        CONFIG_ADDR_biquad_t_b_1                                = 21
        CONFIG_ADDR_biquad_t_b_2                                = 22
        CONFIG_ADDR_biquad_t_enable                             = 23
        CONFIG_ADDR_biquad_f_a_1                                = 25
        CONFIG_ADDR_biquad_f_a_2                                = 26
        CONFIG_ADDR_biquad_f_b_0                                = 28
        CONFIG_ADDR_biquad_f_b_1                                = 29
        CONFIG_ADDR_biquad_f_b_2                                = 30
        CONFIG_ADDR_biquad_f_enable                             = 31
        CONFIG_ADDR_prbs_amplitude                              = 32
        CONFIG_ADDR_prbs_down_sampling_ratio                    = 33
        CONFIG_ADDR_feed_forward_velocity_gain                  = 40
        CONFIG_ADDR_feed_forward_velicity_filter_constant       = 41
        CONFIG_ADDR_feed_forward_torque_gain                    = 42
        CONFIG_ADDR_feed_forward_torgue_filter_constant         = 43
        CONFIG_ADDR_VELOCITY_METER_PPTM_MIN_POS_DEV             = 50
        CONFIG_ADDR_ref_switch_config                           = 51
        CONFIG_ADDR_Encoder_Init_hall_Enable                    = 52
        CONFIG_ADDR_SINGLE_PIN_IF_STATUS_CFG                    = 60
        CONFIG_ADDR_SINGLE_PIN_IF_SCALE_OFFSET                  = 61

        PID_ERROR_ADDR_PID_TORQUE_ERROR                         = 0
        PID_ERROR_ADDR_PID_FLUX_ERROR                           = 1
        PID_ERROR_ADDR_PID_VELOCITY_ERROR                       = 2
        PID_ERROR_ADDR_PID_POSITION_ERROR                       = 3
        PID_ERROR_ADDR_PID_TORQUE_ERROR_SUM                     = 4
        PID_ERROR_ADDR_PID_FLUX_ERROR_SUM                       = 5
        PID_ERROR_ADDR_PID_VELOCITY_ERROR_SUM                   = 6
        PID_ERROR_ADDR_PID_POSITION_ERROR_SUM                   = 7

        INTERIM_ADDR_PIDIN_TARGET_TORQUE                        = 0
        INTERIM_ADDR_PIDIN_TARGET_FLUX                          = 1
        INTERIM_ADDR_PIDIN_TARGET_VELOCITY                      = 2
        INTERIM_ADDR_PIDIN_TARGET_POSITION                      = 3
        INTERIM_ADDR_PIDOUT_TARGET_TORQUE                       = 4
        INTERIM_ADDR_PIDOUT_TARGET_FLUX                         = 5
        INTERIM_ADDR_PIDOUT_TARGET_VELOCITY                     = 6
        INTERIM_ADDR_PIDOUT_TARGET_POSITION                     = 7
        INTERIM_ADDR_FOC_IWY_IUX                                = 8
        INTERIM_ADDR_FOC_IV                                     = 9
        INTERIM_ADDR_FOC_IB_IA                                  = 10
        INTERIM_ADDR_FOC_IQ_ID                                  = 11
        INTERIM_ADDR_FOC_UQ_UD                                  = 12
        INTERIM_ADDR_FOC_UQ_UD_LIMITED                          = 13
        INTERIM_ADDR_FOC_UB_UA                                  = 14
        INTERIM_ADDR_FOC_UWY_UUX                                = 15
        INTERIM_ADDR_FOC_UV                                     = 16
        INTERIM_ADDR_PWM_WY_UX                                  = 17
        INTERIM_ADDR_PWM_UV                                     = 18
        INTERIM_ADDR_ADC_I1_I0                                  = 19
        INTERIM_ADDR_PID_TORQUE_TARGET_TORQUE_ACTUAL            = 21
        INTERIM_ADDR_PID_FLUX_TARGET_FLUX_ACTUAL                = 22
        INTERIM_ADDR_PID_VELOCITY_TARGET_VELOCITY_ACTUAL_DIV256 = 23
        INTERIM_ADDR_PID_VELOCITY_TARGET_VELOCITY_ACTUAL        = 24
        INTERIM_ADDR_PID_POSITION_TARGET_POSITION_ACTUAL_DIV256 = 25
        INTERIM_ADDR_PID_POSITION_TARGET_POSITION_ACTUAL        = 26
        INTERIM_ADDR_FF_VELOCITY                                = 27
        INTERIM_ADDR_FF_TORQUE                                  = 28
        INTERIM_ADDR_ACTUAL_VELOCITY_PPTM                       = 29
        INTERIM_ADDR_REF_SWITCH_STATUS                          = 30
        INTERIM_ADDR_HOME_POSITION                              = 31
        INTERIM_ADDR_LEFT_POSITION                              = 32
        INTERIM_ADDR_RIGHT_POSITION                             = 33
        INTERIM_ADDR_ENC_INIT_HALL_STATUS                       = 34
        INTERIM_ADDR_ENC_INIT_HALL_PHI_E_ABN_OFFSET             = 35
        INTERIM_ADDR_ENC_INIT_HALL_PHI_E_AENC_OFFSET            = 36
        INTERIM_ADDR_ENC_INIT_HALL_PHI_A_AENC_OFFSET            = 37
        INTERIM_ADDR_enc_init_mini_move_u_d_status              = 40
        INTERIM_ADDR_enc_init_mini_move_phi_e_phi_e_offset      = 41
        INTERIM_ADDR_SINGLE_PIN_IF_PWM_DUTY_CYCLE_TORQUE_TARGET = 42
        INTERIM_ADDR_SINGLE_PIN_IF_VELOCITY_TARGET              = 43
        INTERIM_ADDR_SINGLE_PIN_IF_POSITION_TARGET              = 44
        INTERIM_ADDR_DEBUG_VALUE_1_0                            = 192
        INTERIM_ADDR_DEBUG_VALUE_3_2                            = 193
        INTERIM_ADDR_DEBUG_VALUE_5_4                            = 194
        INTERIM_ADDR_DEBUG_VALUE_7_6                            = 195
        INTERIM_ADDR_DEBUG_VALUE_9_8                            = 196
        INTERIM_ADDR_DEBUG_VALUE_11_10                          = 197
        INTERIM_ADDR_DEBUG_VALUE_13_12                          = 198
        INTERIM_ADDR_DEBUG_VALUE_15_14                          = 199
        INTERIM_ADDR_DEBUG_VALUE_16                             = 200
        INTERIM_ADDR_DEBUG_VALUE_17                             = 201
        INTERIM_ADDR_DEBUG_VALUE_18                             = 202
        INTERIM_ADDR_DEBUG_VALUE_19                             = 203
        INTERIM_ADDR_CONFIG_REG_0                               = 208
        INTERIM_ADDR_CONFIG_REG_1                               = 209
        INTERIM_ADDR_CTRL_PARAM_10                              = 210
        INTERIM_ADDR_CTRL_PARAM_32                              = 211
        INTERIM_ADDR_STATUS_REG_0                               = 212
        INTERIM_ADDR_STATUS_REG_1                               = 213
        INTERIM_ADDR_STATUS_PARAM_10                            = 214
        INTERIM_ADDR_STATUS_PARAM_32                            = 215

    class ENUM:
        """
        Defines all constants usable with the TMC4671.
        """
        # motor types
        MOTOR_TYPE_NO           = 0
        MOTOR_TYPE_DC           = 1
        MOTOR_TYPE_STEPPER      = 2
        MOTOR_TYPE_BLDC         = 3

        # PWM modes
        PWM_OFF_FREE_RUNNING    = 0
        PWM_OFF_LOW_SIDE_ON     = 1
        PWM_OFF_HIGH_SIDE_ON    = 2
        PWM_LOW_SIDE_CHOPPER    = 5
        PWM_HIGH_SIDE_CHOPPER   = 6
        PWM_CENTERED_FOR_FOC    = 7

        # motion modes
        MOTION_MODE_STOPPED     = 0
        MOTION_MODE_TORQUE      = 1
        MOTION_MODE_VELOCITY    = 2
        MOTION_MODE_POSITION    = 3
        MOTION_MODE_UQ_UD_EXT   = 8

        # phi_e selections
        PHI_E_EXTERNAL      = 1
        PHI_E_OPEN_LOOP     = 2
        PHI_E_ABN           = 3
        PHI_E_HALL          = 5
        PHI_E_AENC          = 6
        PHI_A_AENC          = 7

        # velocity/position selection
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
