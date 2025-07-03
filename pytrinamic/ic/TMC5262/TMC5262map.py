################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from typing import TypedDict

from pytrinamic.ic import Access, RegisterGroup, Option, Field, Register


class TMC5262Map:

    def __init__(self, *, channel=None, block=None, width=None):
        self.ALL_REGISTERS = _ALL_REGISTERS(channel, block, width)


_GCONF_FAST_STANDSTILL_FIELD_CHOICES = TypedDict("_GCONF_FAST_STANDSTILL_FIELD_CHOICES", {
    "65.536 ms": Option,
    "16.384 ms": Option,
})


_GCONF_EN_STEALTHCHOP_FIELD_CHOICES = TypedDict("_GCONF_EN_STEALTHCHOP_FIELD_CHOICES", {
    "SpreadCycle": Option,
    "StealthChopPlus": Option,
})


_GCONF_MULTISTEP_FILT_FIELD_CHOICES = TypedDict("_GCONF_MULTISTEP_FILT_FIELD_CHOICES", {
    "Filter disabled": Option,
    "Filter enabled": Option,
})


_GCONF_SHAFT_FIELD_CHOICES = TypedDict("_GCONF_SHAFT_FIELD_CHOICES", {
    "default direction": Option,
    "inverse direction": Option,
})


_GCONF_SMALL_HYSTERESIS_FIELD_CHOICES = TypedDict("_GCONF_SMALL_HYSTERESIS_FIELD_CHOICES", {
    "1/16": Option,
    "1/32": Option,
})


_GCONF_STOP_ENABLE_FIELD_CHOICES = TypedDict("_GCONF_STOP_ENABLE_FIELD_CHOICES", {
    "Normal operation": Option,
    "ENCA stops sequencer when tied high.": Option,
})


_GCONF_DIRECT_MODE_FIELD_CHOICES = TypedDict("_GCONF_DIRECT_MODE_FIELD_CHOICES", {
    "Normal operation": Option,
    "Motor coil currents and polarity directly programmed via serial interface.": Option,
})


_GCONF_OV_NN_FIELD_CHOICES = TypedDict("_GCONF_OV_NN_FIELD_CHOICES", {
    "ENCN is N-Channel": Option,
    "ENCN is OV": Option,
})


_GCONF_STEP_DIR_FIELD_CHOICES = TypedDict("_GCONF_STEP_DIR_FIELD_CHOICES", {
    "Motion controller": Option,
    "external step/dir": Option,
})


_GSTAT_RESET_FIELD_CHOICES = TypedDict("_GSTAT_RESET_FIELD_CHOICES", {
    "normal operation": Option,
    "Indicates that the IC has been reset since last clear of this bit": Option,
})


_GSTAT_DRV_ERR_FIELD_CHOICES = TypedDict("_GSTAT_DRV_ERR_FIELD_CHOICES", {
    "normal operation": Option,
    "Error detected": Option,
})


_GSTAT_UV_CP_FIELD_CHOICES = TypedDict("_GSTAT_UV_CP_FIELD_CHOICES", {
    "normal operation": Option,
    "Undervoltage on charge pump detected.": Option,
})


_GSTAT_REGISTER_RESET_FIELD_CHOICES = TypedDict("_GSTAT_REGISTER_RESET_FIELD_CHOICES", {
    "normal operation": Option,
    "Registers have been reset.": Option,
})


_GSTAT_VM_UVLO_FIELD_CHOICES = TypedDict("_GSTAT_VM_UVLO_FIELD_CHOICES", {
    "normal operation": Option,
    "VM undervoltage detected.": Option,
})


_GSTAT_VCCIO_UV_FIELD_CHOICES = TypedDict("_GSTAT_VCCIO_UV_FIELD_CHOICES", {
    "normal operation": Option,
    "VCCIO undervoltage detected.": Option,
})


