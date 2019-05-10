'''
Created on 18.04.2019

@author: LH
'''

class TMC5041_fields(object):
	"""
	Define all register bitfields of the TMC5041.

	Each field is defined as a tuple consisting of ( Address, Mask, Shift ).
	Fields that are present multiple times in different registers (for multiple
	motors) all of the bitfield tuples are bundled together into another tuple.

	The name of the register is written as a comment behind each tuple. This is
	intended for IDE users viewing the definition of a field by hovering over
	it. This allows the user to see the corresponding register name of a field
	without opening this file and searching for the definition.
	"""
	# GCONF
	POSCMP_ENABLE      =  ( 0x00, 0x00000008,  3 ) # GCONF
	TEST_MODE          =  ( 0x00, 0x00000080,  7 ) # GCONF
	SHAFT1             =  ( 0x00, 0x00000100,  8 ) # GCONF
	SHAFT2             =  ( 0x00, 0x00000200,  9 ) # GCONF
	LOCK_GCONF         =  ( 0x00, 0x00000400, 10 ) # GCONF

	# GSTAT
	RESET              =  ( 0x01, 0x00000001,  0 ) # GSTAT
	DRV_ERR1           =  ( 0x01, 0x00000002,  1 ) # GSTAT
	DRV_ERR2           =  ( 0x01, 0x00000004,  2 ) # GSTAT
	UV_CP              =  ( 0x01, 0x00000008,  3 ) # GSTAT

	# TEST_SEL
	TEST_SEL           =  ( 0x03, 0x0000000F,  0 ) # TEST_SEL

	# INPUT
	DRV_ENN            =  ( 0x04, 0x00000080,  7 ) # INPUT
	VERSION            =  ( 0x04, 0xFF000000, 24 ) # INPUT

	# X_COMPARE
	X_COMPARE          =  ( 0x05, 0xFFFFFFFF,  0 ) # X_COMPARE

	# PWMCONF
	PWM_AMPL           = (( 0x10, 0x000000FF,  0 ), ( 0x18, 0x000000FF,  0 )) # PWMCONF
	PWM_GRAD           = (( 0x10, 0x0000FF00,  8 ), ( 0x18, 0x0000FF00,  8 )) # PWMCONF
	PWM_FREQ           = (( 0x10, 0x00030000, 16 ), ( 0x18, 0x00030000, 16 )) # PWMCONF
	PWM_AUTOSCALE      = (( 0x10, 0x00040000, 18 ), ( 0x18, 0x00040000, 18 )) # PWMCONF
	PWM_SYMMETRIC      = (( 0x10, 0x00080000, 19 ), ( 0x18, 0x00080000, 19 )) # PWMCONF
	FREEWHEEL          = (( 0x10, 0x00300000, 20 ), ( 0x18, 0x00300000, 20 )) # PWMCONF

	# PWM_STATUS
	PWM_STATUS         = (( 0x11, 0x000000FF,  0 ), ( 0x19, 0x000000FF,  0 )) # PWM_STATUS

	# RAMPMODE
	RAMPMODE           = (( 0x20, 0x00000003,  0 ), ( 0x40, 0x00000003,  0 )) # RAMPMODE

	# XACTUAL
	XACTUAL            = (( 0x21, 0xFFFFFFFF,  0 ), ( 0x41, 0xFFFFFFFF,  0 )) # XACTUAL

	# VACTUAL
	VACTUAL            = (( 0x22, 0x00FFFFFF,  0 ), ( 0x42, 0x00FFFFFF,  0 )) # VACTUAL

	# VSTART
	VSTART             = (( 0x23, 0x0003FFFF,  0 ), ( 0x43, 0x0003FFFF,  0 )) # VSTART

	# A1
	A1                 = (( 0x24, 0x0000FFFF,  0 ), ( 0x44, 0x0000FFFF,  0 )) # A1

	# V1
	V1                 = (( 0x25, 0x000FFFFF,  0 ), ( 0x45, 0x000FFFFF,  0 )) # V1

	# AMAX
	AMAX               = (( 0x26, 0x0000FFFF,  0 ), ( 0x46, 0x0000FFFF,  0 )) # AMAX

	# VMAX
	VMAX               = (( 0x27, 0x007FFFFF,  0 ), ( 0x47, 0x007FFFFF,  0 )) # VMAX

	# DMAX
	DMAX               = (( 0x28, 0x0000FFFF,  0 ), ( 0x48, 0x0000FFFF,  0 )) # DMAX

	# D1
	D1                 = (( 0x2A, 0x0000FFFF,  0 ), ( 0x4A, 0x0000FFFF,  0 )) # D1

	# VSTOP
	VSTOP              = (( 0x2B, 0x0003FFFF,  0 ), ( 0x4B, 0x0003FFFF,  0 )) # VSTOP

	# TZEROWAIT
	TZEROWAIT          = (( 0x2C, 0x0000FFFF,  0 ), ( 0x4C, 0x0000FFFF,  0 )) # TZEROWAIT

	# XTARGET
	XTARGET            = (( 0x2D, 0xFFFFFFFF,  0 ), ( 0x4D, 0xFFFFFFFF,  0 )) # XTARGET

	# IHOLD_IRUN
	IHOLD              = (( 0x30, 0x0000001F,  0 ), ( 0x50, 0x0000001F,  0 )) # IHOLD_IRUN
	IRUN               = (( 0x30, 0x00001F00,  8 ), ( 0x50, 0x00001F00,  8 )) # IHOLD_IRUN
	IHOLDDELAY         = (( 0x30, 0x000F0000, 16 ), ( 0x50, 0x000F0000, 16 )) # IHOLD_IRUN

	# VCOOLTHRS
	VCOOLTHRS          = (( 0x31, 0x007FFFFF,  0 ), ( 0x51, 0x007FFFFF,  0 )) # VCOOLTHRS

	# VHIGH
	VHIGH              = (( 0x32, 0x007FFFFF,  0 ), ( 0x52, 0x007FFFFF,  0 )) # VHIGH

	# SW_MODE
	STOP_L_ENABLE      = (( 0x34, 0x00000001,  0 ), ( 0x54, 0x00000001,  0 )) # SW_MODE
	STOP_R_ENABLE      = (( 0x34, 0x00000002,  1 ), ( 0x54, 0x00000002,  1 )) # SW_MODE
	POL_STOP_L         = (( 0x34, 0x00000004,  2 ), ( 0x54, 0x00000004,  2 )) # SW_MODE
	POL_STOP_R         = (( 0x34, 0x00000008,  3 ), ( 0x54, 0x00000008,  3 )) # SW_MODE
	SWAP_LR            = (( 0x34, 0x00000010,  4 ), ( 0x54, 0x00000010,  4 )) # SW_MODE
	LATCH_L_ACTIVE     = (( 0x34, 0x00000020,  5 ), ( 0x54, 0x00000020,  5 )) # SW_MODE
	LATCH_L_INACTIVE   = (( 0x34, 0x00000040,  6 ), ( 0x54, 0x00000040,  6 )) # SW_MODE
	LATCH_R_ACTIVE     = (( 0x34, 0x00000080,  7 ), ( 0x54, 0x00000080,  7 )) # SW_MODE
	LATCH_R_INACTIVE   = (( 0x34, 0x00000100,  8 ), ( 0x54, 0x00000100,  8 )) # SW_MODE
	SG_STOP            = (( 0x34, 0x00000400, 10 ), ( 0x54, 0x00000400, 10 )) # SW_MODE
	EN_SOFTSTOP        = (( 0x34, 0x00000800, 11 ), ( 0x54, 0x00000800, 11 )) # SW_MODE

	# RAMP_STAT
	STATUS_STOP_L      = (( 0x35, 0x00000001,  0 ), ( 0x55, 0x00000001,  0 )) # RAMP_STAT
	STATUS_STOP_R      = (( 0x35, 0x00000002,  1 ), ( 0x55, 0x00000002,  1 )) # RAMP_STAT
	STATUS_LATCH_L     = (( 0x35, 0x00000004,  2 ), ( 0x55, 0x00000004,  2 )) # RAMP_STAT
	STATUS_LATCH_R     = (( 0x35, 0x00000008,  3 ), ( 0x55, 0x00000008,  3 )) # RAMP_STAT
	EVENT_STOP_L       = (( 0x35, 0x00000010,  4 ), ( 0x55, 0x00000010,  4 )) # RAMP_STAT
	EVENT_STOP_R       = (( 0x35, 0x00000020,  5 ), ( 0x55, 0x00000020,  5 )) # RAMP_STAT
	EVENT_STOP_SG      = (( 0x35, 0x00000040,  6 ), ( 0x55, 0x00000040,  6 )) # RAMP_STAT
	EVENT_POS_REACHED  = (( 0x35, 0x00000080,  7 ), ( 0x55, 0x00000080,  7 )) # RAMP_STAT
	VELOCITY_REACHED   = (( 0x35, 0x00000100,  8 ), ( 0x55, 0x00000100,  8 )) # RAMP_STAT
	POSITION_REACHED   = (( 0x35, 0x00000200,  9 ), ( 0x55, 0x00000200,  9 )) # RAMP_STAT
	VZERO              = (( 0x35, 0x00000400, 10 ), ( 0x55, 0x00000400, 10 )) # RAMP_STAT
	T_ZEROWAIT_ACTIVE  = (( 0x35, 0x00000800, 11 ), ( 0x55, 0x00000800, 11 )) # RAMP_STAT
	SECOND_MOVE        = (( 0x35, 0x00001000, 12 ), ( 0x55, 0x00001000, 12 )) # RAMP_STAT
	STATUS_SG          = (( 0x35, 0x00002000, 13 ), ( 0x55, 0x00002000, 13 )) # RAMP_STAT

	# XLATCH
	XLATCH             = (( 0x36, 0xFFFFFFFF,  0 ), ( 0x56, 0xFFFFFFFF,  0 )) # XLATCH

	# MSLUT[0]
	OFS0               =  ( 0x60, 0x00000001,  0 ) # MSLUT[0]
	OFS1               =  ( 0x60, 0x00000002,  1 ) # MSLUT[0]
	OFS2               =  ( 0x60, 0x00000004,  2 ) # MSLUT[0]
	OFS3               =  ( 0x60, 0x00000008,  3 ) # MSLUT[0]
	OFS4               =  ( 0x60, 0x00000010,  4 ) # MSLUT[0]
	OFS5               =  ( 0x60, 0x00000020,  5 ) # MSLUT[0]
	OFS6               =  ( 0x60, 0x00000040,  6 ) # MSLUT[0]
	OFS7               =  ( 0x60, 0x00000080,  7 ) # MSLUT[0]
	OFS8               =  ( 0x60, 0x00000100,  8 ) # MSLUT[0]
	OFS9               =  ( 0x60, 0x00000200,  9 ) # MSLUT[0]
	OFS10              =  ( 0x60, 0x00000400, 10 ) # MSLUT[0]
	OFS11              =  ( 0x60, 0x00000800, 11 ) # MSLUT[0]
	OFS12              =  ( 0x60, 0x00001000, 12 ) # MSLUT[0]
	OFS13              =  ( 0x60, 0x00002000, 13 ) # MSLUT[0]
	OFS14              =  ( 0x60, 0x00004000, 14 ) # MSLUT[0]
	OFS15              =  ( 0x60, 0x00008000, 15 ) # MSLUT[0]
	OFS16              =  ( 0x60, 0x00010000, 16 ) # MSLUT[0]
	OFS17              =  ( 0x60, 0x00020000, 17 ) # MSLUT[0]
	OFS18              =  ( 0x60, 0x00040000, 18 ) # MSLUT[0]
	OFS19              =  ( 0x60, 0x00080000, 19 ) # MSLUT[0]
	OFS20              =  ( 0x60, 0x00100000, 20 ) # MSLUT[0]
	OFS21              =  ( 0x60, 0x00200000, 21 ) # MSLUT[0]
	OFS22              =  ( 0x60, 0x00400000, 22 ) # MSLUT[0]
	OFS23              =  ( 0x60, 0x00800000, 23 ) # MSLUT[0]
	OFS24              =  ( 0x60, 0x01000000, 24 ) # MSLUT[0]
	OFS25              =  ( 0x60, 0x02000000, 25 ) # MSLUT[0]
	OFS26              =  ( 0x60, 0x04000000, 26 ) # MSLUT[0]
	OFS27              =  ( 0x60, 0x08000000, 27 ) # MSLUT[0]
	OFS28              =  ( 0x60, 0x10000000, 28 ) # MSLUT[0]
	OFS29              =  ( 0x60, 0x20000000, 29 ) # MSLUT[0]
	OFS30              =  ( 0x60, 0x40000000, 30 ) # MSLUT[0]
	OFS31              =  ( 0x60, 0x80000000, 31 ) # MSLUT[0]

	# MSLUT[1]
	OFS32              =  ( 0x61, 0x00000001,  0 ) # MSLUT[1]
	OFS33              =  ( 0x61, 0x00000002,  1 ) # MSLUT[1]
	OFS34              =  ( 0x61, 0x00000004,  2 ) # MSLUT[1]
	OFS35              =  ( 0x61, 0x00000008,  3 ) # MSLUT[1]
	OFS36              =  ( 0x61, 0x00000010,  4 ) # MSLUT[1]
	OFS37              =  ( 0x61, 0x00000020,  5 ) # MSLUT[1]
	OFS38              =  ( 0x61, 0x00000040,  6 ) # MSLUT[1]
	OFS39              =  ( 0x61, 0x00000080,  7 ) # MSLUT[1]
	OFS40              =  ( 0x61, 0x00000100,  8 ) # MSLUT[1]
	OFS41              =  ( 0x61, 0x00000200,  9 ) # MSLUT[1]
	OFS42              =  ( 0x61, 0x00000400, 10 ) # MSLUT[1]
	OFS43              =  ( 0x61, 0x00000800, 11 ) # MSLUT[1]
	OFS44              =  ( 0x61, 0x00001000, 12 ) # MSLUT[1]
	OFS45              =  ( 0x61, 0x00002000, 13 ) # MSLUT[1]
	OFS46              =  ( 0x61, 0x00004000, 14 ) # MSLUT[1]
	OFS47              =  ( 0x61, 0x00008000, 15 ) # MSLUT[1]
	OFS48              =  ( 0x61, 0x00010000, 16 ) # MSLUT[1]
	OFS49              =  ( 0x61, 0x00020000, 17 ) # MSLUT[1]
	OFS50              =  ( 0x61, 0x00040000, 18 ) # MSLUT[1]
	OFS51              =  ( 0x61, 0x00080000, 19 ) # MSLUT[1]
	OFS52              =  ( 0x61, 0x00100000, 20 ) # MSLUT[1]
	OFS53              =  ( 0x61, 0x00200000, 21 ) # MSLUT[1]
	OFS54              =  ( 0x61, 0x00400000, 22 ) # MSLUT[1]
	OFS55              =  ( 0x61, 0x00800000, 23 ) # MSLUT[1]
	OFS56              =  ( 0x61, 0x01000000, 24 ) # MSLUT[1]
	OFS57              =  ( 0x61, 0x02000000, 25 ) # MSLUT[1]
	OFS58              =  ( 0x61, 0x04000000, 26 ) # MSLUT[1]
	OFS59              =  ( 0x61, 0x08000000, 27 ) # MSLUT[1]
	OFS60              =  ( 0x61, 0x10000000, 28 ) # MSLUT[1]
	OFS61              =  ( 0x61, 0x20000000, 29 ) # MSLUT[1]
	OFS62              =  ( 0x61, 0x40000000, 30 ) # MSLUT[1]
	OFS63              =  ( 0x61, 0x80000000, 31 ) # MSLUT[1]

	# MSLUT[2]
	OFS64              =  ( 0x62, 0x00000001,  0 ) # MSLUT[2]
	OFS65              =  ( 0x62, 0x00000002,  1 ) # MSLUT[2]
	OFS66              =  ( 0x62, 0x00000004,  2 ) # MSLUT[2]
	OFS67              =  ( 0x62, 0x00000008,  3 ) # MSLUT[2]
	OFS68              =  ( 0x62, 0x00000010,  4 ) # MSLUT[2]
	OFS69              =  ( 0x62, 0x00000020,  5 ) # MSLUT[2]
	OFS70              =  ( 0x62, 0x00000040,  6 ) # MSLUT[2]
	OFS71              =  ( 0x62, 0x00000080,  7 ) # MSLUT[2]
	OFS72              =  ( 0x62, 0x00000100,  8 ) # MSLUT[2]
	OFS73              =  ( 0x62, 0x00000200,  9 ) # MSLUT[2]
	OFS74              =  ( 0x62, 0x00000400, 10 ) # MSLUT[2]
	OFS75              =  ( 0x62, 0x00000800, 11 ) # MSLUT[2]
	OFS76              =  ( 0x62, 0x00001000, 12 ) # MSLUT[2]
	OFS77              =  ( 0x62, 0x00002000, 13 ) # MSLUT[2]
	OFS78              =  ( 0x62, 0x00004000, 14 ) # MSLUT[2]
	OFS79              =  ( 0x62, 0x00008000, 15 ) # MSLUT[2]
	OFS80              =  ( 0x62, 0x00010000, 16 ) # MSLUT[2]
	OFS81              =  ( 0x62, 0x00020000, 17 ) # MSLUT[2]
	OFS82              =  ( 0x62, 0x00040000, 18 ) # MSLUT[2]
	OFS83              =  ( 0x62, 0x00080000, 19 ) # MSLUT[2]
	OFS84              =  ( 0x62, 0x00100000, 20 ) # MSLUT[2]
	OFS85              =  ( 0x62, 0x00200000, 21 ) # MSLUT[2]
	OFS86              =  ( 0x62, 0x00400000, 22 ) # MSLUT[2]
	OFS87              =  ( 0x62, 0x00800000, 23 ) # MSLUT[2]
	OFS88              =  ( 0x62, 0x01000000, 24 ) # MSLUT[2]
	OFS89              =  ( 0x62, 0x02000000, 25 ) # MSLUT[2]
	OFS90              =  ( 0x62, 0x04000000, 26 ) # MSLUT[2]
	OFS91              =  ( 0x62, 0x08000000, 27 ) # MSLUT[2]
	OFS92              =  ( 0x62, 0x10000000, 28 ) # MSLUT[2]
	OFS93              =  ( 0x62, 0x20000000, 29 ) # MSLUT[2]
	OFS94              =  ( 0x62, 0x40000000, 30 ) # MSLUT[2]
	OFS95              =  ( 0x62, 0x80000000, 31 ) # MSLUT[2]

	# MSLUT[3]
	OFS96              =  ( 0x63, 0x00000001,  0 ) # MSLUT[3]
	OFS97              =  ( 0x63, 0x00000002,  1 ) # MSLUT[3]
	OFS98              =  ( 0x63, 0x00000004,  2 ) # MSLUT[3]
	OFS99              =  ( 0x63, 0x00000008,  3 ) # MSLUT[3]
	OFS100             =  ( 0x63, 0x00000010,  4 ) # MSLUT[3]
	OFS101             =  ( 0x63, 0x00000020,  5 ) # MSLUT[3]
	OFS102             =  ( 0x63, 0x00000040,  6 ) # MSLUT[3]
	OFS103             =  ( 0x63, 0x00000080,  7 ) # MSLUT[3]
	OFS104             =  ( 0x63, 0x00000100,  8 ) # MSLUT[3]
	OFS105             =  ( 0x63, 0x00000200,  9 ) # MSLUT[3]
	OFS106             =  ( 0x63, 0x00000400, 10 ) # MSLUT[3]
	OFS107             =  ( 0x63, 0x00000800, 11 ) # MSLUT[3]
	OFS108             =  ( 0x63, 0x00001000, 12 ) # MSLUT[3]
	OFS109             =  ( 0x63, 0x00002000, 13 ) # MSLUT[3]
	OFS110             =  ( 0x63, 0x00004000, 14 ) # MSLUT[3]
	OFS111             =  ( 0x63, 0x00008000, 15 ) # MSLUT[3]
	OFS112             =  ( 0x63, 0x00010000, 16 ) # MSLUT[3]
	OFS113             =  ( 0x63, 0x00020000, 17 ) # MSLUT[3]
	OFS114             =  ( 0x63, 0x00040000, 18 ) # MSLUT[3]
	OFS115             =  ( 0x63, 0x00080000, 19 ) # MSLUT[3]
	OFS116             =  ( 0x63, 0x00100000, 20 ) # MSLUT[3]
	OFS117             =  ( 0x63, 0x00200000, 21 ) # MSLUT[3]
	OFS118             =  ( 0x63, 0x00400000, 22 ) # MSLUT[3]
	OFS119             =  ( 0x63, 0x00800000, 23 ) # MSLUT[3]
	OFS120             =  ( 0x63, 0x01000000, 24 ) # MSLUT[3]
	OFS121             =  ( 0x63, 0x02000000, 25 ) # MSLUT[3]
	OFS122             =  ( 0x63, 0x04000000, 26 ) # MSLUT[3]
	OFS123             =  ( 0x63, 0x08000000, 27 ) # MSLUT[3]
	OFS124             =  ( 0x63, 0x10000000, 28 ) # MSLUT[3]
	OFS125             =  ( 0x63, 0x20000000, 29 ) # MSLUT[3]
	OFS126             =  ( 0x63, 0x40000000, 30 ) # MSLUT[3]
	OFS127             =  ( 0x63, 0x80000000, 31 ) # MSLUT[3]

	# MSLUT[4]
	OFS128             =  ( 0x64, 0x00000001,  0 ) # MSLUT[4]
	OFS129             =  ( 0x64, 0x00000002,  1 ) # MSLUT[4]
	OFS130             =  ( 0x64, 0x00000004,  2 ) # MSLUT[4]
	OFS131             =  ( 0x64, 0x00000008,  3 ) # MSLUT[4]
	OFS132             =  ( 0x64, 0x00000010,  4 ) # MSLUT[4]
	OFS133             =  ( 0x64, 0x00000020,  5 ) # MSLUT[4]
	OFS134             =  ( 0x64, 0x00000040,  6 ) # MSLUT[4]
	OFS135             =  ( 0x64, 0x00000080,  7 ) # MSLUT[4]
	OFS136             =  ( 0x64, 0x00000100,  8 ) # MSLUT[4]
	OFS137             =  ( 0x64, 0x00000200,  9 ) # MSLUT[4]
	OFS138             =  ( 0x64, 0x00000400, 10 ) # MSLUT[4]
	OFS139             =  ( 0x64, 0x00000800, 11 ) # MSLUT[4]
	OFS140             =  ( 0x64, 0x00001000, 12 ) # MSLUT[4]
	OFS141             =  ( 0x64, 0x00002000, 13 ) # MSLUT[4]
	OFS142             =  ( 0x64, 0x00004000, 14 ) # MSLUT[4]
	OFS143             =  ( 0x64, 0x00008000, 15 ) # MSLUT[4]
	OFS144             =  ( 0x64, 0x00010000, 16 ) # MSLUT[4]
	OFS145             =  ( 0x64, 0x00020000, 17 ) # MSLUT[4]
	OFS146             =  ( 0x64, 0x00040000, 18 ) # MSLUT[4]
	OFS147             =  ( 0x64, 0x00080000, 19 ) # MSLUT[4]
	OFS148             =  ( 0x64, 0x00100000, 20 ) # MSLUT[4]
	OFS149             =  ( 0x64, 0x00200000, 21 ) # MSLUT[4]
	OFS150             =  ( 0x64, 0x00400000, 22 ) # MSLUT[4]
	OFS151             =  ( 0x64, 0x00800000, 23 ) # MSLUT[4]
	OFS152             =  ( 0x64, 0x01000000, 24 ) # MSLUT[4]
	OFS153             =  ( 0x64, 0x02000000, 25 ) # MSLUT[4]
	OFS154             =  ( 0x64, 0x04000000, 26 ) # MSLUT[4]
	OFS155             =  ( 0x64, 0x08000000, 27 ) # MSLUT[4]
	OFS156             =  ( 0x64, 0x10000000, 28 ) # MSLUT[4]
	OFS157             =  ( 0x64, 0x20000000, 29 ) # MSLUT[4]
	OFS158             =  ( 0x64, 0x40000000, 30 ) # MSLUT[4]
	OFS159             =  ( 0x64, 0x80000000, 31 ) # MSLUT[4]

	# MSLUT[5]
	OFS160             =  ( 0x65, 0x00000001,  0 ) # MSLUT[5]
	OFS161             =  ( 0x65, 0x00000002,  1 ) # MSLUT[5]
	OFS162             =  ( 0x65, 0x00000004,  2 ) # MSLUT[5]
	OFS163             =  ( 0x65, 0x00000008,  3 ) # MSLUT[5]
	OFS164             =  ( 0x65, 0x00000010,  4 ) # MSLUT[5]
	OFS165             =  ( 0x65, 0x00000020,  5 ) # MSLUT[5]
	OFS166             =  ( 0x65, 0x00000040,  6 ) # MSLUT[5]
	OFS167             =  ( 0x65, 0x00000080,  7 ) # MSLUT[5]
	OFS168             =  ( 0x65, 0x00000100,  8 ) # MSLUT[5]
	OFS169             =  ( 0x65, 0x00000200,  9 ) # MSLUT[5]
	OFS170             =  ( 0x65, 0x00000400, 10 ) # MSLUT[5]
	OFS171             =  ( 0x65, 0x00000800, 11 ) # MSLUT[5]
	OFS172             =  ( 0x65, 0x00001000, 12 ) # MSLUT[5]
	OFS173             =  ( 0x65, 0x00002000, 13 ) # MSLUT[5]
	OFS174             =  ( 0x65, 0x00004000, 14 ) # MSLUT[5]
	OFS175             =  ( 0x65, 0x00008000, 15 ) # MSLUT[5]
	OFS176             =  ( 0x65, 0x00010000, 16 ) # MSLUT[5]
	OFS177             =  ( 0x65, 0x00020000, 17 ) # MSLUT[5]
	OFS178             =  ( 0x65, 0x00040000, 18 ) # MSLUT[5]
	OFS179             =  ( 0x65, 0x00080000, 19 ) # MSLUT[5]
	OFS180             =  ( 0x65, 0x00100000, 20 ) # MSLUT[5]
	OFS181             =  ( 0x65, 0x00200000, 21 ) # MSLUT[5]
	OFS182             =  ( 0x65, 0x00400000, 22 ) # MSLUT[5]
	OFS183             =  ( 0x65, 0x00800000, 23 ) # MSLUT[5]
	OFS184             =  ( 0x65, 0x01000000, 24 ) # MSLUT[5]
	OFS185             =  ( 0x65, 0x02000000, 25 ) # MSLUT[5]
	OFS186             =  ( 0x65, 0x04000000, 26 ) # MSLUT[5]
	OFS187             =  ( 0x65, 0x08000000, 27 ) # MSLUT[5]
	OFS188             =  ( 0x65, 0x10000000, 28 ) # MSLUT[5]
	OFS189             =  ( 0x65, 0x20000000, 29 ) # MSLUT[5]
	OFS190             =  ( 0x65, 0x40000000, 30 ) # MSLUT[5]
	OFS191             =  ( 0x65, 0x80000000, 31 ) # MSLUT[5]

	# MSLUT[6]
	OFS192             =  ( 0x66, 0x00000001,  0 ) # MSLUT[6]
	OFS193             =  ( 0x66, 0x00000002,  1 ) # MSLUT[6]
	OFS194             =  ( 0x66, 0x00000004,  2 ) # MSLUT[6]
	OFS195             =  ( 0x66, 0x00000008,  3 ) # MSLUT[6]
	OFS196             =  ( 0x66, 0x00000010,  4 ) # MSLUT[6]
	OFS197             =  ( 0x66, 0x00000020,  5 ) # MSLUT[6]
	OFS198             =  ( 0x66, 0x00000040,  6 ) # MSLUT[6]
	OFS199             =  ( 0x66, 0x00000080,  7 ) # MSLUT[6]
	OFS200             =  ( 0x66, 0x00000100,  8 ) # MSLUT[6]
	OFS201             =  ( 0x66, 0x00000200,  9 ) # MSLUT[6]
	OFS202             =  ( 0x66, 0x00000400, 10 ) # MSLUT[6]
	OFS203             =  ( 0x66, 0x00000800, 11 ) # MSLUT[6]
	OFS204             =  ( 0x66, 0x00001000, 12 ) # MSLUT[6]
	OFS205             =  ( 0x66, 0x00002000, 13 ) # MSLUT[6]
	OFS206             =  ( 0x66, 0x00004000, 14 ) # MSLUT[6]
	OFS207             =  ( 0x66, 0x00008000, 15 ) # MSLUT[6]
	OFS208             =  ( 0x66, 0x00010000, 16 ) # MSLUT[6]
	OFS209             =  ( 0x66, 0x00020000, 17 ) # MSLUT[6]
	OFS210             =  ( 0x66, 0x00040000, 18 ) # MSLUT[6]
	OFS211             =  ( 0x66, 0x00080000, 19 ) # MSLUT[6]
	OFS212             =  ( 0x66, 0x00100000, 20 ) # MSLUT[6]
	OFS213             =  ( 0x66, 0x00200000, 21 ) # MSLUT[6]
	OFS214             =  ( 0x66, 0x00400000, 22 ) # MSLUT[6]
	OFS215             =  ( 0x66, 0x00800000, 23 ) # MSLUT[6]
	OFS216             =  ( 0x66, 0x01000000, 24 ) # MSLUT[6]
	OFS217             =  ( 0x66, 0x02000000, 25 ) # MSLUT[6]
	OFS218             =  ( 0x66, 0x04000000, 26 ) # MSLUT[6]
	OFS219             =  ( 0x66, 0x08000000, 27 ) # MSLUT[6]
	OFS220             =  ( 0x66, 0x10000000, 28 ) # MSLUT[6]
	OFS221             =  ( 0x66, 0x20000000, 29 ) # MSLUT[6]
	OFS222             =  ( 0x66, 0x40000000, 30 ) # MSLUT[6]
	OFS223             =  ( 0x66, 0x80000000, 31 ) # MSLUT[6]

	# MSLUT[7]
	OFS224             =  ( 0x67, 0x00000001,  0 ) # MSLUT[7]
	OFS225             =  ( 0x67, 0x00000002,  1 ) # MSLUT[7]
	OFS226             =  ( 0x67, 0x00000004,  2 ) # MSLUT[7]
	OFS227             =  ( 0x67, 0x00000008,  3 ) # MSLUT[7]
	OFS228             =  ( 0x67, 0x00000010,  4 ) # MSLUT[7]
	OFS229             =  ( 0x67, 0x00000020,  5 ) # MSLUT[7]
	OFS230             =  ( 0x67, 0x00000040,  6 ) # MSLUT[7]
	OFS231             =  ( 0x67, 0x00000080,  7 ) # MSLUT[7]
	OFS232             =  ( 0x67, 0x00000100,  8 ) # MSLUT[7]
	OFS233             =  ( 0x67, 0x00000200,  9 ) # MSLUT[7]
	OFS234             =  ( 0x67, 0x00000400, 10 ) # MSLUT[7]
	OFS235             =  ( 0x67, 0x00000800, 11 ) # MSLUT[7]
	OFS236             =  ( 0x67, 0x00001000, 12 ) # MSLUT[7]
	OFS237             =  ( 0x67, 0x00002000, 13 ) # MSLUT[7]
	OFS238             =  ( 0x67, 0x00004000, 14 ) # MSLUT[7]
	OFS239             =  ( 0x67, 0x00008000, 15 ) # MSLUT[7]
	OFS240             =  ( 0x67, 0x00010000, 16 ) # MSLUT[7]
	OFS241             =  ( 0x67, 0x00020000, 17 ) # MSLUT[7]
	OFS242             =  ( 0x67, 0x00040000, 18 ) # MSLUT[7]
	OFS243             =  ( 0x67, 0x00080000, 19 ) # MSLUT[7]
	OFS244             =  ( 0x67, 0x00100000, 20 ) # MSLUT[7]
	OFS245             =  ( 0x67, 0x00200000, 21 ) # MSLUT[7]
	OFS246             =  ( 0x67, 0x00400000, 22 ) # MSLUT[7]
	OFS247             =  ( 0x67, 0x00800000, 23 ) # MSLUT[7]
	OFS248             =  ( 0x67, 0x01000000, 24 ) # MSLUT[7]
	OFS249             =  ( 0x67, 0x02000000, 25 ) # MSLUT[7]
	OFS250             =  ( 0x67, 0x04000000, 26 ) # MSLUT[7]
	OFS251             =  ( 0x67, 0x08000000, 27 ) # MSLUT[7]
	OFS252             =  ( 0x67, 0x10000000, 28 ) # MSLUT[7]
	OFS253             =  ( 0x67, 0x20000000, 29 ) # MSLUT[7]
	OFS254             =  ( 0x67, 0x40000000, 30 ) # MSLUT[7]
	OFS255             =  ( 0x67, 0x80000000, 31 ) # MSLUT[7]

	# MSLUTSEL
	W0                 =  ( 0x68, 0x00000003,  0 ) # MSLUTSEL
	W1                 =  ( 0x68, 0x0000000C,  2 ) # MSLUTSEL
	W2                 =  ( 0x68, 0x00000030,  4 ) # MSLUTSEL
	W3                 =  ( 0x68, 0x000000C0,  6 ) # MSLUTSEL
	X1                 =  ( 0x68, 0x0000FF00,  8 ) # MSLUTSEL
	X2                 =  ( 0x68, 0x00FF0000, 16 ) # MSLUTSEL
	X3                 =  ( 0x68, 0xFF000000, 24 ) # MSLUTSEL

	# MSLUTSTART
	START_SIN          =  ( 0x69, 0x000000FF,  0 ) # MSLUTSTART
	START_SIN90        =  ( 0x69, 0x00FF0000, 16 ) # MSLUTSTART

	# MSCNT
	MSCNT              = (( 0x6A, 0x000003FF,  0 ), ( 0x7A, 0x000003FF,  0 )) # MSCNT

	# MSCURACT
	CUR_A              = (( 0x6B, 0x000001FF,  0 ), ( 0x7B, 0x000001FF,  0 )) # MSCURACT
	CUR_B              = (( 0x6B, 0x01FF0000, 16 ), ( 0x7B, 0x01FF0000, 16 )) # MSCURACT

	# CHOPCONF
	TOFF               = (( 0x6C, 0x0000000F,  0 ), ( 0x7C, 0x0000000F,  0 )) # CHOPCONF
	TFD_ALL            = (( 0x6C, 0x00000070,  4 ), ( 0x7C, 0x00000070,  4 )) # CHOPCONF
	HSTRT              = (( 0x6C, 0x00000070,  4 ), ( 0x7C, 0x00000070,  4 )) # CHOPCONF
	OFFSET             = (( 0x6C, 0x00000780,  7 ), ( 0x7C, 0x00000780,  7 )) # CHOPCONF
	HEND               = (( 0x6C, 0x00000780,  7 ), ( 0x7C, 0x00000780,  7 )) # CHOPCONF
	TFD_3              = (( 0x6C, 0x00000800, 11 ), ( 0x7C, 0x00000800, 11 )) # CHOPCONF
	DISFDCC            = (( 0x6C, 0x00001000, 12 ), ( 0x7C, 0x00001000, 12 )) # CHOPCONF
	RNDTF              = (( 0x6C, 0x00002000, 13 ), ( 0x7C, 0x00002000, 13 )) # CHOPCONF
	CHM                = (( 0x6C, 0x00004000, 14 ), ( 0x7C, 0x00004000, 14 )) # CHOPCONF
	TBL                = (( 0x6C, 0x00018000, 15 ), ( 0x7C, 0x00018000, 15 )) # CHOPCONF
	VSENSE             = (( 0x6C, 0x00020000, 17 ), ( 0x7C, 0x00020000, 17 )) # CHOPCONF
	VHIGHFS            = (( 0x6C, 0x00040000, 18 ), ( 0x7C, 0x00040000, 18 )) # CHOPCONF
	VHIGHCHM           = (( 0x6C, 0x00080000, 19 ), ( 0x7C, 0x00080000, 19 )) # CHOPCONF
	SYNC               = (( 0x6C, 0x00F00000, 20 ), ( 0x7C, 0x00F00000, 20 )) # CHOPCONF
	MRES               = (( 0x6C, 0x0F000000, 24 ), ( 0x7C, 0x0F000000, 24 )) # CHOPCONF
	DISS2G             = (( 0x6C, 0x40000000, 30 ), ( 0x7C, 0x40000000, 30 )) # CHOPCONF

	# COOLCONF
	SEMIN              = (( 0x6D, 0x0000000F,  0 ), ( 0x7D, 0x0000000F,  0 )) # COOLCONF
	SEUP               = (( 0x6D, 0x00000060,  5 ), ( 0x7D, 0x00000060,  5 )) # COOLCONF
	SEMAX              = (( 0x6D, 0x00000F00,  8 ), ( 0x7D, 0x00000F00,  8 )) # COOLCONF
	SEDN               = (( 0x6D, 0x00006000, 13 ), ( 0x7D, 0x00006000, 13 )) # COOLCONF
	SEIMIN             = (( 0x6D, 0x00008000, 15 ), ( 0x7D, 0x00008000, 15 )) # COOLCONF
	SGT                = (( 0x6D, 0x007F0000, 16 ), ( 0x7D, 0x007F0000, 16 )) # COOLCONF
	SFILT              = (( 0x6D, 0x01000000, 24 ), ( 0x7D, 0x01000000, 24 )) # COOLCONF

	# DRV_STATUS
	SG_RESULT          = (( 0x6F, 0x000003FF,  0 ), ( 0x7F, 0x000003FF,  0 )) # DRV_STATUS
	FSACTIVE           = (( 0x6F, 0x00008000, 15 ), ( 0x7F, 0x00008000, 15 )) # DRV_STATUS
	CS_ACTUAL          = (( 0x6F, 0x001F0000, 16 ), ( 0x7F, 0x001F0000, 16 )) # DRV_STATUS
	STALLGUARD         = (( 0x6F, 0x01000000, 24 ), ( 0x7F, 0x01000000, 24 )) # DRV_STATUS
	OT                 = (( 0x6F, 0x02000000, 25 ), ( 0x7F, 0x02000000, 25 )) # DRV_STATUS
	OTPW               = (( 0x6F, 0x04000000, 26 ), ( 0x7F, 0x04000000, 26 )) # DRV_STATUS
	S2GA               = (( 0x6F, 0x08000000, 27 ), ( 0x7F, 0x08000000, 27 )) # DRV_STATUS
	S2GB               = (( 0x6F, 0x10000000, 28 ), ( 0x7F, 0x10000000, 28 )) # DRV_STATUS
	OLA                = (( 0x6F, 0x20000000, 29 ), ( 0x7F, 0x20000000, 29 )) # DRV_STATUS
	OLB                = (( 0x6F, 0x40000000, 30 ), ( 0x7F, 0x40000000, 30 )) # DRV_STATUS
	STST               = (( 0x6F, 0x80000000, 31 ), ( 0x7F, 0x80000000, 31 )) # DRV_STATUS
