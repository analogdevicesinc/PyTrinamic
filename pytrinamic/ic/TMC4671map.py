################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

import typing

from ..ic import Access, RegisterGroup, Choice, Field, Register

class TMC4671Map:

    def __init__(self):
        self.ALL_REGISTERS = _ALL_REGISTERS()

_CHIP_INFO_ADDRESS_FIELD_CHOICES = typing.TypedDict("_CHIP_INFO_ADDRESS_FIELD_CHOICES", {
    "SI_TYPE": Choice,
    "SI_VERSION": Choice,
    "SI_DATE": Choice,
    "SI_TIME": Choice,
    "SI_VARIANT": Choice,
    "SI_BUILD": Choice,
})

_ADC_RAW_ADDR_FIELD_CHOICES = typing.TypedDict("_ADC_RAW_ADDR_FIELD_CHOICES", {
    "ADC_I1_RAW & ADC_I0_RAW": Choice,
    "ADC_AGPI_A_RAW & ADC_VM_RAW": Choice,
    "ADC_AENC_UX_RAW & ADC_AGPI_B_RAW": Choice,
    "ADC_AENC_WY_RAW & ADC_AENC_VN_RAW": Choice,
})

_cfg_dsmodulator_a_FIELD_CHOICES = typing.TypedDict("_cfg_dsmodulator_a_FIELD_CHOICES", {
    "int. dsMOD": Choice,
    "ext. MCLK input": Choice,
    "ext. MCLK output": Choice,
    "ext. CMP": Choice,
})

_cfg_dsmodulator_b_FIELD_CHOICES = typing.TypedDict("_cfg_dsmodulator_b_FIELD_CHOICES", {
    "int. dsMOD": Choice,
    "ext. MCLK input": Choice,
    "ext. MCLK output": Choice,
    "ext. CMP": Choice,
})

_ADC_I0_SELECT_FIELD_CHOICES = typing.TypedDict("_ADC_I0_SELECT_FIELD_CHOICES", {
    "ADCSD_I0_RAW (sigma delta ADC)": Choice,
    "ADCSD_I1_RAW (sigma delta ADC)": Choice,
    "ADC_I0_EXT (from register)": Choice,
    "ADC_I1_EXT (from register)": Choice,
})

_ADC_I1_SELECT_FIELD_CHOICES = typing.TypedDict("_ADC_I1_SELECT_FIELD_CHOICES", {
    "ADCSD_I0_RAW (sigma delta ADC)": Choice,
    "ADCSD_I1_RAW (sigma delta ADC)": Choice,
    "ADC_I0_EXT (from register)": Choice,
    "ADC_I1_EXT (from register)": Choice,
})

_ADC_I_UX_SELECT_FIELD_CHOICES = typing.TypedDict("_ADC_I_UX_SELECT_FIELD_CHOICES", {
    "UX = ADC_I0 (default)": Choice,
    "UX = ADC_I1": Choice,
    "UX = ADC_I2": Choice,
})

_ADC_I_V_SELECT_FIELD_CHOICES = typing.TypedDict("_ADC_I_V_SELECT_FIELD_CHOICES", {
    "V = ADC_I0": Choice,
    "V = ADC_I1 (default)": Choice,
    "V = ADC_I2": Choice,
})

_ADC_I_WY_SELECT_FIELD_CHOICES = typing.TypedDict("_ADC_I_WY_SELECT_FIELD_CHOICES", {
    "WY = ADC_I0": Choice,
    "WY = ADC_I1": Choice,
    "WY = ADC_I2 (default)": Choice,
})

_ADC_I0_FIELD_CHOICES = typing.TypedDict("_ADC_I0_FIELD_CHOICES", {
    "INP vs. INN": Choice,
    "GND vs. INN": Choice,
    "VDD/4": Choice,
    "3*VDD/4": Choice,
    "INP vs. GND": Choice,
    "VDD/2": Choice,
})

_ADC_I1_FIELD_CHOICES = typing.TypedDict("_ADC_I1_FIELD_CHOICES", {
    "INP vs. INN": Choice,
    "GND vs. INN": Choice,
    "VDD/4": Choice,
    "3*VDD/4": Choice,
    "INP vs. GND": Choice,
    "VDD/2": Choice,
})

_ADC_VM_FIELD_CHOICES = typing.TypedDict("_ADC_VM_FIELD_CHOICES", {
    "INP vs. INN": Choice,
    "GND vs. INN": Choice,
    "VDD/4": Choice,
    "3*VDD/4": Choice,
    "INP vs. GND": Choice,
    "VDD/2": Choice,
})

_ADC_AGPI_A_FIELD_CHOICES = typing.TypedDict("_ADC_AGPI_A_FIELD_CHOICES", {
    "INP vs. INN": Choice,
    "GND vs. INN": Choice,
    "VDD/4": Choice,
    "3*VDD/4": Choice,
    "INP vs. GND": Choice,
    "VDD/2": Choice,
})

_ADC_AGPI_B_FIELD_CHOICES = typing.TypedDict("_ADC_AGPI_B_FIELD_CHOICES", {
    "INP vs. INN": Choice,
    "GND vs. INN": Choice,
    "VDD/4": Choice,
    "3*VDD/4": Choice,
    "INP vs. GND": Choice,
    "VDD/2": Choice,
})

_ADC_AENC_UX_FIELD_CHOICES = typing.TypedDict("_ADC_AENC_UX_FIELD_CHOICES", {
    "INP vs. INN": Choice,
    "GND vs. INN": Choice,
    "VDD/4": Choice,
    "3*VDD/4": Choice,
    "INP vs. GND": Choice,
    "VDD/2": Choice,
})

_ADC_AENC_VN_FIELD_CHOICES = typing.TypedDict("_ADC_AENC_VN_FIELD_CHOICES", {
    "INP vs. INN": Choice,
    "GND vs. INN": Choice,
    "VDD/4": Choice,
    "3*VDD/4": Choice,
    "INP vs. GND": Choice,
    "VDD/2": Choice,
})

_ADC_AENC_WY_FIELD_CHOICES = typing.TypedDict("_ADC_AENC_WY_FIELD_CHOICES", {
    "INP vs. INN": Choice,
    "GND vs. INN": Choice,
    "VDD/4": Choice,
    "3*VDD/4": Choice,
    "INP vs. GND": Choice,
    "VDD/2": Choice,
})

_AENC_0_SELECT_FIELD_CHOICES = typing.TypedDict("_AENC_0_SELECT_FIELD_CHOICES", {
    "<AENC_UX_RAW>": Choice,
    "AENC_VN_RAW": Choice,
    "AENC_WY_RAW": Choice,
})

_AENC_1_SELECT_FIELD_CHOICES = typing.TypedDict("_AENC_1_SELECT_FIELD_CHOICES", {
    "AENC_UX_RAW": Choice,
    "<AENC_VN_RAW>": Choice,
    "AENC_WY_RAW": Choice,
})

_AENC_2_SELECT_FIELD_CHOICES = typing.TypedDict("_AENC_2_SELECT_FIELD_CHOICES", {
    "AENC_UX_RAW": Choice,
    "AENC_VN_RAW": Choice,
    "<AENC_WY_RAW>": Choice,
})

_PWM_CHOP_FIELD_CHOICES = typing.TypedDict("_PWM_CHOP_FIELD_CHOICES", {
    "off, free running": Choice,
    "off, low side permanent = ON": Choice,
    "off, high side permanent = ON": Choice,
    "low side chopper, high side off": Choice,
    "high side chopper, low side off": Choice,
    "centered PWM for FOC": Choice,
})

_MOTOR_TYPE_FIELD_CHOICES = typing.TypedDict("_MOTOR_TYPE_FIELD_CHOICES", {
    "No motor": Choice,
    "Single phase DC": Choice,
    "Two phase Stepper": Choice,
    "Three phase BLDC": Choice,
})

_CONFIG_ADDR_FIELD_CHOICES = typing.TypedDict("_CONFIG_ADDR_FIELD_CHOICES", {
    "biquad_x_a_1": Choice,
    "biquad_x_a_2": Choice,
    "biquad_x_b_0": Choice,
    "biquad_x_b_1": Choice,
    "biquad_x_b_2": Choice,
    "biquad_x_enable": Choice,
    "biquad_v_a_1": Choice,
    "biquad_v_a_2": Choice,
    "biquad_v_b_0": Choice,
    "biquad_v_b_1": Choice,
    "biquad_v_b_2": Choice,
    "biquad_v_enable": Choice,
    "biquad_t_a_1": Choice,
    "biquad_t_a_2": Choice,
    "biquad_t_b_0": Choice,
    "biquad_t_b_1": Choice,
    "biquad_t_b_2": Choice,
    "biquad_t_enable": Choice,
    "biquad_f_a_1": Choice,
    "biquad_f_a_2": Choice,
    "biquad_f_b_0": Choice,
    "biquad_f_b_1": Choice,
    "biquad_f_b_2": Choice,
    "biquad_f_enable": Choice,
    "prbs_amplitude": Choice,
    "prbs_down_sampling_ratio": Choice,
    "ref_switch_config": Choice,
    "Encoder_Init_hall_Enable": Choice,
    "SINGLE_PIN_IF_STATUS_CFG": Choice,
    "SINGLE_PIN_IF_SCALE_OFFSET": Choice,
    "ADVANCED_PI_REPRESENTATION": Choice,
})

_VELOCITY_SELECTION_FIELD_CHOICES = typing.TypedDict("_VELOCITY_SELECTION_FIELD_CHOICES", {
    "PHI_E_SELECTION": Choice,
    "phi_e_ext": Choice,
    "phi_e_openloop": Choice,
    "phi_e_abn": Choice,
    "reserved": Choice,
    "phi_e_hal": Choice,
    "phi_e_aenc": Choice,
    "phi_a_aenc": Choice,
    "phi_m_abn": Choice,
    "phi_m_abn_2": Choice,
    "phi_m_aenc": Choice,
    "phi_m_hal": Choice,
})

_VELOCITY_METER_SELECTION_FIELD_CHOICES = typing.TypedDict("_VELOCITY_METER_SELECTION_FIELD_CHOICES", {
    "default": Choice,
    "advanced": Choice,
})

_POSITION_SELECTION_FIELD_CHOICES = typing.TypedDict("_POSITION_SELECTION_FIELD_CHOICES", {
    "phi_e selected via PHI_E_SELECTION": Choice,
    "phi_e_ext": Choice,
    "phi_e_openloop": Choice,
    "phi_e_abn": Choice,
    "reserved": Choice,
    "phi_e_hal": Choice,
    "phi_e_aenc": Choice,
    "phi_a_aenc": Choice,
    "phi_m_abn": Choice,
    "phi_m_abn_2": Choice,
    "phi_m_aenc": Choice,
    "phi_m_hal": Choice,
})

_PHI_E_SELECTION_FIELD_CHOICES = typing.TypedDict("_PHI_E_SELECTION_FIELD_CHOICES", {
    "reserved": Choice,
    "phi_e_ext": Choice,
    "phi_e_openloop": Choice,
    "phi_e_abn": Choice,
    "phi_e_hal": Choice,
    "phi_e_aenc": Choice,
    "phi_a_aenc": Choice,
})

