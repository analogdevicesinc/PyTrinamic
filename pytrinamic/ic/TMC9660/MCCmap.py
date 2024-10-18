################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from typing import TypedDict

from pytrinamic.ic import Access, RegisterGroup, Choice, Field, Register


class MCCMap:

    def __init__(self, block=None):
        self.ALL_REGISTERS = _ALL_REGISTERS(block)


_UX1_SELECT_FIELD_CHOICES = TypedDict("_UX1_SELECT_FIELD_CHOICES", {
    "ADC_I0 ADC_I0": Choice,
    "ADC_I1 ADC_I1": Choice,
    "ADC_I2 ADC_I2": Choice,
    "ADC_I3 ADC_I3": Choice,
})


_VX2_SELECT_FIELD_CHOICES = TypedDict("_VX2_SELECT_FIELD_CHOICES", {
    "ADC_I0 ADC_I0": Choice,
    "ADC_I1 ADC_I1": Choice,
    "ADC_I2 ADC_I2": Choice,
    "ADC_I3 ADC_I3": Choice,
})


_WY1_SELECT_FIELD_CHOICES = TypedDict("_WY1_SELECT_FIELD_CHOICES", {
    "ADC_I0 ADC_I0": Choice,
    "ADC_I1 ADC_I1": Choice,
    "ADC_I2 ADC_I2": Choice,
    "ADC_I3 ADC_I3": Choice,
})


_Y2_SELECT_FIELD_CHOICES = TypedDict("_Y2_SELECT_FIELD_CHOICES", {
    "ADC_I0 ADC_I0": Choice,
    "ADC_I1 ADC_I1": Choice,
    "ADC_I2 ADC_I2": Choice,
    "ADC_I3 ADC_I3": Choice,
})


_MEASUREMENT_MODE_FIELD_CHOICES = TypedDict("_MEASUREMENT_MODE_FIELD_CHOICES", {
    "Inline 3 channel BLDC/2 channel Stepper Inline Shunt Measurement": Choice,
    "VW 2 channels with I_V and I_WY measured (BLDC)": Choice,
    "UW 2 channels with I_UX and I_WY measured (BLDC)": Choice,
    "UV 2 channels with I_UX and I_V measured (BLDC)": Choice,
    "bottom 3/4 phase bottom shunt with automatic switching (BLDC and Stepper)": Choice,
})


_TYPE_FIELD_CHOICES = TypedDict("_TYPE_FIELD_CHOICES", {
    "NONE No motor": Choice,
    "DC Single phase DC motor": Choice,
    "STEPPER Two phase Stepper motor": Choice,
    "BLDC Three phase BLDC motor": Choice,
})


_MOTION_MODE_FIELD_CHOICES = TypedDict("_MOTION_MODE_FIELD_CHOICES", {
    "STOPPED stopped mode": Choice,
    "TORQUE torque mode": Choice,
    "VELOCITY velocity mode": Choice,
    "POSITION position mode": Choice,
    "PRBS_FLUX prbs flux mode": Choice,
    "PRBS_TORQUE prbs torque mode": Choice,
    "PRBS_VELOCITY prbs velocity mode": Choice,
    "PRBS_POSITION prbs position mode": Choice,
    "VOLTAGE_EXT voltage ext mode": Choice,
    "PRBS_UD prbs ud mode": Choice,
    "PWM_EXT pwm ext mode": Choice,
})


_PHI_E_SELECTION_FIELD_CHOICES = TypedDict("_PHI_E_SELECTION_FIELD_CHOICES", {
    "RESERVED reserved": Choice,
    "PHI_E_EXT phi_e_ext": Choice,
    "PHI_E_RAMP phi_e_ramp": Choice,
    "PHI_E_ABN phi_e_abn": Choice,
    "RAMP_X_ACTUAL ramp_X_actual": Choice,
    "PHI_E_HAL phi_e_hal": Choice,
})


_CHOP_FIELD_CHOICES = TypedDict("_CHOP_FIELD_CHOICES", {
    "OFF_FREE PWM off, free running": Choice,
    "OFF_LSON PWM off, Low Side (LS) permanently on": Choice,
    "OFF_HSON PWM off, High Side (HS) permanent on": Choice,
    "OFF_FREE2 PWM off, free running": Choice,
    "OFF_FREE3 PWM off, free running": Choice,
    "LSPWM_HSOFF Low side (LS) PWM, high side (HS) off": Choice,
    "HSPWM_LSOFF High side (HS) PWM, low side (LS) off": Choice,
    "CENTERED Centered PWM for FOC": Choice,
})


_SV_MODE_FIELD_CHOICES = TypedDict("_SV_MODE_FIELD_CHOICES", {
    "DISABLED Space Vector PWM disabled": Choice,
    "HARMONIC Third Harmonic Injection enabled": Choice,
    "BOTTOM Flat Bottom Modulation": Choice,
    "BOTTOM_OFFSET Flat BottomModulation with Offset": Choice,
})


_Y2_HS_SRC_FIELD_CHOICES = TypedDict("_Y2_HS_SRC_FIELD_CHOICES", {
    "Y2_HS Y2_HS": Choice,
    "Y2_ALT Y2_ALT": Choice,
    "TIM_BASIC TIM_BASIC": Choice,
})


_ORDER_FIELD_CHOICES = TypedDict("_ORDER_FIELD_CHOICES", {
    "UVW Hall Signal Order U/V/W": Choice,
    "VWU Hall Signal Order V/W/U": Choice,
    "WUV Hall Signal Order W/U/V": Choice,
    "RESERVED reserved": Choice,
    "UWV Hall Signal Order U/W/V": Choice,
    "VUW Hall Signal Order V/U/W": Choice,
    "WVU Hall Signal Order W/V/U": Choice,
    "RESERVED2 reserved": Choice,
})


_SELECTION_FIELD_CHOICES = TypedDict("_SELECTION_FIELD_CHOICES", {
    "phi_e phi_e selected via PHI_E_SELECTION": Choice,
    "phi_e_ext phi_e_ext": Choice,
    "phi_e_ramp phi_e_ramp": Choice,
    "phi_e_abn phi_e_abn": Choice,
    "ramp_X_actual ramp_X_actual": Choice,
    "phi_e_hal phi_e_hal (Don't use 0x0 with extrapolated Hall)": Choice,
    "phi_m_ext phi_m_ext": Choice,
    "abn_count abn_count": Choice,
    "phi_m_abn phi_m_abn": Choice,
    "hall_count hall_count": Choice,
})


_MOVING_AVRG_FILTER_SAMPLES_FIELD_CHOICES = TypedDict("_MOVING_AVRG_FILTER_SAMPLES_FIELD_CHOICES", {
    "1 No additional filter": Choice,
    "2 Average over 2 samples": Choice,
    "3 Average over 3 samples": Choice,
    "4 Average over 4 samples": Choice,
    "5 Average over 5 samples": Choice,
    "6 Average over 6 samples": Choice,
    "7 Average over 7 samples": Choice,
    "8 Average over 8 samples": Choice,
})


_START_SELECT_FIELD_CHOICES = TypedDict("_START_SELECT_FIELD_CHOICES", {
    "PWM_CENTER center pulse of pwm": Choice,
    "PWM_ZERO zero pulse of pwm": Choice,
    "PWM_LS raw pwm ls generator output": Choice,
    "PWM_HS raw pwm hs generator output": Choice,
    "GDRV_LS_ON gdrv ls output signal": Choice,
    "GDRV_HS_ON gdrv hs output signal": Choice,
    "OCP_LS_CMP raw ls ocp comperator out": Choice,
    "OCP_HS_CMP raw hs ocp comperator out": Choice,
    "VGS_LS_ON raw ls vgs on out": Choice,
    "VGS_HS_ON raw hs vgs on out": Choice,
    "VGS_LS_OFF raw ls vgs off out": Choice,
    "VGS_HS_OFF raw hs vgs off out": Choice,
    "PHASE_HIGH phase voltage greater than 0.9VM": Choice,
    "PHASE_LOW phase voltage less than 0.1VM": Choice,
})


_END_SELECT_FIELD_CHOICES = TypedDict("_END_SELECT_FIELD_CHOICES", {
    "PWM_CENTER center pulse of pwm": Choice,
    "PWM_ZERO zero pulse of pwm": Choice,
    "PWM_LS raw pwm ls generator output": Choice,
    "PWM_HS raw pwm hs generator output": Choice,
    "GDRV_LS_ON gdrv ls output signal": Choice,
    "GDRV_HS_ON gdrv hs output signal": Choice,
    "OCP_LS_CMP raw ls ocp comperator out": Choice,
    "OCP_HS_CMP raw hs ocp comperator out": Choice,
    "VGS_LS_ON raw ls vgs on out": Choice,
    "VGS_HS_ON raw hs vgs on out": Choice,
    "VGS_LS_OFF raw ls vgs off out": Choice,
    "VGS_HS_OFF raw hs vgs off out": Choice,
    "PHASE_HIGH phase voltage greater than 0.9VM": Choice,
    "PHASE_LOW phase voltage less than 0.1VM": Choice,
})


_PHASE_DIV_GAIN_FIELD_CHOICES = TypedDict("_PHASE_DIV_GAIN_FIELD_CHOICES", {
    "PHDIV_80 div80": Choice,
    "PHDIV_40 div40": Choice,
    "PHDIV_20 div20": Choice,
    "PHDIV_10 div10": Choice,
})


_IGATE_SINK_UVW_FIELD_CHOICES = TypedDict("_IGATE_SINK_UVW_FIELD_CHOICES", {
    "SINK_40MA 40 mA": Choice,
    "SINK_80MA 80 mA": Choice,
    "SINK_160MA 160 mA": Choice,
    "SINK_240MA 240 mA": Choice,
    "SINK_320MA 320 mA": Choice,
    "SINK_400MA 400 mA": Choice,
    "SINK_480MA 480 mA": Choice,
    "SINK_560MA 560 mA": Choice,
    "SINK_640MA 640 mA": Choice,
    "SINK_800MA 800 mA": Choice,
    "SINK_960MA 960 mA": Choice,
    "SINK_1120MA 1120 mA": Choice,
    "SINK_1280MA 1280 mA": Choice,
    "SINK_1600MA 1600 mA": Choice,
    "SINK_1920MA 1920 mA": Choice,
    "SINK_2000MA 2000 mA": Choice,
})


_IGATE_SOURCE_UVW_FIELD_CHOICES = TypedDict("_IGATE_SOURCE_UVW_FIELD_CHOICES", {
    "SOURCE_20MA 20 mA": Choice,
    "SOURCE_40MA 40 mA": Choice,
    "SOURCE_80MA 80 mA": Choice,
    "SOURCE_120MA 120 mA": Choice,
    "SOURCE_160MA 160 mA": Choice,
    "SOURCE_200MA 200 mA": Choice,
    "SOURCE_240MA 240 mA": Choice,
    "SOURCE_280MA 280mA": Choice,
    "SOURCE_320MA 320 mA": Choice,
    "SOURCE_400MA 400 mA": Choice,
    "SOURCE_480MA 480 mA": Choice,
    "SOURCE_560MA 560 mA": Choice,
    "SOURCE_640MA 640 mA": Choice,
    "SOURCE_800MA 800 mA": Choice,
    "SOURCE_960MA 960 mA": Choice,
    "SOURCE_1000MA 1000mA": Choice,
})


_IGATE_SINK_Y2_FIELD_CHOICES = TypedDict("_IGATE_SINK_Y2_FIELD_CHOICES", {
    "SINK_40MA 40 mA": Choice,
    "SINK_80MA 80 mA": Choice,
    "SINK_160MA 160 mA": Choice,
    "SINK_240MA 240 mA": Choice,
    "SINK_320MA 320 mA": Choice,
    "SINK_400MA 400 mA": Choice,
    "SINK_480MA 480 mA": Choice,
    "SINK_560MA 560 mA": Choice,
    "SINK_640MA 640 mA": Choice,
    "SINK_800MA 800 mA": Choice,
    "SINK_960MA 960 mA": Choice,
    "SINK_1120MA 1120 mA": Choice,
    "SINK_1280MA 1280 mA": Choice,
    "SINK_1600MA 1600 mA": Choice,
    "SINK_1920MA 1920 mA": Choice,
    "SINK_2000MA 2000 mA": Choice,
})


_IGATE_SOURCE_Y2_FIELD_CHOICES = TypedDict("_IGATE_SOURCE_Y2_FIELD_CHOICES", {
    "SOURCE_20MA 20 mA": Choice,
    "SOURCE_40MA 40 mA": Choice,
    "SOURCE_80MA 80 mA": Choice,
    "SOURCE_120MA 120 mA": Choice,
    "SOURCE_160MA 160 mA": Choice,
    "SOURCE_200MA 200 mA": Choice,
    "SOURCE_240MA 240 mA": Choice,
    "SOURCE_280MA 280mA": Choice,
    "SOURCE_320MA 320 mA": Choice,
    "SOURCE_400MA 400 mA": Choice,
    "SOURCE_480MA 480 mA": Choice,
    "SOURCE_560MA 560 mA": Choice,
    "SOURCE_640MA 640 mA": Choice,
    "SOURCE_800MA 800 mA": Choice,
    "SOURCE_960MA 960 mA": Choice,
    "SOURCE_1000MA 1000mA": Choice,
})


_VS_UVLO_LVL_FIELD_CHOICES = TypedDict("_VS_UVLO_LVL_FIELD_CHOICES", {
    "VSUVLO_44 4.4V": Choice,
    "VSUVLO_46 4.6V": Choice,
    "VSUVLO_48 4.8V": Choice,
    "VSUVLO_50 5.0V": Choice,
    "VSUVLO_52 5.2V": Choice,
    "VSUVLO_54 5.4V": Choice,
    "VSUVLO_56 5.6V": Choice,
    "VSUVLO_58 5.8V": Choice,
    "VSUVLO_60 6.0V": Choice,
    "VSUVLO_63 6.3V": Choice,
    "VSUVLO_66 6.6V": Choice,
    "VSUVLO_69 6.9V": Choice,
    "VSUVLO_72 7.2V": Choice,
    "VSUVLO_75 7.5V": Choice,
    "VSUVLO_78 7.8V": Choice,
    "VSUVLO_81 8.1V": Choice,
})


_VGS_DEGLITCH_UVW_FIELD_CHOICES = TypedDict("_VGS_DEGLITCH_UVW_FIELD_CHOICES", {
    "DEG_OFF off": Choice,
    "DEG_250NS 0.25us": Choice,
    "DEG_500NS 0.5us": Choice,
    "DEG_1000NS 1us": Choice,
    "DEG_2000NS 2us": Choice,
    "DEG_4000NS 4us": Choice,
    "DEG_6000NS 6us": Choice,
    "DEG_8000NS 8us": Choice,
})


_VGS_BLANKING_UVW_FIELD_CHOICES = TypedDict("_VGS_BLANKING_UVW_FIELD_CHOICES", {
    "BLK_OFF off": Choice,
    "BLK_250NS 0.25us": Choice,
    "BLK_500NS 0.5us": Choice,
    "BLK_1000NS 1us": Choice,
})


_VGS_DEGLITCH_Y2_FIELD_CHOICES = TypedDict("_VGS_DEGLITCH_Y2_FIELD_CHOICES", {
    "DEG_OFF off": Choice,
    "DEG_250NS 0.25us": Choice,
    "DEG_500NS 0.5us": Choice,
    "DEG_1000NS 1us": Choice,
    "DEG_2000NS 2us": Choice,
    "DEG_4000NS 4us": Choice,
    "DEG_6000NS 6us": Choice,
    "DEG_8000NS 8us": Choice,
})


_VGS_BLANKING_Y2_FIELD_CHOICES = TypedDict("_VGS_BLANKING_Y2_FIELD_CHOICES", {
    "BLK_OFF off": Choice,
    "BLK_250NS 0.25us": Choice,
    "BLK_500NS 0.5us": Choice,
    "BLK_1000NS 1us": Choice,
})


_LS_RETRIES_UVW_FIELD_CHOICES = TypedDict("_LS_RETRIES_UVW_FIELD_CHOICES", {
    "OFF No Retries": Choice,
    "ONE 1 Retry": Choice,
    "TWO 2 Retries": Choice,
    "THREE 3 Retries": Choice,
})


_HS_RETRIES_UVW_FIELD_CHOICES = TypedDict("_HS_RETRIES_UVW_FIELD_CHOICES", {
    "OFF No Retries": Choice,
    "ONE 1 Retry": Choice,
    "TWO 2 Retries": Choice,
    "THREE 3 Retries": Choice,
})


_LS_RETRIES_Y2_FIELD_CHOICES = TypedDict("_LS_RETRIES_Y2_FIELD_CHOICES", {
    "OFF No Retries": Choice,
    "ONE 1 Retry": Choice,
    "TWO 2 Retries": Choice,
    "THREE 3 Retries": Choice,
})


_HS_RETRIES_Y2_FIELD_CHOICES = TypedDict("_HS_RETRIES_Y2_FIELD_CHOICES", {
    "OFF No Retries": Choice,
    "ONE 1 Retry": Choice,
    "TWO 2 Retries": Choice,
    "THREE 3 Retries": Choice,
})


_LS_OCP_DEGLITCH_UVW_FIELD_CHOICES = TypedDict("_LS_OCP_DEGLITCH_UVW_FIELD_CHOICES", {
    "DEG_OFF off": Choice,
    "DEG_250NS 0.25us": Choice,
    "DEG_500NS 0.5us": Choice,
    "DEG_1000NS 1us": Choice,
    "DEG_2000NS 2us": Choice,
    "DEG_4000NS 4us": Choice,
    "DEG_6000NS 6us": Choice,
    "DEG_8000NS 8us": Choice,
})


_LS_OCP_BLANKING_UVW_FIELD_CHOICES = TypedDict("_LS_OCP_BLANKING_UVW_FIELD_CHOICES", {
    "BLK_OFF off": Choice,
    "BLK_250NS 0.25us": Choice,
    "BLK_500NS 0.5us": Choice,
    "BLK_1000NS 1us": Choice,
    "BLK_2000NS 2us": Choice,
    "BLK_4000NS 4us": Choice,
    "BLK_6000NS 6us": Choice,
    "BLK_8000NS 8us": Choice,
})


_LS_OCP_THRES_UVW_FIELD_CHOICES = TypedDict("_LS_OCP_THRES_UVW_FIELD_CHOICES", {
    "82mv 63mv": Choice,
    "166mv 125mv": Choice,
    "248mv 187mv": Choice,
    "330mv 248mv": Choice,
    "414mv 312mv": Choice,
    "498mv 374mv": Choice,
    "582mv 434mv": Choice,
    "660mv 504mv": Choice,
    "123mv 705mv": Choice,
    "249mv 940mv": Choice,
    "372mv 1180mv": Choice,
    "495mv 1410mv": Choice,
    "621mv 1650mv": Choice,
    "747mv 1880mv": Choice,
    "873mv 2110mv": Choice,
    "990mv 2350mv": Choice,
})


_HS_OCP_DEGLITCH_UVW_FIELD_CHOICES = TypedDict("_HS_OCP_DEGLITCH_UVW_FIELD_CHOICES", {
    "DEG_OFF off": Choice,
    "DEG_250NS 0.25us": Choice,
    "DEG_500NS 0.5us": Choice,
    "DEG_1000NS 1us": Choice,
    "DEG_2000NS 2us": Choice,
    "DEG_4000NS 4us": Choice,
    "DEG_6000NS 6us": Choice,
    "DEG_8000NS 8us": Choice,
})


_HS_OCP_BLANKING_UVW_FIELD_CHOICES = TypedDict("_HS_OCP_BLANKING_UVW_FIELD_CHOICES", {
    "BLK_OFF off": Choice,
    "BLK_250NS 0.25us": Choice,
    "BLK_500NS 0.5us": Choice,
    "BLK_1000NS 1us": Choice,
    "BLK_2000NS 2us": Choice,
    "BLK_4000NS 4us": Choice,
    "BLK_6000NS 6us": Choice,
    "BLK_8000NS 8us": Choice,
})


_LS_OCP_DEGLITCH_Y2_FIELD_CHOICES = TypedDict("_LS_OCP_DEGLITCH_Y2_FIELD_CHOICES", {
    "DEG_OFF off": Choice,
    "DEG_250NS 0.25us": Choice,
    "DEG_500NS 0.5us": Choice,
    "DEG_1000NS 1us": Choice,
    "DEG_2000NS 2us": Choice,
    "DEG_4000NS 4us": Choice,
    "DEG_6000NS 6us": Choice,
    "DEG_8000NS 8us": Choice,
})


_LS_OCP_BLANKING_Y2_FIELD_CHOICES = TypedDict("_LS_OCP_BLANKING_Y2_FIELD_CHOICES", {
    "BLK_OFF off": Choice,
    "BLK_250NS 0.25us": Choice,
    "BLK_500NS 0.5us": Choice,
    "BLK_1000NS 1us": Choice,
    "BLK_2000NS 2us": Choice,
    "BLK_4000NS 4us": Choice,
    "BLK_6000NS 6us": Choice,
    "BLK_8000NS 8us": Choice,
})


_LS_OCP_THRES_Y2_FIELD_CHOICES = TypedDict("_LS_OCP_THRES_Y2_FIELD_CHOICES", {
    "82mv 63mv": Choice,
    "166mv 125mv": Choice,
    "248mv 187mv": Choice,
    "330mv 248mv": Choice,
    "414mv 312mv": Choice,
    "498mv 374mv": Choice,
    "582mv 434mv": Choice,
    "660mv 504mv": Choice,
    "123mv 705mv": Choice,
    "249mv 940mv": Choice,
    "372mv 1180mv": Choice,
    "495mv 1410mv": Choice,
    "621mv 1650mv": Choice,
    "747mv 1880mv": Choice,
    "873mv 2110mv": Choice,
    "990mv 2350mv": Choice,
})


_HS_OCP_DEGLITCH_Y2_FIELD_CHOICES = TypedDict("_HS_OCP_DEGLITCH_Y2_FIELD_CHOICES", {
    "DEG_OFF off": Choice,
    "DEG_250NS 0.25us": Choice,
    "DEG_500NS 0.5us": Choice,
    "DEG_1000NS 1us": Choice,
    "DEG_2000NS 2us": Choice,
    "DEG_4000NS 4us": Choice,
    "DEG_6000NS 6us": Choice,
    "DEG_8000NS 8us": Choice,
})


_HS_OCP_BLANKING_Y2_FIELD_CHOICES = TypedDict("_HS_OCP_BLANKING_Y2_FIELD_CHOICES", {
    "BLK_OFF off": Choice,
    "BLK_250NS 0.25us": Choice,
    "BLK_500NS 0.5us": Choice,
    "BLK_1000NS 1us": Choice,
    "BLK_2000NS 2us": Choice,
    "BLK_4000NS 4us": Choice,
    "BLK_6000NS 6us": Choice,
    "BLK_8000NS 8us": Choice,
})


