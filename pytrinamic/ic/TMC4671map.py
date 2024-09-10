################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from ..ic import Access, RegisterGroup, Field, Register

class TMC4671Map:

    def __init__(self):
        self.ALL_REGISTERS = _ALL_REGISTERS()


class _ALL_REGISTERS(RegisterGroup):

    class _CHIPINFO_DATA(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("CHIPINFO_DATA", parent, access, address, signed)
            self.SI_TYPE = Field("SI_TYPE", self, Access.R, 0xFFFFFFFF,  0, signed=False)

    class _CHIPINFO_ADDR(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("CHIPINFO_ADDR", parent, access, address, signed)
            self.CHIP_INFO_ADDRESS = Field("CHIP_INFO_ADDRESS", self, Access.RW, 0x000000FF,  0, signed=False)

    class _ADC_RAW_DATA(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_RAW_DATA", parent, access, address, signed)
            self.ADC_I0_RAW = Field("ADC_I0_RAW", self, Access.R, 0x0000FFFF,  0, signed=False)
            self.ADC_I1_RAW = Field("ADC_I1_RAW", self, Access.R, 0xFFFF0000, 16, signed=False)

    class _ADC_RAW_ADDR(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_RAW_ADDR", parent, access, address, signed)
            self.ADC_RAW_ADDR = Field("ADC_RAW_ADDR", self, Access.RW, 0x000000FF,  0, signed=False)

    class _dsADC_MCFG_B_MCFG_A(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("dsADC_MCFG_B_MCFG_A", parent, access, address, signed)
            self.cfg_dsmodulator_a = Field("cfg_dsmodulator_a", self, Access.RW, 0x00000003,  0, signed=False)
            self.mclk_polarity_a = Field("mclk_polarity_a", self, Access.RW, 0x00000004,  2, signed=False)
            self.mdat_polarity_a = Field("mdat_polarity_a", self, Access.RW, 0x00000008,  3, signed=False)
            self.sel_nclk_mclk_i_a = Field("sel_nclk_mclk_i_a", self, Access.RW, 0x00000010,  4, signed=False)
            self.blanking_a = Field("blanking_a", self, Access.RW, 0x0000FF00,  8, signed=False)
            self.cfg_dsmodulator_b = Field("cfg_dsmodulator_b", self, Access.RW, 0x00030000, 16, signed=False)
            self.mclk_polarity_b = Field("mclk_polarity_b", self, Access.RW, 0x00040000, 18, signed=False)
            self.mdat_polarity_b = Field("mdat_polarity_b", self, Access.RW, 0x00080000, 19, signed=False)
            self.sel_nclk_mclk_i_b = Field("sel_nclk_mclk_i_b", self, Access.RW, 0x00100000, 20, signed=False)
            self.blanking_b = Field("blanking_b", self, Access.RW, 0xFF000000, 24, signed=False)

    class _dsADC_MCLK_A(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("dsADC_MCLK_A", parent, access, address, signed)
            self.dsADC_MCLK_A = Field("dsADC_MCLK_A", self, Access.RW, 0xFFFFFFFF,  0, signed=False)

    class _dsADC_MCLK_B(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("dsADC_MCLK_B", parent, access, address, signed)
            self.dsADC_MCLK_B = Field("dsADC_MCLK_B", self, Access.RW, 0xFFFFFFFF,  0, signed=False)

    class _dsADC_MDEC_B_MDEC_A(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("dsADC_MDEC_B_MDEC_A", parent, access, address, signed)
            self.dsADC_MDEC_A = Field("dsADC_MDEC_A", self, Access.RW, 0x0000FFFF,  0, signed=False)
            self.dsADC_MDEC_B = Field("dsADC_MDEC_B", self, Access.RW, 0xFFFF0000, 16, signed=False)

    class _ADC_I1_SCALE_OFFSET(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_I1_SCALE_OFFSET", parent, access, address, signed)
            self.ADC_I1_OFFSET = Field("ADC_I1_OFFSET", self, Access.RW, 0x0000FFFF,  0, signed=False)
            self.ADC_I1_SCALE = Field("ADC_I1_SCALE", self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _ADC_I0_SCALE_OFFSET(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_I0_SCALE_OFFSET", parent, access, address, signed)
            self.ADC_I0_OFFSET = Field("ADC_I0_OFFSET", self, Access.RW, 0x0000FFFF,  0, signed=False)
            self.ADC_I0_SCALE = Field("ADC_I0_SCALE", self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _ADC_I_SELECT(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_I_SELECT", parent, access, address, signed)
            self.ADC_I0_SELECT = Field("ADC_I0_SELECT", self, Access.RW, 0x000000FF,  0, signed=False)
            self.ADC_I1_SELECT = Field("ADC_I1_SELECT", self, Access.RW, 0x0000FF00,  8, signed=False)
            self.ADC_I_UX_SELECT = Field("ADC_I_UX_SELECT", self, Access.RW, 0x03000000, 24, signed=False)
            self.ADC_I_V_SELECT = Field("ADC_I_V_SELECT", self, Access.RW, 0x0C000000, 26, signed=False)
            self.ADC_I_WY_SELECT = Field("ADC_I_WY_SELECT", self, Access.RW, 0x30000000, 28, signed=False)

    class _ADC_I1_I0_EXT(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_I1_I0_EXT", parent, access, address, signed)
            self.ADC_I0_EXT = Field("ADC_I0_EXT", self, Access.RW, 0x0000FFFF,  0, signed=False)
            self.ADC_I1_EXT = Field("ADC_I1_EXT", self, Access.RW, 0xFFFF0000, 16, signed=False)

    class _DS_ANALOG_INPUT_STAGE_CFG(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("DS_ANALOG_INPUT_STAGE_CFG", parent, access, address, signed)
            self.ADC_I0 = Field("ADC_I0", self, Access.RW, 0x0000000F,  0, signed=False)
            self.ADC_I1 = Field("ADC_I1", self, Access.RW, 0x000000F0,  4, signed=False)
            self.ADC_VM = Field("ADC_VM", self, Access.RW, 0x00000F00,  8, signed=False)
            self.ADC_AGPI_A = Field("ADC_AGPI_A", self, Access.RW, 0x0000F000, 12, signed=False)
            self.ADC_AGPI_B = Field("ADC_AGPI_B", self, Access.RW, 0x000F0000, 16, signed=False)
            self.ADC_AENC_UX = Field("ADC_AENC_UX", self, Access.RW, 0x00F00000, 20, signed=False)
            self.ADC_AENC_VN = Field("ADC_AENC_VN", self, Access.RW, 0x0F000000, 24, signed=False)
            self.ADC_AENC_WY = Field("ADC_AENC_WY", self, Access.RW, 0xF0000000, 28, signed=False)

    class _AENC_0_SCALE_OFFSET(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_0_SCALE_OFFSET", parent, access, address, signed)
            self.AENC_0_OFFSET = Field("AENC_0_OFFSET", self, Access.RW, 0x0000FFFF,  0, signed=False)
            self.AENC_0_SCALE = Field("AENC_0_SCALE", self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _AENC_1_SCALE_OFFSET(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_1_SCALE_OFFSET", parent, access, address, signed)
            self.AENC_1_OFFSET = Field("AENC_1_OFFSET", self, Access.RW, 0x0000FFFF,  0, signed=False)
            self.AENC_1_SCALE = Field("AENC_1_SCALE", self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _AENC_2_SCALE_OFFSET(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_2_SCALE_OFFSET", parent, access, address, signed)
            self.AENC_2_OFFSET = Field("AENC_2_OFFSET", self, Access.RW, 0x0000FFFF,  0, signed=False)
            self.AENC_2_SCALE = Field("AENC_2_SCALE", self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _AENC_SELECT(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_SELECT", parent, access, address, signed)
            self.AENC_0_SELECT = Field("AENC_0_SELECT", self, Access.RW, 0x000000FF,  0, signed=False)
            self.AENC_1_SELECT = Field("AENC_1_SELECT", self, Access.RW, 0x0000FF00,  8, signed=False)
            self.AENC_2_SELECT = Field("AENC_2_SELECT", self, Access.RW, 0x00FF0000, 16, signed=False)

    class _ADC_IWY_IUX(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_IWY_IUX", parent, access, address, signed)
            self.ADC_IUX = Field("ADC_IUX", self, Access.R, 0x0000FFFF,  0, signed=True)
            self.ADC_IWY = Field("ADC_IWY", self, Access.R, 0xFFFF0000, 16, signed=True)

    class _ADC_IV(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_IV", parent, access, address, signed)
            self.ADC_IV = Field("ADC_IV", self, Access.R, 0x0000FFFF,  0, signed=True)

    class _AENC_WY_UX(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_WY_UX", parent, access, address, signed)
            self.AENC_UX = Field("AENC_UX", self, Access.R, 0x0000FFFF,  0, signed=True)
            self.AENC_WY = Field("AENC_WY", self, Access.R, 0xFFFF0000, 16, signed=True)

    class _AENC_VN(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_VN", parent, access, address, signed)
            self.AENC_VN = Field("AENC_VN", self, Access.R, 0x0000FFFF,  0, signed=True)

    class _PWM_POLARITIES(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PWM_POLARITIES", parent, access, address, signed)
            self.PWM_POLARITIES_0 = Field("PWM_POLARITIES_0", self, Access.RW, 0x00000001,  0, signed=False)
            self.PWM_POLARITIES_1 = Field("PWM_POLARITIES_1", self, Access.RW, 0x00000002,  1, signed=False)

    class _PWM_MAXCNT(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PWM_MAXCNT", parent, access, address, signed)
            self.PWM_MAXCNT = Field("PWM_MAXCNT", self, Access.RW, 0x0000FFFF,  0, signed=False)

    class _PWM_BBM_H_BBM_L(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PWM_BBM_H_BBM_L", parent, access, address, signed)
            self.PWM_BBM_L = Field("PWM_BBM_L", self, Access.RW, 0x000000FF,  0, signed=False)
            self.PWM_BBM_H = Field("PWM_BBM_H", self, Access.RW, 0x0000FF00,  8, signed=False)

    class _PWM_SV_CHOP(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PWM_SV_CHOP", parent, access, address, signed)
            self.PWM_CHOP = Field("PWM_CHOP", self, Access.RW, 0x000000FF,  0, signed=False)
            self.PWM_SV = Field("PWM_SV", self, Access.RW, 0x00000100,  8, signed=False)

    class _MOTOR_TYPE_N_POLE_PAIRS(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("MOTOR_TYPE_N_POLE_PAIRS", parent, access, address, signed)
            self.N_POLE_PAIRS = Field("N_POLE_PAIRS", self, Access.RW, 0x0000FFFF,  0, signed=False)
            self.MOTOR_TYPE = Field("MOTOR_TYPE", self, Access.RW, 0x00FF0000, 16, signed=False)

    class _PHI_E_EXT(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PHI_E_EXT", parent, access, address, signed)
            self.PHI_E_EXT = Field("PHI_E_EXT", self, Access.RW, 0x0000FFFF,  0, signed=True)

    class _OPENLOOP_MODE(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("OPENLOOP_MODE", parent, access, address, signed)
            self.OPENLOOP_PHI_DIRECTION = Field("OPENLOOP_PHI_DIRECTION", self, Access.RW, 0x00001000, 12, signed=False)

    class _OPENLOOP_ACCELERATION(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("OPENLOOP_ACCELERATION", parent, access, address, signed)
            self.OPENLOOP_ACCELERATION = Field("OPENLOOP_ACCELERATION", self, Access.RW, 0x000FFFFF,  0, signed=False)

    class _OPENLOOP_VELOCITY_TARGET(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("OPENLOOP_VELOCITY_TARGET", parent, access, address, signed)
            self.OPENLOOP_VELOCITY_TARGET = Field("OPENLOOP_VELOCITY_TARGET", self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _OPENLOOP_VELOCITY_ACTUAL(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("OPENLOOP_VELOCITY_ACTUAL", parent, access, address, signed)
            self.OPENLOOP_VELOCITY_ACTUAL = Field("OPENLOOP_VELOCITY_ACTUAL", self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _OPENLOOP_PHI(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("OPENLOOP_PHI", parent, access, address, signed)
            self.OPENLOOP_PHI = Field("OPENLOOP_PHI", self, Access.RW, 0x0000FFFF,  0, signed=True)

    class _UQ_UD_EXT(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("UQ_UD_EXT", parent, access, address, signed)
            self.UD_EXT = Field("UD_EXT", self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.UQ_EXT = Field("UQ_EXT", self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _ABN_DECODER_MODE(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_DECODER_MODE", parent, access, address, signed)
            self.apol = Field("apol", self, Access.RW, 0x00000001,  0, signed=False)
            self.bpol = Field("bpol", self, Access.RW, 0x00000002,  1, signed=False)
            self.npol = Field("npol", self, Access.RW, 0x00000004,  2, signed=False)
            self.use_abn_as_n = Field("use_abn_as_n", self, Access.RW, 0x00000008,  3, signed=False)
            self.cln = Field("cln", self, Access.RW, 0x00000100,  8, signed=False)
            self.direction = Field("direction", self, Access.RW, 0x00001000, 12, signed=False)

    class _ABN_DECODER_PPR(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_DECODER_PPR", parent, access, address, signed)
            self.ABN_DECODER_PPR = Field("ABN_DECODER_PPR", self, Access.RW, 0x00FFFFFF,  0, signed=False)

    class _ABN_DECODER_COUNT(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_DECODER_COUNT", parent, access, address, signed)
            self.ABN_DECODER_COUNT = Field("ABN_DECODER_COUNT", self, Access.RW, 0x00FFFFFF,  0, signed=False)

    class _ABN_DECODER_COUNT_N(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_DECODER_COUNT_N", parent, access, address, signed)
            self.ABN_DECODER_COUNT_N = Field("ABN_DECODER_COUNT_N", self, Access.RW, 0x00FFFFFF,  0, signed=False)

    class _ABN_DECODER_PHI_E_PHI_M_OFFSET(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_DECODER_PHI_E_PHI_M_OFFSET", parent, access, address, signed)
            self.ABN_DECODER_PHI_M_OFFSET = Field("ABN_DECODER_PHI_M_OFFSET", self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.ABN_DECODER_PHI_E_OFFSET = Field("ABN_DECODER_PHI_E_OFFSET", self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _ABN_DECODER_PHI_E_PHI_M(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_DECODER_PHI_E_PHI_M", parent, access, address, signed)
            self.ABN_DECODER_PHI_M = Field("ABN_DECODER_PHI_M", self, Access.R, 0x0000FFFF,  0, signed=True)
            self.ABN_DECODER_PHI_E = Field("ABN_DECODER_PHI_E", self, Access.R, 0xFFFF0000, 16, signed=True)

    class _ABN_2_DECODER_MODE(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_2_DECODER_MODE", parent, access, address, signed)
            self.apol = Field("apol", self, Access.RW, 0x00000001,  0, signed=False)
            self.bpol = Field("bpol", self, Access.RW, 0x00000002,  1, signed=False)
            self.npol = Field("npol", self, Access.RW, 0x00000004,  2, signed=False)
            self.use_abn_as_n = Field("use_abn_as_n", self, Access.RW, 0x00000008,  3, signed=False)
            self.cln = Field("cln", self, Access.RW, 0x00000100,  8, signed=False)
            self.direction = Field("direction", self, Access.RW, 0x00001000, 12, signed=False)

    class _ABN_2_DECODER_PPR(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_2_DECODER_PPR", parent, access, address, signed)
            self.ABN_2_DECODER_PPR = Field("ABN_2_DECODER_PPR", self, Access.RW, 0x00FFFFFF,  0, signed=False)

    class _ABN_2_DECODER_COUNT(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_2_DECODER_COUNT", parent, access, address, signed)
            self.ABN_2_DECODER_COUNT = Field("ABN_2_DECODER_COUNT", self, Access.RW, 0x00FFFFFF,  0, signed=False)

    class _ABN_2_DECODER_COUNT_N(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_2_DECODER_COUNT_N", parent, access, address, signed)
            self.ABN_2_DECODER_COUNT_N = Field("ABN_2_DECODER_COUNT_N", self, Access.RW, 0x00FFFFFF,  0, signed=False)

    class _ABN_2_DECODER_PHI_M_OFFSET(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_2_DECODER_PHI_M_OFFSET", parent, access, address, signed)
            self.ABN_2_DECODER_PHI_M_OFFSET = Field("ABN_2_DECODER_PHI_M_OFFSET", self, Access.RW, 0x0000FFFF,  0, signed=True)

    class _ABN_2_DECODER_PHI_M(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_2_DECODER_PHI_M", parent, access, address, signed)
            self.ABN_2_DECODER_PHI_M = Field("ABN_2_DECODER_PHI_M", self, Access.R, 0x0000FFFF,  0, signed=True)

    class _HALL_MODE(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("HALL_MODE", parent, access, address, signed)
            self.polarity = Field("polarity", self, Access.RW, 0x00000001,  0, signed=False)
            self.synchronous_PWM_sampling = Field("synchronous_PWM_sampling", self, Access.RW, 0x00000010,  4, signed=False)
            self.interpolation = Field("interpolation", self, Access.RW, 0x00000100,  8, signed=False)
            self.direction = Field("direction", self, Access.RW, 0x00001000, 12, signed=False)
            self.HALL_BLANK = Field("HALL_BLANK", self, Access.RW, 0x0FFF0000, 16, signed=False)

    class _HALL_POSITION_060_000(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("HALL_POSITION_060_000", parent, access, address, signed)
            self.HALL_POSITION_000 = Field("HALL_POSITION_000", self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.HALL_POSITION_060 = Field("HALL_POSITION_060", self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _HALL_POSITION_180_120(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("HALL_POSITION_180_120", parent, access, address, signed)
            self.HALL_POSITION_120 = Field("HALL_POSITION_120", self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.HALL_POSITION_180 = Field("HALL_POSITION_180", self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _HALL_POSITION_300_240(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("HALL_POSITION_300_240", parent, access, address, signed)
            self.HALL_POSITION_240 = Field("HALL_POSITION_240", self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.HALL_POSITION_300 = Field("HALL_POSITION_300", self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _HALL_PHI_E_PHI_M_OFFSET(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("HALL_PHI_E_PHI_M_OFFSET", parent, access, address, signed)
            self.HALL_PHI_M_OFFSET = Field("HALL_PHI_M_OFFSET", self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.HALL_PHI_E_OFFSET = Field("HALL_PHI_E_OFFSET", self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _HALL_DPHI_MAX(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("HALL_DPHI_MAX", parent, access, address, signed)
            self.HALL_DPHI_MAX = Field("HALL_DPHI_MAX", self, Access.RW, 0x0000FFFF,  0, signed=False)

    class _HALL_PHI_E_INTERPOLATED_PHI_E(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("HALL_PHI_E_INTERPOLATED_PHI_E", parent, access, address, signed)
            self.HALL_PHI_E = Field("HALL_PHI_E", self, Access.R, 0x0000FFFF,  0, signed=True)
            self.HALL_PHI_E_INTERPOLATED = Field("HALL_PHI_E_INTERPOLATED", self, Access.R, 0xFFFF0000, 16, signed=True)

    class _HALL_PHI_M(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("HALL_PHI_M", parent, access, address, signed)
            self.HALL_PHI_M = Field("HALL_PHI_M", self, Access.R, 0x0000FFFF,  0, signed=True)

    class _AENC_DECODER_MODE(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_DECODER_MODE", parent, access, address, signed)
            self.AENC_DECODER_MODE_0 = Field("AENC_DECODER_MODE_0", self, Access.RW, 0x00000001,  0, signed=False)
            self.AENC_DECODER_MODE_12 = Field("AENC_DECODER_MODE_12", self, Access.RW, 0x00001000, 12, signed=False)

    class _AENC_DECODER_N_THRESHOLD(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_DECODER_N_THRESHOLD", parent, access, address, signed)
            self.AENC_DECODER_N_THRESHOLD = Field("AENC_DECODER_N_THRESHOLD", self, Access.RW, 0x0000FFFF,  0, signed=False)

    class _AENC_DECODER_PHI_A_RAW(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_DECODER_PHI_A_RAW", parent, access, address, signed)
            self.AENC_DECODER_PHI_A_RAW = Field("AENC_DECODER_PHI_A_RAW", self, Access.R, 0x0000FFFF,  0, signed=True)

    class _AENC_DECODER_PHI_A_OFFSET(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_DECODER_PHI_A_OFFSET", parent, access, address, signed)
            self.AENC_DECODER_PHI_A_OFFSET = Field("AENC_DECODER_PHI_A_OFFSET", self, Access.RW, 0x0000FFFF,  0, signed=True)

    class _AENC_DECODER_PHI_A(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_DECODER_PHI_A", parent, access, address, signed)
            self.AENC_DECODER_PHI_A = Field("AENC_DECODER_PHI_A", self, Access.R, 0x0000FFFF,  0, signed=True)

    class _AENC_DECODER_PPR(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_DECODER_PPR", parent, access, address, signed)
            self.AENC_DECODER_PPR = Field("AENC_DECODER_PPR", self, Access.RW, 0x0000FFFF,  0, signed=True)

    class _AENC_DECODER_COUNT(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_DECODER_COUNT", parent, access, address, signed)
            self.AENC_DECODER_COUNT = Field("AENC_DECODER_COUNT", self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _AENC_DECODER_COUNT_N(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_DECODER_COUNT_N", parent, access, address, signed)
            self.AENC_DECODER_COUNT_N = Field("AENC_DECODER_COUNT_N", self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _AENC_DECODER_PHI_E_PHI_M_OFFSET(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_DECODER_PHI_E_PHI_M_OFFSET", parent, access, address, signed)
            self.AENC_DECODER_PHI_M_OFFSET = Field("AENC_DECODER_PHI_M_OFFSET", self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.AENC_DECODER_PHI_E_OFFSET = Field("AENC_DECODER_PHI_E_OFFSET", self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _AENC_DECODER_PHI_E_PHI_M(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_DECODER_PHI_E_PHI_M", parent, access, address, signed)
            self.AENC_DECODER_PHI_M = Field("AENC_DECODER_PHI_M", self, Access.R, 0x0000FFFF,  0, signed=True)
            self.AENC_DECODER_PHI_E = Field("AENC_DECODER_PHI_E", self, Access.R, 0xFFFF0000, 16, signed=True)

    class _CONFIG_DATA(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("CONFIG_DATA", parent, access, address, signed)
            self.biquad_x_a_1 = Field("biquad_x_a_1", self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _CONFIG_ADDR(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("CONFIG_ADDR", parent, access, address, signed)
            self.CONFIG_ADDR = Field("CONFIG_ADDR", self, Access.RW, 0xFFFFFFFF,  0, signed=False)

    class _VELOCITY_SELECTION(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("VELOCITY_SELECTION", parent, access, address, signed)
            self.VELOCITY_SELECTION = Field("VELOCITY_SELECTION", self, Access.RW, 0x000000FF,  0, signed=False)
            self.VELOCITY_METER_SELECTION = Field("VELOCITY_METER_SELECTION", self, Access.RW, 0x0000FF00,  8, signed=False)

    class _POSITION_SELECTION(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("POSITION_SELECTION", parent, access, address, signed)
            self.POSITION_SELECTION = Field("POSITION_SELECTION", self, Access.RW, 0x000000FF,  0, signed=False)

    class _PHI_E_SELECTION(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PHI_E_SELECTION", parent, access, address, signed)
            self.PHI_E_SELECTION = Field("PHI_E_SELECTION", self, Access.RW, 0x000000FF,  0, signed=False)

    class _PHI_E(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PHI_E", parent, access, address, signed)
            self.PHI_E = Field("PHI_E", self, Access.R, 0x0000FFFF,  0, signed=True)

    class _PID_FLUX_P_FLUX_I(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_FLUX_P_FLUX_I", parent, access, address, signed)
            self.PID_FLUX_I = Field("PID_FLUX_I", self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.PID_FLUX_P = Field("PID_FLUX_P", self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _PID_TORQUE_P_TORQUE_I(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_TORQUE_P_TORQUE_I", parent, access, address, signed)
            self.PID_TORQUE_I = Field("PID_TORQUE_I", self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.PID_TORQUE_P = Field("PID_TORQUE_P", self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _PID_VELOCITY_P_VELOCITY_I(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_VELOCITY_P_VELOCITY_I", parent, access, address, signed)
            self.PID_VELOCITY_I = Field("PID_VELOCITY_I", self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.PID_VELOCITY_P = Field("PID_VELOCITY_P", self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _PID_POSITION_P_POSITION_I(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_POSITION_P_POSITION_I", parent, access, address, signed)
            self.PID_POSITION_I = Field("PID_POSITION_I", self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.PID_POSITION_P = Field("PID_POSITION_P", self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _PIDOUT_UQ_UD_LIMITS(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PIDOUT_UQ_UD_LIMITS", parent, access, address, signed)
            self.PIDOUT_UQ_UD_LIMITS = Field("PIDOUT_UQ_UD_LIMITS", self, Access.RW, 0x0000FFFF,  0, signed=False)

    class _PID_TORQUE_FLUX_LIMITS(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_TORQUE_FLUX_LIMITS", parent, access, address, signed)
            self.PID_TORQUE_FLUX_LIMITS = Field("PID_TORQUE_FLUX_LIMITS", self, Access.RW, 0x0000FFFF,  0, signed=False)

    class _PID_VELOCITY_LIMIT(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_VELOCITY_LIMIT", parent, access, address, signed)
            self.PID_VELOCITY_LIMIT = Field("PID_VELOCITY_LIMIT", self, Access.RW, 0xFFFFFFFF,  0, signed=False)

    class _PID_POSITION_LIMIT_LOW(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_POSITION_LIMIT_LOW", parent, access, address, signed)
            self.PID_POSITION_LIMIT_LOW = Field("PID_POSITION_LIMIT_LOW", self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _PID_POSITION_LIMIT_HIGH(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_POSITION_LIMIT_HIGH", parent, access, address, signed)
            self.PID_POSITION_LIMIT_HIGH = Field("PID_POSITION_LIMIT_HIGH", self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _MODE_RAMP_MODE_MOTION(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("MODE_RAMP_MODE_MOTION", parent, access, address, signed)
            self.MODE_MOTION = Field("MODE_MOTION", self, Access.RW, 0x000000FF,  0, signed=False)
            self.MODE_RAMP = Field("MODE_RAMP", self, Access.RW, 0x0000FF00,  8, signed=False)
            self.MODE_FF = Field("MODE_FF", self, Access.RW, 0x00FF0000, 16, signed=False)
            self.MODE_PID_SMPL = Field("MODE_PID_SMPL", self, Access.RW, 0x7F000000, 24, signed=False)
            self.MODE_PID_TYPE = Field("MODE_PID_TYPE", self, Access.RW, 0x80000000, 31, signed=False)

    class _PID_TORQUE_FLUX_TARGET(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_TORQUE_FLUX_TARGET", parent, access, address, signed)
            self.PID_FLUX_TARGET = Field("PID_FLUX_TARGET", self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.PID_TORQUE_TARGET = Field("PID_TORQUE_TARGET", self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _PID_TORQUE_FLUX_OFFSET(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_TORQUE_FLUX_OFFSET", parent, access, address, signed)
            self.PID_FLUX_OFFSET = Field("PID_FLUX_OFFSET", self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.PID_TORQUE_OFFSET = Field("PID_TORQUE_OFFSET", self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _PID_VELOCITY_TARGET(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_VELOCITY_TARGET", parent, access, address, signed)
            self.PID_VELOCITY_TARGET = Field("PID_VELOCITY_TARGET", self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _PID_VELOCITY_OFFSET(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_VELOCITY_OFFSET", parent, access, address, signed)
            self.PID_VELOCITY_OFFSET = Field("PID_VELOCITY_OFFSET", self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _PID_POSITION_TARGET(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_POSITION_TARGET", parent, access, address, signed)
            self.PID_POSITION_TARGET = Field("PID_POSITION_TARGET", self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _PID_TORQUE_FLUX_ACTUAL(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_TORQUE_FLUX_ACTUAL", parent, access, address, signed)
            self.PID_FLUX_ACTUAL = Field("PID_FLUX_ACTUAL", self, Access.R, 0x0000FFFF,  0, signed=True)
            self.PID_TORQUE_ACTUAL = Field("PID_TORQUE_ACTUAL", self, Access.R, 0xFFFF0000, 16, signed=True)

    class _PID_VELOCITY_ACTUAL(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_VELOCITY_ACTUAL", parent, access, address, signed)
            self.PID_VELOCITY_ACTUAL = Field("PID_VELOCITY_ACTUAL", self, Access.R, 0xFFFFFFFF,  0, signed=True)

    class _PID_POSITION_ACTUAL(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_POSITION_ACTUAL", parent, access, address, signed)
            self.PID_POSITION_ACTUAL = Field("PID_POSITION_ACTUAL", self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _PID_ERROR_DATA(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_ERROR_DATA", parent, access, address, signed)
            self.PID_TORQUE_ERROR = Field("PID_TORQUE_ERROR", self, Access.R, 0xFFFFFFFF,  0, signed=True)

    class _PID_ERROR_ADDR(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_ERROR_ADDR", parent, access, address, signed)
            self.PID_ERROR_ADDR = Field("PID_ERROR_ADDR", self, Access.RW, 0x000000FF,  0, signed=False)

    class _INTERIM_DATA(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("INTERIM_DATA", parent, access, address, signed)
            self.PIDIN_TARGET_TORQUE = Field("PIDIN_TARGET_TORQUE", self, Access.R, 0xFFFFFFFF,  0, signed=True)

    class _INTERIM_ADDR(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("INTERIM_ADDR", parent, access, address, signed)
            self.INTERIM_ADDR = Field("INTERIM_ADDR", self, Access.RW, 0x000000FF,  0, signed=False)

    class _WATCHDOG_CFG(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("WATCHDOG_CFG", parent, access, address, signed)
            self.WATCHDOG_CFG = Field("WATCHDOG_CFG", self, Access.RW, 0x00000003,  0, signed=False)

    class _ADC_VM_LIMITS(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_VM_LIMITS", parent, access, address, signed)
            self.ADC_VM_LIMIT_LOW = Field("ADC_VM_LIMIT_LOW", self, Access.RW, 0x0000FFFF,  0, signed=False)
            self.ADC_VM_LIMIT_HIGH = Field("ADC_VM_LIMIT_HIGH", self, Access.RW, 0xFFFF0000, 16, signed=False)

    class _TMC4671_INPUTS_RAW(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("TMC4671_INPUTS_RAW", parent, access, address, signed)
            self.A_of_ABN_RAW = Field("A_of_ABN_RAW", self, Access.R, 0x00000001,  0, signed=False)
            self.B_of_ABN_RAW = Field("B_of_ABN_RAW", self, Access.R, 0x00000002,  1, signed=False)
            self.N_of_ABN_RAW = Field("N_of_ABN_RAW", self, Access.R, 0x00000004,  2, signed=False)
            self.A_of_ABN_2_RAW = Field("A_of_ABN_2_RAW", self, Access.R, 0x00000010,  4, signed=False)
            self.B_of_ABN_2_RAW = Field("B_of_ABN_2_RAW", self, Access.R, 0x00000020,  5, signed=False)
            self.N_of_ABN_2_RAW = Field("N_of_ABN_2_RAW", self, Access.R, 0x00000040,  6, signed=False)
            self.HALL_UX_of_HALL_RAW = Field("HALL_UX_of_HALL_RAW", self, Access.R, 0x00000100,  8, signed=False)
            self.HALL_V_of_HALL_RAW = Field("HALL_V_of_HALL_RAW", self, Access.R, 0x00000200,  9, signed=False)
            self.HALL_WY_of_HALL_RAW = Field("HALL_WY_of_HALL_RAW", self, Access.R, 0x00000400, 10, signed=False)
            self.REF_SW_R_RAW = Field("REF_SW_R_RAW", self, Access.R, 0x00001000, 12, signed=False)
            self.REF_SW_H_RAW = Field("REF_SW_H_RAW", self, Access.R, 0x00002000, 13, signed=False)
            self.REF_SW_L_RAW = Field("REF_SW_L_RAW", self, Access.R, 0x00004000, 14, signed=False)
            self.ENABLE_IN_RAW = Field("ENABLE_IN_RAW", self, Access.R, 0x00008000, 15, signed=False)
            self.STP_of_DIRSTP_RAW = Field("STP_of_DIRSTP_RAW", self, Access.R, 0x00010000, 16, signed=False)
            self.DIR_of_DIRSTP_RAW = Field("DIR_of_DIRSTP_RAW", self, Access.R, 0x00020000, 17, signed=False)
            self.PWM_IN_RAW = Field("PWM_IN_RAW", self, Access.R, 0x00040000, 18, signed=False)
            self.HALL_UX_FILT = Field("HALL_UX_FILT", self, Access.R, 0x00100000, 20, signed=False)
            self.HALL_V_FILT = Field("HALL_V_FILT", self, Access.R, 0x00200000, 21, signed=False)
            self.HALL_WY_FILT = Field("HALL_WY_FILT", self, Access.R, 0x00400000, 22, signed=False)
            self.PWM_IDLE_L_RAW = Field("PWM_IDLE_L_RAW", self, Access.R, 0x10000000, 28, signed=False)
            self.PWM_IDLE_H_RAW = Field("PWM_IDLE_H_RAW", self, Access.R, 0x20000000, 29, signed=False)

    class _TMC4671_OUTPUTS_RAW(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("TMC4671_OUTPUTS_RAW", parent, access, address, signed)
            self.TMC4671_OUTPUTS_RAW_0 = Field("TMC4671_OUTPUTS_RAW_0", self, Access.R, 0x00000001,  0, signed=False)
            self.TMC4671_OUTPUTS_RAW_1 = Field("TMC4671_OUTPUTS_RAW_1", self, Access.R, 0x00000002,  1, signed=False)
            self.TMC4671_OUTPUTS_RAW_2 = Field("TMC4671_OUTPUTS_RAW_2", self, Access.R, 0x00000004,  2, signed=False)
            self.TMC4671_OUTPUTS_RAW_3 = Field("TMC4671_OUTPUTS_RAW_3", self, Access.R, 0x00000008,  3, signed=False)
            self.TMC4671_OUTPUTS_RAW_4 = Field("TMC4671_OUTPUTS_RAW_4", self, Access.R, 0x00000010,  4, signed=False)
            self.TMC4671_OUTPUTS_RAW_5 = Field("TMC4671_OUTPUTS_RAW_5", self, Access.R, 0x00000020,  5, signed=False)
            self.TMC4671_OUTPUTS_RAW_6 = Field("TMC4671_OUTPUTS_RAW_6", self, Access.R, 0x00000040,  6, signed=False)
            self.TMC4671_OUTPUTS_RAW_7 = Field("TMC4671_OUTPUTS_RAW_7", self, Access.R, 0x00000080,  7, signed=False)

    class _STEP_WIDTH(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("STEP_WIDTH", parent, access, address, signed)
            self.STEP_WIDTH = Field("STEP_WIDTH", self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _UART_BPS(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("UART_BPS", parent, access, address, signed)
            self.UART_BPS = Field("UART_BPS", self, Access.RW, 0x03FFFFFF,  0, signed=False)

    class _UART_ADDRS(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("UART_ADDRS", parent, access, address, signed)
            self.ADDR_A = Field("ADDR_A", self, Access.RW, 0x000000FF,  0, signed=False)
            self.ADDR_B = Field("ADDR_B", self, Access.RW, 0x0000FF00,  8, signed=False)
            self.ADDR_C = Field("ADDR_C", self, Access.RW, 0x00FF0000, 16, signed=False)
            self.ADDR_D = Field("ADDR_D", self, Access.RW, 0xFF000000, 24, signed=False)

    class _GPIO_dsADCI_CONFIG(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("GPIO_dsADCI_CONFIG", parent, access, address, signed)
            self.GPIO_dsADCI_CONFIG_0 = Field("GPIO_dsADCI_CONFIG_0", self, Access.RW, 0x00000001,  0, signed=False)
            self.GPIO_dsADCI_CONFIG_1 = Field("GPIO_dsADCI_CONFIG_1", self, Access.RW, 0x00000002,  1, signed=False)
            self.GPIO_dsADCI_CONFIG_2 = Field("GPIO_dsADCI_CONFIG_2", self, Access.RW, 0x00000004,  2, signed=False)
            self.GPIO_dsADCI_CONFIG_3 = Field("GPIO_dsADCI_CONFIG_3", self, Access.RW, 0x00000008,  3, signed=False)
            self.GPIO_dsADCI_CONFIG_4 = Field("GPIO_dsADCI_CONFIG_4", self, Access.RW, 0x00000010,  4, signed=False)
            self.GPIO_dsADCI_CONFIG_5 = Field("GPIO_dsADCI_CONFIG_5", self, Access.RW, 0x00000020,  5, signed=False)
            self.GPIO_dsADCI_CONFIG_6 = Field("GPIO_dsADCI_CONFIG_6", self, Access.RW, 0x00000040,  6, signed=False)
            self.GPO = Field("GPO", self, Access.RW, 0x00FF0000, 16, signed=False)
            self.GPI = Field("GPI", self, Access.R, 0xFF000000, 24, signed=False)

    class _STATUS_FLAGS(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("STATUS_FLAGS", parent, access, address, signed)
            self.STATUS_FLAGS_0 = Field("STATUS_FLAGS_0", self, Access.RW, 0x00000001,  0, signed=False)
            self.STATUS_FLAGS_1 = Field("STATUS_FLAGS_1", self, Access.RW, 0x00000002,  1, signed=False)
            self.STATUS_FLAGS_2 = Field("STATUS_FLAGS_2", self, Access.RW, 0x00000004,  2, signed=False)
            self.STATUS_FLAGS_3 = Field("STATUS_FLAGS_3", self, Access.RW, 0x00000008,  3, signed=False)
            self.STATUS_FLAGS_4 = Field("STATUS_FLAGS_4", self, Access.RW, 0x00000010,  4, signed=False)
            self.STATUS_FLAGS_5 = Field("STATUS_FLAGS_5", self, Access.RW, 0x00000020,  5, signed=False)
            self.STATUS_FLAGS_6 = Field("STATUS_FLAGS_6", self, Access.RW, 0x00000040,  6, signed=False)
            self.STATUS_FLAGS_7 = Field("STATUS_FLAGS_7", self, Access.RW, 0x00000080,  7, signed=False)
            self.STATUS_FLAGS_8 = Field("STATUS_FLAGS_8", self, Access.RW, 0x00000100,  8, signed=False)
            self.STATUS_FLAGS_9 = Field("STATUS_FLAGS_9", self, Access.RW, 0x00000200,  9, signed=False)
            self.STATUS_FLAGS_10 = Field("STATUS_FLAGS_10", self, Access.RW, 0x00000400, 10, signed=False)
            self.STATUS_FLAGS_11 = Field("STATUS_FLAGS_11", self, Access.RW, 0x00000800, 11, signed=False)
            self.STATUS_FLAGS_12 = Field("STATUS_FLAGS_12", self, Access.RW, 0x00001000, 12, signed=False)
            self.STATUS_FLAGS_13 = Field("STATUS_FLAGS_13", self, Access.RW, 0x00002000, 13, signed=False)
            self.STATUS_FLAGS_14 = Field("STATUS_FLAGS_14", self, Access.RW, 0x00004000, 14, signed=False)
            self.STATUS_FLAGS_15 = Field("STATUS_FLAGS_15", self, Access.RW, 0x00008000, 15, signed=False)
            self.STATUS_FLAGS_16 = Field("STATUS_FLAGS_16", self, Access.RW, 0x00010000, 16, signed=False)
            self.STATUS_FLAGS_17 = Field("STATUS_FLAGS_17", self, Access.RW, 0x00020000, 17, signed=False)
            self.STATUS_FLAGS_18 = Field("STATUS_FLAGS_18", self, Access.RW, 0x00040000, 18, signed=False)
            self.STATUS_FLAGS_19 = Field("STATUS_FLAGS_19", self, Access.RW, 0x00080000, 19, signed=False)
            self.STATUS_FLAGS_20 = Field("STATUS_FLAGS_20", self, Access.RW, 0x00100000, 20, signed=False)
            self.STATUS_FLAGS_21 = Field("STATUS_FLAGS_21", self, Access.RW, 0x00200000, 21, signed=False)
            self.STATUS_FLAGS_22 = Field("STATUS_FLAGS_22", self, Access.RW, 0x00400000, 22, signed=False)
            self.STATUS_FLAGS_23 = Field("STATUS_FLAGS_23", self, Access.RW, 0x00800000, 23, signed=False)
            self.STATUS_FLAGS_24 = Field("STATUS_FLAGS_24", self, Access.RW, 0x01000000, 24, signed=False)
            self.STATUS_FLAGS_25 = Field("STATUS_FLAGS_25", self, Access.RW, 0x02000000, 25, signed=False)
            self.STATUS_FLAGS_26 = Field("STATUS_FLAGS_26", self, Access.RW, 0x04000000, 26, signed=False)
            self.STATUS_FLAGS_27 = Field("STATUS_FLAGS_27", self, Access.RW, 0x08000000, 27, signed=False)
            self.STATUS_FLAGS_28 = Field("STATUS_FLAGS_28", self, Access.RW, 0x10000000, 28, signed=False)
            self.STATUS_FLAGS_29 = Field("STATUS_FLAGS_29", self, Access.RW, 0x20000000, 29, signed=False)
            self.STATUS_FLAGS_30 = Field("STATUS_FLAGS_30", self, Access.RW, 0x40000000, 30, signed=False)
            self.STATUS_FLAGS_31 = Field("STATUS_FLAGS_31", self, Access.RW, 0x80000000, 31, signed=False)

    class _STATUS_MASK(Register):

        def __init__(self, parent, access, address, signed):
            super().__init__("STATUS_MASK", parent, access, address, signed)
            self.WARNING_MASK = Field("WARNING_MASK", self, Access.RW, 0xFFFFFFFF,  0, signed=False)

    def __init__(self):
        super().__init__("ALL_REGISTERS")
        self.CHIPINFO_DATA = self._CHIPINFO_DATA(self, Access.R, 0x0000, False)
        self.CHIPINFO_ADDR = self._CHIPINFO_ADDR(self, Access.RW, 0x0001, False)
        self.ADC_RAW_DATA = self._ADC_RAW_DATA(self, Access.R, 0x0002, False)
        self.ADC_RAW_ADDR = self._ADC_RAW_ADDR(self, Access.RW, 0x0003, False)
        self.dsADC_MCFG_B_MCFG_A = self._dsADC_MCFG_B_MCFG_A(self, Access.RW, 0x0004, False)
        self.dsADC_MCLK_A = self._dsADC_MCLK_A(self, Access.RW, 0x0005, False)
        self.dsADC_MCLK_B = self._dsADC_MCLK_B(self, Access.RW, 0x0006, False)
        self.dsADC_MDEC_B_MDEC_A = self._dsADC_MDEC_B_MDEC_A(self, Access.RW, 0x0007, False)
        self.ADC_I1_SCALE_OFFSET = self._ADC_I1_SCALE_OFFSET(self, Access.RW, 0x0008, False)
        self.ADC_I0_SCALE_OFFSET = self._ADC_I0_SCALE_OFFSET(self, Access.RW, 0x0009, False)
        self.ADC_I_SELECT = self._ADC_I_SELECT(self, Access.RW, 0x000A, False)
        self.ADC_I1_I0_EXT = self._ADC_I1_I0_EXT(self, Access.RW, 0x000B, False)
        self.DS_ANALOG_INPUT_STAGE_CFG = self._DS_ANALOG_INPUT_STAGE_CFG(self, Access.RW, 0x000C, False)
        self.AENC_0_SCALE_OFFSET = self._AENC_0_SCALE_OFFSET(self, Access.RW, 0x000D, False)
        self.AENC_1_SCALE_OFFSET = self._AENC_1_SCALE_OFFSET(self, Access.RW, 0x000E, False)
        self.AENC_2_SCALE_OFFSET = self._AENC_2_SCALE_OFFSET(self, Access.RW, 0x000F, False)
        self.AENC_SELECT = self._AENC_SELECT(self, Access.RW, 0x0011, False)
        self.ADC_IWY_IUX = self._ADC_IWY_IUX(self, Access.R, 0x0012, False)
        self.ADC_IV = self._ADC_IV(self, Access.R, 0x0013, True)
        self.AENC_WY_UX = self._AENC_WY_UX(self, Access.R, 0x0015, False)
        self.AENC_VN = self._AENC_VN(self, Access.R, 0x0016, True)
        self.PWM_POLARITIES = self._PWM_POLARITIES(self, Access.RW, 0x0017, False)
        self.PWM_MAXCNT = self._PWM_MAXCNT(self, Access.RW, 0x0018, False)
        self.PWM_BBM_H_BBM_L = self._PWM_BBM_H_BBM_L(self, Access.RW, 0x0019, False)
        self.PWM_SV_CHOP = self._PWM_SV_CHOP(self, Access.RW, 0x001A, False)
        self.MOTOR_TYPE_N_POLE_PAIRS = self._MOTOR_TYPE_N_POLE_PAIRS(self, Access.RW, 0x001B, False)
        self.PHI_E_EXT = self._PHI_E_EXT(self, Access.RW, 0x001C, True)
        self.OPENLOOP_MODE = self._OPENLOOP_MODE(self, Access.RW, 0x001F, False)
        self.OPENLOOP_ACCELERATION = self._OPENLOOP_ACCELERATION(self, Access.RW, 0x0020, False)
        self.OPENLOOP_VELOCITY_TARGET = self._OPENLOOP_VELOCITY_TARGET(self, Access.RW, 0x0021, True)
        self.OPENLOOP_VELOCITY_ACTUAL = self._OPENLOOP_VELOCITY_ACTUAL(self, Access.RW, 0x0022, True)
        self.OPENLOOP_PHI = self._OPENLOOP_PHI(self, Access.RW, 0x0023, True)
        self.UQ_UD_EXT = self._UQ_UD_EXT(self, Access.RW, 0x0024, False)
        self.ABN_DECODER_MODE = self._ABN_DECODER_MODE(self, Access.RW, 0x0025, False)
        self.ABN_DECODER_PPR = self._ABN_DECODER_PPR(self, Access.RW, 0x0026, False)
        self.ABN_DECODER_COUNT = self._ABN_DECODER_COUNT(self, Access.RW, 0x0027, False)
        self.ABN_DECODER_COUNT_N = self._ABN_DECODER_COUNT_N(self, Access.RW, 0x0028, False)
        self.ABN_DECODER_PHI_E_PHI_M_OFFSET = self._ABN_DECODER_PHI_E_PHI_M_OFFSET(self, Access.RW, 0x0029, False)
        self.ABN_DECODER_PHI_E_PHI_M = self._ABN_DECODER_PHI_E_PHI_M(self, Access.R, 0x002A, False)
        self.ABN_2_DECODER_MODE = self._ABN_2_DECODER_MODE(self, Access.RW, 0x002C, False)
        self.ABN_2_DECODER_PPR = self._ABN_2_DECODER_PPR(self, Access.RW, 0x002D, False)
        self.ABN_2_DECODER_COUNT = self._ABN_2_DECODER_COUNT(self, Access.RW, 0x002E, False)
        self.ABN_2_DECODER_COUNT_N = self._ABN_2_DECODER_COUNT_N(self, Access.RW, 0x002F, False)
        self.ABN_2_DECODER_PHI_M_OFFSET = self._ABN_2_DECODER_PHI_M_OFFSET(self, Access.RW, 0x0030, True)
        self.ABN_2_DECODER_PHI_M = self._ABN_2_DECODER_PHI_M(self, Access.R, 0x0031, True)
        self.HALL_MODE = self._HALL_MODE(self, Access.RW, 0x0033, False)
        self.HALL_POSITION_060_000 = self._HALL_POSITION_060_000(self, Access.RW, 0x0034, False)
        self.HALL_POSITION_180_120 = self._HALL_POSITION_180_120(self, Access.RW, 0x0035, False)
        self.HALL_POSITION_300_240 = self._HALL_POSITION_300_240(self, Access.RW, 0x0036, False)
        self.HALL_PHI_E_PHI_M_OFFSET = self._HALL_PHI_E_PHI_M_OFFSET(self, Access.RW, 0x0037, False)
        self.HALL_DPHI_MAX = self._HALL_DPHI_MAX(self, Access.RW, 0x0038, False)
        self.HALL_PHI_E_INTERPOLATED_PHI_E = self._HALL_PHI_E_INTERPOLATED_PHI_E(self, Access.R, 0x0039, False)
        self.HALL_PHI_M = self._HALL_PHI_M(self, Access.R, 0x003A, True)
        self.AENC_DECODER_MODE = self._AENC_DECODER_MODE(self, Access.RW, 0x003B, False)
        self.AENC_DECODER_N_THRESHOLD = self._AENC_DECODER_N_THRESHOLD(self, Access.RW, 0x003C, False)
        self.AENC_DECODER_PHI_A_RAW = self._AENC_DECODER_PHI_A_RAW(self, Access.R, 0x003D, True)
        self.AENC_DECODER_PHI_A_OFFSET = self._AENC_DECODER_PHI_A_OFFSET(self, Access.RW, 0x003E, True)
        self.AENC_DECODER_PHI_A = self._AENC_DECODER_PHI_A(self, Access.R, 0x003F, True)
        self.AENC_DECODER_PPR = self._AENC_DECODER_PPR(self, Access.RW, 0x0040, True)
        self.AENC_DECODER_COUNT = self._AENC_DECODER_COUNT(self, Access.RW, 0x0041, True)
        self.AENC_DECODER_COUNT_N = self._AENC_DECODER_COUNT_N(self, Access.RW, 0x0042, True)
        self.AENC_DECODER_PHI_E_PHI_M_OFFSET = self._AENC_DECODER_PHI_E_PHI_M_OFFSET(self, Access.RW, 0x0045, False)
        self.AENC_DECODER_PHI_E_PHI_M = self._AENC_DECODER_PHI_E_PHI_M(self, Access.R, 0x0046, False)
        self.CONFIG_DATA = self._CONFIG_DATA(self, Access.RW, 0x004D, True)
        self.CONFIG_ADDR = self._CONFIG_ADDR(self, Access.RW, 0x004E, False)
        self.VELOCITY_SELECTION = self._VELOCITY_SELECTION(self, Access.RW, 0x0050, False)
        self.POSITION_SELECTION = self._POSITION_SELECTION(self, Access.RW, 0x0051, False)
        self.PHI_E_SELECTION = self._PHI_E_SELECTION(self, Access.RW, 0x0052, False)
        self.PHI_E = self._PHI_E(self, Access.R, 0x0053, True)
        self.PID_FLUX_P_FLUX_I = self._PID_FLUX_P_FLUX_I(self, Access.RW, 0x0054, False)
        self.PID_TORQUE_P_TORQUE_I = self._PID_TORQUE_P_TORQUE_I(self, Access.RW, 0x0056, False)
        self.PID_VELOCITY_P_VELOCITY_I = self._PID_VELOCITY_P_VELOCITY_I(self, Access.RW, 0x0058, False)
        self.PID_POSITION_P_POSITION_I = self._PID_POSITION_P_POSITION_I(self, Access.RW, 0x005A, False)
        self.PIDOUT_UQ_UD_LIMITS = self._PIDOUT_UQ_UD_LIMITS(self, Access.RW, 0x005D, False)
        self.PID_TORQUE_FLUX_LIMITS = self._PID_TORQUE_FLUX_LIMITS(self, Access.RW, 0x005E, False)
        self.PID_VELOCITY_LIMIT = self._PID_VELOCITY_LIMIT(self, Access.RW, 0x0060, False)
        self.PID_POSITION_LIMIT_LOW = self._PID_POSITION_LIMIT_LOW(self, Access.RW, 0x0061, True)
        self.PID_POSITION_LIMIT_HIGH = self._PID_POSITION_LIMIT_HIGH(self, Access.RW, 0x0062, True)
        self.MODE_RAMP_MODE_MOTION = self._MODE_RAMP_MODE_MOTION(self, Access.RW, 0x0063, False)
        self.PID_TORQUE_FLUX_TARGET = self._PID_TORQUE_FLUX_TARGET(self, Access.RW, 0x0064, False)
        self.PID_TORQUE_FLUX_OFFSET = self._PID_TORQUE_FLUX_OFFSET(self, Access.RW, 0x0065, False)
        self.PID_VELOCITY_TARGET = self._PID_VELOCITY_TARGET(self, Access.RW, 0x0066, True)
        self.PID_VELOCITY_OFFSET = self._PID_VELOCITY_OFFSET(self, Access.RW, 0x0067, True)
        self.PID_POSITION_TARGET = self._PID_POSITION_TARGET(self, Access.RW, 0x0068, True)
        self.PID_TORQUE_FLUX_ACTUAL = self._PID_TORQUE_FLUX_ACTUAL(self, Access.R, 0x0069, False)
        self.PID_VELOCITY_ACTUAL = self._PID_VELOCITY_ACTUAL(self, Access.R, 0x006A, True)
        self.PID_POSITION_ACTUAL = self._PID_POSITION_ACTUAL(self, Access.RW, 0x006B, True)
        self.PID_ERROR_DATA = self._PID_ERROR_DATA(self, Access.R, 0x006C, True)
        self.PID_ERROR_ADDR = self._PID_ERROR_ADDR(self, Access.RW, 0x006D, False)
        self.INTERIM_DATA = self._INTERIM_DATA(self, Access.R, 0x006E, True)
        self.INTERIM_ADDR = self._INTERIM_ADDR(self, Access.RW, 0x006F, False)
        self.WATCHDOG_CFG = self._WATCHDOG_CFG(self, Access.RW, 0x0074, False)
        self.ADC_VM_LIMITS = self._ADC_VM_LIMITS(self, Access.RW, 0x0075, False)
        self.TMC4671_INPUTS_RAW = self._TMC4671_INPUTS_RAW(self, Access.R, 0x0076, False)
        self.TMC4671_OUTPUTS_RAW = self._TMC4671_OUTPUTS_RAW(self, Access.R, 0x0077, False)
        self.STEP_WIDTH = self._STEP_WIDTH(self, Access.RW, 0x0078, True)
        self.UART_BPS = self._UART_BPS(self, Access.RW, 0x0079, False)
        self.UART_ADDRS = self._UART_ADDRS(self, Access.RW, 0x007A, False)
        self.GPIO_dsADCI_CONFIG = self._GPIO_dsADCI_CONFIG(self, Access.RW, 0x007B, False)
        self.STATUS_FLAGS = self._STATUS_FLAGS(self, Access.RW, 0x007C, False)
        self.STATUS_MASK = self._STATUS_MASK(self, Access.RW, 0x007D, False)

