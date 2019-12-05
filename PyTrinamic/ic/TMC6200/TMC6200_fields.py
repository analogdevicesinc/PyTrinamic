'''
Created on 06.03.2019

@author: ed
'''

class TMC6200_fields(object):

	# GCONF
	DISABLE           = ( 0x00, 0x00000001,  0 ) # GCONF
	SINGLELINE        = ( 0x00, 0x00000002,  1 ) # GCONF
	FAULTDIRECT       = ( 0x00, 0x00000004,  2 ) # GCONF
	UNUSED            = ( 0x00, 0x00000008,  3 ) # GCONF
	AMPLIFICATION     = ( 0x00, 0x00000030,  4 ) # GCONF
	AMPLIFIER_OFF     = ( 0x00, 0x00000040,  6 ) # GCONF
	TEST_MODE         = ( 0x00, 0x00000080,  7 ) # GCONF

	# GSTAT
	RESET             = ( 0x01, 0x00000001,  0 ) # GSTAT
	DRV_OTPW          = ( 0x01, 0x00000002,  1 ) # GSTAT
	DRV_OT            = ( 0x01, 0x00000004,  2 ) # GSTAT
	UV_CP             = ( 0x01, 0x00000008,  3 ) # GSTAT
	SHORTDET_U        = ( 0x01, 0x00000010,  4 ) # GSTAT
	S2GU              = ( 0x01, 0x00000020,  5 ) # GSTAT
	S2VSU             = ( 0x01, 0x00000040,  6 ) # GSTAT
	SHORTDET_V        = ( 0x01, 0x00000100,  8 ) # GSTAT
	S2GV              = ( 0x01, 0x00000200,  9 ) # GSTAT
	S2VSV             = ( 0x01, 0x00000400, 10 ) # GSTAT
	SHORTDET_W        = ( 0x01, 0x00001000, 12 ) # GSTAT
	S2GW              = ( 0x01, 0x00002000, 13 ) # GSTAT
	S2VSW             = ( 0x01, 0x00004000, 14 ) # GSTAT

	# IOIN / OUTPUT
	UL                = ( 0x04, 0x00000001,  0 ) # IOIN / OUTPUT
	UH                = ( 0x04, 0x00000002,  1 ) # IOIN / OUTPUT
	VL                = ( 0x04, 0x00000004,  2 ) # IOIN / OUTPUT
	VH                = ( 0x04, 0x00000008,  3 ) # IOIN / OUTPUT
	WL                = ( 0x04, 0x00000010,  4 ) # IOIN / OUTPUT
	WH                = ( 0x04, 0x00000020,  5 ) # IOIN / OUTPUT
	DRV_EN            = ( 0x04, 0x00000040,  6 ) # IOIN / OUTPUT
	OTPW              = ( 0x04, 0x00000100,  8 ) # IOIN / OUTPUT
	OT136_C           = ( 0x04, 0x00000200,  9 ) # IOIN / OUTPUT
	OT143_C           = ( 0x04, 0x00000400, 10 ) # IOIN / OUTPUT
	OT150_C           = ( 0x04, 0x00000800, 11 ) # IOIN / OUTPUT
	VERSION           = ( 0x04, 0xFF000000, 24 ) # IOIN / OUTPUT

	# OTP_PROG
	OTPBIT            = ( 0x06, 0x00000007,  0 ) # OTP_PROG
	OTPBYTE           = ( 0x06, 0x00000030,  4 ) # OTP_PROG
	OTPMAGIC          = ( 0x06, 0x0000FF00,  8 ) # OTP_PROG

	# OTP_READ
	OTP_BBM           = ( 0x07, 0x000000C0,  6 ) # OTP_READ
	OTP_S2_LEVEL      = ( 0x07, 0x00000020,  5 ) # OTP_READ
	OTP_FCLKTRIM      = ( 0x07, 0x0000001F,  0 ) # OTP_READ

	# FACTORY_CONF
	FACTORY_CONF      = ( 0x08, 0x0000001F,  0 ) # FACTORY_CONF

	# SHORT_CONF
	S2VS_LEVEL        = ( 0x09, 0x0000000F,  0 ) # SHORT_CONF
	S2G_LEVEL         = ( 0x09, 0x00000F00,  8 ) # SHORT_CONF
	SHORTFILTER       = ( 0x09, 0x00030000, 16 ) # SHORT_CONF
	SHORTDELAY        = ( 0x09, 0x00100000, 20 ) # SHORT_CONF
	RETRY             = ( 0x09, 0x03000000, 24 ) # SHORT_CONF
	PROTECT_PARALLEL  = ( 0x09, 0x10000000, 28 ) # SHORT_CONF
	DISABLE_S2G       = ( 0x09, 0x20000000, 29 ) # SHORT_CONF
	DISABLE_S2VS      = ( 0x09, 0x40000000, 30 ) # SHORT_CONF

	# DRV_CONF
	BBMCLKS           = ( 0x0A, 0x0000000F,  0 ) # DRV_CONF
	OTSELECT          = ( 0x0A, 0x00030000, 16 ) # DRV_CONF
	DRVSTRENGTH       = ( 0x0A, 0x000C0000, 18 ) # DRV_CONF