class _ALL_REGISTERS(RegisterGroup):

    class _INFO_CHIP(Register):

        class _ID(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ID", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PREFIX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PREFIX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("INFO_CHIP", parent, access, address, block, signed)
            self.ID      =  self._ID(self,      Access.R,  0x0000FFFF,  0,   signed=False)
            self.PREFIX  =  self._PREFIX(self,  Access.R,  0xFFFF0000,  16,  signed=False)

    class _INFO_VARIANT(Register):

        class _PMU_VAR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PMU_VAR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _GDRV_VAR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("GDRV_VAR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ENABLE_JTAG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENABLE_JTAG", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("INFO_VARIANT", parent, access, address, block, signed)
            self.PMU_VAR      =  self._PMU_VAR(self,      Access.R,  0x00000003,  0,   signed=False)
            self.GDRV_VAR     =  self._GDRV_VAR(self,     Access.R,  0x0000000C,  2,   signed=False)
            self.ENABLE_JTAG  =  self._ENABLE_JTAG(self,  Access.R,  0x80000000,  31,  signed=False)

    class _INFO_REVISION(Register):

        class _REVISION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REVISION", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IS_FPGA(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IS_FPGA", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("INFO_REVISION", parent, access, address, block, signed)
            self.REVISION  =  self._REVISION(self,  Access.R,  0x7FFFFFFF,  0,   signed=False)
            self.IS_FPGA   =  self._IS_FPGA(self,   Access.R,  0x80000000,  31,  signed=False)

    class _INFO_DATE(Register):

        class _MINUTE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MINUTE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HOUR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HOUR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DAY(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DAY", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _MONTH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MONTH", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _YEAR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("YEAR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("INFO_DATE", parent, access, address, block, signed)
            self.MINUTE  =  self._MINUTE(self,  Access.R,  0x0000003F,  0,   signed=False)
            self.HOUR    =  self._HOUR(self,    Access.R,  0x000007C0,  6,   signed=False)
            self.DAY     =  self._DAY(self,     Access.R,  0x0000F800,  11,  signed=False)
            self.MONTH   =  self._MONTH(self,   Access.R,  0x000F0000,  16,  signed=False)
            self.YEAR    =  self._YEAR(self,    Access.R,  0xFFF00000,  20,  signed=False)

    class _ADC_I1_I0_RAW(Register):

        class _ADC_RAW_I0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_RAW_I0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_RAW_I1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_RAW_I1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I1_I0_RAW", parent, access, address, block, signed)
            self.ADC_RAW_I0  =  self._ADC_RAW_I0(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.ADC_RAW_I1  =  self._ADC_RAW_I1(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ADC_I3_I2_RAW(Register):

        class _ADC_RAW_I2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_RAW_I2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_RAW_I3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_RAW_I3", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I3_I2_RAW", parent, access, address, block, signed)
            self.ADC_RAW_I2  =  self._ADC_RAW_I2(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.ADC_RAW_I3  =  self._ADC_RAW_I3(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ADC_U1_U0_RAW(Register):

        class _ADC_RAW_U0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_RAW_U0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_RAW_U1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_RAW_U1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_U1_U0_RAW", parent, access, address, block, signed)
            self.ADC_RAW_U0  =  self._ADC_RAW_U0(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.ADC_RAW_U1  =  self._ADC_RAW_U1(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ADC_U3_U2_RAW(Register):

        class _ADC_RAW_U2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_RAW_U2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_RAW_U3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_RAW_U3", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_U3_U2_RAW", parent, access, address, block, signed)
            self.ADC_RAW_U2  =  self._ADC_RAW_U2(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.ADC_RAW_U3  =  self._ADC_RAW_U3(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ADC_TEMP_VM_RAW(Register):

        class _ADC_RAW_VM(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_RAW_VM", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_RAW_TEMP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_RAW_TEMP", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_TEMP_VM_RAW", parent, access, address, block, signed)
            self.ADC_RAW_VM    =  self._ADC_RAW_VM(self,    Access.R,  0x0000FFFF,  0,   signed=True)
            self.ADC_RAW_TEMP  =  self._ADC_RAW_TEMP(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ADC_AIN1_AIN0_RAW(Register):

        class _AIN0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AIN1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_AIN1_AIN0_RAW", parent, access, address, block, signed)
            self.AIN0  =  self._AIN0(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.AIN1  =  self._AIN1(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ADC_AIN3_AIN2_RAW(Register):

        class _AIN2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AIN3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN3", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_AIN3_AIN2_RAW", parent, access, address, block, signed)
            self.AIN2  =  self._AIN2(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.AIN3  =  self._AIN3(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ADC_I_GEN_CONFIG(Register):

        class _UX1_SELECT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UX1_SELECT", parent, access, mask, shift, signed=signed)

                self.choice : _UX1_SELECT_FIELD_CHOICES = {
                    "ADC_I0 ADC_I0": Choice(0, self),
                    "ADC_I1 ADC_I1": Choice(1, self),
                    "ADC_I2 ADC_I2": Choice(2, self),
                    "ADC_I3 ADC_I3": Choice(3, self),
                }

        class _VX2_SELECT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VX2_SELECT", parent, access, mask, shift, signed=signed)

                self.choice : _VX2_SELECT_FIELD_CHOICES = {
                    "ADC_I0 ADC_I0": Choice(0, self),
                    "ADC_I1 ADC_I1": Choice(1, self),
                    "ADC_I2 ADC_I2": Choice(2, self),
                    "ADC_I3 ADC_I3": Choice(3, self),
                }

        class _WY1_SELECT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("WY1_SELECT", parent, access, mask, shift, signed=signed)

                self.choice : _WY1_SELECT_FIELD_CHOICES = {
                    "ADC_I0 ADC_I0": Choice(0, self),
                    "ADC_I1 ADC_I1": Choice(1, self),
                    "ADC_I2 ADC_I2": Choice(2, self),
                    "ADC_I3 ADC_I3": Choice(3, self),
                }

        class _Y2_SELECT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("Y2_SELECT", parent, access, mask, shift, signed=signed)

                self.choice : _Y2_SELECT_FIELD_CHOICES = {
                    "ADC_I0 ADC_I0": Choice(0, self),
                    "ADC_I1 ADC_I1": Choice(1, self),
                    "ADC_I2 ADC_I2": Choice(2, self),
                    "ADC_I3 ADC_I3": Choice(3, self),
                }

        class _SOURCE_SELECT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SOURCE_SELECT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _MEASUREMENT_MODE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MEASUREMENT_MODE", parent, access, mask, shift, signed=signed)

                self.choice : _MEASUREMENT_MODE_FIELD_CHOICES = {
                    "Inline 3 channel BLDC/2 channel Stepper Inline Shunt Measurement": Choice(0, self),
                    "VW 2 channels with I_V and I_WY measured (BLDC)": Choice(1, self),
                    "UW 2 channels with I_UX and I_WY measured (BLDC)": Choice(2, self),
                    "UV 2 channels with I_UX and I_V measured (BLDC)": Choice(3, self),
                    "bottom 3/4 phase bottom shunt with automatic switching (BLDC and Stepper)": Choice(4, self),
                }

        class _TRIGGER_SELECT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TRIGGER_SELECT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TRIGGER_POS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TRIGGER_POS", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I_GEN_CONFIG", parent, access, address, block, signed)
            self.UX1_SELECT        =  self._UX1_SELECT(self,        Access.RW,  0x00000003,  0,   signed=False)
            self.VX2_SELECT        =  self._VX2_SELECT(self,        Access.RW,  0x0000000C,  2,   signed=False)
            self.WY1_SELECT        =  self._WY1_SELECT(self,        Access.RW,  0x00000030,  4,   signed=False)
            self.Y2_SELECT         =  self._Y2_SELECT(self,         Access.RW,  0x000000C0,  6,   signed=False)
            self.SOURCE_SELECT     =  self._SOURCE_SELECT(self,     Access.RW,  0x00000100,  8,   signed=False)
            self.MEASUREMENT_MODE  =  self._MEASUREMENT_MODE(self,  Access.RW,  0x00000E00,  9,   signed=False)
            self.TRIGGER_SELECT    =  self._TRIGGER_SELECT(self,    Access.RW,  0x00001000,  12,  signed=False)
            self.TRIGGER_POS       =  self._TRIGGER_POS(self,       Access.RW,  0xFFFF0000,  16,  signed=False)

    class _ADC_I0_CONFIG(Register):

        class _OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SCALE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SCALE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I0_CONFIG", parent, access, address, block, signed)
            self.OFFSET  =  self._OFFSET(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.SCALE   =  self._SCALE(self,   Access.RW,  0xFFFF0000,  16,  signed=True)

    class _ADC_I1_CONFIG(Register):

        class _OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SCALE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SCALE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I1_CONFIG", parent, access, address, block, signed)
            self.OFFSET  =  self._OFFSET(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.SCALE   =  self._SCALE(self,   Access.RW,  0xFFFF0000,  16,  signed=True)

    class _ADC_I2_CONFIG(Register):

        class _OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SCALE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SCALE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I2_CONFIG", parent, access, address, block, signed)
            self.OFFSET  =  self._OFFSET(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.SCALE   =  self._SCALE(self,   Access.RW,  0xFFFF0000,  16,  signed=True)

    class _ADC_I3_CONFIG(Register):

        class _OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SCALE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SCALE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I3_CONFIG", parent, access, address, block, signed)
            self.OFFSET  =  self._OFFSET(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.SCALE   =  self._SCALE(self,   Access.RW,  0xFFFF0000,  16,  signed=True)

    class _ADC_I1_I0_SCALED(Register):

        class _ADC_SCALED_I0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_SCALED_I0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_SCALED_I1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_SCALED_I1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I1_I0_SCALED", parent, access, address, block, signed)
            self.ADC_SCALED_I0  =  self._ADC_SCALED_I0(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.ADC_SCALED_I1  =  self._ADC_SCALED_I1(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ADC_I3_I2_SCALED(Register):

        class _ADC_SCALED_I2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_SCALED_I2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_SCALED_I3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_SCALED_I3", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I3_I2_SCALED", parent, access, address, block, signed)
            self.ADC_SCALED_I2  =  self._ADC_SCALED_I2(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.ADC_SCALED_I3  =  self._ADC_SCALED_I3(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ADC_IWY_IUX(Register):

        class _ADC_IUX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_IUX", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_IWY(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_IWY", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_IWY_IUX", parent, access, address, block, signed)
            self.ADC_IUX  =  self._ADC_IUX(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.ADC_IWY  =  self._ADC_IWY(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ADC_IV(Register):

        class _ADC_IV(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_IV", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_IV", parent, access, address, block, signed)
            self.ADC_IV  =  self._ADC_IV(self,  Access.R,  0x0000FFFF,  0,  signed=True)

    class _ADC_STATUS(Register):

        class _I0_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I0_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _I1_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I1_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _I2_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I2_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _I3_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I3_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _U0_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U0_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _U1_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U1_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _U2_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U2_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _U3_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U3_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AIN0_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN0_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AIN1_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN1_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AIN2_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN2_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AIN3_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN3_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VM_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VM_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TEMP_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TEMP_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _I0_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I0_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _I1_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I1_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _I2_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I2_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _I3_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I3_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _U0_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U0_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _U1_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U1_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _U2_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U2_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _U3_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U3_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AIN0_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN0_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AIN1_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN1_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AIN2_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN2_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AIN3_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN3_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VM_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VM_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TEMP_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TEMP_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_STATUS", parent, access, address, block, signed)
            self.I0_CLIPPED    =  self._I0_CLIPPED(self,    Access.RWC,  0x00000001,  0,   signed=False)
            self.I1_CLIPPED    =  self._I1_CLIPPED(self,    Access.RWC,  0x00000002,  1,   signed=False)
            self.I2_CLIPPED    =  self._I2_CLIPPED(self,    Access.RWC,  0x00000004,  2,   signed=False)
            self.I3_CLIPPED    =  self._I3_CLIPPED(self,    Access.RWC,  0x00000008,  3,   signed=False)
            self.U0_CLIPPED    =  self._U0_CLIPPED(self,    Access.RWC,  0x00000010,  4,   signed=False)
            self.U1_CLIPPED    =  self._U1_CLIPPED(self,    Access.RWC,  0x00000020,  5,   signed=False)
            self.U2_CLIPPED    =  self._U2_CLIPPED(self,    Access.RWC,  0x00000040,  6,   signed=False)
            self.U3_CLIPPED    =  self._U3_CLIPPED(self,    Access.RWC,  0x00000080,  7,   signed=False)
            self.AIN0_CLIPPED  =  self._AIN0_CLIPPED(self,  Access.RWC,  0x00000100,  8,   signed=False)
            self.AIN1_CLIPPED  =  self._AIN1_CLIPPED(self,  Access.RWC,  0x00000200,  9,   signed=False)
            self.AIN2_CLIPPED  =  self._AIN2_CLIPPED(self,  Access.RWC,  0x00000400,  10,  signed=False)
            self.AIN3_CLIPPED  =  self._AIN3_CLIPPED(self,  Access.RWC,  0x00000800,  11,  signed=False)
            self.VM_CLIPPED    =  self._VM_CLIPPED(self,    Access.RWC,  0x00001000,  12,  signed=False)
            self.TEMP_CLIPPED  =  self._TEMP_CLIPPED(self,  Access.RWC,  0x00002000,  13,  signed=False)
            self.I0_DONE       =  self._I0_DONE(self,       Access.RWC,  0x00010000,  16,  signed=False)
            self.I1_DONE       =  self._I1_DONE(self,       Access.RWC,  0x00020000,  17,  signed=False)
            self.I2_DONE       =  self._I2_DONE(self,       Access.RWC,  0x00040000,  18,  signed=False)
            self.I3_DONE       =  self._I3_DONE(self,       Access.RWC,  0x00080000,  19,  signed=False)
            self.U0_DONE       =  self._U0_DONE(self,       Access.RWC,  0x00100000,  20,  signed=False)
            self.U1_DONE       =  self._U1_DONE(self,       Access.RWC,  0x00200000,  21,  signed=False)
            self.U2_DONE       =  self._U2_DONE(self,       Access.RWC,  0x00400000,  22,  signed=False)
            self.U3_DONE       =  self._U3_DONE(self,       Access.RWC,  0x00800000,  23,  signed=False)
            self.AIN0_DONE     =  self._AIN0_DONE(self,     Access.RWC,  0x01000000,  24,  signed=False)
            self.AIN1_DONE     =  self._AIN1_DONE(self,     Access.RWC,  0x02000000,  25,  signed=False)
            self.AIN2_DONE     =  self._AIN2_DONE(self,     Access.RWC,  0x04000000,  26,  signed=False)
            self.AIN3_DONE     =  self._AIN3_DONE(self,     Access.RWC,  0x08000000,  27,  signed=False)
            self.VM_DONE       =  self._VM_DONE(self,       Access.RWC,  0x10000000,  28,  signed=False)
            self.TEMP_DONE     =  self._TEMP_DONE(self,     Access.RWC,  0x20000000,  29,  signed=False)

    class _MOTOR_CONFIG(Register):

        class _N_POLE_PAIRS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("N_POLE_PAIRS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TYPE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TYPE", parent, access, mask, shift, signed=signed)

                self.choice : _TYPE_FIELD_CHOICES = {
                    "NONE No motor": Choice(0, self),
                    "DC Single phase DC motor": Choice(1, self),
                    "STEPPER Two phase Stepper motor": Choice(2, self),
                    "BLDC Three phase BLDC motor": Choice(3, self),
                }

        def __init__(self, parent, access, address, block, signed):
            super().__init__("MOTOR_CONFIG", parent, access, address, block, signed)
            self.N_POLE_PAIRS  =  self._N_POLE_PAIRS(self,  Access.RW,  0x0000007F,  0,   signed=False)
            self.TYPE          =  self._TYPE(self,          Access.RW,  0x00030000,  16,  signed=False)

    class _MOTION_CONFIG(Register):

        class _MOTION_MODE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MOTION_MODE", parent, access, mask, shift, signed=signed)

                self.choice : _MOTION_MODE_FIELD_CHOICES = {
                    "STOPPED stopped mode": Choice(0, self),
                    "TORQUE torque mode": Choice(1, self),
                    "VELOCITY velocity mode": Choice(2, self),
                    "POSITION position mode": Choice(3, self),
                    "PRBS_FLUX prbs flux mode": Choice(4, self),
                    "PRBS_TORQUE prbs torque mode": Choice(5, self),
                    "PRBS_VELOCITY prbs velocity mode": Choice(6, self),
                    "PRBS_POSITION prbs position mode": Choice(7, self),
                    "VOLTAGE_EXT voltage ext mode": Choice(8, self),
                    "PRBS_UD prbs ud mode": Choice(9, self),
                    "PWM_EXT pwm ext mode": Choice(10, self),
                }

        class _RAMP_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _RAMP_MODE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_MODE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _FEEDFORWARD(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FEEDFORWARD", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("MOTION_CONFIG", parent, access, address, block, signed)
            self.MOTION_MODE  =  self._MOTION_MODE(self,  Access.RW,  0x0000000F,  0,  signed=False)
            self.RAMP_ENABLE  =  self._RAMP_ENABLE(self,  Access.RW,  0x00000010,  4,  signed=False)
            self.RAMP_MODE    =  self._RAMP_MODE(self,    Access.RW,  0x00000020,  5,  signed=False)
            self.FEEDFORWARD  =  self._FEEDFORWARD(self,  Access.RW,  0x000000C0,  6,  signed=False)

    class _PHI_E_SELECTION(Register):

        class _PHI_E_SELECTION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_E_SELECTION", parent, access, mask, shift, signed=signed)

                self.choice : _PHI_E_SELECTION_FIELD_CHOICES = {
                    "RESERVED reserved": Choice(0, self),
                    "PHI_E_EXT phi_e_ext": Choice(1, self),
                    "PHI_E_RAMP phi_e_ramp": Choice(2, self),
                    "PHI_E_ABN phi_e_abn": Choice(3, self),
                    "RAMP_X_ACTUAL ramp_X_actual": Choice(4, self),
                    "PHI_E_HAL phi_e_hal": Choice(5, self),
                }

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PHI_E_SELECTION", parent, access, address, block, signed)
            self.PHI_E_SELECTION  =  self._PHI_E_SELECTION(self,  Access.RW,  0x0000000F,  0,  signed=False)

    class _PHI_E(Register):

        class _PHI_E(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_E", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PHI_E", parent, access, address, block, signed)
            self.PHI_E  =  self._PHI_E(self,  Access.R,  0x0000FFFF,  0,  signed=True)

    class _PWM_CONFIG(Register):

        class _CHOP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CHOP", parent, access, mask, shift, signed=signed)

                self.choice : _CHOP_FIELD_CHOICES = {
                    "OFF_FREE PWM off, free running": Choice(0, self),
                    "OFF_LSON PWM off, Low Side (LS) permanently on": Choice(1, self),
                    "OFF_HSON PWM off, High Side (HS) permanent on": Choice(2, self),
                    "OFF_FREE2 PWM off, free running": Choice(3, self),
                    "OFF_FREE3 PWM off, free running": Choice(4, self),
                    "LSPWM_HSOFF Low side (LS) PWM, high side (HS) off": Choice(5, self),
                    "HSPWM_LSOFF High side (HS) PWM, low side (LS) off": Choice(6, self),
                    "CENTERED Centered PWM for FOC": Choice(7, self),
                }

        class _SV_MODE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SV_MODE", parent, access, mask, shift, signed=signed)

                self.choice : _SV_MODE_FIELD_CHOICES = {
                    "DISABLED Space Vector PWM disabled": Choice(0, self),
                    "HARMONIC Third Harmonic Injection enabled": Choice(1, self),
                    "BOTTOM Flat Bottom Modulation": Choice(2, self),
                    "BOTTOM_OFFSET Flat BottomModulation with Offset": Choice(3, self),
                }

        class _Y2_HS_SRC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("Y2_HS_SRC", parent, access, mask, shift, signed=signed)

                self.choice : _Y2_HS_SRC_FIELD_CHOICES = {
                    "Y2_HS Y2_HS": Choice(0, self),
                    "Y2_ALT Y2_ALT": Choice(1, self),
                    "TIM_BASIC TIM_BASIC": Choice(2, self),
                }

        class _ENABLE_UX1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENABLE_UX1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ENABLE_VX2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENABLE_VX2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ENABLE_WY1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENABLE_WY1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ENABLE_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENABLE_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EXT_ENABLE_UX1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXT_ENABLE_UX1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EXT_ENABLE_VX2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXT_ENABLE_VX2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EXT_ENABLE_WY1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXT_ENABLE_WY1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EXT_ENABLE_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXT_ENABLE_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DUTY_CYCLE_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DUTY_CYCLE_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PWM_CONFIG", parent, access, address, block, signed)
            self.CHOP               =  self._CHOP(self,               Access.RW,  0x00000007,  0,   signed=False)
            self.SV_MODE            =  self._SV_MODE(self,            Access.RW,  0x00000030,  4,   signed=False)
            self.Y2_HS_SRC          =  self._Y2_HS_SRC(self,          Access.RW,  0x000000C0,  6,   signed=False)
            self.ENABLE_UX1         =  self._ENABLE_UX1(self,         Access.RW,  0x00000100,  8,   signed=False)
            self.ENABLE_VX2         =  self._ENABLE_VX2(self,         Access.RW,  0x00000200,  9,   signed=False)
            self.ENABLE_WY1         =  self._ENABLE_WY1(self,         Access.RW,  0x00000400,  10,  signed=False)
            self.ENABLE_Y2          =  self._ENABLE_Y2(self,          Access.RW,  0x00000800,  11,  signed=False)
            self.EXT_ENABLE_UX1     =  self._EXT_ENABLE_UX1(self,     Access.RW,  0x00001000,  12,  signed=False)
            self.EXT_ENABLE_VX2     =  self._EXT_ENABLE_VX2(self,     Access.RW,  0x00002000,  13,  signed=False)
            self.EXT_ENABLE_WY1     =  self._EXT_ENABLE_WY1(self,     Access.RW,  0x00004000,  14,  signed=False)
            self.EXT_ENABLE_Y2      =  self._EXT_ENABLE_Y2(self,      Access.RW,  0x00008000,  15,  signed=False)
            self.DUTY_CYCLE_OFFSET  =  self._DUTY_CYCLE_OFFSET(self,  Access.RW,  0xFFFF0000,  16,  signed=False)

    class _PWM_MAXCNT(Register):

        class _PWM_MAXCNT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_MAXCNT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PWM_MAXCNT", parent, access, address, block, signed)
            self.PWM_MAXCNT  =  self._PWM_MAXCNT(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

    class _PWM_SWITCH_LIMIT(Register):

        class _PWM_SWITCH_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_SWITCH_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PWM_SWITCH_LIMIT", parent, access, address, block, signed)
            self.PWM_SWITCH_LIMIT  =  self._PWM_SWITCH_LIMIT(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

    class _PWM_WATCHDOG_CFG(Register):

        class _ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DIV2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIV2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TRIGGER(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TRIGGER", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PWM_WATCHDOG_CFG", parent, access, address, block, signed)
            self.ENABLE   =  self._ENABLE(self,   Access.RW,  0x00000001,  0,  signed=False)
            self.DIV2     =  self._DIV2(self,     Access.RW,  0x00000002,  1,  signed=False)
            self.TRIGGER  =  self._TRIGGER(self,  Access.RW,  0x00000004,  2,  signed=False)

    class _ABN_PHI_E_PHI_M(Register):

        class _ABN_PHI_M(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_PHI_M", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ABN_PHI_E(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_PHI_E", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ABN_PHI_E_PHI_M", parent, access, address, block, signed)
            self.ABN_PHI_M  =  self._ABN_PHI_M(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.ABN_PHI_E  =  self._ABN_PHI_E(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ABN_MODE(Register):

        class _A_POL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("A_POL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _B_POL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("B_POL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _N_POL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("N_POL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COMBINED_N(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COMBINED_N", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CLEAR_COUNT_ON_N(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLEAR_COUNT_ON_N", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DISABLE_FILTER(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DISABLE_FILTER", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CLN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DIRECTION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIRECTION", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ABN_MODE", parent, access, address, block, signed)
            self.A_POL             =  self._A_POL(self,             Access.RW,  0x00000001,  0,   signed=False)
            self.B_POL             =  self._B_POL(self,             Access.RW,  0x00000002,  1,   signed=False)
            self.N_POL             =  self._N_POL(self,             Access.RW,  0x00000004,  2,   signed=False)
            self.COMBINED_N        =  self._COMBINED_N(self,        Access.RW,  0x00000008,  3,   signed=False)
            self.CLEAR_COUNT_ON_N  =  self._CLEAR_COUNT_ON_N(self,  Access.RW,  0x00000010,  4,   signed=False)
            self.DISABLE_FILTER    =  self._DISABLE_FILTER(self,    Access.RW,  0x00000020,  5,   signed=False)
            self.CLN               =  self._CLN(self,               Access.RW,  0x00000100,  8,   signed=False)
            self.DIRECTION         =  self._DIRECTION(self,         Access.RW,  0x00001000,  12,  signed=False)

    class _ABN_PPR(Register):

        class _ABN_PPR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_PPR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ABN_PPR", parent, access, address, block, signed)
            self.ABN_PPR  =  self._ABN_PPR(self,  Access.RW,  0x00FFFFFF,  0,  signed=False)

    class _ABN_PPR_INV(Register):

        class _ABN_PPR_INV(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_PPR_INV", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ABN_PPR_INV", parent, access, address, block, signed)
            self.ABN_PPR_INV  =  self._ABN_PPR_INV(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _ABN_COUNT(Register):

        class _ABN_COUNT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_COUNT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ABN_COUNT", parent, access, address, block, signed)
            self.ABN_COUNT  =  self._ABN_COUNT(self,  Access.RW,  0x00FFFFFF,  0,  signed=False)

    class _ABN_COUNT_N(Register):

        class _ABN_COUNT_N(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_COUNT_N", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ABN_COUNT_N", parent, access, address, block, signed)
            self.ABN_COUNT_N  =  self._ABN_COUNT_N(self,  Access.RW,  0x00FFFFFF,  0,  signed=False)

    class _ABN_PHI_E_OFFSET(Register):

        class _ABN_PHI_E_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_PHI_E_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ABN_PHI_E_OFFSET", parent, access, address, block, signed)
            self.ABN_PHI_E_OFFSET  =  self._ABN_PHI_E_OFFSET(self,  Access.RW,  0x0000FFFF,  0,  signed=True)

    class _HALL_MODE(Register):

        class _POLARITY(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POLARITY", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EXTRAPOLATION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXTRAPOLATION", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ORDER(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ORDER", parent, access, mask, shift, signed=signed)

                self.choice : _ORDER_FIELD_CHOICES = {
                    "UVW Hall Signal Order U/V/W": Choice(0, self),
                    "VWU Hall Signal Order V/W/U": Choice(1, self),
                    "WUV Hall Signal Order W/U/V": Choice(2, self),
                    "RESERVED reserved": Choice(3, self),
                    "UWV Hall Signal Order U/W/V": Choice(4, self),
                    "VUW Hall Signal Order V/U/W": Choice(5, self),
                    "WVU Hall Signal Order W/V/U": Choice(6, self),
                    "RESERVED2 reserved": Choice(7, self),
                }

        class _FILTER(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FILTER", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("HALL_MODE", parent, access, address, block, signed)
            self.POLARITY       =  self._POLARITY(self,       Access.RW,  0x00000001,  0,  signed=False)
            self.EXTRAPOLATION  =  self._EXTRAPOLATION(self,  Access.RW,  0x00000002,  1,  signed=False)
            self.ORDER          =  self._ORDER(self,          Access.RW,  0x00000070,  4,  signed=False)
            self.FILTER         =  self._FILTER(self,         Access.RW,  0x0000FF00,  8,  signed=False)

    class _HALL_DPHI_MAX(Register):

        class _HALL_DPHI_MAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_DPHI_MAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("HALL_DPHI_MAX", parent, access, address, block, signed)
            self.HALL_DPHI_MAX  =  self._HALL_DPHI_MAX(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

    class _HALL_PHI_E_OFFSET(Register):

        class _HALL_PHI_E_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_PHI_E_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("HALL_PHI_E_OFFSET", parent, access, address, block, signed)
            self.HALL_PHI_E_OFFSET  =  self._HALL_PHI_E_OFFSET(self,  Access.RW,  0x0000FFFF,  0,  signed=True)

    class _HALL_COUNT(Register):

        class _HALL_COUNT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_COUNT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("HALL_COUNT", parent, access, address, block, signed)
            self.HALL_COUNT  =  self._HALL_COUNT(self,  Access.R,  0x0000FFFF,  0,  signed=True)

    class _HALL_PHI_E_EXTRAPOLATED_PHI_E(Register):

        class _HALL_PHI_E(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_PHI_E", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_PHI_E_EXTRAPOLATED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_PHI_E_EXTRAPOLATED", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("HALL_PHI_E_EXTRAPOLATED_PHI_E", parent, access, address, block, signed)
            self.HALL_PHI_E               =  self._HALL_PHI_E(self,               Access.R,  0x0000FFFF,  0,   signed=True)
            self.HALL_PHI_E_EXTRAPOLATED  =  self._HALL_PHI_E_EXTRAPOLATED(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _HALL_POSITION_060_POSITION_000(Register):

        class _POSITION_000(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_000", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _POSITION_060(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_060", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("HALL_POSITION_060_POSITION_000", parent, access, address, block, signed)
            self.POSITION_000  =  self._POSITION_000(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.POSITION_060  =  self._POSITION_060(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

    class _HALL_POSITION_180_POSITION_120(Register):

        class _POSITION_120(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_120", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _POSITION_180(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_180", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("HALL_POSITION_180_POSITION_120", parent, access, address, block, signed)
            self.POSITION_120  =  self._POSITION_120(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.POSITION_180  =  self._POSITION_180(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

    class _HALL_POSITION_300_POSITION_240(Register):

        class _POSITION_240(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_240", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _POSITION_300(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_300", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("HALL_POSITION_300_POSITION_240", parent, access, address, block, signed)
            self.POSITION_240  =  self._POSITION_240(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.POSITION_300  =  self._POSITION_300(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

    class _BIQUAD_V_A_1(Register):

        class _BIQUAD_V_A_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_V_A_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_V_A_1", parent, access, address, block, signed)
            self.BIQUAD_V_A_1  =  self._BIQUAD_V_A_1(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

    class _BIQUAD_V_A_2(Register):

        class _BIQUAD_V_A_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_V_A_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_V_A_2", parent, access, address, block, signed)
            self.BIQUAD_V_A_2  =  self._BIQUAD_V_A_2(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

    class _BIQUAD_V_B_0(Register):

        class _BIQUAD_V_B_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_V_B_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_V_B_0", parent, access, address, block, signed)
            self.BIQUAD_V_B_0  =  self._BIQUAD_V_B_0(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

    class _BIQUAD_V_B_1(Register):

        class _BIQUAD_V_B_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_V_B_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_V_B_1", parent, access, address, block, signed)
            self.BIQUAD_V_B_1  =  self._BIQUAD_V_B_1(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

    class _BIQUAD_V_B_2(Register):

        class _BIQUAD_V_B_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_V_B_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_V_B_2", parent, access, address, block, signed)
            self.BIQUAD_V_B_2  =  self._BIQUAD_V_B_2(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

    class _BIQUAD_V_ENABLE(Register):

        class _BIQUAD_V_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_V_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_V_ENABLE", parent, access, address, block, signed)
            self.BIQUAD_V_ENABLE  =  self._BIQUAD_V_ENABLE(self,  Access.RW,  0x00000001,  0,  signed=False)

    class _BIQUAD_T_A_1(Register):

        class _BIQUAD_T_A_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_T_A_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_T_A_1", parent, access, address, block, signed)
            self.BIQUAD_T_A_1  =  self._BIQUAD_T_A_1(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

    class _BIQUAD_T_A_2(Register):

        class _BIQUAD_T_A_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_T_A_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_T_A_2", parent, access, address, block, signed)
            self.BIQUAD_T_A_2  =  self._BIQUAD_T_A_2(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

    class _BIQUAD_T_B_0(Register):

        class _BIQUAD_T_B_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_T_B_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_T_B_0", parent, access, address, block, signed)
            self.BIQUAD_T_B_0  =  self._BIQUAD_T_B_0(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

    class _BIQUAD_T_B_1(Register):

        class _BIQUAD_T_B_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_T_B_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_T_B_1", parent, access, address, block, signed)
            self.BIQUAD_T_B_1  =  self._BIQUAD_T_B_1(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

    class _BIQUAD_T_B_2(Register):

        class _BIQUAD_T_B_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_T_B_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_T_B_2", parent, access, address, block, signed)
            self.BIQUAD_T_B_2  =  self._BIQUAD_T_B_2(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

    class _BIQUAD_T_ENABLE(Register):

        class _BIQUAD_T_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_T_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_T_ENABLE", parent, access, address, block, signed)
            self.BIQUAD_T_ENABLE  =  self._BIQUAD_T_ENABLE(self,  Access.RW,  0x00000001,  0,  signed=False)

    class _VELOCITY_CONFIG(Register):

        class _SELECTION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SELECTION", parent, access, mask, shift, signed=signed)

                self.choice : _SELECTION_FIELD_CHOICES = {
                    "phi_e phi_e selected via PHI_E_SELECTION": Choice(0, self),
                    "phi_e_ext phi_e_ext": Choice(1, self),
                    "phi_e_ramp phi_e_ramp": Choice(2, self),
                    "phi_e_abn phi_e_abn": Choice(3, self),
                    "ramp_X_actual ramp_X_actual": Choice(4, self),
                    "phi_e_hal phi_e_hal (Don't use 0x0 with extrapolated Hall)": Choice(5, self),
                    "phi_m_ext phi_m_ext": Choice(6, self),
                    "abn_count abn_count": Choice(8, self),
                    "phi_m_abn phi_m_abn": Choice(9, self),
                    "hall_count hall_count": Choice(12, self),
                }

        class _METER_SYNC_PULSE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("METER_SYNC_PULSE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _METER_TYPE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("METER_TYPE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _MOVING_AVRG_FILTER_SAMPLES(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MOVING_AVRG_FILTER_SAMPLES", parent, access, mask, shift, signed=signed)

                self.choice : _MOVING_AVRG_FILTER_SAMPLES_FIELD_CHOICES = {
                    "1 No additional filter": Choice(0, self),
                    "2 Average over 2 samples": Choice(1, self),
                    "3 Average over 3 samples": Choice(2, self),
                    "4 Average over 4 samples": Choice(3, self),
                    "5 Average over 5 samples": Choice(4, self),
                    "6 Average over 6 samples": Choice(5, self),
                    "7 Average over 7 samples": Choice(6, self),
                    "8 Average over 8 samples": Choice(7, self),
                }

        def __init__(self, parent, access, address, block, signed):
            super().__init__("VELOCITY_CONFIG", parent, access, address, block, signed)
            self.SELECTION                   =  self._SELECTION(self,                   Access.RW,  0x000000FF,  0,   signed=False)
            self.METER_SYNC_PULSE            =  self._METER_SYNC_PULSE(self,            Access.RW,  0x00000100,  8,   signed=False)
            self.METER_TYPE                  =  self._METER_TYPE(self,                  Access.RW,  0x00000600,  9,   signed=False)
            self.MOVING_AVRG_FILTER_SAMPLES  =  self._MOVING_AVRG_FILTER_SAMPLES(self,  Access.RW,  0x00007000,  12,  signed=False)

    class _VELOCITY_SCALING(Register):

        class _VELOCITY_SCALING(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_SCALING", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("VELOCITY_SCALING", parent, access, address, block, signed)
            self.VELOCITY_SCALING  =  self._VELOCITY_SCALING(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

    class _V_MIN_POS_DEV_TIME_COUNTER_LIMIT(Register):

        class _TIME_COUNTER_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TIME_COUNTER_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _V_MIN_POS_DEV(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V_MIN_POS_DEV", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("V_MIN_POS_DEV_TIME_COUNTER_LIMIT", parent, access, address, block, signed)
            self.TIME_COUNTER_LIMIT  =  self._TIME_COUNTER_LIMIT(self,  Access.RW,  0x0000FFFF,  0,   signed=False)
            self.V_MIN_POS_DEV       =  self._V_MIN_POS_DEV(self,       Access.RW,  0x7FFF0000,  16,  signed=False)

    class _MAX_VEL_DEVIATION(Register):

        class _MAX_VEL_DEVIATION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MAX_VEL_DEVIATION", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("MAX_VEL_DEVIATION", parent, access, address, block, signed)
            self.MAX_VEL_DEVIATION  =  self._MAX_VEL_DEVIATION(self,  Access.RW,  0x7FFFFFFF,  0,  signed=False)

    class _POSITION_CONFIG(Register):

        class _SELECTION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SELECTION", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("POSITION_CONFIG", parent, access, address, block, signed)
            self.SELECTION  =  self._SELECTION(self,  Access.RW,  0x000000FF,  0,  signed=False)

    class _MAX_POS_DEVIATION(Register):

        class _MAX_POS_DEVIATION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MAX_POS_DEVIATION", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("MAX_POS_DEVIATION", parent, access, address, block, signed)
            self.MAX_POS_DEVIATION  =  self._MAX_POS_DEVIATION(self,  Access.RW,  0x7FFFFFFF,  0,  signed=False)

    class _POSITION_STEP_WIDTH(Register):

        class _POSITION_STEP_WIDTH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_STEP_WIDTH", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("POSITION_STEP_WIDTH", parent, access, address, block, signed)
            self.POSITION_STEP_WIDTH  =  self._POSITION_STEP_WIDTH(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _RAMPER_STATUS(Register):

        class _STATUS_STOP_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_STOP_L", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_STOP_R(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_STOP_R", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_STOP_H(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_STOP_H", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_LATCH_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_LATCH_L", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_LATCH_R(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_LATCH_R", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_LATCH_H(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_LATCH_H", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EVENT_STOP_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EVENT_STOP_L", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EVENT_STOP_R(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EVENT_STOP_R", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EVENT_STOP_H(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EVENT_STOP_H", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EVENT_STOP_SG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EVENT_STOP_SG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EVENT_POS_REACHED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EVENT_POS_REACHED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VELOCITY_REACHED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_REACHED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _POSITION_REACHED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_REACHED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _V_ZERO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V_ZERO", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _T_ZEROWAIT_ACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("T_ZEROWAIT_ACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SECOND_MOVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SECOND_MOVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STALL_IN_VEL_ERR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STALL_IN_VEL_ERR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STALL_IN_POS_ERR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STALL_IN_POS_ERR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_STATUS", parent, access, address, block, signed)
            self.STATUS_STOP_L      =  self._STATUS_STOP_L(self,      Access.R,    0x00000001,  0,   signed=False)
            self.STATUS_STOP_R      =  self._STATUS_STOP_R(self,      Access.R,    0x00000002,  1,   signed=False)
            self.STATUS_STOP_H      =  self._STATUS_STOP_H(self,      Access.R,    0x00000004,  2,   signed=False)
            self.STATUS_LATCH_L     =  self._STATUS_LATCH_L(self,     Access.RWC,  0x00000008,  3,   signed=False)
            self.STATUS_LATCH_R     =  self._STATUS_LATCH_R(self,     Access.RWC,  0x00000010,  4,   signed=False)
            self.STATUS_LATCH_H     =  self._STATUS_LATCH_H(self,     Access.RWC,  0x00000020,  5,   signed=False)
            self.EVENT_STOP_L       =  self._EVENT_STOP_L(self,       Access.R,    0x00000040,  6,   signed=False)
            self.EVENT_STOP_R       =  self._EVENT_STOP_R(self,       Access.R,    0x00000080,  7,   signed=False)
            self.EVENT_STOP_H       =  self._EVENT_STOP_H(self,       Access.R,    0x00000100,  8,   signed=False)
            self.EVENT_STOP_SG      =  self._EVENT_STOP_SG(self,      Access.RWC,  0x00000200,  9,   signed=False)
            self.EVENT_POS_REACHED  =  self._EVENT_POS_REACHED(self,  Access.RWC,  0x00000400,  10,  signed=False)
            self.VELOCITY_REACHED   =  self._VELOCITY_REACHED(self,   Access.R,    0x00000800,  11,  signed=False)
            self.POSITION_REACHED   =  self._POSITION_REACHED(self,   Access.R,    0x00001000,  12,  signed=False)
            self.V_ZERO             =  self._V_ZERO(self,             Access.R,    0x00002000,  13,  signed=False)
            self.T_ZEROWAIT_ACTIVE  =  self._T_ZEROWAIT_ACTIVE(self,  Access.R,    0x00004000,  14,  signed=False)
            self.SECOND_MOVE        =  self._SECOND_MOVE(self,        Access.RWC,  0x00008000,  15,  signed=False)
            self.STALL_IN_VEL_ERR   =  self._STALL_IN_VEL_ERR(self,   Access.R,    0x00010000,  16,  signed=False)
            self.STALL_IN_POS_ERR   =  self._STALL_IN_POS_ERR(self,   Access.R,    0x00020000,  17,  signed=False)

    class _RAMPER_A1(Register):

        class _RAMPER_A1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_A1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_A1", parent, access, address, block, signed)
            self.RAMPER_A1  =  self._RAMPER_A1(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

    class _RAMPER_A2(Register):

        class _RAMPER_A2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_A2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_A2", parent, access, address, block, signed)
            self.RAMPER_A2  =  self._RAMPER_A2(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

    class _RAMPER_A_MAX(Register):

        class _RAMPER_A_MAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_A_MAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_A_MAX", parent, access, address, block, signed)
            self.RAMPER_A_MAX  =  self._RAMPER_A_MAX(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

    class _RAMPER_D1(Register):

        class _RAMPER_D1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_D1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_D1", parent, access, address, block, signed)
            self.RAMPER_D1  =  self._RAMPER_D1(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

    class _RAMPER_D2(Register):

        class _RAMPER_D2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_D2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_D2", parent, access, address, block, signed)
            self.RAMPER_D2  =  self._RAMPER_D2(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

    class _RAMPER_D_MAX(Register):

        class _RAMPER_D_MAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_D_MAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_D_MAX", parent, access, address, block, signed)
            self.RAMPER_D_MAX  =  self._RAMPER_D_MAX(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

    class _RAMPER_V_START(Register):

        class _RAMPER_V_START(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_V_START", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_V_START", parent, access, address, block, signed)
            self.RAMPER_V_START  =  self._RAMPER_V_START(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

    class _RAMPER_V1(Register):

        class _RAMPER_V1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_V1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_V1", parent, access, address, block, signed)
            self.RAMPER_V1  =  self._RAMPER_V1(self,  Access.RW,  0x07FFFFFF,  0,  signed=False)

    class _RAMPER_V2(Register):

        class _RAMPER_V2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_V2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_V2", parent, access, address, block, signed)
            self.RAMPER_V2  =  self._RAMPER_V2(self,  Access.RW,  0x07FFFFFF,  0,  signed=False)

    class _RAMPER_V_STOP(Register):

        class _RAMPER_V_STOP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_V_STOP", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_V_STOP", parent, access, address, block, signed)
            self.RAMPER_V_STOP  =  self._RAMPER_V_STOP(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

    class _RAMPER_V_MAX(Register):

        class _RAMPER_V_MAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_V_MAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_V_MAX", parent, access, address, block, signed)
            self.RAMPER_V_MAX  =  self._RAMPER_V_MAX(self,  Access.RW,  0x07FFFFFF,  0,  signed=False)

    class _RAMPER_V_TARGET(Register):

        class _RAMPER_V_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_V_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_V_TARGET", parent, access, address, block, signed)
            self.RAMPER_V_TARGET  =  self._RAMPER_V_TARGET(self,  Access.RW,  0x0FFFFFFF,  0,  signed=True)

    class _RAMPER_SWITCH_MODE(Register):

        class _STOP_L_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_L_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STOP_R_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_R_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STOP_H_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_H_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STOP_L_POL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_L_POL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STOP_R_POL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_R_POL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STOP_H_POL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_H_POL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SWAP_LR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SWAP_LR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LATCH_L_ACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_L_ACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LATCH_L_INACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_L_INACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LATCH_R_ACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_R_ACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LATCH_R_INACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_R_INACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LATCH_H_ACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_H_ACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LATCH_H_INACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_H_INACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SG_STOP_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SG_STOP_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SOFTSTOP_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SOFTSTOP_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SW_HARD_STOP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SW_HARD_STOP", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STOP_ON_POS_DEVIATION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_ON_POS_DEVIATION", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STOP_ON_VEL_DEVIATION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_ON_VEL_DEVIATION", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VELOCITY_OVERWRITE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_OVERWRITE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_SWITCH_MODE", parent, access, address, block, signed)
            self.STOP_L_ENABLE          =  self._STOP_L_ENABLE(self,          Access.RW,  0x00000001,  0,   signed=False)
            self.STOP_R_ENABLE          =  self._STOP_R_ENABLE(self,          Access.RW,  0x00000002,  1,   signed=False)
            self.STOP_H_ENABLE          =  self._STOP_H_ENABLE(self,          Access.RW,  0x00000004,  2,   signed=False)
            self.STOP_L_POL             =  self._STOP_L_POL(self,             Access.RW,  0x00000008,  3,   signed=False)
            self.STOP_R_POL             =  self._STOP_R_POL(self,             Access.RW,  0x00000010,  4,   signed=False)
            self.STOP_H_POL             =  self._STOP_H_POL(self,             Access.RW,  0x00000020,  5,   signed=False)
            self.SWAP_LR                =  self._SWAP_LR(self,                Access.RW,  0x00000040,  6,   signed=False)
            self.LATCH_L_ACTIVE         =  self._LATCH_L_ACTIVE(self,         Access.RW,  0x00000080,  7,   signed=False)
            self.LATCH_L_INACTIVE       =  self._LATCH_L_INACTIVE(self,       Access.RW,  0x00000100,  8,   signed=False)
            self.LATCH_R_ACTIVE         =  self._LATCH_R_ACTIVE(self,         Access.RW,  0x00000200,  9,   signed=False)
            self.LATCH_R_INACTIVE       =  self._LATCH_R_INACTIVE(self,       Access.RW,  0x00000400,  10,  signed=False)
            self.LATCH_H_ACTIVE         =  self._LATCH_H_ACTIVE(self,         Access.RW,  0x00000800,  11,  signed=False)
            self.LATCH_H_INACTIVE       =  self._LATCH_H_INACTIVE(self,       Access.RW,  0x00001000,  12,  signed=False)
            self.SG_STOP_ENABLE         =  self._SG_STOP_ENABLE(self,         Access.RW,  0x00004000,  14,  signed=False)
            self.SOFTSTOP_ENABLE        =  self._SOFTSTOP_ENABLE(self,        Access.RW,  0x00008000,  15,  signed=False)
            self.SW_HARD_STOP           =  self._SW_HARD_STOP(self,           Access.RW,  0x00010000,  16,  signed=False)
            self.STOP_ON_POS_DEVIATION  =  self._STOP_ON_POS_DEVIATION(self,  Access.RW,  0x00020000,  17,  signed=False)
            self.STOP_ON_VEL_DEVIATION  =  self._STOP_ON_VEL_DEVIATION(self,  Access.RW,  0x00040000,  18,  signed=False)
            self.VELOCITY_OVERWRITE     =  self._VELOCITY_OVERWRITE(self,     Access.RW,  0x00080000,  19,  signed=False)

    class _RAMPER_TIME_CONFIG(Register):

        class _T_ZEROWAIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("T_ZEROWAIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _T_VMAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("T_VMAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_TIME_CONFIG", parent, access, address, block, signed)
            self.T_ZEROWAIT  =  self._T_ZEROWAIT(self,  Access.RW,  0x0000FFFF,  0,   signed=False)
            self.T_VMAX      =  self._T_VMAX(self,      Access.RW,  0xFFFF0000,  16,  signed=False)

    class _RAMPER_A_ACTUAL(Register):

        class _RAMPER_A_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_A_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_A_ACTUAL", parent, access, address, block, signed)
            self.RAMPER_A_ACTUAL  =  self._RAMPER_A_ACTUAL(self,  Access.R,  0x00FFFFFF,  0,  signed=True)

    class _RAMPER_X_ACTUAL(Register):

        class _RAMPER_X_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_X_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_X_ACTUAL", parent, access, address, block, signed)
            self.RAMPER_X_ACTUAL  =  self._RAMPER_X_ACTUAL(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _RAMPER_V_ACTUAL(Register):

        class _RAMPER_V_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_V_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_V_ACTUAL", parent, access, address, block, signed)
            self.RAMPER_V_ACTUAL  =  self._RAMPER_V_ACTUAL(self,  Access.R,  0x0FFFFFFF,  0,  signed=True)

    class _RAMPER_X_TARGET(Register):

        class _RAMPER_X_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_X_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_X_TARGET", parent, access, address, block, signed)
            self.RAMPER_X_TARGET  =  self._RAMPER_X_TARGET(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _RAMPER_PHI_E(Register):

        class _RAMPER_PHI_E(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_PHI_E", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_PHI_E", parent, access, address, block, signed)
            self.RAMPER_PHI_E  =  self._RAMPER_PHI_E(self,  Access.R,  0x0000FFFF,  0,  signed=True)

    class _RAMPER_PHI_E_OFFSET(Register):

        class _RAMPER_PHI_E_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_PHI_E_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_PHI_E_OFFSET", parent, access, address, block, signed)
            self.RAMPER_PHI_E_OFFSET  =  self._RAMPER_PHI_E_OFFSET(self,  Access.RW,  0x0000FFFF,  0,  signed=True)

    class _RAMPER_ACC_FF(Register):

        class _GAIN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("GAIN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SHIFT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SHIFT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_ACC_FF", parent, access, address, block, signed)
            self.GAIN   =  self._GAIN(self,   Access.RW,  0x0000FFFF,  0,   signed=False)
            self.SHIFT  =  self._SHIFT(self,  Access.RW,  0x00070000,  16,  signed=False)

    class _RAMPER_X_ACTUAL_LATCH(Register):

        class _RAMPER_X_ACTUAL_LATCH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_X_ACTUAL_LATCH", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_X_ACTUAL_LATCH", parent, access, address, block, signed)
            self.RAMPER_X_ACTUAL_LATCH  =  self._RAMPER_X_ACTUAL_LATCH(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _POSITION_ACTUAL_LATCH(Register):

        class _POSITION_ACTUAL_LATCH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_ACTUAL_LATCH", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("POSITION_ACTUAL_LATCH", parent, access, address, block, signed)
            self.POSITION_ACTUAL_LATCH  =  self._POSITION_ACTUAL_LATCH(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _PRBS_AMPLITUDE(Register):

        class _PRBS_AMPLITUDE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PRBS_AMPLITUDE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PRBS_AMPLITUDE", parent, access, address, block, signed)
            self.PRBS_AMPLITUDE  =  self._PRBS_AMPLITUDE(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PRBS_DOWN_SAMPLING_RATIO(Register):

        class _PRBS_DOWN_SAMPLING_RATIO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PRBS_DOWN_SAMPLING_RATIO", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PRBS_DOWN_SAMPLING_RATIO", parent, access, address, block, signed)
            self.PRBS_DOWN_SAMPLING_RATIO  =  self._PRBS_DOWN_SAMPLING_RATIO(self,  Access.RW,  0x000000FF,  0,  signed=False)

    class _PID_CONFIG(Register):

        class _KEEP_POS_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("KEEP_POS_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CURRENT_NORM_P(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CURRENT_NORM_P", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CURRENT_NORM_I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CURRENT_NORM_I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VELOCITY_NORM_P(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_NORM_P", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VELOCITY_NORM_I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_NORM_I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _POSITION_NORM_P(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_NORM_P", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _POSITION_NORM_I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_NORM_I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VEL_SCALE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VEL_SCALE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _POS_SMPL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POS_SMPL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VEL_SMPL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VEL_SMPL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_CONFIG", parent, access, address, block, signed)
            self.KEEP_POS_TARGET  =  self._KEEP_POS_TARGET(self,  Access.RW,  0x00000001,  0,   signed=False)
            self.CURRENT_NORM_P   =  self._CURRENT_NORM_P(self,   Access.RW,  0x00000004,  2,   signed=False)
            self.CURRENT_NORM_I   =  self._CURRENT_NORM_I(self,   Access.RW,  0x00000008,  3,   signed=False)
            self.VELOCITY_NORM_P  =  self._VELOCITY_NORM_P(self,  Access.RW,  0x00000030,  4,   signed=False)
            self.VELOCITY_NORM_I  =  self._VELOCITY_NORM_I(self,  Access.RW,  0x000000C0,  6,   signed=False)
            self.POSITION_NORM_P  =  self._POSITION_NORM_P(self,  Access.RW,  0x00000300,  8,   signed=False)
            self.POSITION_NORM_I  =  self._POSITION_NORM_I(self,  Access.RW,  0x00000C00,  10,  signed=False)
            self.VEL_SCALE        =  self._VEL_SCALE(self,        Access.RW,  0x0000F000,  12,  signed=False)
            self.POS_SMPL         =  self._POS_SMPL(self,         Access.RW,  0x007F0000,  16,  signed=False)
            self.VEL_SMPL         =  self._VEL_SMPL(self,         Access.RW,  0x7F000000,  24,  signed=False)

    class _PID_FLUX_COEFF(Register):

        class _I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _P(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("P", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_FLUX_COEFF", parent, access, address, block, signed)
            self.I  =  self._I(self,  Access.RW,  0x00007FFF,  0,   signed=False)
            self.P  =  self._P(self,  Access.RW,  0x7FFF0000,  16,  signed=False)

    class _PID_TORQUE_COEFF(Register):

        class _I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _P(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("P", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_TORQUE_COEFF", parent, access, address, block, signed)
            self.I  =  self._I(self,  Access.RW,  0x00007FFF,  0,   signed=False)
            self.P  =  self._P(self,  Access.RW,  0x7FFF0000,  16,  signed=False)

    class _PID_FIELDWEAK_COEFF(Register):

        class _I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _P(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("P", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_FIELDWEAK_COEFF", parent, access, address, block, signed)
            self.I  =  self._I(self,  Access.RW,  0x00007FFF,  0,   signed=False)
            self.P  =  self._P(self,  Access.RW,  0x7FFF0000,  16,  signed=False)

    class _PID_U_S_MAX(Register):

        class _U_S_MAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U_S_MAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_U_S_MAX", parent, access, address, block, signed)
            self.U_S_MAX  =  self._U_S_MAX(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

    class _PID_VELOCITY_COEFF(Register):

        class _I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _P(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("P", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_VELOCITY_COEFF", parent, access, address, block, signed)
            self.I  =  self._I(self,  Access.RW,  0x00007FFF,  0,   signed=False)
            self.P  =  self._P(self,  Access.RW,  0x7FFF0000,  16,  signed=False)

    class _PID_POSITION_COEFF(Register):

        class _I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _P(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("P", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_POSITION_COEFF", parent, access, address, block, signed)
            self.I  =  self._I(self,  Access.RW,  0x00007FFF,  0,   signed=False)
            self.P  =  self._P(self,  Access.RW,  0x7FFF0000,  16,  signed=False)

    class _PID_POSITION_TOLERANCE(Register):

        class _PID_POSITION_TOLERANCE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_TOLERANCE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_POSITION_TOLERANCE", parent, access, address, block, signed)
            self.PID_POSITION_TOLERANCE  =  self._PID_POSITION_TOLERANCE(self,  Access.RW,  0x7FFFFFFF,  0,  signed=False)

    class _PID_POSITION_TOLERANCE_DELAY(Register):

        class _PID_POSITION_TOLERANCE_DELAY(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_TOLERANCE_DELAY", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_POSITION_TOLERANCE_DELAY", parent, access, address, block, signed)
            self.PID_POSITION_TOLERANCE_DELAY  =  self._PID_POSITION_TOLERANCE_DELAY(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

    class _PID_UQ_UD_LIMITS(Register):

        class _PID_UQ_UD_LIMITS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_UQ_UD_LIMITS", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_UQ_UD_LIMITS", parent, access, address, block, signed)
            self.PID_UQ_UD_LIMITS  =  self._PID_UQ_UD_LIMITS(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

    class _PID_TORQUE_FLUX_LIMITS(Register):

        class _PID_FLUX_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_TORQUE_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_TORQUE_FLUX_LIMITS", parent, access, address, block, signed)
            self.PID_FLUX_LIMIT    =  self._PID_FLUX_LIMIT(self,    Access.RW,  0x00007FFF,  0,   signed=False)
            self.PID_TORQUE_LIMIT  =  self._PID_TORQUE_LIMIT(self,  Access.RW,  0x7FFF0000,  16,  signed=False)

    class _PID_VELOCITY_LIMIT(Register):

        class _PID_VELOCITY_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_VELOCITY_LIMIT", parent, access, address, block, signed)
            self.PID_VELOCITY_LIMIT  =  self._PID_VELOCITY_LIMIT(self,  Access.RW,  0x7FFFFFFF,  0,  signed=False)

    class _PID_POSITION_LIMIT_LOW(Register):

        class _PID_POSITION_LIMIT_LOW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_LIMIT_LOW", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_POSITION_LIMIT_LOW", parent, access, address, block, signed)
            self.PID_POSITION_LIMIT_LOW  =  self._PID_POSITION_LIMIT_LOW(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PID_POSITION_LIMIT_HIGH(Register):

        class _PID_POSITION_LIMIT_HIGH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_LIMIT_HIGH", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_POSITION_LIMIT_HIGH", parent, access, address, block, signed)
            self.PID_POSITION_LIMIT_HIGH  =  self._PID_POSITION_LIMIT_HIGH(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PID_TORQUE_FLUX_TARGET(Register):

        class _PID_FLUX_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_TORQUE_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_TORQUE_FLUX_TARGET", parent, access, address, block, signed)
            self.PID_FLUX_TARGET    =  self._PID_FLUX_TARGET(self,    Access.RW,  0x0000FFFF,  0,   signed=True)
            self.PID_TORQUE_TARGET  =  self._PID_TORQUE_TARGET(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

    class _PID_TORQUE_FLUX_OFFSET(Register):

        class _PID_FLUX_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_TORQUE_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_TORQUE_FLUX_OFFSET", parent, access, address, block, signed)
            self.PID_FLUX_OFFSET    =  self._PID_FLUX_OFFSET(self,    Access.RW,  0x0000FFFF,  0,   signed=True)
            self.PID_TORQUE_OFFSET  =  self._PID_TORQUE_OFFSET(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

    class _PID_VELOCITY_TARGET(Register):

        class _PID_VELOCITY_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_VELOCITY_TARGET", parent, access, address, block, signed)
            self.PID_VELOCITY_TARGET  =  self._PID_VELOCITY_TARGET(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PID_VELOCITY_OFFSET(Register):

        class _PID_VELOCITY_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_VELOCITY_OFFSET", parent, access, address, block, signed)
            self.PID_VELOCITY_OFFSET  =  self._PID_VELOCITY_OFFSET(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PID_POSITION_TARGET(Register):

        class _PID_POSITION_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_POSITION_TARGET", parent, access, address, block, signed)
            self.PID_POSITION_TARGET  =  self._PID_POSITION_TARGET(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PID_TORQUE_FLUX_ACTUAL(Register):

        class _PID_FLUX_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_TORQUE_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_TORQUE_FLUX_ACTUAL", parent, access, address, block, signed)
            self.PID_FLUX_ACTUAL    =  self._PID_FLUX_ACTUAL(self,    Access.R,  0x0000FFFF,  0,   signed=True)
            self.PID_TORQUE_ACTUAL  =  self._PID_TORQUE_ACTUAL(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _PID_VELOCITY_ACTUAL(Register):

        class _PID_VELOCITY_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_VELOCITY_ACTUAL", parent, access, address, block, signed)
            self.PID_VELOCITY_ACTUAL  =  self._PID_VELOCITY_ACTUAL(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _PID_POSITION_ACTUAL(Register):

        class _PID_POSITION_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_POSITION_ACTUAL", parent, access, address, block, signed)
            self.PID_POSITION_ACTUAL  =  self._PID_POSITION_ACTUAL(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PID_POSITION_ACTUAL_OFFSET(Register):

        class _PID_POSITION_ACTUAL_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_ACTUAL_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_POSITION_ACTUAL_OFFSET", parent, access, address, block, signed)
            self.PID_POSITION_ACTUAL_OFFSET  =  self._PID_POSITION_ACTUAL_OFFSET(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PID_TORQUE_ERROR(Register):

        class _PID_TORQUE_ERROR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_ERROR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_TORQUE_ERROR", parent, access, address, block, signed)
            self.PID_TORQUE_ERROR  =  self._PID_TORQUE_ERROR(self,  Access.R,  0x0000FFFF,  0,  signed=True)

    class _PID_FLUX_ERROR(Register):

        class _PID_FLUX_ERROR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_ERROR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_FLUX_ERROR", parent, access, address, block, signed)
            self.PID_FLUX_ERROR  =  self._PID_FLUX_ERROR(self,  Access.R,  0x0000FFFF,  0,  signed=True)

    class _PID_VELOCITY_ERROR(Register):

        class _PID_VELOCITY_ERROR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_ERROR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_VELOCITY_ERROR", parent, access, address, block, signed)
            self.PID_VELOCITY_ERROR  =  self._PID_VELOCITY_ERROR(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _PID_POSITION_ERROR(Register):

        class _PID_POSITION_ERROR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_ERROR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_POSITION_ERROR", parent, access, address, block, signed)
            self.PID_POSITION_ERROR  =  self._PID_POSITION_ERROR(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _PID_TORQUE_INTEGRATOR(Register):

        class _PID_TORQUE_INTEGRATOR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_INTEGRATOR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_TORQUE_INTEGRATOR", parent, access, address, block, signed)
            self.PID_TORQUE_INTEGRATOR  =  self._PID_TORQUE_INTEGRATOR(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PID_FLUX_INTEGRATOR(Register):

        class _PID_FLUX_INTEGRATOR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_INTEGRATOR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_FLUX_INTEGRATOR", parent, access, address, block, signed)
            self.PID_FLUX_INTEGRATOR  =  self._PID_FLUX_INTEGRATOR(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PID_VELOCITY_INTEGRATOR(Register):

        class _PID_VELOCITY_INTEGRATOR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_INTEGRATOR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_VELOCITY_INTEGRATOR", parent, access, address, block, signed)
            self.PID_VELOCITY_INTEGRATOR  =  self._PID_VELOCITY_INTEGRATOR(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PID_POSITION_INTEGRATOR(Register):

        class _PID_POSITION_INTEGRATOR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_INTEGRATOR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_POSITION_INTEGRATOR", parent, access, address, block, signed)
            self.PID_POSITION_INTEGRATOR  =  self._PID_POSITION_INTEGRATOR(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PIDIN_TORQUE_FLUX_TARGET(Register):

        class _PIDIN_FLUX_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_FLUX_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIDIN_TORQUE_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_TORQUE_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PIDIN_TORQUE_FLUX_TARGET", parent, access, address, block, signed)
            self.PIDIN_FLUX_TARGET    =  self._PIDIN_FLUX_TARGET(self,    Access.R,  0x0000FFFF,  0,   signed=True)
            self.PIDIN_TORQUE_TARGET  =  self._PIDIN_TORQUE_TARGET(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _PIDIN_VELOCITY_TARGET(Register):

        class _PIDIN_VELOCITY_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_VELOCITY_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PIDIN_VELOCITY_TARGET", parent, access, address, block, signed)
            self.PIDIN_VELOCITY_TARGET  =  self._PIDIN_VELOCITY_TARGET(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _PIDIN_POSITION_TARGET(Register):

        class _PIDIN_POSITION_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_POSITION_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PIDIN_POSITION_TARGET", parent, access, address, block, signed)
            self.PIDIN_POSITION_TARGET  =  self._PIDIN_POSITION_TARGET(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _PIDIN_TORQUE_FLUX_TARGET_LIMITED(Register):

        class _PIDIN_FLUX_TARGET_LIMITED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_FLUX_TARGET_LIMITED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIDIN_TORQUE_TARGET_LIMITED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_TORQUE_TARGET_LIMITED", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PIDIN_TORQUE_FLUX_TARGET_LIMITED", parent, access, address, block, signed)
            self.PIDIN_FLUX_TARGET_LIMITED    =  self._PIDIN_FLUX_TARGET_LIMITED(self,    Access.R,  0x0000FFFF,  0,   signed=True)
            self.PIDIN_TORQUE_TARGET_LIMITED  =  self._PIDIN_TORQUE_TARGET_LIMITED(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _PIDIN_VELOCITY_TARGET_LIMITED(Register):

        class _PIDIN_VELOCITY_TARGET_LIMITED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_VELOCITY_TARGET_LIMITED", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PIDIN_VELOCITY_TARGET_LIMITED", parent, access, address, block, signed)
            self.PIDIN_VELOCITY_TARGET_LIMITED  =  self._PIDIN_VELOCITY_TARGET_LIMITED(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _PIDIN_POSITION_TARGET_LIMITED(Register):

        class _PIDIN_POSITION_TARGET_LIMITED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_POSITION_TARGET_LIMITED", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PIDIN_POSITION_TARGET_LIMITED", parent, access, address, block, signed)
            self.PIDIN_POSITION_TARGET_LIMITED  =  self._PIDIN_POSITION_TARGET_LIMITED(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _FOC_IBETA_IALPHA(Register):

        class _IALPHA(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IALPHA", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IBETA(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IBETA", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FOC_IBETA_IALPHA", parent, access, address, block, signed)
            self.IALPHA  =  self._IALPHA(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.IBETA   =  self._IBETA(self,   Access.R,  0xFFFF0000,  16,  signed=True)

    class _FOC_IQ_ID(Register):

        class _ID(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ID", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IQ(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IQ", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FOC_IQ_ID", parent, access, address, block, signed)
            self.ID  =  self._ID(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.IQ  =  self._IQ(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _FOC_UQ_UD(Register):

        class _UD(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UD", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UQ(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UQ", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FOC_UQ_UD", parent, access, address, block, signed)
            self.UD  =  self._UD(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.UQ  =  self._UQ(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _FOC_UQ_UD_LIMITED(Register):

        class _UD(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UD", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UQ(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UQ", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FOC_UQ_UD_LIMITED", parent, access, address, block, signed)
            self.UD  =  self._UD(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.UQ  =  self._UQ(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _FOC_UBETA_UALPHA(Register):

        class _UALPHA(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UALPHA", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UBETA(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UBETA", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FOC_UBETA_UALPHA", parent, access, address, block, signed)
            self.UALPHA  =  self._UALPHA(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.UBETA   =  self._UBETA(self,   Access.R,  0xFFFF0000,  16,  signed=True)

    class _FOC_UWY_UUX(Register):

        class _UUX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UUX", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UWY(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UWY", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FOC_UWY_UUX", parent, access, address, block, signed)
            self.UUX  =  self._UUX(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.UWY  =  self._UWY(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _FOC_UV(Register):

        class _UV(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UV", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FOC_UV", parent, access, address, block, signed)
            self.UV  =  self._UV(self,  Access.R,  0x0000FFFF,  0,  signed=True)

    class _PWM_VX2_UX1(Register):

        class _UX1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UX1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VX2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VX2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PWM_VX2_UX1", parent, access, address, block, signed)
            self.UX1  =  self._UX1(self,  Access.R,  0x0000FFFF,  0,   signed=False)
            self.VX2  =  self._VX2(self,  Access.R,  0xFFFF0000,  16,  signed=False)

    class _PWM_Y2_WY1(Register):

        class _WY1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("WY1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PWM_Y2_WY1", parent, access, address, block, signed)
            self.WY1  =  self._WY1(self,  Access.R,  0x0000FFFF,  0,   signed=False)
            self.Y2   =  self._Y2(self,   Access.R,  0xFFFF0000,  16,  signed=False)

    class _VELOCITY_FRQ(Register):

        class _VELOCITY_FRQ(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_FRQ", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("VELOCITY_FRQ", parent, access, address, block, signed)
            self.VELOCITY_FRQ  =  self._VELOCITY_FRQ(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _VELOCITY_PER(Register):

        class _VELOCITY_PER(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_PER", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("VELOCITY_PER", parent, access, address, block, signed)
            self.VELOCITY_PER  =  self._VELOCITY_PER(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _FOC_STATUS(Register):

        class _FOC_STATUS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FOC_STATUS", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FOC_STATUS", parent, access, address, block, signed)
            self.FOC_STATUS  =  self._FOC_STATUS(self,  Access.R,  0x0000000F,  0,  signed=False)

    class _U_S_ACTUAL_I_S_ACTUAL(Register):

        class _I_S_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I_S_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _U_S_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U_S_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("U_S_ACTUAL_I_S_ACTUAL", parent, access, address, block, signed)
            self.I_S_ACTUAL  =  self._I_S_ACTUAL(self,  Access.R,  0x0000FFFF,  0,   signed=False)
            self.U_S_ACTUAL  =  self._U_S_ACTUAL(self,  Access.R,  0xFFFF0000,  16,  signed=False)

    class _P_MOTOR(Register):

        class _P_MOTOR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("P_MOTOR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("P_MOTOR", parent, access, address, block, signed)
            self.P_MOTOR  =  self._P_MOTOR(self,  Access.R,  0xFFFFFFFF,  0,  signed=False)

    class _INPUTS_RAW(Register):

        class _ENC_A(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_A", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ENC_B(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_B", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ENC_N(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_N", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _REF_SW_R(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REF_SW_R", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _REF_SW_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REF_SW_L", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _REF_SW_H(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REF_SW_H", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ENI(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENI", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_U_FILT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_U_FILT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_V_FILT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_V_FILT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_W_FILT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_W_FILT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("INPUTS_RAW", parent, access, address, block, signed)
            self.ENC_A        =  self._ENC_A(self,        Access.R,  0x00000001,  0,   signed=False)
            self.ENC_B        =  self._ENC_B(self,        Access.R,  0x00000002,  1,   signed=False)
            self.ENC_N        =  self._ENC_N(self,        Access.R,  0x00000004,  2,   signed=False)
            self.HALL_U       =  self._HALL_U(self,       Access.R,  0x00000100,  8,   signed=False)
            self.HALL_V       =  self._HALL_V(self,       Access.R,  0x00000200,  9,   signed=False)
            self.HALL_W       =  self._HALL_W(self,       Access.R,  0x00000400,  10,  signed=False)
            self.REF_SW_R     =  self._REF_SW_R(self,     Access.R,  0x00001000,  12,  signed=False)
            self.REF_SW_L     =  self._REF_SW_L(self,     Access.R,  0x00002000,  13,  signed=False)
            self.REF_SW_H     =  self._REF_SW_H(self,     Access.R,  0x00004000,  14,  signed=False)
            self.ENI          =  self._ENI(self,          Access.R,  0x00008000,  15,  signed=False)
            self.HALL_U_FILT  =  self._HALL_U_FILT(self,  Access.R,  0x00100000,  20,  signed=False)
            self.HALL_V_FILT  =  self._HALL_V_FILT(self,  Access.R,  0x00200000,  21,  signed=False)
            self.HALL_W_FILT  =  self._HALL_W_FILT(self,  Access.R,  0x00400000,  22,  signed=False)

    class _OUTPUTS_RAW(Register):

        class _PWM_UX1_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_UX1_L", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_UX1_H(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_UX1_H", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_VX2_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_VX2_L", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_VX2_H(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_VX2_H", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_WY1_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_WY1_L", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_WY1_H(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_WY1_H", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_Y2_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_Y2_L", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_Y2_H(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_Y2_H", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("OUTPUTS_RAW", parent, access, address, block, signed)
            self.PWM_UX1_L  =  self._PWM_UX1_L(self,  Access.R,  0x00000001,  0,  signed=False)
            self.PWM_UX1_H  =  self._PWM_UX1_H(self,  Access.R,  0x00000002,  1,  signed=False)
            self.PWM_VX2_L  =  self._PWM_VX2_L(self,  Access.R,  0x00000004,  2,  signed=False)
            self.PWM_VX2_H  =  self._PWM_VX2_H(self,  Access.R,  0x00000008,  3,  signed=False)
            self.PWM_WY1_L  =  self._PWM_WY1_L(self,  Access.R,  0x00000010,  4,  signed=False)
            self.PWM_WY1_H  =  self._PWM_WY1_H(self,  Access.R,  0x00000020,  5,  signed=False)
            self.PWM_Y2_L   =  self._PWM_Y2_L(self,   Access.R,  0x00000040,  6,  signed=False)
            self.PWM_Y2_H   =  self._PWM_Y2_H(self,   Access.R,  0x00000080,  7,  signed=False)

    class _STATUS_FLAGS(Register):

        class _PID_X_TARGET_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_X_TARGET_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_X_OUTPUT_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_X_OUTPUT_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_V_TARGET_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_V_TARGET_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_V_OUTPUT_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_V_OUTPUT_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_ID_TARGET_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_ID_TARGET_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_ID_OUTPUT_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_ID_OUTPUT_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_IQ_TARGET_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_IQ_TARGET_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_IQ_OUTPUT_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_IQ_OUTPUT_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IPARK_VOLTLIM_LIMIT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IPARK_VOLTLIM_LIMIT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_SWITCH_LIMIT_ACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_SWITCH_LIMIT_ACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_ERROR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_ERROR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _POSITION_TRACKING_ERROR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_TRACKING_ERROR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VELOCITY_TRACKING_ERROR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_TRACKING_ERROR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_FW_OUTPUT_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FW_OUTPUT_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _WATCHDOG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("WATCHDOG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SHORT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SHORT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _REF_SW_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REF_SW_L", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _REF_SW_R(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REF_SW_R", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _REF_SW_H(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REF_SW_H", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _POSITION_REACHED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_REACHED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_I_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ENC_N(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_N", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ENI(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENI", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("STATUS_FLAGS", parent, access, address, block, signed)
            self.PID_X_TARGET_LIMIT       =  self._PID_X_TARGET_LIMIT(self,       Access.RWC,  0x00000001,  0,   signed=False)
            self.PID_X_OUTPUT_LIMIT       =  self._PID_X_OUTPUT_LIMIT(self,       Access.RWC,  0x00000002,  1,   signed=False)
            self.PID_V_TARGET_LIMIT       =  self._PID_V_TARGET_LIMIT(self,       Access.RWC,  0x00000004,  2,   signed=False)
            self.PID_V_OUTPUT_LIMIT       =  self._PID_V_OUTPUT_LIMIT(self,       Access.RWC,  0x00000008,  3,   signed=False)
            self.PID_ID_TARGET_LIMIT      =  self._PID_ID_TARGET_LIMIT(self,      Access.RWC,  0x00000010,  4,   signed=False)
            self.PID_ID_OUTPUT_LIMIT      =  self._PID_ID_OUTPUT_LIMIT(self,      Access.RWC,  0x00000020,  5,   signed=False)
            self.PID_IQ_TARGET_LIMIT      =  self._PID_IQ_TARGET_LIMIT(self,      Access.RWC,  0x00000040,  6,   signed=False)
            self.PID_IQ_OUTPUT_LIMIT      =  self._PID_IQ_OUTPUT_LIMIT(self,      Access.RWC,  0x00000080,  7,   signed=False)
            self.IPARK_VOLTLIM_LIMIT_U    =  self._IPARK_VOLTLIM_LIMIT_U(self,    Access.RWC,  0x00000100,  8,   signed=False)
            self.PWM_SWITCH_LIMIT_ACTIVE  =  self._PWM_SWITCH_LIMIT_ACTIVE(self,  Access.RWC,  0x00000200,  9,   signed=False)
            self.HALL_ERROR               =  self._HALL_ERROR(self,               Access.RWC,  0x00000800,  11,  signed=False)
            self.POSITION_TRACKING_ERROR  =  self._POSITION_TRACKING_ERROR(self,  Access.RWC,  0x00001000,  12,  signed=False)
            self.VELOCITY_TRACKING_ERROR  =  self._VELOCITY_TRACKING_ERROR(self,  Access.RWC,  0x00002000,  13,  signed=False)
            self.PID_FW_OUTPUT_LIMIT      =  self._PID_FW_OUTPUT_LIMIT(self,      Access.RWC,  0x00004000,  14,  signed=False)
            self.WATCHDOG                 =  self._WATCHDOG(self,                 Access.RWC,  0x00010000,  16,  signed=False)
            self.SHORT                    =  self._SHORT(self,                    Access.RWC,  0x00020000,  17,  signed=False)
            self.REF_SW_L                 =  self._REF_SW_L(self,                 Access.RWC,  0x00100000,  20,  signed=False)
            self.REF_SW_R                 =  self._REF_SW_R(self,                 Access.RWC,  0x00200000,  21,  signed=False)
            self.REF_SW_H                 =  self._REF_SW_H(self,                 Access.RWC,  0x00400000,  22,  signed=False)
            self.POSITION_REACHED         =  self._POSITION_REACHED(self,         Access.RWC,  0x00800000,  23,  signed=False)
            self.ADC_I_CLIPPED            =  self._ADC_I_CLIPPED(self,            Access.RWC,  0x04000000,  26,  signed=False)
            self.ENC_N                    =  self._ENC_N(self,                    Access.RWC,  0x10000000,  28,  signed=False)
            self.ENI                      =  self._ENI(self,                      Access.RWC,  0x80000000,  31,  signed=False)

    class _STATUS_MASK(Register):

        class _STATUS_MASK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_MASK", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("STATUS_MASK", parent, access, address, block, signed)
            self.STATUS_MASK  =  self._STATUS_MASK(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _FLEX_COMP_CONF(Register):

        class _START_SELECT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("START_SELECT", parent, access, mask, shift, signed=signed)

                self.choice : _START_SELECT_FIELD_CHOICES = {
                    "PWM_CENTER center pulse of pwm": Choice(0, self),
                    "PWM_ZERO zero pulse of pwm": Choice(1, self),
                    "PWM_LS raw pwm ls generator output": Choice(2, self),
                    "PWM_HS raw pwm hs generator output": Choice(3, self),
                    "GDRV_LS_ON gdrv ls output signal": Choice(4, self),
                    "GDRV_HS_ON gdrv hs output signal": Choice(5, self),
                    "OCP_LS_CMP raw ls ocp comperator out": Choice(6, self),
                    "OCP_HS_CMP raw hs ocp comperator out": Choice(7, self),
                    "VGS_LS_ON raw ls vgs on out": Choice(8, self),
                    "VGS_HS_ON raw hs vgs on out": Choice(9, self),
                    "VGS_LS_OFF raw ls vgs off out": Choice(10, self),
                    "VGS_HS_OFF raw hs vgs off out": Choice(11, self),
                    "PHASE_HIGH phase voltage greater than 0.9VM": Choice(12, self),
                    "PHASE_LOW phase voltage less than 0.1VM": Choice(13, self),
                }

        class _START_DEGLITCH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("START_DEGLITCH", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _START_EDGE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("START_EDGE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _END_SELECT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("END_SELECT", parent, access, mask, shift, signed=signed)

                self.choice : _END_SELECT_FIELD_CHOICES = {
                    "PWM_CENTER center pulse of pwm": Choice(0, self),
                    "PWM_ZERO zero pulse of pwm": Choice(1, self),
                    "PWM_LS raw pwm ls generator output": Choice(2, self),
                    "PWM_HS raw pwm hs generator output": Choice(3, self),
                    "GDRV_LS_ON gdrv ls output signal": Choice(4, self),
                    "GDRV_HS_ON gdrv hs output signal": Choice(5, self),
                    "OCP_LS_CMP raw ls ocp comperator out": Choice(6, self),
                    "OCP_HS_CMP raw hs ocp comperator out": Choice(7, self),
                    "VGS_LS_ON raw ls vgs on out": Choice(8, self),
                    "VGS_HS_ON raw hs vgs on out": Choice(9, self),
                    "VGS_LS_OFF raw ls vgs off out": Choice(10, self),
                    "VGS_HS_OFF raw hs vgs off out": Choice(11, self),
                    "PHASE_HIGH phase voltage greater than 0.9VM": Choice(12, self),
                    "PHASE_LOW phase voltage less than 0.1VM": Choice(13, self),
                }

        class _END_DEGLITCH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("END_DEGLITCH", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _END_EDGE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("END_EDGE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SINGLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SINGLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CONTINUOUS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CONTINUOUS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DONE_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DONE_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DONE_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DONE_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DONE_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DONE_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DONE_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DONE_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FLEX_COMP_CONF", parent, access, address, block, signed)
            self.START_SELECT    =  self._START_SELECT(self,    Access.RW,   0x0000000F,  0,   signed=False)
            self.START_DEGLITCH  =  self._START_DEGLITCH(self,  Access.RW,   0x000000F0,  4,   signed=False)
            self.START_EDGE      =  self._START_EDGE(self,      Access.RW,   0x00000100,  8,   signed=False)
            self.END_SELECT      =  self._END_SELECT(self,      Access.RW,   0x00001E00,  9,   signed=False)
            self.END_DEGLITCH    =  self._END_DEGLITCH(self,    Access.RW,   0x0001E000,  13,  signed=False)
            self.END_EDGE        =  self._END_EDGE(self,        Access.RW,   0x00020000,  17,  signed=False)
            self.SINGLE          =  self._SINGLE(self,          Access.RWC,  0x01000000,  24,  signed=False)
            self.CONTINUOUS      =  self._CONTINUOUS(self,      Access.RW,   0x02000000,  25,  signed=False)
            self.DONE_U          =  self._DONE_U(self,          Access.RWC,  0x10000000,  28,  signed=False)
            self.DONE_V          =  self._DONE_V(self,          Access.RWC,  0x20000000,  29,  signed=False)
            self.DONE_W          =  self._DONE_W(self,          Access.RWC,  0x40000000,  30,  signed=False)
            self.DONE_Y2         =  self._DONE_Y2(self,         Access.RWC,  0x80000000,  31,  signed=False)

    class _FLEX_COMP_RESULT_V_U(Register):

        class _U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FLEX_COMP_RESULT_V_U", parent, access, address, block, signed)
            self.U  =  self._U(self,  Access.R,  0x0000FFFF,  0,   signed=False)
            self.V  =  self._V(self,  Access.R,  0xFFFF0000,  16,  signed=False)

    class _FLEX_COMP_RESULT_Y2_W(Register):

        class _W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FLEX_COMP_RESULT_Y2_W", parent, access, address, block, signed)
            self.W   =  self._W(self,   Access.R,  0x0000FFFF,  0,   signed=False)
            self.Y2  =  self._Y2(self,  Access.R,  0xFFFF0000,  16,  signed=False)

    class _GDRV_HW(Register):

        class _BRIDGE_ENABLE_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BRIDGE_ENABLE_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BRIDGE_ENABLE_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BRIDGE_ENABLE_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BRIDGE_ENABLE_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BRIDGE_ENABLE_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BRIDGE_ENABLE_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BRIDGE_ENABLE_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_OCP_CMP_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_OCP_CMP_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_OCP_CMP_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_OCP_CMP_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDRV_UVLO_CMP_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDRV_UVLO_CMP_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VS_UVLO_CMP_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VS_UVLO_CMP_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_ILIM_MAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_ILIM_MAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_SW_CP_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_SW_CP_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DISCHARGE_BST(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DISCHARGE_BST", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PHASE_DIV_GAIN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHASE_DIV_GAIN", parent, access, mask, shift, signed=signed)

                self.choice : _PHASE_DIV_GAIN_FIELD_CHOICES = {
                    "PHDIV_80 div80": Choice(0, self),
                    "PHDIV_40 div40": Choice(1, self),
                    "PHDIV_20 div20": Choice(2, self),
                    "PHDIV_10 div10": Choice(3, self),
                }

        class _PHASE_DIV_EN_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHASE_DIV_EN_UVW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PHASE_DIV_EN_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHASE_DIV_EN_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PHASE_CMP_EN_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHASE_CMP_EN_UVW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PHASE_CMP_EN_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHASE_CMP_EN_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CHARGEPUMP_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CHARGEPUMP_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BIAS_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIAS_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_AS_LS_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_AS_LS_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HIGHZ_ON_IDLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HIGHZ_ON_IDLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_HW", parent, access, address, block, signed)
            self.BRIDGE_ENABLE_U   =  self._BRIDGE_ENABLE_U(self,   Access.RW,  0x00000001,  0,   signed=False)
            self.BRIDGE_ENABLE_V   =  self._BRIDGE_ENABLE_V(self,   Access.RW,  0x00000002,  1,   signed=False)
            self.BRIDGE_ENABLE_W   =  self._BRIDGE_ENABLE_W(self,   Access.RW,  0x00000004,  2,   signed=False)
            self.BRIDGE_ENABLE_Y2  =  self._BRIDGE_ENABLE_Y2(self,  Access.RW,  0x00000008,  3,   signed=False)
            self.LS_OCP_CMP_EN     =  self._LS_OCP_CMP_EN(self,     Access.RW,  0x00000010,  4,   signed=False)
            self.HS_OCP_CMP_EN     =  self._HS_OCP_CMP_EN(self,     Access.RW,  0x00000020,  5,   signed=False)
            self.VDRV_UVLO_CMP_EN  =  self._VDRV_UVLO_CMP_EN(self,  Access.RW,  0x00000040,  6,   signed=False)
            self.VS_UVLO_CMP_EN    =  self._VS_UVLO_CMP_EN(self,    Access.RW,  0x00000080,  7,   signed=False)
            self.BST_ILIM_MAX      =  self._BST_ILIM_MAX(self,      Access.RW,  0x00000700,  8,   signed=False)
            self.BST_SW_CP_EN      =  self._BST_SW_CP_EN(self,      Access.RW,  0x00000800,  11,  signed=False)
            self.DISCHARGE_BST     =  self._DISCHARGE_BST(self,     Access.RW,  0x00001000,  12,  signed=False)
            self.PHASE_DIV_GAIN    =  self._PHASE_DIV_GAIN(self,    Access.RW,  0x00030000,  16,  signed=False)
            self.PHASE_DIV_EN_UVW  =  self._PHASE_DIV_EN_UVW(self,  Access.RW,  0x00040000,  18,  signed=False)
            self.PHASE_DIV_EN_Y2   =  self._PHASE_DIV_EN_Y2(self,   Access.RW,  0x00080000,  19,  signed=False)
            self.PHASE_CMP_EN_UVW  =  self._PHASE_CMP_EN_UVW(self,  Access.RW,  0x00100000,  20,  signed=False)
            self.PHASE_CMP_EN_Y2   =  self._PHASE_CMP_EN_Y2(self,   Access.RW,  0x00200000,  21,  signed=False)
            self.CHARGEPUMP_EN     =  self._CHARGEPUMP_EN(self,     Access.RW,  0x01000000,  24,  signed=False)
            self.BIAS_EN           =  self._BIAS_EN(self,           Access.RW,  0x02000000,  25,  signed=False)
            self.HS_AS_LS_Y2       =  self._HS_AS_LS_Y2(self,       Access.RW,  0x10000000,  28,  signed=False)
            self.HIGHZ_ON_IDLE     =  self._HIGHZ_ON_IDLE(self,     Access.RW,  0x20000000,  29,  signed=False)

    class _GDRV_CFG(Register):

        class _IGATE_SINK_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IGATE_SINK_UVW", parent, access, mask, shift, signed=signed)

                self.choice : _IGATE_SINK_UVW_FIELD_CHOICES = {
                    "SINK_40MA 40 mA": Choice(0, self),
                    "SINK_80MA 80 mA": Choice(1, self),
                    "SINK_160MA 160 mA": Choice(2, self),
                    "SINK_240MA 240 mA": Choice(3, self),
                    "SINK_320MA 320 mA": Choice(4, self),
                    "SINK_400MA 400 mA": Choice(5, self),
                    "SINK_480MA 480 mA": Choice(6, self),
                    "SINK_560MA 560 mA": Choice(7, self),
                    "SINK_640MA 640 mA": Choice(8, self),
                    "SINK_800MA 800 mA": Choice(9, self),
                    "SINK_960MA 960 mA": Choice(10, self),
                    "SINK_1120MA 1120 mA": Choice(11, self),
                    "SINK_1280MA 1280 mA": Choice(12, self),
                    "SINK_1600MA 1600 mA": Choice(13, self),
                    "SINK_1920MA 1920 mA": Choice(14, self),
                    "SINK_2000MA 2000 mA": Choice(15, self),
                }

        class _IGATE_SOURCE_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IGATE_SOURCE_UVW", parent, access, mask, shift, signed=signed)

                self.choice : _IGATE_SOURCE_UVW_FIELD_CHOICES = {
                    "SOURCE_20MA 20 mA": Choice(0, self),
                    "SOURCE_40MA 40 mA": Choice(1, self),
                    "SOURCE_80MA 80 mA": Choice(2, self),
                    "SOURCE_120MA 120 mA": Choice(3, self),
                    "SOURCE_160MA 160 mA": Choice(4, self),
                    "SOURCE_200MA 200 mA": Choice(5, self),
                    "SOURCE_240MA 240 mA": Choice(6, self),
                    "SOURCE_280MA 280mA": Choice(7, self),
                    "SOURCE_320MA 320 mA": Choice(8, self),
                    "SOURCE_400MA 400 mA": Choice(9, self),
                    "SOURCE_480MA 480 mA": Choice(10, self),
                    "SOURCE_560MA 560 mA": Choice(11, self),
                    "SOURCE_640MA 640 mA": Choice(12, self),
                    "SOURCE_800MA 800 mA": Choice(13, self),
                    "SOURCE_960MA 960 mA": Choice(14, self),
                    "SOURCE_1000MA 1000mA": Choice(15, self),
                }

        class _IGATE_SINK_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IGATE_SINK_Y2", parent, access, mask, shift, signed=signed)

                self.choice : _IGATE_SINK_Y2_FIELD_CHOICES = {
                    "SINK_40MA 40 mA": Choice(0, self),
                    "SINK_80MA 80 mA": Choice(1, self),
                    "SINK_160MA 160 mA": Choice(2, self),
                    "SINK_240MA 240 mA": Choice(3, self),
                    "SINK_320MA 320 mA": Choice(4, self),
                    "SINK_400MA 400 mA": Choice(5, self),
                    "SINK_480MA 480 mA": Choice(6, self),
                    "SINK_560MA 560 mA": Choice(7, self),
                    "SINK_640MA 640 mA": Choice(8, self),
                    "SINK_800MA 800 mA": Choice(9, self),
                    "SINK_960MA 960 mA": Choice(10, self),
                    "SINK_1120MA 1120 mA": Choice(11, self),
                    "SINK_1280MA 1280 mA": Choice(12, self),
                    "SINK_1600MA 1600 mA": Choice(13, self),
                    "SINK_1920MA 1920 mA": Choice(14, self),
                    "SINK_2000MA 2000 mA": Choice(15, self),
                }

        class _IGATE_SOURCE_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IGATE_SOURCE_Y2", parent, access, mask, shift, signed=signed)

                self.choice : _IGATE_SOURCE_Y2_FIELD_CHOICES = {
                    "SOURCE_20MA 20 mA": Choice(0, self),
                    "SOURCE_40MA 40 mA": Choice(1, self),
                    "SOURCE_80MA 80 mA": Choice(2, self),
                    "SOURCE_120MA 120 mA": Choice(3, self),
                    "SOURCE_160MA 160 mA": Choice(4, self),
                    "SOURCE_200MA 200 mA": Choice(5, self),
                    "SOURCE_240MA 240 mA": Choice(6, self),
                    "SOURCE_280MA 280mA": Choice(7, self),
                    "SOURCE_320MA 320 mA": Choice(8, self),
                    "SOURCE_400MA 400 mA": Choice(9, self),
                    "SOURCE_480MA 480 mA": Choice(10, self),
                    "SOURCE_560MA 560 mA": Choice(11, self),
                    "SOURCE_640MA 640 mA": Choice(12, self),
                    "SOURCE_800MA 800 mA": Choice(13, self),
                    "SOURCE_960MA 960 mA": Choice(14, self),
                    "SOURCE_1000MA 1000mA": Choice(15, self),
                }

        class _ADAPTIVE_MODE_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADAPTIVE_MODE_UVW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADAPTIVE_MODE_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADAPTIVE_MODE_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VS_UVLO_LVL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VS_UVLO_LVL", parent, access, mask, shift, signed=signed)

                self.choice : _VS_UVLO_LVL_FIELD_CHOICES = {
                    "VSUVLO_44 4.4V": Choice(0, self),
                    "VSUVLO_46 4.6V": Choice(1, self),
                    "VSUVLO_48 4.8V": Choice(2, self),
                    "VSUVLO_50 5.0V": Choice(3, self),
                    "VSUVLO_52 5.2V": Choice(4, self),
                    "VSUVLO_54 5.4V": Choice(5, self),
                    "VSUVLO_56 5.6V": Choice(6, self),
                    "VSUVLO_58 5.8V": Choice(7, self),
                    "VSUVLO_60 6.0V": Choice(8, self),
                    "VSUVLO_63 6.3V": Choice(9, self),
                    "VSUVLO_66 6.6V": Choice(10, self),
                    "VSUVLO_69 6.9V": Choice(11, self),
                    "VSUVLO_72 7.2V": Choice(12, self),
                    "VSUVLO_75 7.5V": Choice(13, self),
                    "VSUVLO_78 7.8V": Choice(14, self),
                    "VSUVLO_81 8.1V": Choice(15, self),
                }

        class _EXT_LS_POL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXT_LS_POL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EXT_HS_POL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXT_HS_POL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EXT_MODE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXT_MODE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_CFG", parent, access, address, block, signed)
            self.IGATE_SINK_UVW     =  self._IGATE_SINK_UVW(self,     Access.RW,  0x0000000F,  0,   signed=False)
            self.IGATE_SOURCE_UVW   =  self._IGATE_SOURCE_UVW(self,   Access.RW,  0x000000F0,  4,   signed=False)
            self.IGATE_SINK_Y2      =  self._IGATE_SINK_Y2(self,      Access.RW,  0x00000F00,  8,   signed=False)
            self.IGATE_SOURCE_Y2    =  self._IGATE_SOURCE_Y2(self,    Access.RW,  0x0000F000,  12,  signed=False)
            self.ADAPTIVE_MODE_UVW  =  self._ADAPTIVE_MODE_UVW(self,  Access.RW,  0x00010000,  16,  signed=False)
            self.ADAPTIVE_MODE_Y2   =  self._ADAPTIVE_MODE_Y2(self,   Access.RW,  0x00020000,  17,  signed=False)
            self.VS_UVLO_LVL        =  self._VS_UVLO_LVL(self,        Access.RW,  0x00F00000,  20,  signed=False)
            self.EXT_LS_POL         =  self._EXT_LS_POL(self,         Access.RW,  0x10000000,  28,  signed=False)
            self.EXT_HS_POL         =  self._EXT_HS_POL(self,         Access.RW,  0x20000000,  29,  signed=False)
            self.EXT_MODE           =  self._EXT_MODE(self,           Access.RW,  0x40000000,  30,  signed=False)

    class _GDRV_TIMING(Register):

        class _T_DRIVE_SINK_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("T_DRIVE_SINK_UVW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _T_DRIVE_SOURCE_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("T_DRIVE_SOURCE_UVW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _T_DRIVE_SINK_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("T_DRIVE_SINK_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _T_DRIVE_SOURCE_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("T_DRIVE_SOURCE_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_TIMING", parent, access, address, block, signed)
            self.T_DRIVE_SINK_UVW    =  self._T_DRIVE_SINK_UVW(self,    Access.RW,  0x000000FF,  0,   signed=False)
            self.T_DRIVE_SOURCE_UVW  =  self._T_DRIVE_SOURCE_UVW(self,  Access.RW,  0x0000FF00,  8,   signed=False)
            self.T_DRIVE_SINK_Y2     =  self._T_DRIVE_SINK_Y2(self,     Access.RW,  0x00FF0000,  16,  signed=False)
            self.T_DRIVE_SOURCE_Y2   =  self._T_DRIVE_SOURCE_Y2(self,   Access.RW,  0xFF000000,  24,  signed=False)

    class _GDRV_BBM(Register):

        class _BBM_L_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BBM_L_UVW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BBM_H_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BBM_H_UVW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BBM_L_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BBM_L_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BBM_H_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BBM_H_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_BBM", parent, access, address, block, signed)
            self.BBM_L_UVW  =  self._BBM_L_UVW(self,  Access.RW,  0x000000FF,  0,   signed=False)
            self.BBM_H_UVW  =  self._BBM_H_UVW(self,  Access.RW,  0x0000FF00,  8,   signed=False)
            self.BBM_L_Y2   =  self._BBM_L_Y2(self,   Access.RW,  0x00FF0000,  16,  signed=False)
            self.BBM_H_Y2   =  self._BBM_H_Y2(self,   Access.RW,  0xFF000000,  24,  signed=False)

    class _GDRV_PROT(Register):

        class _VGS_DEGLITCH_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VGS_DEGLITCH_UVW", parent, access, mask, shift, signed=signed)

                self.choice : _VGS_DEGLITCH_UVW_FIELD_CHOICES = {
                    "DEG_OFF off": Choice(0, self),
                    "DEG_250NS 0.25us": Choice(1, self),
                    "DEG_500NS 0.5us": Choice(2, self),
                    "DEG_1000NS 1us": Choice(3, self),
                    "DEG_2000NS 2us": Choice(4, self),
                    "DEG_4000NS 4us": Choice(5, self),
                    "DEG_6000NS 6us": Choice(6, self),
                    "DEG_8000NS 8us": Choice(7, self),
                }

        class _VGS_BLANKING_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VGS_BLANKING_UVW", parent, access, mask, shift, signed=signed)

                self.choice : _VGS_BLANKING_UVW_FIELD_CHOICES = {
                    "BLK_OFF off": Choice(0, self),
                    "BLK_250NS 0.25us": Choice(1, self),
                    "BLK_500NS 0.5us": Choice(2, self),
                    "BLK_1000NS 1us": Choice(3, self),
                }

        class _VGS_DEGLITCH_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VGS_DEGLITCH_Y2", parent, access, mask, shift, signed=signed)

                self.choice : _VGS_DEGLITCH_Y2_FIELD_CHOICES = {
                    "DEG_OFF off": Choice(0, self),
                    "DEG_250NS 0.25us": Choice(1, self),
                    "DEG_500NS 0.5us": Choice(2, self),
                    "DEG_1000NS 1us": Choice(3, self),
                    "DEG_2000NS 2us": Choice(4, self),
                    "DEG_4000NS 4us": Choice(5, self),
                    "DEG_6000NS 6us": Choice(6, self),
                    "DEG_8000NS 8us": Choice(7, self),
                }

        class _VGS_BLANKING_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VGS_BLANKING_Y2", parent, access, mask, shift, signed=signed)

                self.choice : _VGS_BLANKING_Y2_FIELD_CHOICES = {
                    "BLK_OFF off": Choice(0, self),
                    "BLK_250NS 0.25us": Choice(1, self),
                    "BLK_500NS 0.5us": Choice(2, self),
                    "BLK_1000NS 1us": Choice(3, self),
                }

        class _LS_RETRIES_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_RETRIES_UVW", parent, access, mask, shift, signed=signed)

                self.choice : _LS_RETRIES_UVW_FIELD_CHOICES = {
                    "OFF No Retries": Choice(0, self),
                    "ONE 1 Retry": Choice(1, self),
                    "TWO 2 Retries": Choice(2, self),
                    "THREE 3 Retries": Choice(3, self),
                }

        class _HS_RETRIES_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_RETRIES_UVW", parent, access, mask, shift, signed=signed)

                self.choice : _HS_RETRIES_UVW_FIELD_CHOICES = {
                    "OFF No Retries": Choice(0, self),
                    "ONE 1 Retry": Choice(1, self),
                    "TWO 2 Retries": Choice(2, self),
                    "THREE 3 Retries": Choice(3, self),
                }

        class _LS_RETRIES_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_RETRIES_Y2", parent, access, mask, shift, signed=signed)

                self.choice : _LS_RETRIES_Y2_FIELD_CHOICES = {
                    "OFF No Retries": Choice(0, self),
                    "ONE 1 Retry": Choice(1, self),
                    "TWO 2 Retries": Choice(2, self),
                    "THREE 3 Retries": Choice(3, self),
                }

        class _HS_RETRIES_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_RETRIES_Y2", parent, access, mask, shift, signed=signed)

                self.choice : _HS_RETRIES_Y2_FIELD_CHOICES = {
                    "OFF No Retries": Choice(0, self),
                    "ONE 1 Retry": Choice(1, self),
                    "TWO 2 Retries": Choice(2, self),
                    "THREE 3 Retries": Choice(3, self),
                }

        class _TERM_PWM_ON_SHORT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TERM_PWM_ON_SHORT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_PROT", parent, access, address, block, signed)
            self.VGS_DEGLITCH_UVW   =  self._VGS_DEGLITCH_UVW(self,   Access.RW,  0x00000007,  0,   signed=False)
            self.VGS_BLANKING_UVW   =  self._VGS_BLANKING_UVW(self,   Access.RW,  0x00000030,  4,   signed=False)
            self.VGS_DEGLITCH_Y2    =  self._VGS_DEGLITCH_Y2(self,    Access.RW,  0x00000700,  8,   signed=False)
            self.VGS_BLANKING_Y2    =  self._VGS_BLANKING_Y2(self,    Access.RW,  0x00003000,  12,  signed=False)
            self.LS_RETRIES_UVW     =  self._LS_RETRIES_UVW(self,     Access.RW,  0x00030000,  16,  signed=False)
            self.HS_RETRIES_UVW     =  self._HS_RETRIES_UVW(self,     Access.RW,  0x000C0000,  18,  signed=False)
            self.LS_RETRIES_Y2      =  self._LS_RETRIES_Y2(self,      Access.RW,  0x00300000,  20,  signed=False)
            self.HS_RETRIES_Y2      =  self._HS_RETRIES_Y2(self,      Access.RW,  0x00C00000,  22,  signed=False)
            self.TERM_PWM_ON_SHORT  =  self._TERM_PWM_ON_SHORT(self,  Access.RW,  0x10000000,  28,  signed=False)

    class _GDRV_OCP_UVW(Register):

        class _LS_OCP_DEGLITCH_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_OCP_DEGLITCH_UVW", parent, access, mask, shift, signed=signed)

                self.choice : _LS_OCP_DEGLITCH_UVW_FIELD_CHOICES = {
                    "DEG_OFF off": Choice(0, self),
                    "DEG_250NS 0.25us": Choice(1, self),
                    "DEG_500NS 0.5us": Choice(2, self),
                    "DEG_1000NS 1us": Choice(3, self),
                    "DEG_2000NS 2us": Choice(4, self),
                    "DEG_4000NS 4us": Choice(5, self),
                    "DEG_6000NS 6us": Choice(6, self),
                    "DEG_8000NS 8us": Choice(7, self),
                }

        class _LS_OCP_BLANKING_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_OCP_BLANKING_UVW", parent, access, mask, shift, signed=signed)

                self.choice : _LS_OCP_BLANKING_UVW_FIELD_CHOICES = {
                    "BLK_OFF off": Choice(0, self),
                    "BLK_250NS 0.25us": Choice(1, self),
                    "BLK_500NS 0.5us": Choice(2, self),
                    "BLK_1000NS 1us": Choice(3, self),
                    "BLK_2000NS 2us": Choice(4, self),
                    "BLK_4000NS 4us": Choice(5, self),
                    "BLK_6000NS 6us": Choice(6, self),
                    "BLK_8000NS 8us": Choice(7, self),
                }

        class _LS_OCP_THRES_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_OCP_THRES_UVW", parent, access, mask, shift, signed=signed)

                self.choice : _LS_OCP_THRES_UVW_FIELD_CHOICES = {
                    "82mv 63mv": Choice(0, self),
                    "166mv 125mv": Choice(1, self),
                    "248mv 187mv": Choice(2, self),
                    "330mv 248mv": Choice(3, self),
                    "414mv 312mv": Choice(4, self),
                    "498mv 374mv": Choice(5, self),
                    "582mv 434mv": Choice(6, self),
                    "660mv 504mv": Choice(7, self),
                    "123mv 705mv": Choice(8, self),
                    "249mv 940mv": Choice(9, self),
                    "372mv 1180mv": Choice(10, self),
                    "495mv 1410mv": Choice(11, self),
                    "621mv 1650mv": Choice(12, self),
                    "747mv 1880mv": Choice(13, self),
                    "873mv 2110mv": Choice(14, self),
                    "990mv 2350mv": Choice(15, self),
                }

        class _LS_OCP_USE_VDS_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_OCP_USE_VDS_UVW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_OCP_DEGLITCH_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_OCP_DEGLITCH_UVW", parent, access, mask, shift, signed=signed)

                self.choice : _HS_OCP_DEGLITCH_UVW_FIELD_CHOICES = {
                    "DEG_OFF off": Choice(0, self),
                    "DEG_250NS 0.25us": Choice(1, self),
                    "DEG_500NS 0.5us": Choice(2, self),
                    "DEG_1000NS 1us": Choice(3, self),
                    "DEG_2000NS 2us": Choice(4, self),
                    "DEG_4000NS 4us": Choice(5, self),
                    "DEG_6000NS 6us": Choice(6, self),
                    "DEG_8000NS 8us": Choice(7, self),
                }

        class _HS_OCP_BLANKING_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_OCP_BLANKING_UVW", parent, access, mask, shift, signed=signed)

                self.choice : _HS_OCP_BLANKING_UVW_FIELD_CHOICES = {
                    "BLK_OFF off": Choice(0, self),
                    "BLK_250NS 0.25us": Choice(1, self),
                    "BLK_500NS 0.5us": Choice(2, self),
                    "BLK_1000NS 1us": Choice(3, self),
                    "BLK_2000NS 2us": Choice(4, self),
                    "BLK_4000NS 4us": Choice(5, self),
                    "BLK_6000NS 6us": Choice(6, self),
                    "BLK_8000NS 8us": Choice(7, self),
                }

        class _HS_OCP_THRES_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_OCP_THRES_UVW", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_OCP_UVW", parent, access, address, block, signed)
            self.LS_OCP_DEGLITCH_UVW  =  self._LS_OCP_DEGLITCH_UVW(self,  Access.RW,  0x00000007,  0,   signed=False)
            self.LS_OCP_BLANKING_UVW  =  self._LS_OCP_BLANKING_UVW(self,  Access.RW,  0x00000070,  4,   signed=False)
            self.LS_OCP_THRES_UVW     =  self._LS_OCP_THRES_UVW(self,     Access.RW,  0x00000F00,  8,   signed=False)
            self.LS_OCP_USE_VDS_UVW   =  self._LS_OCP_USE_VDS_UVW(self,   Access.RW,  0x00008000,  15,  signed=False)
            self.HS_OCP_DEGLITCH_UVW  =  self._HS_OCP_DEGLITCH_UVW(self,  Access.RW,  0x00070000,  16,  signed=False)
            self.HS_OCP_BLANKING_UVW  =  self._HS_OCP_BLANKING_UVW(self,  Access.RW,  0x00700000,  20,  signed=False)
            self.HS_OCP_THRES_UVW     =  self._HS_OCP_THRES_UVW(self,     Access.RW,  0x0F000000,  24,  signed=False)

    class _GDRV_OCP_Y2(Register):

        class _LS_OCP_DEGLITCH_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_OCP_DEGLITCH_Y2", parent, access, mask, shift, signed=signed)

                self.choice : _LS_OCP_DEGLITCH_Y2_FIELD_CHOICES = {
                    "DEG_OFF off": Choice(0, self),
                    "DEG_250NS 0.25us": Choice(1, self),
                    "DEG_500NS 0.5us": Choice(2, self),
                    "DEG_1000NS 1us": Choice(3, self),
                    "DEG_2000NS 2us": Choice(4, self),
                    "DEG_4000NS 4us": Choice(5, self),
                    "DEG_6000NS 6us": Choice(6, self),
                    "DEG_8000NS 8us": Choice(7, self),
                }

        class _LS_OCP_BLANKING_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_OCP_BLANKING_Y2", parent, access, mask, shift, signed=signed)

                self.choice : _LS_OCP_BLANKING_Y2_FIELD_CHOICES = {
                    "BLK_OFF off": Choice(0, self),
                    "BLK_250NS 0.25us": Choice(1, self),
                    "BLK_500NS 0.5us": Choice(2, self),
                    "BLK_1000NS 1us": Choice(3, self),
                    "BLK_2000NS 2us": Choice(4, self),
                    "BLK_4000NS 4us": Choice(5, self),
                    "BLK_6000NS 6us": Choice(6, self),
                    "BLK_8000NS 8us": Choice(7, self),
                }

        class _LS_OCP_THRES_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_OCP_THRES_Y2", parent, access, mask, shift, signed=signed)

                self.choice : _LS_OCP_THRES_Y2_FIELD_CHOICES = {
                    "82mv 63mv": Choice(0, self),
                    "166mv 125mv": Choice(1, self),
                    "248mv 187mv": Choice(2, self),
                    "330mv 248mv": Choice(3, self),
                    "414mv 312mv": Choice(4, self),
                    "498mv 374mv": Choice(5, self),
                    "582mv 434mv": Choice(6, self),
                    "660mv 504mv": Choice(7, self),
                    "123mv 705mv": Choice(8, self),
                    "249mv 940mv": Choice(9, self),
                    "372mv 1180mv": Choice(10, self),
                    "495mv 1410mv": Choice(11, self),
                    "621mv 1650mv": Choice(12, self),
                    "747mv 1880mv": Choice(13, self),
                    "873mv 2110mv": Choice(14, self),
                    "990mv 2350mv": Choice(15, self),
                }

        class _LS_OCP_USE_VDS_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_OCP_USE_VDS_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_OCP_DEGLITCH_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_OCP_DEGLITCH_Y2", parent, access, mask, shift, signed=signed)

                self.choice : _HS_OCP_DEGLITCH_Y2_FIELD_CHOICES = {
                    "DEG_OFF off": Choice(0, self),
                    "DEG_250NS 0.25us": Choice(1, self),
                    "DEG_500NS 0.5us": Choice(2, self),
                    "DEG_1000NS 1us": Choice(3, self),
                    "DEG_2000NS 2us": Choice(4, self),
                    "DEG_4000NS 4us": Choice(5, self),
                    "DEG_6000NS 6us": Choice(6, self),
                    "DEG_8000NS 8us": Choice(7, self),
                }

        class _HS_OCP_BLANKING_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_OCP_BLANKING_Y2", parent, access, mask, shift, signed=signed)

                self.choice : _HS_OCP_BLANKING_Y2_FIELD_CHOICES = {
                    "BLK_OFF off": Choice(0, self),
                    "BLK_250NS 0.25us": Choice(1, self),
                    "BLK_500NS 0.5us": Choice(2, self),
                    "BLK_1000NS 1us": Choice(3, self),
                    "BLK_2000NS 2us": Choice(4, self),
                    "BLK_4000NS 4us": Choice(5, self),
                    "BLK_6000NS 6us": Choice(6, self),
                    "BLK_8000NS 8us": Choice(7, self),
                }

        class _HS_OCP_THRES_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_OCP_THRES_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_OCP_Y2", parent, access, address, block, signed)
            self.LS_OCP_DEGLITCH_Y2  =  self._LS_OCP_DEGLITCH_Y2(self,  Access.RW,  0x00000007,  0,   signed=False)
            self.LS_OCP_BLANKING_Y2  =  self._LS_OCP_BLANKING_Y2(self,  Access.RW,  0x00000070,  4,   signed=False)
            self.LS_OCP_THRES_Y2     =  self._LS_OCP_THRES_Y2(self,     Access.RW,  0x00000F00,  8,   signed=False)
            self.LS_OCP_USE_VDS_Y2   =  self._LS_OCP_USE_VDS_Y2(self,   Access.RW,  0x00008000,  15,  signed=False)
            self.HS_OCP_DEGLITCH_Y2  =  self._HS_OCP_DEGLITCH_Y2(self,  Access.RW,  0x00070000,  16,  signed=False)
            self.HS_OCP_BLANKING_Y2  =  self._HS_OCP_BLANKING_Y2(self,  Access.RW,  0x00700000,  20,  signed=False)
            self.HS_OCP_THRES_Y2     =  self._HS_OCP_THRES_Y2(self,     Access.RW,  0x0F000000,  24,  signed=False)

    class _GDRV_PROT_EN(Register):

        class _LS_SHORT_PROT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_PROT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_SHORT_PROT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_PROT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_SHORT_PROT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_PROT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_SHORT_PROT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_PROT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_PROT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_PROT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_PROT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_PROT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_PROT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_PROT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_PROT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_PROT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_PROT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_PROT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_PROT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_PROT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_PROT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_PROT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_PROT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_PROT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_PROT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_PROT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_PROT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_PROT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_PROT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_PROT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_PROT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_PROT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_PROT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_PROT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_PROT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_PROT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_PROT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_PROT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_PROT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_PROT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_PROT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_PROT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_PROT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_PROT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_PROT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_PROT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_PROT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_PROT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_PROT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_PROT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_PROT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_PROT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_PROT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_PROT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_PROT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_PROT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDRV_UVLO_PROT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDRV_UVLO_PROT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VS_UVLO_PROT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VS_UVLO_PROT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_PROT_EN", parent, access, address, block, signed)
            self.LS_SHORT_PROT_U           =  self._LS_SHORT_PROT_U(self,           Access.RW,  0x00000001,  0,   signed=False)
            self.LS_SHORT_PROT_V           =  self._LS_SHORT_PROT_V(self,           Access.RW,  0x00000002,  1,   signed=False)
            self.LS_SHORT_PROT_W           =  self._LS_SHORT_PROT_W(self,           Access.RW,  0x00000004,  2,   signed=False)
            self.LS_SHORT_PROT_Y2          =  self._LS_SHORT_PROT_Y2(self,          Access.RW,  0x00000008,  3,   signed=False)
            self.LS_VGS_OFF_SHORT_PROT_U   =  self._LS_VGS_OFF_SHORT_PROT_U(self,   Access.RW,  0x00000010,  4,   signed=False)
            self.LS_VGS_OFF_SHORT_PROT_V   =  self._LS_VGS_OFF_SHORT_PROT_V(self,   Access.RW,  0x00000020,  5,   signed=False)
            self.LS_VGS_OFF_SHORT_PROT_W   =  self._LS_VGS_OFF_SHORT_PROT_W(self,   Access.RW,  0x00000040,  6,   signed=False)
            self.LS_VGS_OFF_SHORT_PROT_Y2  =  self._LS_VGS_OFF_SHORT_PROT_Y2(self,  Access.RW,  0x00000080,  7,   signed=False)
            self.LS_VGS_ON_SHORT_PROT_U    =  self._LS_VGS_ON_SHORT_PROT_U(self,    Access.RW,  0x00000100,  8,   signed=False)
            self.LS_VGS_ON_SHORT_PROT_V    =  self._LS_VGS_ON_SHORT_PROT_V(self,    Access.RW,  0x00000200,  9,   signed=False)
            self.LS_VGS_ON_SHORT_PROT_W    =  self._LS_VGS_ON_SHORT_PROT_W(self,    Access.RW,  0x00000400,  10,  signed=False)
            self.LS_VGS_ON_SHORT_PROT_Y2   =  self._LS_VGS_ON_SHORT_PROT_Y2(self,   Access.RW,  0x00000800,  11,  signed=False)
            self.BST_UVLO_PROT_U           =  self._BST_UVLO_PROT_U(self,           Access.RW,  0x00001000,  12,  signed=False)
            self.BST_UVLO_PROT_V           =  self._BST_UVLO_PROT_V(self,           Access.RW,  0x00002000,  13,  signed=False)
            self.BST_UVLO_PROT_W           =  self._BST_UVLO_PROT_W(self,           Access.RW,  0x00004000,  14,  signed=False)
            self.BST_UVLO_PROT_Y2          =  self._BST_UVLO_PROT_Y2(self,          Access.RW,  0x00008000,  15,  signed=False)
            self.HS_SHORT_PROT_U           =  self._HS_SHORT_PROT_U(self,           Access.RW,  0x00010000,  16,  signed=False)
            self.HS_SHORT_PROT_V           =  self._HS_SHORT_PROT_V(self,           Access.RW,  0x00020000,  17,  signed=False)
            self.HS_SHORT_PROT_W           =  self._HS_SHORT_PROT_W(self,           Access.RW,  0x00040000,  18,  signed=False)
            self.HS_SHORT_PROT_Y2          =  self._HS_SHORT_PROT_Y2(self,          Access.RW,  0x00080000,  19,  signed=False)
            self.HS_VGS_OFF_SHORT_PROT_U   =  self._HS_VGS_OFF_SHORT_PROT_U(self,   Access.RW,  0x00100000,  20,  signed=False)
            self.HS_VGS_OFF_SHORT_PROT_V   =  self._HS_VGS_OFF_SHORT_PROT_V(self,   Access.RW,  0x00200000,  21,  signed=False)
            self.HS_VGS_OFF_SHORT_PROT_W   =  self._HS_VGS_OFF_SHORT_PROT_W(self,   Access.RW,  0x00400000,  22,  signed=False)
            self.HS_VGS_OFF_SHORT_PROT_Y2  =  self._HS_VGS_OFF_SHORT_PROT_Y2(self,  Access.RW,  0x00800000,  23,  signed=False)
            self.HS_VGS_ON_SHORT_PROT_U    =  self._HS_VGS_ON_SHORT_PROT_U(self,    Access.RW,  0x01000000,  24,  signed=False)
            self.HS_VGS_ON_SHORT_PROT_V    =  self._HS_VGS_ON_SHORT_PROT_V(self,    Access.RW,  0x02000000,  25,  signed=False)
            self.HS_VGS_ON_SHORT_PROT_W    =  self._HS_VGS_ON_SHORT_PROT_W(self,    Access.RW,  0x04000000,  26,  signed=False)
            self.HS_VGS_ON_SHORT_PROT_Y2   =  self._HS_VGS_ON_SHORT_PROT_Y2(self,   Access.RW,  0x08000000,  27,  signed=False)
            self.VDRV_UVLO_PROT            =  self._VDRV_UVLO_PROT(self,            Access.RW,  0x20000000,  29,  signed=False)
            self.VS_UVLO_PROT              =  self._VS_UVLO_PROT(self,              Access.RW,  0x80000000,  31,  signed=False)

    class _GDRV_STATUS_EN(Register):

        class _LS_SHORT_EN_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_EN_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_SHORT_EN_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_EN_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_SHORT_EN_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_EN_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_SHORT_EN_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_EN_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_EN_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_EN_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_EN_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_EN_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_EN_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_EN_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_EN_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_EN_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_EN_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_EN_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_EN_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_EN_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_EN_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_EN_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_EN_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_EN_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_EN_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_EN_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_EN_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_EN_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_EN_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_EN_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_EN_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_EN_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_EN_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_EN_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_EN_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_EN_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_EN_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_EN_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_EN_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_EN_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_EN_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_EN_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_EN_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_EN_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_EN_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_EN_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_EN_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_EN_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_EN_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_EN_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_EN_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_EN_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_EN_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_EN_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_EN_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_EN_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDRV_UVLO_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDRV_UVLO_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDRV_UVLWRN_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDRV_UVLWRN_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VS_UVLO_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VS_UVLO_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_STATUS_EN", parent, access, address, block, signed)
            self.LS_SHORT_EN_U           =  self._LS_SHORT_EN_U(self,           Access.RW,  0x00000001,  0,   signed=False)
            self.LS_SHORT_EN_V           =  self._LS_SHORT_EN_V(self,           Access.RW,  0x00000002,  1,   signed=False)
            self.LS_SHORT_EN_W           =  self._LS_SHORT_EN_W(self,           Access.RW,  0x00000004,  2,   signed=False)
            self.LS_SHORT_EN_Y2          =  self._LS_SHORT_EN_Y2(self,          Access.RW,  0x00000008,  3,   signed=False)
            self.LS_VGS_OFF_SHORT_EN_U   =  self._LS_VGS_OFF_SHORT_EN_U(self,   Access.RW,  0x00000010,  4,   signed=False)
            self.LS_VGS_OFF_SHORT_EN_V   =  self._LS_VGS_OFF_SHORT_EN_V(self,   Access.RW,  0x00000020,  5,   signed=False)
            self.LS_VGS_OFF_SHORT_EN_W   =  self._LS_VGS_OFF_SHORT_EN_W(self,   Access.RW,  0x00000040,  6,   signed=False)
            self.LS_VGS_OFF_SHORT_EN_Y2  =  self._LS_VGS_OFF_SHORT_EN_Y2(self,  Access.RW,  0x00000080,  7,   signed=False)
            self.LS_VGS_ON_SHORT_EN_U    =  self._LS_VGS_ON_SHORT_EN_U(self,    Access.RW,  0x00000100,  8,   signed=False)
            self.LS_VGS_ON_SHORT_EN_V    =  self._LS_VGS_ON_SHORT_EN_V(self,    Access.RW,  0x00000200,  9,   signed=False)
            self.LS_VGS_ON_SHORT_EN_W    =  self._LS_VGS_ON_SHORT_EN_W(self,    Access.RW,  0x00000400,  10,  signed=False)
            self.LS_VGS_ON_SHORT_EN_Y2   =  self._LS_VGS_ON_SHORT_EN_Y2(self,   Access.RW,  0x00000800,  11,  signed=False)
            self.BST_UVLO_EN_U           =  self._BST_UVLO_EN_U(self,           Access.RW,  0x00001000,  12,  signed=False)
            self.BST_UVLO_EN_V           =  self._BST_UVLO_EN_V(self,           Access.RW,  0x00002000,  13,  signed=False)
            self.BST_UVLO_EN_W           =  self._BST_UVLO_EN_W(self,           Access.RW,  0x00004000,  14,  signed=False)
            self.BST_UVLO_EN_Y2          =  self._BST_UVLO_EN_Y2(self,          Access.RW,  0x00008000,  15,  signed=False)
            self.HS_SHORT_EN_U           =  self._HS_SHORT_EN_U(self,           Access.RW,  0x00010000,  16,  signed=False)
            self.HS_SHORT_EN_V           =  self._HS_SHORT_EN_V(self,           Access.RW,  0x00020000,  17,  signed=False)
            self.HS_SHORT_EN_W           =  self._HS_SHORT_EN_W(self,           Access.RW,  0x00040000,  18,  signed=False)
            self.HS_SHORT_EN_Y2          =  self._HS_SHORT_EN_Y2(self,          Access.RW,  0x00080000,  19,  signed=False)
            self.HS_VGS_OFF_SHORT_EN_U   =  self._HS_VGS_OFF_SHORT_EN_U(self,   Access.RW,  0x00100000,  20,  signed=False)
            self.HS_VGS_OFF_SHORT_EN_V   =  self._HS_VGS_OFF_SHORT_EN_V(self,   Access.RW,  0x00200000,  21,  signed=False)
            self.HS_VGS_OFF_SHORT_EN_W   =  self._HS_VGS_OFF_SHORT_EN_W(self,   Access.RW,  0x00400000,  22,  signed=False)
            self.HS_VGS_OFF_SHORT_EN_Y2  =  self._HS_VGS_OFF_SHORT_EN_Y2(self,  Access.RW,  0x00800000,  23,  signed=False)
            self.HS_VGS_ON_SHORT_EN_U    =  self._HS_VGS_ON_SHORT_EN_U(self,    Access.RW,  0x01000000,  24,  signed=False)
            self.HS_VGS_ON_SHORT_EN_V    =  self._HS_VGS_ON_SHORT_EN_V(self,    Access.RW,  0x02000000,  25,  signed=False)
            self.HS_VGS_ON_SHORT_EN_W    =  self._HS_VGS_ON_SHORT_EN_W(self,    Access.RW,  0x04000000,  26,  signed=False)
            self.HS_VGS_ON_SHORT_EN_Y2   =  self._HS_VGS_ON_SHORT_EN_Y2(self,   Access.RW,  0x08000000,  27,  signed=False)
            self.VDRV_UVLO_EN            =  self._VDRV_UVLO_EN(self,            Access.RW,  0x20000000,  29,  signed=False)
            self.VDRV_UVLWRN_EN          =  self._VDRV_UVLWRN_EN(self,          Access.RW,  0x40000000,  30,  signed=False)
            self.VS_UVLO_EN              =  self._VS_UVLO_EN(self,              Access.RW,  0x80000000,  31,  signed=False)

    class _GDRV_STATUS(Register):

        class _LS_SHORT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_SHORT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_SHORT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_SHORT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDRV_UVLO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDRV_UVLO", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDRV_UVLWRN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDRV_UVLWRN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VS_UVLO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VS_UVLO", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_STATUS", parent, access, address, block, signed)
            self.LS_SHORT_U           =  self._LS_SHORT_U(self,           Access.RWC,  0x00000001,  0,   signed=False)
            self.LS_SHORT_V           =  self._LS_SHORT_V(self,           Access.RWC,  0x00000002,  1,   signed=False)
            self.LS_SHORT_W           =  self._LS_SHORT_W(self,           Access.RWC,  0x00000004,  2,   signed=False)
            self.LS_SHORT_Y2          =  self._LS_SHORT_Y2(self,          Access.RWC,  0x00000008,  3,   signed=False)
            self.LS_VGS_OFF_SHORT_U   =  self._LS_VGS_OFF_SHORT_U(self,   Access.RWC,  0x00000010,  4,   signed=False)
            self.LS_VGS_OFF_SHORT_V   =  self._LS_VGS_OFF_SHORT_V(self,   Access.RWC,  0x00000020,  5,   signed=False)
            self.LS_VGS_OFF_SHORT_W   =  self._LS_VGS_OFF_SHORT_W(self,   Access.RWC,  0x00000040,  6,   signed=False)
            self.LS_VGS_OFF_SHORT_Y2  =  self._LS_VGS_OFF_SHORT_Y2(self,  Access.RWC,  0x00000080,  7,   signed=False)
            self.LS_VGS_ON_SHORT_U    =  self._LS_VGS_ON_SHORT_U(self,    Access.RWC,  0x00000100,  8,   signed=False)
            self.LS_VGS_ON_SHORT_V    =  self._LS_VGS_ON_SHORT_V(self,    Access.RWC,  0x00000200,  9,   signed=False)
            self.LS_VGS_ON_SHORT_W    =  self._LS_VGS_ON_SHORT_W(self,    Access.RWC,  0x00000400,  10,  signed=False)
            self.LS_VGS_ON_SHORT_Y2   =  self._LS_VGS_ON_SHORT_Y2(self,   Access.RWC,  0x00000800,  11,  signed=False)
            self.BST_UVLO_U           =  self._BST_UVLO_U(self,           Access.RWC,  0x00001000,  12,  signed=False)
            self.BST_UVLO_V           =  self._BST_UVLO_V(self,           Access.RWC,  0x00002000,  13,  signed=False)
            self.BST_UVLO_W           =  self._BST_UVLO_W(self,           Access.RWC,  0x00004000,  14,  signed=False)
            self.BST_UVLO_Y2          =  self._BST_UVLO_Y2(self,          Access.RWC,  0x00008000,  15,  signed=False)
            self.HS_SHORT_U           =  self._HS_SHORT_U(self,           Access.RWC,  0x00010000,  16,  signed=False)
            self.HS_SHORT_V           =  self._HS_SHORT_V(self,           Access.RWC,  0x00020000,  17,  signed=False)
            self.HS_SHORT_W           =  self._HS_SHORT_W(self,           Access.RWC,  0x00040000,  18,  signed=False)
            self.HS_SHORT_Y2          =  self._HS_SHORT_Y2(self,          Access.RWC,  0x00080000,  19,  signed=False)
            self.HS_VGS_OFF_SHORT_U   =  self._HS_VGS_OFF_SHORT_U(self,   Access.RWC,  0x00100000,  20,  signed=False)
            self.HS_VGS_OFF_SHORT_V   =  self._HS_VGS_OFF_SHORT_V(self,   Access.RWC,  0x00200000,  21,  signed=False)
            self.HS_VGS_OFF_SHORT_W   =  self._HS_VGS_OFF_SHORT_W(self,   Access.RWC,  0x00400000,  22,  signed=False)
            self.HS_VGS_OFF_SHORT_Y2  =  self._HS_VGS_OFF_SHORT_Y2(self,  Access.RWC,  0x00800000,  23,  signed=False)
            self.HS_VGS_ON_SHORT_U    =  self._HS_VGS_ON_SHORT_U(self,    Access.RWC,  0x01000000,  24,  signed=False)
            self.HS_VGS_ON_SHORT_V    =  self._HS_VGS_ON_SHORT_V(self,    Access.RWC,  0x02000000,  25,  signed=False)
            self.HS_VGS_ON_SHORT_W    =  self._HS_VGS_ON_SHORT_W(self,    Access.RWC,  0x04000000,  26,  signed=False)
            self.HS_VGS_ON_SHORT_Y2   =  self._HS_VGS_ON_SHORT_Y2(self,   Access.RWC,  0x08000000,  27,  signed=False)
            self.VDRV_UVLO            =  self._VDRV_UVLO(self,            Access.RWC,  0x20000000,  29,  signed=False)
            self.VDRV_UVLWRN          =  self._VDRV_UVLWRN(self,          Access.RWC,  0x40000000,  30,  signed=False)
            self.VS_UVLO              =  self._VS_UVLO(self,              Access.RWC,  0x80000000,  31,  signed=False)

    class _GDRV_FAULT(Register):

        class _LS_FAULT_ACTIVE_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_FAULT_ACTIVE_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_FAULT_ACTIVE_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_FAULT_ACTIVE_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_FAULT_ACTIVE_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_FAULT_ACTIVE_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_FAULT_ACTIVE_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_FAULT_ACTIVE_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_STS_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_STS_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_STS_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_STS_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_STS_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_STS_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_STS_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_STS_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_FAULT_ACTIVE_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_FAULT_ACTIVE_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_FAULT_ACTIVE_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_FAULT_ACTIVE_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_FAULT_ACTIVE_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_FAULT_ACTIVE_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_FAULT_ACTIVE_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_FAULT_ACTIVE_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDRV_UVLO_STS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDRV_UVLO_STS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDRV_UVLWRN_STS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDRV_UVLWRN_STS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VS_UVLO_STS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VS_UVLO_STS", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_FAULT", parent, access, address, block, signed)
            self.LS_FAULT_ACTIVE_U   =  self._LS_FAULT_ACTIVE_U(self,   Access.RWC,  0x00000001,  0,   signed=False)
            self.LS_FAULT_ACTIVE_V   =  self._LS_FAULT_ACTIVE_V(self,   Access.RWC,  0x00000002,  1,   signed=False)
            self.LS_FAULT_ACTIVE_W   =  self._LS_FAULT_ACTIVE_W(self,   Access.RWC,  0x00000004,  2,   signed=False)
            self.LS_FAULT_ACTIVE_Y2  =  self._LS_FAULT_ACTIVE_Y2(self,  Access.RWC,  0x00000008,  3,   signed=False)
            self.BST_UVLO_STS_U      =  self._BST_UVLO_STS_U(self,      Access.R,    0x00001000,  12,  signed=False)
            self.BST_UVLO_STS_V      =  self._BST_UVLO_STS_V(self,      Access.R,    0x00002000,  13,  signed=False)
            self.BST_UVLO_STS_W      =  self._BST_UVLO_STS_W(self,      Access.R,    0x00004000,  14,  signed=False)
            self.BST_UVLO_STS_Y2     =  self._BST_UVLO_STS_Y2(self,     Access.R,    0x00008000,  15,  signed=False)
            self.HS_FAULT_ACTIVE_U   =  self._HS_FAULT_ACTIVE_U(self,   Access.RWC,  0x00010000,  16,  signed=False)
            self.HS_FAULT_ACTIVE_V   =  self._HS_FAULT_ACTIVE_V(self,   Access.RWC,  0x00020000,  17,  signed=False)
            self.HS_FAULT_ACTIVE_W   =  self._HS_FAULT_ACTIVE_W(self,   Access.RWC,  0x00040000,  18,  signed=False)
            self.HS_FAULT_ACTIVE_Y2  =  self._HS_FAULT_ACTIVE_Y2(self,  Access.RWC,  0x00080000,  19,  signed=False)
            self.VDRV_UVLO_STS       =  self._VDRV_UVLO_STS(self,       Access.R,    0x20000000,  29,  signed=False)
            self.VDRV_UVLWRN_STS     =  self._VDRV_UVLWRN_STS(self,     Access.R,    0x40000000,  30,  signed=False)
            self.VS_UVLO_STS         =  self._VS_UVLO_STS(self,         Access.R,    0x80000000,  31,  signed=False)

    class _ADC_I1_I0_EXT(Register):

        class _I0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _I1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I1_I0_EXT", parent, access, address, block, signed)
            self.I0  =  self._I0(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.I1  =  self._I1(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

    class _ADC_I2_EXT(Register):

        class _I2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I2_EXT", parent, access, address, block, signed)
            self.I2  =  self._I2(self,  Access.RW,  0x0000FFFF,  0,  signed=True)

    class _PWM_VX2_UX1_EXT(Register):

        class _UX1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UX1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VX2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VX2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PWM_VX2_UX1_EXT", parent, access, address, block, signed)
            self.UX1  =  self._UX1(self,  Access.RW,  0x0000FFFF,  0,   signed=False)
            self.VX2  =  self._VX2(self,  Access.RW,  0xFFFF0000,  16,  signed=False)

    class _PWM_Y2_WY1_EXT(Register):

        class _WY1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("WY1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PWM_Y2_WY1_EXT", parent, access, address, block, signed)
            self.WY1  =  self._WY1(self,  Access.RW,  0x0000FFFF,  0,   signed=False)
            self.Y2   =  self._Y2(self,   Access.RW,  0xFFFF0000,  16,  signed=False)

    class _PWM_EXT_Y2_ALT(Register):

        class _PWM_EXT_Y2_ALT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_EXT_Y2_ALT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PWM_EXT_Y2_ALT", parent, access, address, block, signed)
            self.PWM_EXT_Y2_ALT  =  self._PWM_EXT_Y2_ALT(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

    class _VOLTAGE_EXT(Register):

        class _UD(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UD", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UQ(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UQ", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("VOLTAGE_EXT", parent, access, address, block, signed)
            self.UD  =  self._UD(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.UQ  =  self._UQ(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

    class _PHI_EXT(Register):

        class _PHI_E_EXT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_E_EXT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PHI_M_EXT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_M_EXT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PHI_EXT", parent, access, address, block, signed)
            self.PHI_E_EXT  =  self._PHI_E_EXT(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.PHI_M_EXT  =  self._PHI_M_EXT(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

    class _VELOCITY_EXT(Register):

        class _VELOCITY_EXT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_EXT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("VELOCITY_EXT", parent, access, address, block, signed)
            self.VELOCITY_EXT  =  self._VELOCITY_EXT(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    def __init__(self, block=None):
        super().__init__("ALL_REGISTERS", block)
        self.INFO_CHIP                         =  self._INFO_CHIP(self,                         Access.R,    0x0000,  block,  False)
        self.INFO_VARIANT                      =  self._INFO_VARIANT(self,                      Access.R,    0x0001,  block,  False)
        self.INFO_REVISION                     =  self._INFO_REVISION(self,                     Access.R,    0x0002,  block,  False)
        self.INFO_DATE                         =  self._INFO_DATE(self,                         Access.R,    0x0003,  block,  False)
        self.ADC_I1_I0_RAW                     =  self._ADC_I1_I0_RAW(self,                     Access.R,    0x0020,  block,  False)
        self.ADC_I3_I2_RAW                     =  self._ADC_I3_I2_RAW(self,                     Access.R,    0x0021,  block,  False)
        self.ADC_U1_U0_RAW                     =  self._ADC_U1_U0_RAW(self,                     Access.R,    0x0022,  block,  False)
        self.ADC_U3_U2_RAW                     =  self._ADC_U3_U2_RAW(self,                     Access.R,    0x0023,  block,  False)
        self.ADC_TEMP_VM_RAW                   =  self._ADC_TEMP_VM_RAW(self,                   Access.R,    0x0024,  block,  False)
        self.ADC_AIN1_AIN0_RAW                 =  self._ADC_AIN1_AIN0_RAW(self,                 Access.R,    0x0025,  block,  False)
        self.ADC_AIN3_AIN2_RAW                 =  self._ADC_AIN3_AIN2_RAW(self,                 Access.R,    0x0026,  block,  False)
        self.ADC_I_GEN_CONFIG                  =  self._ADC_I_GEN_CONFIG(self,                  Access.RW,   0x0040,  block,  False)
        self.ADC_I0_CONFIG                     =  self._ADC_I0_CONFIG(self,                     Access.RW,   0x0041,  block,  False)
        self.ADC_I1_CONFIG                     =  self._ADC_I1_CONFIG(self,                     Access.RW,   0x0042,  block,  False)
        self.ADC_I2_CONFIG                     =  self._ADC_I2_CONFIG(self,                     Access.RW,   0x0043,  block,  False)
        self.ADC_I3_CONFIG                     =  self._ADC_I3_CONFIG(self,                     Access.RW,   0x0044,  block,  False)
        self.ADC_I1_I0_SCALED                  =  self._ADC_I1_I0_SCALED(self,                  Access.R,    0x0045,  block,  False)
        self.ADC_I3_I2_SCALED                  =  self._ADC_I3_I2_SCALED(self,                  Access.R,    0x0046,  block,  False)
        self.ADC_IWY_IUX                       =  self._ADC_IWY_IUX(self,                       Access.R,    0x0047,  block,  False)
        self.ADC_IV                            =  self._ADC_IV(self,                            Access.R,    0x0048,  block,  True)
        self.ADC_STATUS                        =  self._ADC_STATUS(self,                        Access.RWC,  0x0049,  block,  False)
        self.MOTOR_CONFIG                      =  self._MOTOR_CONFIG(self,                      Access.RW,   0x0060,  block,  False)
        self.MOTION_CONFIG                     =  self._MOTION_CONFIG(self,                     Access.RW,   0x0061,  block,  False)
        self.PHI_E_SELECTION                   =  self._PHI_E_SELECTION(self,                   Access.RW,   0x0062,  block,  False)
        self.PHI_E                             =  self._PHI_E(self,                             Access.R,    0x0063,  block,  True)
        self.PWM_CONFIG                        =  self._PWM_CONFIG(self,                        Access.RW,   0x0080,  block,  False)
        self.PWM_MAXCNT                        =  self._PWM_MAXCNT(self,                        Access.RW,   0x0081,  block,  False)
        self.PWM_SWITCH_LIMIT                  =  self._PWM_SWITCH_LIMIT(self,                  Access.RW,   0x0083,  block,  False)
        self.PWM_WATCHDOG_CFG                  =  self._PWM_WATCHDOG_CFG(self,                  Access.RW,   0x0084,  block,  False)
        self.ABN_PHI_E_PHI_M                   =  self._ABN_PHI_E_PHI_M(self,                   Access.R,    0x00A0,  block,  False)
        self.ABN_MODE                          =  self._ABN_MODE(self,                          Access.RW,   0x00A1,  block,  False)
        self.ABN_PPR                           =  self._ABN_PPR(self,                           Access.RW,   0x00A2,  block,  False)
        self.ABN_PPR_INV                       =  self._ABN_PPR_INV(self,                       Access.RW,   0x00A3,  block,  False)
        self.ABN_COUNT                         =  self._ABN_COUNT(self,                         Access.RW,   0x00A4,  block,  False)
        self.ABN_COUNT_N                       =  self._ABN_COUNT_N(self,                       Access.RW,   0x00A5,  block,  False)
        self.ABN_PHI_E_OFFSET                  =  self._ABN_PHI_E_OFFSET(self,                  Access.RW,   0x00A6,  block,  True)
        self.HALL_MODE                         =  self._HALL_MODE(self,                         Access.RW,   0x00C0,  block,  False)
        self.HALL_DPHI_MAX                     =  self._HALL_DPHI_MAX(self,                     Access.RW,   0x00C1,  block,  False)
        self.HALL_PHI_E_OFFSET                 =  self._HALL_PHI_E_OFFSET(self,                 Access.RW,   0x00C2,  block,  True)
        self.HALL_COUNT                        =  self._HALL_COUNT(self,                        Access.R,    0x00C3,  block,  True)
        self.HALL_PHI_E_EXTRAPOLATED_PHI_E     =  self._HALL_PHI_E_EXTRAPOLATED_PHI_E(self,     Access.R,    0x00C4,  block,  False)
        self.HALL_POSITION_060_POSITION_000    =  self._HALL_POSITION_060_POSITION_000(self,    Access.RW,   0x00C5,  block,  False)
        self.HALL_POSITION_180_POSITION_120    =  self._HALL_POSITION_180_POSITION_120(self,    Access.RW,   0x00C6,  block,  False)
        self.HALL_POSITION_300_POSITION_240    =  self._HALL_POSITION_300_POSITION_240(self,    Access.RW,   0x00C7,  block,  False)
        self.BIQUAD_V_A_1                      =  self._BIQUAD_V_A_1(self,                      Access.RW,   0x00E0,  block,  True)
        self.BIQUAD_V_A_2                      =  self._BIQUAD_V_A_2(self,                      Access.RW,   0x00E1,  block,  True)
        self.BIQUAD_V_B_0                      =  self._BIQUAD_V_B_0(self,                      Access.RW,   0x00E2,  block,  True)
        self.BIQUAD_V_B_1                      =  self._BIQUAD_V_B_1(self,                      Access.RW,   0x00E3,  block,  True)
        self.BIQUAD_V_B_2                      =  self._BIQUAD_V_B_2(self,                      Access.RW,   0x00E4,  block,  True)
        self.BIQUAD_V_ENABLE                   =  self._BIQUAD_V_ENABLE(self,                   Access.RW,   0x00E5,  block,  False)
        self.BIQUAD_T_A_1                      =  self._BIQUAD_T_A_1(self,                      Access.RW,   0x00E6,  block,  True)
        self.BIQUAD_T_A_2                      =  self._BIQUAD_T_A_2(self,                      Access.RW,   0x00E7,  block,  True)
        self.BIQUAD_T_B_0                      =  self._BIQUAD_T_B_0(self,                      Access.RW,   0x00E8,  block,  True)
        self.BIQUAD_T_B_1                      =  self._BIQUAD_T_B_1(self,                      Access.RW,   0x00E9,  block,  True)
        self.BIQUAD_T_B_2                      =  self._BIQUAD_T_B_2(self,                      Access.RW,   0x00EA,  block,  True)
        self.BIQUAD_T_ENABLE                   =  self._BIQUAD_T_ENABLE(self,                   Access.RW,   0x00EB,  block,  False)
        self.VELOCITY_CONFIG                   =  self._VELOCITY_CONFIG(self,                   Access.RW,   0x0100,  block,  False)
        self.VELOCITY_SCALING                  =  self._VELOCITY_SCALING(self,                  Access.RW,   0x0101,  block,  False)
        self.V_MIN_POS_DEV_TIME_COUNTER_LIMIT  =  self._V_MIN_POS_DEV_TIME_COUNTER_LIMIT(self,  Access.RW,   0x0102,  block,  False)
        self.MAX_VEL_DEVIATION                 =  self._MAX_VEL_DEVIATION(self,                 Access.RW,   0x0103,  block,  False)
        self.POSITION_CONFIG                   =  self._POSITION_CONFIG(self,                   Access.RW,   0x0120,  block,  False)
        self.MAX_POS_DEVIATION                 =  self._MAX_POS_DEVIATION(self,                 Access.RW,   0x0121,  block,  False)
        self.POSITION_STEP_WIDTH               =  self._POSITION_STEP_WIDTH(self,               Access.RW,   0x0122,  block,  False)
        self.RAMPER_STATUS                     =  self._RAMPER_STATUS(self,                     Access.RWC,  0x0140,  block,  False)
        self.RAMPER_A1                         =  self._RAMPER_A1(self,                         Access.RW,   0x0141,  block,  False)
        self.RAMPER_A2                         =  self._RAMPER_A2(self,                         Access.RW,   0x0142,  block,  False)
        self.RAMPER_A_MAX                      =  self._RAMPER_A_MAX(self,                      Access.RW,   0x0143,  block,  False)
        self.RAMPER_D1                         =  self._RAMPER_D1(self,                         Access.RW,   0x0144,  block,  False)
        self.RAMPER_D2                         =  self._RAMPER_D2(self,                         Access.RW,   0x0145,  block,  False)
        self.RAMPER_D_MAX                      =  self._RAMPER_D_MAX(self,                      Access.RW,   0x0146,  block,  False)
        self.RAMPER_V_START                    =  self._RAMPER_V_START(self,                    Access.RW,   0x0147,  block,  False)
        self.RAMPER_V1                         =  self._RAMPER_V1(self,                         Access.RW,   0x0148,  block,  False)
        self.RAMPER_V2                         =  self._RAMPER_V2(self,                         Access.RW,   0x0149,  block,  False)
        self.RAMPER_V_STOP                     =  self._RAMPER_V_STOP(self,                     Access.RW,   0x014A,  block,  False)
        self.RAMPER_V_MAX                      =  self._RAMPER_V_MAX(self,                      Access.RW,   0x014B,  block,  False)
        self.RAMPER_V_TARGET                   =  self._RAMPER_V_TARGET(self,                   Access.RW,   0x014C,  block,  True)
        self.RAMPER_SWITCH_MODE                =  self._RAMPER_SWITCH_MODE(self,                Access.RW,   0x014D,  block,  False)
        self.RAMPER_TIME_CONFIG                =  self._RAMPER_TIME_CONFIG(self,                Access.RW,   0x014E,  block,  False)
        self.RAMPER_A_ACTUAL                   =  self._RAMPER_A_ACTUAL(self,                   Access.R,    0x014F,  block,  True)
        self.RAMPER_X_ACTUAL                   =  self._RAMPER_X_ACTUAL(self,                   Access.R,    0x0150,  block,  True)
        self.RAMPER_V_ACTUAL                   =  self._RAMPER_V_ACTUAL(self,                   Access.R,    0x0151,  block,  True)
        self.RAMPER_X_TARGET                   =  self._RAMPER_X_TARGET(self,                   Access.RW,   0x0152,  block,  True)
        self.RAMPER_PHI_E                      =  self._RAMPER_PHI_E(self,                      Access.R,    0x0153,  block,  True)
        self.RAMPER_PHI_E_OFFSET               =  self._RAMPER_PHI_E_OFFSET(self,               Access.RW,   0x0154,  block,  True)
        self.RAMPER_ACC_FF                     =  self._RAMPER_ACC_FF(self,                     Access.RW,   0x0155,  block,  False)
        self.RAMPER_X_ACTUAL_LATCH             =  self._RAMPER_X_ACTUAL_LATCH(self,             Access.R,    0x0156,  block,  True)
        self.POSITION_ACTUAL_LATCH             =  self._POSITION_ACTUAL_LATCH(self,             Access.R,    0x0157,  block,  True)
        self.PRBS_AMPLITUDE                    =  self._PRBS_AMPLITUDE(self,                    Access.RW,   0x0160,  block,  True)
        self.PRBS_DOWN_SAMPLING_RATIO          =  self._PRBS_DOWN_SAMPLING_RATIO(self,          Access.RW,   0x0161,  block,  False)
        self.PID_CONFIG                        =  self._PID_CONFIG(self,                        Access.RW,   0x0180,  block,  False)
        self.PID_FLUX_COEFF                    =  self._PID_FLUX_COEFF(self,                    Access.RW,   0x0181,  block,  False)
        self.PID_TORQUE_COEFF                  =  self._PID_TORQUE_COEFF(self,                  Access.RW,   0x0182,  block,  False)
        self.PID_FIELDWEAK_COEFF               =  self._PID_FIELDWEAK_COEFF(self,               Access.RW,   0x0183,  block,  False)
        self.PID_U_S_MAX                       =  self._PID_U_S_MAX(self,                       Access.RW,   0x0184,  block,  False)
        self.PID_VELOCITY_COEFF                =  self._PID_VELOCITY_COEFF(self,                Access.RW,   0x0185,  block,  False)
        self.PID_POSITION_COEFF                =  self._PID_POSITION_COEFF(self,                Access.RW,   0x0186,  block,  False)
        self.PID_POSITION_TOLERANCE            =  self._PID_POSITION_TOLERANCE(self,            Access.RW,   0x0187,  block,  False)
        self.PID_POSITION_TOLERANCE_DELAY      =  self._PID_POSITION_TOLERANCE_DELAY(self,      Access.RW,   0x0188,  block,  False)
        self.PID_UQ_UD_LIMITS                  =  self._PID_UQ_UD_LIMITS(self,                  Access.RW,   0x0189,  block,  False)
        self.PID_TORQUE_FLUX_LIMITS            =  self._PID_TORQUE_FLUX_LIMITS(self,            Access.RW,   0x018A,  block,  False)
        self.PID_VELOCITY_LIMIT                =  self._PID_VELOCITY_LIMIT(self,                Access.RW,   0x018B,  block,  False)
        self.PID_POSITION_LIMIT_LOW            =  self._PID_POSITION_LIMIT_LOW(self,            Access.RW,   0x018C,  block,  True)
        self.PID_POSITION_LIMIT_HIGH           =  self._PID_POSITION_LIMIT_HIGH(self,           Access.RW,   0x018D,  block,  True)
        self.PID_TORQUE_FLUX_TARGET            =  self._PID_TORQUE_FLUX_TARGET(self,            Access.RW,   0x018E,  block,  False)
        self.PID_TORQUE_FLUX_OFFSET            =  self._PID_TORQUE_FLUX_OFFSET(self,            Access.RW,   0x018F,  block,  False)
        self.PID_VELOCITY_TARGET               =  self._PID_VELOCITY_TARGET(self,               Access.RW,   0x0190,  block,  True)
        self.PID_VELOCITY_OFFSET               =  self._PID_VELOCITY_OFFSET(self,               Access.RW,   0x0191,  block,  True)
        self.PID_POSITION_TARGET               =  self._PID_POSITION_TARGET(self,               Access.RW,   0x0192,  block,  True)
        self.PID_TORQUE_FLUX_ACTUAL            =  self._PID_TORQUE_FLUX_ACTUAL(self,            Access.R,    0x0193,  block,  False)
        self.PID_VELOCITY_ACTUAL               =  self._PID_VELOCITY_ACTUAL(self,               Access.R,    0x0194,  block,  True)
        self.PID_POSITION_ACTUAL               =  self._PID_POSITION_ACTUAL(self,               Access.RW,   0x0195,  block,  True)
        self.PID_POSITION_ACTUAL_OFFSET        =  self._PID_POSITION_ACTUAL_OFFSET(self,        Access.RW,   0x0196,  block,  True)
        self.PID_TORQUE_ERROR                  =  self._PID_TORQUE_ERROR(self,                  Access.R,    0x0197,  block,  True)
        self.PID_FLUX_ERROR                    =  self._PID_FLUX_ERROR(self,                    Access.R,    0x0198,  block,  True)
        self.PID_VELOCITY_ERROR                =  self._PID_VELOCITY_ERROR(self,                Access.R,    0x0199,  block,  True)
        self.PID_POSITION_ERROR                =  self._PID_POSITION_ERROR(self,                Access.R,    0x019A,  block,  True)
        self.PID_TORQUE_INTEGRATOR             =  self._PID_TORQUE_INTEGRATOR(self,             Access.RW,   0x019B,  block,  True)
        self.PID_FLUX_INTEGRATOR               =  self._PID_FLUX_INTEGRATOR(self,               Access.RW,   0x019C,  block,  True)
        self.PID_VELOCITY_INTEGRATOR           =  self._PID_VELOCITY_INTEGRATOR(self,           Access.RW,   0x019D,  block,  True)
        self.PID_POSITION_INTEGRATOR           =  self._PID_POSITION_INTEGRATOR(self,           Access.RW,   0x019E,  block,  True)
        self.PIDIN_TORQUE_FLUX_TARGET          =  self._PIDIN_TORQUE_FLUX_TARGET(self,          Access.R,    0x01A0,  block,  False)
        self.PIDIN_VELOCITY_TARGET             =  self._PIDIN_VELOCITY_TARGET(self,             Access.R,    0x01A1,  block,  True)
        self.PIDIN_POSITION_TARGET             =  self._PIDIN_POSITION_TARGET(self,             Access.R,    0x01A2,  block,  True)
        self.PIDIN_TORQUE_FLUX_TARGET_LIMITED  =  self._PIDIN_TORQUE_FLUX_TARGET_LIMITED(self,  Access.R,    0x01A3,  block,  False)
        self.PIDIN_VELOCITY_TARGET_LIMITED     =  self._PIDIN_VELOCITY_TARGET_LIMITED(self,     Access.R,    0x01A4,  block,  True)
        self.PIDIN_POSITION_TARGET_LIMITED     =  self._PIDIN_POSITION_TARGET_LIMITED(self,     Access.R,    0x01A5,  block,  True)
        self.FOC_IBETA_IALPHA                  =  self._FOC_IBETA_IALPHA(self,                  Access.R,    0x01A6,  block,  False)
        self.FOC_IQ_ID                         =  self._FOC_IQ_ID(self,                         Access.R,    0x01A7,  block,  False)
        self.FOC_UQ_UD                         =  self._FOC_UQ_UD(self,                         Access.R,    0x01A8,  block,  False)
        self.FOC_UQ_UD_LIMITED                 =  self._FOC_UQ_UD_LIMITED(self,                 Access.R,    0x01A9,  block,  False)
        self.FOC_UBETA_UALPHA                  =  self._FOC_UBETA_UALPHA(self,                  Access.R,    0x01AA,  block,  False)
        self.FOC_UWY_UUX                       =  self._FOC_UWY_UUX(self,                       Access.R,    0x01AB,  block,  False)
        self.FOC_UV                            =  self._FOC_UV(self,                            Access.R,    0x01AC,  block,  True)
        self.PWM_VX2_UX1                       =  self._PWM_VX2_UX1(self,                       Access.R,    0x01AD,  block,  False)
        self.PWM_Y2_WY1                        =  self._PWM_Y2_WY1(self,                        Access.R,    0x01AE,  block,  False)
        self.VELOCITY_FRQ                      =  self._VELOCITY_FRQ(self,                      Access.R,    0x01AF,  block,  True)
        self.VELOCITY_PER                      =  self._VELOCITY_PER(self,                      Access.R,    0x01B0,  block,  True)
        self.FOC_STATUS                        =  self._FOC_STATUS(self,                        Access.R,    0x01B1,  block,  False)
        self.U_S_ACTUAL_I_S_ACTUAL             =  self._U_S_ACTUAL_I_S_ACTUAL(self,             Access.R,    0x01C0,  block,  False)
        self.P_MOTOR                           =  self._P_MOTOR(self,                           Access.R,    0x01C1,  block,  False)
        self.INPUTS_RAW                        =  self._INPUTS_RAW(self,                        Access.R,    0x01C2,  block,  False)
        self.OUTPUTS_RAW                       =  self._OUTPUTS_RAW(self,                       Access.R,    0x01C3,  block,  False)
        self.STATUS_FLAGS                      =  self._STATUS_FLAGS(self,                      Access.RWC,  0x01C4,  block,  False)
        self.STATUS_MASK                       =  self._STATUS_MASK(self,                       Access.RW,   0x01C5,  block,  False)
        self.FLEX_COMP_CONF                    =  self._FLEX_COMP_CONF(self,                    Access.RWC,  0x01E0,  block,  False)
        self.FLEX_COMP_RESULT_V_U              =  self._FLEX_COMP_RESULT_V_U(self,              Access.R,    0x01E1,  block,  False)
        self.FLEX_COMP_RESULT_Y2_W             =  self._FLEX_COMP_RESULT_Y2_W(self,             Access.R,    0x01E2,  block,  False)
        self.GDRV_HW                           =  self._GDRV_HW(self,                           Access.RW,   0x01E3,  block,  False)
        self.GDRV_CFG                          =  self._GDRV_CFG(self,                          Access.RW,   0x01E4,  block,  False)
        self.GDRV_TIMING                       =  self._GDRV_TIMING(self,                       Access.RW,   0x01E9,  block,  False)
        self.GDRV_BBM                          =  self._GDRV_BBM(self,                          Access.RW,   0x01EA,  block,  False)
        self.GDRV_PROT                         =  self._GDRV_PROT(self,                         Access.RW,   0x01EB,  block,  False)
        self.GDRV_OCP_UVW                      =  self._GDRV_OCP_UVW(self,                      Access.RW,   0x01EC,  block,  False)
        self.GDRV_OCP_Y2                       =  self._GDRV_OCP_Y2(self,                       Access.RW,   0x01ED,  block,  False)
        self.GDRV_PROT_EN                      =  self._GDRV_PROT_EN(self,                      Access.RW,   0x01EE,  block,  False)
        self.GDRV_STATUS_EN                    =  self._GDRV_STATUS_EN(self,                    Access.RW,   0x01EF,  block,  False)
        self.GDRV_STATUS                       =  self._GDRV_STATUS(self,                       Access.RWC,  0x01F0,  block,  False)
        self.GDRV_FAULT                        =  self._GDRV_FAULT(self,                        Access.RWC,  0x01F1,  block,  False)
        self.ADC_I1_I0_EXT                     =  self._ADC_I1_I0_EXT(self,                     Access.RW,   0x0200,  block,  False)
        self.ADC_I2_EXT                        =  self._ADC_I2_EXT(self,                        Access.RW,   0x0201,  block,  True)
        self.PWM_VX2_UX1_EXT                   =  self._PWM_VX2_UX1_EXT(self,                   Access.RW,   0x0202,  block,  False)
        self.PWM_Y2_WY1_EXT                    =  self._PWM_Y2_WY1_EXT(self,                    Access.RW,   0x0203,  block,  False)
        self.PWM_EXT_Y2_ALT                    =  self._PWM_EXT_Y2_ALT(self,                    Access.RW,   0x0204,  block,  False)
        self.VOLTAGE_EXT                       =  self._VOLTAGE_EXT(self,                       Access.RW,   0x0205,  block,  False)
        self.PHI_EXT                           =  self._PHI_EXT(self,                           Access.RW,   0x0206,  block,  False)
        self.VELOCITY_EXT                      =  self._VELOCITY_EXT(self,                      Access.RW,   0x0208,  block,  True)