_MODE_MOTION_FIELD_CHOICES = typing.TypedDict("_MODE_MOTION_FIELD_CHOICES", {
    "stopped_mode": Choice,
    "torque_mode": Choice,
    "velocity_mode": Choice,
    "position_mode": Choice,
    "prbs_flux_mode": Choice,
    "prbs_torque_mode": Choice,
    "prbs_velocity_mode": Choice,
    "prbs_position_mode": Choice,
    "uq_ud_ext": Choice,
    "enc_init_mini_move": Choice,
    "AGPI_A torque_mode": Choice,
    "AGPI_A velocity_mode": Choice,
    "AGPI_A position_mode": Choice,
    "PWM_I torque_mode": Choice,
    "PWM_I velocity_mode": Choice,
    "PWM_I position_mode": Choice,
})

_MODE_RAMP_FIELD_CHOICES = typing.TypedDict("_MODE_RAMP_FIELD_CHOICES", {
    "no velocity ramping": Choice,
    "reserved": Choice,
})

_MODE_FF_FIELD_CHOICES = typing.TypedDict("_MODE_FF_FIELD_CHOICES", {
    "disabled": Choice,
    "velocity control": Choice,
    "torque control": Choice,
})

_MODE_PID_TYPE_FIELD_CHOICES = typing.TypedDict("_MODE_PID_TYPE_FIELD_CHOICES", {
    "parallel PI": Choice,
    "sequential PI": Choice,
})

_PID_ERROR_ADDR_FIELD_CHOICES = typing.TypedDict("_PID_ERROR_ADDR_FIELD_CHOICES", {
    "PID_TORQUE_ERROR": Choice,
    "PID_FLUX_ERROR": Choice,
    "PID_VELOCITY_ERROR": Choice,
    "PID_POSITION_ERROR": Choice,
    "PID_TORQUE_ERROR_SUM": Choice,
    "PID_FLUX_ERROR_SUM": Choice,
    "PID_VELOCITY_ERROR_SUM": Choice,
    "PID_POSITION_ERROR_SUM": Choice,
})

_INTERIM_ADDR_FIELD_CHOICES = typing.TypedDict("_INTERIM_ADDR_FIELD_CHOICES", {
    "PIDIN_TARGET_TORQUE": Choice,
    "PIDIN_TARGET_FLUX": Choice,
    "PIDIN_TARGET_VELOCITY": Choice,
    "PIDIN_TARGET_POSITION": Choice,
    "PIDOUT_TARGET_TORQUE": Choice,
    "PIDOUT_TARGET_FLUX": Choice,
    "PIDOUT_TARGET_VELOCITY": Choice,
    "PIDOUT_TARGET_POSITION": Choice,
    "FOC_IWY_IUX": Choice,
    "FOC_IV": Choice,
    "FOC_IB_IA": Choice,
    "FOC_IQ_ID": Choice,
    "FOC_UQ_UD": Choice,
    "FOC_UQ_UD_LIMITED": Choice,
    "FOC_UB_UA": Choice,
    "FOC_UWY_UUX": Choice,
    "FOC_UV": Choice,
    "PWM_WY_UX": Choice,
    "PWM_UV": Choice,
    "ADC_I1_I0": Choice,
    "PID_TORQUE_TARGET_FLUX_TARGET_TORQUE_ACTUAL_FLUX_ACTUAL_DIV256": Choice,
    "PID_TORQUE_TARGET_TORQUE_ACTUAL": Choice,
    "PID_FLUX_TARGET_FLUX_ACTUAL": Choice,
    "PID_VELOCITY_TARGET_VELOCITY_ACTUAL_DIV256": Choice,
    "PID_VELOCITY_TARGET_VELOCITY_ACTUAL": Choice,
    "PID_POSITION_TARGET_POSITION_ACTUAL_DIV256": Choice,
    "PID_POSITION_TARGET_POSITION_ACTUAL": Choice,
    "FF_VELOCITY": Choice,
    "FF_TORQUE": Choice,
    "ACTUAL_VELOCITY_PPTM": Choice,
    "REF_SWITCH_STATUS": Choice,
    "HOME_POSITION": Choice,
    "LEFT_POSITION": Choice,
    "RIGHT_POSITION": Choice,
    "ENC_INIT_HALL_STATUS": Choice,
    "ENC_INIT_HALL_PHI_E_ABN_OFFSET": Choice,
    "ENC_INIT_HALL_PHI_E_AENC_OFFSET": Choice,
    "ENC_INIT_HALL_PHI_A_AENC_OFFSET": Choice,
    "enc_init_mini_move_u_d_status": Choice,
    "enc_init_mini_move_phi_e_phi_e_offset": Choice,
    "SINGLE_PIN_IF_PWM_DUTY_CYCLE_TORQUE_TARGET": Choice,
    "SINGLE_PIN_IF_VELOCITY_TARGET": Choice,
    "SINGLE_PIN_IF_POSITION_TARGET": Choice,
})

_WATCHDOG_CFG_FIELD_CHOICES = typing.TypedDict("_WATCHDOG_CFG_FIELD_CHOICES", {
    "No action on watchdog error": Choice,
    "PWM and power stage disable on watchdog error": Choice,
    "Global reset on watchdog error": Choice,
    "reserved": Choice,
})

