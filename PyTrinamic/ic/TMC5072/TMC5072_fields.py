'''
Created on 20.09.2019

@author: JM
'''

class TMC5072_fields(object):
	"""
	Define all register bitfields of the TMC5072.

	Each field is defined as a tuple consisting of ( Address, Mask, Shift ).
	Fields that are present multiple times in different registers (for multiple
	motors) all of the bitfield tuples are bundled together into another tuple.

	The name of the register is written as a comment behind each tuple. This is
	intended for IDE users viewing the definition of a field by hovering over
	it. This allows the user to see the corresponding register name of a field
	without opening this file and searching for the definition.
	"""

	# GCONF
	SINGLE_DRIVER      = ( 0x00, 0x00000001,  0 ) # GCONF
	STEPDIR1_ENABLE    = ( 0x00, 0x00000002,  1 ) # GCONF
	STEPDIR2_ENABLE    = ( 0x00, 0x00000004,  2 ) # GCONF
	POSCMP_ENABLE      = ( 0x00, 0x00000008,  3 ) # GCONF
	ENC1_REFSEL        = ( 0x00, 0x00000010,  4 ) # GCONF
	ENC2_ENABLE        = ( 0x00, 0x00000020,  5 ) # GCONF
	ENC2_REFSEL        = ( 0x00, 0x00000040,  6 ) # GCONF
	TEST_MODE          = ( 0x00, 0x00000080,  7 ) # GCONF
	SHAFT1             = ( 0x00, 0x00000100,  8 ) # GCONF
	SHAFT2             = ( 0x00, 0x00000200,  9 ) # GCONF
	LOCK_GCONF         = ( 0x00, 0x00000400, 10 ) # GCONF
	DC_SYNC            = ( 0x00, 0x00000800, 11 ) # GCONF

	# GSTAT
	RESET              = ( 0x01, 0x00000001,  0 ) # GSTAT
	DRV_ERR1           = ( 0x01, 0x00000002,  1 ) # GSTAT
	DRV_ERR1           = ( 0x01, 0x00000004,  2 ) # GSTAT
	UV_CP              = ( 0x01, 0x00000008,  3 ) # GSTAT

	# IFCNT
	IFCNT              = ( 0x02, 0x000000FF,  0 ) # IFCNT

	# SLAVECONF
	SLAVEADDR          = ( 0x03, 0x0000000F,  0 ) # SLAVECONF
	SENDDELAY          = ( 0x03, 0x000000F0,  4 ) # SLAVECONF
	TEST_SEL           = ( 0x03, 0x0000000F,  0 ) # SLAVECONF
	SENDDELAY          = ( 0x03, 0x000000F0,  4 ) # SLAVECONF

	# INPUT / OUTPUT
	IO0_IN             = ( 0x04, 0x00000001,  0 ) # INPUT / OUTPUT
	IO1_IN             = ( 0x04, 0x00000002,  1 ) # INPUT / OUTPUT
	IO2_IN             = ( 0x04, 0x00000004,  2 ) # INPUT / OUTPUT
	IO3_IN             = ( 0x04, 0x00000008,  3 ) # INPUT / OUTPUT
	IOP_IN             = ( 0x04, 0x00000010,  4 ) # INPUT / OUTPUT
	ION_IN             = ( 0x04, 0x00000020,  5 ) # INPUT / OUTPUT
	NEXTADDR_IN        = ( 0x04, 0x00000040,  6 ) # INPUT / OUTPUT
	DRV_ENN            = ( 0x04, 0x00000080,  7 ) # INPUT / OUTPUT
	SW_COMP_IN         = ( 0x04, 0x00000100,  8 ) # INPUT / OUTPUT
	VERSION            = ( 0x04, 0xFF000000, 24 ) # INPUT / OUTPUT
	IO0_OUT            = ( 0x04, 0x00000001,  0 ) # INPUT / OUTPUT
	IO1_OUT            = ( 0x04, 0x00000002,  1 ) # INPUT / OUTPUT
	IO2_OUT            = ( 0x04, 0x00000004,  2 ) # INPUT / OUTPUT
	IODDR0             = ( 0x04, 0x00000100,  8 ) # INPUT / OUTPUT
	IODDR1             = ( 0x04, 0x00000200,  9 ) # INPUT / OUTPUT
	IODDR2             = ( 0x04, 0x00000400, 10 ) # INPUT / OUTPUT

	# X_COMPARE
	X_COMPARE          = ( 0x05, 0xFFFFFFFF,  0 ) # X_COMPARE

	# PWMCONF_M1
	PWM_AMPL           = ( 0x10, 0x000000FF,  0 ) # PWMCONF_M1
	PWM_GRAD           = ( 0x10, 0x0000FF00,  8 ) # PWMCONF_M1
	PWM_FREQ           = ( 0x10, 0x00030000, 16 ) # PWMCONF_M1
	PWM_AUTOSCALE      = ( 0x10, 0x00040000, 18 ) # PWMCONF_M1
	PWM_SYMMETRIC      = ( 0x10, 0x00080000, 19 ) # PWMCONF_M1
	FREEWHEEL          = ( 0x10, 0x00300000, 20 ) # PWMCONF_M1
	PWM_AMPL           = ( 0x10, 0x000000FF,  0 ) # PWMCONF_M1
	PWM_GRAD           = ( 0x10, 0x0000FF00,  8 ) # PWMCONF_M1
	PWM_FREQ           = ( 0x10, 0x00030000, 16 ) # PWMCONF_M1
	PWM_AUTOSCALE      = ( 0x10, 0x00040000, 18 ) # PWMCONF_M1
	PWM_SYMMETRIC      = ( 0x10, 0x00080000, 19 ) # PWMCONF_M1
	FREEWHEEL          = ( 0x10, 0x00300000, 20 ) # PWMCONF_M1

	# PWM_STATUS_M1
	PWM_STATUS         = ( 0x11, 0x000000FF,  0 ) # PWM_STATUS_M1

	# PWMCONF_M2
	PWM_AMPL           = ( 0x18, 0x000000FF,  0 ) # PWMCONF_M2
	PWM_GRAD           = ( 0x18, 0x0000FF00,  8 ) # PWMCONF_M2
	PWM_FREQ           = ( 0x18, 0x00030000, 16 ) # PWMCONF_M2
	PWM_AUTOSCALE      = ( 0x18, 0x00040000, 18 ) # PWMCONF_M2
	PWM_SYMMETRIC      = ( 0x18, 0x00080000, 19 ) # PWMCONF_M2
	FREEWHEEL          = ( 0x18, 0x00300000, 20 ) # PWMCONF_M2
	PWM_AMPL           = ( 0x18, 0x000000FF,  0 ) # PWMCONF_M2
	PWM_GRAD           = ( 0x18, 0x0000FF00,  8 ) # PWMCONF_M2
	PWM_FREQ           = ( 0x18, 0x00030000, 16 ) # PWMCONF_M2
	PWM_AUTOSCALE      = ( 0x18, 0x00040000, 18 ) # PWMCONF_M2
	PWM_SYMMETRIC      = ( 0x18, 0x00080000, 19 ) # PWMCONF_M2
	FREEWHEEL          = ( 0x18, 0x00300000, 20 ) # PWMCONF_M2

	# PWM_STATUS_M2
	PWM_STATUS         = ( 0x19, 0x000000FF,  0 ) # PWM_STATUS_M2

	# RAMPMODE_M1
	RAMPMODE           = ( 0x20, 0x00000003,  0 ) # RAMPMODE_M1

	# XACTUAL_M1
	XACTUAL            = ( 0x21, 0xFFFFFFFF,  0 ) # XACTUAL_M1

	# VACTUAL_M1
	VACTUAL            = ( 0x22, 0x00FFFFFF,  0 ) # VACTUAL_M1

	# VSTART_M1
	VSTART             = ( 0x23, 0x0003FFFF,  0 ) # VSTART_M1

	# A1_M1
	A1                 = ( 0x24, 0x0000FFFF,  0 ) # A1_M1

	# V1_M1
	V1_                = ( 0x25, 0x000FFFFF,  0 ) # V1_M1

	# AMAX_M1
	AMAX               = ( 0x26, 0x0000FFFF,  0 ) # AMAX_M1

	# VMAX_M1
	VMAX               = ( 0x27, 0x007FFFFF,  0 ) # VMAX_M1

	# DMAX_M1
	DMAX               = ( 0x28, 0x0000FFFF,  0 ) # DMAX_M1

	# D1_M1
	D1                 = ( 0x2A, 0x0000FFFF,  0 ) # D1_M1

	# VSTOP_M1
	VSTOP              = ( 0x2B, 0x0003FFFF,  0 ) # VSTOP_M1

	# TZEROWAIT_M1
	TZEROWAIT          = ( 0x2C, 0x0000FFFF,  0 ) # TZEROWAIT_M1

	# XTARGET_M1
	XTARGET            = ( 0x2D, 0xFFFFFFFF,  0 ) # XTARGET_M1

	# RAMPMODE_M2
	RAMPMODE           = ( 0x40, 0x00000003,  0 ) # RAMPMODE_M2

	# XACTUAL_M2
	XACTUAL            = ( 0x41, 0xFFFFFFFF,  0 ) # XACTUAL_M2

	# VACTUAL_M2
	VACTUAL            = ( 0x42, 0x00FFFFFF,  0 ) # VACTUAL_M2

	# VSTART_M2
	VSTART             = ( 0x43, 0x0003FFFF,  0 ) # VSTART_M2

	# A1_M2
	A1                 = ( 0x44, 0x0000FFFF,  0 ) # A1_M2

	# V1_M2
	V1_                = ( 0x45, 0x000FFFFF,  0 ) # V1_M2

	# AMAX_M2
	AMAX               = ( 0x46, 0x0000FFFF,  0 ) # AMAX_M2

	# VMAX_M2
	VMAX               = ( 0x47, 0x007FFFFF,  0 ) # VMAX_M2

	# DMAX_M2
	DMAX               = ( 0x48, 0x0000FFFF,  0 ) # DMAX_M2

	# D1_M2
	D1                 = ( 0x4A, 0x0000FFFF,  0 ) # D1_M2

	# VSTOP_M2
	VSTOP              = ( 0x4B, 0x0003FFFF,  0 ) # VSTOP_M2

	# TZEROWAIT_M2
	TZEROWAIT          = ( 0x4C, 0x0000FFFF,  0 ) # TZEROWAIT_M2

	# XTARGET_M2
	XTARGET            = ( 0x4D, 0xFFFFFFFF,  0 ) # XTARGET_M2

	# IHOLD_IRUN_M1
	IHOLD              = ( 0x30, 0x0000001F,  0 ) # IHOLD_IRUN_M1
	IRUN               = ( 0x30, 0x00001F00,  8 ) # IHOLD_IRUN_M1
	IHOLDDELAY         = ( 0x30, 0x000F0000, 16 ) # IHOLD_IRUN_M1

	# VCOOLTHRS_M1
	VCOOLTHRS          = ( 0x31, 0x007FFFFF,  0 ) # VCOOLTHRS_M1

	# VHIGH_M1
	VHIGH              = ( 0x32, 0x007FFFFF,  0 ) # VHIGH_M1

	# VDCMIN_M1
	VDCMIN             = ( 0x33, 0x007FFFFF,  0 ) # VDCMIN_M1

	# SW_MODE_M1
	STOP_L_ENABLE      = ( 0x34, 0x00000001,  0 ) # SW_MODE_M1
	STOP_R_ENABLE      = ( 0x34, 0x00000002,  1 ) # SW_MODE_M1
	POL_STOP_L         = ( 0x34, 0x00000004,  2 ) # SW_MODE_M1
	POL_STOP_R         = ( 0x34, 0x00000008,  3 ) # SW_MODE_M1
	SWAP_LR            = ( 0x34, 0x00000010,  4 ) # SW_MODE_M1
	LATCH_L_ACTIVE     = ( 0x34, 0x00000020,  5 ) # SW_MODE_M1
	LATCH_L_INACTIVE   = ( 0x34, 0x00000040,  6 ) # SW_MODE_M1
	LATCH_R_ACTIVE     = ( 0x34, 0x00000080,  7 ) # SW_MODE_M1
	LATCH_R_INACTIVE   = ( 0x34, 0x00000100,  8 ) # SW_MODE_M1
	EN_LATCH_ENCODER   = ( 0x34, 0x00000200,  9 ) # SW_MODE_M1
	SG_STOP            = ( 0x34, 0x00000400, 10 ) # SW_MODE_M1
	EN_SOFTSTOP        = ( 0x34, 0x00000800, 11 ) # SW_MODE_M1

	# RAMP_STAT_M1
	STATUS_STOP_L      = ( 0x35, 0x00000001,  0 ) # RAMP_STAT_M1
	STATUS_STOP_R      = ( 0x35, 0x00000002,  1 ) # RAMP_STAT_M1
	STATUS_LATCH_L     = ( 0x35, 0x00000004,  2 ) # RAMP_STAT_M1
	STATUS_LATCH_R     = ( 0x35, 0x00000008,  3 ) # RAMP_STAT_M1
	EVENT_STOP_L       = ( 0x35, 0x00000010,  4 ) # RAMP_STAT_M1
	EVENT_STOP_R       = ( 0x35, 0x00000020,  5 ) # RAMP_STAT_M1
	EVENT_STOP_SG      = ( 0x35, 0x00000040,  6 ) # RAMP_STAT_M1
	EVENT_POS_REACHED  = ( 0x35, 0x00000080,  7 ) # RAMP_STAT_M1
	VELOCITY_REACHED   = ( 0x35, 0x00000100,  8 ) # RAMP_STAT_M1
	POSITION_REACHED   = ( 0x35, 0x00000200,  9 ) # RAMP_STAT_M1
	VZERO              = ( 0x35, 0x00000400, 10 ) # RAMP_STAT_M1
	T_ZEROWAIT_ACTIVE  = ( 0x35, 0x00000800, 11 ) # RAMP_STAT_M1
	SECOND_MOVE        = ( 0x35, 0x00001000, 12 ) # RAMP_STAT_M1
	STATUS_SG          = ( 0x35, 0x00002000, 13 ) # RAMP_STAT_M1

	# XLATCH_M1
	XLATCH             = ( 0x36, 0xFFFFFFFF,  0 ) # XLATCH_M1

	# IHOLD_IRUN_M2
	IHOLD              = ( 0x50, 0x0000001F,  0 ) # IHOLD_IRUN_M2
	IRUN               = ( 0x50, 0x00001F00,  8 ) # IHOLD_IRUN_M2
	IHOLDDELAY         = ( 0x50, 0x000F0000, 16 ) # IHOLD_IRUN_M2

	# VCOOLTHRS_M2
	VCOOLTHRS          = ( 0x51, 0x007FFFFF,  0 ) # VCOOLTHRS_M2

	# VHIGH_M2
	VHIGH              = ( 0x52, 0x007FFFFF,  0 ) # VHIGH_M2

	# VDCMIN_M2
	VDCMIN             = ( 0x53, 0x007FFFFF,  0 ) # VDCMIN_M2

	# SW_MODE_M2
	STOP_L_ENABLE      = ( 0x54, 0x00000001,  0 ) # SW_MODE_M2
	STOP_R_ENABLE      = ( 0x54, 0x00000002,  1 ) # SW_MODE_M2
	POL_STOP_L         = ( 0x54, 0x00000004,  2 ) # SW_MODE_M2
	POL_STOP_R         = ( 0x54, 0x00000008,  3 ) # SW_MODE_M2
	SWAP_LR            = ( 0x54, 0x00000010,  4 ) # SW_MODE_M2
	LATCH_L_ACTIVE     = ( 0x54, 0x00000020,  5 ) # SW_MODE_M2
	LATCH_L_INACTIVE   = ( 0x54, 0x00000040,  6 ) # SW_MODE_M2
	LATCH_R_ACTIVE     = ( 0x54, 0x00000080,  7 ) # SW_MODE_M2
	LATCH_R_INACTIVE   = ( 0x54, 0x00000100,  8 ) # SW_MODE_M2
	EN_LATCH_ENCODER   = ( 0x54, 0x00000200,  9 ) # SW_MODE_M2
	SG_STOP            = ( 0x54, 0x00000400, 10 ) # SW_MODE_M2
	EN_SOFTSTOP        = ( 0x54, 0x00000800, 11 ) # SW_MODE_M2

	# RAMP_STAT_M2
	STATUS_STOP_L      = ( 0x55, 0x00000001,  0 ) # RAMP_STAT_M2
	STATUS_STOP_R      = ( 0x55, 0x00000002,  1 ) # RAMP_STAT_M2
	STATUS_LATCH_L     = ( 0x55, 0x00000004,  2 ) # RAMP_STAT_M2
	STATUS_LATCH_R     = ( 0x55, 0x00000008,  3 ) # RAMP_STAT_M2
	EVENT_STOP_L       = ( 0x55, 0x00000010,  4 ) # RAMP_STAT_M2
	EVENT_STOP_R       = ( 0x55, 0x00000020,  5 ) # RAMP_STAT_M2
	EVENT_STOP_SG      = ( 0x55, 0x00000040,  6 ) # RAMP_STAT_M2
	EVENT_POS_REACHED  = ( 0x55, 0x00000080,  7 ) # RAMP_STAT_M2
	VELOCITY_REACHED   = ( 0x55, 0x00000100,  8 ) # RAMP_STAT_M2
	POSITION_REACHED   = ( 0x55, 0x00000200,  9 ) # RAMP_STAT_M2
	VZERO              = ( 0x55, 0x00000400, 10 ) # RAMP_STAT_M2
	T_ZEROWAIT_ACTIVE  = ( 0x55, 0x00000800, 11 ) # RAMP_STAT_M2
	SECOND_MOVE        = ( 0x55, 0x00001000, 12 ) # RAMP_STAT_M2
	STATUS_SG          = ( 0x55, 0x00002000, 13 ) # RAMP_STAT_M2

	# XLATCH_M2
	XLATCH             = ( 0x56, 0xFFFFFFFF,  0 ) # XLATCH_M2

	# ENCMODE_M1
	POL_A              = ( 0x38, 0x00000001,  0 ) # ENCMODE_M1
	POL_B              = ( 0x38, 0x00000002,  1 ) # ENCMODE_M1
	POL_N              = ( 0x38, 0x00000004,  2 ) # ENCMODE_M1
	IGNORE_AB          = ( 0x38, 0x00000008,  3 ) # ENCMODE_M1
	CLR_CONT           = ( 0x38, 0x00000010,  4 ) # ENCMODE_M1
	CLR_ONCE           = ( 0x38, 0x00000020,  5 ) # ENCMODE_M1
	POS_EDGE_NEG_EDGE  = ( 0x38, 0x000000C0,  6 ) # ENCMODE_M1
	CLR_ENC_X          = ( 0x38, 0x00000100,  8 ) # ENCMODE_M1
	LATCH_X_ACT        = ( 0x38, 0x00000200,  9 ) # ENCMODE_M1
	ENC_SEL_DECIMAL    = ( 0x38, 0x00000400, 10 ) # ENCMODE_M1
	LATCH_NOW_         = ( 0x38, 0x00000800, 11 ) # ENCMODE_M1

	# X_ENC_M1
	X_ENC              = ( 0x39, 0xFFFFFFFF,  0 ) # X_ENC_M1

	# ENC_CONST_M1
	INTEGER            = ( 0x3A, 0xFFFF0000, 16 ) # ENC_CONST_M1
	FRACTIONAL         = ( 0x3A, 0x0000FFFF,  0 ) # ENC_CONST_M1

	# ENC_STATUS_M1
	ENC_STATUS         = ( 0x3B, 0x00000001,  0 ) # ENC_STATUS_M1

	# ENC_LATCH_M1
	ENC_LATCH          = ( 0x3C, 0xFFFFFFFF,  0 ) # ENC_LATCH_M1

	# ENCMODE_M2
	POL_A              = ( 0x58, 0x00000001,  0 ) # ENCMODE_M2
	POL_B              = ( 0x58, 0x00000002,  1 ) # ENCMODE_M2
	POL_N              = ( 0x58, 0x00000004,  2 ) # ENCMODE_M2
	IGNORE_AB          = ( 0x58, 0x00000008,  3 ) # ENCMODE_M2
	CLR_CONT           = ( 0x58, 0x00000010,  4 ) # ENCMODE_M2
	CLR_ONCE           = ( 0x58, 0x00000020,  5 ) # ENCMODE_M2
	POS_EDGE_NEG_EDGE  = ( 0x58, 0x000000C0,  6 ) # ENCMODE_M2
	CLR_ENC_X          = ( 0x58, 0x00000100,  8 ) # ENCMODE_M2
	LATCH_X_ACT        = ( 0x58, 0x00000200,  9 ) # ENCMODE_M2
	ENC_SEL_DECIMAL    = ( 0x58, 0x00000400, 10 ) # ENCMODE_M2
	LATCH_NOW_         = ( 0x58, 0x00000800, 11 ) # ENCMODE_M2

	# X_ENC_M2
	X_ENC              = ( 0x59, 0xFFFFFFFF,  0 ) # X_ENC_M2

	# ENC_CONST_M2
	INTEGER            = ( 0x5A, 0xFFFF0000, 16 ) # ENC_CONST_M2
	FRACTIONAL         = ( 0x5A, 0x0000FFFF,  0 ) # ENC_CONST_M2

	# ENC_STATUS_M2
	ENC_STATUS         = ( 0x5B, 0x00000001,  0 ) # ENC_STATUS_M2

	# ENC_LATCH_M2
	ENC_LATCH          = ( 0x5C, 0xFFFFFFFF,  0 ) # ENC_LATCH_M2

	# MSLUT[0]
	OFS0               = ( 0x60, 0x00000001,  0 ) # MSLUT[0]
	OFS1               = ( 0x60, 0x00000002,  1 ) # MSLUT[0]
	OFS2               = ( 0x60, 0x00000004,  2 ) # MSLUT[0]
	OFS3               = ( 0x60, 0x00000008,  3 ) # MSLUT[0]
	OFS4               = ( 0x60, 0x00000010,  4 ) # MSLUT[0]
	OFS5               = ( 0x60, 0x00000020,  5 ) # MSLUT[0]
	OFS6               = ( 0x60, 0x00000040,  6 ) # MSLUT[0]
	OFS7               = ( 0x60, 0x00000080,  7 ) # MSLUT[0]
	OFS8               = ( 0x60, 0x00000100,  8 ) # MSLUT[0]
	OFS9               = ( 0x60, 0x00000200,  9 ) # MSLUT[0]
	OFS10              = ( 0x60, 0x00000400, 10 ) # MSLUT[0]
	OFS11              = ( 0x60, 0x00000800, 11 ) # MSLUT[0]
	OFS12              = ( 0x60, 0x00001000, 12 ) # MSLUT[0]
	OFS13              = ( 0x60, 0x00002000, 13 ) # MSLUT[0]
	OFS14              = ( 0x60, 0x00004000, 14 ) # MSLUT[0]
	OFS15              = ( 0x60, 0x00008000, 15 ) # MSLUT[0]
	OFS16              = ( 0x60, 0x00010000, 16 ) # MSLUT[0]
	OFS17              = ( 0x60, 0x00020000, 17 ) # MSLUT[0]
	OFS18              = ( 0x60, 0x00040000, 18 ) # MSLUT[0]
	OFS19              = ( 0x60, 0x00080000, 19 ) # MSLUT[0]
	OFS20              = ( 0x60, 0x00100000, 20 ) # MSLUT[0]
	OFS21              = ( 0x60, 0x00200000, 21 ) # MSLUT[0]
	OFS22              = ( 0x60, 0x00400000, 22 ) # MSLUT[0]
	OFS23              = ( 0x60, 0x00800000, 23 ) # MSLUT[0]
	OFS24              = ( 0x60, 0x01000000, 24 ) # MSLUT[0]
	OFS25              = ( 0x60, 0x02000000, 25 ) # MSLUT[0]
	OFS26              = ( 0x60, 0x04000000, 26 ) # MSLUT[0]
	OFS27              = ( 0x60, 0x08000000, 27 ) # MSLUT[0]
	OFS28              = ( 0x60, 0x10000000, 28 ) # MSLUT[0]
	OFS29              = ( 0x60, 0x20000000, 29 ) # MSLUT[0]
	OFS30              = ( 0x60, 0x40000000, 30 ) # MSLUT[0]
	OFS31              = ( 0x60, 0x80000000, 31 ) # MSLUT[0]

	# MSLUT[1]
	OFS32              = ( 0x61, 0x00000001,  0 ) # MSLUT[1]
	OFS33              = ( 0x61, 0x00000002,  1 ) # MSLUT[1]
	OFS34              = ( 0x61, 0x00000004,  2 ) # MSLUT[1]
	OFS35              = ( 0x61, 0x00000008,  3 ) # MSLUT[1]
	OFS36              = ( 0x61, 0x00000010,  4 ) # MSLUT[1]
	OFS37              = ( 0x61, 0x00000020,  5 ) # MSLUT[1]
	OFS38              = ( 0x61, 0x00000040,  6 ) # MSLUT[1]
	OFS39              = ( 0x61, 0x00000080,  7 ) # MSLUT[1]
	OFS40              = ( 0x61, 0x00000100,  8 ) # MSLUT[1]
	OFS41              = ( 0x61, 0x00000200,  9 ) # MSLUT[1]
	OFS42              = ( 0x61, 0x00000400, 10 ) # MSLUT[1]
	OFS43              = ( 0x61, 0x00000800, 11 ) # MSLUT[1]
	OFS44              = ( 0x61, 0x00001000, 12 ) # MSLUT[1]
	OFS45              = ( 0x61, 0x00002000, 13 ) # MSLUT[1]
	OFS46              = ( 0x61, 0x00004000, 14 ) # MSLUT[1]
	OFS47              = ( 0x61, 0x00008000, 15 ) # MSLUT[1]
	OFS48              = ( 0x61, 0x00010000, 16 ) # MSLUT[1]
	OFS49              = ( 0x61, 0x00020000, 17 ) # MSLUT[1]
	OFS50              = ( 0x61, 0x00040000, 18 ) # MSLUT[1]
	OFS51              = ( 0x61, 0x00080000, 19 ) # MSLUT[1]
	OFS52              = ( 0x61, 0x00100000, 20 ) # MSLUT[1]
	OFS53              = ( 0x61, 0x00200000, 21 ) # MSLUT[1]
	OFS54              = ( 0x61, 0x00400000, 22 ) # MSLUT[1]
	OFS55              = ( 0x61, 0x00800000, 23 ) # MSLUT[1]
	OFS56              = ( 0x61, 0x01000000, 24 ) # MSLUT[1]
	OFS57              = ( 0x61, 0x02000000, 25 ) # MSLUT[1]
	OFS58              = ( 0x61, 0x04000000, 26 ) # MSLUT[1]
	OFS59              = ( 0x61, 0x08000000, 27 ) # MSLUT[1]
	OFS60              = ( 0x61, 0x10000000, 28 ) # MSLUT[1]
	OFS61              = ( 0x61, 0x20000000, 29 ) # MSLUT[1]
	OFS62              = ( 0x61, 0x40000000, 30 ) # MSLUT[1]
	OFS63              = ( 0x61, 0x80000000, 31 ) # MSLUT[1]

	# MSLUT[2]
	OFS64              = ( 0x62, 0x00000001,  0 ) # MSLUT[2]
	OFS65              = ( 0x62, 0x00000002,  1 ) # MSLUT[2]
	OFS66              = ( 0x62, 0x00000004,  2 ) # MSLUT[2]
	OFS67              = ( 0x62, 0x00000008,  3 ) # MSLUT[2]
	OFS68              = ( 0x62, 0x00000010,  4 ) # MSLUT[2]
	OFS69              = ( 0x62, 0x00000020,  5 ) # MSLUT[2]
	OFS70              = ( 0x62, 0x00000040,  6 ) # MSLUT[2]
	OFS71              = ( 0x62, 0x00000080,  7 ) # MSLUT[2]
	OFS72              = ( 0x62, 0x00000100,  8 ) # MSLUT[2]
	OFS73              = ( 0x62, 0x00000200,  9 ) # MSLUT[2]
	OFS74              = ( 0x62, 0x00000400, 10 ) # MSLUT[2]
	OFS75              = ( 0x62, 0x00000800, 11 ) # MSLUT[2]
	OFS76              = ( 0x62, 0x00001000, 12 ) # MSLUT[2]
	OFS77              = ( 0x62, 0x00002000, 13 ) # MSLUT[2]
	OFS78              = ( 0x62, 0x00004000, 14 ) # MSLUT[2]
	OFS79              = ( 0x62, 0x00008000, 15 ) # MSLUT[2]
	OFS80              = ( 0x62, 0x00010000, 16 ) # MSLUT[2]
	OFS81              = ( 0x62, 0x00020000, 17 ) # MSLUT[2]
	OFS82              = ( 0x62, 0x00040000, 18 ) # MSLUT[2]
	OFS83              = ( 0x62, 0x00080000, 19 ) # MSLUT[2]
	OFS84              = ( 0x62, 0x00100000, 20 ) # MSLUT[2]
	OFS85              = ( 0x62, 0x00200000, 21 ) # MSLUT[2]
	OFS86              = ( 0x62, 0x00400000, 22 ) # MSLUT[2]
	OFS87              = ( 0x62, 0x00800000, 23 ) # MSLUT[2]
	OFS88              = ( 0x62, 0x01000000, 24 ) # MSLUT[2]
	OFS89              = ( 0x62, 0x02000000, 25 ) # MSLUT[2]
	OFS90              = ( 0x62, 0x04000000, 26 ) # MSLUT[2]
	OFS91              = ( 0x62, 0x08000000, 27 ) # MSLUT[2]
	OFS92              = ( 0x62, 0x10000000, 28 ) # MSLUT[2]
	OFS93              = ( 0x62, 0x20000000, 29 ) # MSLUT[2]
	OFS94              = ( 0x62, 0x40000000, 30 ) # MSLUT[2]
	OFS95              = ( 0x62, 0x80000000, 31 ) # MSLUT[2]

	# MSLUT[3]
	OFS96              = ( 0x63, 0x00000001,  0 ) # MSLUT[3]
	OFS97              = ( 0x63, 0x00000002,  1 ) # MSLUT[3]
	OFS98              = ( 0x63, 0x00000004,  2 ) # MSLUT[3]
	OFS99              = ( 0x63, 0x00000008,  3 ) # MSLUT[3]
	OFS100             = ( 0x63, 0x00000010,  4 ) # MSLUT[3]
	OFS101             = ( 0x63, 0x00000020,  5 ) # MSLUT[3]
	OFS102             = ( 0x63, 0x00000040,  6 ) # MSLUT[3]
	OFS103             = ( 0x63, 0x00000080,  7 ) # MSLUT[3]
	OFS104             = ( 0x63, 0x00000100,  8 ) # MSLUT[3]
	OFS105             = ( 0x63, 0x00000200,  9 ) # MSLUT[3]
	OFS106             = ( 0x63, 0x00000400, 10 ) # MSLUT[3]
	OFS107             = ( 0x63, 0x00000800, 11 ) # MSLUT[3]
	OFS108             = ( 0x63, 0x00001000, 12 ) # MSLUT[3]
	OFS109             = ( 0x63, 0x00002000, 13 ) # MSLUT[3]
	OFS110             = ( 0x63, 0x00004000, 14 ) # MSLUT[3]
	OFS111             = ( 0x63, 0x00008000, 15 ) # MSLUT[3]
	OFS112             = ( 0x63, 0x00010000, 16 ) # MSLUT[3]
	OFS113             = ( 0x63, 0x00020000, 17 ) # MSLUT[3]
	OFS114             = ( 0x63, 0x00040000, 18 ) # MSLUT[3]
	OFS115             = ( 0x63, 0x00080000, 19 ) # MSLUT[3]
	OFS116             = ( 0x63, 0x00100000, 20 ) # MSLUT[3]
	OFS117             = ( 0x63, 0x00200000, 21 ) # MSLUT[3]
	OFS118             = ( 0x63, 0x00400000, 22 ) # MSLUT[3]
	OFS119             = ( 0x63, 0x00800000, 23 ) # MSLUT[3]
	OFS120             = ( 0x63, 0x01000000, 24 ) # MSLUT[3]
	OFS121             = ( 0x63, 0x02000000, 25 ) # MSLUT[3]
	OFS122             = ( 0x63, 0x04000000, 26 ) # MSLUT[3]
	OFS123             = ( 0x63, 0x08000000, 27 ) # MSLUT[3]
	OFS124             = ( 0x63, 0x10000000, 28 ) # MSLUT[3]
	OFS125             = ( 0x63, 0x20000000, 29 ) # MSLUT[3]
	OFS126             = ( 0x63, 0x40000000, 30 ) # MSLUT[3]
	OFS127             = ( 0x63, 0x80000000, 31 ) # MSLUT[3]

	# MSLUT[4]
	OFS128             = ( 0x64, 0x00000001,  0 ) # MSLUT[4]
	OFS129             = ( 0x64, 0x00000002,  1 ) # MSLUT[4]
	OFS130             = ( 0x64, 0x00000004,  2 ) # MSLUT[4]
	OFS131             = ( 0x64, 0x00000008,  3 ) # MSLUT[4]
	OFS132             = ( 0x64, 0x00000010,  4 ) # MSLUT[4]
	OFS133             = ( 0x64, 0x00000020,  5 ) # MSLUT[4]
	OFS134             = ( 0x64, 0x00000040,  6 ) # MSLUT[4]
	OFS135             = ( 0x64, 0x00000080,  7 ) # MSLUT[4]
	OFS136             = ( 0x64, 0x00000100,  8 ) # MSLUT[4]
	OFS137             = ( 0x64, 0x00000200,  9 ) # MSLUT[4]
	OFS138             = ( 0x64, 0x00000400, 10 ) # MSLUT[4]
	OFS139             = ( 0x64, 0x00000800, 11 ) # MSLUT[4]
	OFS140             = ( 0x64, 0x00001000, 12 ) # MSLUT[4]
	OFS141             = ( 0x64, 0x00002000, 13 ) # MSLUT[4]
	OFS142             = ( 0x64, 0x00004000, 14 ) # MSLUT[4]
	OFS143             = ( 0x64, 0x00008000, 15 ) # MSLUT[4]
	OFS144             = ( 0x64, 0x00010000, 16 ) # MSLUT[4]
	OFS145             = ( 0x64, 0x00020000, 17 ) # MSLUT[4]
	OFS146             = ( 0x64, 0x00040000, 18 ) # MSLUT[4]
	OFS147             = ( 0x64, 0x00080000, 19 ) # MSLUT[4]
	OFS148             = ( 0x64, 0x00100000, 20 ) # MSLUT[4]
	OFS149             = ( 0x64, 0x00200000, 21 ) # MSLUT[4]
	OFS150             = ( 0x64, 0x00400000, 22 ) # MSLUT[4]
	OFS151             = ( 0x64, 0x00800000, 23 ) # MSLUT[4]
	OFS152             = ( 0x64, 0x01000000, 24 ) # MSLUT[4]
	OFS153             = ( 0x64, 0x02000000, 25 ) # MSLUT[4]
	OFS154             = ( 0x64, 0x04000000, 26 ) # MSLUT[4]
	OFS155             = ( 0x64, 0x08000000, 27 ) # MSLUT[4]
	OFS156             = ( 0x64, 0x10000000, 28 ) # MSLUT[4]
	OFS157             = ( 0x64, 0x20000000, 29 ) # MSLUT[4]
	OFS158             = ( 0x64, 0x40000000, 30 ) # MSLUT[4]
	OFS159             = ( 0x64, 0x80000000, 31 ) # MSLUT[4]

	# MSLUT[5]
	OFS160             = ( 0x65, 0x00000001,  0 ) # MSLUT[5]
	OFS161             = ( 0x65, 0x00000002,  1 ) # MSLUT[5]
	OFS162             = ( 0x65, 0x00000004,  2 ) # MSLUT[5]
	OFS163             = ( 0x65, 0x00000008,  3 ) # MSLUT[5]
	OFS164             = ( 0x65, 0x00000010,  4 ) # MSLUT[5]
	OFS165             = ( 0x65, 0x00000020,  5 ) # MSLUT[5]
	OFS166             = ( 0x65, 0x00000040,  6 ) # MSLUT[5]
	OFS167             = ( 0x65, 0x00000080,  7 ) # MSLUT[5]
	OFS168             = ( 0x65, 0x00000100,  8 ) # MSLUT[5]
	OFS169             = ( 0x65, 0x00000200,  9 ) # MSLUT[5]
	OFS170             = ( 0x65, 0x00000400, 10 ) # MSLUT[5]
	OFS171             = ( 0x65, 0x00000800, 11 ) # MSLUT[5]
	OFS172             = ( 0x65, 0x00001000, 12 ) # MSLUT[5]
	OFS173             = ( 0x65, 0x00002000, 13 ) # MSLUT[5]
	OFS174             = ( 0x65, 0x00004000, 14 ) # MSLUT[5]
	OFS175             = ( 0x65, 0x00008000, 15 ) # MSLUT[5]
	OFS176             = ( 0x65, 0x00010000, 16 ) # MSLUT[5]
	OFS177             = ( 0x65, 0x00020000, 17 ) # MSLUT[5]
	OFS178             = ( 0x65, 0x00040000, 18 ) # MSLUT[5]
	OFS179             = ( 0x65, 0x00080000, 19 ) # MSLUT[5]
	OFS180             = ( 0x65, 0x00100000, 20 ) # MSLUT[5]
	OFS181             = ( 0x65, 0x00200000, 21 ) # MSLUT[5]
	OFS182             = ( 0x65, 0x00400000, 22 ) # MSLUT[5]
	OFS183             = ( 0x65, 0x00800000, 23 ) # MSLUT[5]
	OFS184             = ( 0x65, 0x01000000, 24 ) # MSLUT[5]
	OFS185             = ( 0x65, 0x02000000, 25 ) # MSLUT[5]
	OFS186             = ( 0x65, 0x04000000, 26 ) # MSLUT[5]
	OFS187             = ( 0x65, 0x08000000, 27 ) # MSLUT[5]
	OFS188             = ( 0x65, 0x10000000, 28 ) # MSLUT[5]
	OFS189             = ( 0x65, 0x20000000, 29 ) # MSLUT[5]
	OFS190             = ( 0x65, 0x40000000, 30 ) # MSLUT[5]
	OFS191             = ( 0x65, 0x80000000, 31 ) # MSLUT[5]

	# MSLUT[6]
	OFS192             = ( 0x66, 0x00000001,  0 ) # MSLUT[6]
	OFS193             = ( 0x66, 0x00000002,  1 ) # MSLUT[6]
	OFS194             = ( 0x66, 0x00000004,  2 ) # MSLUT[6]
	OFS195             = ( 0x66, 0x00000008,  3 ) # MSLUT[6]
	OFS196             = ( 0x66, 0x00000010,  4 ) # MSLUT[6]
	OFS197             = ( 0x66, 0x00000020,  5 ) # MSLUT[6]
	OFS198             = ( 0x66, 0x00000040,  6 ) # MSLUT[6]
	OFS199             = ( 0x66, 0x00000080,  7 ) # MSLUT[6]
	OFS200             = ( 0x66, 0x00000100,  8 ) # MSLUT[6]
	OFS201             = ( 0x66, 0x00000200,  9 ) # MSLUT[6]
	OFS202             = ( 0x66, 0x00000400, 10 ) # MSLUT[6]
	OFS203             = ( 0x66, 0x00000800, 11 ) # MSLUT[6]
	OFS204             = ( 0x66, 0x00001000, 12 ) # MSLUT[6]
	OFS205             = ( 0x66, 0x00002000, 13 ) # MSLUT[6]
	OFS206             = ( 0x66, 0x00004000, 14 ) # MSLUT[6]
	OFS207             = ( 0x66, 0x00008000, 15 ) # MSLUT[6]
	OFS208             = ( 0x66, 0x00010000, 16 ) # MSLUT[6]
	OFS209             = ( 0x66, 0x00020000, 17 ) # MSLUT[6]
	OFS210             = ( 0x66, 0x00040000, 18 ) # MSLUT[6]
	OFS211             = ( 0x66, 0x00080000, 19 ) # MSLUT[6]
	OFS212             = ( 0x66, 0x00100000, 20 ) # MSLUT[6]
	OFS213             = ( 0x66, 0x00200000, 21 ) # MSLUT[6]
	OFS214             = ( 0x66, 0x00400000, 22 ) # MSLUT[6]
	OFS215             = ( 0x66, 0x00800000, 23 ) # MSLUT[6]
	OFS216             = ( 0x66, 0x01000000, 24 ) # MSLUT[6]
	OFS217             = ( 0x66, 0x02000000, 25 ) # MSLUT[6]
	OFS218             = ( 0x66, 0x04000000, 26 ) # MSLUT[6]
	OFS219             = ( 0x66, 0x08000000, 27 ) # MSLUT[6]
	OFS220             = ( 0x66, 0x10000000, 28 ) # MSLUT[6]
	OFS221             = ( 0x66, 0x20000000, 29 ) # MSLUT[6]
	OFS222             = ( 0x66, 0x40000000, 30 ) # MSLUT[6]
	OFS223             = ( 0x66, 0x80000000, 31 ) # MSLUT[6]

	# MSLUT[7]
	OFS224             = ( 0x67, 0x00000001,  0 ) # MSLUT[7]
	OFS225             = ( 0x67, 0x00000002,  1 ) # MSLUT[7]
	OFS226             = ( 0x67, 0x00000004,  2 ) # MSLUT[7]
	OFS227             = ( 0x67, 0x00000008,  3 ) # MSLUT[7]
	OFS228             = ( 0x67, 0x00000010,  4 ) # MSLUT[7]
	OFS229             = ( 0x67, 0x00000020,  5 ) # MSLUT[7]
	OFS230             = ( 0x67, 0x00000040,  6 ) # MSLUT[7]
	OFS231             = ( 0x67, 0x00000080,  7 ) # MSLUT[7]
	OFS232             = ( 0x67, 0x00000100,  8 ) # MSLUT[7]
	OFS233             = ( 0x67, 0x00000200,  9 ) # MSLUT[7]
	OFS234             = ( 0x67, 0x00000400, 10 ) # MSLUT[7]
	OFS235             = ( 0x67, 0x00000800, 11 ) # MSLUT[7]
	OFS236             = ( 0x67, 0x00001000, 12 ) # MSLUT[7]
	OFS237             = ( 0x67, 0x00002000, 13 ) # MSLUT[7]
	OFS238             = ( 0x67, 0x00004000, 14 ) # MSLUT[7]
	OFS239             = ( 0x67, 0x00008000, 15 ) # MSLUT[7]
	OFS240             = ( 0x67, 0x00010000, 16 ) # MSLUT[7]
	OFS241             = ( 0x67, 0x00020000, 17 ) # MSLUT[7]
	OFS242             = ( 0x67, 0x00040000, 18 ) # MSLUT[7]
	OFS243             = ( 0x67, 0x00080000, 19 ) # MSLUT[7]
	OFS244             = ( 0x67, 0x00100000, 20 ) # MSLUT[7]
	OFS245             = ( 0x67, 0x00200000, 21 ) # MSLUT[7]
	OFS246             = ( 0x67, 0x00400000, 22 ) # MSLUT[7]
	OFS247             = ( 0x67, 0x00800000, 23 ) # MSLUT[7]
	OFS248             = ( 0x67, 0x01000000, 24 ) # MSLUT[7]
	OFS249             = ( 0x67, 0x02000000, 25 ) # MSLUT[7]
	OFS250             = ( 0x67, 0x04000000, 26 ) # MSLUT[7]
	OFS251             = ( 0x67, 0x08000000, 27 ) # MSLUT[7]
	OFS252             = ( 0x67, 0x10000000, 28 ) # MSLUT[7]
	OFS253             = ( 0x67, 0x20000000, 29 ) # MSLUT[7]
	OFS254             = ( 0x67, 0x40000000, 30 ) # MSLUT[7]
	OFS255             = ( 0x67, 0x80000000, 31 ) # MSLUT[7]

	# MSLUTSEL
	W0                 = ( 0x68, 0x00000003,  0 ) # MSLUTSEL
	W1                 = ( 0x68, 0x0000000C,  2 ) # MSLUTSEL
	W2                 = ( 0x68, 0x00000030,  4 ) # MSLUTSEL
	W3                 = ( 0x68, 0x000000C0,  6 ) # MSLUTSEL
	X1                 = ( 0x68, 0x0000FF00,  8 ) # MSLUTSEL
	X2                 = ( 0x68, 0x00FF0000, 16 ) # MSLUTSEL
	X3                 = ( 0x68, 0xFF000000, 24 ) # MSLUTSEL

	# MSLUTSTART
	START_SIN          = ( 0x69, 0x000000FF,  0 ) # MSLUTSTART
	START_SIN90        = ( 0x69, 0x00FF0000, 16 ) # MSLUTSTART

	# MSCNT_M1
	MSCNT              = ( 0x6A, 0x000003FF,  0 ) # MSCNT_M1

	# MSCURACT_M1
	CUR_A              = ( 0x6B, 0x000001FF,  0 ) # MSCURACT_M1
	CUR_B              = ( 0x6B, 0x01FF0000, 16 ) # MSCURACT_M1

	# CHOPCONF_M1
	TOFF               = ( 0x6C, 0x0000000F,  0 ) # CHOPCONF_M1
	TFD_2__0_          = ( 0x6C, 0x00000070,  4 ) # CHOPCONF_M1
	OFFSET             = ( 0x6C, 0x00000780,  7 ) # CHOPCONF_M1
	TFD__              = ( 0x6C, 0x00000800, 11 ) # CHOPCONF_M1
	DISFDCC            = ( 0x6C, 0x00001000, 12 ) # CHOPCONF_M1
	RNDTF              = ( 0x6C, 0x00002000, 13 ) # CHOPCONF_M1
	CHM                = ( 0x6C, 0x00004000, 14 ) # CHOPCONF_M1
	TBL                = ( 0x6C, 0x00018000, 15 ) # CHOPCONF_M1
	VSENSE             = ( 0x6C, 0x00020000, 17 ) # CHOPCONF_M1
	VHIGHFS            = ( 0x6C, 0x00040000, 18 ) # CHOPCONF_M1
	VHIGHCHM           = ( 0x6C, 0x00080000, 19 ) # CHOPCONF_M1
	MRES               = ( 0x6C, 0x0F000000, 24 ) # CHOPCONF_M1
	INTPOL             = ( 0x6C, 0x10000000, 28 ) # CHOPCONF_M1
	DEDGE              = ( 0x6C, 0x20000000, 29 ) # CHOPCONF_M1
	DISS2G             = ( 0x6C, 0x40000000, 30 ) # CHOPCONF_M1
	TOFF               = ( 0x6C, 0x0000000F,  0 ) # CHOPCONF_M1
	TFD_2__0_          = ( 0x6C, 0x00000070,  4 ) # CHOPCONF_M1
	OFFSET             = ( 0x6C, 0x00000780,  7 ) # CHOPCONF_M1
	TFD__              = ( 0x6C, 0x00000800, 11 ) # CHOPCONF_M1
	DISFDCC            = ( 0x6C, 0x00001000, 12 ) # CHOPCONF_M1
	RNDTF              = ( 0x6C, 0x00002000, 13 ) # CHOPCONF_M1
	CHM                = ( 0x6C, 0x00004000, 14 ) # CHOPCONF_M1
	TBL                = ( 0x6C, 0x00018000, 15 ) # CHOPCONF_M1
	VSENSE             = ( 0x6C, 0x00020000, 17 ) # CHOPCONF_M1
	VHIGHFS            = ( 0x6C, 0x00040000, 18 ) # CHOPCONF_M1
	VHIGHCHM           = ( 0x6C, 0x00080000, 19 ) # CHOPCONF_M1
	MRES               = ( 0x6C, 0x0F000000, 24 ) # CHOPCONF_M1
	INTPOL             = ( 0x6C, 0x10000000, 28 ) # CHOPCONF_M1
	DEDGE              = ( 0x6C, 0x20000000, 29 ) # CHOPCONF_M1
	DISS2G             = ( 0x6C, 0x40000000, 30 ) # CHOPCONF_M1
	TOFF               = ( 0x6C, 0x0000000F,  0 ) # CHOPCONF_M1
	HSTRT              = ( 0x6C, 0x00000070,  4 ) # CHOPCONF_M1
	HEND               = ( 0x6C, 0x00000780,  7 ) # CHOPCONF_M1
	RNDTF              = ( 0x6C, 0x00002000, 13 ) # CHOPCONF_M1
	CHM                = ( 0x6C, 0x00004000, 14 ) # CHOPCONF_M1
	TBL                = ( 0x6C, 0x00018000, 15 ) # CHOPCONF_M1
	VSENSE             = ( 0x6C, 0x00020000, 17 ) # CHOPCONF_M1
	VHIGHFS            = ( 0x6C, 0x00040000, 18 ) # CHOPCONF_M1
	VHIGHCHM           = ( 0x6C, 0x00080000, 19 ) # CHOPCONF_M1
	MRES               = ( 0x6C, 0x0F000000, 24 ) # CHOPCONF_M1
	INTPOL             = ( 0x6C, 0x10000000, 28 ) # CHOPCONF_M1
	DEDGE              = ( 0x6C, 0x20000000, 29 ) # CHOPCONF_M1
	DISS2G             = ( 0x6C, 0x40000000, 30 ) # CHOPCONF_M1

	# COOLCONF_M1
	SEMIN              = ( 0x6D, 0x0000000F,  0 ) # COOLCONF_M1
	SEUP               = ( 0x6D, 0x00000060,  5 ) # COOLCONF_M1
	SEMAX              = ( 0x6D, 0x00000F00,  8 ) # COOLCONF_M1
	SEDN               = ( 0x6D, 0x00006000, 13 ) # COOLCONF_M1
	SEIMIN             = ( 0x6D, 0x00008000, 15 ) # COOLCONF_M1
	SGT                = ( 0x6D, 0x007F0000, 16 ) # COOLCONF_M1
	SFILT              = ( 0x6D, 0x01000000, 24 ) # COOLCONF_M1

	# DCCTRL_M1
	DC_TIME            = ( 0x6E, 0x000003FF,  0 ) # DCCTRL_M1
	DC_SG              = ( 0x6E, 0x00FF0000, 16 ) # DCCTRL_M1

	# DRV_STATUS_M1
	SG_RESULT          = ( 0x6F, 0x000003FF,  0 ) # DRV_STATUS_M1
	FSACTIVE           = ( 0x6F, 0x00008000, 15 ) # DRV_STATUS_M1
	CS_ACTUAL          = ( 0x6F, 0x001F0000, 16 ) # DRV_STATUS_M1
	STALLGUARD         = ( 0x6F, 0x01000000, 24 ) # DRV_STATUS_M1
	OT                 = ( 0x6F, 0x02000000, 25 ) # DRV_STATUS_M1
	OTPW               = ( 0x6F, 0x04000000, 26 ) # DRV_STATUS_M1
	S2GA               = ( 0x6F, 0x08000000, 27 ) # DRV_STATUS_M1
	S2GB               = ( 0x6F, 0x10000000, 28 ) # DRV_STATUS_M1
	OLA                = ( 0x6F, 0x20000000, 29 ) # DRV_STATUS_M1
	OLB                = ( 0x6F, 0x40000000, 30 ) # DRV_STATUS_M1
	STST               = ( 0x6F, 0x80000000, 31 ) # DRV_STATUS_M1

	# MSCNT_M2
	MSCNT              = ( 0x7A, 0x000003FF,  0 ) # MSCNT_M2

	# MSCURACT_M2
	CUR_A              = ( 0x7B, 0x000001FF,  0 ) # MSCURACT_M2
	CUR_B              = ( 0x7B, 0x01FF0000, 16 ) # MSCURACT_M2

	# CHOPCONF_M2
	TOFF               = ( 0x7C, 0x0000000F,  0 ) # CHOPCONF_M2
	TFD_2__0_          = ( 0x7C, 0x00000070,  4 ) # CHOPCONF_M2
	OFFSET             = ( 0x7C, 0x00000780,  7 ) # CHOPCONF_M2
	TFD__              = ( 0x7C, 0x00000800, 11 ) # CHOPCONF_M2
	DISFDCC            = ( 0x7C, 0x00001000, 12 ) # CHOPCONF_M2
	RNDTF              = ( 0x7C, 0x00002000, 13 ) # CHOPCONF_M2
	CHM                = ( 0x7C, 0x00004000, 14 ) # CHOPCONF_M2
	TBL                = ( 0x7C, 0x00018000, 15 ) # CHOPCONF_M2
	VSENSE             = ( 0x7C, 0x00020000, 17 ) # CHOPCONF_M2
	VHIGHFS            = ( 0x7C, 0x00040000, 18 ) # CHOPCONF_M2
	VHIGHCHM           = ( 0x7C, 0x00080000, 19 ) # CHOPCONF_M2
	MRES               = ( 0x7C, 0x0F000000, 24 ) # CHOPCONF_M2
	INTPOL             = ( 0x7C, 0x10000000, 28 ) # CHOPCONF_M2
	DEDGE              = ( 0x7C, 0x20000000, 29 ) # CHOPCONF_M2
	DISS2G             = ( 0x7C, 0x40000000, 30 ) # CHOPCONF_M2
	TOFF               = ( 0x7C, 0x0000000F,  0 ) # CHOPCONF_M2
	TFD_2__0_          = ( 0x7C, 0x00000070,  4 ) # CHOPCONF_M2
	OFFSET             = ( 0x7C, 0x00000780,  7 ) # CHOPCONF_M2
	TFD__              = ( 0x7C, 0x00000800, 11 ) # CHOPCONF_M2
	DISFDCC            = ( 0x7C, 0x00001000, 12 ) # CHOPCONF_M2
	RNDTF              = ( 0x7C, 0x00002000, 13 ) # CHOPCONF_M2
	CHM                = ( 0x7C, 0x00004000, 14 ) # CHOPCONF_M2
	TBL                = ( 0x7C, 0x00018000, 15 ) # CHOPCONF_M2
	VSENSE             = ( 0x7C, 0x00020000, 17 ) # CHOPCONF_M2
	VHIGHFS            = ( 0x7C, 0x00040000, 18 ) # CHOPCONF_M2
	VHIGHCHM           = ( 0x7C, 0x00080000, 19 ) # CHOPCONF_M2
	MRES               = ( 0x7C, 0x0F000000, 24 ) # CHOPCONF_M2
	INTPOL             = ( 0x7C, 0x10000000, 28 ) # CHOPCONF_M2
	DEDGE              = ( 0x7C, 0x20000000, 29 ) # CHOPCONF_M2
	DISS2G             = ( 0x7C, 0x40000000, 30 ) # CHOPCONF_M2
	TOFF               = ( 0x7C, 0x0000000F,  0 ) # CHOPCONF_M2
	HSTRT              = ( 0x7C, 0x00000070,  4 ) # CHOPCONF_M2
	HEND               = ( 0x7C, 0x00000780,  7 ) # CHOPCONF_M2
	RNDTF              = ( 0x7C, 0x00002000, 13 ) # CHOPCONF_M2
	CHM                = ( 0x7C, 0x00004000, 14 ) # CHOPCONF_M2
	TBL                = ( 0x7C, 0x00018000, 15 ) # CHOPCONF_M2
	VSENSE             = ( 0x7C, 0x00020000, 17 ) # CHOPCONF_M2
	VHIGHFS            = ( 0x7C, 0x00040000, 18 ) # CHOPCONF_M2
	VHIGHCHM           = ( 0x7C, 0x00080000, 19 ) # CHOPCONF_M2
	MRES               = ( 0x7C, 0x0F000000, 24 ) # CHOPCONF_M2
	INTPOL             = ( 0x7C, 0x10000000, 28 ) # CHOPCONF_M2
	DEDGE              = ( 0x7C, 0x20000000, 29 ) # CHOPCONF_M2
	DISS2G             = ( 0x7C, 0x40000000, 30 ) # CHOPCONF_M2

	# COOLCONF_M2
	SEMIN              = ( 0x7D, 0x0000000F,  0 ) # COOLCONF_M2
	SEUP               = ( 0x7D, 0x00000060,  5 ) # COOLCONF_M2
	SEMAX              = ( 0x7D, 0x00000F00,  8 ) # COOLCONF_M2
	SEDN               = ( 0x7D, 0x00006000, 13 ) # COOLCONF_M2
	SEIMIN             = ( 0x7D, 0x00008000, 15 ) # COOLCONF_M2
	SGT                = ( 0x7D, 0x007F0000, 16 ) # COOLCONF_M2
	SFILT              = ( 0x7D, 0x01000000, 24 ) # COOLCONF_M2

	# DCCTRL_M2
	DC_TIME            = ( 0x7E, 0x000003FF,  0 ) # DCCTRL_M2
	DC_SG              = ( 0x7E, 0x00FF0000, 16 ) # DCCTRL_M2

	# DRV_STATUS_M2
	SG_RESULT          = ( 0x7F, 0x000003FF,  0 ) # DRV_STATUS_M2
	FSACTIVE           = ( 0x7F, 0x00008000, 15 ) # DRV_STATUS_M2
	CS_ACTUAL          = ( 0x7F, 0x001F0000, 16 ) # DRV_STATUS_M2
	STALLGUARD         = ( 0x7F, 0x01000000, 24 ) # DRV_STATUS_M2
	OT                 = ( 0x7F, 0x02000000, 25 ) # DRV_STATUS_M2
	OTPW               = ( 0x7F, 0x04000000, 26 ) # DRV_STATUS_M2
	S2GA               = ( 0x7F, 0x08000000, 27 ) # DRV_STATUS_M2
	S2GB               = ( 0x7F, 0x10000000, 28 ) # DRV_STATUS_M2
	OLA                = ( 0x7F, 0x20000000, 29 ) # DRV_STATUS_M2
	OLB                = ( 0x7F, 0x40000000, 30 ) # DRV_STATUS_M2
	STST               = ( 0x7F, 0x80000000, 31 ) # DRV_STATUS_M2
