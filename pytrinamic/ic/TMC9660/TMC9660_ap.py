################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from pytrinamic.modules import Parameter


class Ap:

    def __init__(self):
        self.MOTOR_TYPE                                      =  _MOTOR_TYPE(                                      0,    Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.MOTOR_POLE_PAIRS                                =  _MOTOR_POLE_PAIRS(                                1,    Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.MOTOR_DIRECTION                                 =  _MOTOR_DIRECTION(                                 2,    Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.MOTOR_PWM_FREQUENCY                             =  _MOTOR_PWM_FREQUENCY(                             3,    Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.COMMUTATION_MODE                                =  _COMMUTATION_MODE(                                4,    Parameter.Access.RW,   Parameter.Datatype.ENUM)
        self.OUTPUT_VOLTAGE_LIMIT                            =  _OUTPUT_VOLTAGE_LIMIT(                            5,    Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.MAX_TORQUE                                      =  _MAX_TORQUE(                                      6,    Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.MAX_FLUX                                        =  _MAX_FLUX(                                        7,    Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.PWM_SWITCHING_SCHEME                            =  _PWM_SWITCHING_SCHEME(                            8,    Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.IDLE_MOTOR_PWM_BEHAVIOR                         =  _IDLE_MOTOR_PWM_BEHAVIOR(                         9,    Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.ADC_SHUNT_TYPE                                  =  _ADC_SHUNT_TYPE(                                  12,   Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.ADC_I0_RAW                                      =  _ADC_I0_RAW(                                      13,   Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.ADC_I1_RAW                                      =  _ADC_I1_RAW(                                      14,   Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.ADC_I2_RAW                                      =  _ADC_I2_RAW(                                      15,   Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.ADC_I3_RAW                                      =  _ADC_I3_RAW(                                      16,   Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.CSA_GAIN_ADC_I0_TO_ADC_I2                       =  _CSA_GAIN_ADC_I0_TO_ADC_I2(                       17,   Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.CSA_GAIN_ADC_I3                                 =  _CSA_GAIN_ADC_I3(                                 18,   Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.CSA_FILTER_ADC_I0_TO_ADC_I2                     =  _CSA_FILTER_ADC_I0_TO_ADC_I2(                     19,   Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.CSA_FILTER_ADC_I3                               =  _CSA_FILTER_ADC_I3(                               20,   Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.CURRENT_SCALING_FACTOR                          =  _CURRENT_SCALING_FACTOR(                          21,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.PHASE_UX1_ADC_MAPPING                           =  _PHASE_UX1_ADC_MAPPING(                           22,   Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.PHASE_VX2_ADC_MAPPING                           =  _PHASE_VX2_ADC_MAPPING(                           23,   Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.PHASE_WY1_ADC_MAPPING                           =  _PHASE_WY1_ADC_MAPPING(                           24,   Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.PHASE_Y2_ADC_MAPPING                            =  _PHASE_Y2_ADC_MAPPING(                            25,   Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.ADC_I0_SCALE                                    =  _ADC_I0_SCALE(                                    26,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.ADC_I1_SCALE                                    =  _ADC_I1_SCALE(                                    27,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.ADC_I2_SCALE                                    =  _ADC_I2_SCALE(                                    28,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.ADC_I3_SCALE                                    =  _ADC_I3_SCALE(                                    29,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.ADC_I0_INVERTED                                 =  _ADC_I0_INVERTED(                                 30,   Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.ADC_I1_INVERTED                                 =  _ADC_I1_INVERTED(                                 31,   Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.ADC_I2_INVERTED                                 =  _ADC_I2_INVERTED(                                 32,   Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.ADC_I3_INVERTED                                 =  _ADC_I3_INVERTED(                                 33,   Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.ADC_I0_OFFSET                                   =  _ADC_I0_OFFSET(                                   34,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.ADC_I1_OFFSET                                   =  _ADC_I1_OFFSET(                                   35,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.ADC_I2_OFFSET                                   =  _ADC_I2_OFFSET(                                   36,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.ADC_I3_OFFSET                                   =  _ADC_I3_OFFSET(                                   37,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.ADC_I0                                          =  _ADC_I0(                                          38,   Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.ADC_I1                                          =  _ADC_I1(                                          39,   Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.ADC_I2                                          =  _ADC_I2(                                          40,   Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.ADC_I3                                          =  _ADC_I3(                                          41,   Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.OPENLOOP_ANGLE                                  =  _OPENLOOP_ANGLE(                                  45,   Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.OPENLOOP_CURRENT                                =  _OPENLOOP_CURRENT(                                46,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.OPENLOOP_VOLTAGE                                =  _OPENLOOP_VOLTAGE(                                47,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.ACCELERATION_FF_GAIN                            =  _ACCELERATION_FF_GAIN(                            50,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.ACCELERATION_FF_SHIFT                           =  _ACCELERATION_FF_SHIFT(                           51,   Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.RAMP_ENABLE                                     =  _RAMP_ENABLE(                                     52,   Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.DIRECT_VELOCITY_MODE                            =  _DIRECT_VELOCITY_MODE(                            53,   Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.RAMP_AMAX                                       =  _RAMP_AMAX(                                       54,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.RAMP_A1                                         =  _RAMP_A1(                                         55,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.RAMP_A2                                         =  _RAMP_A2(                                         56,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.RAMP_DMAX                                       =  _RAMP_DMAX(                                       57,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.RAMP_D1                                         =  _RAMP_D1(                                         58,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.RAMP_D2                                         =  _RAMP_D2(                                         59,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.RAMP_VMAX                                       =  _RAMP_VMAX(                                       60,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.RAMP_V1                                         =  _RAMP_V1(                                         61,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.RAMP_V2                                         =  _RAMP_V2(                                         62,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.RAMP_VSTART                                     =  _RAMP_VSTART(                                     63,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.RAMP_VSTOP                                      =  _RAMP_VSTOP(                                      64,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.RAMP_TVMAX                                      =  _RAMP_TVMAX(                                      65,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.RAMP_TZEROWAIT                                  =  _RAMP_TZEROWAIT(                                  66,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.ACCELERATION_FEEDFORWARD_ENABLE                 =  _ACCELERATION_FEEDFORWARD_ENABLE(                 67,   Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.VELOCITY_FEEDFORWARD_ENABLE                     =  _VELOCITY_FEEDFORWARD_ENABLE(                     68,   Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.RAMP_VELOCITY                                   =  _RAMP_VELOCITY(                                   69,   Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.RAMP_POSITION                                   =  _RAMP_POSITION(                                   70,   Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.HALL_PHI_E                                      =  _HALL_PHI_E(                                      74,   Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.HALL_SECTOR_OFFSET                              =  _HALL_SECTOR_OFFSET(                              75,   Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.HALL_FILTER_LENGTH                              =  _HALL_FILTER_LENGTH(                              76,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.HALL_POSITION_0_OFFSET                          =  _HALL_POSITION_0_OFFSET(                          77,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.HALL_POSITION_60_OFFSET                         =  _HALL_POSITION_60_OFFSET(                         78,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.HALL_POSITION_120_OFFSET                        =  _HALL_POSITION_120_OFFSET(                        79,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.HALL_POSITION_180_OFFSET                        =  _HALL_POSITION_180_OFFSET(                        80,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.HALL_POSITION_240_OFFSET                        =  _HALL_POSITION_240_OFFSET(                        81,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.HALL_POSITION_300_OFFSET                        =  _HALL_POSITION_300_OFFSET(                        82,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.HALL_INVERT_DIRECTION                           =  _HALL_INVERT_DIRECTION(                           83,   Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.HALL_EXTRAPOLATION_ENABLE                       =  _HALL_EXTRAPOLATION_ENABLE(                       84,   Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.HALL_PHI_E_OFFSET                               =  _HALL_PHI_E_OFFSET(                               85,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.ABN_1_PHI_E                                     =  _ABN_1_PHI_E(                                     89,   Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.ABN_1_STEPS                                     =  _ABN_1_STEPS(                                     90,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.ABN_1_DIRECTION                                 =  _ABN_1_DIRECTION(                                 91,   Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.ABN_1_INIT_METHOD                               =  _ABN_1_INIT_METHOD(                               92,   Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.ABN_1_INIT_STATE                                =  _ABN_1_INIT_STATE(                                93,   Parameter.Access.R,    Parameter.Datatype.ENUM)
        self.ABN_1_INIT_DELAY                                =  _ABN_1_INIT_DELAY(                                94,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.ABN_1_INIT_VELOCITY                             =  _ABN_1_INIT_VELOCITY(                             95,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.ABN_1_N_CHANNEL_PHI_E_OFFSET                    =  _ABN_1_N_CHANNEL_PHI_E_OFFSET(                    96,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.ABN_1_N_CHANNEL_INVERTED                        =  _ABN_1_N_CHANNEL_INVERTED(                        97,   Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.ABN_1_N_CHANNEL_FILTERING                       =  _ABN_1_N_CHANNEL_FILTERING(                       98,   Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.ABN_1_CLEAR_ON_NEXT_NULL                        =  _ABN_1_CLEAR_ON_NEXT_NULL(                        99,   Parameter.Access.RW,   Parameter.Datatype.BOOLEAN)
        self.ABN_1_VALUE                                     =  _ABN_1_VALUE(                                     100,  Parameter.Access.R,    Parameter.Datatype.UNSIGNED)
        self.TARGET_TORQUE                                   =  _TARGET_TORQUE(                                   104,  Parameter.Access.RW,   Parameter.Datatype.SIGNED)
        self.ACTUAL_TORQUE                                   =  _ACTUAL_TORQUE(                                   105,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.TARGET_FLUX                                     =  _TARGET_FLUX(                                     106,  Parameter.Access.RW,   Parameter.Datatype.SIGNED)
        self.ACTUAL_FLUX                                     =  _ACTUAL_FLUX(                                     107,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.TORQUE_OFFSET                                   =  _TORQUE_OFFSET(                                   108,  Parameter.Access.RW,   Parameter.Datatype.SIGNED)
        self.TORQUE_P                                        =  _TORQUE_P(                                        109,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.TORQUE_I                                        =  _TORQUE_I(                                        110,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.FLUX_P                                          =  _FLUX_P(                                          111,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.FLUX_I                                          =  _FLUX_I(                                          112,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.SEPARATE_TORQUE_FLUX_PI_PARAMTERS               =  _SEPARATE_TORQUE_FLUX_PI_PARAMTERS(               113,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.CURRENT_NORM_P                                  =  _CURRENT_NORM_P(                                  114,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.CURRENT_NORM_I                                  =  _CURRENT_NORM_I(                                  115,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.TORQUE_PI_ERROR                                 =  _TORQUE_PI_ERROR(                                 116,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.FLUX_PI_ERROR                                   =  _FLUX_PI_ERROR(                                   117,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.TORQUE_PI_INTEGRATOR                            =  _TORQUE_PI_INTEGRATOR(                            118,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.FLUX_PI_INTEGRATOR                              =  _FLUX_PI_INTEGRATOR(                              119,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.FLUX_OFFSET                                     =  _FLUX_OFFSET(                                     120,  Parameter.Access.RW,   Parameter.Datatype.SIGNED)
        self.VELOCITY_SENSOR_SELECTION                       =  _VELOCITY_SENSOR_SELECTION(                       123,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.TARGET_VELOCITY                                 =  _TARGET_VELOCITY(                                 124,  Parameter.Access.RW,   Parameter.Datatype.SIGNED)
        self.ACTUAL_VELOCITY                                 =  _ACTUAL_VELOCITY(                                 125,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.VELOCITY_OFFSET                                 =  _VELOCITY_OFFSET(                                 126,  Parameter.Access.RW,   Parameter.Datatype.SIGNED)
        self.VELOCITY_P                                      =  _VELOCITY_P(                                      127,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.VELOCITY_I                                      =  _VELOCITY_I(                                      128,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.VELOCITY_NORM_P                                 =  _VELOCITY_NORM_P(                                 129,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.VELOCITY_NORM_I                                 =  _VELOCITY_NORM_I(                                 130,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.VELOCITY_PI_INTEGRATOR                          =  _VELOCITY_PI_INTEGRATOR(                          131,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.VELOCITY_PI_ERROR                               =  _VELOCITY_PI_ERROR(                               132,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.VELOCITY_SCALING_FACTOR                         =  _VELOCITY_SCALING_FACTOR(                         133,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.STOP_ON_VELOCITY_DEVIATION                      =  _STOP_ON_VELOCITY_DEVIATION(                      134,  Parameter.Access.RW,   Parameter.Datatype.UNSIGNED)
        self.VELOCITY_LOOP_DOWNSAMPLING                      =  _VELOCITY_LOOP_DOWNSAMPLING(                      135,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.VELOCITY_REACHED_THRESHOLD                      =  _VELOCITY_REACHED_THRESHOLD(                      136,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.VELOCITY_METER_SWITCH_THRESHOLD                 =  _VELOCITY_METER_SWITCH_THRESHOLD(                 137,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.VELOCITY_METER_SWITCH_HYSTERESIS                =  _VELOCITY_METER_SWITCH_HYSTERESIS(                138,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.VELOCITY_METER_MODE                             =  _VELOCITY_METER_MODE(                             139,  Parameter.Access.R,    Parameter.Datatype.ENUM)
        self.POSITION_SENSOR_SELECTION                       =  _POSITION_SENSOR_SELECTION(                       142,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.TARGET_POSITION                                 =  _TARGET_POSITION(                                 143,  Parameter.Access.RW,   Parameter.Datatype.SIGNED)
        self.ACTUAL_POSITION                                 =  _ACTUAL_POSITION(                                 144,  Parameter.Access.RW,   Parameter.Datatype.SIGNED)
        self.POSITION_SCALING_FACTOR                         =  _POSITION_SCALING_FACTOR(                         145,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.POSITION_P                                      =  _POSITION_P(                                      146,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.POSITION_I                                      =  _POSITION_I(                                      147,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.POSITION_NORM_P                                 =  _POSITION_NORM_P(                                 148,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.POSITION_NORM_I                                 =  _POSITION_NORM_I(                                 149,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.POSITION_PI_INTEGRATOR                          =  _POSITION_PI_INTEGRATOR(                          150,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.POSITION_PI_ERROR                               =  _POSITION_PI_ERROR(                               151,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.STOP_ON_POSITION_DEVIATION                      =  _STOP_ON_POSITION_DEVIATION(                      152,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.POSITION_LOOP_DOWNSAMPLING                      =  _POSITION_LOOP_DOWNSAMPLING(                      153,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.LATCH_POSITION                                  =  _LATCH_POSITION(                                  154,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.POSITION_LIMIT_LOW                              =  _POSITION_LIMIT_LOW(                              155,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.POSITION_LIMIT_HIGH                             =  _POSITION_LIMIT_HIGH(                             156,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.POSITION_REACHED_THRESHOLD                      =  _POSITION_REACHED_THRESHOLD(                      157,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.REFERENCE_SWITCH_ENABLE                         =  _REFERENCE_SWITCH_ENABLE(                         161,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.REFERENCE_SWITCH_POLARITY_AND_SWAP              =  _REFERENCE_SWITCH_POLARITY_AND_SWAP(              162,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.REFERENCE_SWITCH_LATCH_SETTINGS                 =  _REFERENCE_SWITCH_LATCH_SETTINGS(                 163,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.EVENT_STOP_SETTINGS                             =  _EVENT_STOP_SETTINGS(                             164,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.REFERENCE_SWITCH_SEARCH_MODE                    =  _REFERENCE_SWITCH_SEARCH_MODE(                    165,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.REFERENCE_SWITCH_SEARCH_SPEED                   =  _REFERENCE_SWITCH_SEARCH_SPEED(                   166,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.REFERENCE_SWITCH_SPEED                          =  _REFERENCE_SWITCH_SPEED(                          167,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.RIGHT_LIMIT_SWITCH_POSITION                     =  _RIGHT_LIMIT_SWITCH_POSITION(                     168,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.HOME_SWITCH_POSITION                            =  _HOME_SWITCH_POSITION(                            169,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.LAST_REFERENCE_POSITION                         =  _LAST_REFERENCE_POSITION(                         170,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.ABN_2_STEPS                                     =  _ABN_2_STEPS(                                     174,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.ABN_2_DIRECTION                                 =  _ABN_2_DIRECTION(                                 175,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.ABN_2_GEAR_RATIO                                =  _ABN_2_GEAR_RATIO(                                176,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.ABN_2_ENABLE                                    =  _ABN_2_ENABLE(                                    177,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.ABN_2_VALUE                                     =  _ABN_2_VALUE(                                     178,  Parameter.Access.R,    Parameter.Datatype.UNSIGNED)
        self.SPI_ENCODE_CS_SETTLE_DELAY_TIME                 =  _SPI_ENCODE_CS_SETTLE_DELAY_TIME(                 181,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.SPI_ENCODER_CS_IDLE_DELAY_TIME                  =  _SPI_ENCODER_CS_IDLE_DELAY_TIME(                  182,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.SPI_ENCODER_MAIN_TRANSFER_CMD_SIZE              =  _SPI_ENCODER_MAIN_TRANSFER_CMD_SIZE(              183,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.SPI_ENCODER_SECONDARY_TRANSFER_CMD_SIZE         =  _SPI_ENCODER_SECONDARY_TRANSFER_CMD_SIZE(         184,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.SPI_ENCODER_TRANSFER_DATA_3_0                   =  _SPI_ENCODER_TRANSFER_DATA_3_0(                   185,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.SPI_ENCODER_TRANSFER_DATA_7_4                   =  _SPI_ENCODER_TRANSFER_DATA_7_4(                   186,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.SPI_ENCODER_TRANSFER_DATA_11_8                  =  _SPI_ENCODER_TRANSFER_DATA_11_8(                  187,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.SPI_ENCODER_TRANSFER_DATA_15_12                 =  _SPI_ENCODER_TRANSFER_DATA_15_12(                 188,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.SPI_ENCODER_TRANSFER                            =  _SPI_ENCODER_TRANSFER(                            189,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.SPI_ENCODER_POSITION_COUNTER_MASK               =  _SPI_ENCODER_POSITION_COUNTER_MASK(               190,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.SPI_ENCODER_POSITION_COUNTER_SHIFT              =  _SPI_ENCODER_POSITION_COUNTER_SHIFT(              191,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.SPI_ENCODER_POSITION_COUNTER_VALUE              =  _SPI_ENCODER_POSITION_COUNTER_VALUE(              192,  Parameter.Access.R,    Parameter.Datatype.UNSIGNED)
        self.SPI_ENCODER_COMMUTATION_ANGLE                   =  _SPI_ENCODER_COMMUTATION_ANGLE(                   193,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.SPI_ENCODER_INITIALIZATION_METHOD               =  _SPI_ENCODER_INITIALIZATION_METHOD(               194,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.SPI_ENCODER_DIRECTION                           =  _SPI_ENCODER_DIRECTION(                           195,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.SPI_ENCODER_OFFSET                              =  _SPI_ENCODER_OFFSET(                              196,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.SPI_LUT_CORRECTION_ENABLE                       =  _SPI_LUT_CORRECTION_ENABLE(                       197,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.SPI_LUT_ADDRESS_SELECT                          =  _SPI_LUT_ADDRESS_SELECT(                          198,  Parameter.Access.RW,   Parameter.Datatype.UNSIGNED)
        self.SPI_LUT_DATA                                    =  _SPI_LUT_DATA(                                    199,  Parameter.Access.RW,   Parameter.Datatype.SIGNED)
        self.SPI_LUT_COMMON_SHIFT_FACTOR                     =  _SPI_LUT_COMMON_SHIFT_FACTOR(                     201,  Parameter.Access.RW,   Parameter.Datatype.UNSIGNED)
        self.STEP_DIR_STEP_DIVIDER_SHIFT                     =  _STEP_DIR_STEP_DIVIDER_SHIFT(                     205,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.STEP_DIR_ENABLE                                 =  _STEP_DIR_ENABLE(                                 206,  Parameter.Access.RW,   Parameter.Datatype.BOOLEAN)
        self.STEP_DIR_EXTRAPOLATION_ENABLE                   =  _STEP_DIR_EXTRAPOLATION_ENABLE(                   207,  Parameter.Access.RW,   Parameter.Datatype.BOOLEAN)
        self.STEP_DIR_STEP_SIGNAL_TIMEOUT_LIMIT              =  _STEP_DIR_STEP_SIGNAL_TIMEOUT_LIMIT(              208,  Parameter.Access.RW,   Parameter.Datatype.UNSIGNED)
        self.STEP_DIR_MAXIMUM_EXTRAPOLATION_VELOCITY         =  _STEP_DIR_MAXIMUM_EXTRAPOLATION_VELOCITY(         209,  Parameter.Access.RW,   Parameter.Datatype.UNSIGNED)
        self.BRAKE_CHOPPER_ENABLE                            =  _BRAKE_CHOPPER_ENABLE(                            212,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.BRAKE_CHOPPER_VOLTAGE_LIMIT                     =  _BRAKE_CHOPPER_VOLTAGE_LIMIT(                     213,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.BRAKE_CHOPPER_HYSTERESIS                        =  _BRAKE_CHOPPER_HYSTERESIS(                        214,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.RELEASE_BRAKE                                   =  _RELEASE_BRAKE(                                   216,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.BRAKE_RELEASING_DUTY_CYCLE                      =  _BRAKE_RELEASING_DUTY_CYCLE(                      217,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.BRAKE_HOLDING_DUTY_CYCLE                        =  _BRAKE_HOLDING_DUTY_CYCLE(                        218,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.BRAKE_RELEASING_DURATION                        =  _BRAKE_RELEASING_DURATION(                        219,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.INVERT_BRAKE_OUTPUT                             =  _INVERT_BRAKE_OUTPUT(                             221,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.THERMAL_WINDING_TIME_CONSTANT_1                 =  _THERMAL_WINDING_TIME_CONSTANT_1(                 224,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.IIT_LIMIT_1                                     =  _IIT_LIMIT_1(                                     225,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.IIT_SUM_1                                       =  _IIT_SUM_1(                                       226,  Parameter.Access.R,    Parameter.Datatype.UNSIGNED)
        self.THERMAL_WINDING_TIME_CONSTANT_2                 =  _THERMAL_WINDING_TIME_CONSTANT_2(                 227,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.IIT_LIMIT_2                                     =  _IIT_LIMIT_2(                                     228,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.IIT_SUM_2                                       =  _IIT_SUM_2(                                       229,  Parameter.Access.R,    Parameter.Datatype.UNSIGNED)
        self.RESET_IIT_SUMS                                  =  _RESET_IIT_SUMS(                                  230,  Parameter.Access.W,    Parameter.Datatype.UNSIGNED)
        self.ACTUAL_TOTAL_MOTOR_CURRENT                      =  _ACTUAL_TOTAL_MOTOR_CURRENT(                      231,  Parameter.Access.R,    Parameter.Datatype.UNSIGNED)
        self.PWM_L_OUTPUT_POLARITY                           =  _PWM_L_OUTPUT_POLARITY(                           233,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.PWM_H_OUTPUT_POLARITY                           =  _PWM_H_OUTPUT_POLARITY(                           234,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.BREAK_BEFORE_MAKE_TIME_LOW_UVW                  =  _BREAK_BEFORE_MAKE_TIME_LOW_UVW(                  235,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.BREAK_BEFORE_MAKE_TIME_HIGH_UVW                 =  _BREAK_BEFORE_MAKE_TIME_HIGH_UVW(                 236,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.BREAK_BEFORE_MAKE_TIME_LOW_Y2                   =  _BREAK_BEFORE_MAKE_TIME_LOW_Y2(                   237,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.BREAK_BEFORE_MAKE_TIME_HIGH_Y2                  =  _BREAK_BEFORE_MAKE_TIME_HIGH_Y2(                  238,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.USE_ADAPTIVE_DRIVE_TIME_UVW                     =  _USE_ADAPTIVE_DRIVE_TIME_UVW(                     239,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.USE_ADAPTIVE_DRIVE_TIME_Y2                      =  _USE_ADAPTIVE_DRIVE_TIME_Y2(                      240,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.DRIVE_TIME_SINK_UVW                             =  _DRIVE_TIME_SINK_UVW(                             241,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.DRIVE_TIME_SOURCE_UVW                           =  _DRIVE_TIME_SOURCE_UVW(                           242,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.DRIVE_TIME_SINK_Y2                              =  _DRIVE_TIME_SINK_Y2(                              243,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.DRIVE_TIME_SOURCE_Y2                            =  _DRIVE_TIME_SOURCE_Y2(                            244,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.UVW_SINK_CURRENT                                =  _UVW_SINK_CURRENT(                                245,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.UVW_SOURCE_CURRENT                              =  _UVW_SOURCE_CURRENT(                              246,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.Y2_SINK_CURRENT                                 =  _Y2_SINK_CURRENT(                                 247,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.Y2_SOURCE_CURRENT                               =  _Y2_SOURCE_CURRENT(                               248,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.BOOTSTRAP_CURRENT_LIMIT                         =  _BOOTSTRAP_CURRENT_LIMIT(                         249,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.UNDERVOLTAGE_PROTECTION_SUPPLY_LEVEL            =  _UNDERVOLTAGE_PROTECTION_SUPPLY_LEVEL(            250,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.UNDERVOLTAGE_PROTECTION_VDRV_ENABLE             =  _UNDERVOLTAGE_PROTECTION_VDRV_ENABLE(             251,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.UNDERVOLTAGE_PROTECTION_BST_UVW_ENABLE          =  _UNDERVOLTAGE_PROTECTION_BST_UVW_ENABLE(          252,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.UNDERVOLTAGE_PROTECTION_BST_Y2_ENABLE           =  _UNDERVOLTAGE_PROTECTION_BST_Y2_ENABLE(           253,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.OVERCURRENT_PROTECTION_UVW_LOW_SIDE_ENABLE      =  _OVERCURRENT_PROTECTION_UVW_LOW_SIDE_ENABLE(      254,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.OVERCURRENT_PROTECTION_UVW_HIGH_SIDE_ENABLE     =  _OVERCURRENT_PROTECTION_UVW_HIGH_SIDE_ENABLE(     255,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.OVERCURRENT_PROTECTION_Y2_LOW_SIDE_ENABLE       =  _OVERCURRENT_PROTECTION_Y2_LOW_SIDE_ENABLE(       256,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.OVERCURRENT_PROTECTION_Y2_HIGH_SIDE_ENABLE      =  _OVERCURRENT_PROTECTION_Y2_HIGH_SIDE_ENABLE(      257,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.OVERCURRENT_PROTECTION_UVW_LOW_SIDE_THRESHOLD   =  _OVERCURRENT_PROTECTION_UVW_LOW_SIDE_THRESHOLD(   258,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.OVERCURRENT_PROTECTION_UVW_HIGH_SIDE_THRESHOLD  =  _OVERCURRENT_PROTECTION_UVW_HIGH_SIDE_THRESHOLD(  259,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.OVERCURRENT_PROTECTION_Y2_LOW_SIDE_THRESHOLD    =  _OVERCURRENT_PROTECTION_Y2_LOW_SIDE_THRESHOLD(    260,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.OVERCURRENT_PROTECTION_Y2_HIGH_SIDE_THRESHOLD   =  _OVERCURRENT_PROTECTION_Y2_HIGH_SIDE_THRESHOLD(   261,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.OVERCURRENT_PROTECTION_UVW_LOW_SIDE_BLANKING    =  _OVERCURRENT_PROTECTION_UVW_LOW_SIDE_BLANKING(    262,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.OVERCURRENT_PROTECTION_UVW_HIGH_SIDE_BLANKING   =  _OVERCURRENT_PROTECTION_UVW_HIGH_SIDE_BLANKING(   263,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.OVERCURRENT_PROTECTION_Y2_LOW_SIDE_BLANKING     =  _OVERCURRENT_PROTECTION_Y2_LOW_SIDE_BLANKING(     264,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.OVERCURRENT_PROTECTION_Y2_HIGH_SIDE_BLANKING    =  _OVERCURRENT_PROTECTION_Y2_HIGH_SIDE_BLANKING(    265,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.OVERCURRENT_PROTECTION_UVW_LOW_SIDE_DEGLITCH    =  _OVERCURRENT_PROTECTION_UVW_LOW_SIDE_DEGLITCH(    266,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.OVERCURRENT_PROTECTION_UVW_HIGH_SIDE_DEGLITCH   =  _OVERCURRENT_PROTECTION_UVW_HIGH_SIDE_DEGLITCH(   267,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.OVERCURRENT_PROTECTION_Y2_LOW_SIDE_DEGLITCH     =  _OVERCURRENT_PROTECTION_Y2_LOW_SIDE_DEGLITCH(     268,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.OVERCURRENT_PROTECTION_Y2_HIGH_SIDE_DEGLITCH    =  _OVERCURRENT_PROTECTION_Y2_HIGH_SIDE_DEGLITCH(    269,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.OVERCURRENT_PROTECTION_UVW_LOW_SIDE_USE_VDS     =  _OVERCURRENT_PROTECTION_UVW_LOW_SIDE_USE_VDS(     270,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.OVERCURRENT_PROTECTION_Y2_LOW_SIDE_USE_VDS      =  _OVERCURRENT_PROTECTION_Y2_LOW_SIDE_USE_VDS(      271,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.VGS_SHORT_ON_PROTECTION_UVW_LOW_SIDE_ENABLE     =  _VGS_SHORT_ON_PROTECTION_UVW_LOW_SIDE_ENABLE(     272,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.VGS_SHORT_OFF_PROTECTION_UVW_LOW_SIDE_ENABLE    =  _VGS_SHORT_OFF_PROTECTION_UVW_LOW_SIDE_ENABLE(    273,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.VGS_SHORT_ON_PROTECTION_UVW_HIGH_SIDE_ENABLE    =  _VGS_SHORT_ON_PROTECTION_UVW_HIGH_SIDE_ENABLE(    274,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.VGS_SHORT_OFF_PROTECTION_UVW_HIGH_SIDE_ENABLE   =  _VGS_SHORT_OFF_PROTECTION_UVW_HIGH_SIDE_ENABLE(   275,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.VGS_SHORT_ON_PROTECTION_Y2_LOW_SIDE_ENABLE      =  _VGS_SHORT_ON_PROTECTION_Y2_LOW_SIDE_ENABLE(      276,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.VGS_SHORT_OFF_PROTECTION_Y2_LOW_SIDE_ENABLE     =  _VGS_SHORT_OFF_PROTECTION_Y2_LOW_SIDE_ENABLE(     277,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.VGS_SHORT_ON_PROTECTION_Y2_HIGH_SIDE_ENABLE     =  _VGS_SHORT_ON_PROTECTION_Y2_HIGH_SIDE_ENABLE(     278,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.VGS_SHORT_OFF_PROTECTION_Y2_HIGH_SIDE_ENABLE    =  _VGS_SHORT_OFF_PROTECTION_Y2_HIGH_SIDE_ENABLE(    279,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.VGS_SHORT_PROTECTION_UVW_BLANKING               =  _VGS_SHORT_PROTECTION_UVW_BLANKING(               280,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.VGS_SHORT_PROTECTION_Y2_BLANKING                =  _VGS_SHORT_PROTECTION_Y2_BLANKING(                281,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.VGS_SHORT_PROTECTION_UVW_DEGLITCH               =  _VGS_SHORT_PROTECTION_UVW_DEGLITCH(               282,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.VGS_SHORT_PROTECTION_Y2_DEGLITCH                =  _VGS_SHORT_PROTECTION_Y2_DEGLITCH(                283,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.GDRV_RETRY_BEHAVIOUR                            =  _GDRV_RETRY_BEHAVIOUR(                            286,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.DRIVE_FAULT_BEHAVIOUR                           =  _DRIVE_FAULT_BEHAVIOUR(                           287,  Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.FAULT_HANDLER_NUMBER_OF_RETRIES                 =  _FAULT_HANDLER_NUMBER_OF_RETRIES(                 288,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.GENERAL_STATUS_FLAGS                            =  _GENERAL_STATUS_FLAGS(                            289,  Parameter.Access.R,    Parameter.Datatype.FIELD)
        self.SUPPLY_VOLTAGE                                  =  _SUPPLY_VOLTAGE(                                  290,  Parameter.Access.R,    Parameter.Datatype.UNSIGNED)
        self.SUPPLY_OVERVOLTAGE_WARNING_THRESHOLD            =  _SUPPLY_OVERVOLTAGE_WARNING_THRESHOLD(            291,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.SUPPLY_UNDERVOLTAGE_WARNING_THRESHOLD           =  _SUPPLY_UNDERVOLTAGE_WARNING_THRESHOLD(           292,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.EXTERNAL_TEMPERATURE                            =  _EXTERNAL_TEMPERATURE(                            293,  Parameter.Access.R,    Parameter.Datatype.UNSIGNED)
        self.EXTERNAL_TEMPERATURE_SHUTDOWN_THRESHOLD         =  _EXTERNAL_TEMPERATURE_SHUTDOWN_THRESHOLD(         294,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.EXTERNAL_TEMPERATURE_WARNING_THRESHOLD          =  _EXTERNAL_TEMPERATURE_WARNING_THRESHOLD(          295,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.CHIP_TEMPERATURE                                =  _CHIP_TEMPERATURE(                                296,  Parameter.Access.R,    Parameter.Datatype.UNSIGNED)
        self.CHIP_TEMPERATURE_SHUTDOWN_THRESHOLD             =  _CHIP_TEMPERATURE_SHUTDOWN_THRESHOLD(             297,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.CHIP_TEMPERATURE_WARNING_THRESHOLD              =  _CHIP_TEMPERATURE_WARNING_THRESHOLD(              298,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.GENERAL_ERROR_FLAGS                             =  _GENERAL_ERROR_FLAGS(                             299,  Parameter.Access.R,    Parameter.Datatype.FIELD)
        self.GDRV_ERROR_FLAGS                                =  _GDRV_ERROR_FLAGS(                                300,  Parameter.Access.R,    Parameter.Datatype.FIELD)
        self.ADC_STATUS_FLAGS                                =  _ADC_STATUS_FLAGS(                                301,  Parameter.Access.R,    Parameter.Datatype.FIELD)
        self.MCC_INPUTS_RAW                                  =  _MCC_INPUTS_RAW(                                  304,  Parameter.Access.R,    Parameter.Datatype.UNSIGNED)
        self.FOC_VOLTAGE_UX                                  =  _FOC_VOLTAGE_UX(                                  305,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.FOC_VOLTAGE_WY                                  =  _FOC_VOLTAGE_WY(                                  306,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.FOC_VOLTAGE_V                                   =  _FOC_VOLTAGE_V(                                   307,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.FIELDWEAKENING_I                                =  _FIELDWEAKENING_I(                                308,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.FIELDWEAKENING_VOLTAGE_THRESHOLD                =  _FIELDWEAKENING_VOLTAGE_THRESHOLD(                310,  Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.FOC_CURRENT_UX                                  =  _FOC_CURRENT_UX(                                  311,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.FOC_CURRENT_V                                   =  _FOC_CURRENT_V(                                   312,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.FOC_CURRENT_WY                                  =  _FOC_CURRENT_WY(                                  313,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.FOC_VOLTAGE_UQ                                  =  _FOC_VOLTAGE_UQ(                                  314,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.FOC_CURRENT_IQ                                  =  _FOC_CURRENT_IQ(                                  315,  Parameter.Access.R,    Parameter.Datatype.SIGNED)
        self.TARGET_TORQUE_BIQUAD_FILTER_ENABLE              =  _TARGET_TORQUE_BIQUAD_FILTER_ENABLE(              318,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.TARGET_TORQUE_BIQUAD_FILTER_ACOEFF_1            =  _TARGET_TORQUE_BIQUAD_FILTER_ACOEFF_1(            319,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.TARGET_TORQUE_BIQUAD_FILTER_ACOEFF_2            =  _TARGET_TORQUE_BIQUAD_FILTER_ACOEFF_2(            320,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.TARGET_TORQUE_BIQUAD_FILTER_BCOEFF_0            =  _TARGET_TORQUE_BIQUAD_FILTER_BCOEFF_0(            321,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.TARGET_TORQUE_BIQUAD_FILTER_BCOEFF_1            =  _TARGET_TORQUE_BIQUAD_FILTER_BCOEFF_1(            322,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.TARGET_TORQUE_BIQUAD_FILTER_BCOEFF_2            =  _TARGET_TORQUE_BIQUAD_FILTER_BCOEFF_2(            323,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.ACTUAL_VELOCITY_BIQUAD_FILTER_ENABLE            =  _ACTUAL_VELOCITY_BIQUAD_FILTER_ENABLE(            324,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.ACTUAL_VELOCITY_BIQUAD_FILTER_ACOEFF_1          =  _ACTUAL_VELOCITY_BIQUAD_FILTER_ACOEFF_1(          325,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.ACTUAL_VELOCITY_BIQUAD_FILTER_ACOEFF_2          =  _ACTUAL_VELOCITY_BIQUAD_FILTER_ACOEFF_2(          326,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.ACTUAL_VELOCITY_BIQUAD_FILTER_BCOEFF_0          =  _ACTUAL_VELOCITY_BIQUAD_FILTER_BCOEFF_0(          327,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.ACTUAL_VELOCITY_BIQUAD_FILTER_BCOEFF_1          =  _ACTUAL_VELOCITY_BIQUAD_FILTER_BCOEFF_1(          328,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.ACTUAL_VELOCITY_BIQUAD_FILTER_BCOEFF_2          =  _ACTUAL_VELOCITY_BIQUAD_FILTER_BCOEFF_2(          329,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.TORQUE_FLUX_COMBINED_TARGET_VALUES              =  _TORQUE_FLUX_COMBINED_TARGET_VALUES(              330,  Parameter.Access.R,    Parameter.Datatype.UNSIGNED)
        self.TORQUE_FLUX_COMBINED_ACTUAL_VALUES              =  _TORQUE_FLUX_COMBINED_ACTUAL_VALUES(              331,  Parameter.Access.R,    Parameter.Datatype.UNSIGNED)
        self.VOLTAGE_D_Q_COMBINED_ACTUAL_VALUES              =  _VOLTAGE_D_Q_COMBINED_ACTUAL_VALUES(              332,  Parameter.Access.R,    Parameter.Datatype.UNSIGNED)
        self.INTEGRATED_ACTUAL_TORQUE_VALUE                  =  _INTEGRATED_ACTUAL_TORQUE_VALUE(                  333,  Parameter.Access.R,    Parameter.Datatype.UNSIGNED)
        self.INTEGRATED_ACTUAL_VELOCITY_VALUE                =  _INTEGRATED_ACTUAL_VELOCITY_VALUE(                334,  Parameter.Access.R,    Parameter.Datatype.UNSIGNED)


class _MOTOR_TYPE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.NO_MOTOR = 0
            self.DC_MOTOR = 1
            self.STEPPER_MOTOR = 2
            self.BLDC_MOTOR = 3

    def __init__(self, index, access, datatype):
        super().__init__("MOTOR_TYPE", index, access, datatype)

        self.choice = self._Choices()


class _MOTOR_POLE_PAIRS(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("MOTOR_POLE_PAIRS", index, access, datatype)

        self.choice = None


class _MOTOR_DIRECTION(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.NOT_INVERTED = False
            self.INVERTED = True

    def __init__(self, index, access, datatype):
        super().__init__("MOTOR_DIRECTION", index, access, datatype)

        self.choice = self._Choices()


class _MOTOR_PWM_FREQUENCY(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("MOTOR_PWM_FREQUENCY", index, access, datatype)

        self.choice = None


class _COMMUTATION_MODE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.SYSTEM_OFF = 0
            self.SYSTEM_OFF_LOW_SIDE_FETS_ON = 1
            self.SYSTEM_OFF_HIGH_SIDE_FETS_ON = 2
            self.FOC_OPENLOOP_VOLTAGE_MODE = 3
            self.FOC_OPENLOOP_CURRENT_MODE = 4
            self.FOC_ABN = 5
            self.FOC_HALL_SENSOR = 6
            self.RESERVED = 7
            self.FOC_SPI_ENC = 8

    def __init__(self, index, access, datatype):
        super().__init__("COMMUTATION_MODE", index, access, datatype)

        self.choice = self._Choices()


class _OUTPUT_VOLTAGE_LIMIT(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("OUTPUT_VOLTAGE_LIMIT", index, access, datatype)

        self.choice = None


class _MAX_TORQUE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("MAX_TORQUE", index, access, datatype)

        self.choice = None


class _MAX_FLUX(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("MAX_FLUX", index, access, datatype)

        self.choice = None


class _PWM_SWITCHING_SCHEME(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.STANDARD = 0
            self.SVPWM = 1
            self.FLAT_BOTTOM = 2

    def __init__(self, index, access, datatype):
        super().__init__("PWM_SWITCHING_SCHEME", index, access, datatype)

        self.choice = self._Choices()


class _IDLE_MOTOR_PWM_BEHAVIOR(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.PWM_ON_WHEN_MOTOR_IDLE = False
            self.PWM_OFF_WHEN_MOTOR_IDLE = True

    def __init__(self, index, access, datatype):
        super().__init__("IDLE_MOTOR_PWM_BEHAVIOR", index, access, datatype)

        self.choice = self._Choices()


class _ADC_SHUNT_TYPE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.INLINE_UVW = 0
            self.INLINE_VW = 1
            self.INLINE_UW = 2
            self.INLINE_UV = 3
            self.BOTTOM_SHUNTS = 4

    def __init__(self, index, access, datatype):
        super().__init__("ADC_SHUNT_TYPE", index, access, datatype)

        self.choice = self._Choices()


class _ADC_I0_RAW(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ADC_I0_RAW", index, access, datatype)

        self.choice = None


class _ADC_I1_RAW(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ADC_I1_RAW", index, access, datatype)

        self.choice = None


class _ADC_I2_RAW(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ADC_I2_RAW", index, access, datatype)

        self.choice = None


class _ADC_I3_RAW(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ADC_I3_RAW", index, access, datatype)

        self.choice = None


class _CSA_GAIN_ADC_I0_TO_ADC_I2(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.GAIN_5X = 0
            self.GAIN_10X = 1
            self.GAIN_20X = 2
            self.GAIN_40X = 3
            self.GAIN_1X_BYPASS_CSA = 4

    def __init__(self, index, access, datatype):
        super().__init__("CSA_GAIN_ADC_I0_TO_ADC_I2", index, access, datatype)

        self.choice = self._Choices()


class _CSA_GAIN_ADC_I3(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.GAIN_5X = 0
            self.GAIN_10X = 1
            self.GAIN_20X = 2
            self.GAIN_40X = 3
            self.GAIN_1X_BYPASS_CSA = 4

    def __init__(self, index, access, datatype):
        super().__init__("CSA_GAIN_ADC_I3", index, access, datatype)

        self.choice = self._Choices()


class _CSA_FILTER_ADC_I0_TO_ADC_I2(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.T_0_55_MICROSEC = 0
            self.T_0_75_MICROSEC = 1
            self.T_1_0_MICROSEC = 2
            self.T_1_35_MICROSEC = 3

    def __init__(self, index, access, datatype):
        super().__init__("CSA_FILTER_ADC_I0_TO_ADC_I2", index, access, datatype)

        self.choice = self._Choices()


class _CSA_FILTER_ADC_I3(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.T_0_55_MICROSEC = 0
            self.T_0_75_MICROSEC = 1
            self.T_1_0_MICROSEC = 2
            self.T_1_35_MICROSEC = 3

    def __init__(self, index, access, datatype):
        super().__init__("CSA_FILTER_ADC_I3", index, access, datatype)

        self.choice = self._Choices()


class _CURRENT_SCALING_FACTOR(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("CURRENT_SCALING_FACTOR", index, access, datatype)

        self.choice = None


class _PHASE_UX1_ADC_MAPPING(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.ADC_I0 = 0
            self.ADC_I1 = 1
            self.ADC_I2 = 2
            self.ADC_I3 = 3

    def __init__(self, index, access, datatype):
        super().__init__("PHASE_UX1_ADC_MAPPING", index, access, datatype)

        self.choice = self._Choices()


class _PHASE_VX2_ADC_MAPPING(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.ADC_I0 = 0
            self.ADC_I1 = 1
            self.ADC_I2 = 2
            self.ADC_I3 = 3

    def __init__(self, index, access, datatype):
        super().__init__("PHASE_VX2_ADC_MAPPING", index, access, datatype)

        self.choice = self._Choices()


class _PHASE_WY1_ADC_MAPPING(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.ADC_I0 = 0
            self.ADC_I1 = 1
            self.ADC_I2 = 2
            self.ADC_I3 = 3

    def __init__(self, index, access, datatype):
        super().__init__("PHASE_WY1_ADC_MAPPING", index, access, datatype)

        self.choice = self._Choices()


class _PHASE_Y2_ADC_MAPPING(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.ADC_I0 = 0
            self.ADC_I1 = 1
            self.ADC_I2 = 2
            self.ADC_I3 = 3

    def __init__(self, index, access, datatype):
        super().__init__("PHASE_Y2_ADC_MAPPING", index, access, datatype)

        self.choice = self._Choices()


class _ADC_I0_SCALE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ADC_I0_SCALE", index, access, datatype)

        self.choice = None


class _ADC_I1_SCALE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ADC_I1_SCALE", index, access, datatype)

        self.choice = None


class _ADC_I2_SCALE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ADC_I2_SCALE", index, access, datatype)

        self.choice = None


class _ADC_I3_SCALE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ADC_I3_SCALE", index, access, datatype)

        self.choice = None


class _ADC_I0_INVERTED(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.NOT_INVERTED = False
            self.INVERTED = True

    def __init__(self, index, access, datatype):
        super().__init__("ADC_I0_INVERTED", index, access, datatype)

        self.choice = self._Choices()


class _ADC_I1_INVERTED(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.NOT_INVERTED = False
            self.INVERTED = True

    def __init__(self, index, access, datatype):
        super().__init__("ADC_I1_INVERTED", index, access, datatype)

        self.choice = self._Choices()


class _ADC_I2_INVERTED(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.NOT_INVERTED = False
            self.INVERTED = True

    def __init__(self, index, access, datatype):
        super().__init__("ADC_I2_INVERTED", index, access, datatype)

        self.choice = self._Choices()


class _ADC_I3_INVERTED(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.NOT_INVERTED = False
            self.INVERTED = True

    def __init__(self, index, access, datatype):
        super().__init__("ADC_I3_INVERTED", index, access, datatype)

        self.choice = self._Choices()


class _ADC_I0_OFFSET(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ADC_I0_OFFSET", index, access, datatype)

        self.choice = None


class _ADC_I1_OFFSET(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ADC_I1_OFFSET", index, access, datatype)

        self.choice = None


class _ADC_I2_OFFSET(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ADC_I2_OFFSET", index, access, datatype)

        self.choice = None


class _ADC_I3_OFFSET(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ADC_I3_OFFSET", index, access, datatype)

        self.choice = None


class _ADC_I0(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ADC_I0", index, access, datatype)

        self.choice = None


class _ADC_I1(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ADC_I1", index, access, datatype)

        self.choice = None


class _ADC_I2(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ADC_I2", index, access, datatype)

        self.choice = None


class _ADC_I3(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ADC_I3", index, access, datatype)

        self.choice = None


class _OPENLOOP_ANGLE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("OPENLOOP_ANGLE", index, access, datatype)

        self.choice = None


class _OPENLOOP_CURRENT(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("OPENLOOP_CURRENT", index, access, datatype)

        self.choice = None


class _OPENLOOP_VOLTAGE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("OPENLOOP_VOLTAGE", index, access, datatype)

        self.choice = None


class _ACCELERATION_FF_GAIN(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ACCELERATION_FF_GAIN", index, access, datatype)

        self.choice = None


class _ACCELERATION_FF_SHIFT(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.NO_SHIFT = 0
            self.SHIFT_4_BIT = 1
            self.SHIFT_8_BIT = 2
            self.SHIFT_12_BIT = 3
            self.SHIFT_16_BIT = 4
            self.SHIFT_20_BIT = 5
            self.SHIFT_24_BIT = 6

    def __init__(self, index, access, datatype):
        super().__init__("ACCELERATION_FF_SHIFT", index, access, datatype)

        self.choice = self._Choices()


class _RAMP_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("RAMP_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _DIRECT_VELOCITY_MODE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("DIRECT_VELOCITY_MODE", index, access, datatype)

        self.choice = self._Choices()


class _RAMP_AMAX(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("RAMP_AMAX", index, access, datatype)

        self.choice = None


class _RAMP_A1(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("RAMP_A1", index, access, datatype)

        self.choice = None


class _RAMP_A2(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("RAMP_A2", index, access, datatype)

        self.choice = None


class _RAMP_DMAX(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("RAMP_DMAX", index, access, datatype)

        self.choice = None


class _RAMP_D1(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("RAMP_D1", index, access, datatype)

        self.choice = None


class _RAMP_D2(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("RAMP_D2", index, access, datatype)

        self.choice = None


class _RAMP_VMAX(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("RAMP_VMAX", index, access, datatype)

        self.choice = None


class _RAMP_V1(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("RAMP_V1", index, access, datatype)

        self.choice = None


class _RAMP_V2(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("RAMP_V2", index, access, datatype)

        self.choice = None


class _RAMP_VSTART(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("RAMP_VSTART", index, access, datatype)

        self.choice = None


class _RAMP_VSTOP(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("RAMP_VSTOP", index, access, datatype)

        self.choice = None


class _RAMP_TVMAX(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("RAMP_TVMAX", index, access, datatype)

        self.choice = None


class _RAMP_TZEROWAIT(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("RAMP_TZEROWAIT", index, access, datatype)

        self.choice = None


class _ACCELERATION_FEEDFORWARD_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("ACCELERATION_FEEDFORWARD_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _VELOCITY_FEEDFORWARD_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("VELOCITY_FEEDFORWARD_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _RAMP_VELOCITY(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("RAMP_VELOCITY", index, access, datatype)

        self.choice = None


class _RAMP_POSITION(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("RAMP_POSITION", index, access, datatype)

        self.choice = None


class _HALL_PHI_E(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("HALL_PHI_E", index, access, datatype)

        self.choice = None


class _HALL_SECTOR_OFFSET(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DEG_0 = 0
            self.DEG_60 = 1
            self.DEG_120 = 2
            self.DEG_180 = 3
            self.DEG_240 = 4
            self.DEG_300 = 5

    def __init__(self, index, access, datatype):
        super().__init__("HALL_SECTOR_OFFSET", index, access, datatype)

        self.choice = self._Choices()


class _HALL_FILTER_LENGTH(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("HALL_FILTER_LENGTH", index, access, datatype)

        self.choice = None


class _HALL_POSITION_0_OFFSET(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("HALL_POSITION_0_OFFSET", index, access, datatype)

        self.choice = None


class _HALL_POSITION_60_OFFSET(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("HALL_POSITION_60_OFFSET", index, access, datatype)

        self.choice = None


class _HALL_POSITION_120_OFFSET(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("HALL_POSITION_120_OFFSET", index, access, datatype)

        self.choice = None


class _HALL_POSITION_180_OFFSET(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("HALL_POSITION_180_OFFSET", index, access, datatype)

        self.choice = None


class _HALL_POSITION_240_OFFSET(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("HALL_POSITION_240_OFFSET", index, access, datatype)

        self.choice = None


class _HALL_POSITION_300_OFFSET(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("HALL_POSITION_300_OFFSET", index, access, datatype)

        self.choice = None


class _HALL_INVERT_DIRECTION(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.NOT_INVERTED = False
            self.INVERTED = True

    def __init__(self, index, access, datatype):
        super().__init__("HALL_INVERT_DIRECTION", index, access, datatype)

        self.choice = self._Choices()


class _HALL_EXTRAPOLATION_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("HALL_EXTRAPOLATION_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _HALL_PHI_E_OFFSET(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("HALL_PHI_E_OFFSET", index, access, datatype)

        self.choice = None


class _ABN_1_PHI_E(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ABN_1_PHI_E", index, access, datatype)

        self.choice = None


class _ABN_1_STEPS(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ABN_1_STEPS", index, access, datatype)

        self.choice = None


class _ABN_1_DIRECTION(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.NOT_INVERTED = False
            self.INVERTED = True

    def __init__(self, index, access, datatype):
        super().__init__("ABN_1_DIRECTION", index, access, datatype)

        self.choice = self._Choices()


class _ABN_1_INIT_METHOD(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.FORCED_PHI_E_ZERO_WITH_ACTIVE_SWING = 0
            self.FORCED_PHI_E_90_ZERO = 1
            self.USE_HALL = 2
            self.USE_N_CHANNEL_OFFSET = 3

    def __init__(self, index, access, datatype):
        super().__init__("ABN_1_INIT_METHOD", index, access, datatype)

        self.choice = self._Choices()


class _ABN_1_INIT_STATE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.IDLE = 0
            self.BUSY = 1
            self.WAIT = 2
            self.DONE = 3

    def __init__(self, index, access, datatype):
        super().__init__("ABN_1_INIT_STATE", index, access, datatype)

        self.choice = self._Choices()


class _ABN_1_INIT_DELAY(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ABN_1_INIT_DELAY", index, access, datatype)

        self.choice = None


class _ABN_1_INIT_VELOCITY(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ABN_1_INIT_VELOCITY", index, access, datatype)

        self.choice = None


class _ABN_1_N_CHANNEL_PHI_E_OFFSET(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ABN_1_N_CHANNEL_PHI_E_OFFSET", index, access, datatype)

        self.choice = None


class _ABN_1_N_CHANNEL_INVERTED(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.ACTIVE_HIGH = False
            self.ACTIVE_LOW = True

    def __init__(self, index, access, datatype):
        super().__init__("ABN_1_N_CHANNEL_INVERTED", index, access, datatype)

        self.choice = self._Choices()


class _ABN_1_N_CHANNEL_FILTERING(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.FILTERING_OFF = 0
            self.N_EVENT_ON_A_HIGH_B_HIGH = 1
            self.N_EVENT_ON_A_HIGH_B_LOW = 2
            self.N_EVENT_ON_A_LOW_B_HIGH = 3
            self.N_EVENT_ON_A_LOW_B_LOW = 4

    def __init__(self, index, access, datatype):
        super().__init__("ABN_1_N_CHANNEL_FILTERING", index, access, datatype)

        self.choice = self._Choices()


class _ABN_1_CLEAR_ON_NEXT_NULL(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("ABN_1_CLEAR_ON_NEXT_NULL", index, access, datatype)

        self.choice = self._Choices()


class _ABN_1_VALUE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ABN_1_VALUE", index, access, datatype)

        self.choice = None


class _TARGET_TORQUE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("TARGET_TORQUE", index, access, datatype)

        self.choice = None


class _ACTUAL_TORQUE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ACTUAL_TORQUE", index, access, datatype)

        self.choice = None


class _TARGET_FLUX(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("TARGET_FLUX", index, access, datatype)

        self.choice = None


class _ACTUAL_FLUX(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ACTUAL_FLUX", index, access, datatype)

        self.choice = None


class _TORQUE_OFFSET(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("TORQUE_OFFSET", index, access, datatype)

        self.choice = None


class _TORQUE_P(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("TORQUE_P", index, access, datatype)

        self.choice = None


class _TORQUE_I(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("TORQUE_I", index, access, datatype)

        self.choice = None


class _FLUX_P(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("FLUX_P", index, access, datatype)

        self.choice = None


class _FLUX_I(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("FLUX_I", index, access, datatype)

        self.choice = None


class _SEPARATE_TORQUE_FLUX_PI_PARAMTERS(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.TORQUE_FLUX_PI_COMBINED = False
            self.TORQUE_FLUX_PI_SEPARATED = True

    def __init__(self, index, access, datatype):
        super().__init__("SEPARATE_TORQUE_FLUX_PI_PARAMTERS", index, access, datatype)

        self.choice = self._Choices()


class _CURRENT_NORM_P(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.SHIFT_8_BIT = 0
            self.SHIFT_16_BIT = 1

    def __init__(self, index, access, datatype):
        super().__init__("CURRENT_NORM_P", index, access, datatype)

        self.choice = self._Choices()


class _CURRENT_NORM_I(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.SHIFT_8_BIT = 0
            self.SHIFT_16_BIT = 1

    def __init__(self, index, access, datatype):
        super().__init__("CURRENT_NORM_I", index, access, datatype)

        self.choice = self._Choices()


class _TORQUE_PI_ERROR(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("TORQUE_PI_ERROR", index, access, datatype)

        self.choice = None


class _FLUX_PI_ERROR(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("FLUX_PI_ERROR", index, access, datatype)

        self.choice = None


class _TORQUE_PI_INTEGRATOR(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("TORQUE_PI_INTEGRATOR", index, access, datatype)

        self.choice = None


class _FLUX_PI_INTEGRATOR(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("FLUX_PI_INTEGRATOR", index, access, datatype)

        self.choice = None


class _FLUX_OFFSET(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("FLUX_OFFSET", index, access, datatype)

        self.choice = None


class _VELOCITY_SENSOR_SELECTION(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.SAME_AS_COMMUTATION = 0
            self.DIGITAL_HALL = 1
            self.ABN1_ENCODER = 2
            self.ABN2_ENCODER = 3
            self.SPI_ENCODER = 4

    def __init__(self, index, access, datatype):
        super().__init__("VELOCITY_SENSOR_SELECTION", index, access, datatype)

        self.choice = self._Choices()


class _TARGET_VELOCITY(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("TARGET_VELOCITY", index, access, datatype)

        self.choice = None


class _ACTUAL_VELOCITY(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ACTUAL_VELOCITY", index, access, datatype)

        self.choice = None


class _VELOCITY_OFFSET(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("VELOCITY_OFFSET", index, access, datatype)

        self.choice = None


class _VELOCITY_P(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("VELOCITY_P", index, access, datatype)

        self.choice = None


class _VELOCITY_I(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("VELOCITY_I", index, access, datatype)

        self.choice = None


class _VELOCITY_NORM_P(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.NO_SHIFT = 0
            self.SHIFT_8_BIT = 1
            self.SHIFT_16_BIT = 2
            self.SHIFT_24_BIT = 3

    def __init__(self, index, access, datatype):
        super().__init__("VELOCITY_NORM_P", index, access, datatype)

        self.choice = self._Choices()


class _VELOCITY_NORM_I(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.SHIFT_8_BIT = 0
            self.SHIFT_16_BIT = 1
            self.SHIFT_24_BIT = 2
            self.SHIFT_32_BIT = 3

    def __init__(self, index, access, datatype):
        super().__init__("VELOCITY_NORM_I", index, access, datatype)

        self.choice = self._Choices()


class _VELOCITY_PI_INTEGRATOR(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("VELOCITY_PI_INTEGRATOR", index, access, datatype)

        self.choice = None


class _VELOCITY_PI_ERROR(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("VELOCITY_PI_ERROR", index, access, datatype)

        self.choice = None


class _VELOCITY_SCALING_FACTOR(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("VELOCITY_SCALING_FACTOR", index, access, datatype)

        self.choice = None


class _STOP_ON_VELOCITY_DEVIATION(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("STOP_ON_VELOCITY_DEVIATION", index, access, datatype)

        self.choice = None


class _VELOCITY_LOOP_DOWNSAMPLING(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("VELOCITY_LOOP_DOWNSAMPLING", index, access, datatype)

        self.choice = None


class _VELOCITY_REACHED_THRESHOLD(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("VELOCITY_REACHED_THRESHOLD", index, access, datatype)

        self.choice = None


class _VELOCITY_METER_SWITCH_THRESHOLD(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("VELOCITY_METER_SWITCH_THRESHOLD", index, access, datatype)

        self.choice = None


class _VELOCITY_METER_SWITCH_HYSTERESIS(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("VELOCITY_METER_SWITCH_HYSTERESIS", index, access, datatype)

        self.choice = None


class _VELOCITY_METER_MODE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.PERIOD_METER = 0
            self.FREQUENCY_METER = 1
            self.SOFTWARE_METER = 2

    def __init__(self, index, access, datatype):
        super().__init__("VELOCITY_METER_MODE", index, access, datatype)

        self.choice = self._Choices()


class _POSITION_SENSOR_SELECTION(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.SAME_AS_COMMUTATION = 0
            self.DIGITAL_HALL = 1
            self.ABN1_ENCODER = 2
            self.ABN2_ENCODER = 3
            self.SPI_ENCODER = 4

    def __init__(self, index, access, datatype):
        super().__init__("POSITION_SENSOR_SELECTION", index, access, datatype)

        self.choice = self._Choices()


class _TARGET_POSITION(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("TARGET_POSITION", index, access, datatype)

        self.choice = None


class _ACTUAL_POSITION(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ACTUAL_POSITION", index, access, datatype)

        self.choice = None


class _POSITION_SCALING_FACTOR(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("POSITION_SCALING_FACTOR", index, access, datatype)

        self.choice = None


class _POSITION_P(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("POSITION_P", index, access, datatype)

        self.choice = None


class _POSITION_I(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("POSITION_I", index, access, datatype)

        self.choice = None


class _POSITION_NORM_P(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.NO_SHIFT = 0
            self.SHIFT_8_BIT = 1
            self.SHIFT_16_BIT = 2
            self.SHIFT_24_BIT = 3

    def __init__(self, index, access, datatype):
        super().__init__("POSITION_NORM_P", index, access, datatype)

        self.choice = self._Choices()


class _POSITION_NORM_I(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.SHIFT_8_BIT = 0
            self.SHIFT_16_BIT = 1
            self.SHIFT_24_BIT = 2
            self.SHIFT_32_BIT = 3

    def __init__(self, index, access, datatype):
        super().__init__("POSITION_NORM_I", index, access, datatype)

        self.choice = self._Choices()


class _POSITION_PI_INTEGRATOR(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("POSITION_PI_INTEGRATOR", index, access, datatype)

        self.choice = None


class _POSITION_PI_ERROR(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("POSITION_PI_ERROR", index, access, datatype)

        self.choice = None


class _STOP_ON_POSITION_DEVIATION(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("STOP_ON_POSITION_DEVIATION", index, access, datatype)

        self.choice = None


class _POSITION_LOOP_DOWNSAMPLING(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("POSITION_LOOP_DOWNSAMPLING", index, access, datatype)

        self.choice = None


class _LATCH_POSITION(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("LATCH_POSITION", index, access, datatype)

        self.choice = None


class _POSITION_LIMIT_LOW(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("POSITION_LIMIT_LOW", index, access, datatype)

        self.choice = None


class _POSITION_LIMIT_HIGH(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("POSITION_LIMIT_HIGH", index, access, datatype)

        self.choice = None


class _POSITION_REACHED_THRESHOLD(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("POSITION_REACHED_THRESHOLD", index, access, datatype)

        self.choice = None


class _REFERENCE_SWITCH_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.NO_STOP_ON_SWITCH_TRIGGERED = 0
            self.STOP_ON_L = 1
            self.STOP_ON_R = 2
            self.STOP_ON_R_AND_L = 3
            self.STOP_ON_H = 4
            self.STOP_ON_H_AND_L = 5
            self.STOP_ON_H_AND_R = 6
            self.STOP_ON_H_R_AND_L = 7

    def __init__(self, index, access, datatype):
        super().__init__("REFERENCE_SWITCH_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _REFERENCE_SWITCH_POLARITY_AND_SWAP(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.NOT_SWAPPED_NOT_INVERTED = 0
            self.L_INVERTED = 1
            self.R_INVERTED = 2
            self.R_AND_L_INVERTED = 3
            self.H_INVERTED = 4
            self.H_AND_L_INVERTED = 5
            self.H_AND_R_INVERTED = 6
            self.H_R_AND_L_INVERTED = 7
            self.L_R_SWAPPED_L_INVERTED = 8
            self.L_R_SWAPPED_R_INVERTED = 9
            self.L_R_SWAPPED_R_AND_L_INVERTED = 10
            self.L_R_SWAPPED_H_INVERTED = 11
            self.L_R_SWAPPED_H_AND_L_INVERTED = 12
            self.L_R_SWAPPED = 13
            self.L_R_SWAPPED_H_AND_R_INVERTED = 14
            self.L_R_SWAPPED_H_R_AND_L_INVERTED = 15

    def __init__(self, index, access, datatype):
        super().__init__("REFERENCE_SWITCH_POLARITY_AND_SWAP", index, access, datatype)

        self.choice = self._Choices()


class _REFERENCE_SWITCH_LATCH_SETTINGS(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.NO_TRIGGER = 0
            self.L_R_RISING_EDGE = 1
            self.L_R_FALLING_EDGE = 2
            self.L_R_BOTH_EDGES = 3
            self.H_RISING_EDGE = 4
            self.H_L_R_RISING_EDGE = 5
            self.H_RISING_L_R_FALLING_EDGE = 6
            self.H_RISING_L_R_BOTH_EDGES = 7
            self.H_FALLING_EDGE = 8
            self.H_FALLING_L_R_RISING_EDGE = 9
            self.H_L_R_FALLING_EDGE = 10
            self.H_FALLING_L_R_BOTH_EDGES = 11
            self.H_BOTH_EDGES = 12
            self.H_BOTH_L_R_RISING_EDGE = 13
            self.H_BOTH_L_R_FALLING_EDGE = 14
            self.H_L_R_BOTH_EDGES = 15

    def __init__(self, index, access, datatype):
        super().__init__("REFERENCE_SWITCH_LATCH_SETTINGS", index, access, datatype)

        self.choice = self._Choices()


class _EVENT_STOP_SETTINGS(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DO_HARD_STOP = 0
            self.DO_SOFT_STOP = 1
            self.STOP_ON_POS_DEVIATION = 2
            self.STOP_ON_POS_DEVIATION_SOFT_STOP = 3
            self.STOP_ON_VEL_DEVIATION = 4
            self.STOP_ON_VEL_DEVIATION_SOFT_STOP = 5
            self.STOP_ON_POS_VEL_DEVIATION = 6
            self.STOP_ON_POS_VEL_DEVIATION_SOFT_STOP = 7

    def __init__(self, index, access, datatype):
        super().__init__("EVENT_STOP_SETTINGS", index, access, datatype)

        self.choice = self._Choices()


class _REFERENCE_SWITCH_SEARCH_MODE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.LEFT_SWITCH = 1
            self.RIGHT_SWITCH_LEFT_SWITCH = 2
            self.RIGHT_SWITCH_LEFT_SWITCH_BOTH_SIDES = 3
            self.LEFT_SWITCH_BOTH_SIDES = 4
            self.HOME_SWITCH_NEG_DIR_LEFT_END_SWITCH = 5
            self.HOME_SWITCH_POS_DIR_RIGHT_END_SWITCH = 6
            self.HOME_SWITCH_NEG_DIR_IGNORE_END_SWITCH = 7
            self.HOME_SWITCH_POS_DIR_IGNORE_END_SWITCH = 8

    def __init__(self, index, access, datatype):
        super().__init__("REFERENCE_SWITCH_SEARCH_MODE", index, access, datatype)

        self.choice = self._Choices()


class _REFERENCE_SWITCH_SEARCH_SPEED(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("REFERENCE_SWITCH_SEARCH_SPEED", index, access, datatype)

        self.choice = None


class _REFERENCE_SWITCH_SPEED(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("REFERENCE_SWITCH_SPEED", index, access, datatype)

        self.choice = None


class _RIGHT_LIMIT_SWITCH_POSITION(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("RIGHT_LIMIT_SWITCH_POSITION", index, access, datatype)

        self.choice = None


class _HOME_SWITCH_POSITION(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("HOME_SWITCH_POSITION", index, access, datatype)

        self.choice = None


class _LAST_REFERENCE_POSITION(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("LAST_REFERENCE_POSITION", index, access, datatype)

        self.choice = None


class _ABN_2_STEPS(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ABN_2_STEPS", index, access, datatype)

        self.choice = None


class _ABN_2_DIRECTION(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.NORMAL = False
            self.INVERTED = True

    def __init__(self, index, access, datatype):
        super().__init__("ABN_2_DIRECTION", index, access, datatype)

        self.choice = self._Choices()


class _ABN_2_GEAR_RATIO(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ABN_2_GEAR_RATIO", index, access, datatype)

        self.choice = None


class _ABN_2_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("ABN_2_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _ABN_2_VALUE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ABN_2_VALUE", index, access, datatype)

        self.choice = None


class _SPI_ENCODE_CS_SETTLE_DELAY_TIME(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SPI_ENCODE_CS_SETTLE_DELAY_TIME", index, access, datatype)

        self.choice = None


class _SPI_ENCODER_CS_IDLE_DELAY_TIME(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SPI_ENCODER_CS_IDLE_DELAY_TIME", index, access, datatype)

        self.choice = None


class _SPI_ENCODER_MAIN_TRANSFER_CMD_SIZE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SPI_ENCODER_MAIN_TRANSFER_CMD_SIZE", index, access, datatype)

        self.choice = None


class _SPI_ENCODER_SECONDARY_TRANSFER_CMD_SIZE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SPI_ENCODER_SECONDARY_TRANSFER_CMD_SIZE", index, access, datatype)

        self.choice = None


class _SPI_ENCODER_TRANSFER_DATA_3_0(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SPI_ENCODER_TRANSFER_DATA_3_0", index, access, datatype)

        self.choice = None


class _SPI_ENCODER_TRANSFER_DATA_7_4(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SPI_ENCODER_TRANSFER_DATA_7_4", index, access, datatype)

        self.choice = None


class _SPI_ENCODER_TRANSFER_DATA_11_8(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SPI_ENCODER_TRANSFER_DATA_11_8", index, access, datatype)

        self.choice = None


class _SPI_ENCODER_TRANSFER_DATA_15_12(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SPI_ENCODER_TRANSFER_DATA_15_12", index, access, datatype)

        self.choice = None


class _SPI_ENCODER_TRANSFER(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.OFF = 0
            self.TRIGGER_SINGLE_TRANSFER = 1
            self.CONTINUOUS_POSITION_COUNTER_READ = 2

    def __init__(self, index, access, datatype):
        super().__init__("SPI_ENCODER_TRANSFER", index, access, datatype)

        self.choice = self._Choices()


class _SPI_ENCODER_POSITION_COUNTER_MASK(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SPI_ENCODER_POSITION_COUNTER_MASK", index, access, datatype)

        self.choice = None


class _SPI_ENCODER_POSITION_COUNTER_SHIFT(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SPI_ENCODER_POSITION_COUNTER_SHIFT", index, access, datatype)

        self.choice = None


class _SPI_ENCODER_POSITION_COUNTER_VALUE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SPI_ENCODER_POSITION_COUNTER_VALUE", index, access, datatype)

        self.choice = None


class _SPI_ENCODER_COMMUTATION_ANGLE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SPI_ENCODER_COMMUTATION_ANGLE", index, access, datatype)

        self.choice = None


class _SPI_ENCODER_INITIALIZATION_METHOD(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.FORCED_PHI_E_ZERO_WITH_ACTIVE_SWING = 0
            self.FORCED_PHI_E_90_ZERO = 1
            self.USE_OFFSET = 2

    def __init__(self, index, access, datatype):
        super().__init__("SPI_ENCODER_INITIALIZATION_METHOD", index, access, datatype)

        self.choice = self._Choices()


class _SPI_ENCODER_DIRECTION(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.NOT_INVERTED = False
            self.INVERTED = True

    def __init__(self, index, access, datatype):
        super().__init__("SPI_ENCODER_DIRECTION", index, access, datatype)

        self.choice = self._Choices()


class _SPI_ENCODER_OFFSET(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SPI_ENCODER_OFFSET", index, access, datatype)

        self.choice = None


class _SPI_LUT_CORRECTION_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("SPI_LUT_CORRECTION_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _SPI_LUT_ADDRESS_SELECT(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SPI_LUT_ADDRESS_SELECT", index, access, datatype)

        self.choice = None


class _SPI_LUT_DATA(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SPI_LUT_DATA", index, access, datatype)

        self.choice = None


class _SPI_LUT_COMMON_SHIFT_FACTOR(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SPI_LUT_COMMON_SHIFT_FACTOR", index, access, datatype)

        self.choice = None


class _STEP_DIR_STEP_DIVIDER_SHIFT(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.STEP_MODE_FULL = 0
            self.STEP_MODE_HALF = 1
            self.STEP_MODE_QUARTER = 2
            self.STEP_MODE_1_8TH = 3
            self.STEP_MODE_1_16TH = 4
            self.STEP_MODE_1_32ND = 5
            self.STEP_MODE_1_64TH = 6
            self.STEP_MODE_1_128TH = 7
            self.STEP_MODE_1_256TH = 8
            self.STEP_MODE_1_512TH = 9
            self.STEP_MODE_1_1024TH = 10

    def __init__(self, index, access, datatype):
        super().__init__("STEP_DIR_STEP_DIVIDER_SHIFT", index, access, datatype)

        self.choice = self._Choices()


class _STEP_DIR_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("STEP_DIR_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _STEP_DIR_EXTRAPOLATION_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("STEP_DIR_EXTRAPOLATION_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _STEP_DIR_STEP_SIGNAL_TIMEOUT_LIMIT(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("STEP_DIR_STEP_SIGNAL_TIMEOUT_LIMIT", index, access, datatype)

        self.choice = None


class _STEP_DIR_MAXIMUM_EXTRAPOLATION_VELOCITY(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("STEP_DIR_MAXIMUM_EXTRAPOLATION_VELOCITY", index, access, datatype)

        self.choice = None


class _BRAKE_CHOPPER_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("BRAKE_CHOPPER_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _BRAKE_CHOPPER_VOLTAGE_LIMIT(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("BRAKE_CHOPPER_VOLTAGE_LIMIT", index, access, datatype)

        self.choice = None


class _BRAKE_CHOPPER_HYSTERESIS(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("BRAKE_CHOPPER_HYSTERESIS", index, access, datatype)

        self.choice = None


class _RELEASE_BRAKE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.BRAKE_PWM_DEACTIVATED = False
            self.BRAKE_PWM_ACTIVATED = True

    def __init__(self, index, access, datatype):
        super().__init__("RELEASE_BRAKE", index, access, datatype)

        self.choice = self._Choices()


class _BRAKE_RELEASING_DUTY_CYCLE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("BRAKE_RELEASING_DUTY_CYCLE", index, access, datatype)

        self.choice = None


class _BRAKE_HOLDING_DUTY_CYCLE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("BRAKE_HOLDING_DUTY_CYCLE", index, access, datatype)

        self.choice = None


class _BRAKE_RELEASING_DURATION(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("BRAKE_RELEASING_DURATION", index, access, datatype)

        self.choice = None


class _INVERT_BRAKE_OUTPUT(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.NORMAL = False
            self.INVERTED = True

    def __init__(self, index, access, datatype):
        super().__init__("INVERT_BRAKE_OUTPUT", index, access, datatype)

        self.choice = self._Choices()


class _THERMAL_WINDING_TIME_CONSTANT_1(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("THERMAL_WINDING_TIME_CONSTANT_1", index, access, datatype)

        self.choice = None


class _IIT_LIMIT_1(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("IIT_LIMIT_1", index, access, datatype)

        self.choice = None


class _IIT_SUM_1(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("IIT_SUM_1", index, access, datatype)

        self.choice = None


class _THERMAL_WINDING_TIME_CONSTANT_2(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("THERMAL_WINDING_TIME_CONSTANT_2", index, access, datatype)

        self.choice = None


class _IIT_LIMIT_2(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("IIT_LIMIT_2", index, access, datatype)

        self.choice = None


class _IIT_SUM_2(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("IIT_SUM_2", index, access, datatype)

        self.choice = None


class _RESET_IIT_SUMS(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("RESET_IIT_SUMS", index, access, datatype)

        self.choice = None


class _ACTUAL_TOTAL_MOTOR_CURRENT(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ACTUAL_TOTAL_MOTOR_CURRENT", index, access, datatype)

        self.choice = None


class _PWM_L_OUTPUT_POLARITY(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.ACTIVE_HIGH = False
            self.ACTIVE_LOW = True

    def __init__(self, index, access, datatype):
        super().__init__("PWM_L_OUTPUT_POLARITY", index, access, datatype)

        self.choice = self._Choices()


class _PWM_H_OUTPUT_POLARITY(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.ACTIVE_HIGH = False
            self.ACTIVE_LOW = True

    def __init__(self, index, access, datatype):
        super().__init__("PWM_H_OUTPUT_POLARITY", index, access, datatype)

        self.choice = self._Choices()


class _BREAK_BEFORE_MAKE_TIME_LOW_UVW(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("BREAK_BEFORE_MAKE_TIME_LOW_UVW", index, access, datatype)

        self.choice = None


class _BREAK_BEFORE_MAKE_TIME_HIGH_UVW(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("BREAK_BEFORE_MAKE_TIME_HIGH_UVW", index, access, datatype)

        self.choice = None


class _BREAK_BEFORE_MAKE_TIME_LOW_Y2(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("BREAK_BEFORE_MAKE_TIME_LOW_Y2", index, access, datatype)

        self.choice = None


class _BREAK_BEFORE_MAKE_TIME_HIGH_Y2(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("BREAK_BEFORE_MAKE_TIME_HIGH_Y2", index, access, datatype)

        self.choice = None


class _USE_ADAPTIVE_DRIVE_TIME_UVW(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("USE_ADAPTIVE_DRIVE_TIME_UVW", index, access, datatype)

        self.choice = self._Choices()


class _USE_ADAPTIVE_DRIVE_TIME_Y2(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("USE_ADAPTIVE_DRIVE_TIME_Y2", index, access, datatype)

        self.choice = self._Choices()


class _DRIVE_TIME_SINK_UVW(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("DRIVE_TIME_SINK_UVW", index, access, datatype)

        self.choice = None


class _DRIVE_TIME_SOURCE_UVW(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("DRIVE_TIME_SOURCE_UVW", index, access, datatype)

        self.choice = None


class _DRIVE_TIME_SINK_Y2(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("DRIVE_TIME_SINK_Y2", index, access, datatype)

        self.choice = None


class _DRIVE_TIME_SOURCE_Y2(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("DRIVE_TIME_SOURCE_Y2", index, access, datatype)

        self.choice = None


class _UVW_SINK_CURRENT(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.CUR_50_MILLIAMP = 0
            self.CUR_100_MILLIAMP = 1
            self.CUR_160_MILLIAMP = 2
            self.CUR_210_MILLIAMP = 3
            self.CUR_270_MILLIAMP = 4
            self.CUR_320_MILLIAMP = 5
            self.CUR_380_MILLIAMP = 6
            self.CUR_430_MILLIAMP = 7
            self.CUR_580_MILLIAMP = 8
            self.CUR_720_MILLIAMP = 9
            self.CUR_860_MILLIAMP = 10
            self.CUR_1000_MILLIAMP = 11
            self.CUR_1250_MILLIAMP = 12
            self.CUR_1510_MILLIAMP = 13
            self.CUR_1770_MILLIAMP = 14
            self.CUR_2000_MILLIAMP = 15

    def __init__(self, index, access, datatype):
        super().__init__("UVW_SINK_CURRENT", index, access, datatype)

        self.choice = self._Choices()


class _UVW_SOURCE_CURRENT(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.CUR_25_MILLIAMP = 0
            self.CUR_50_MILLIAMP = 1
            self.CUR_80_MILLIAMP = 2
            self.CUR_105_MILLIAMP = 3
            self.CUR_135_MILLIAMP = 4
            self.CUR_160_MILLIAMP = 5
            self.CUR_190_MILLIAMP = 6
            self.CUR_215_MILLIAMP = 7
            self.CUR_290_MILLIAMP = 8
            self.CUR_360_MILLIAMP = 9
            self.CUR_430_MILLIAMP = 10
            self.CUR_500_MILLIAMP = 11
            self.CUR_625_MILLIAMP = 12
            self.CUR_755_MILLIAMP = 13
            self.CUR_855_MILLIAMP = 14
            self.CUR_1000_MILLIAMP = 15

    def __init__(self, index, access, datatype):
        super().__init__("UVW_SOURCE_CURRENT", index, access, datatype)

        self.choice = self._Choices()


class _Y2_SINK_CURRENT(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.CUR_50_MILLIAMP = 0
            self.CUR_100_MILLIAMP = 1
            self.CUR_160_MILLIAMP = 2
            self.CUR_210_MILLIAMP = 3
            self.CUR_270_MILLIAMP = 4
            self.CUR_320_MILLIAMP = 5
            self.CUR_380_MILLIAMP = 6
            self.CUR_430_MILLIAMP = 7
            self.CUR_580_MILLIAMP = 8
            self.CUR_720_MILLIAMP = 9
            self.CUR_860_MILLIAMP = 10
            self.CUR_1000_MILLIAMP = 11
            self.CUR_1250_MILLIAMP = 12
            self.CUR_1510_MILLIAMP = 13
            self.CUR_1770_MILLIAMP = 14
            self.CUR_2000_MILLIAMP = 15

    def __init__(self, index, access, datatype):
        super().__init__("Y2_SINK_CURRENT", index, access, datatype)

        self.choice = self._Choices()


class _Y2_SOURCE_CURRENT(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.CUR_25_MILLIAMP = 0
            self.CUR_50_MILLIAMP = 1
            self.CUR_80_MILLIAMP = 2
            self.CUR_105_MILLIAMP = 3
            self.CUR_135_MILLIAMP = 4
            self.CUR_160_MILLIAMP = 5
            self.CUR_190_MILLIAMP = 6
            self.CUR_215_MILLIAMP = 7
            self.CUR_290_MILLIAMP = 8
            self.CUR_360_MILLIAMP = 9
            self.CUR_430_MILLIAMP = 10
            self.CUR_500_MILLIAMP = 11
            self.CUR_625_MILLIAMP = 12
            self.CUR_755_MILLIAMP = 13
            self.CUR_855_MILLIAMP = 14
            self.CUR_1000_MILLIAMP = 15

    def __init__(self, index, access, datatype):
        super().__init__("Y2_SOURCE_CURRENT", index, access, datatype)

        self.choice = self._Choices()


class _BOOTSTRAP_CURRENT_LIMIT(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.CUR_45_MILLIAMP = 0
            self.CUR_91_MILLIAMP = 1
            self.CUR_141_MILLIAMP = 2
            self.CUR_191_MILLIAMP = 3
            self.CUR_267_MILLIAMP = 4
            self.CUR_292_MILLIAMP = 5
            self.CUR_341_MILLIAMP = 6
            self.CUR_391_MILLIAMP = 7

    def __init__(self, index, access, datatype):
        super().__init__("BOOTSTRAP_CURRENT_LIMIT", index, access, datatype)

        self.choice = self._Choices()


class _UNDERVOLTAGE_PROTECTION_SUPPLY_LEVEL(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("UNDERVOLTAGE_PROTECTION_SUPPLY_LEVEL", index, access, datatype)

        self.choice = None


class _UNDERVOLTAGE_PROTECTION_VDRV_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("UNDERVOLTAGE_PROTECTION_VDRV_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _UNDERVOLTAGE_PROTECTION_BST_UVW_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("UNDERVOLTAGE_PROTECTION_BST_UVW_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _UNDERVOLTAGE_PROTECTION_BST_Y2_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("UNDERVOLTAGE_PROTECTION_BST_Y2_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _OVERCURRENT_PROTECTION_UVW_LOW_SIDE_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("OVERCURRENT_PROTECTION_UVW_LOW_SIDE_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _OVERCURRENT_PROTECTION_UVW_HIGH_SIDE_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("OVERCURRENT_PROTECTION_UVW_HIGH_SIDE_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _OVERCURRENT_PROTECTION_Y2_LOW_SIDE_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("OVERCURRENT_PROTECTION_Y2_LOW_SIDE_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _OVERCURRENT_PROTECTION_Y2_HIGH_SIDE_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("OVERCURRENT_PROTECTION_Y2_HIGH_SIDE_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _OVERCURRENT_PROTECTION_UVW_LOW_SIDE_THRESHOLD(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.V_80_OR_63_MILLIVOLT = 0
            self.V_165_OR_125_MILLIVOLT = 1
            self.V_250_OR_187_MILLIVOLT = 2
            self.V_330_OR_248_MILLIVOLT = 3
            self.V_415_OR_312_MILLIVOLT = 4
            self.V_500_OR_374_MILLIVOLT = 5
            self.V_582_OR_434_MILLIVOLT = 6
            self.V_660_OR_504_MILLIVOLT = 7
            self.V_125_OR_705_MILLIVOLT = 8
            self.V_250_OR_940_MILLIVOLT = 9
            self.V_375_OR_1180_MILLIVOLT = 10
            self.V_500_OR_1410_MILLIVOLT = 11
            self.V_625_OR_1650_MILLIVOLT = 12
            self.V_750_OR_1880_MILLIVOLT = 13
            self.V_875_OR_2110_MILLIVOLT = 14
            self.V_1000_OR_2350_MILLIVOLT = 15

    def __init__(self, index, access, datatype):
        super().__init__("OVERCURRENT_PROTECTION_UVW_LOW_SIDE_THRESHOLD", index, access, datatype)

        self.choice = self._Choices()


class _OVERCURRENT_PROTECTION_UVW_HIGH_SIDE_THRESHOLD(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.V_63_MILLIVOLT = 0
            self.V_125_MILLIVOLT = 1
            self.V_187_MILLIVOLT = 2
            self.V_248_MILLIVOLT = 3
            self.V_312_MILLIVOLT = 4
            self.V_374_MILLIVOLT = 5
            self.V_434_MILLIVOLT = 6
            self.V_504_MILLIVOLT = 7
            self.V_705_MILLIVOLT = 8
            self.V_940_MILLIVOLT = 9
            self.V_1180_MILLIVOLT = 10
            self.V_1410_MILLIVOLT = 11
            self.V_1650_MILLIVOLT = 12
            self.V_1880_MILLIVOLT = 13
            self.V_2110_MILLIVOLT = 14
            self.V_2350_MILLIVOLT = 15

    def __init__(self, index, access, datatype):
        super().__init__("OVERCURRENT_PROTECTION_UVW_HIGH_SIDE_THRESHOLD", index, access, datatype)

        self.choice = self._Choices()


class _OVERCURRENT_PROTECTION_Y2_LOW_SIDE_THRESHOLD(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.V_80_OR_63_MILLIVOLT = 0
            self.V_165_OR_125_MILLIVOLT = 1
            self.V_250_OR_187_MILLIVOLT = 2
            self.V_330_OR_248_MILLIVOLT = 3
            self.V_415_OR_312_MILLIVOLT = 4
            self.V_500_OR_374_MILLIVOLT = 5
            self.V_582_OR_434_MILLIVOLT = 6
            self.V_660_OR_504_MILLIVOLT = 7
            self.V_125_OR_705_MILLIVOLT = 8
            self.V_250_OR_940_MILLIVOLT = 9
            self.V_375_OR_1180_MILLIVOLT = 10
            self.V_500_OR_1410_MILLIVOLT = 11
            self.V_625_OR_1650_MILLIVOLT = 12
            self.V_750_OR_1880_MILLIVOLT = 13
            self.V_875_OR_2110_MILLIVOLT = 14
            self.V_1000_OR_2350_MILLIVOLT = 15

    def __init__(self, index, access, datatype):
        super().__init__("OVERCURRENT_PROTECTION_Y2_LOW_SIDE_THRESHOLD", index, access, datatype)

        self.choice = self._Choices()


class _OVERCURRENT_PROTECTION_Y2_HIGH_SIDE_THRESHOLD(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.V_63_MILLIVOLT = 0
            self.V_125_MILLIVOLT = 1
            self.V_187_MILLIVOLT = 2
            self.V_248_MILLIVOLT = 3
            self.V_312_MILLIVOLT = 4
            self.V_374_MILLIVOLT = 5
            self.V_434_MILLIVOLT = 6
            self.V_504_MILLIVOLT = 7
            self.V_705_MILLIVOLT = 8
            self.V_940_MILLIVOLT = 9
            self.V_1180_MILLIVOLT = 10
            self.V_1410_MILLIVOLT = 11
            self.V_1650_MILLIVOLT = 12
            self.V_1880_MILLIVOLT = 13
            self.V_2110_MILLIVOLT = 14
            self.V_2350_MILLIVOLT = 15

    def __init__(self, index, access, datatype):
        super().__init__("OVERCURRENT_PROTECTION_Y2_HIGH_SIDE_THRESHOLD", index, access, datatype)

        self.choice = self._Choices()


class _OVERCURRENT_PROTECTION_UVW_LOW_SIDE_BLANKING(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.OFF = 0
            self.T_0_25_MICROSEC = 1
            self.T_0_5_MICROSEC = 2
            self.T_1_MICROSEC = 3
            self.T_2_MICROSEC = 4
            self.T_4_MICROSEC = 5
            self.T_6_MICROSEC = 6
            self.T_8_MICROSEC = 7

    def __init__(self, index, access, datatype):
        super().__init__("OVERCURRENT_PROTECTION_UVW_LOW_SIDE_BLANKING", index, access, datatype)

        self.choice = self._Choices()


class _OVERCURRENT_PROTECTION_UVW_HIGH_SIDE_BLANKING(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.OFF = 0
            self.T_0_25_MICROSEC = 1
            self.T_0_5_MICROSEC = 2
            self.T_1_MICROSEC = 3
            self.T_2_MICROSEC = 4
            self.T_4_MICROSEC = 5
            self.T_6_MICROSEC = 6
            self.T_8_MICROSEC = 7

    def __init__(self, index, access, datatype):
        super().__init__("OVERCURRENT_PROTECTION_UVW_HIGH_SIDE_BLANKING", index, access, datatype)

        self.choice = self._Choices()


class _OVERCURRENT_PROTECTION_Y2_LOW_SIDE_BLANKING(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.OFF = 0
            self.T_0_25_MICROSEC = 1
            self.T_0_5_MICROSEC = 2
            self.T_1_MICROSEC = 3
            self.T_2_MICROSEC = 4
            self.T_4_MICROSEC = 5
            self.T_6_MICROSEC = 6
            self.T_8_MICROSEC = 7

    def __init__(self, index, access, datatype):
        super().__init__("OVERCURRENT_PROTECTION_Y2_LOW_SIDE_BLANKING", index, access, datatype)

        self.choice = self._Choices()


class _OVERCURRENT_PROTECTION_Y2_HIGH_SIDE_BLANKING(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.OFF = 0
            self.T_0_25_MICROSEC = 1
            self.T_0_5_MICROSEC = 2
            self.T_1_MICROSEC = 3
            self.T_2_MICROSEC = 4
            self.T_4_MICROSEC = 5
            self.T_6_MICROSEC = 6
            self.T_8_MICROSEC = 7

    def __init__(self, index, access, datatype):
        super().__init__("OVERCURRENT_PROTECTION_Y2_HIGH_SIDE_BLANKING", index, access, datatype)

        self.choice = self._Choices()


class _OVERCURRENT_PROTECTION_UVW_LOW_SIDE_DEGLITCH(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.OFF = 0
            self.T_0_25_MICROSEC = 1
            self.T_0_5_MICROSEC = 2
            self.T_1_MICROSEC = 3
            self.T_2_MICROSEC = 4
            self.T_4_MICROSEC = 5
            self.T_6_MICROSEC = 6
            self.T_8_MICROSEC = 7

    def __init__(self, index, access, datatype):
        super().__init__("OVERCURRENT_PROTECTION_UVW_LOW_SIDE_DEGLITCH", index, access, datatype)

        self.choice = self._Choices()


class _OVERCURRENT_PROTECTION_UVW_HIGH_SIDE_DEGLITCH(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.OFF = 0
            self.T_0_25_MICROSEC = 1
            self.T_0_5_MICROSEC = 2
            self.T_1_MICROSEC = 3
            self.T_2_MICROSEC = 4
            self.T_4_MICROSEC = 5
            self.T_6_MICROSEC = 6
            self.T_8_MICROSEC = 7

    def __init__(self, index, access, datatype):
        super().__init__("OVERCURRENT_PROTECTION_UVW_HIGH_SIDE_DEGLITCH", index, access, datatype)

        self.choice = self._Choices()


class _OVERCURRENT_PROTECTION_Y2_LOW_SIDE_DEGLITCH(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.OFF = 0
            self.T_0_25_MICROSEC = 1
            self.T_0_5_MICROSEC = 2
            self.T_1_MICROSEC = 3
            self.T_2_MICROSEC = 4
            self.T_4_MICROSEC = 5
            self.T_6_MICROSEC = 6
            self.T_8_MICROSEC = 7

    def __init__(self, index, access, datatype):
        super().__init__("OVERCURRENT_PROTECTION_Y2_LOW_SIDE_DEGLITCH", index, access, datatype)

        self.choice = self._Choices()


class _OVERCURRENT_PROTECTION_Y2_HIGH_SIDE_DEGLITCH(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.OFF = 0
            self.T_0_25_MICROSEC = 1
            self.T_0_5_MICROSEC = 2
            self.T_1_MICROSEC = 3
            self.T_2_MICROSEC = 4
            self.T_4_MICROSEC = 5
            self.T_6_MICROSEC = 6
            self.T_8_MICROSEC = 7

    def __init__(self, index, access, datatype):
        super().__init__("OVERCURRENT_PROTECTION_Y2_HIGH_SIDE_DEGLITCH", index, access, datatype)

        self.choice = self._Choices()


class _OVERCURRENT_PROTECTION_UVW_LOW_SIDE_USE_VDS(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("OVERCURRENT_PROTECTION_UVW_LOW_SIDE_USE_VDS", index, access, datatype)

        self.choice = self._Choices()


class _OVERCURRENT_PROTECTION_Y2_LOW_SIDE_USE_VDS(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("OVERCURRENT_PROTECTION_Y2_LOW_SIDE_USE_VDS", index, access, datatype)

        self.choice = self._Choices()


class _VGS_SHORT_ON_PROTECTION_UVW_LOW_SIDE_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("VGS_SHORT_ON_PROTECTION_UVW_LOW_SIDE_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _VGS_SHORT_OFF_PROTECTION_UVW_LOW_SIDE_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("VGS_SHORT_OFF_PROTECTION_UVW_LOW_SIDE_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _VGS_SHORT_ON_PROTECTION_UVW_HIGH_SIDE_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("VGS_SHORT_ON_PROTECTION_UVW_HIGH_SIDE_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _VGS_SHORT_OFF_PROTECTION_UVW_HIGH_SIDE_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("VGS_SHORT_OFF_PROTECTION_UVW_HIGH_SIDE_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _VGS_SHORT_ON_PROTECTION_Y2_LOW_SIDE_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("VGS_SHORT_ON_PROTECTION_Y2_LOW_SIDE_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _VGS_SHORT_OFF_PROTECTION_Y2_LOW_SIDE_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("VGS_SHORT_OFF_PROTECTION_Y2_LOW_SIDE_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _VGS_SHORT_ON_PROTECTION_Y2_HIGH_SIDE_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("VGS_SHORT_ON_PROTECTION_Y2_HIGH_SIDE_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _VGS_SHORT_OFF_PROTECTION_Y2_HIGH_SIDE_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("VGS_SHORT_OFF_PROTECTION_Y2_HIGH_SIDE_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _VGS_SHORT_PROTECTION_UVW_BLANKING(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.OFF = 0
            self.T_0_25_MICROSEC = 1
            self.T_0_5_MICROSEC = 2
            self.T_1_MICROSEC = 3

    def __init__(self, index, access, datatype):
        super().__init__("VGS_SHORT_PROTECTION_UVW_BLANKING", index, access, datatype)

        self.choice = self._Choices()


class _VGS_SHORT_PROTECTION_Y2_BLANKING(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.OFF = 0
            self.T_0_25_MICROSEC = 1
            self.T_0_5_MICROSEC = 2
            self.T_1_MICROSEC = 3

    def __init__(self, index, access, datatype):
        super().__init__("VGS_SHORT_PROTECTION_Y2_BLANKING", index, access, datatype)

        self.choice = self._Choices()


class _VGS_SHORT_PROTECTION_UVW_DEGLITCH(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.OFF = 0
            self.T_0_25_MICROSEC = 1
            self.T_0_5_MICROSEC = 2
            self.T_1_MICROSEC = 3
            self.T_2_MICROSEC = 4
            self.T_4_MICROSEC = 5
            self.T_6_MICROSEC = 6
            self.T_8_MICROSEC = 7

    def __init__(self, index, access, datatype):
        super().__init__("VGS_SHORT_PROTECTION_UVW_DEGLITCH", index, access, datatype)

        self.choice = self._Choices()


class _VGS_SHORT_PROTECTION_Y2_DEGLITCH(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.OFF = 0
            self.T_0_25_MICROSEC = 1
            self.T_0_5_MICROSEC = 2
            self.T_1_MICROSEC = 3
            self.T_2_MICROSEC = 4
            self.T_4_MICROSEC = 5
            self.T_6_MICROSEC = 6
            self.T_8_MICROSEC = 7

    def __init__(self, index, access, datatype):
        super().__init__("VGS_SHORT_PROTECTION_Y2_DEGLITCH", index, access, datatype)

        self.choice = self._Choices()


class _GDRV_RETRY_BEHAVIOUR(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.OPEN_CIRCUIT = 0
            self.ELECTRICAL_BRAKING = 1

    def __init__(self, index, access, datatype):
        super().__init__("GDRV_RETRY_BEHAVIOUR", index, access, datatype)

        self.choice = self._Choices()


class _DRIVE_FAULT_BEHAVIOUR(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.OPEN_CIRCUIT = 0
            self.ELECTRICAL_BRAKING = 1
            self.MECHANICAL_BRAKING_AND_OPEN_CIRCUIT = 2
            self.MECHANICAL_AND_ELECTRICAL_BRAKING = 3

    def __init__(self, index, access, datatype):
        super().__init__("DRIVE_FAULT_BEHAVIOUR", index, access, datatype)

        self.choice = self._Choices()


class _FAULT_HANDLER_NUMBER_OF_RETRIES(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("FAULT_HANDLER_NUMBER_OF_RETRIES", index, access, datatype)

        self.choice = None


class _GENERAL_STATUS_FLAGS(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("GENERAL_STATUS_FLAGS", index, access, datatype)

        self.choice = None


class _SUPPLY_VOLTAGE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SUPPLY_VOLTAGE", index, access, datatype)

        self.choice = None


class _SUPPLY_OVERVOLTAGE_WARNING_THRESHOLD(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SUPPLY_OVERVOLTAGE_WARNING_THRESHOLD", index, access, datatype)

        self.choice = None


class _SUPPLY_UNDERVOLTAGE_WARNING_THRESHOLD(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SUPPLY_UNDERVOLTAGE_WARNING_THRESHOLD", index, access, datatype)

        self.choice = None


class _EXTERNAL_TEMPERATURE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("EXTERNAL_TEMPERATURE", index, access, datatype)

        self.choice = None


class _EXTERNAL_TEMPERATURE_SHUTDOWN_THRESHOLD(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("EXTERNAL_TEMPERATURE_SHUTDOWN_THRESHOLD", index, access, datatype)

        self.choice = None


class _EXTERNAL_TEMPERATURE_WARNING_THRESHOLD(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("EXTERNAL_TEMPERATURE_WARNING_THRESHOLD", index, access, datatype)

        self.choice = None


class _CHIP_TEMPERATURE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("CHIP_TEMPERATURE", index, access, datatype)

        self.choice = None


class _CHIP_TEMPERATURE_SHUTDOWN_THRESHOLD(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("CHIP_TEMPERATURE_SHUTDOWN_THRESHOLD", index, access, datatype)

        self.choice = None


class _CHIP_TEMPERATURE_WARNING_THRESHOLD(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("CHIP_TEMPERATURE_WARNING_THRESHOLD", index, access, datatype)

        self.choice = None


class _GENERAL_ERROR_FLAGS(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("GENERAL_ERROR_FLAGS", index, access, datatype)

        self.choice = None


class _GDRV_ERROR_FLAGS(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("GDRV_ERROR_FLAGS", index, access, datatype)

        self.choice = None


class _ADC_STATUS_FLAGS(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ADC_STATUS_FLAGS", index, access, datatype)

        self.choice = None


class _MCC_INPUTS_RAW(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("MCC_INPUTS_RAW", index, access, datatype)

        self.choice = None


class _FOC_VOLTAGE_UX(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("FOC_VOLTAGE_UX", index, access, datatype)

        self.choice = None


class _FOC_VOLTAGE_WY(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("FOC_VOLTAGE_WY", index, access, datatype)

        self.choice = None


class _FOC_VOLTAGE_V(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("FOC_VOLTAGE_V", index, access, datatype)

        self.choice = None


class _FIELDWEAKENING_I(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("FIELDWEAKENING_I", index, access, datatype)

        self.choice = None


class _FIELDWEAKENING_VOLTAGE_THRESHOLD(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("FIELDWEAKENING_VOLTAGE_THRESHOLD", index, access, datatype)

        self.choice = None


class _FOC_CURRENT_UX(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("FOC_CURRENT_UX", index, access, datatype)

        self.choice = None


class _FOC_CURRENT_V(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("FOC_CURRENT_V", index, access, datatype)

        self.choice = None


class _FOC_CURRENT_WY(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("FOC_CURRENT_WY", index, access, datatype)

        self.choice = None


class _FOC_VOLTAGE_UQ(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("FOC_VOLTAGE_UQ", index, access, datatype)

        self.choice = None


class _FOC_CURRENT_IQ(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("FOC_CURRENT_IQ", index, access, datatype)

        self.choice = None


class _TARGET_TORQUE_BIQUAD_FILTER_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("TARGET_TORQUE_BIQUAD_FILTER_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _TARGET_TORQUE_BIQUAD_FILTER_ACOEFF_1(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("TARGET_TORQUE_BIQUAD_FILTER_ACOEFF_1", index, access, datatype)

        self.choice = None


class _TARGET_TORQUE_BIQUAD_FILTER_ACOEFF_2(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("TARGET_TORQUE_BIQUAD_FILTER_ACOEFF_2", index, access, datatype)

        self.choice = None


class _TARGET_TORQUE_BIQUAD_FILTER_BCOEFF_0(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("TARGET_TORQUE_BIQUAD_FILTER_BCOEFF_0", index, access, datatype)

        self.choice = None


class _TARGET_TORQUE_BIQUAD_FILTER_BCOEFF_1(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("TARGET_TORQUE_BIQUAD_FILTER_BCOEFF_1", index, access, datatype)

        self.choice = None


class _TARGET_TORQUE_BIQUAD_FILTER_BCOEFF_2(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("TARGET_TORQUE_BIQUAD_FILTER_BCOEFF_2", index, access, datatype)

        self.choice = None


class _ACTUAL_VELOCITY_BIQUAD_FILTER_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("ACTUAL_VELOCITY_BIQUAD_FILTER_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _ACTUAL_VELOCITY_BIQUAD_FILTER_ACOEFF_1(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ACTUAL_VELOCITY_BIQUAD_FILTER_ACOEFF_1", index, access, datatype)

        self.choice = None


class _ACTUAL_VELOCITY_BIQUAD_FILTER_ACOEFF_2(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ACTUAL_VELOCITY_BIQUAD_FILTER_ACOEFF_2", index, access, datatype)

        self.choice = None


class _ACTUAL_VELOCITY_BIQUAD_FILTER_BCOEFF_0(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ACTUAL_VELOCITY_BIQUAD_FILTER_BCOEFF_0", index, access, datatype)

        self.choice = None


class _ACTUAL_VELOCITY_BIQUAD_FILTER_BCOEFF_1(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ACTUAL_VELOCITY_BIQUAD_FILTER_BCOEFF_1", index, access, datatype)

        self.choice = None


class _ACTUAL_VELOCITY_BIQUAD_FILTER_BCOEFF_2(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("ACTUAL_VELOCITY_BIQUAD_FILTER_BCOEFF_2", index, access, datatype)

        self.choice = None


class _TORQUE_FLUX_COMBINED_TARGET_VALUES(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("TORQUE_FLUX_COMBINED_TARGET_VALUES", index, access, datatype)

        self.choice = None


class _TORQUE_FLUX_COMBINED_ACTUAL_VALUES(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("TORQUE_FLUX_COMBINED_ACTUAL_VALUES", index, access, datatype)

        self.choice = None


class _VOLTAGE_D_Q_COMBINED_ACTUAL_VALUES(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("VOLTAGE_D_Q_COMBINED_ACTUAL_VALUES", index, access, datatype)

        self.choice = None


class _INTEGRATED_ACTUAL_TORQUE_VALUE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("INTEGRATED_ACTUAL_TORQUE_VALUE", index, access, datatype)

        self.choice = None


class _INTEGRATED_ACTUAL_VELOCITY_VALUE(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("INTEGRATED_ACTUAL_VELOCITY_VALUE", index, access, datatype)

        self.choice = None

