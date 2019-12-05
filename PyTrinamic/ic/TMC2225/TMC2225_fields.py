'''
Created on 17.10.2019

@author: JM
'''

class TMC2225_fields(object):
	"""
	Define all register bitfields of the TMC2225.

	Each field is defined as a tuple consisting of ( Address, Mask, Shift ).

	The name of the register is written as a comment behind each tuple. This is
	intended for IDE users viewing the definition of a field by hovering over
	it. This allows the user to see the corresponding register name of a field
	without opening this file and searching for the definition.
	"""

	# GCONF
	I_SCALE_ANALOG         = ( 0x00, 0x00000001,  0 ) # GCONF
	INTERNAL_RSENSE        = ( 0x00, 0x00000002,  1 ) # GCONF
	EN_SPREADCYCLE         = ( 0x00, 0x00000004,  2 ) # GCONF
	SHAFT                  = ( 0x00, 0x00000008,  3 ) # GCONF
	INDEX_OTPW             = ( 0x00, 0x00000010,  4 ) # GCONF
	INDEX_STEP             = ( 0x00, 0x00000020,  5 ) # GCONF
	PDN_DISABLE            = ( 0x00, 0x00000040,  6 ) # GCONF
	MSTEP_REG_SELECT       = ( 0x00, 0x00000080,  7 ) # GCONF
	MULTISTEP_FILT         = ( 0x00, 0x00000100,  8 ) # GCONF
	TEST_MODE              = ( 0x00, 0x00000200,  9 ) # GCONF

	# GSTAT
	RESET                  = ( 0x01, 0x00000001,  0 ) # GSTAT
	DRV_ERR                = ( 0x01, 0x00000002,  1 ) # GSTAT
	UV_CP                  = ( 0x01, 0x00000004,  2 ) # GSTAT

	# IFCNT
	IFCNT                  = ( 0x02, 0x000000FF,  0 ) # IFCNT

	# SLAVECONF
	SLAVECONF              = ( 0x03, 0x00000F00,  8 ) # SLAVECONF

	# OTP_PROG
	OTPBIT                 = ( 0x04, 0x00000007,  0 ) # OTP_PROG
	OTPBYTE                = ( 0x04, 0x00000030,  4 ) # OTP_PROG
	OTPMAGIC               = ( 0x04, 0x0000FF00,  8 ) # OTP_PROG

	# OTP_READ
	OTP0_BYTE_0_READ_DATA  = ( 0x05, 0x000000FF,  0 ) # OTP_READ
	OTP1_BYTE_1_READ_DATA  = ( 0x05, 0x0000FF00,  8 ) # OTP_READ
	OTP2_BYTE_2_READ_DATA  = ( 0x05, 0x00FF0000, 16 ) # OTP_READ

	# IOIN
	ENN                    = ( 0x06, 0x00000001,  0 ) # IOIN
	MS1                    = ( 0x06, 0x00000004,  2 ) # IOIN
	MS2                    = ( 0x06, 0x00000008,  3 ) # IOIN
	DIAG                   = ( 0x06, 0x00000010,  4 ) # IOIN
	PDN_UART               = ( 0x06, 0x00000040,  6 ) # IOIN
	STEP                   = ( 0x06, 0x00000080,  7 ) # IOIN
	SEL_A                  = ( 0x06, 0x00000100,  8 ) # IOIN
	DIR                    = ( 0x06, 0x00000200,  9 ) # IOIN
	VERSION                = ( 0x06, 0xFF000000, 24 ) # IOIN

	# FACTORY_CONF
	FCLKTRIM               = ( 0x07, 0x0000001F,  0 ) # FACTORY_CONF
	OTTRIM                 = ( 0x07, 0x00000300,  8 ) # FACTORY_CONF

	# IHOLD_IRUN
	IHOLD                  = ( 0x10, 0x0000001F,  0 ) # IHOLD_IRUN
	IRUN                   = ( 0x10, 0x00001F00,  8 ) # IHOLD_IRUN
	IHOLDDELAY             = ( 0x10, 0x000F0000, 16 ) # IHOLD_IRUN

	# TPOWERDOWN
	TPOWERDOWN             = ( 0x11, 0x000000FF,  0 ) # TPOWERDOWN

	# TSTEP
	TSTEP                  = ( 0x12, 0x000FFFFF,  0 ) # TSTEP

	# TPWMTHRS
	TPWMTHRS               = ( 0x13, 0x000FFFFF,  0 ) # TPWMTHRS

	# VACTUAL
	VACTUAL                = ( 0x22, 0x00FFFFFF,  0 ) # VACTUAL

	# MSCNT
	MSCNT                  = ( 0x6A, 0x000003FF,  0 ) # MSCNT

	# MSCURACT
	CUR_A                  = ( 0x6B, 0x000001FF,  0 ) # MSCURACT
	CUR_B                  = ( 0x6B, 0x01FF0000, 16 ) # MSCURACT

	# CHOPCONF
	TOFF                   = ( 0x6C, 0x0000000F,  0 ) # CHOPCONF
	HSTRT                  = ( 0x6C, 0x00000070,  4 ) # CHOPCONF
	HEND                   = ( 0x6C, 0x00000780,  7 ) # CHOPCONF
	TBL                    = ( 0x6C, 0x00018000, 15 ) # CHOPCONF
	VSENSE                 = ( 0x6C, 0x00020000, 17 ) # CHOPCONF
	MRES                   = ( 0x6C, 0x0F000000, 24 ) # CHOPCONF
	INTPOL                 = ( 0x6C, 0x10000000, 28 ) # CHOPCONF
	DEDGE                  = ( 0x6C, 0x20000000, 29 ) # CHOPCONF
	DISS2G                 = ( 0x6C, 0x40000000, 30 ) # CHOPCONF
	DISS2VS                = ( 0x6C, 0x80000000, 31 ) # CHOPCONF
	TOFF                   = ( 0x6C, 0x0000000F,  0 ) # CHOPCONF
	HSTRT                  = ( 0x6C, 0x00000070,  4 ) # CHOPCONF
	HEND                   = ( 0x6C, 0x00000780,  7 ) # CHOPCONF
	TBL                    = ( 0x6C, 0x00018000, 15 ) # CHOPCONF
	VSENSE                 = ( 0x6C, 0x00020000, 17 ) # CHOPCONF
	MRES                   = ( 0x6C, 0x0F000000, 24 ) # CHOPCONF
	INTPOL                 = ( 0x6C, 0x10000000, 28 ) # CHOPCONF
	DEDGE                  = ( 0x6C, 0x20000000, 29 ) # CHOPCONF
	DISS2G                 = ( 0x6C, 0x40000000, 30 ) # CHOPCONF
	DISS2VS                = ( 0x6C, 0x80000000, 31 ) # CHOPCONF

	# DRV_STATUS
	OTPW                   = ( 0x6F, 0x00000001,  0 ) # DRV_STATUS
	OT                     = ( 0x6F, 0x00000002,  1 ) # DRV_STATUS
	S2GA                   = ( 0x6F, 0x00000004,  2 ) # DRV_STATUS
	S2GB                   = ( 0x6F, 0x00000008,  3 ) # DRV_STATUS
	S2VSA                  = ( 0x6F, 0x00000010,  4 ) # DRV_STATUS
	S2VSB                  = ( 0x6F, 0x00000020,  5 ) # DRV_STATUS
	OLA                    = ( 0x6F, 0x00000040,  6 ) # DRV_STATUS
	OLB                    = ( 0x6F, 0x00000080,  7 ) # DRV_STATUS
	T120                   = ( 0x6F, 0x00000100,  8 ) # DRV_STATUS
	T143                   = ( 0x6F, 0x00000200,  9 ) # DRV_STATUS
	T150                   = ( 0x6F, 0x00000400, 10 ) # DRV_STATUS
	T157                   = ( 0x6F, 0x00000800, 11 ) # DRV_STATUS
	CS_ACTUAL              = ( 0x6F, 0x001F0000, 16 ) # DRV_STATUS
	STEALTH                = ( 0x6F, 0x40000000, 30 ) # DRV_STATUS
	STST                   = ( 0x6F, 0x80000000, 31 ) # DRV_STATUS

	# PWMCONF
	PWM_OFS                = ( 0x70, 0x000000FF,  0 ) # PWMCONF
	PWM_GRAD               = ( 0x70, 0x0000FF00,  8 ) # PWMCONF
	PWM_FREQ               = ( 0x70, 0x00030000, 16 ) # PWMCONF
	PWM_AUTOSCALE          = ( 0x70, 0x00040000, 18 ) # PWMCONF
	PWM_AUTOGRAD           = ( 0x70, 0x00080000, 19 ) # PWMCONF
	FREEWHEEL              = ( 0x70, 0x00300000, 20 ) # PWMCONF
	PWM_REG                = ( 0x70, 0x0F000000, 24 ) # PWMCONF
	PWM_LIM                = ( 0x70, 0xF0000000, 28 ) # PWMCONF

	# PWM_SCALE
	PWM_SCALE_SUM          = ( 0x71, 0x000000FF,  0 ) # PWM_SCALE
	PWM_SCALE_AUTO         = ( 0x71, 0x01FF0000, 16 ) # PWM_SCALE

	# PWM_AUTO
	PWM_OFS_AUTO           = ( 0x72, 0x000000FF,  0 ) # PWM_AUTO
	PWM_GRAD_AUTO          = ( 0x72, 0x00FF0000, 16 ) # PWM_AUTO