class _ALL_REGISTERS(RegisterGroup):

    class _CHIPINFO_DATA(Register):

        class _SI_TYPE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SI_TYPE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("CHIPINFO_DATA", parent, access, address, signed)
            self.SI_TYPE = self._SI_TYPE(self, Access.R, 0xFFFFFFFF,  0, signed=False)

    class _CHIPINFO_ADDR(Register):

        class _CHIP_INFO_ADDRESS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CHIP_INFO_ADDRESS", parent, access, mask, shift, signed=signed)

                self.choice : _CHIP_INFO_ADDRESS_FIELD_CHOICES = {
                    "SI_TYPE": Choice(0, self),
                    "SI_VERSION": Choice(1, self),
                    "SI_DATE": Choice(2, self),
                    "SI_TIME": Choice(3, self),
                    "SI_VARIANT": Choice(4, self),
                    "SI_BUILD": Choice(5, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("CHIPINFO_ADDR", parent, access, address, signed)
            self.CHIP_INFO_ADDRESS = self._CHIP_INFO_ADDRESS(self, Access.RW, 0x000000FF,  0, signed=False)

    class _ADC_RAW_DATA(Register):

        class _ADC_I0_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I0_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_I1_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I1_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_RAW_DATA", parent, access, address, signed)
            self.ADC_I0_RAW = self._ADC_I0_RAW(self, Access.R, 0x0000FFFF,  0, signed=False)
            self.ADC_I1_RAW = self._ADC_I1_RAW(self, Access.R, 0xFFFF0000, 16, signed=False)

    class _ADC_RAW_ADDR(Register):

        class _ADC_RAW_ADDR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_RAW_ADDR", parent, access, mask, shift, signed=signed)

                self.choice : _ADC_RAW_ADDR_FIELD_CHOICES = {
                    "ADC_I1_RAW & ADC_I0_RAW": Choice(0, self),
                    "ADC_AGPI_A_RAW & ADC_VM_RAW": Choice(1, self),
                    "ADC_AENC_UX_RAW & ADC_AGPI_B_RAW": Choice(2, self),
                    "ADC_AENC_WY_RAW & ADC_AENC_VN_RAW": Choice(3, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_RAW_ADDR", parent, access, address, signed)
            self.ADC_RAW_ADDR = self._ADC_RAW_ADDR(self, Access.RW, 0x000000FF,  0, signed=False)

    class _dsADC_MCFG_B_MCFG_A(Register):

        class _cfg_dsmodulator_a(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("cfg_dsmodulator_a", parent, access, mask, shift, signed=signed)

                self.choice : _cfg_dsmodulator_a_FIELD_CHOICES = {
                    "int. dsMOD": Choice(0, self),
                    "ext. MCLK input": Choice(1, self),
                    "ext. MCLK output": Choice(2, self),
                    "ext. CMP": Choice(3, self),
                }

        class _mclk_polarity_a(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("mclk_polarity_a", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _mdat_polarity_a(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("mdat_polarity_a", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _sel_nclk_mclk_i_a(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("sel_nclk_mclk_i_a", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _blanking_a(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("blanking_a", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _cfg_dsmodulator_b(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("cfg_dsmodulator_b", parent, access, mask, shift, signed=signed)

                self.choice : _cfg_dsmodulator_b_FIELD_CHOICES = {
                    "int. dsMOD": Choice(0, self),
                    "ext. MCLK input": Choice(1, self),
                    "ext. MCLK output": Choice(2, self),
                    "ext. CMP": Choice(3, self),
                }

        class _mclk_polarity_b(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("mclk_polarity_b", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _mdat_polarity_b(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("mdat_polarity_b", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _sel_nclk_mclk_i_b(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("sel_nclk_mclk_i_b", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _blanking_b(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("blanking_b", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("dsADC_MCFG_B_MCFG_A", parent, access, address, signed)
            self.cfg_dsmodulator_a = self._cfg_dsmodulator_a(self, Access.RW, 0x00000003,  0, signed=False)
            self.mclk_polarity_a = self._mclk_polarity_a(self, Access.RW, 0x00000004,  2, signed=False)
            self.mdat_polarity_a = self._mdat_polarity_a(self, Access.RW, 0x00000008,  3, signed=False)
            self.sel_nclk_mclk_i_a = self._sel_nclk_mclk_i_a(self, Access.RW, 0x00000010,  4, signed=False)
            self.blanking_a = self._blanking_a(self, Access.RW, 0x0000FF00,  8, signed=False)
            self.cfg_dsmodulator_b = self._cfg_dsmodulator_b(self, Access.RW, 0x00030000, 16, signed=False)
            self.mclk_polarity_b = self._mclk_polarity_b(self, Access.RW, 0x00040000, 18, signed=False)
            self.mdat_polarity_b = self._mdat_polarity_b(self, Access.RW, 0x00080000, 19, signed=False)
            self.sel_nclk_mclk_i_b = self._sel_nclk_mclk_i_b(self, Access.RW, 0x00100000, 20, signed=False)
            self.blanking_b = self._blanking_b(self, Access.RW, 0xFF000000, 24, signed=False)

    class _dsADC_MCLK_A(Register):

        class _dsADC_MCLK_A(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("dsADC_MCLK_A", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("dsADC_MCLK_A", parent, access, address, signed)
            self.dsADC_MCLK_A = self._dsADC_MCLK_A(self, Access.RW, 0xFFFFFFFF,  0, signed=False)

    class _dsADC_MCLK_B(Register):

        class _dsADC_MCLK_B(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("dsADC_MCLK_B", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("dsADC_MCLK_B", parent, access, address, signed)
            self.dsADC_MCLK_B = self._dsADC_MCLK_B(self, Access.RW, 0xFFFFFFFF,  0, signed=False)

    class _dsADC_MDEC_B_MDEC_A(Register):

        class _dsADC_MDEC_A(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("dsADC_MDEC_A", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _dsADC_MDEC_B(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("dsADC_MDEC_B", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("dsADC_MDEC_B_MDEC_A", parent, access, address, signed)
            self.dsADC_MDEC_A = self._dsADC_MDEC_A(self, Access.RW, 0x0000FFFF,  0, signed=False)
            self.dsADC_MDEC_B = self._dsADC_MDEC_B(self, Access.RW, 0xFFFF0000, 16, signed=False)

    class _ADC_I1_SCALE_OFFSET(Register):

        class _ADC_I1_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I1_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_I1_SCALE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I1_SCALE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_I1_SCALE_OFFSET", parent, access, address, signed)
            self.ADC_I1_OFFSET = self._ADC_I1_OFFSET(self, Access.RW, 0x0000FFFF,  0, signed=False)
            self.ADC_I1_SCALE = self._ADC_I1_SCALE(self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _ADC_I0_SCALE_OFFSET(Register):

        class _ADC_I0_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I0_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_I0_SCALE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I0_SCALE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_I0_SCALE_OFFSET", parent, access, address, signed)
            self.ADC_I0_OFFSET = self._ADC_I0_OFFSET(self, Access.RW, 0x0000FFFF,  0, signed=False)
            self.ADC_I0_SCALE = self._ADC_I0_SCALE(self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _ADC_I_SELECT(Register):

        class _ADC_I0_SELECT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I0_SELECT", parent, access, mask, shift, signed=signed)

                self.choice : _ADC_I0_SELECT_FIELD_CHOICES = {
                    "ADCSD_I0_RAW (sigma delta ADC)": Choice(0, self),
                    "ADCSD_I1_RAW (sigma delta ADC)": Choice(1, self),
                    "ADC_I0_EXT (from register)": Choice(2, self),
                    "ADC_I1_EXT (from register)": Choice(3, self),
                }

        class _ADC_I1_SELECT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I1_SELECT", parent, access, mask, shift, signed=signed)

                self.choice : _ADC_I1_SELECT_FIELD_CHOICES = {
                    "ADCSD_I0_RAW (sigma delta ADC)": Choice(0, self),
                    "ADCSD_I1_RAW (sigma delta ADC)": Choice(1, self),
                    "ADC_I0_EXT (from register)": Choice(2, self),
                    "ADC_I1_EXT (from register)": Choice(3, self),
                }

        class _ADC_I_UX_SELECT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I_UX_SELECT", parent, access, mask, shift, signed=signed)

                self.choice : _ADC_I_UX_SELECT_FIELD_CHOICES = {
                    "UX = ADC_I0 (default)": Choice(0, self),
                    "UX = ADC_I1": Choice(1, self),
                    "UX = ADC_I2": Choice(2, self),
                }

        class _ADC_I_V_SELECT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I_V_SELECT", parent, access, mask, shift, signed=signed)

                self.choice : _ADC_I_V_SELECT_FIELD_CHOICES = {
                    "V = ADC_I0": Choice(0, self),
                    "V = ADC_I1 (default)": Choice(1, self),
                    "V = ADC_I2": Choice(2, self),
                }

        class _ADC_I_WY_SELECT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I_WY_SELECT", parent, access, mask, shift, signed=signed)

                self.choice : _ADC_I_WY_SELECT_FIELD_CHOICES = {
                    "WY = ADC_I0": Choice(0, self),
                    "WY = ADC_I1": Choice(1, self),
                    "WY = ADC_I2 (default)": Choice(2, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_I_SELECT", parent, access, address, signed)
            self.ADC_I0_SELECT = self._ADC_I0_SELECT(self, Access.RW, 0x000000FF,  0, signed=False)
            self.ADC_I1_SELECT = self._ADC_I1_SELECT(self, Access.RW, 0x0000FF00,  8, signed=False)
            self.ADC_I_UX_SELECT = self._ADC_I_UX_SELECT(self, Access.RW, 0x03000000, 24, signed=False)
            self.ADC_I_V_SELECT = self._ADC_I_V_SELECT(self, Access.RW, 0x0C000000, 26, signed=False)
            self.ADC_I_WY_SELECT = self._ADC_I_WY_SELECT(self, Access.RW, 0x30000000, 28, signed=False)

    class _ADC_I1_I0_EXT(Register):

        class _ADC_I0_EXT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I0_EXT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_I1_EXT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I1_EXT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_I1_I0_EXT", parent, access, address, signed)
            self.ADC_I0_EXT = self._ADC_I0_EXT(self, Access.RW, 0x0000FFFF,  0, signed=False)
            self.ADC_I1_EXT = self._ADC_I1_EXT(self, Access.RW, 0xFFFF0000, 16, signed=False)

    class _DS_ANALOG_INPUT_STAGE_CFG(Register):

        class _ADC_I0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I0", parent, access, mask, shift, signed=signed)

                self.choice : _ADC_I0_FIELD_CHOICES = {
                    "INP vs. INN": Choice(0, self),
                    "GND vs. INN": Choice(1, self),
                    "VDD/4": Choice(6, self),
                    "3*VDD/4": Choice(7, self),
                    "INP vs. GND": Choice(4, self),
                    "VDD/2": Choice(5, self),
                }

        class _ADC_I1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I1", parent, access, mask, shift, signed=signed)

                self.choice : _ADC_I1_FIELD_CHOICES = {
                    "INP vs. INN": Choice(0, self),
                    "GND vs. INN": Choice(1, self),
                    "VDD/4": Choice(6, self),
                    "3*VDD/4": Choice(7, self),
                    "INP vs. GND": Choice(4, self),
                    "VDD/2": Choice(5, self),
                }

        class _ADC_VM(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_VM", parent, access, mask, shift, signed=signed)

                self.choice : _ADC_VM_FIELD_CHOICES = {
                    "INP vs. INN": Choice(0, self),
                    "GND vs. INN": Choice(1, self),
                    "VDD/4": Choice(6, self),
                    "3*VDD/4": Choice(7, self),
                    "INP vs. GND": Choice(4, self),
                    "VDD/2": Choice(5, self),
                }

        class _ADC_AGPI_A(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_AGPI_A", parent, access, mask, shift, signed=signed)

                self.choice : _ADC_AGPI_A_FIELD_CHOICES = {
                    "INP vs. INN": Choice(0, self),
                    "GND vs. INN": Choice(1, self),
                    "VDD/4": Choice(6, self),
                    "3*VDD/4": Choice(7, self),
                    "INP vs. GND": Choice(4, self),
                    "VDD/2": Choice(5, self),
                }

        class _ADC_AGPI_B(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_AGPI_B", parent, access, mask, shift, signed=signed)

                self.choice : _ADC_AGPI_B_FIELD_CHOICES = {
                    "INP vs. INN": Choice(0, self),
                    "GND vs. INN": Choice(1, self),
                    "VDD/4": Choice(6, self),
                    "3*VDD/4": Choice(7, self),
                    "INP vs. GND": Choice(4, self),
                    "VDD/2": Choice(5, self),
                }

        class _ADC_AENC_UX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_AENC_UX", parent, access, mask, shift, signed=signed)

                self.choice : _ADC_AENC_UX_FIELD_CHOICES = {
                    "INP vs. INN": Choice(0, self),
                    "GND vs. INN": Choice(1, self),
                    "VDD/4": Choice(6, self),
                    "3*VDD/4": Choice(7, self),
                    "INP vs. GND": Choice(4, self),
                    "VDD/2": Choice(5, self),
                }

        class _ADC_AENC_VN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_AENC_VN", parent, access, mask, shift, signed=signed)

                self.choice : _ADC_AENC_VN_FIELD_CHOICES = {
                    "INP vs. INN": Choice(0, self),
                    "GND vs. INN": Choice(1, self),
                    "VDD/4": Choice(6, self),
                    "3*VDD/4": Choice(7, self),
                    "INP vs. GND": Choice(4, self),
                    "VDD/2": Choice(5, self),
                }

        class _ADC_AENC_WY(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_AENC_WY", parent, access, mask, shift, signed=signed)

                self.choice : _ADC_AENC_WY_FIELD_CHOICES = {
                    "INP vs. INN": Choice(0, self),
                    "GND vs. INN": Choice(1, self),
                    "VDD/4": Choice(6, self),
                    "3*VDD/4": Choice(7, self),
                    "INP vs. GND": Choice(4, self),
                    "VDD/2": Choice(5, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("DS_ANALOG_INPUT_STAGE_CFG", parent, access, address, signed)
            self.ADC_I0 = self._ADC_I0(self, Access.RW, 0x0000000F,  0, signed=False)
            self.ADC_I1 = self._ADC_I1(self, Access.RW, 0x000000F0,  4, signed=False)
            self.ADC_VM = self._ADC_VM(self, Access.RW, 0x00000F00,  8, signed=False)
            self.ADC_AGPI_A = self._ADC_AGPI_A(self, Access.RW, 0x0000F000, 12, signed=False)
            self.ADC_AGPI_B = self._ADC_AGPI_B(self, Access.RW, 0x000F0000, 16, signed=False)
            self.ADC_AENC_UX = self._ADC_AENC_UX(self, Access.RW, 0x00F00000, 20, signed=False)
            self.ADC_AENC_VN = self._ADC_AENC_VN(self, Access.RW, 0x0F000000, 24, signed=False)
            self.ADC_AENC_WY = self._ADC_AENC_WY(self, Access.RW, 0xF0000000, 28, signed=False)

    class _AENC_0_SCALE_OFFSET(Register):

        class _AENC_0_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_0_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AENC_0_SCALE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_0_SCALE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_0_SCALE_OFFSET", parent, access, address, signed)
            self.AENC_0_OFFSET = self._AENC_0_OFFSET(self, Access.RW, 0x0000FFFF,  0, signed=False)
            self.AENC_0_SCALE = self._AENC_0_SCALE(self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _AENC_1_SCALE_OFFSET(Register):

        class _AENC_1_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_1_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AENC_1_SCALE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_1_SCALE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_1_SCALE_OFFSET", parent, access, address, signed)
            self.AENC_1_OFFSET = self._AENC_1_OFFSET(self, Access.RW, 0x0000FFFF,  0, signed=False)
            self.AENC_1_SCALE = self._AENC_1_SCALE(self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _AENC_2_SCALE_OFFSET(Register):

        class _AENC_2_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_2_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AENC_2_SCALE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_2_SCALE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_2_SCALE_OFFSET", parent, access, address, signed)
            self.AENC_2_OFFSET = self._AENC_2_OFFSET(self, Access.RW, 0x0000FFFF,  0, signed=False)
            self.AENC_2_SCALE = self._AENC_2_SCALE(self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _AENC_SELECT(Register):

        class _AENC_0_SELECT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_0_SELECT", parent, access, mask, shift, signed=signed)

                self.choice : _AENC_0_SELECT_FIELD_CHOICES = {
                    "<AENC_UX_RAW>": Choice(0, self),
                    "AENC_VN_RAW": Choice(1, self),
                    "AENC_WY_RAW": Choice(2, self),
                }

        class _AENC_1_SELECT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_1_SELECT", parent, access, mask, shift, signed=signed)

                self.choice : _AENC_1_SELECT_FIELD_CHOICES = {
                    "AENC_UX_RAW": Choice(0, self),
                    "<AENC_VN_RAW>": Choice(1, self),
                    "AENC_WY_RAW": Choice(2, self),
                }

        class _AENC_2_SELECT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_2_SELECT", parent, access, mask, shift, signed=signed)

                self.choice : _AENC_2_SELECT_FIELD_CHOICES = {
                    "AENC_UX_RAW": Choice(0, self),
                    "AENC_VN_RAW": Choice(1, self),
                    "<AENC_WY_RAW>": Choice(2, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_SELECT", parent, access, address, signed)
            self.AENC_0_SELECT = self._AENC_0_SELECT(self, Access.RW, 0x000000FF,  0, signed=False)
            self.AENC_1_SELECT = self._AENC_1_SELECT(self, Access.RW, 0x0000FF00,  8, signed=False)
            self.AENC_2_SELECT = self._AENC_2_SELECT(self, Access.RW, 0x00FF0000, 16, signed=False)

    class _ADC_IWY_IUX(Register):

        class _ADC_IUX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_IUX", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_IWY(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_IWY", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_IWY_IUX", parent, access, address, signed)
            self.ADC_IUX = self._ADC_IUX(self, Access.R, 0x0000FFFF,  0, signed=True)
            self.ADC_IWY = self._ADC_IWY(self, Access.R, 0xFFFF0000, 16, signed=True)

    class _ADC_IV(Register):

        class _ADC_IV(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_IV", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_IV", parent, access, address, signed)
            self.ADC_IV = self._ADC_IV(self, Access.R, 0x0000FFFF,  0, signed=True)

    class _AENC_WY_UX(Register):

        class _AENC_UX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_UX", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AENC_WY(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_WY", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_WY_UX", parent, access, address, signed)
            self.AENC_UX = self._AENC_UX(self, Access.R, 0x0000FFFF,  0, signed=True)
            self.AENC_WY = self._AENC_WY(self, Access.R, 0xFFFF0000, 16, signed=True)

    class _AENC_VN(Register):

        class _AENC_VN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_VN", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_VN", parent, access, address, signed)
            self.AENC_VN = self._AENC_VN(self, Access.R, 0x0000FFFF,  0, signed=True)

    class _PWM_POLARITIES(Register):

        class _PWM_POLARITIES_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_POLARITIES_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_POLARITIES_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_POLARITIES_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PWM_POLARITIES", parent, access, address, signed)
            self.PWM_POLARITIES_0 = self._PWM_POLARITIES_0(self, Access.RW, 0x00000001,  0, signed=False)
            self.PWM_POLARITIES_1 = self._PWM_POLARITIES_1(self, Access.RW, 0x00000002,  1, signed=False)

    class _PWM_MAXCNT(Register):

        class _PWM_MAXCNT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_MAXCNT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PWM_MAXCNT", parent, access, address, signed)
            self.PWM_MAXCNT = self._PWM_MAXCNT(self, Access.RW, 0x0000FFFF,  0, signed=False)

    class _PWM_BBM_H_BBM_L(Register):

        class _PWM_BBM_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_BBM_L", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_BBM_H(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_BBM_H", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PWM_BBM_H_BBM_L", parent, access, address, signed)
            self.PWM_BBM_L = self._PWM_BBM_L(self, Access.RW, 0x000000FF,  0, signed=False)
            self.PWM_BBM_H = self._PWM_BBM_H(self, Access.RW, 0x0000FF00,  8, signed=False)

    class _PWM_SV_CHOP(Register):

        class _PWM_CHOP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_CHOP", parent, access, mask, shift, signed=signed)

                self.choice : _PWM_CHOP_FIELD_CHOICES = {
                    "off, free running": Choice(4, self),
                    "off, low side permanent = ON": Choice(1, self),
                    "off, high side permanent = ON": Choice(2, self),
                    "low side chopper, high side off": Choice(5, self),
                    "high side chopper, low side off": Choice(6, self),
                    "centered PWM for FOC": Choice(7, self),
                }

        class _PWM_SV(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_SV", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PWM_SV_CHOP", parent, access, address, signed)
            self.PWM_CHOP = self._PWM_CHOP(self, Access.RW, 0x000000FF,  0, signed=False)
            self.PWM_SV = self._PWM_SV(self, Access.RW, 0x00000100,  8, signed=False)

    class _MOTOR_TYPE_N_POLE_PAIRS(Register):

        class _N_POLE_PAIRS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("N_POLE_PAIRS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _MOTOR_TYPE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MOTOR_TYPE", parent, access, mask, shift, signed=signed)

                self.choice : _MOTOR_TYPE_FIELD_CHOICES = {
                    "No motor": Choice(0, self),
                    "Single phase DC": Choice(1, self),
                    "Two phase Stepper": Choice(2, self),
                    "Three phase BLDC": Choice(3, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("MOTOR_TYPE_N_POLE_PAIRS", parent, access, address, signed)
            self.N_POLE_PAIRS = self._N_POLE_PAIRS(self, Access.RW, 0x0000FFFF,  0, signed=False)
            self.MOTOR_TYPE = self._MOTOR_TYPE(self, Access.RW, 0x00FF0000, 16, signed=False)

    class _PHI_E_EXT(Register):

        class _PHI_E_EXT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_E_EXT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PHI_E_EXT", parent, access, address, signed)
            self.PHI_E_EXT = self._PHI_E_EXT(self, Access.RW, 0x0000FFFF,  0, signed=True)

    class _OPENLOOP_MODE(Register):

        class _OPENLOOP_PHI_DIRECTION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OPENLOOP_PHI_DIRECTION", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("OPENLOOP_MODE", parent, access, address, signed)
            self.OPENLOOP_PHI_DIRECTION = self._OPENLOOP_PHI_DIRECTION(self, Access.RW, 0x00001000, 12, signed=False)

    class _OPENLOOP_ACCELERATION(Register):

        class _OPENLOOP_ACCELERATION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OPENLOOP_ACCELERATION", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("OPENLOOP_ACCELERATION", parent, access, address, signed)
            self.OPENLOOP_ACCELERATION = self._OPENLOOP_ACCELERATION(self, Access.RW, 0x000FFFFF,  0, signed=False)

    class _OPENLOOP_VELOCITY_TARGET(Register):

        class _OPENLOOP_VELOCITY_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OPENLOOP_VELOCITY_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("OPENLOOP_VELOCITY_TARGET", parent, access, address, signed)
            self.OPENLOOP_VELOCITY_TARGET = self._OPENLOOP_VELOCITY_TARGET(self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _OPENLOOP_VELOCITY_ACTUAL(Register):

        class _OPENLOOP_VELOCITY_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OPENLOOP_VELOCITY_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("OPENLOOP_VELOCITY_ACTUAL", parent, access, address, signed)
            self.OPENLOOP_VELOCITY_ACTUAL = self._OPENLOOP_VELOCITY_ACTUAL(self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _OPENLOOP_PHI(Register):

        class _OPENLOOP_PHI(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OPENLOOP_PHI", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("OPENLOOP_PHI", parent, access, address, signed)
            self.OPENLOOP_PHI = self._OPENLOOP_PHI(self, Access.RW, 0x0000FFFF,  0, signed=True)

    class _UQ_UD_EXT(Register):

        class _UD_EXT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UD_EXT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UQ_EXT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UQ_EXT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("UQ_UD_EXT", parent, access, address, signed)
            self.UD_EXT = self._UD_EXT(self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.UQ_EXT = self._UQ_EXT(self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _ABN_DECODER_MODE(Register):

        class _apol(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("apol", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _bpol(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("bpol", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _npol(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("npol", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _use_abn_as_n(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("use_abn_as_n", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _cln(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("cln", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _direction(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("direction", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_DECODER_MODE", parent, access, address, signed)
            self.apol = self._apol(self, Access.RW, 0x00000001,  0, signed=False)
            self.bpol = self._bpol(self, Access.RW, 0x00000002,  1, signed=False)
            self.npol = self._npol(self, Access.RW, 0x00000004,  2, signed=False)
            self.use_abn_as_n = self._use_abn_as_n(self, Access.RW, 0x00000008,  3, signed=False)
            self.cln = self._cln(self, Access.RW, 0x00000100,  8, signed=False)
            self.direction = self._direction(self, Access.RW, 0x00001000, 12, signed=False)

    class _ABN_DECODER_PPR(Register):

        class _ABN_DECODER_PPR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_DECODER_PPR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_DECODER_PPR", parent, access, address, signed)
            self.ABN_DECODER_PPR = self._ABN_DECODER_PPR(self, Access.RW, 0x00FFFFFF,  0, signed=False)

    class _ABN_DECODER_COUNT(Register):

        class _ABN_DECODER_COUNT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_DECODER_COUNT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_DECODER_COUNT", parent, access, address, signed)
            self.ABN_DECODER_COUNT = self._ABN_DECODER_COUNT(self, Access.RW, 0x00FFFFFF,  0, signed=False)

    class _ABN_DECODER_COUNT_N(Register):

        class _ABN_DECODER_COUNT_N(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_DECODER_COUNT_N", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_DECODER_COUNT_N", parent, access, address, signed)
            self.ABN_DECODER_COUNT_N = self._ABN_DECODER_COUNT_N(self, Access.RW, 0x00FFFFFF,  0, signed=False)

    class _ABN_DECODER_PHI_E_PHI_M_OFFSET(Register):

        class _ABN_DECODER_PHI_M_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_DECODER_PHI_M_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ABN_DECODER_PHI_E_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_DECODER_PHI_E_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_DECODER_PHI_E_PHI_M_OFFSET", parent, access, address, signed)
            self.ABN_DECODER_PHI_M_OFFSET = self._ABN_DECODER_PHI_M_OFFSET(self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.ABN_DECODER_PHI_E_OFFSET = self._ABN_DECODER_PHI_E_OFFSET(self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _ABN_DECODER_PHI_E_PHI_M(Register):

        class _ABN_DECODER_PHI_M(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_DECODER_PHI_M", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ABN_DECODER_PHI_E(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_DECODER_PHI_E", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_DECODER_PHI_E_PHI_M", parent, access, address, signed)
            self.ABN_DECODER_PHI_M = self._ABN_DECODER_PHI_M(self, Access.R, 0x0000FFFF,  0, signed=True)
            self.ABN_DECODER_PHI_E = self._ABN_DECODER_PHI_E(self, Access.R, 0xFFFF0000, 16, signed=True)

    class _ABN_2_DECODER_MODE(Register):

        class _apol(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("apol", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _bpol(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("bpol", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _npol(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("npol", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _use_abn_as_n(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("use_abn_as_n", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _cln(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("cln", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _direction(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("direction", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_2_DECODER_MODE", parent, access, address, signed)
            self.apol = self._apol(self, Access.RW, 0x00000001,  0, signed=False)
            self.bpol = self._bpol(self, Access.RW, 0x00000002,  1, signed=False)
            self.npol = self._npol(self, Access.RW, 0x00000004,  2, signed=False)
            self.use_abn_as_n = self._use_abn_as_n(self, Access.RW, 0x00000008,  3, signed=False)
            self.cln = self._cln(self, Access.RW, 0x00000100,  8, signed=False)
            self.direction = self._direction(self, Access.RW, 0x00001000, 12, signed=False)

    class _ABN_2_DECODER_PPR(Register):

        class _ABN_2_DECODER_PPR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_2_DECODER_PPR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_2_DECODER_PPR", parent, access, address, signed)
            self.ABN_2_DECODER_PPR = self._ABN_2_DECODER_PPR(self, Access.RW, 0x00FFFFFF,  0, signed=False)

    class _ABN_2_DECODER_COUNT(Register):

        class _ABN_2_DECODER_COUNT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_2_DECODER_COUNT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_2_DECODER_COUNT", parent, access, address, signed)
            self.ABN_2_DECODER_COUNT = self._ABN_2_DECODER_COUNT(self, Access.RW, 0x00FFFFFF,  0, signed=False)

    class _ABN_2_DECODER_COUNT_N(Register):

        class _ABN_2_DECODER_COUNT_N(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_2_DECODER_COUNT_N", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_2_DECODER_COUNT_N", parent, access, address, signed)
            self.ABN_2_DECODER_COUNT_N = self._ABN_2_DECODER_COUNT_N(self, Access.RW, 0x00FFFFFF,  0, signed=False)

    class _ABN_2_DECODER_PHI_M_OFFSET(Register):

        class _ABN_2_DECODER_PHI_M_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_2_DECODER_PHI_M_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_2_DECODER_PHI_M_OFFSET", parent, access, address, signed)
            self.ABN_2_DECODER_PHI_M_OFFSET = self._ABN_2_DECODER_PHI_M_OFFSET(self, Access.RW, 0x0000FFFF,  0, signed=True)

    class _ABN_2_DECODER_PHI_M(Register):

        class _ABN_2_DECODER_PHI_M(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_2_DECODER_PHI_M", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ABN_2_DECODER_PHI_M", parent, access, address, signed)
            self.ABN_2_DECODER_PHI_M = self._ABN_2_DECODER_PHI_M(self, Access.R, 0x0000FFFF,  0, signed=True)

    class _HALL_MODE(Register):

        class _polarity(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("polarity", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _synchronous_PWM_sampling(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("synchronous_PWM_sampling", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _interpolation(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("interpolation", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _direction(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("direction", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_BLANK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_BLANK", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("HALL_MODE", parent, access, address, signed)
            self.polarity = self._polarity(self, Access.RW, 0x00000001,  0, signed=False)
            self.synchronous_PWM_sampling = self._synchronous_PWM_sampling(self, Access.RW, 0x00000010,  4, signed=False)
            self.interpolation = self._interpolation(self, Access.RW, 0x00000100,  8, signed=False)
            self.direction = self._direction(self, Access.RW, 0x00001000, 12, signed=False)
            self.HALL_BLANK = self._HALL_BLANK(self, Access.RW, 0x0FFF0000, 16, signed=False)

    class _HALL_POSITION_060_000(Register):

        class _HALL_POSITION_000(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_POSITION_000", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_POSITION_060(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_POSITION_060", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("HALL_POSITION_060_000", parent, access, address, signed)
            self.HALL_POSITION_000 = self._HALL_POSITION_000(self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.HALL_POSITION_060 = self._HALL_POSITION_060(self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _HALL_POSITION_180_120(Register):

        class _HALL_POSITION_120(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_POSITION_120", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_POSITION_180(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_POSITION_180", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("HALL_POSITION_180_120", parent, access, address, signed)
            self.HALL_POSITION_120 = self._HALL_POSITION_120(self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.HALL_POSITION_180 = self._HALL_POSITION_180(self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _HALL_POSITION_300_240(Register):

        class _HALL_POSITION_240(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_POSITION_240", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_POSITION_300(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_POSITION_300", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("HALL_POSITION_300_240", parent, access, address, signed)
            self.HALL_POSITION_240 = self._HALL_POSITION_240(self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.HALL_POSITION_300 = self._HALL_POSITION_300(self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _HALL_PHI_E_PHI_M_OFFSET(Register):

        class _HALL_PHI_M_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_PHI_M_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_PHI_E_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_PHI_E_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("HALL_PHI_E_PHI_M_OFFSET", parent, access, address, signed)
            self.HALL_PHI_M_OFFSET = self._HALL_PHI_M_OFFSET(self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.HALL_PHI_E_OFFSET = self._HALL_PHI_E_OFFSET(self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _HALL_DPHI_MAX(Register):

        class _HALL_DPHI_MAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_DPHI_MAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("HALL_DPHI_MAX", parent, access, address, signed)
            self.HALL_DPHI_MAX = self._HALL_DPHI_MAX(self, Access.RW, 0x0000FFFF,  0, signed=False)

    class _HALL_PHI_E_INTERPOLATED_PHI_E(Register):

        class _HALL_PHI_E(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_PHI_E", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_PHI_E_INTERPOLATED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_PHI_E_INTERPOLATED", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("HALL_PHI_E_INTERPOLATED_PHI_E", parent, access, address, signed)
            self.HALL_PHI_E = self._HALL_PHI_E(self, Access.R, 0x0000FFFF,  0, signed=True)
            self.HALL_PHI_E_INTERPOLATED = self._HALL_PHI_E_INTERPOLATED(self, Access.R, 0xFFFF0000, 16, signed=True)

    class _HALL_PHI_M(Register):

        class _HALL_PHI_M(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_PHI_M", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("HALL_PHI_M", parent, access, address, signed)
            self.HALL_PHI_M = self._HALL_PHI_M(self, Access.R, 0x0000FFFF,  0, signed=True)

    class _AENC_DECODER_MODE(Register):

        class _AENC_DECODER_MODE_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_DECODER_MODE_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AENC_DECODER_MODE_12(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_DECODER_MODE_12", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_DECODER_MODE", parent, access, address, signed)
            self.AENC_DECODER_MODE_0 = self._AENC_DECODER_MODE_0(self, Access.RW, 0x00000001,  0, signed=False)
            self.AENC_DECODER_MODE_12 = self._AENC_DECODER_MODE_12(self, Access.RW, 0x00001000, 12, signed=False)

    class _AENC_DECODER_N_THRESHOLD(Register):

        class _AENC_DECODER_N_THRESHOLD(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_DECODER_N_THRESHOLD", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_DECODER_N_THRESHOLD", parent, access, address, signed)
            self.AENC_DECODER_N_THRESHOLD = self._AENC_DECODER_N_THRESHOLD(self, Access.RW, 0x0000FFFF,  0, signed=False)

    class _AENC_DECODER_PHI_A_RAW(Register):

        class _AENC_DECODER_PHI_A_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_DECODER_PHI_A_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_DECODER_PHI_A_RAW", parent, access, address, signed)
            self.AENC_DECODER_PHI_A_RAW = self._AENC_DECODER_PHI_A_RAW(self, Access.R, 0x0000FFFF,  0, signed=True)

    class _AENC_DECODER_PHI_A_OFFSET(Register):

        class _AENC_DECODER_PHI_A_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_DECODER_PHI_A_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_DECODER_PHI_A_OFFSET", parent, access, address, signed)
            self.AENC_DECODER_PHI_A_OFFSET = self._AENC_DECODER_PHI_A_OFFSET(self, Access.RW, 0x0000FFFF,  0, signed=True)

    class _AENC_DECODER_PHI_A(Register):

        class _AENC_DECODER_PHI_A(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_DECODER_PHI_A", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_DECODER_PHI_A", parent, access, address, signed)
            self.AENC_DECODER_PHI_A = self._AENC_DECODER_PHI_A(self, Access.R, 0x0000FFFF,  0, signed=True)

    class _AENC_DECODER_PPR(Register):

        class _AENC_DECODER_PPR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_DECODER_PPR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_DECODER_PPR", parent, access, address, signed)
            self.AENC_DECODER_PPR = self._AENC_DECODER_PPR(self, Access.RW, 0x0000FFFF,  0, signed=True)

    class _AENC_DECODER_COUNT(Register):

        class _AENC_DECODER_COUNT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_DECODER_COUNT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_DECODER_COUNT", parent, access, address, signed)
            self.AENC_DECODER_COUNT = self._AENC_DECODER_COUNT(self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _AENC_DECODER_COUNT_N(Register):

        class _AENC_DECODER_COUNT_N(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_DECODER_COUNT_N", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_DECODER_COUNT_N", parent, access, address, signed)
            self.AENC_DECODER_COUNT_N = self._AENC_DECODER_COUNT_N(self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _AENC_DECODER_PHI_E_PHI_M_OFFSET(Register):

        class _AENC_DECODER_PHI_M_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_DECODER_PHI_M_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AENC_DECODER_PHI_E_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_DECODER_PHI_E_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_DECODER_PHI_E_PHI_M_OFFSET", parent, access, address, signed)
            self.AENC_DECODER_PHI_M_OFFSET = self._AENC_DECODER_PHI_M_OFFSET(self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.AENC_DECODER_PHI_E_OFFSET = self._AENC_DECODER_PHI_E_OFFSET(self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _AENC_DECODER_PHI_E_PHI_M(Register):

        class _AENC_DECODER_PHI_M(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_DECODER_PHI_M", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AENC_DECODER_PHI_E(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AENC_DECODER_PHI_E", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("AENC_DECODER_PHI_E_PHI_M", parent, access, address, signed)
            self.AENC_DECODER_PHI_M = self._AENC_DECODER_PHI_M(self, Access.R, 0x0000FFFF,  0, signed=True)
            self.AENC_DECODER_PHI_E = self._AENC_DECODER_PHI_E(self, Access.R, 0xFFFF0000, 16, signed=True)

    class _CONFIG_DATA(Register):

        class _biquad_x_a_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("biquad_x_a_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("CONFIG_DATA", parent, access, address, signed)
            self.biquad_x_a_1 = self._biquad_x_a_1(self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _CONFIG_ADDR(Register):

        class _CONFIG_ADDR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CONFIG_ADDR", parent, access, mask, shift, signed=signed)

                self.choice : _CONFIG_ADDR_FIELD_CHOICES = {
                    "biquad_x_a_1": Choice(1, self),
                    "biquad_x_a_2": Choice(2, self),
                    "biquad_x_b_0": Choice(4, self),
                    "biquad_x_b_1": Choice(5, self),
                    "biquad_x_b_2": Choice(6, self),
                    "biquad_x_enable": Choice(7, self),
                    "biquad_v_a_1": Choice(9, self),
                    "biquad_v_a_2": Choice(10, self),
                    "biquad_v_b_0": Choice(12, self),
                    "biquad_v_b_1": Choice(13, self),
                    "biquad_v_b_2": Choice(14, self),
                    "biquad_v_enable": Choice(15, self),
                    "biquad_t_a_1": Choice(17, self),
                    "biquad_t_a_2": Choice(18, self),
                    "biquad_t_b_0": Choice(20, self),
                    "biquad_t_b_1": Choice(21, self),
                    "biquad_t_b_2": Choice(22, self),
                    "biquad_t_enable": Choice(23, self),
                    "biquad_f_a_1": Choice(25, self),
                    "biquad_f_a_2": Choice(26, self),
                    "biquad_f_b_0": Choice(28, self),
                    "biquad_f_b_1": Choice(29, self),
                    "biquad_f_b_2": Choice(30, self),
                    "biquad_f_enable": Choice(31, self),
                    "prbs_amplitude": Choice(32, self),
                    "prbs_down_sampling_ratio": Choice(33, self),
                    "ref_switch_config": Choice(51, self),
                    "Encoder_Init_hall_Enable": Choice(52, self),
                    "SINGLE_PIN_IF_STATUS_CFG": Choice(60, self),
                    "SINGLE_PIN_IF_SCALE_OFFSET": Choice(61, self),
                    "ADVANCED_PI_REPRESENTATION": Choice(62, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("CONFIG_ADDR", parent, access, address, signed)
            self.CONFIG_ADDR = self._CONFIG_ADDR(self, Access.RW, 0xFFFFFFFF,  0, signed=False)

    class _VELOCITY_SELECTION(Register):

        class _VELOCITY_SELECTION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_SELECTION", parent, access, mask, shift, signed=signed)

                self.choice : _VELOCITY_SELECTION_FIELD_CHOICES = {
                    "PHI_E_SELECTION": Choice(0, self),
                    "phi_e_ext": Choice(1, self),
                    "phi_e_openloop": Choice(2, self),
                    "phi_e_abn": Choice(3, self),
                    "reserved": Choice(8, self),
                    "phi_e_hal": Choice(5, self),
                    "phi_e_aenc": Choice(6, self),
                    "phi_a_aenc": Choice(7, self),
                    "phi_m_abn": Choice(9, self),
                    "phi_m_abn_2": Choice(10, self),
                    "phi_m_aenc": Choice(11, self),
                    "phi_m_hal": Choice(12, self),
                }

        class _VELOCITY_METER_SELECTION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_METER_SELECTION", parent, access, mask, shift, signed=signed)

                self.choice : _VELOCITY_METER_SELECTION_FIELD_CHOICES = {
                    "default": Choice(0, self),
                    "advanced": Choice(1, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("VELOCITY_SELECTION", parent, access, address, signed)
            self.VELOCITY_SELECTION = self._VELOCITY_SELECTION(self, Access.RW, 0x000000FF,  0, signed=False)
            self.VELOCITY_METER_SELECTION = self._VELOCITY_METER_SELECTION(self, Access.RW, 0x0000FF00,  8, signed=False)

    class _POSITION_SELECTION(Register):

        class _POSITION_SELECTION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_SELECTION", parent, access, mask, shift, signed=signed)

                self.choice : _POSITION_SELECTION_FIELD_CHOICES = {
                    "phi_e selected via PHI_E_SELECTION": Choice(0, self),
                    "phi_e_ext": Choice(1, self),
                    "phi_e_openloop": Choice(2, self),
                    "phi_e_abn": Choice(3, self),
                    "reserved": Choice(8, self),
                    "phi_e_hal": Choice(5, self),
                    "phi_e_aenc": Choice(6, self),
                    "phi_a_aenc": Choice(7, self),
                    "phi_m_abn": Choice(9, self),
                    "phi_m_abn_2": Choice(10, self),
                    "phi_m_aenc": Choice(11, self),
                    "phi_m_hal": Choice(12, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("POSITION_SELECTION", parent, access, address, signed)
            self.POSITION_SELECTION = self._POSITION_SELECTION(self, Access.RW, 0x000000FF,  0, signed=False)

    class _PHI_E_SELECTION(Register):

        class _PHI_E_SELECTION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_E_SELECTION", parent, access, mask, shift, signed=signed)

                self.choice : _PHI_E_SELECTION_FIELD_CHOICES = {
                    "reserved": Choice(4, self),
                    "phi_e_ext": Choice(1, self),
                    "phi_e_openloop": Choice(2, self),
                    "phi_e_abn": Choice(3, self),
                    "phi_e_hal": Choice(5, self),
                    "phi_e_aenc": Choice(6, self),
                    "phi_a_aenc": Choice(7, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("PHI_E_SELECTION", parent, access, address, signed)
            self.PHI_E_SELECTION = self._PHI_E_SELECTION(self, Access.RW, 0x000000FF,  0, signed=False)

    class _PHI_E(Register):

        class _PHI_E(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_E", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PHI_E", parent, access, address, signed)
            self.PHI_E = self._PHI_E(self, Access.R, 0x0000FFFF,  0, signed=True)

    class _PID_FLUX_P_FLUX_I(Register):

        class _PID_FLUX_I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_FLUX_P(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_P", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_FLUX_P_FLUX_I", parent, access, address, signed)
            self.PID_FLUX_I = self._PID_FLUX_I(self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.PID_FLUX_P = self._PID_FLUX_P(self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _PID_TORQUE_P_TORQUE_I(Register):

        class _PID_TORQUE_I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_TORQUE_P(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_P", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_TORQUE_P_TORQUE_I", parent, access, address, signed)
            self.PID_TORQUE_I = self._PID_TORQUE_I(self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.PID_TORQUE_P = self._PID_TORQUE_P(self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _PID_VELOCITY_P_VELOCITY_I(Register):

        class _PID_VELOCITY_I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_VELOCITY_P(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_P", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_VELOCITY_P_VELOCITY_I", parent, access, address, signed)
            self.PID_VELOCITY_I = self._PID_VELOCITY_I(self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.PID_VELOCITY_P = self._PID_VELOCITY_P(self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _PID_POSITION_P_POSITION_I(Register):

        class _PID_POSITION_I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_POSITION_P(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_P", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_POSITION_P_POSITION_I", parent, access, address, signed)
            self.PID_POSITION_I = self._PID_POSITION_I(self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.PID_POSITION_P = self._PID_POSITION_P(self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _PIDOUT_UQ_UD_LIMITS(Register):

        class _PIDOUT_UQ_UD_LIMITS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDOUT_UQ_UD_LIMITS", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PIDOUT_UQ_UD_LIMITS", parent, access, address, signed)
            self.PIDOUT_UQ_UD_LIMITS = self._PIDOUT_UQ_UD_LIMITS(self, Access.RW, 0x0000FFFF,  0, signed=False)

    class _PID_TORQUE_FLUX_LIMITS(Register):

        class _PID_TORQUE_FLUX_LIMITS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_FLUX_LIMITS", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_TORQUE_FLUX_LIMITS", parent, access, address, signed)
            self.PID_TORQUE_FLUX_LIMITS = self._PID_TORQUE_FLUX_LIMITS(self, Access.RW, 0x0000FFFF,  0, signed=False)

    class _PID_VELOCITY_LIMIT(Register):

        class _PID_VELOCITY_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_VELOCITY_LIMIT", parent, access, address, signed)
            self.PID_VELOCITY_LIMIT = self._PID_VELOCITY_LIMIT(self, Access.RW, 0xFFFFFFFF,  0, signed=False)

    class _PID_POSITION_LIMIT_LOW(Register):

        class _PID_POSITION_LIMIT_LOW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_LIMIT_LOW", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_POSITION_LIMIT_LOW", parent, access, address, signed)
            self.PID_POSITION_LIMIT_LOW = self._PID_POSITION_LIMIT_LOW(self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _PID_POSITION_LIMIT_HIGH(Register):

        class _PID_POSITION_LIMIT_HIGH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_LIMIT_HIGH", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_POSITION_LIMIT_HIGH", parent, access, address, signed)
            self.PID_POSITION_LIMIT_HIGH = self._PID_POSITION_LIMIT_HIGH(self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _MODE_RAMP_MODE_MOTION(Register):

        class _MODE_MOTION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MODE_MOTION", parent, access, mask, shift, signed=signed)

                self.choice : _MODE_MOTION_FIELD_CHOICES = {
                    "stopped_mode": Choice(0, self),
                    "torque_mode": Choice(1, self),
                    "velocity_mode": Choice(2, self),
                    "position_mode": Choice(3, self),
                    "prbs_flux_mode": Choice(4, self),
                    "prbs_torque_mode": Choice(5, self),
                    "prbs_velocity_mode": Choice(6, self),
                    "prbs_position_mode": Choice(7, self),
                    "uq_ud_ext": Choice(8, self),
                    "enc_init_mini_move": Choice(9, self),
                    "AGPI_A torque_mode": Choice(10, self),
                    "AGPI_A velocity_mode": Choice(11, self),
                    "AGPI_A position_mode": Choice(12, self),
                    "PWM_I torque_mode": Choice(13, self),
                    "PWM_I velocity_mode": Choice(14, self),
                    "PWM_I position_mode": Choice(15, self),
                }

        class _MODE_RAMP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MODE_RAMP", parent, access, mask, shift, signed=signed)

                self.choice : _MODE_RAMP_FIELD_CHOICES = {
                    "no velocity ramping": Choice(0, self),
                    "reserved": Choice(7, self),
                }

        class _MODE_FF(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MODE_FF", parent, access, mask, shift, signed=signed)

                self.choice : _MODE_FF_FIELD_CHOICES = {
                    "disabled": Choice(0, self),
                    "velocity control": Choice(1, self),
                    "torque control": Choice(2, self),
                }

        class _MODE_PID_SMPL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MODE_PID_SMPL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _MODE_PID_TYPE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MODE_PID_TYPE", parent, access, mask, shift, signed=signed)

                self.choice : _MODE_PID_TYPE_FIELD_CHOICES = {
                    "parallel PI": Choice(0, self),
                    "sequential PI": Choice(1, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("MODE_RAMP_MODE_MOTION", parent, access, address, signed)
            self.MODE_MOTION = self._MODE_MOTION(self, Access.RW, 0x000000FF,  0, signed=False)
            self.MODE_RAMP = self._MODE_RAMP(self, Access.RW, 0x0000FF00,  8, signed=False)
            self.MODE_FF = self._MODE_FF(self, Access.RW, 0x00FF0000, 16, signed=False)
            self.MODE_PID_SMPL = self._MODE_PID_SMPL(self, Access.RW, 0x7F000000, 24, signed=False)
            self.MODE_PID_TYPE = self._MODE_PID_TYPE(self, Access.RW, 0x80000000, 31, signed=False)

    class _PID_TORQUE_FLUX_TARGET(Register):

        class _PID_FLUX_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_TORQUE_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_TORQUE_FLUX_TARGET", parent, access, address, signed)
            self.PID_FLUX_TARGET = self._PID_FLUX_TARGET(self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.PID_TORQUE_TARGET = self._PID_TORQUE_TARGET(self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _PID_TORQUE_FLUX_OFFSET(Register):

        class _PID_FLUX_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_TORQUE_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_TORQUE_FLUX_OFFSET", parent, access, address, signed)
            self.PID_FLUX_OFFSET = self._PID_FLUX_OFFSET(self, Access.RW, 0x0000FFFF,  0, signed=True)
            self.PID_TORQUE_OFFSET = self._PID_TORQUE_OFFSET(self, Access.RW, 0xFFFF0000, 16, signed=True)

    class _PID_VELOCITY_TARGET(Register):

        class _PID_VELOCITY_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_VELOCITY_TARGET", parent, access, address, signed)
            self.PID_VELOCITY_TARGET = self._PID_VELOCITY_TARGET(self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _PID_VELOCITY_OFFSET(Register):

        class _PID_VELOCITY_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_VELOCITY_OFFSET", parent, access, address, signed)
            self.PID_VELOCITY_OFFSET = self._PID_VELOCITY_OFFSET(self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _PID_POSITION_TARGET(Register):

        class _PID_POSITION_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_POSITION_TARGET", parent, access, address, signed)
            self.PID_POSITION_TARGET = self._PID_POSITION_TARGET(self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _PID_TORQUE_FLUX_ACTUAL(Register):

        class _PID_FLUX_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_TORQUE_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_TORQUE_FLUX_ACTUAL", parent, access, address, signed)
            self.PID_FLUX_ACTUAL = self._PID_FLUX_ACTUAL(self, Access.R, 0x0000FFFF,  0, signed=True)
            self.PID_TORQUE_ACTUAL = self._PID_TORQUE_ACTUAL(self, Access.R, 0xFFFF0000, 16, signed=True)

    class _PID_VELOCITY_ACTUAL(Register):

        class _PID_VELOCITY_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_VELOCITY_ACTUAL", parent, access, address, signed)
            self.PID_VELOCITY_ACTUAL = self._PID_VELOCITY_ACTUAL(self, Access.R, 0xFFFFFFFF,  0, signed=True)

    class _PID_POSITION_ACTUAL(Register):

        class _PID_POSITION_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_POSITION_ACTUAL", parent, access, address, signed)
            self.PID_POSITION_ACTUAL = self._PID_POSITION_ACTUAL(self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _PID_ERROR_DATA(Register):

        class _PID_TORQUE_ERROR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_ERROR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_ERROR_DATA", parent, access, address, signed)
            self.PID_TORQUE_ERROR = self._PID_TORQUE_ERROR(self, Access.R, 0xFFFFFFFF,  0, signed=True)

    class _PID_ERROR_ADDR(Register):

        class _PID_ERROR_ADDR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_ERROR_ADDR", parent, access, mask, shift, signed=signed)

                self.choice : _PID_ERROR_ADDR_FIELD_CHOICES = {
                    "PID_TORQUE_ERROR": Choice(0, self),
                    "PID_FLUX_ERROR": Choice(1, self),
                    "PID_VELOCITY_ERROR": Choice(2, self),
                    "PID_POSITION_ERROR": Choice(3, self),
                    "PID_TORQUE_ERROR_SUM": Choice(4, self),
                    "PID_FLUX_ERROR_SUM": Choice(5, self),
                    "PID_VELOCITY_ERROR_SUM": Choice(6, self),
                    "PID_POSITION_ERROR_SUM": Choice(7, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("PID_ERROR_ADDR", parent, access, address, signed)
            self.PID_ERROR_ADDR = self._PID_ERROR_ADDR(self, Access.RW, 0x000000FF,  0, signed=False)

    class _INTERIM_DATA(Register):

        class _PIDIN_TARGET_TORQUE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_TARGET_TORQUE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("INTERIM_DATA", parent, access, address, signed)
            self.PIDIN_TARGET_TORQUE = self._PIDIN_TARGET_TORQUE(self, Access.R, 0xFFFFFFFF,  0, signed=True)

    class _INTERIM_ADDR(Register):

        class _INTERIM_ADDR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INTERIM_ADDR", parent, access, mask, shift, signed=signed)

                self.choice : _INTERIM_ADDR_FIELD_CHOICES = {
                    "PIDIN_TARGET_TORQUE": Choice(0, self),
                    "PIDIN_TARGET_FLUX": Choice(1, self),
                    "PIDIN_TARGET_VELOCITY": Choice(2, self),
                    "PIDIN_TARGET_POSITION": Choice(3, self),
                    "PIDOUT_TARGET_TORQUE": Choice(4, self),
                    "PIDOUT_TARGET_FLUX": Choice(5, self),
                    "PIDOUT_TARGET_VELOCITY": Choice(6, self),
                    "PIDOUT_TARGET_POSITION": Choice(7, self),
                    "FOC_IWY_IUX": Choice(8, self),
                    "FOC_IV": Choice(9, self),
                    "FOC_IB_IA": Choice(10, self),
                    "FOC_IQ_ID": Choice(11, self),
                    "FOC_UQ_UD": Choice(12, self),
                    "FOC_UQ_UD_LIMITED": Choice(13, self),
                    "FOC_UB_UA": Choice(14, self),
                    "FOC_UWY_UUX": Choice(15, self),
                    "FOC_UV": Choice(16, self),
                    "PWM_WY_UX": Choice(17, self),
                    "PWM_UV": Choice(18, self),
                    "ADC_I1_I0": Choice(19, self),
                    "PID_TORQUE_TARGET_FLUX_TARGET_TORQUE_ACTUAL_FLUX_ACTUAL_DIV256": Choice(20, self),
                    "PID_TORQUE_TARGET_TORQUE_ACTUAL": Choice(21, self),
                    "PID_FLUX_TARGET_FLUX_ACTUAL": Choice(22, self),
                    "PID_VELOCITY_TARGET_VELOCITY_ACTUAL_DIV256": Choice(23, self),
                    "PID_VELOCITY_TARGET_VELOCITY_ACTUAL": Choice(24, self),
                    "PID_POSITION_TARGET_POSITION_ACTUAL_DIV256": Choice(25, self),
                    "PID_POSITION_TARGET_POSITION_ACTUAL": Choice(26, self),
                    "FF_VELOCITY": Choice(27, self),
                    "FF_TORQUE": Choice(28, self),
                    "ACTUAL_VELOCITY_PPTM": Choice(29, self),
                    "REF_SWITCH_STATUS": Choice(30, self),
                    "HOME_POSITION": Choice(31, self),
                    "LEFT_POSITION": Choice(32, self),
                    "RIGHT_POSITION": Choice(33, self),
                    "ENC_INIT_HALL_STATUS": Choice(34, self),
                    "ENC_INIT_HALL_PHI_E_ABN_OFFSET": Choice(35, self),
                    "ENC_INIT_HALL_PHI_E_AENC_OFFSET": Choice(36, self),
                    "ENC_INIT_HALL_PHI_A_AENC_OFFSET": Choice(37, self),
                    "enc_init_mini_move_u_d_status": Choice(40, self),
                    "enc_init_mini_move_phi_e_phi_e_offset": Choice(41, self),
                    "SINGLE_PIN_IF_PWM_DUTY_CYCLE_TORQUE_TARGET": Choice(42, self),
                    "SINGLE_PIN_IF_VELOCITY_TARGET": Choice(43, self),
                    "SINGLE_PIN_IF_POSITION_TARGET": Choice(44, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("INTERIM_ADDR", parent, access, address, signed)
            self.INTERIM_ADDR = self._INTERIM_ADDR(self, Access.RW, 0x000000FF,  0, signed=False)

    class _WATCHDOG_CFG(Register):

        class _WATCHDOG_CFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("WATCHDOG_CFG", parent, access, mask, shift, signed=signed)

                self.choice : _WATCHDOG_CFG_FIELD_CHOICES = {
                    "No action on watchdog error": Choice(0, self),
                    "PWM and power stage disable on watchdog error": Choice(1, self),
                    "Global reset on watchdog error": Choice(2, self),
                    "reserved": Choice(3, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("WATCHDOG_CFG", parent, access, address, signed)
            self.WATCHDOG_CFG = self._WATCHDOG_CFG(self, Access.RW, 0x00000003,  0, signed=False)

    class _ADC_VM_LIMITS(Register):

        class _ADC_VM_LIMIT_LOW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_VM_LIMIT_LOW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_VM_LIMIT_HIGH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_VM_LIMIT_HIGH", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_VM_LIMITS", parent, access, address, signed)
            self.ADC_VM_LIMIT_LOW = self._ADC_VM_LIMIT_LOW(self, Access.RW, 0x0000FFFF,  0, signed=False)
            self.ADC_VM_LIMIT_HIGH = self._ADC_VM_LIMIT_HIGH(self, Access.RW, 0xFFFF0000, 16, signed=False)

    class _TMC4671_INPUTS_RAW(Register):

        class _A_of_ABN_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("A_of_ABN_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _B_of_ABN_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("B_of_ABN_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _N_of_ABN_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("N_of_ABN_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _A_of_ABN_2_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("A_of_ABN_2_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _B_of_ABN_2_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("B_of_ABN_2_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _N_of_ABN_2_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("N_of_ABN_2_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_UX_of_HALL_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_UX_of_HALL_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_V_of_HALL_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_V_of_HALL_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_WY_of_HALL_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_WY_of_HALL_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _REF_SW_R_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REF_SW_R_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _REF_SW_H_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REF_SW_H_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _REF_SW_L_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REF_SW_L_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ENABLE_IN_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENABLE_IN_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STP_of_DIRSTP_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STP_of_DIRSTP_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DIR_of_DIRSTP_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIR_of_DIRSTP_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_IN_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_IN_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_UX_FILT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_UX_FILT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_V_FILT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_V_FILT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_WY_FILT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_WY_FILT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_IDLE_L_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_IDLE_L_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_IDLE_H_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_IDLE_H_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("TMC4671_INPUTS_RAW", parent, access, address, signed)
            self.A_of_ABN_RAW = self._A_of_ABN_RAW(self, Access.R, 0x00000001,  0, signed=False)
            self.B_of_ABN_RAW = self._B_of_ABN_RAW(self, Access.R, 0x00000002,  1, signed=False)
            self.N_of_ABN_RAW = self._N_of_ABN_RAW(self, Access.R, 0x00000004,  2, signed=False)
            self.A_of_ABN_2_RAW = self._A_of_ABN_2_RAW(self, Access.R, 0x00000010,  4, signed=False)
            self.B_of_ABN_2_RAW = self._B_of_ABN_2_RAW(self, Access.R, 0x00000020,  5, signed=False)
            self.N_of_ABN_2_RAW = self._N_of_ABN_2_RAW(self, Access.R, 0x00000040,  6, signed=False)
            self.HALL_UX_of_HALL_RAW = self._HALL_UX_of_HALL_RAW(self, Access.R, 0x00000100,  8, signed=False)
            self.HALL_V_of_HALL_RAW = self._HALL_V_of_HALL_RAW(self, Access.R, 0x00000200,  9, signed=False)
            self.HALL_WY_of_HALL_RAW = self._HALL_WY_of_HALL_RAW(self, Access.R, 0x00000400, 10, signed=False)
            self.REF_SW_R_RAW = self._REF_SW_R_RAW(self, Access.R, 0x00001000, 12, signed=False)
            self.REF_SW_H_RAW = self._REF_SW_H_RAW(self, Access.R, 0x00002000, 13, signed=False)
            self.REF_SW_L_RAW = self._REF_SW_L_RAW(self, Access.R, 0x00004000, 14, signed=False)
            self.ENABLE_IN_RAW = self._ENABLE_IN_RAW(self, Access.R, 0x00008000, 15, signed=False)
            self.STP_of_DIRSTP_RAW = self._STP_of_DIRSTP_RAW(self, Access.R, 0x00010000, 16, signed=False)
            self.DIR_of_DIRSTP_RAW = self._DIR_of_DIRSTP_RAW(self, Access.R, 0x00020000, 17, signed=False)
            self.PWM_IN_RAW = self._PWM_IN_RAW(self, Access.R, 0x00040000, 18, signed=False)
            self.HALL_UX_FILT = self._HALL_UX_FILT(self, Access.R, 0x00100000, 20, signed=False)
            self.HALL_V_FILT = self._HALL_V_FILT(self, Access.R, 0x00200000, 21, signed=False)
            self.HALL_WY_FILT = self._HALL_WY_FILT(self, Access.R, 0x00400000, 22, signed=False)
            self.PWM_IDLE_L_RAW = self._PWM_IDLE_L_RAW(self, Access.R, 0x10000000, 28, signed=False)
            self.PWM_IDLE_H_RAW = self._PWM_IDLE_H_RAW(self, Access.R, 0x20000000, 29, signed=False)

    class _TMC4671_OUTPUTS_RAW(Register):

        class _TMC4671_OUTPUTS_RAW_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TMC4671_OUTPUTS_RAW_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TMC4671_OUTPUTS_RAW_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TMC4671_OUTPUTS_RAW_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TMC4671_OUTPUTS_RAW_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TMC4671_OUTPUTS_RAW_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TMC4671_OUTPUTS_RAW_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TMC4671_OUTPUTS_RAW_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TMC4671_OUTPUTS_RAW_4(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TMC4671_OUTPUTS_RAW_4", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TMC4671_OUTPUTS_RAW_5(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TMC4671_OUTPUTS_RAW_5", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TMC4671_OUTPUTS_RAW_6(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TMC4671_OUTPUTS_RAW_6", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TMC4671_OUTPUTS_RAW_7(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TMC4671_OUTPUTS_RAW_7", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("TMC4671_OUTPUTS_RAW", parent, access, address, signed)
            self.TMC4671_OUTPUTS_RAW_0 = self._TMC4671_OUTPUTS_RAW_0(self, Access.R, 0x00000001,  0, signed=False)
            self.TMC4671_OUTPUTS_RAW_1 = self._TMC4671_OUTPUTS_RAW_1(self, Access.R, 0x00000002,  1, signed=False)
            self.TMC4671_OUTPUTS_RAW_2 = self._TMC4671_OUTPUTS_RAW_2(self, Access.R, 0x00000004,  2, signed=False)
            self.TMC4671_OUTPUTS_RAW_3 = self._TMC4671_OUTPUTS_RAW_3(self, Access.R, 0x00000008,  3, signed=False)
            self.TMC4671_OUTPUTS_RAW_4 = self._TMC4671_OUTPUTS_RAW_4(self, Access.R, 0x00000010,  4, signed=False)
            self.TMC4671_OUTPUTS_RAW_5 = self._TMC4671_OUTPUTS_RAW_5(self, Access.R, 0x00000020,  5, signed=False)
            self.TMC4671_OUTPUTS_RAW_6 = self._TMC4671_OUTPUTS_RAW_6(self, Access.R, 0x00000040,  6, signed=False)
            self.TMC4671_OUTPUTS_RAW_7 = self._TMC4671_OUTPUTS_RAW_7(self, Access.R, 0x00000080,  7, signed=False)

    class _STEP_WIDTH(Register):

        class _STEP_WIDTH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STEP_WIDTH", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("STEP_WIDTH", parent, access, address, signed)
            self.STEP_WIDTH = self._STEP_WIDTH(self, Access.RW, 0xFFFFFFFF,  0, signed=True)

    class _UART_BPS(Register):

        class _UART_BPS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UART_BPS", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("UART_BPS", parent, access, address, signed)
            self.UART_BPS = self._UART_BPS(self, Access.RW, 0x03FFFFFF,  0, signed=False)

    class _UART_ADDRS(Register):

        class _ADDR_A(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADDR_A", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADDR_B(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADDR_B", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADDR_C(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADDR_C", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADDR_D(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADDR_D", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("UART_ADDRS", parent, access, address, signed)
            self.ADDR_A = self._ADDR_A(self, Access.RW, 0x000000FF,  0, signed=False)
            self.ADDR_B = self._ADDR_B(self, Access.RW, 0x0000FF00,  8, signed=False)
            self.ADDR_C = self._ADDR_C(self, Access.RW, 0x00FF0000, 16, signed=False)
            self.ADDR_D = self._ADDR_D(self, Access.RW, 0xFF000000, 24, signed=False)

    class _GPIO_dsADCI_CONFIG(Register):

        class _GPIO_dsADCI_CONFIG_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("GPIO_dsADCI_CONFIG_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _GPIO_dsADCI_CONFIG_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("GPIO_dsADCI_CONFIG_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _GPIO_dsADCI_CONFIG_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("GPIO_dsADCI_CONFIG_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _GPIO_dsADCI_CONFIG_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("GPIO_dsADCI_CONFIG_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _GPIO_dsADCI_CONFIG_4(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("GPIO_dsADCI_CONFIG_4", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _GPIO_dsADCI_CONFIG_5(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("GPIO_dsADCI_CONFIG_5", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _GPIO_dsADCI_CONFIG_6(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("GPIO_dsADCI_CONFIG_6", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _GPO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("GPO", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _GPI(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("GPI", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("GPIO_dsADCI_CONFIG", parent, access, address, signed)
            self.GPIO_dsADCI_CONFIG_0 = self._GPIO_dsADCI_CONFIG_0(self, Access.RW, 0x00000001,  0, signed=False)
            self.GPIO_dsADCI_CONFIG_1 = self._GPIO_dsADCI_CONFIG_1(self, Access.RW, 0x00000002,  1, signed=False)
            self.GPIO_dsADCI_CONFIG_2 = self._GPIO_dsADCI_CONFIG_2(self, Access.RW, 0x00000004,  2, signed=False)
            self.GPIO_dsADCI_CONFIG_3 = self._GPIO_dsADCI_CONFIG_3(self, Access.RW, 0x00000008,  3, signed=False)
            self.GPIO_dsADCI_CONFIG_4 = self._GPIO_dsADCI_CONFIG_4(self, Access.RW, 0x00000010,  4, signed=False)
            self.GPIO_dsADCI_CONFIG_5 = self._GPIO_dsADCI_CONFIG_5(self, Access.RW, 0x00000020,  5, signed=False)
            self.GPIO_dsADCI_CONFIG_6 = self._GPIO_dsADCI_CONFIG_6(self, Access.RW, 0x00000040,  6, signed=False)
            self.GPO = self._GPO(self, Access.RW, 0x00FF0000, 16, signed=False)
            self.GPI = self._GPI(self, Access.R, 0xFF000000, 24, signed=False)

    class _STATUS_FLAGS(Register):

        class _STATUS_FLAGS_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_4(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_4", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_5(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_5", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_6(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_6", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_7(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_7", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_8(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_8", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_9(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_9", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_10(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_10", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_11(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_11", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_12(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_12", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_13(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_13", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_14(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_14", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_15(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_15", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_16(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_16", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_17(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_17", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_18(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_18", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_19(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_19", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_20(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_20", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_21(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_21", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_22(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_22", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_23(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_23", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_24(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_24", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_25(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_25", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_26(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_26", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_27(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_27", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_28(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_28", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_29(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_29", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_30(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_30", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLAGS_31(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLAGS_31", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("STATUS_FLAGS", parent, access, address, signed)
            self.STATUS_FLAGS_0 = self._STATUS_FLAGS_0(self, Access.RW, 0x00000001,  0, signed=False)
            self.STATUS_FLAGS_1 = self._STATUS_FLAGS_1(self, Access.RW, 0x00000002,  1, signed=False)
            self.STATUS_FLAGS_2 = self._STATUS_FLAGS_2(self, Access.RW, 0x00000004,  2, signed=False)
            self.STATUS_FLAGS_3 = self._STATUS_FLAGS_3(self, Access.RW, 0x00000008,  3, signed=False)
            self.STATUS_FLAGS_4 = self._STATUS_FLAGS_4(self, Access.RW, 0x00000010,  4, signed=False)
            self.STATUS_FLAGS_5 = self._STATUS_FLAGS_5(self, Access.RW, 0x00000020,  5, signed=False)
            self.STATUS_FLAGS_6 = self._STATUS_FLAGS_6(self, Access.RW, 0x00000040,  6, signed=False)
            self.STATUS_FLAGS_7 = self._STATUS_FLAGS_7(self, Access.RW, 0x00000080,  7, signed=False)
            self.STATUS_FLAGS_8 = self._STATUS_FLAGS_8(self, Access.RW, 0x00000100,  8, signed=False)
            self.STATUS_FLAGS_9 = self._STATUS_FLAGS_9(self, Access.RW, 0x00000200,  9, signed=False)
            self.STATUS_FLAGS_10 = self._STATUS_FLAGS_10(self, Access.RW, 0x00000400, 10, signed=False)
            self.STATUS_FLAGS_11 = self._STATUS_FLAGS_11(self, Access.RW, 0x00000800, 11, signed=False)
            self.STATUS_FLAGS_12 = self._STATUS_FLAGS_12(self, Access.RW, 0x00001000, 12, signed=False)
            self.STATUS_FLAGS_13 = self._STATUS_FLAGS_13(self, Access.RW, 0x00002000, 13, signed=False)
            self.STATUS_FLAGS_14 = self._STATUS_FLAGS_14(self, Access.RW, 0x00004000, 14, signed=False)
            self.STATUS_FLAGS_15 = self._STATUS_FLAGS_15(self, Access.RW, 0x00008000, 15, signed=False)
            self.STATUS_FLAGS_16 = self._STATUS_FLAGS_16(self, Access.RW, 0x00010000, 16, signed=False)
            self.STATUS_FLAGS_17 = self._STATUS_FLAGS_17(self, Access.RW, 0x00020000, 17, signed=False)
            self.STATUS_FLAGS_18 = self._STATUS_FLAGS_18(self, Access.RW, 0x00040000, 18, signed=False)
            self.STATUS_FLAGS_19 = self._STATUS_FLAGS_19(self, Access.RW, 0x00080000, 19, signed=False)
            self.STATUS_FLAGS_20 = self._STATUS_FLAGS_20(self, Access.RW, 0x00100000, 20, signed=False)
            self.STATUS_FLAGS_21 = self._STATUS_FLAGS_21(self, Access.RW, 0x00200000, 21, signed=False)
            self.STATUS_FLAGS_22 = self._STATUS_FLAGS_22(self, Access.RW, 0x00400000, 22, signed=False)
            self.STATUS_FLAGS_23 = self._STATUS_FLAGS_23(self, Access.RW, 0x00800000, 23, signed=False)
            self.STATUS_FLAGS_24 = self._STATUS_FLAGS_24(self, Access.RW, 0x01000000, 24, signed=False)
            self.STATUS_FLAGS_25 = self._STATUS_FLAGS_25(self, Access.RW, 0x02000000, 25, signed=False)
            self.STATUS_FLAGS_26 = self._STATUS_FLAGS_26(self, Access.RW, 0x04000000, 26, signed=False)
            self.STATUS_FLAGS_27 = self._STATUS_FLAGS_27(self, Access.RW, 0x08000000, 27, signed=False)
            self.STATUS_FLAGS_28 = self._STATUS_FLAGS_28(self, Access.RW, 0x10000000, 28, signed=False)
            self.STATUS_FLAGS_29 = self._STATUS_FLAGS_29(self, Access.RW, 0x20000000, 29, signed=False)
            self.STATUS_FLAGS_30 = self._STATUS_FLAGS_30(self, Access.RW, 0x40000000, 30, signed=False)
            self.STATUS_FLAGS_31 = self._STATUS_FLAGS_31(self, Access.RW, 0x80000000, 31, signed=False)

    class _STATUS_MASK(Register):

        class _WARNING_MASK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("WARNING_MASK", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("STATUS_MASK", parent, access, address, signed)
            self.WARNING_MASK = self._WARNING_MASK(self, Access.RW, 0xFFFFFFFF,  0, signed=False)

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