_DO_CONF_DO0_ERROR_FIELD_CHOICES = TypedDict("_DO_CONF_DO0_ERROR_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO0_OTPW_FIELD_CHOICES = TypedDict("_DO_CONF_DO0_OTPW_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO0_STALL_FIELD_CHOICES = TypedDict("_DO_CONF_DO0_STALL_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO0_INDEX_FIELD_CHOICES = TypedDict("_DO_CONF_DO0_INDEX_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO0_STEP_FIELD_CHOICES = TypedDict("_DO_CONF_DO0_STEP_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO0_DIR_FIELD_CHOICES = TypedDict("_DO_CONF_DO0_DIR_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO0_XCOMP_FIELD_CHOICES = TypedDict("_DO_CONF_DO0_XCOMP_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO0_OV_FIELD_CHOICES = TypedDict("_DO_CONF_DO0_OV_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO0_DCUSTEP_FIELD_CHOICES = TypedDict("_DO_CONF_DO0_DCUSTEP_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO0_EV_STOP_REF_FIELD_CHOICES = TypedDict("_DO_CONF_DO0_EV_STOP_REF_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO0_EV_STOP_SG_FIELD_CHOICES = TypedDict("_DO_CONF_DO0_EV_STOP_SG_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO0_EV_POS_REACHED_FIELD_CHOICES = TypedDict("_DO_CONF_DO0_EV_POS_REACHED_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO0_EV_N_DEVIATION_FIELD_CHOICES = TypedDict("_DO_CONF_DO0_EV_N_DEVIATION_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO1_ERROR_FIELD_CHOICES = TypedDict("_DO_CONF_DO1_ERROR_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO1_OTPW_FIELD_CHOICES = TypedDict("_DO_CONF_DO1_OTPW_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO1_STALL_FIELD_CHOICES = TypedDict("_DO_CONF_DO1_STALL_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO1_INDEX_FIELD_CHOICES = TypedDict("_DO_CONF_DO1_INDEX_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO1_STEP_FIELD_CHOICES = TypedDict("_DO_CONF_DO1_STEP_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO1_DIR_FIELD_CHOICES = TypedDict("_DO_CONF_DO1_DIR_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO1_XCOMP_FIELD_CHOICES = TypedDict("_DO_CONF_DO1_XCOMP_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO1_OV_FIELD_CHOICES = TypedDict("_DO_CONF_DO1_OV_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO1_UDCSTEP_FIELD_CHOICES = TypedDict("_DO_CONF_DO1_UDCSTEP_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO1_EV_STOP_REF_FIELD_CHOICES = TypedDict("_DO_CONF_DO1_EV_STOP_REF_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO1_EV_STOP_SG_FIELD_CHOICES = TypedDict("_DO_CONF_DO1_EV_STOP_SG_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO1_EV_POS_REACHED_FIELD_CHOICES = TypedDict("_DO_CONF_DO1_EV_POS_REACHED_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO1_EV_N_DEVIATION_FIELD_CHOICES = TypedDict("_DO_CONF_DO1_EV_N_DEVIATION_FIELD_CHOICES", {
    "disabled": Option,
    "mapped": Option,
})


_DO_CONF_DO0_NOD_PP_FIELD_CHOICES = TypedDict("_DO_CONF_DO0_NOD_PP_FIELD_CHOICES", {
    "open drain": Option,
    "push pull": Option,
})


_DO_CONF_DO0_INVPP_FIELD_CHOICES = TypedDict("_DO_CONF_DO0_INVPP_FIELD_CHOICES", {
    "high active": Option,
    "low active": Option,
})


_DO_CONF_DO1_NOD_PP_FIELD_CHOICES = TypedDict("_DO_CONF_DO1_NOD_PP_FIELD_CHOICES", {
    "open drain": Option,
    "push pull": Option,
})


_DO_CONF_DO1_INVPP_FIELD_CHOICES = TypedDict("_DO_CONF_DO1_INVPP_FIELD_CHOICES", {
    "high active": Option,
    "low active": Option,
})


_DO_SCOPE_CONF_DO0_SCOPE_SEL_FIELD_CHOICES = TypedDict("_DO_SCOPE_CONF_DO0_SCOPE_SEL_FIELD_CHOICES", {
    "ADC_I_A": Option,
    "ADC_I_B": Option,
    "RCOIL_A": Option,
    "RCOIL_B": Option,
    "UL_A": Option,
    "UL_B": Option,
    "COOLSTEP_LOAD_RESERVE": Option,
    "ADC_TEMPERATURE": Option,
    "ANGLE_MEAS": Option,
    "SGP_RAW": Option,
    "ANGLE_CORR_CALC": Option,
    "AMPL_MEAS": Option,
    "PWM_CALC": Option,
    "CS_ACTUAL": Option,
    "UBEMF_ABS": Option,
    "SG_RESULT": Option,
    "SGP_RESULT": Option,
    "CUR_A": Option,
    "CUR_B": Option,
    "DAC_X": Option,
    "DAC_Y": Option,
    "ANGLE_ERROR": Option,
    "MSCNT": Option,
    "MSCNT_SNPSHT": Option,
    "MSCNT_OFFSET": Option,
    "TSTEP_VELOCITY[20:13]": Option,
    "TSTEP_VELOCITY[18:11]": Option,
    "TSTEP_VELOCITY[16: 9]": Option,
    "USER_VALUE": Option,
    "BEMF_A[13..7]+128": Option,
    "BEMF_A[11..5]+128": Option,
    "BEMF_A[9..3].128": Option,
})


_DO_SCOPE_CONF_DO1_SCOPE_SEL_FIELD_CHOICES = TypedDict("_DO_SCOPE_CONF_DO1_SCOPE_SEL_FIELD_CHOICES", {
    "ADC_I_A": Option,
    "ADC_I_B": Option,
    "RCOIL_A": Option,
    "RCOIL_B": Option,
    "UL_A": Option,
    "UL_B": Option,
    "COOLSTEP_LOAD_RESERVE": Option,
    "ADC_TEMPERATURE": Option,
    "ANGLE_MEAS": Option,
    "SGP_RAW": Option,
    "ANGLE_CORR_CALC": Option,
    "AMPL_MEAS": Option,
    "PWM_CALC": Option,
    "CS_ACTUAL": Option,
    "UBEMF_ABS": Option,
    "SG_RESULT": Option,
    "SGP_RESULT": Option,
    "CUR_A": Option,
    "CUR_B": Option,
    "DAC_X": Option,
    "DAC_Y": Option,
    "ANGLE_ERROR": Option,
    "MSCNT": Option,
    "MSCNT_SNPSHT": Option,
    "MSCNT_OFFSET": Option,
    "TSTEP_VELOCITY[20:13]": Option,
    "TSTEP_VELOCITY[18:11]": Option,
    "TSTEP_VELOCITY[16: 9]": Option,
    "USER_VALUE": Option,
    "BEMF_B[13..7]+128": Option,
    "BEMF_B[11..5]+128": Option,
    "BEMF_B[9..3].128": Option,
})


_IOIN_REFL_FIELD_CHOICES = TypedDict("_IOIN_REFL_FIELD_CHOICES", {
    "low": Option,
    "high": Option,
})


_IOIN_REFR_FIELD_CHOICES = TypedDict("_IOIN_REFR_FIELD_CHOICES", {
    "low": Option,
    "high": Option,
})


_IOIN_ENCB_FIELD_CHOICES = TypedDict("_IOIN_ENCB_FIELD_CHOICES", {
    "low": Option,
    "high": Option,
})


_IOIN_ENCA_FIELD_CHOICES = TypedDict("_IOIN_ENCA_FIELD_CHOICES", {
    "low": Option,
    "high": Option,
})


_IOIN_DRV_ENN_FIELD_CHOICES = TypedDict("_IOIN_DRV_ENN_FIELD_CHOICES", {
    "low": Option,
    "high": Option,
})


_IOIN_ENCN_FIELD_CHOICES = TypedDict("_IOIN_ENCN_FIELD_CHOICES", {
    "low": Option,
    "high": Option,
})


_IOIN_EXT_RES_DET_FIELD_CHOICES = TypedDict("_IOIN_EXT_RES_DET_FIELD_CHOICES", {
    "not detected. no driver operation possible": Option,
    "Detected. Normal operation.": Option,
})


_IOIN_EXT_CLK_FIELD_CHOICES = TypedDict("_IOIN_EXT_CLK_FIELD_CHOICES", {
    "no external clock detected": Option,
    "valid external clock detected": Option,
})


_X_COMPARE_REPEAT_X_COMPARE_REPEAT_FIELD_CHOICES = TypedDict("_X_COMPARE_REPEAT_X_COMPARE_REPEAT_FIELD_CHOICES", {
    "0": Option,
})


_DRV_CONF_CURRENT_RANGE_FIELD_CHOICES = TypedDict("_DRV_CONF_CURRENT_RANGE_FIELD_CHOICES", {
    "1 A": Option,
    "2 A": Option,
    "3 A": Option,
    "4 A": Option,
})


_DRV_CONF_CURRENT_RANGE_SCALE_FIELD_CHOICES = TypedDict("_DRV_CONF_CURRENT_RANGE_SCALE_FIELD_CHOICES", {
    "25 %": Option,
    "50 %": Option,
    "75 %": Option,
    "100 %": Option,
})


_DRV_CONF_SLOPE_CONTROL_FIELD_CHOICES = TypedDict("_DRV_CONF_SLOPE_CONTROL_FIELD_CHOICES", {
    "100V/us": Option,
    "200V/us": Option,
    "400V/us": Option,
    "800V/us": Option,
})


_PLL_EXT_NOT_INT_FIELD_CHOICES = TypedDict("_PLL_EXT_NOT_INT_FIELD_CHOICES", {
    "Select internal clock": Option,
    "Select external clock": Option,
})


_PLL_CLK_SYS_SEL_FIELD_CHOICES = TypedDict("_PLL_CLK_SYS_SEL_FIELD_CHOICES", {
    "Internal 16MHz clock": Option,
    "PLL clock": Option,
})


_PLL_CLK_1MO_TMO_FIELD_CHOICES = TypedDict("_PLL_CLK_1MO_TMO_FIELD_CHOICES", {
    "operational": Option,
    "pll timeout expired": Option,
})


_PLL_CLK_LOSS_FIELD_CHOICES = TypedDict("_PLL_CLK_LOSS_FIELD_CHOICES", {
    "operational": Option,
    "clock loss on pll": Option,
})


_PLL_CLK_IS_STUCK_FIELD_CHOICES = TypedDict("_PLL_CLK_IS_STUCK_FIELD_CHOICES", {
    "operational": Option,
    "issue with external clock": Option,
})


_PLL_PLL_LOCK_LOSS_FIELD_CHOICES = TypedDict("_PLL_PLL_LOCK_LOSS_FIELD_CHOICES", {
    "operational": Option,
    "pll lock loss": Option,
})


_RAMPMODE_RAMPMODE_FIELD_CHOICES = TypedDict("_RAMPMODE_RAMPMODE_FIELD_CHOICES", {
    "POSITION": Option,
    "VEL_POS": Option,
    "VEL_NEG": Option,
    "HOLD": Option,
})


_SW_MODE_STOP_L_ENABLE_FIELD_CHOICES = TypedDict("_SW_MODE_STOP_L_ENABLE_FIELD_CHOICES", {
    "disabled": Option,
    "REFL enabled": Option,
})


_SW_MODE_STOP_R_ENABLE_FIELD_CHOICES = TypedDict("_SW_MODE_STOP_R_ENABLE_FIELD_CHOICES", {
    "disabled": Option,
    "REFR enabled": Option,
})


_SW_MODE_POL_STOP_L_FIELD_CHOICES = TypedDict("_SW_MODE_POL_STOP_L_FIELD_CHOICES", {
    "high active": Option,
    "low active": Option,
})


_SW_MODE_POL_STOP_R_FIELD_CHOICES = TypedDict("_SW_MODE_POL_STOP_R_FIELD_CHOICES", {
    "high active": Option,
    "low active": Option,
})


_SW_MODE_SWAP_LR_FIELD_CHOICES = TypedDict("_SW_MODE_SWAP_LR_FIELD_CHOICES", {
    "normal order": Option,
    "left and right switch swapped": Option,
})


_SW_MODE_LATCH_L_ACTIVE_FIELD_CHOICES = TypedDict("_SW_MODE_LATCH_L_ACTIVE_FIELD_CHOICES", {
    "disabled": Option,
    "latch on active going edge": Option,
})


_SW_MODE_LATCH_L_INACTIVE_FIELD_CHOICES = TypedDict("_SW_MODE_LATCH_L_INACTIVE_FIELD_CHOICES", {
    "disabled": Option,
    "latch on inactive going edge": Option,
})


_SW_MODE_LATCH_R_ACTIVE_FIELD_CHOICES = TypedDict("_SW_MODE_LATCH_R_ACTIVE_FIELD_CHOICES", {
    "disabled": Option,
    "latch on active going edge": Option,
})


_SW_MODE_LATCH_R_INACTIVE_FIELD_CHOICES = TypedDict("_SW_MODE_LATCH_R_INACTIVE_FIELD_CHOICES", {
    "disabled": Option,
    "latch on inactive going edge": Option,
})


_SW_MODE_EN_LATCH_ENCODER_FIELD_CHOICES = TypedDict("_SW_MODE_EN_LATCH_ENCODER_FIELD_CHOICES", {
    "disabled": Option,
    "latch encoder position to ENC_LATCH": Option,
})


_SW_MODE_SG_STOP_FIELD_CHOICES = TypedDict("_SW_MODE_SG_STOP_FIELD_CHOICES", {
    "disabled": Option,
    "stop on stall": Option,
})


_SW_MODE_EN_SOFTSTOP_FIELD_CHOICES = TypedDict("_SW_MODE_EN_SOFTSTOP_FIELD_CHOICES", {
    "hardstop": Option,
    "softstop": Option,
})


_SW_MODE_EN_VIRTUAL_STOP_L_FIELD_CHOICES = TypedDict("_SW_MODE_EN_VIRTUAL_STOP_L_FIELD_CHOICES", {
    "disabled": Option,
    "enabled": Option,
})


_SW_MODE_EN_VIRTUAL_STOP_R_FIELD_CHOICES = TypedDict("_SW_MODE_EN_VIRTUAL_STOP_R_FIELD_CHOICES", {
    "disabled": Option,
    "enabled": Option,
})


_SW_MODE_VIRTUAL_STOP_ENC_FIELD_CHOICES = TypedDict("_SW_MODE_VIRTUAL_STOP_ENC_FIELD_CHOICES", {
    "XACTUAL": Option,
    "X_ENC": Option,
})


_SW_MODE_HARD_STOP_CLR_CUR_INT_FIELD_CHOICES = TypedDict("_SW_MODE_HARD_STOP_CLR_CUR_INT_FIELD_CHOICES", {
    "Keep integrator": Option,
    "Clear integrator (recommended)": Option,
})


_RAMP_STAT_STATUS_STOP_L_FIELD_CHOICES = TypedDict("_RAMP_STAT_STATUS_STOP_L_FIELD_CHOICES", {
    "inactive": Option,
    "active": Option,
})


_RAMP_STAT_STATUS_STOP_R_FIELD_CHOICES = TypedDict("_RAMP_STAT_STATUS_STOP_R_FIELD_CHOICES", {
    "inactive": Option,
    "active": Option,
})


_RAMP_STAT_STATUS_LATCH_L_FIELD_CHOICES = TypedDict("_RAMP_STAT_STATUS_LATCH_L_FIELD_CHOICES", {
    "no event": Option,
    "position latched": Option,
})


_RAMP_STAT_STATUS_LATCH_R_FIELD_CHOICES = TypedDict("_RAMP_STAT_STATUS_LATCH_R_FIELD_CHOICES", {
    "no event": Option,
    "position latched": Option,
})


_RAMP_STAT_EVENT_STOP_L_FIELD_CHOICES = TypedDict("_RAMP_STAT_EVENT_STOP_L_FIELD_CHOICES", {
    "inactive": Option,
    "active": Option,
})


_RAMP_STAT_EVENT_STOP_R_FIELD_CHOICES = TypedDict("_RAMP_STAT_EVENT_STOP_R_FIELD_CHOICES", {
    "inactive": Option,
    "active": Option,
})


_RAMP_STAT_EVENT_STOP_SG_FIELD_CHOICES = TypedDict("_RAMP_STAT_EVENT_STOP_SG_FIELD_CHOICES", {
    "inactive": Option,
    "active": Option,
})


_RAMP_STAT_EVENT_POS_REACHED_FIELD_CHOICES = TypedDict("_RAMP_STAT_EVENT_POS_REACHED_FIELD_CHOICES", {
    "inactive": Option,
    "active": Option,
})


_RAMP_STAT_VELOCITY_REACHED_FIELD_CHOICES = TypedDict("_RAMP_STAT_VELOCITY_REACHED_FIELD_CHOICES", {
    "+/-VMAX not reached": Option,
    "+/-VMAX reached": Option,
})


_RAMP_STAT_POSITION_REACHED_FIELD_CHOICES = TypedDict("_RAMP_STAT_POSITION_REACHED_FIELD_CHOICES", {
    "Target not reached": Option,
    "Target reached and stopped": Option,
})


_RAMP_STAT_VZERO_FIELD_CHOICES = TypedDict("_RAMP_STAT_VZERO_FIELD_CHOICES", {
    "moving with VACTUAL": Option,
    "velocity is 0": Option,
})


_RAMP_STAT_T_ZEROWAIT_ACTIVE_FIELD_CHOICES = TypedDict("_RAMP_STAT_T_ZEROWAIT_ACTIVE_FIELD_CHOICES", {
    "inactive": Option,
    "Motion controller in TZEROWAIT time.": Option,
})


_RAMP_STAT_SECOND_MOVE_FIELD_CHOICES = TypedDict("_RAMP_STAT_SECOND_MOVE_FIELD_CHOICES", {
    "normal motion": Option,
    "direction was changed to reach target position": Option,
})


_RAMP_STAT_STATUS_SG_FIELD_CHOICES = TypedDict("_RAMP_STAT_STATUS_SG_FIELD_CHOICES", {
    "momentary inactive": Option,
    "momentary active": Option,
})


_RAMP_STAT_STATUS_VIRTUAL_STOP_L_FIELD_CHOICES = TypedDict("_RAMP_STAT_STATUS_VIRTUAL_STOP_L_FIELD_CHOICES", {
    "inactive": Option,
    "active": Option,
})


_RAMP_STAT_STATUS_VIRTUAL_STOP_R_FIELD_CHOICES = TypedDict("_RAMP_STAT_STATUS_VIRTUAL_STOP_R_FIELD_CHOICES", {
    "0": Option,
    "1": Option,
})


_ENCMODE_POL_A_FIELD_CHOICES = TypedDict("_ENCMODE_POL_A_FIELD_CHOICES", {
    "neg": Option,
    "pos": Option,
})


_ENCMODE_POL_B_FIELD_CHOICES = TypedDict("_ENCMODE_POL_B_FIELD_CHOICES", {
    "neg": Option,
    "pos": Option,
})


_ENCMODE_POL_N_FIELD_CHOICES = TypedDict("_ENCMODE_POL_N_FIELD_CHOICES", {
    "low active": Option,
    "high active": Option,
})


_ENCMODE_IGNORE_AB_FIELD_CHOICES = TypedDict("_ENCMODE_IGNORE_AB_FIELD_CHOICES", {
    "N event when POL_A, POL_B, POL_N match": Option,
    "ignore POL_A and POL_B for N event": Option,
})


_ENCMODE_CLR_CONT_FIELD_CHOICES = TypedDict("_ENCMODE_CLR_CONT_FIELD_CHOICES", {
    "disabled": Option,
    "Always latch or latch and clear X_ENC upon an N event": Option,
})


_ENCMODE_CLR_ONCE_FIELD_CHOICES = TypedDict("_ENCMODE_CLR_ONCE_FIELD_CHOICES", {
    "disabled": Option,
    "Latch or latch and clear X_ENC on the next N event after setting this bit.": Option,
})


_ENCMODE_POS_NEG_EDGE_FIELD_CHOICES = TypedDict("_ENCMODE_POS_NEG_EDGE_FIELD_CHOICES", {
    "N channel event is active during active N event level": Option,
    "N channel is valid upon active going N event": Option,
    "N channel is valid upon inactive going N event": Option,
    "N channel is valid upon active and inactive going N event": Option,
})


_ENCMODE_CLR_ENC_X_FIELD_CHOICES = TypedDict("_ENCMODE_CLR_ENC_X_FIELD_CHOICES", {
    "Upon N event, X_ENC becomes latched to ENC_LATCH only": Option,
    "Latch and additionally clear encoder counter X_ENC at N-event": Option,
})


_ENCMODE_LATCH_X_ACT_FIELD_CHOICES = TypedDict("_ENCMODE_LATCH_X_ACT_FIELD_CHOICES", {
    "disabled": Option,
    "Latch XACTUAL together with X_ENC upon N channel event": Option,
})


_ENCMODE_ENC_SEL_DECIMAL_FIELD_CHOICES = TypedDict("_ENCMODE_ENC_SEL_DECIMAL_FIELD_CHOICES", {
    "binary": Option,
    "decimal": Option,
})


_ENCMODE_NBEMF_ABN_SEL_FIELD_CHOICES = TypedDict("_ENCMODE_NBEMF_ABN_SEL_FIELD_CHOICES", {
    "Tricoder": Option,
    "ABN-Interface": Option,
})


_ENCMODE_BEMF_HYST_FIELD_CHOICES = TypedDict("_ENCMODE_BEMF_HYST_FIELD_CHOICES", {
    "10 mV": Option,
    "25 mV": Option,
    "50 mV": Option,
    "75 mV": Option,
    "100 mV": Option,
    "150 mV": Option,
    "200 mV": Option,
    "250 mV": Option,
})


_ENCMODE_BEMF_FILTER_SEL_FIELD_CHOICES = TypedDict("_ENCMODE_BEMF_FILTER_SEL_FIELD_CHOICES", {
    "0.5 kHz": Option,
    "1 kHz": Option,
    "2 kHz": Option,
    "4.3 kHz": Option,
})


_ENC_STATUS_N_EVENT_FIELD_CHOICES = TypedDict("_ENC_STATUS_N_EVENT_FIELD_CHOICES", {
    "No event": Option,
    "N event detected": Option,
})


_ENC_STATUS_DEVIATION_WARN_FIELD_CHOICES = TypedDict("_ENC_STATUS_DEVIATION_WARN_FIELD_CHOICES", {
    "no warning": Option,
    "ENC_DEVIATION reached": Option,
})


_CUR_ANGLE_LIMIT_ANGLE_PI_INT_POS_CLIP_FIELD_CHOICES = TypedDict("_CUR_ANGLE_LIMIT_ANGLE_PI_INT_POS_CLIP_FIELD_CHOICES", {
    "Normal operation": Option,
    "Integrator reached Angle Limit": Option,
})


_CUR_ANGLE_LIMIT_ANGLE_PI_INT_NEG_CLIP_FIELD_CHOICES = TypedDict("_CUR_ANGLE_LIMIT_ANGLE_PI_INT_NEG_CLIP_FIELD_CHOICES", {
    "Normal operation": Option,
    "Integrator reached -Angle Limit": Option,
})


_CUR_ANGLE_LIMIT_ANGLE_PI_POS_CLIP_FIELD_CHOICES = TypedDict("_CUR_ANGLE_LIMIT_ANGLE_PI_POS_CLIP_FIELD_CHOICES", {
    "Normal operation": Option,
    "Angle Limit reached": Option,
})


_CUR_ANGLE_LIMIT_ANGLE_PI_NEG_CLIP_FIELD_CHOICES = TypedDict("_CUR_ANGLE_LIMIT_ANGLE_PI_NEG_CLIP_FIELD_CHOICES", {
    "Normal operation": Option,
    "-Angle Limit reached": Option,
})


_CUR_ANGLE_LIMIT_CUR_PI_INT_POS_CLIP_FIELD_CHOICES = TypedDict("_CUR_ANGLE_LIMIT_CUR_PI_INT_POS_CLIP_FIELD_CHOICES", {
    "Normal operation": Option,
    "Integrator reached CUR_PI_LIMIT": Option,
})


_CUR_ANGLE_LIMIT_CUR_PI_INT_NEG_CLIP_FIELD_CHOICES = TypedDict("_CUR_ANGLE_LIMIT_CUR_PI_INT_NEG_CLIP_FIELD_CHOICES", {
    "Normal operation": Option,
    "Integrator reached 0": Option,
})


_CUR_ANGLE_LIMIT_CUR_PI_POS_CLIP_FIELD_CHOICES = TypedDict("_CUR_ANGLE_LIMIT_CUR_PI_POS_CLIP_FIELD_CHOICES", {
    "Normal operation": Option,
    "CUR_PI_LIMIT reached": Option,
})


_CUR_ANGLE_LIMIT_CUR_PI_NEG_CLIP_FIELD_CHOICES = TypedDict("_CUR_ANGLE_LIMIT_CUR_PI_NEG_CLIP_FIELD_CHOICES", {
    "Normal operation": Option,
    "0 reached": Option,
})


_COIL_INDUCT_RCOIL_MANUAL_FIELD_CHOICES = TypedDict("_COIL_INDUCT_RCOIL_MANUAL_FIELD_CHOICES", {
    "Automatic resistance measurement: R_COIL_AUTO_A/B": Option,
    "User defined value: R_COIL_USER_A/B": Option,
})


_COIL_INDUCT_RCOIL_THERMAL_COUPLING_FIELD_CHOICES = TypedDict("_COIL_INDUCT_RCOIL_THERMAL_COUPLING_FIELD_CHOICES", {
    "disabled": Option,
    "thermal coupling enabled": Option,
})


_SGP_CONF_SGP_FILT_EN_FIELD_CHOICES = TypedDict("_SGP_CONF_SGP_FILT_EN_FIELD_CHOICES", {
    "filter disabled": Option,
    "filter enabled": Option,
})


_SGP_CONF_SGP_LOW_VEL_FREEZE_FIELD_CHOICES = TypedDict("_SGP_CONF_SGP_LOW_VEL_FREEZE_FIELD_CHOICES", {
    "clear": Option,
    "freeze": Option,
})


_SGP_CONF_SGP_CLEAR_CUR_PI_FIELD_CHOICES = TypedDict("_SGP_CONF_SGP_CLEAR_CUR_PI_FIELD_CHOICES", {
    "disabled": Option,
    "enabled": Option,
})


_SGP_CONF_SGP_LOW_VEL_CNTS_FIELD_CHOICES = TypedDict("_SGP_CONF_SGP_LOW_VEL_CNTS_FIELD_CHOICES", {
    "1 event": Option,
    "2 events": Option,
    "3 events": Option,
    "4 events": Option,
})


_COOLSTEPPLUS_CONF_COOL_CUR_DIV_FIELD_CHOICES = TypedDict("_COOLSTEPPLUS_CONF_COOL_CUR_DIV_FIELD_CHOICES", {
    "Off": Option,
    "Off, uses PI_OFF_SPEED for current increment to full current": Option,
    "1/2 IRUN": Option,
    "1/3 IRUN": Option,
    "1/4 IRUN": Option,
    "1/5 IRUN": Option,
    "1/6 IRUN": Option,
    "1/7 IRUN": Option,
    "1/8 IRUN": Option,
    "1/9 IRUN": Option,
    "1/10 IRUN": Option,
})


_COOLSTEPPLUS_CONF_LOAD_FILT_EN_FIELD_CHOICES = TypedDict("_COOLSTEPPLUS_CONF_LOAD_FILT_EN_FIELD_CHOICES", {
    "0": Option,
    "1": Option,
})


_CHOPCONF_DISFDCC_FIELD_CHOICES = TypedDict("_CHOPCONF_DISFDCC_FIELD_CHOICES", {
    "chm: current comparator terminates fd cycle": Option,
    "chm: current comparator ignored for fd cycle termination": Option,
})


_CHOPCONF_CHM_FIELD_CHOICES = TypedDict("_CHOPCONF_CHM_FIELD_CHOICES", {
    "SpreadCycle": Option,
    "Constant TOFF chopper": Option,
})


_CHOPCONF_TBL_FIELD_CHOICES = TypedDict("_CHOPCONF_TBL_FIELD_CHOICES", {
    "1.25 us": Option,
    "1.75 us": Option,
    "2.5 us": Option,
    "3.625 us": Option,
})


_CHOPCONF_MRES_FIELD_CHOICES = TypedDict("_CHOPCONF_MRES_FIELD_CHOICES", {
    "256 usteps": Option,
    "128 usteps": Option,
    "64 usteps": Option,
    "32 usteps": Option,
    "16 usteps": Option,
    "8 usteps": Option,
    "4 usteps": Option,
    "2 usteps": Option,
    "1 ustep / fullstep": Option,
    "unused": Option,
})


_CHOPCONF_INTPOL_FIELD_CHOICES = TypedDict("_CHOPCONF_INTPOL_FIELD_CHOICES", {
    "Interpolation disabled": Option,
    "Interpolation enabled": Option,
})


_CHOPCONF_DEDGE_FIELD_CHOICES = TypedDict("_CHOPCONF_DEDGE_FIELD_CHOICES", {
    "step on rising edge": Option,
    "step on both edges": Option,
})


_COOLCONF_SEUP_FIELD_CHOICES = TypedDict("_COOLCONF_SEUP_FIELD_CHOICES", {
    "8 increment per StallGuard value": Option,
    "16 increments per StallGuard value": Option,
    "32 increments per StallGuard value": Option,
    "64 increments per StallGuard value": Option,
})


_COOLCONF_SEDN_FIELD_CHOICES = TypedDict("_COOLCONF_SEDN_FIELD_CHOICES", {
    "For each 8 StallGuard2 values decrease by one": Option,
    "For each 4 StallGuard2 values decrease by one": Option,
    "For each 2 StallGuard2 values decrease by one": Option,
    "For each StallGuard2 values decrease by one": Option,
    "For each StallGuard2 values decrease by two": Option,
    "For each StallGuard2 values decrease by four": Option,
    "For each StallGuard2 values decrease by eight": Option,
    "For each StallGuard2 values decrease by sixteen": Option,
})


_COOLCONF_SEIMIN_FIELD_CHOICES = TypedDict("_COOLCONF_SEIMIN_FIELD_CHOICES", {
    "0.5 * IRUN": Option,
    "0.25 * IRUN": Option,
})


_COOLCONF_THIGH_SG_OFF_FIELD_CHOICES = TypedDict("_COOLCONF_THIGH_SG_OFF_FIELD_CHOICES", {
    "Reaching VHIGH disables coolstep": Option,
    "Reaching VHIGH disables coolstep and stop on stall": Option,
})


_COOLCONF_SFILT_FIELD_CHOICES = TypedDict("_COOLCONF_SFILT_FIELD_CHOICES", {
    "disabled": Option,
    "Stallguard signal updated every 4 fullsteps": Option,
})


_DRV_STATUS_SEQ_STOPPED_FIELD_CHOICES = TypedDict("_DRV_STATUS_SEQ_STOPPED_FIELD_CHOICES", {
    "Normal operation": Option,
    "Sequencer stopped": Option,
})


_DRV_STATUS_OV_FIELD_CHOICES = TypedDict("_DRV_STATUS_OV_FIELD_CHOICES", {
    "Normal operation": Option,
    "OVERVOLTAGE_VTH reached": Option,
})


_DRV_STATUS_S2VSA_FIELD_CHOICES = TypedDict("_DRV_STATUS_S2VSA_FIELD_CHOICES", {
    "Normal operation": Option,
    "Short to supply on phase A: driver disabled": Option,
})


_DRV_STATUS_S2VSB_FIELD_CHOICES = TypedDict("_DRV_STATUS_S2VSB_FIELD_CHOICES", {
    "Normal operation": Option,
    "Short to supply on phase B: driver disabled": Option,
})


_DRV_STATUS_STEALTH_FIELD_CHOICES = TypedDict("_DRV_STATUS_STEALTH_FIELD_CHOICES", {
    "SpreadCycle": Option,
    "StealthChop+": Option,
})


_DRV_STATUS_STALLGUARD_FIELD_CHOICES = TypedDict("_DRV_STATUS_STALLGUARD_FIELD_CHOICES", {
    "No Stall": Option,
    "Stall detected": Option,
})


_DRV_STATUS_OT_FIELD_CHOICES = TypedDict("_DRV_STATUS_OT_FIELD_CHOICES", {
    "Normal Operation": Option,
    "Overtemperature detected. Driver turned off.": Option,
})


_DRV_STATUS_OTPW_FIELD_CHOICES = TypedDict("_DRV_STATUS_OTPW_FIELD_CHOICES", {
    "Normal operation": Option,
    "OVERTEMPPREWARNING_VTH has been reached": Option,
})


_DRV_STATUS_S2GA_FIELD_CHOICES = TypedDict("_DRV_STATUS_S2GA_FIELD_CHOICES", {
    "Normal operation": Option,
    "Short to ground on phase A: driver disabled": Option,
})


_DRV_STATUS_S2GB_FIELD_CHOICES = TypedDict("_DRV_STATUS_S2GB_FIELD_CHOICES", {
    "Normal operation": Option,
    "Short to ground on phase B: driver disabled": Option,
})


_DRV_STATUS_OLA_FIELD_CHOICES = TypedDict("_DRV_STATUS_OLA_FIELD_CHOICES", {
    "Normal operation": Option,
    "open load on phase A detected": Option,
})


_DRV_STATUS_OLB_FIELD_CHOICES = TypedDict("_DRV_STATUS_OLB_FIELD_CHOICES", {
    "Normal operation": Option,
    "open load on phase B detected": Option,
})


_DRV_STATUS_STST_FIELD_CHOICES = TypedDict("_DRV_STATUS_STST_FIELD_CHOICES", {
    "no standstill detected": Option,
    "standstill detected": Option,
})


_PWMCONF_PWM_FREQ_FIELD_CHOICES = TypedDict("_PWMCONF_PWM_FREQ_FIELD_CHOICES", {
    "19.5 kHz": Option,
    "24.4 kHz": Option,
    "29.3 kHz": Option,
    "34.2 kHz": Option,
    "39.1 kHz": Option,
    "44.0 kHz": Option,
    "48.8 kHz": Option,
    "53.7 kHz": Option,
    "58.6 kHz": Option,
})


_PWMCONF_FREEWHEEL_FIELD_CHOICES = TypedDict("_PWMCONF_FREEWHEEL_FIELD_CHOICES", {
    "Normal Operation": Option,
    "Freewheeling": Option,
    "Coil shorted using LS drivers": Option,
    "Coil shorted using HS drivers": Option,
})


_PWMCONF_OL_THRSH_FIELD_CHOICES = TypedDict("_PWMCONF_OL_THRSH_FIELD_CHOICES", {
    "12.5% of target current": Option,
    "25% of target current": Option,
    "50% of target current": Option,
    "75% of target current": Option,
})


class _ALL_REGISTERS(RegisterGroup):

    class _GCONF(Register):

        class _FAST_STANDSTILL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FAST_STANDSTILL", parent, access, mask, shift, signed=signed)

                self.choice : _GCONF_FAST_STANDSTILL_FIELD_CHOICES = {
                    "65.536 ms": Option(False, self),
                    "16.384 ms": Option(True, self),
                }

        class _EN_STEALTHCHOP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EN_STEALTHCHOP", parent, access, mask, shift, signed=signed)

                self.choice : _GCONF_EN_STEALTHCHOP_FIELD_CHOICES = {
                    "SpreadCycle": Option(False, self),
                    "StealthChopPlus": Option(True, self),
                }

        class _MULTISTEP_FILT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MULTISTEP_FILT", parent, access, mask, shift, signed=signed)

                self.choice : _GCONF_MULTISTEP_FILT_FIELD_CHOICES = {
                    "Filter disabled": Option(False, self),
                    "Filter enabled": Option(True, self),
                }

        class _SHAFT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SHAFT", parent, access, mask, shift, signed=signed)

                self.choice : _GCONF_SHAFT_FIELD_CHOICES = {
                    "default direction": Option(False, self),
                    "inverse direction": Option(True, self),
                }

        class _SMALL_HYSTERESIS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SMALL_HYSTERESIS", parent, access, mask, shift, signed=signed)

                self.choice : _GCONF_SMALL_HYSTERESIS_FIELD_CHOICES = {
                    "1/16": Option(False, self),
                    "1/32": Option(True, self),
                }

        class _STOP_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice : _GCONF_STOP_ENABLE_FIELD_CHOICES = {
                    "Normal operation": Option(False, self),
                    "ENCA stops sequencer when tied high.": Option(True, self),
                }

        class _DIRECT_MODE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIRECT_MODE", parent, access, mask, shift, signed=signed)

                self.choice : _GCONF_DIRECT_MODE_FIELD_CHOICES = {
                    "Normal operation": Option(False, self),
                    "Motor coil currents and polarity directly programmed via serial interface.": Option(True, self),
                }

        class _LENGTH_STEPPULSE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LENGTH_STEPPULSE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OV_NN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OV_NN", parent, access, mask, shift, signed=signed)

                self.choice : _GCONF_OV_NN_FIELD_CHOICES = {
                    "ENCN is N-Channel": Option(False, self),
                    "ENCN is OV": Option(True, self),
                }

        class _STEP_DIR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STEP_DIR", parent, access, mask, shift, signed=signed)

                self.choice : _GCONF_STEP_DIR_FIELD_CHOICES = {
                    "Motion controller": Option(False, self),
                    "external step/dir": Option(True, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("GCONF", parent, access, address, signed)
            self.FAST_STANDSTILL   =  self._FAST_STANDSTILL( self,  Access.RW,  0x00000001,  0,   signed=False)
            self.EN_STEALTHCHOP    =  self._EN_STEALTHCHOP(  self,  Access.RW,  0x00000002,  1,   signed=False)
            self.MULTISTEP_FILT    =  self._MULTISTEP_FILT(  self,  Access.RW,  0x00000004,  2,   signed=False)
            self.SHAFT             =  self._SHAFT(           self,  Access.RW,  0x00000008,  3,   signed=False)
            self.SMALL_HYSTERESIS  =  self._SMALL_HYSTERESIS(self,  Access.RW,  0x00000010,  4,   signed=False)
            self.STOP_ENABLE       =  self._STOP_ENABLE(     self,  Access.RW,  0x00000020,  5,   signed=False)
            self.DIRECT_MODE       =  self._DIRECT_MODE(     self,  Access.RW,  0x00000040,  6,   signed=False)
            self.LENGTH_STEPPULSE  =  self._LENGTH_STEPPULSE(self,  Access.RW,  0x00000F00,  8,   signed=False)
            self.OV_NN             =  self._OV_NN(           self,  Access.RW,  0x00001000,  12,  signed=False)
            self.STEP_DIR          =  self._STEP_DIR(        self,  Access.RW,  0x80000000,  31,  signed=False)

    class _GSTAT(Register):

        class _RESET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RESET", parent, access, mask, shift, signed=signed)

                self.choice : _GSTAT_RESET_FIELD_CHOICES = {
                    "normal operation": Option(False, self),
                    "Indicates that the IC has been reset since last clear of this bit": Option(True, self),
                }

        class _DRV_ERR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DRV_ERR", parent, access, mask, shift, signed=signed)

                self.choice : _GSTAT_DRV_ERR_FIELD_CHOICES = {
                    "normal operation": Option(False, self),
                    "Error detected": Option(True, self),
                }

        class _UV_CP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UV_CP", parent, access, mask, shift, signed=signed)

                self.choice : _GSTAT_UV_CP_FIELD_CHOICES = {
                    "normal operation": Option(False, self),
                    "Undervoltage on charge pump detected.": Option(True, self),
                }

        class _REGISTER_RESET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REGISTER_RESET", parent, access, mask, shift, signed=signed)

                self.choice : _GSTAT_REGISTER_RESET_FIELD_CHOICES = {
                    "normal operation": Option(False, self),
                    "Registers have been reset.": Option(True, self),
                }

        class _VM_UVLO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VM_UVLO", parent, access, mask, shift, signed=signed)

                self.choice : _GSTAT_VM_UVLO_FIELD_CHOICES = {
                    "normal operation": Option(False, self),
                    "VM undervoltage detected.": Option(True, self),
                }

        class _VCCIO_UV(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VCCIO_UV", parent, access, mask, shift, signed=signed)

                self.choice : _GSTAT_VCCIO_UV_FIELD_CHOICES = {
                    "normal operation": Option(False, self),
                    "VCCIO undervoltage detected.": Option(True, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("GSTAT", parent, access, address, signed)
            self.RESET           =  self._RESET(         self,  Access.RWC,  0x00000001,  0,  signed=False)
            self.DRV_ERR         =  self._DRV_ERR(       self,  Access.RWC,  0x00000002,  1,  signed=False)
            self.UV_CP           =  self._UV_CP(         self,  Access.RWC,  0x00000004,  2,  signed=False)
            self.REGISTER_RESET  =  self._REGISTER_RESET(self,  Access.RWC,  0x00000008,  3,  signed=False)
            self.VM_UVLO         =  self._VM_UVLO(       self,  Access.RWC,  0x00000010,  4,  signed=False)
            self.VCCIO_UV        =  self._VCCIO_UV(      self,  Access.RWC,  0x00000020,  5,  signed=False)

    class _DO_CONF(Register):

        class _DO0_ERROR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_ERROR", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO0_ERROR_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO0_OTPW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_OTPW", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO0_OTPW_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO0_STALL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_STALL", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO0_STALL_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO0_INDEX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_INDEX", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO0_INDEX_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO0_STEP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_STEP", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO0_STEP_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO0_DIR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_DIR", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO0_DIR_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO0_XCOMP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_XCOMP", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO0_XCOMP_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO0_OV(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_OV", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO0_OV_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO0_DCUSTEP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_DCUSTEP", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO0_DCUSTEP_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO0_EV_STOP_REF(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_EV_STOP_REF", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO0_EV_STOP_REF_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO0_EV_STOP_SG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_EV_STOP_SG", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO0_EV_STOP_SG_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO0_EV_POS_REACHED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_EV_POS_REACHED", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO0_EV_POS_REACHED_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO0_EV_N_DEVIATION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_EV_N_DEVIATION", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO0_EV_N_DEVIATION_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO1_ERROR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_ERROR", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO1_ERROR_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO1_OTPW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_OTPW", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO1_OTPW_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO1_STALL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_STALL", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO1_STALL_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO1_INDEX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_INDEX", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO1_INDEX_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO1_STEP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_STEP", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO1_STEP_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO1_DIR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_DIR", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO1_DIR_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO1_XCOMP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_XCOMP", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO1_XCOMP_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO1_OV(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_OV", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO1_OV_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO1_UDCSTEP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_UDCSTEP", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO1_UDCSTEP_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO1_EV_STOP_REF(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_EV_STOP_REF", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO1_EV_STOP_REF_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO1_EV_STOP_SG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_EV_STOP_SG", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO1_EV_STOP_SG_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO1_EV_POS_REACHED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_EV_POS_REACHED", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO1_EV_POS_REACHED_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO1_EV_N_DEVIATION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_EV_N_DEVIATION", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO1_EV_N_DEVIATION_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "mapped": Option(True, self),
                }

        class _DO0_NOD_PP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_NOD_PP", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO0_NOD_PP_FIELD_CHOICES = {
                    "open drain": Option(False, self),
                    "push pull": Option(True, self),
                }

        class _DO0_INVPP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_INVPP", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO0_INVPP_FIELD_CHOICES = {
                    "high active": Option(False, self),
                    "low active": Option(True, self),
                }

        class _DO1_NOD_PP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_NOD_PP", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO1_NOD_PP_FIELD_CHOICES = {
                    "open drain": Option(False, self),
                    "push pull": Option(True, self),
                }

        class _DO1_INVPP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_INVPP", parent, access, mask, shift, signed=signed)

                self.choice : _DO_CONF_DO1_INVPP_FIELD_CHOICES = {
                    "high active": Option(False, self),
                    "low active": Option(True, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("DO_CONF", parent, access, address, signed)
            self.DO0_ERROR           =  self._DO0_ERROR(         self,  Access.RW,  0x00000001,  0,   signed=False)
            self.DO0_OTPW            =  self._DO0_OTPW(          self,  Access.RW,  0x00000002,  1,   signed=False)
            self.DO0_STALL           =  self._DO0_STALL(         self,  Access.RW,  0x00000004,  2,   signed=False)
            self.DO0_INDEX           =  self._DO0_INDEX(         self,  Access.RW,  0x00000008,  3,   signed=False)
            self.DO0_STEP            =  self._DO0_STEP(          self,  Access.RW,  0x00000010,  4,   signed=False)
            self.DO0_DIR             =  self._DO0_DIR(           self,  Access.RW,  0x00000020,  5,   signed=False)
            self.DO0_XCOMP           =  self._DO0_XCOMP(         self,  Access.RW,  0x00000040,  6,   signed=False)
            self.DO0_OV              =  self._DO0_OV(            self,  Access.RW,  0x00000080,  7,   signed=False)
            self.DO0_DCUSTEP         =  self._DO0_DCUSTEP(       self,  Access.RW,  0x00000100,  8,   signed=False)
            self.DO0_EV_STOP_REF     =  self._DO0_EV_STOP_REF(   self,  Access.RW,  0x00000200,  9,   signed=False)
            self.DO0_EV_STOP_SG      =  self._DO0_EV_STOP_SG(    self,  Access.RW,  0x00000400,  10,  signed=False)
            self.DO0_EV_POS_REACHED  =  self._DO0_EV_POS_REACHED(self,  Access.RW,  0x00000800,  11,  signed=False)
            self.DO0_EV_N_DEVIATION  =  self._DO0_EV_N_DEVIATION(self,  Access.RW,  0x00001000,  12,  signed=False)
            self.DO1_ERROR           =  self._DO1_ERROR(         self,  Access.RW,  0x00002000,  13,  signed=False)
            self.DO1_OTPW            =  self._DO1_OTPW(          self,  Access.RW,  0x00004000,  14,  signed=False)
            self.DO1_STALL           =  self._DO1_STALL(         self,  Access.RW,  0x00008000,  15,  signed=False)
            self.DO1_INDEX           =  self._DO1_INDEX(         self,  Access.RW,  0x00010000,  16,  signed=False)
            self.DO1_STEP            =  self._DO1_STEP(          self,  Access.RW,  0x00020000,  17,  signed=False)
            self.DO1_DIR             =  self._DO1_DIR(           self,  Access.RW,  0x00040000,  18,  signed=False)
            self.DO1_XCOMP           =  self._DO1_XCOMP(         self,  Access.RW,  0x00080000,  19,  signed=False)
            self.DO1_OV              =  self._DO1_OV(            self,  Access.RW,  0x00100000,  20,  signed=False)
            self.DO1_UDCSTEP         =  self._DO1_UDCSTEP(       self,  Access.RW,  0x00200000,  21,  signed=False)
            self.DO1_EV_STOP_REF     =  self._DO1_EV_STOP_REF(   self,  Access.RW,  0x00400000,  22,  signed=False)
            self.DO1_EV_STOP_SG      =  self._DO1_EV_STOP_SG(    self,  Access.RW,  0x00800000,  23,  signed=False)
            self.DO1_EV_POS_REACHED  =  self._DO1_EV_POS_REACHED(self,  Access.RW,  0x01000000,  24,  signed=False)
            self.DO1_EV_N_DEVIATION  =  self._DO1_EV_N_DEVIATION(self,  Access.RW,  0x02000000,  25,  signed=False)
            self.DO0_NOD_PP          =  self._DO0_NOD_PP(        self,  Access.RW,  0x10000000,  28,  signed=False)
            self.DO0_INVPP           =  self._DO0_INVPP(         self,  Access.RW,  0x20000000,  29,  signed=False)
            self.DO1_NOD_PP          =  self._DO1_NOD_PP(        self,  Access.RW,  0x40000000,  30,  signed=False)
            self.DO1_INVPP           =  self._DO1_INVPP(         self,  Access.RW,  0x80000000,  31,  signed=False)

    class _DO_SCOPE_CONF(Register):

        class _DO0_SCOPE_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_SCOPE_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DO0_SCOPE_SEL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_SCOPE_SEL", parent, access, mask, shift, signed=signed)

                self.choice : _DO_SCOPE_CONF_DO0_SCOPE_SEL_FIELD_CHOICES = {
                    "ADC_I_A": Option(0, self),
                    "ADC_I_B": Option(1, self),
                    "RCOIL_A": Option(2, self),
                    "RCOIL_B": Option(3, self),
                    "UL_A": Option(4, self),
                    "UL_B": Option(5, self),
                    "COOLSTEP_LOAD_RESERVE": Option(6, self),
                    "ADC_TEMPERATURE": Option(7, self),
                    "ANGLE_MEAS": Option(8, self),
                    "SGP_RAW": Option(9, self),
                    "ANGLE_CORR_CALC": Option(10, self),
                    "AMPL_MEAS": Option(11, self),
                    "PWM_CALC": Option(12, self),
                    "CS_ACTUAL": Option(13, self),
                    "UBEMF_ABS": Option(14, self),
                    "SG_RESULT": Option(15, self),
                    "SGP_RESULT": Option(16, self),
                    "CUR_A": Option(17, self),
                    "CUR_B": Option(18, self),
                    "DAC_X": Option(19, self),
                    "DAC_Y": Option(20, self),
                    "ANGLE_ERROR": Option(21, self),
                    "MSCNT": Option(22, self),
                    "MSCNT_SNPSHT": Option(23, self),
                    "MSCNT_OFFSET": Option(24, self),
                    "TSTEP_VELOCITY[20:13]": Option(25, self),
                    "TSTEP_VELOCITY[18:11]": Option(26, self),
                    "TSTEP_VELOCITY[16: 9]": Option(27, self),
                    "USER_VALUE": Option(28, self),
                    "BEMF_A[13..7]+128": Option(29, self),
                    "BEMF_A[11..5]+128": Option(30, self),
                    "BEMF_A[9..3].128": Option(31, self),
                }

        class _DO1_SCOPE_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_SCOPE_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DO1_SCOPE_SEL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_SCOPE_SEL", parent, access, mask, shift, signed=signed)

                self.choice : _DO_SCOPE_CONF_DO1_SCOPE_SEL_FIELD_CHOICES = {
                    "ADC_I_A": Option(0, self),
                    "ADC_I_B": Option(1, self),
                    "RCOIL_A": Option(2, self),
                    "RCOIL_B": Option(3, self),
                    "UL_A": Option(4, self),
                    "UL_B": Option(5, self),
                    "COOLSTEP_LOAD_RESERVE": Option(6, self),
                    "ADC_TEMPERATURE": Option(7, self),
                    "ANGLE_MEAS": Option(8, self),
                    "SGP_RAW": Option(9, self),
                    "ANGLE_CORR_CALC": Option(10, self),
                    "AMPL_MEAS": Option(11, self),
                    "PWM_CALC": Option(12, self),
                    "CS_ACTUAL": Option(13, self),
                    "UBEMF_ABS": Option(14, self),
                    "SG_RESULT": Option(15, self),
                    "SGP_RESULT": Option(16, self),
                    "CUR_A": Option(17, self),
                    "CUR_B": Option(18, self),
                    "DAC_X": Option(19, self),
                    "DAC_Y": Option(20, self),
                    "ANGLE_ERROR": Option(21, self),
                    "MSCNT": Option(22, self),
                    "MSCNT_SNPSHT": Option(23, self),
                    "MSCNT_OFFSET": Option(24, self),
                    "TSTEP_VELOCITY[20:13]": Option(25, self),
                    "TSTEP_VELOCITY[18:11]": Option(26, self),
                    "TSTEP_VELOCITY[16: 9]": Option(27, self),
                    "USER_VALUE": Option(28, self),
                    "BEMF_B[13..7]+128": Option(29, self),
                    "BEMF_B[11..5]+128": Option(30, self),
                    "BEMF_B[9..3].128": Option(31, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("DO_SCOPE_CONF", parent, access, address, signed)
            self.DO0_SCOPE_EN   =  self._DO0_SCOPE_EN( self,  Access.RW,  0x00000001,  0,   signed=False)
            self.DO0_SCOPE_SEL  =  self._DO0_SCOPE_SEL(self,  Access.RW,  0x000001F0,  4,   signed=False)
            self.DO1_SCOPE_EN   =  self._DO1_SCOPE_EN( self,  Access.RW,  0x00001000,  12,  signed=False)
            self.DO1_SCOPE_SEL  =  self._DO1_SCOPE_SEL(self,  Access.RW,  0x001F0000,  16,  signed=False)

    class _IOIN(Register):

        class _REFL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REFL", parent, access, mask, shift, signed=signed)

                self.choice : _IOIN_REFL_FIELD_CHOICES = {
                    "low": Option(False, self),
                    "high": Option(True, self),
                }

        class _REFR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REFR", parent, access, mask, shift, signed=signed)

                self.choice : _IOIN_REFR_FIELD_CHOICES = {
                    "low": Option(False, self),
                    "high": Option(True, self),
                }

        class _ENCB(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENCB", parent, access, mask, shift, signed=signed)

                self.choice : _IOIN_ENCB_FIELD_CHOICES = {
                    "low": Option(False, self),
                    "high": Option(True, self),
                }

        class _ENCA(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENCA", parent, access, mask, shift, signed=signed)

                self.choice : _IOIN_ENCA_FIELD_CHOICES = {
                    "low": Option(False, self),
                    "high": Option(True, self),
                }

        class _DRV_ENN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DRV_ENN", parent, access, mask, shift, signed=signed)

                self.choice : _IOIN_DRV_ENN_FIELD_CHOICES = {
                    "low": Option(False, self),
                    "high": Option(True, self),
                }

        class _ENCN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENCN", parent, access, mask, shift, signed=signed)

                self.choice : _IOIN_ENCN_FIELD_CHOICES = {
                    "low": Option(False, self),
                    "high": Option(True, self),
                }

        class _EXT_RES_DET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXT_RES_DET", parent, access, mask, shift, signed=signed)

                self.choice : _IOIN_EXT_RES_DET_FIELD_CHOICES = {
                    "not detected. no driver operation possible": Option(False, self),
                    "Detected. Normal operation.": Option(True, self),
                }

        class _EXT_CLK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXT_CLK", parent, access, mask, shift, signed=signed)

                self.choice : _IOIN_EXT_CLK_FIELD_CHOICES = {
                    "no external clock detected": Option(False, self),
                    "valid external clock detected": Option(True, self),
                }

        class _SILICON_RV(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SILICON_RV", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("IOIN", parent, access, address, signed)
            self.REFL         =  self._REFL(       self,  Access.R,  0x00000001,  0,   signed=False)
            self.REFR         =  self._REFR(       self,  Access.R,  0x00000002,  1,   signed=False)
            self.ENCB         =  self._ENCB(       self,  Access.R,  0x00000004,  2,   signed=False)
            self.ENCA         =  self._ENCA(       self,  Access.R,  0x00000008,  3,   signed=False)
            self.DRV_ENN      =  self._DRV_ENN(    self,  Access.R,  0x00000010,  4,   signed=False)
            self.ENCN         =  self._ENCN(       self,  Access.R,  0x00000020,  5,   signed=False)
            self.EXT_RES_DET  =  self._EXT_RES_DET(self,  Access.R,  0x00002000,  13,  signed=False)
            self.EXT_CLK      =  self._EXT_CLK(    self,  Access.R,  0x00004000,  14,  signed=False)
            self.SILICON_RV   =  self._SILICON_RV( self,  Access.R,  0x00070000,  16,  signed=False)

    class _X_COMPARE(Register):

        class _X_COMPARE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("X_COMPARE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("X_COMPARE", parent, access, address, signed)
            self.X_COMPARE  =  self._X_COMPARE(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _X_COMPARE_REPEAT(Register):

        class _X_COMPARE_REPEAT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("X_COMPARE_REPEAT", parent, access, mask, shift, signed=signed)

                self.choice : _X_COMPARE_REPEAT_X_COMPARE_REPEAT_FIELD_CHOICES = {
                    "0": Option(0, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("X_COMPARE_REPEAT", parent, access, address, signed)
            self.X_COMPARE_REPEAT  =  self._X_COMPARE_REPEAT(self,  Access.RW,  0x00FFFFFF,  0,  signed=False)

    class _DRV_CONF(Register):

        class _CURRENT_RANGE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CURRENT_RANGE", parent, access, mask, shift, signed=signed)

                self.choice : _DRV_CONF_CURRENT_RANGE_FIELD_CHOICES = {
                    "1 A": Option(0, self),
                    "2 A": Option(1, self),
                    "3 A": Option(2, self),
                    "4 A": Option(3, self),
                }

        class _CURRENT_RANGE_SCALE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CURRENT_RANGE_SCALE", parent, access, mask, shift, signed=signed)

                self.choice : _DRV_CONF_CURRENT_RANGE_SCALE_FIELD_CHOICES = {
                    "25 %": Option(0, self),
                    "50 %": Option(1, self),
                    "75 %": Option(2, self),
                    "100 %": Option(3, self),
                }

        class _SLOPE_CONTROL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SLOPE_CONTROL", parent, access, mask, shift, signed=signed)

                self.choice : _DRV_CONF_SLOPE_CONTROL_FIELD_CHOICES = {
                    "100V/us": Option(0, self),
                    "200V/us": Option(1, self),
                    "400V/us": Option(2, self),
                    "800V/us": Option(3, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("DRV_CONF", parent, access, address, signed)
            self.CURRENT_RANGE        =  self._CURRENT_RANGE(      self,  Access.RW,  0x00000003,  0,  signed=False)
            self.CURRENT_RANGE_SCALE  =  self._CURRENT_RANGE_SCALE(self,  Access.RW,  0x0000000C,  2,  signed=False)
            self.SLOPE_CONTROL        =  self._SLOPE_CONTROL(      self,  Access.RW,  0x00000030,  4,  signed=False)

    class _PLL(Register):

        class _COMMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COMMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EXT_NOT_INT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXT_NOT_INT", parent, access, mask, shift, signed=signed)

                self.choice : _PLL_EXT_NOT_INT_FIELD_CHOICES = {
                    "Select internal clock": Option(False, self),
                    "Select external clock": Option(True, self),
                }

        class _CLK_SYS_SEL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_SYS_SEL", parent, access, mask, shift, signed=signed)

                self.choice : _PLL_CLK_SYS_SEL_FIELD_CHOICES = {
                    "Internal 16MHz clock": Option(False, self),
                    "PLL clock": Option(True, self),
                }

        class _ADC_CLK_ENA(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_CLK_ENA", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_CLK_ENA(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_CLK_ENA", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CLOCK_DIVIDER(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLOCK_DIVIDER", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CLK_FSM_ENA(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_FSM_ENA", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CLK_1MO_TMO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_1MO_TMO", parent, access, mask, shift, signed=signed)

                self.choice : _PLL_CLK_1MO_TMO_FIELD_CHOICES = {
                    "operational": Option(False, self),
                    "pll timeout expired": Option(True, self),
                }

        class _CLK_LOSS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_LOSS", parent, access, mask, shift, signed=signed)

                self.choice : _PLL_CLK_LOSS_FIELD_CHOICES = {
                    "operational": Option(False, self),
                    "clock loss on pll": Option(True, self),
                }

        class _CLK_IS_STUCK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_IS_STUCK", parent, access, mask, shift, signed=signed)

                self.choice : _PLL_CLK_IS_STUCK_FIELD_CHOICES = {
                    "operational": Option(False, self),
                    "issue with external clock": Option(True, self),
                }

        class _PLL_LOCK_LOSS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PLL_LOCK_LOSS", parent, access, mask, shift, signed=signed)

                self.choice : _PLL_PLL_LOCK_LOSS_FIELD_CHOICES = {
                    "operational": Option(False, self),
                    "pll lock loss": Option(True, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("PLL", parent, access, address, signed)
            self.COMMIT         =  self._COMMIT(       self,  Access.RW,  0x00000001,  0,   signed=False)
            self.EXT_NOT_INT    =  self._EXT_NOT_INT(  self,  Access.RW,  0x00000002,  1,   signed=False)
            self.CLK_SYS_SEL    =  self._CLK_SYS_SEL(  self,  Access.RW,  0x00000004,  2,   signed=False)
            self.ADC_CLK_ENA    =  self._ADC_CLK_ENA(  self,  Access.RW,  0x00000008,  3,   signed=False)
            self.PWM_CLK_ENA    =  self._PWM_CLK_ENA(  self,  Access.RW,  0x00000010,  4,   signed=False)
            self.CLOCK_DIVIDER  =  self._CLOCK_DIVIDER(self,  Access.RW,  0x000003E0,  5,   signed=False)
            self.CLK_FSM_ENA    =  self._CLK_FSM_ENA(  self,  Access.RW,  0x00000400,  10,  signed=False)
            self.CLK_1MO_TMO    =  self._CLK_1MO_TMO(  self,  Access.RW,  0x00001000,  12,  signed=False)
            self.CLK_LOSS       =  self._CLK_LOSS(     self,  Access.RW,  0x00002000,  13,  signed=False)
            self.CLK_IS_STUCK   =  self._CLK_IS_STUCK( self,  Access.RW,  0x00004000,  14,  signed=False)
            self.PLL_LOCK_LOSS  =  self._PLL_LOCK_LOSS(self,  Access.RW,  0x00008000,  15,  signed=False)

    class _IHOLD_IRUN(Register):

        class _IHOLD(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IHOLD", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IRUN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IRUN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IHOLDDELAY(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IHOLDDELAY", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IRUNDELAY(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IRUNDELAY", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("IHOLD_IRUN", parent, access, address, signed)
            self.IHOLD       =  self._IHOLD(     self,  Access.RW,  0x000000FF,  0,   signed=False)
            self.IRUN        =  self._IRUN(      self,  Access.RW,  0x0000FF00,  8,   signed=False)
            self.IHOLDDELAY  =  self._IHOLDDELAY(self,  Access.RW,  0x00FF0000,  16,  signed=False)
            self.IRUNDELAY   =  self._IRUNDELAY( self,  Access.RW,  0x0F000000,  24,  signed=False)

    class _TPOWERDOWN(Register):

        class _TPOWERDOWN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TPOWERDOWN", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("TPOWERDOWN", parent, access, address, signed)
            self.TPOWERDOWN  =  self._TPOWERDOWN(self,  Access.RW,  0x000000FF,  0,  signed=False)

    class _TSTEP(Register):

        class _TSTEP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TSTEP", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("TSTEP", parent, access, address, signed)
            self.TSTEP  =  self._TSTEP(self,  Access.R,  0x000FFFFF,  0,  signed=False)

    class _TPWMTHRS(Register):

        class _TPWMTHRS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TPWMTHRS", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("TPWMTHRS", parent, access, address, signed)
            self.TPWMTHRS  =  self._TPWMTHRS(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

    class _TCOOLTHRS(Register):

        class _TCOOLTHRS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TCOOLTHRS", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("TCOOLTHRS", parent, access, address, signed)
            self.TCOOLTHRS  =  self._TCOOLTHRS(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

    class _THIGH(Register):

        class _THIGH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("THIGH", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("THIGH", parent, access, address, signed)
            self.THIGH  =  self._THIGH(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

    class _TSGP_LOW_VEL_THRS(Register):

        class _TSGP_LOW_VEL_THRS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TSGP_LOW_VEL_THRS", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("TSGP_LOW_VEL_THRS", parent, access, address, signed)
            self.TSGP_LOW_VEL_THRS  =  self._TSGP_LOW_VEL_THRS(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

    class _T_RCOIL_MEAS(Register):

        class _T_RCOIL_MEAS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("T_RCOIL_MEAS", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("T_RCOIL_MEAS", parent, access, address, signed)
            self.T_RCOIL_MEAS  =  self._T_RCOIL_MEAS(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

    class _TUDCSTEP(Register):

        class _TUDCSTEP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TUDCSTEP", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("TUDCSTEP", parent, access, address, signed)
            self.TUDCSTEP  =  self._TUDCSTEP(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

    class _UDC_CONF(Register):

        class _DECEL_THRS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DECEL_THRS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ACCEL_THRS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ACCEL_THRS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UDC_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UDC_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("UDC_CONF", parent, access, address, signed)
            self.DECEL_THRS  =  self._DECEL_THRS(self,  Access.RW,  0x0000000F,  0,  signed=False)
            self.ACCEL_THRS  =  self._ACCEL_THRS(self,  Access.RW,  0x000000F0,  4,  signed=False)
            self.UDC_ENABLE  =  self._UDC_ENABLE(self,  Access.RW,  0x00000100,  8,  signed=False)

    class _STEPS_LOST(Register):

        class _STEPS_LOST(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STEPS_LOST", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("STEPS_LOST", parent, access, address, signed)
            self.STEPS_LOST  =  self._STEPS_LOST(self,  Access.RW,  0x000FFFFF,  0,  signed=True)

    class _RAMPMODE(Register):

        class _RAMPMODE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPMODE", parent, access, mask, shift, signed=signed)

                self.choice : _RAMPMODE_RAMPMODE_FIELD_CHOICES = {
                    "POSITION": Option(0, self),
                    "VEL_POS": Option(1, self),
                    "VEL_NEG": Option(2, self),
                    "HOLD": Option(3, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("RAMPMODE", parent, access, address, signed)
            self.RAMPMODE  =  self._RAMPMODE(self,  Access.RW,  0x00000003,  0,  signed=False)

    class _XACTUAL(Register):

        class _XACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("XACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("XACTUAL", parent, access, address, signed)
            self.XACTUAL  =  self._XACTUAL(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _VACTUAL(Register):

        class _VACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("VACTUAL", parent, access, address, signed)
            self.VACTUAL  =  self._VACTUAL(self,  Access.R,  0x00FFFFFF,  0,  signed=True)

    class _VSTART(Register):

        class _VSTART(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VSTART", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("VSTART", parent, access, address, signed)
            self.VSTART  =  self._VSTART(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

    class _A1(Register):

        class _A1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("A1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("A1", parent, access, address, signed)
            self.A1  =  self._A1(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

    class _V1(Register):

        class _V1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("V1", parent, access, address, signed)
            self.V1  =  self._V1(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

    class _AMAX(Register):

        class _AMAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AMAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("AMAX", parent, access, address, signed)
            self.AMAX  =  self._AMAX(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

    class _VMAX(Register):

        class _VMAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VMAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("VMAX", parent, access, address, signed)
            self.VMAX  =  self._VMAX(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

    class _DMAX(Register):

        class _DMAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DMAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("DMAX", parent, access, address, signed)
            self.DMAX  =  self._DMAX(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

    class _TVMAX(Register):

        class _TVMAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TVMAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("TVMAX", parent, access, address, signed)
            self.TVMAX  =  self._TVMAX(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

    class _D1(Register):

        class _D1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("D1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("D1", parent, access, address, signed)
            self.D1  =  self._D1(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

    class _VSTOP(Register):

        class _VSTOP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VSTOP", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("VSTOP", parent, access, address, signed)
            self.VSTOP  =  self._VSTOP(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

    class _TZEROWAIT(Register):

        class _TZEROWAIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TZEROWAIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("TZEROWAIT", parent, access, address, signed)
            self.TZEROWAIT  =  self._TZEROWAIT(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

    class _XTARGET(Register):

        class _XTARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("XTARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("XTARGET", parent, access, address, signed)
            self.XTARGET  =  self._XTARGET(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _V2(Register):

        class _V2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("V2", parent, access, address, signed)
            self.V2  =  self._V2(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

    class _A2(Register):

        class _A2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("A2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("A2", parent, access, address, signed)
            self.A2  =  self._A2(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

    class _D2(Register):

        class _D2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("D2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("D2", parent, access, address, signed)
            self.D2  =  self._D2(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

    class _AACTUAL(Register):

        class _AACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("AACTUAL", parent, access, address, signed)
            self.AACTUAL  =  self._AACTUAL(self,  Access.R,  0x00FFFFFF,  0,  signed=True)

    class _SW_MODE(Register):

        class _STOP_L_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_L_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice : _SW_MODE_STOP_L_ENABLE_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "REFL enabled": Option(True, self),
                }

        class _STOP_R_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_R_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice : _SW_MODE_STOP_R_ENABLE_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "REFR enabled": Option(True, self),
                }

        class _POL_STOP_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POL_STOP_L", parent, access, mask, shift, signed=signed)

                self.choice : _SW_MODE_POL_STOP_L_FIELD_CHOICES = {
                    "high active": Option(False, self),
                    "low active": Option(True, self),
                }

        class _POL_STOP_R(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POL_STOP_R", parent, access, mask, shift, signed=signed)

                self.choice : _SW_MODE_POL_STOP_R_FIELD_CHOICES = {
                    "high active": Option(False, self),
                    "low active": Option(True, self),
                }

        class _SWAP_LR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SWAP_LR", parent, access, mask, shift, signed=signed)

                self.choice : _SW_MODE_SWAP_LR_FIELD_CHOICES = {
                    "normal order": Option(False, self),
                    "left and right switch swapped": Option(True, self),
                }

        class _LATCH_L_ACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_L_ACTIVE", parent, access, mask, shift, signed=signed)

                self.choice : _SW_MODE_LATCH_L_ACTIVE_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "latch on active going edge": Option(True, self),
                }

        class _LATCH_L_INACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_L_INACTIVE", parent, access, mask, shift, signed=signed)

                self.choice : _SW_MODE_LATCH_L_INACTIVE_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "latch on inactive going edge": Option(True, self),
                }

        class _LATCH_R_ACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_R_ACTIVE", parent, access, mask, shift, signed=signed)

                self.choice : _SW_MODE_LATCH_R_ACTIVE_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "latch on active going edge": Option(True, self),
                }

        class _LATCH_R_INACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_R_INACTIVE", parent, access, mask, shift, signed=signed)

                self.choice : _SW_MODE_LATCH_R_INACTIVE_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "latch on inactive going edge": Option(True, self),
                }

        class _EN_LATCH_ENCODER(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EN_LATCH_ENCODER", parent, access, mask, shift, signed=signed)

                self.choice : _SW_MODE_EN_LATCH_ENCODER_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "latch encoder position to ENC_LATCH": Option(True, self),
                }

        class _SG_STOP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SG_STOP", parent, access, mask, shift, signed=signed)

                self.choice : _SW_MODE_SG_STOP_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "stop on stall": Option(True, self),
                }

        class _EN_SOFTSTOP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EN_SOFTSTOP", parent, access, mask, shift, signed=signed)

                self.choice : _SW_MODE_EN_SOFTSTOP_FIELD_CHOICES = {
                    "hardstop": Option(False, self),
                    "softstop": Option(True, self),
                }

        class _EN_VIRTUAL_STOP_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EN_VIRTUAL_STOP_L", parent, access, mask, shift, signed=signed)

                self.choice : _SW_MODE_EN_VIRTUAL_STOP_L_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "enabled": Option(True, self),
                }

        class _EN_VIRTUAL_STOP_R(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EN_VIRTUAL_STOP_R", parent, access, mask, shift, signed=signed)

                self.choice : _SW_MODE_EN_VIRTUAL_STOP_R_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "enabled": Option(True, self),
                }

        class _VIRTUAL_STOP_ENC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VIRTUAL_STOP_ENC", parent, access, mask, shift, signed=signed)

                self.choice : _SW_MODE_VIRTUAL_STOP_ENC_FIELD_CHOICES = {
                    "XACTUAL": Option(False, self),
                    "X_ENC": Option(True, self),
                }

        class _HARD_STOP_CLR_CUR_INT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HARD_STOP_CLR_CUR_INT", parent, access, mask, shift, signed=signed)

                self.choice : _SW_MODE_HARD_STOP_CLR_CUR_INT_FIELD_CHOICES = {
                    "Keep integrator": Option(False, self),
                    "Clear integrator (recommended)": Option(True, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("SW_MODE", parent, access, address, signed)
            self.STOP_L_ENABLE          =  self._STOP_L_ENABLE(        self,  Access.RW,  0x00000001,  0,   signed=False)
            self.STOP_R_ENABLE          =  self._STOP_R_ENABLE(        self,  Access.RW,  0x00000002,  1,   signed=False)
            self.POL_STOP_L             =  self._POL_STOP_L(           self,  Access.RW,  0x00000004,  2,   signed=False)
            self.POL_STOP_R             =  self._POL_STOP_R(           self,  Access.RW,  0x00000008,  3,   signed=False)
            self.SWAP_LR                =  self._SWAP_LR(              self,  Access.RW,  0x00000010,  4,   signed=False)
            self.LATCH_L_ACTIVE         =  self._LATCH_L_ACTIVE(       self,  Access.RW,  0x00000020,  5,   signed=False)
            self.LATCH_L_INACTIVE       =  self._LATCH_L_INACTIVE(     self,  Access.RW,  0x00000040,  6,   signed=False)
            self.LATCH_R_ACTIVE         =  self._LATCH_R_ACTIVE(       self,  Access.RW,  0x00000080,  7,   signed=False)
            self.LATCH_R_INACTIVE       =  self._LATCH_R_INACTIVE(     self,  Access.RW,  0x00000100,  8,   signed=False)
            self.EN_LATCH_ENCODER       =  self._EN_LATCH_ENCODER(     self,  Access.RW,  0x00000200,  9,   signed=False)
            self.SG_STOP                =  self._SG_STOP(              self,  Access.RW,  0x00000400,  10,  signed=False)
            self.EN_SOFTSTOP            =  self._EN_SOFTSTOP(          self,  Access.RW,  0x00000800,  11,  signed=False)
            self.EN_VIRTUAL_STOP_L      =  self._EN_VIRTUAL_STOP_L(    self,  Access.RW,  0x00001000,  12,  signed=False)
            self.EN_VIRTUAL_STOP_R      =  self._EN_VIRTUAL_STOP_R(    self,  Access.RW,  0x00002000,  13,  signed=False)
            self.VIRTUAL_STOP_ENC       =  self._VIRTUAL_STOP_ENC(     self,  Access.RW,  0x00004000,  14,  signed=False)
            self.HARD_STOP_CLR_CUR_INT  =  self._HARD_STOP_CLR_CUR_INT(self,  Access.RW,  0x00008000,  15,  signed=False)

    class _RAMP_STAT(Register):

        class _STATUS_STOP_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_STOP_L", parent, access, mask, shift, signed=signed)

                self.choice : _RAMP_STAT_STATUS_STOP_L_FIELD_CHOICES = {
                    "inactive": Option(False, self),
                    "active": Option(True, self),
                }

        class _STATUS_STOP_R(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_STOP_R", parent, access, mask, shift, signed=signed)

                self.choice : _RAMP_STAT_STATUS_STOP_R_FIELD_CHOICES = {
                    "inactive": Option(False, self),
                    "active": Option(True, self),
                }

        class _STATUS_LATCH_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_LATCH_L", parent, access, mask, shift, signed=signed)

                self.choice : _RAMP_STAT_STATUS_LATCH_L_FIELD_CHOICES = {
                    "no event": Option(False, self),
                    "position latched": Option(True, self),
                }

        class _STATUS_LATCH_R(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_LATCH_R", parent, access, mask, shift, signed=signed)

                self.choice : _RAMP_STAT_STATUS_LATCH_R_FIELD_CHOICES = {
                    "no event": Option(False, self),
                    "position latched": Option(True, self),
                }

        class _EVENT_STOP_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EVENT_STOP_L", parent, access, mask, shift, signed=signed)

                self.choice : _RAMP_STAT_EVENT_STOP_L_FIELD_CHOICES = {
                    "inactive": Option(False, self),
                    "active": Option(True, self),
                }

        class _EVENT_STOP_R(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EVENT_STOP_R", parent, access, mask, shift, signed=signed)

                self.choice : _RAMP_STAT_EVENT_STOP_R_FIELD_CHOICES = {
                    "inactive": Option(False, self),
                    "active": Option(True, self),
                }

        class _EVENT_STOP_SG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EVENT_STOP_SG", parent, access, mask, shift, signed=signed)

                self.choice : _RAMP_STAT_EVENT_STOP_SG_FIELD_CHOICES = {
                    "inactive": Option(False, self),
                    "active": Option(True, self),
                }

        class _EVENT_POS_REACHED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EVENT_POS_REACHED", parent, access, mask, shift, signed=signed)

                self.choice : _RAMP_STAT_EVENT_POS_REACHED_FIELD_CHOICES = {
                    "inactive": Option(False, self),
                    "active": Option(True, self),
                }

        class _VELOCITY_REACHED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_REACHED", parent, access, mask, shift, signed=signed)

                self.choice : _RAMP_STAT_VELOCITY_REACHED_FIELD_CHOICES = {
                    "+/-VMAX not reached": Option(False, self),
                    "+/-VMAX reached": Option(True, self),
                }

        class _POSITION_REACHED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_REACHED", parent, access, mask, shift, signed=signed)

                self.choice : _RAMP_STAT_POSITION_REACHED_FIELD_CHOICES = {
                    "Target not reached": Option(False, self),
                    "Target reached and stopped": Option(True, self),
                }

        class _VZERO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VZERO", parent, access, mask, shift, signed=signed)

                self.choice : _RAMP_STAT_VZERO_FIELD_CHOICES = {
                    "moving with VACTUAL": Option(False, self),
                    "velocity is 0": Option(True, self),
                }

        class _T_ZEROWAIT_ACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("T_ZEROWAIT_ACTIVE", parent, access, mask, shift, signed=signed)

                self.choice : _RAMP_STAT_T_ZEROWAIT_ACTIVE_FIELD_CHOICES = {
                    "inactive": Option(False, self),
                    "Motion controller in TZEROWAIT time.": Option(True, self),
                }

        class _SECOND_MOVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SECOND_MOVE", parent, access, mask, shift, signed=signed)

                self.choice : _RAMP_STAT_SECOND_MOVE_FIELD_CHOICES = {
                    "normal motion": Option(False, self),
                    "direction was changed to reach target position": Option(True, self),
                }

        class _STATUS_SG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_SG", parent, access, mask, shift, signed=signed)

                self.choice : _RAMP_STAT_STATUS_SG_FIELD_CHOICES = {
                    "momentary inactive": Option(False, self),
                    "momentary active": Option(True, self),
                }

        class _STATUS_VIRTUAL_STOP_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_VIRTUAL_STOP_L", parent, access, mask, shift, signed=signed)

                self.choice : _RAMP_STAT_STATUS_VIRTUAL_STOP_L_FIELD_CHOICES = {
                    "inactive": Option(False, self),
                    "active": Option(True, self),
                }

        class _STATUS_VIRTUAL_STOP_R(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_VIRTUAL_STOP_R", parent, access, mask, shift, signed=signed)

                self.choice : _RAMP_STAT_STATUS_VIRTUAL_STOP_R_FIELD_CHOICES = {
                    "0": Option(False, self),
                    "1": Option(True, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("RAMP_STAT", parent, access, address, signed)
            self.STATUS_STOP_L          =  self._STATUS_STOP_L(        self,  Access.R,    0x00000001,  0,   signed=False)
            self.STATUS_STOP_R          =  self._STATUS_STOP_R(        self,  Access.R,    0x00000002,  1,   signed=False)
            self.STATUS_LATCH_L         =  self._STATUS_LATCH_L(       self,  Access.RWC,  0x00000004,  2,   signed=False)
            self.STATUS_LATCH_R         =  self._STATUS_LATCH_R(       self,  Access.RWC,  0x00000008,  3,   signed=False)
            self.EVENT_STOP_L           =  self._EVENT_STOP_L(         self,  Access.R,    0x00000010,  4,   signed=False)
            self.EVENT_STOP_R           =  self._EVENT_STOP_R(         self,  Access.R,    0x00000020,  5,   signed=False)
            self.EVENT_STOP_SG          =  self._EVENT_STOP_SG(        self,  Access.RWC,  0x00000040,  6,   signed=False)
            self.EVENT_POS_REACHED      =  self._EVENT_POS_REACHED(    self,  Access.RWC,  0x00000080,  7,   signed=False)
            self.VELOCITY_REACHED       =  self._VELOCITY_REACHED(     self,  Access.R,    0x00000100,  8,   signed=False)
            self.POSITION_REACHED       =  self._POSITION_REACHED(     self,  Access.R,    0x00000200,  9,   signed=False)
            self.VZERO                  =  self._VZERO(                self,  Access.R,    0x00000400,  10,  signed=False)
            self.T_ZEROWAIT_ACTIVE      =  self._T_ZEROWAIT_ACTIVE(    self,  Access.R,    0x00000800,  11,  signed=False)
            self.SECOND_MOVE            =  self._SECOND_MOVE(          self,  Access.RWC,  0x00001000,  12,  signed=False)
            self.STATUS_SG              =  self._STATUS_SG(            self,  Access.R,    0x00002000,  13,  signed=False)
            self.STATUS_VIRTUAL_STOP_L  =  self._STATUS_VIRTUAL_STOP_L(self,  Access.R,    0x00004000,  14,  signed=False)
            self.STATUS_VIRTUAL_STOP_R  =  self._STATUS_VIRTUAL_STOP_R(self,  Access.R,    0x00008000,  15,  signed=False)

    class _XLATCH(Register):

        class _XLATCH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("XLATCH", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("XLATCH", parent, access, address, signed)
            self.XLATCH  =  self._XLATCH(self,  Access.R,  0xFFFFFFFF,  0,  signed=False)

    class _ENCMODE(Register):

        class _POL_A(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POL_A", parent, access, mask, shift, signed=signed)

                self.choice : _ENCMODE_POL_A_FIELD_CHOICES = {
                    "neg": Option(False, self),
                    "pos": Option(True, self),
                }

        class _POL_B(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POL_B", parent, access, mask, shift, signed=signed)

                self.choice : _ENCMODE_POL_B_FIELD_CHOICES = {
                    "neg": Option(False, self),
                    "pos": Option(True, self),
                }

        class _POL_N(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POL_N", parent, access, mask, shift, signed=signed)

                self.choice : _ENCMODE_POL_N_FIELD_CHOICES = {
                    "low active": Option(False, self),
                    "high active": Option(True, self),
                }

        class _IGNORE_AB(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IGNORE_AB", parent, access, mask, shift, signed=signed)

                self.choice : _ENCMODE_IGNORE_AB_FIELD_CHOICES = {
                    "N event when POL_A, POL_B, POL_N match": Option(False, self),
                    "ignore POL_A and POL_B for N event": Option(True, self),
                }

        class _CLR_CONT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLR_CONT", parent, access, mask, shift, signed=signed)

                self.choice : _ENCMODE_CLR_CONT_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "Always latch or latch and clear X_ENC upon an N event": Option(True, self),
                }

        class _CLR_ONCE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLR_ONCE", parent, access, mask, shift, signed=signed)

                self.choice : _ENCMODE_CLR_ONCE_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "Latch or latch and clear X_ENC on the next N event after setting this bit.": Option(True, self),
                }

        class _POS_NEG_EDGE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POS_NEG_EDGE", parent, access, mask, shift, signed=signed)

                self.choice : _ENCMODE_POS_NEG_EDGE_FIELD_CHOICES = {
                    "N channel event is active during active N event level": Option(0, self),
                    "N channel is valid upon active going N event": Option(1, self),
                    "N channel is valid upon inactive going N event": Option(2, self),
                    "N channel is valid upon active and inactive going N event": Option(3, self),
                }

        class _CLR_ENC_X(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLR_ENC_X", parent, access, mask, shift, signed=signed)

                self.choice : _ENCMODE_CLR_ENC_X_FIELD_CHOICES = {
                    "Upon N event, X_ENC becomes latched to ENC_LATCH only": Option(False, self),
                    "Latch and additionally clear encoder counter X_ENC at N-event": Option(True, self),
                }

        class _LATCH_X_ACT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_X_ACT", parent, access, mask, shift, signed=signed)

                self.choice : _ENCMODE_LATCH_X_ACT_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "Latch XACTUAL together with X_ENC upon N channel event": Option(True, self),
                }

        class _ENC_SEL_DECIMAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_SEL_DECIMAL", parent, access, mask, shift, signed=signed)

                self.choice : _ENCMODE_ENC_SEL_DECIMAL_FIELD_CHOICES = {
                    "binary": Option(False, self),
                    "decimal": Option(True, self),
                }

        class _NBEMF_ABN_SEL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("NBEMF_ABN_SEL", parent, access, mask, shift, signed=signed)

                self.choice : _ENCMODE_NBEMF_ABN_SEL_FIELD_CHOICES = {
                    "Tricoder": Option(False, self),
                    "ABN-Interface": Option(True, self),
                }

        class _BEMF_HYST(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BEMF_HYST", parent, access, mask, shift, signed=signed)

                self.choice : _ENCMODE_BEMF_HYST_FIELD_CHOICES = {
                    "10 mV": Option(0, self),
                    "25 mV": Option(1, self),
                    "50 mV": Option(2, self),
                    "75 mV": Option(3, self),
                    "100 mV": Option(4, self),
                    "150 mV": Option(5, self),
                    "200 mV": Option(6, self),
                    "250 mV": Option(7, self),
                }

        class _BEMF_BLANK_TIME(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BEMF_BLANK_TIME", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BEMF_FILTER_SEL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BEMF_FILTER_SEL", parent, access, mask, shift, signed=signed)

                self.choice : _ENCMODE_BEMF_FILTER_SEL_FIELD_CHOICES = {
                    "0.5 kHz": Option(0, self),
                    "1 kHz": Option(1, self),
                    "2 kHz": Option(2, self),
                    "4.3 kHz": Option(3, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("ENCMODE", parent, access, address, signed)
            self.POL_A            =  self._POL_A(          self,  Access.RW,  0x00000001,  0,   signed=False)
            self.POL_B            =  self._POL_B(          self,  Access.RW,  0x00000002,  1,   signed=False)
            self.POL_N            =  self._POL_N(          self,  Access.RW,  0x00000004,  2,   signed=False)
            self.IGNORE_AB        =  self._IGNORE_AB(      self,  Access.RW,  0x00000008,  3,   signed=False)
            self.CLR_CONT         =  self._CLR_CONT(       self,  Access.RW,  0x00000010,  4,   signed=False)
            self.CLR_ONCE         =  self._CLR_ONCE(       self,  Access.RW,  0x00000020,  5,   signed=False)
            self.POS_NEG_EDGE     =  self._POS_NEG_EDGE(   self,  Access.RW,  0x000000C0,  6,   signed=False)
            self.CLR_ENC_X        =  self._CLR_ENC_X(      self,  Access.RW,  0x00000100,  8,   signed=False)
            self.LATCH_X_ACT      =  self._LATCH_X_ACT(    self,  Access.RW,  0x00000200,  9,   signed=False)
            self.ENC_SEL_DECIMAL  =  self._ENC_SEL_DECIMAL(self,  Access.RW,  0x00000400,  10,  signed=False)
            self.NBEMF_ABN_SEL    =  self._NBEMF_ABN_SEL(  self,  Access.RW,  0x00000800,  11,  signed=False)
            self.BEMF_HYST        =  self._BEMF_HYST(      self,  Access.RW,  0x00007000,  12,  signed=False)
            self.BEMF_BLANK_TIME  =  self._BEMF_BLANK_TIME(self,  Access.RW,  0x00FF0000,  16,  signed=False)
            self.BEMF_FILTER_SEL  =  self._BEMF_FILTER_SEL(self,  Access.RW,  0x30000000,  28,  signed=False)

    class _X_ENC(Register):

        class _X_ENC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("X_ENC", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("X_ENC", parent, access, address, signed)
            self.X_ENC  =  self._X_ENC(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _ENC_CONST(Register):

        class _ENC_CONST(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_CONST", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ENC_CONST", parent, access, address, signed)
            self.ENC_CONST  =  self._ENC_CONST(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _ENC_STATUS(Register):

        class _N_EVENT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("N_EVENT", parent, access, mask, shift, signed=signed)

                self.choice : _ENC_STATUS_N_EVENT_FIELD_CHOICES = {
                    "No event": Option(False, self),
                    "N event detected": Option(True, self),
                }

        class _DEVIATION_WARN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DEVIATION_WARN", parent, access, mask, shift, signed=signed)

                self.choice : _ENC_STATUS_DEVIATION_WARN_FIELD_CHOICES = {
                    "no warning": Option(False, self),
                    "ENC_DEVIATION reached": Option(True, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("ENC_STATUS", parent, access, address, signed)
            self.N_EVENT         =  self._N_EVENT(       self,  Access.RWC,  0x00000001,  0,  signed=False)
            self.DEVIATION_WARN  =  self._DEVIATION_WARN(self,  Access.RWC,  0x00000002,  1,  signed=False)

    class _ENC_LATCH(Register):

        class _ENC_LATCH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_LATCH", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ENC_LATCH", parent, access, address, signed)
            self.ENC_LATCH  =  self._ENC_LATCH(self,  Access.R,  0xFFFFFFFF,  0,  signed=False)

    class _ENC_DEVIATION(Register):

        class _ENC_DEVIATION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_DEVIATION", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ENC_DEVIATION", parent, access, address, signed)
            self.ENC_DEVIATION  =  self._ENC_DEVIATION(self,  Access.R,  0x000FFFFF,  0,  signed=False)

    class _VIRTUAL_STOP_L(Register):

        class _VIRTUAL_STOP_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VIRTUAL_STOP_L", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("VIRTUAL_STOP_L", parent, access, address, signed)
            self.VIRTUAL_STOP_L  =  self._VIRTUAL_STOP_L(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _VIRTUAL_STOP_R(Register):

        class _VIRTUAL_STOP_R(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VIRTUAL_STOP_R", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("VIRTUAL_STOP_R", parent, access, address, signed)
            self.VIRTUAL_STOP_R  =  self._VIRTUAL_STOP_R(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _CURRENT_PI_REG(Register):

        class _CUR_P(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_P", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CUR_I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_I", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("CURRENT_PI_REG", parent, access, address, signed)
            self.CUR_P  =  self._CUR_P(self,  Access.RW,  0x00000FFF,  0,   signed=False)
            self.CUR_I  =  self._CUR_I(self,  Access.RW,  0x03FF0000,  16,  signed=False)

    class _ANGLE_PI_REG(Register):

        class _ANGLE_P(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_P", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ANGLE_I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_I", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ANGLE_PI_REG", parent, access, address, signed)
            self.ANGLE_P  =  self._ANGLE_P(self,  Access.RW,  0x00000FFF,  0,   signed=False)
            self.ANGLE_I  =  self._ANGLE_I(self,  Access.RW,  0x03FF0000,  16,  signed=False)

    class _CUR_ANGLE_LIMIT(Register):

        class _ANGLE_PI_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_PI_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ANGLE_PI_INT_POS_CLIP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_PI_INT_POS_CLIP", parent, access, mask, shift, signed=signed)

                self.choice : _CUR_ANGLE_LIMIT_ANGLE_PI_INT_POS_CLIP_FIELD_CHOICES = {
                    "Normal operation": Option(False, self),
                    "Integrator reached Angle Limit": Option(True, self),
                }

        class _ANGLE_PI_INT_NEG_CLIP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_PI_INT_NEG_CLIP", parent, access, mask, shift, signed=signed)

                self.choice : _CUR_ANGLE_LIMIT_ANGLE_PI_INT_NEG_CLIP_FIELD_CHOICES = {
                    "Normal operation": Option(False, self),
                    "Integrator reached -Angle Limit": Option(True, self),
                }

        class _ANGLE_PI_POS_CLIP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_PI_POS_CLIP", parent, access, mask, shift, signed=signed)

                self.choice : _CUR_ANGLE_LIMIT_ANGLE_PI_POS_CLIP_FIELD_CHOICES = {
                    "Normal operation": Option(False, self),
                    "Angle Limit reached": Option(True, self),
                }

        class _ANGLE_PI_NEG_CLIP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_PI_NEG_CLIP", parent, access, mask, shift, signed=signed)

                self.choice : _CUR_ANGLE_LIMIT_ANGLE_PI_NEG_CLIP_FIELD_CHOICES = {
                    "Normal operation": Option(False, self),
                    "-Angle Limit reached": Option(True, self),
                }

        class _CUR_PI_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_PI_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CUR_PI_INT_POS_CLIP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_PI_INT_POS_CLIP", parent, access, mask, shift, signed=signed)

                self.choice : _CUR_ANGLE_LIMIT_CUR_PI_INT_POS_CLIP_FIELD_CHOICES = {
                    "Normal operation": Option(False, self),
                    "Integrator reached CUR_PI_LIMIT": Option(True, self),
                }

        class _CUR_PI_INT_NEG_CLIP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_PI_INT_NEG_CLIP", parent, access, mask, shift, signed=signed)

                self.choice : _CUR_ANGLE_LIMIT_CUR_PI_INT_NEG_CLIP_FIELD_CHOICES = {
                    "Normal operation": Option(False, self),
                    "Integrator reached 0": Option(True, self),
                }

        class _CUR_PI_POS_CLIP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_PI_POS_CLIP", parent, access, mask, shift, signed=signed)

                self.choice : _CUR_ANGLE_LIMIT_CUR_PI_POS_CLIP_FIELD_CHOICES = {
                    "Normal operation": Option(False, self),
                    "CUR_PI_LIMIT reached": Option(True, self),
                }

        class _CUR_PI_NEG_CLIP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_PI_NEG_CLIP", parent, access, mask, shift, signed=signed)

                self.choice : _CUR_ANGLE_LIMIT_CUR_PI_NEG_CLIP_FIELD_CHOICES = {
                    "Normal operation": Option(False, self),
                    "0 reached": Option(True, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("CUR_ANGLE_LIMIT", parent, access, address, signed)
            self.ANGLE_PI_LIMIT         =  self._ANGLE_PI_LIMIT(       self,  Access.RW,  0x000003FF,  0,   signed=False)
            self.ANGLE_PI_INT_POS_CLIP  =  self._ANGLE_PI_INT_POS_CLIP(self,  Access.R,   0x00001000,  12,  signed=False)
            self.ANGLE_PI_INT_NEG_CLIP  =  self._ANGLE_PI_INT_NEG_CLIP(self,  Access.R,   0x00002000,  13,  signed=False)
            self.ANGLE_PI_POS_CLIP      =  self._ANGLE_PI_POS_CLIP(    self,  Access.R,   0x00004000,  14,  signed=False)
            self.ANGLE_PI_NEG_CLIP      =  self._ANGLE_PI_NEG_CLIP(    self,  Access.R,   0x00008000,  15,  signed=False)
            self.CUR_PI_LIMIT           =  self._CUR_PI_LIMIT(         self,  Access.RW,  0x0FFF0000,  16,  signed=False)
            self.CUR_PI_INT_POS_CLIP    =  self._CUR_PI_INT_POS_CLIP(  self,  Access.R,   0x10000000,  28,  signed=False)
            self.CUR_PI_INT_NEG_CLIP    =  self._CUR_PI_INT_NEG_CLIP(  self,  Access.R,   0x20000000,  29,  signed=False)
            self.CUR_PI_POS_CLIP        =  self._CUR_PI_POS_CLIP(      self,  Access.R,   0x40000000,  30,  signed=False)
            self.CUR_PI_NEG_CLIP        =  self._CUR_PI_NEG_CLIP(      self,  Access.R,   0x80000000,  31,  signed=False)

    class _ANGLE_LOWER_LIMIT(Register):

        class _ANGLE_LOWER_I_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_LOWER_I_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ANGLE_ERROR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_ERROR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ANGLE_LOWER_LIMIT", parent, access, address, signed)
            self.ANGLE_LOWER_I_LIMIT  =  self._ANGLE_LOWER_I_LIMIT(self,  Access.RW,  0x000003FF,  0,   signed=False)
            self.ANGLE_ERROR          =  self._ANGLE_ERROR(        self,  Access.R,   0x03FF0000,  16,  signed=True)

    class _CUR_ANGLE_MEAS(Register):

        class _AMPL_MEAS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AMPL_MEAS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ANGLE_MEAS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_MEAS", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("CUR_ANGLE_MEAS", parent, access, address, signed)
            self.AMPL_MEAS   =  self._AMPL_MEAS( self,  Access.R,  0x00000FFF,  0,   signed=False)
            self.ANGLE_MEAS  =  self._ANGLE_MEAS(self,  Access.R,  0x03FF0000,  16,  signed=False)

    class _PI_RESULTS(Register):

        class _PWM_CALC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_CALC", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ANGLE_CORR_CALC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_CORR_CALC", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PI_RESULTS", parent, access, address, signed)
            self.PWM_CALC         =  self._PWM_CALC(       self,  Access.R,  0x00001FFF,  0,   signed=True)
            self.ANGLE_CORR_CALC  =  self._ANGLE_CORR_CALC(self,  Access.R,  0x03FF0000,  16,  signed=True)

    class _COIL_INDUCT(Register):

        class _COIL_INDUCT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COIL_INDUCT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _RCOIL_MANUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RCOIL_MANUAL", parent, access, mask, shift, signed=signed)

                self.choice : _COIL_INDUCT_RCOIL_MANUAL_FIELD_CHOICES = {
                    "Automatic resistance measurement: R_COIL_AUTO_A/B": Option(False, self),
                    "User defined value: R_COIL_USER_A/B": Option(True, self),
                }

        class _RCOIL_THERMAL_COUPLING(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RCOIL_THERMAL_COUPLING", parent, access, mask, shift, signed=signed)

                self.choice : _COIL_INDUCT_RCOIL_THERMAL_COUPLING_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "thermal coupling enabled": Option(True, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("COIL_INDUCT", parent, access, address, signed)
            self.COIL_INDUCT             =  self._COIL_INDUCT(           self,  Access.RW,  0x00007FFF,  0,   signed=False)
            self.RCOIL_MANUAL            =  self._RCOIL_MANUAL(          self,  Access.RW,  0x00010000,  16,  signed=False)
            self.RCOIL_THERMAL_COUPLING  =  self._RCOIL_THERMAL_COUPLING(self,  Access.RW,  0x00020000,  17,  signed=False)

    class _R_COIL(Register):

        class _R_COIL_AUTO_B(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("R_COIL_AUTO_B", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _R_COIL_AUTO_A(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("R_COIL_AUTO_A", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("R_COIL", parent, access, address, signed)
            self.R_COIL_AUTO_B  =  self._R_COIL_AUTO_B(self,  Access.R,  0x00000FFF,  0,   signed=False)
            self.R_COIL_AUTO_A  =  self._R_COIL_AUTO_A(self,  Access.R,  0x0FFF0000,  16,  signed=False)

    class _R_COIL_USER(Register):

        class _R_COIL_USER_B(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("R_COIL_USER_B", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _R_COIL_USER_A(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("R_COIL_USER_A", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("R_COIL_USER", parent, access, address, signed)
            self.R_COIL_USER_B  =  self._R_COIL_USER_B(self,  Access.RW,  0x00000FFF,  0,   signed=False)
            self.R_COIL_USER_A  =  self._R_COIL_USER_A(self,  Access.RW,  0x0FFF0000,  16,  signed=False)

    class _SGP_CONF(Register):

        class _SGP_THRS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_THRS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SGP_FILT_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_FILT_EN", parent, access, mask, shift, signed=signed)

                self.choice : _SGP_CONF_SGP_FILT_EN_FIELD_CHOICES = {
                    "filter disabled": Option(False, self),
                    "filter enabled": Option(True, self),
                }

        class _SGP_LOW_VEL_FREEZE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_LOW_VEL_FREEZE", parent, access, mask, shift, signed=signed)

                self.choice : _SGP_CONF_SGP_LOW_VEL_FREEZE_FIELD_CHOICES = {
                    "clear": Option(False, self),
                    "freeze": Option(True, self),
                }

        class _SGP_CLEAR_CUR_PI(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_CLEAR_CUR_PI", parent, access, mask, shift, signed=signed)

                self.choice : _SGP_CONF_SGP_CLEAR_CUR_PI_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "enabled": Option(True, self),
                }

        class _SGP_LOW_VEL_SLOPE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_LOW_VEL_SLOPE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SGP_LOW_VEL_CNTS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_LOW_VEL_CNTS", parent, access, mask, shift, signed=signed)

                self.choice : _SGP_CONF_SGP_LOW_VEL_CNTS_FIELD_CHOICES = {
                    "1 event": Option(0, self),
                    "2 events": Option(1, self),
                    "3 events": Option(2, self),
                    "4 events": Option(3, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("SGP_CONF", parent, access, address, signed)
            self.SGP_THRS            =  self._SGP_THRS(          self,  Access.RW,  0x000001FF,  0,   signed=True)
            self.SGP_FILT_EN         =  self._SGP_FILT_EN(       self,  Access.RW,  0x00001000,  12,  signed=False)
            self.SGP_LOW_VEL_FREEZE  =  self._SGP_LOW_VEL_FREEZE(self,  Access.RW,  0x00002000,  13,  signed=False)
            self.SGP_CLEAR_CUR_PI    =  self._SGP_CLEAR_CUR_PI(  self,  Access.RW,  0x00004000,  14,  signed=False)
            self.SGP_LOW_VEL_SLOPE   =  self._SGP_LOW_VEL_SLOPE( self,  Access.RW,  0x00FF0000,  16,  signed=False)
            self.SGP_LOW_VEL_CNTS    =  self._SGP_LOW_VEL_CNTS(  self,  Access.RW,  0x30000000,  28,  signed=False)

    class _SGP_IND_2_3(Register):

        class _SGP_IND_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_IND_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SGP_IND_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_IND_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("SGP_IND_2_3", parent, access, address, signed)
            self.SGP_IND_2  =  self._SGP_IND_2(self,  Access.R,  0x000003FF,  0,   signed=True)
            self.SGP_IND_3  =  self._SGP_IND_3(self,  Access.R,  0x03FF0000,  16,  signed=True)

    class _SGP_IND_0_1(Register):

        class _SGP_IND_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_IND_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SGP_IND_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_IND_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("SGP_IND_0_1", parent, access, address, signed)
            self.SGP_IND_0  =  self._SGP_IND_0(self,  Access.R,  0x000003FF,  0,   signed=True)
            self.SGP_IND_1  =  self._SGP_IND_1(self,  Access.R,  0x03FF0000,  16,  signed=True)

    class _INDUCTANCE_VOLTAGE(Register):

        class _UL_B(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UL_B", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UL_A(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UL_A", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("INDUCTANCE_VOLTAGE", parent, access, address, signed)
            self.UL_B  =  self._UL_B(self,  Access.R,  0x00000FFF,  0,   signed=True)
            self.UL_A  =  self._UL_A(self,  Access.R,  0x0FFF0000,  16,  signed=True)

    class _SGP_BEMF(Register):

        class _SGP_RAW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UBEMF_ABS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UBEMF_ABS", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("SGP_BEMF", parent, access, address, signed)
            self.SGP_RAW    =  self._SGP_RAW(  self,  Access.R,  0x000003FF,  0,   signed=True)
            self.UBEMF_ABS  =  self._UBEMF_ABS(self,  Access.R,  0x0FFF0000,  16,  signed=False)

    class _COOLSTEPPLUS_CONF(Register):

        class _COOL_CUR_DIV(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COOL_CUR_DIV", parent, access, mask, shift, signed=signed)

                self.choice : _COOLSTEPPLUS_CONF_COOL_CUR_DIV_FIELD_CHOICES = {
                    "Off": Option(0, self),
                    "Off, uses PI_OFF_SPEED for current increment to full current": Option(1, self),
                    "1/2 IRUN": Option(2, self),
                    "1/3 IRUN": Option(3, self),
                    "1/4 IRUN": Option(4, self),
                    "1/5 IRUN": Option(5, self),
                    "1/6 IRUN": Option(6, self),
                    "1/7 IRUN": Option(7, self),
                    "1/8 IRUN": Option(8, self),
                    "1/9 IRUN": Option(9, self),
                    "1/10 IRUN": Option(10, self),
                }

        class _LOAD_FILT_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LOAD_FILT_EN", parent, access, mask, shift, signed=signed)

                self.choice : _COOLSTEPPLUS_CONF_LOAD_FILT_EN_FIELD_CHOICES = {
                    "0": Option(False, self),
                    "1": Option(True, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("COOLSTEPPLUS_CONF", parent, access, address, signed)
            self.COOL_CUR_DIV  =  self._COOL_CUR_DIV(self,  Access.RW,  0x0000000F,  0,  signed=False)
            self.LOAD_FILT_EN  =  self._LOAD_FILT_EN(self,  Access.RW,  0x00000010,  4,  signed=False)

    class _COOLSTEPPLUS_PI_REG(Register):

        class _COOLSTEP_P(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COOLSTEP_P", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COOLSTEP_I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COOLSTEP_I", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("COOLSTEPPLUS_PI_REG", parent, access, address, signed)
            self.COOLSTEP_P  =  self._COOLSTEP_P(self,  Access.RW,  0x00000FFF,  0,   signed=False)
            self.COOLSTEP_I  =  self._COOLSTEP_I(self,  Access.RW,  0x03FF0000,  16,  signed=False)

    class _COOLSTEPPLUS_PI_DOWN(Register):

        class _COOL_PI_DOWN_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COOL_PI_DOWN_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COOL_PI_OFF_SPEED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COOL_PI_OFF_SPEED", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("COOLSTEPPLUS_PI_DOWN", parent, access, address, signed)
            self.COOL_PI_DOWN_LIMIT  =  self._COOL_PI_DOWN_LIMIT(self,  Access.RW,  0x00000FFF,  0,   signed=False)
            self.COOL_PI_OFF_SPEED   =  self._COOL_PI_OFF_SPEED( self,  Access.RW,  0x0FFF0000,  16,  signed=False)

    class _COOLSTEPPLUS_RESERVE_CONF(Register):

        class _COOL_LOW_LOAD_RESERVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COOL_LOW_LOAD_RESERVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COOL_HI_LOAD_RESERVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COOL_HI_LOAD_RESERVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COOL_LOW_GENERATORIC_RESERVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COOL_LOW_GENERATORIC_RESERVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COOL_HI_GENERATORIC_RESERVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COOL_HI_GENERATORIC_RESERVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("COOLSTEPPLUS_RESERVE_CONF", parent, access, address, signed)
            self.COOL_LOW_LOAD_RESERVE         =  self._COOL_LOW_LOAD_RESERVE(       self,  Access.RW,  0x000000FF,  0,   signed=False)
            self.COOL_HI_LOAD_RESERVE          =  self._COOL_HI_LOAD_RESERVE(        self,  Access.RW,  0x0000FF00,  8,   signed=False)
            self.COOL_LOW_GENERATORIC_RESERVE  =  self._COOL_LOW_GENERATORIC_RESERVE(self,  Access.RW,  0x00FF0000,  16,  signed=False)
            self.COOL_HI_GENERATORIC_RESERVE   =  self._COOL_HI_GENERATORIC_RESERVE( self,  Access.RW,  0xFF000000,  24,  signed=False)

    class _COOLSTEPPLUS_LOAD_RESERVE(Register):

        class _SGP_RESULT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_RESULT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COOLSTEP_LOAD_RESERVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COOLSTEP_LOAD_RESERVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("COOLSTEPPLUS_LOAD_RESERVE", parent, access, address, signed)
            self.SGP_RESULT             =  self._SGP_RESULT(           self,  Access.R,  0x000003FF,  0,   signed=True)
            self.COOLSTEP_LOAD_RESERVE  =  self._COOLSTEP_LOAD_RESERVE(self,  Access.R,  0x01FF0000,  16,  signed=False)

    class _TSTEP_VELOCITY(Register):

        class _TSTEP_VELOCITY(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TSTEP_VELOCITY", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("TSTEP_VELOCITY", parent, access, address, signed)
            self.TSTEP_VELOCITY  =  self._TSTEP_VELOCITY(self,  Access.R,  0x007FFFFF,  0,  signed=True)

    class _ADC_VSUPPLY_TEMP(Register):

        class _ADC_VSUPPLY(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_VSUPPLY", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_TEMP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_TEMP", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_VSUPPLY_TEMP", parent, access, address, signed)
            self.ADC_VSUPPLY  =  self._ADC_VSUPPLY(self,  Access.R,  0x000001FF,  0,   signed=False)
            self.ADC_TEMP     =  self._ADC_TEMP(   self,  Access.R,  0x01FF0000,  16,  signed=False)

    class _ADC_I(Register):

        class _ADC_I_A(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I_A", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_I_B(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I_B", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_I", parent, access, address, signed)
            self.ADC_I_A  =  self._ADC_I_A(self,  Access.R,  0x00000FFF,  0,   signed=True)
            self.ADC_I_B  =  self._ADC_I_B(self,  Access.R,  0x0FFF0000,  16,  signed=True)

    class _OTW_OV_VTH(Register):

        class _OVERVOLTAGE_VTH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OVERVOLTAGE_VTH", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OVERTEMPPREWARNING_VTH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OVERTEMPPREWARNING_VTH", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("OTW_OV_VTH", parent, access, address, signed)
            self.OVERVOLTAGE_VTH         =  self._OVERVOLTAGE_VTH(       self,  Access.RW,  0x000001FF,  0,   signed=False)
            self.OVERTEMPPREWARNING_VTH  =  self._OVERTEMPPREWARNING_VTH(self,  Access.RW,  0x01FF0000,  16,  signed=False)

    class _MSLUT_0(Register):

        class _MSLUT_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_0", parent, access, address, signed)
            self.MSLUT_0  =  self._MSLUT_0(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _MSLUT_1(Register):

        class _MSLUT_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_1", parent, access, address, signed)
            self.MSLUT_1  =  self._MSLUT_1(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _MSLUT_2(Register):

        class _MSLUT_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_2", parent, access, address, signed)
            self.MSLUT_2  =  self._MSLUT_2(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _MSLUT_3(Register):

        class _MSLUT_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_3", parent, access, address, signed)
            self.MSLUT_3  =  self._MSLUT_3(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _MSLUT_4(Register):

        class _MSLUT_4(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_4", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_4", parent, access, address, signed)
            self.MSLUT_4  =  self._MSLUT_4(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _MSLUT_5(Register):

        class _MSLUT_5(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_5", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_5", parent, access, address, signed)
            self.MSLUT_5  =  self._MSLUT_5(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _MSLUT_6(Register):

        class _MSLUT_6(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_6", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_6", parent, access, address, signed)
            self.MSLUT_6  =  self._MSLUT_6(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _MSLUT_7(Register):

        class _MSLUT_7(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_7", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_7", parent, access, address, signed)
            self.MSLUT_7  =  self._MSLUT_7(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _MSLUTSEL(Register):

        class _W0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("W0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _W1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("W1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _W2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("W2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _W3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("W3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _X1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("X1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _X2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("X2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _X3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("X3", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUTSEL", parent, access, address, signed)
            self.W0  =  self._W0(self,  Access.RW,  0x00000003,  0,   signed=False)
            self.W1  =  self._W1(self,  Access.RW,  0x0000000C,  2,   signed=False)
            self.W2  =  self._W2(self,  Access.RW,  0x00000030,  4,   signed=False)
            self.W3  =  self._W3(self,  Access.RW,  0x000000C0,  6,   signed=False)
            self.X1  =  self._X1(self,  Access.RW,  0x0000FF00,  8,   signed=False)
            self.X2  =  self._X2(self,  Access.RW,  0x00FF0000,  16,  signed=False)
            self.X3  =  self._X3(self,  Access.RW,  0xFF000000,  24,  signed=False)

    class _MSLUTSTART(Register):

        class _START_SIN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("START_SIN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _START_SIN90(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("START_SIN90", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFFSET_SIN90(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFFSET_SIN90", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUTSTART", parent, access, address, signed)
            self.START_SIN     =  self._START_SIN(   self,  Access.RW,  0x000000FF,  0,   signed=False)
            self.START_SIN90   =  self._START_SIN90( self,  Access.RW,  0x00FF0000,  16,  signed=False)
            self.OFFSET_SIN90  =  self._OFFSET_SIN90(self,  Access.RW,  0xFF000000,  24,  signed=True)

    class _MSCNT(Register):

        class _MSCNT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSCNT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSCNT", parent, access, address, signed)
            self.MSCNT  =  self._MSCNT(self,  Access.R,  0x000003FF,  0,  signed=False)

    class _MSCURACT(Register):

        class _CUR_B(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_B", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CUR_A(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_A", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSCURACT", parent, access, address, signed)
            self.CUR_B  =  self._CUR_B(self,  Access.R,  0x000001FF,  0,   signed=True)
            self.CUR_A  =  self._CUR_A(self,  Access.R,  0x01FF0000,  16,  signed=True)

    class _CHOPCONF(Register):

        class _TOFF(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TOFF", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HSTRT_TFD210(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HSTRT_TFD210", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HEND_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HEND_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _FD3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FD3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DISFDCC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DISFDCC", parent, access, mask, shift, signed=signed)

                self.choice : _CHOPCONF_DISFDCC_FIELD_CHOICES = {
                    "chm: current comparator terminates fd cycle": Option(False, self),
                    "chm: current comparator ignored for fd cycle termination": Option(True, self),
                }

        class _CHM(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CHM", parent, access, mask, shift, signed=signed)

                self.choice : _CHOPCONF_CHM_FIELD_CHOICES = {
                    "SpreadCycle": Option(False, self),
                    "Constant TOFF chopper": Option(True, self),
                }

        class _TBL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TBL", parent, access, mask, shift, signed=signed)

                self.choice : _CHOPCONF_TBL_FIELD_CHOICES = {
                    "1.25 us": Option(0, self),
                    "1.75 us": Option(1, self),
                    "2.5 us": Option(2, self),
                    "3.625 us": Option(3, self),
                }

        class _TPFD(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TPFD", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _MRES(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MRES", parent, access, mask, shift, signed=signed)

                self.choice : _CHOPCONF_MRES_FIELD_CHOICES = {
                    "256 usteps": Option(0, self),
                    "128 usteps": Option(1, self),
                    "64 usteps": Option(2, self),
                    "32 usteps": Option(3, self),
                    "16 usteps": Option(4, self),
                    "8 usteps": Option(5, self),
                    "4 usteps": Option(6, self),
                    "2 usteps": Option(7, self),
                    "1 ustep / fullstep": Option(8, self),
                    "unused": Option(15, self),
                }

        class _INTPOL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INTPOL", parent, access, mask, shift, signed=signed)

                self.choice : _CHOPCONF_INTPOL_FIELD_CHOICES = {
                    "Interpolation disabled": Option(False, self),
                    "Interpolation enabled": Option(True, self),
                }

        class _DEDGE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DEDGE", parent, access, mask, shift, signed=signed)

                self.choice : _CHOPCONF_DEDGE_FIELD_CHOICES = {
                    "step on rising edge": Option(False, self),
                    "step on both edges": Option(True, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("CHOPCONF", parent, access, address, signed)
            self.TOFF          =  self._TOFF(        self,  Access.RW,  0x0000000F,  0,   signed=False)
            self.HSTRT_TFD210  =  self._HSTRT_TFD210(self,  Access.RW,  0x00000070,  4,   signed=False)
            self.HEND_OFFSET   =  self._HEND_OFFSET( self,  Access.RW,  0x00000780,  7,   signed=False)
            self.FD3           =  self._FD3(         self,  Access.RW,  0x00000800,  11,  signed=False)
            self.DISFDCC       =  self._DISFDCC(     self,  Access.RW,  0x00001000,  12,  signed=False)
            self.CHM           =  self._CHM(         self,  Access.RW,  0x00004000,  14,  signed=False)
            self.TBL           =  self._TBL(         self,  Access.RW,  0x00018000,  15,  signed=False)
            self.TPFD          =  self._TPFD(        self,  Access.RW,  0x00F00000,  20,  signed=False)
            self.MRES          =  self._MRES(        self,  Access.RW,  0x0F000000,  24,  signed=False)
            self.INTPOL        =  self._INTPOL(      self,  Access.RW,  0x10000000,  28,  signed=False)
            self.DEDGE         =  self._DEDGE(       self,  Access.RW,  0x20000000,  29,  signed=False)

    class _COOLCONF(Register):

        class _SEMIN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SEMIN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SEUP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SEUP", parent, access, mask, shift, signed=signed)

                self.choice : _COOLCONF_SEUP_FIELD_CHOICES = {
                    "8 increment per StallGuard value": Option(0, self),
                    "16 increments per StallGuard value": Option(1, self),
                    "32 increments per StallGuard value": Option(2, self),
                    "64 increments per StallGuard value": Option(3, self),
                }

        class _SEMAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SEMAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SEDN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SEDN", parent, access, mask, shift, signed=signed)

                self.choice : _COOLCONF_SEDN_FIELD_CHOICES = {
                    "For each 8 StallGuard2 values decrease by one": Option(0, self),
                    "For each 4 StallGuard2 values decrease by one": Option(1, self),
                    "For each 2 StallGuard2 values decrease by one": Option(2, self),
                    "For each StallGuard2 values decrease by one": Option(3, self),
                    "For each StallGuard2 values decrease by two": Option(4, self),
                    "For each StallGuard2 values decrease by four": Option(5, self),
                    "For each StallGuard2 values decrease by eight": Option(6, self),
                    "For each StallGuard2 values decrease by sixteen": Option(7, self),
                }

        class _SEIMIN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SEIMIN", parent, access, mask, shift, signed=signed)

                self.choice : _COOLCONF_SEIMIN_FIELD_CHOICES = {
                    "0.5 * IRUN": Option(False, self),
                    "0.25 * IRUN": Option(True, self),
                }

        class _SGT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _THIGH_SG_OFF(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("THIGH_SG_OFF", parent, access, mask, shift, signed=signed)

                self.choice : _COOLCONF_THIGH_SG_OFF_FIELD_CHOICES = {
                    "Reaching VHIGH disables coolstep": Option(False, self),
                    "Reaching VHIGH disables coolstep and stop on stall": Option(True, self),
                }

        class _SFILT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SFILT", parent, access, mask, shift, signed=signed)

                self.choice : _COOLCONF_SFILT_FIELD_CHOICES = {
                    "disabled": Option(False, self),
                    "Stallguard signal updated every 4 fullsteps": Option(True, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("COOLCONF", parent, access, address, signed)
            self.SEMIN         =  self._SEMIN(       self,  Access.RW,  0x0000000F,  0,   signed=False)
            self.SEUP          =  self._SEUP(        self,  Access.RW,  0x00000060,  5,   signed=False)
            self.SEMAX         =  self._SEMAX(       self,  Access.RW,  0x00000F00,  8,   signed=False)
            self.SEDN          =  self._SEDN(        self,  Access.RW,  0x00007000,  12,  signed=False)
            self.SEIMIN        =  self._SEIMIN(      self,  Access.RW,  0x00008000,  15,  signed=False)
            self.SGT           =  self._SGT(         self,  Access.RW,  0x007F0000,  16,  signed=True)
            self.THIGH_SG_OFF  =  self._THIGH_SG_OFF(self,  Access.RW,  0x00800000,  23,  signed=False)
            self.SFILT         =  self._SFILT(       self,  Access.RW,  0x01000000,  24,  signed=False)

    class _DRV_STATUS(Register):

        class _SG_RESULT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SG_RESULT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SEQ_STOPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SEQ_STOPPED", parent, access, mask, shift, signed=signed)

                self.choice : _DRV_STATUS_SEQ_STOPPED_FIELD_CHOICES = {
                    "Normal operation": Option(False, self),
                    "Sequencer stopped": Option(True, self),
                }

        class _OV(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OV", parent, access, mask, shift, signed=signed)

                self.choice : _DRV_STATUS_OV_FIELD_CHOICES = {
                    "Normal operation": Option(False, self),
                    "OVERVOLTAGE_VTH reached": Option(True, self),
                }

        class _S2VSA(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("S2VSA", parent, access, mask, shift, signed=signed)

                self.choice : _DRV_STATUS_S2VSA_FIELD_CHOICES = {
                    "Normal operation": Option(False, self),
                    "Short to supply on phase A: driver disabled": Option(True, self),
                }

        class _S2VSB(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("S2VSB", parent, access, mask, shift, signed=signed)

                self.choice : _DRV_STATUS_S2VSB_FIELD_CHOICES = {
                    "Normal operation": Option(False, self),
                    "Short to supply on phase B: driver disabled": Option(True, self),
                }

        class _STEALTH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STEALTH", parent, access, mask, shift, signed=signed)

                self.choice : _DRV_STATUS_STEALTH_FIELD_CHOICES = {
                    "SpreadCycle": Option(False, self),
                    "StealthChop+": Option(True, self),
                }

        class _CS_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CS_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STALLGUARD(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STALLGUARD", parent, access, mask, shift, signed=signed)

                self.choice : _DRV_STATUS_STALLGUARD_FIELD_CHOICES = {
                    "No Stall": Option(False, self),
                    "Stall detected": Option(True, self),
                }

        class _OT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OT", parent, access, mask, shift, signed=signed)

                self.choice : _DRV_STATUS_OT_FIELD_CHOICES = {
                    "Normal Operation": Option(False, self),
                    "Overtemperature detected. Driver turned off.": Option(True, self),
                }

        class _OTPW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OTPW", parent, access, mask, shift, signed=signed)

                self.choice : _DRV_STATUS_OTPW_FIELD_CHOICES = {
                    "Normal operation": Option(False, self),
                    "OVERTEMPPREWARNING_VTH has been reached": Option(True, self),
                }

        class _S2GA(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("S2GA", parent, access, mask, shift, signed=signed)

                self.choice : _DRV_STATUS_S2GA_FIELD_CHOICES = {
                    "Normal operation": Option(False, self),
                    "Short to ground on phase A: driver disabled": Option(True, self),
                }

        class _S2GB(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("S2GB", parent, access, mask, shift, signed=signed)

                self.choice : _DRV_STATUS_S2GB_FIELD_CHOICES = {
                    "Normal operation": Option(False, self),
                    "Short to ground on phase B: driver disabled": Option(True, self),
                }

        class _OLA(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OLA", parent, access, mask, shift, signed=signed)

                self.choice : _DRV_STATUS_OLA_FIELD_CHOICES = {
                    "Normal operation": Option(False, self),
                    "open load on phase A detected": Option(True, self),
                }

        class _OLB(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OLB", parent, access, mask, shift, signed=signed)

                self.choice : _DRV_STATUS_OLB_FIELD_CHOICES = {
                    "Normal operation": Option(False, self),
                    "open load on phase B detected": Option(True, self),
                }

        class _STST(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STST", parent, access, mask, shift, signed=signed)

                self.choice : _DRV_STATUS_STST_FIELD_CHOICES = {
                    "no standstill detected": Option(False, self),
                    "standstill detected": Option(True, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("DRV_STATUS", parent, access, address, signed)
            self.SG_RESULT    =  self._SG_RESULT(  self,  Access.R,  0x000003FF,  0,   signed=False)
            self.SEQ_STOPPED  =  self._SEQ_STOPPED(self,  Access.R,  0x00000400,  10,  signed=False)
            self.OV           =  self._OV(         self,  Access.R,  0x00000800,  11,  signed=False)
            self.S2VSA        =  self._S2VSA(      self,  Access.R,  0x00001000,  12,  signed=False)
            self.S2VSB        =  self._S2VSB(      self,  Access.R,  0x00002000,  13,  signed=False)
            self.STEALTH      =  self._STEALTH(    self,  Access.R,  0x00004000,  14,  signed=False)
            self.CS_ACTUAL    =  self._CS_ACTUAL(  self,  Access.R,  0x00FF0000,  16,  signed=False)
            self.STALLGUARD   =  self._STALLGUARD( self,  Access.R,  0x01000000,  24,  signed=False)
            self.OT           =  self._OT(         self,  Access.R,  0x02000000,  25,  signed=False)
            self.OTPW         =  self._OTPW(       self,  Access.R,  0x04000000,  26,  signed=False)
            self.S2GA         =  self._S2GA(       self,  Access.R,  0x08000000,  27,  signed=False)
            self.S2GB         =  self._S2GB(       self,  Access.R,  0x10000000,  28,  signed=False)
            self.OLA          =  self._OLA(        self,  Access.R,  0x20000000,  29,  signed=False)
            self.OLB          =  self._OLB(        self,  Access.R,  0x40000000,  30,  signed=False)
            self.STST         =  self._STST(       self,  Access.R,  0x80000000,  31,  signed=False)

    class _PWMCONF(Register):

        class _PWM_FREQ(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_FREQ", parent, access, mask, shift, signed=signed)

                self.choice : _PWMCONF_PWM_FREQ_FIELD_CHOICES = {
                    "19.5 kHz": Option(0, self),
                    "24.4 kHz": Option(1, self),
                    "29.3 kHz": Option(2, self),
                    "34.2 kHz": Option(3, self),
                    "39.1 kHz": Option(4, self),
                    "44.0 kHz": Option(5, self),
                    "48.8 kHz": Option(6, self),
                    "53.7 kHz": Option(7, self),
                    "58.6 kHz": Option(8, self),
                }

        class _FREEWHEEL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FREEWHEEL", parent, access, mask, shift, signed=signed)

                self.choice : _PWMCONF_FREEWHEEL_FIELD_CHOICES = {
                    "Normal Operation": Option(0, self),
                    "Freewheeling": Option(1, self),
                    "Coil shorted using LS drivers": Option(2, self),
                    "Coil shorted using HS drivers": Option(3, self),
                }

        class _OL_THRSH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OL_THRSH", parent, access, mask, shift, signed=signed)

                self.choice : _PWMCONF_OL_THRSH_FIELD_CHOICES = {
                    "12.5% of target current": Option(0, self),
                    "25% of target current": Option(1, self),
                    "50% of target current": Option(2, self),
                    "75% of target current": Option(3, self),
                }

        class _SD_ON_MEAS_LO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SD_ON_MEAS_LO", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SD_ON_MEAS_HI(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SD_ON_MEAS_HI", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PWMCONF", parent, access, address, signed)
            self.PWM_FREQ       =  self._PWM_FREQ(     self,  Access.RW,  0x0000000F,  0,   signed=False)
            self.FREEWHEEL      =  self._FREEWHEEL(    self,  Access.RW,  0x00000030,  4,   signed=False)
            self.OL_THRSH       =  self._OL_THRSH(     self,  Access.RW,  0x000000C0,  6,   signed=False)
            self.SD_ON_MEAS_LO  =  self._SD_ON_MEAS_LO(self,  Access.RW,  0x0000F000,  12,  signed=False)
            self.SD_ON_MEAS_HI  =  self._SD_ON_MEAS_HI(self,  Access.RW,  0x000F0000,  16,  signed=False)

    def __init__(self, channel, block, width):
        super().__init__("ALL_REGISTERS", channel, block, width)
        self.GCONF                      =  self._GCONF(                    self,  Access.RW,   0x0000,  False)
        self.GSTAT                      =  self._GSTAT(                    self,  Access.RWC,  0x0001,  False)
        self.DO_CONF                    =  self._DO_CONF(                  self,  Access.RW,   0x0002,  False)
        self.DO_SCOPE_CONF              =  self._DO_SCOPE_CONF(            self,  Access.RW,   0x0003,  False)
        self.IOIN                       =  self._IOIN(                     self,  Access.R,    0x0004,  False)
        self.X_COMPARE                  =  self._X_COMPARE(                self,  Access.RW,   0x0005,  True)
        self.X_COMPARE_REPEAT           =  self._X_COMPARE_REPEAT(         self,  Access.RW,   0x0006,  False)
        self.DRV_CONF                   =  self._DRV_CONF(                 self,  Access.RW,   0x000A,  False)
        self.PLL                        =  self._PLL(                      self,  Access.RW,   0x000B,  False)
        self.IHOLD_IRUN                 =  self._IHOLD_IRUN(               self,  Access.RW,   0x0010,  False)
        self.TPOWERDOWN                 =  self._TPOWERDOWN(               self,  Access.RW,   0x0011,  False)
        self.TSTEP                      =  self._TSTEP(                    self,  Access.R,    0x0012,  False)
        self.TPWMTHRS                   =  self._TPWMTHRS(                 self,  Access.RW,   0x0013,  False)
        self.TCOOLTHRS                  =  self._TCOOLTHRS(                self,  Access.RW,   0x0014,  False)
        self.THIGH                      =  self._THIGH(                    self,  Access.RW,   0x0015,  False)
        self.TSGP_LOW_VEL_THRS          =  self._TSGP_LOW_VEL_THRS(        self,  Access.RW,   0x0016,  False)
        self.T_RCOIL_MEAS               =  self._T_RCOIL_MEAS(             self,  Access.RW,   0x0017,  False)
        self.TUDCSTEP                   =  self._TUDCSTEP(                 self,  Access.RW,   0x0018,  False)
        self.UDC_CONF                   =  self._UDC_CONF(                 self,  Access.RW,   0x0019,  False)
        self.STEPS_LOST                 =  self._STEPS_LOST(               self,  Access.RW,   0x001A,  True)
        self.RAMPMODE                   =  self._RAMPMODE(                 self,  Access.RW,   0x0020,  False)
        self.XACTUAL                    =  self._XACTUAL(                  self,  Access.RW,   0x0021,  True)
        self.VACTUAL                    =  self._VACTUAL(                  self,  Access.R,    0x0022,  True)
        self.VSTART                     =  self._VSTART(                   self,  Access.RW,   0x0023,  False)
        self.A1                         =  self._A1(                       self,  Access.RW,   0x0024,  False)
        self.V1                         =  self._V1(                       self,  Access.RW,   0x0025,  False)
        self.AMAX                       =  self._AMAX(                     self,  Access.RW,   0x0026,  False)
        self.VMAX                       =  self._VMAX(                     self,  Access.RW,   0x0027,  False)
        self.DMAX                       =  self._DMAX(                     self,  Access.RW,   0x0028,  False)
        self.TVMAX                      =  self._TVMAX(                    self,  Access.RW,   0x0029,  False)
        self.D1                         =  self._D1(                       self,  Access.RW,   0x002A,  False)
        self.VSTOP                      =  self._VSTOP(                    self,  Access.RW,   0x002B,  False)
        self.TZEROWAIT                  =  self._TZEROWAIT(                self,  Access.RW,   0x002C,  False)
        self.XTARGET                    =  self._XTARGET(                  self,  Access.RW,   0x002D,  True)
        self.V2                         =  self._V2(                       self,  Access.RW,   0x002E,  False)
        self.A2                         =  self._A2(                       self,  Access.RW,   0x002F,  False)
        self.D2                         =  self._D2(                       self,  Access.RW,   0x0030,  False)
        self.AACTUAL                    =  self._AACTUAL(                  self,  Access.R,    0x0031,  True)
        self.SW_MODE                    =  self._SW_MODE(                  self,  Access.RW,   0x0034,  False)
        self.RAMP_STAT                  =  self._RAMP_STAT(                self,  Access.RWC,  0x0035,  False)
        self.XLATCH                     =  self._XLATCH(                   self,  Access.R,    0x0036,  False)
        self.ENCMODE                    =  self._ENCMODE(                  self,  Access.RW,   0x0038,  False)
        self.X_ENC                      =  self._X_ENC(                    self,  Access.RW,   0x0039,  True)
        self.ENC_CONST                  =  self._ENC_CONST(                self,  Access.RW,   0x003A,  True)
        self.ENC_STATUS                 =  self._ENC_STATUS(               self,  Access.RWC,  0x003B,  False)
        self.ENC_LATCH                  =  self._ENC_LATCH(                self,  Access.R,    0x003C,  False)
        self.ENC_DEVIATION              =  self._ENC_DEVIATION(            self,  Access.R,    0x003D,  False)
        self.VIRTUAL_STOP_L             =  self._VIRTUAL_STOP_L(           self,  Access.RW,   0x003E,  True)
        self.VIRTUAL_STOP_R             =  self._VIRTUAL_STOP_R(           self,  Access.RW,   0x003F,  True)
        self.CURRENT_PI_REG             =  self._CURRENT_PI_REG(           self,  Access.RW,   0x0040,  False)
        self.ANGLE_PI_REG               =  self._ANGLE_PI_REG(             self,  Access.RW,   0x0041,  False)
        self.CUR_ANGLE_LIMIT            =  self._CUR_ANGLE_LIMIT(          self,  Access.RW,   0x0042,  False)
        self.ANGLE_LOWER_LIMIT          =  self._ANGLE_LOWER_LIMIT(        self,  Access.RW,   0x0043,  False)
        self.CUR_ANGLE_MEAS             =  self._CUR_ANGLE_MEAS(           self,  Access.R,    0x0044,  False)
        self.PI_RESULTS                 =  self._PI_RESULTS(               self,  Access.R,    0x0045,  False)
        self.COIL_INDUCT                =  self._COIL_INDUCT(              self,  Access.RW,   0x0046,  False)
        self.R_COIL                     =  self._R_COIL(                   self,  Access.R,    0x0047,  False)
        self.R_COIL_USER                =  self._R_COIL_USER(              self,  Access.RW,   0x0048,  False)
        self.SGP_CONF                   =  self._SGP_CONF(                 self,  Access.RW,   0x0049,  False)
        self.SGP_IND_2_3                =  self._SGP_IND_2_3(              self,  Access.R,    0x004A,  False)
        self.SGP_IND_0_1                =  self._SGP_IND_0_1(              self,  Access.R,    0x004B,  False)
        self.INDUCTANCE_VOLTAGE         =  self._INDUCTANCE_VOLTAGE(       self,  Access.R,    0x004C,  False)
        self.SGP_BEMF                   =  self._SGP_BEMF(                 self,  Access.R,    0x004D,  False)
        self.COOLSTEPPLUS_CONF          =  self._COOLSTEPPLUS_CONF(        self,  Access.RW,   0x004E,  False)
        self.COOLSTEPPLUS_PI_REG        =  self._COOLSTEPPLUS_PI_REG(      self,  Access.RW,   0x004F,  False)
        self.COOLSTEPPLUS_PI_DOWN       =  self._COOLSTEPPLUS_PI_DOWN(     self,  Access.RW,   0x0050,  False)
        self.COOLSTEPPLUS_RESERVE_CONF  =  self._COOLSTEPPLUS_RESERVE_CONF(self,  Access.RW,   0x0051,  False)
        self.COOLSTEPPLUS_LOAD_RESERVE  =  self._COOLSTEPPLUS_LOAD_RESERVE(self,  Access.R,    0x0052,  False)
        self.TSTEP_VELOCITY             =  self._TSTEP_VELOCITY(           self,  Access.R,    0x0053,  True)
        self.ADC_VSUPPLY_TEMP           =  self._ADC_VSUPPLY_TEMP(         self,  Access.R,    0x0058,  False)
        self.ADC_I                      =  self._ADC_I(                    self,  Access.R,    0x0059,  False)
        self.OTW_OV_VTH                 =  self._OTW_OV_VTH(               self,  Access.RW,   0x005A,  False)
        self.MSLUT_0                    =  self._MSLUT_0(                  self,  Access.RW,   0x0060,  False)
        self.MSLUT_1                    =  self._MSLUT_1(                  self,  Access.RW,   0x0061,  False)
        self.MSLUT_2                    =  self._MSLUT_2(                  self,  Access.RW,   0x0062,  False)
        self.MSLUT_3                    =  self._MSLUT_3(                  self,  Access.RW,   0x0063,  False)
        self.MSLUT_4                    =  self._MSLUT_4(                  self,  Access.RW,   0x0064,  False)
        self.MSLUT_5                    =  self._MSLUT_5(                  self,  Access.RW,   0x0065,  False)
        self.MSLUT_6                    =  self._MSLUT_6(                  self,  Access.RW,   0x0066,  False)
        self.MSLUT_7                    =  self._MSLUT_7(                  self,  Access.RW,   0x0067,  False)
        self.MSLUTSEL                   =  self._MSLUTSEL(                 self,  Access.RW,   0x0068,  False)
        self.MSLUTSTART                 =  self._MSLUTSTART(               self,  Access.RW,   0x0069,  False)
        self.MSCNT                      =  self._MSCNT(                    self,  Access.R,    0x006A,  False)
        self.MSCURACT                   =  self._MSCURACT(                 self,  Access.R,    0x006B,  False)
        self.CHOPCONF                   =  self._CHOPCONF(                 self,  Access.RW,   0x006C,  False)
        self.COOLCONF                   =  self._COOLCONF(                 self,  Access.RW,   0x006D,  False)
        self.DRV_STATUS                 =  self._DRV_STATUS(               self,  Access.R,    0x006F,  False)
        self.PWMCONF                    =  self._PWMCONF(                  self,  Access.RW,   0x0070,  False)
