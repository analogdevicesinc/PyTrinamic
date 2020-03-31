'''
Created on 30.03.2020

@author: JM
'''

class TMC7300_fields(object):
	"""
	Define all register bitfields of the TMC7300.

	Each field is defined as a tuple consisting of ( Address, Mask, Shift ).

	The name of the register is written as a comment behind each tuple. This is
	intended for IDE users viewing the definition of a field by hovering over
	it. This allows the user to see the corresponding register name of a field
	without opening this file and searching for the definition.
	"""

	# GCONF
	PWM_DIRECT    = ( 0x00, 0x00000001,  0 ) # GCONF
	EXTCAP        = ( 0x00, 0x00000002,  1 ) # GCONF
	PAR_MODE      = ( 0x00, 0x00000004,  2 ) # GCONF
	TEST_MODE     = ( 0x00, 0x00000080,  7 ) # GCONF

	# GSTAT
	RESET         = ( 0x01, 0x00000001,  0 ) # GSTAT
	DRV_ERR       = ( 0x01, 0x00000002,  1 ) # GSTAT
	U3V5          = ( 0x01, 0x00000004,  2 ) # GSTAT

	# IFCNT
	IFCNT         = ( 0x02, 0x000000FF,  0 ) # IFCNT

	# SLAVECONF
	SLAVECONF     = ( 0x03, 0x00000F00,  8 ) # SLAVECONF

	# IOIN
	EN            = ( 0x06, 0x00000001,  0 ) # IOIN
	NSTDBY        = ( 0x06, 0x00000002,  1 ) # IOIN
	AD0           = ( 0x06, 0x00000004,  2 ) # IOIN
	AD1           = ( 0x06, 0x00000008,  3 ) # IOIN
	DIAG          = ( 0x06, 0x00000010,  4 ) # IOIN
	UART_ENABLED  = ( 0x06, 0x00000020,  5 ) # IOIN
	UART_INPUT    = ( 0x06, 0x00000040,  6 ) # IOIN
	MODE_INPUT    = ( 0x06, 0x00000080,  7 ) # IOIN
	A2            = ( 0x06, 0x00000100,  8 ) # IOIN
	A1            = ( 0x06, 0x00000200,  9 ) # IOIN
	COMP_A1A2     = ( 0x06, 0x00000400, 10 ) # IOIN
	COMP_B1B2     = ( 0x06, 0x00000800, 11 ) # IOIN
	VERSION       = ( 0x06, 0xFF000000, 24 ) # IOIN

	# CURRENT_LIMIT
	MOTORRUN      = ( 0x10, 0x00000001,  0 ) # CURRENT_LIMIT
	IRUN          = ( 0x10, 0x00001F00,  8 ) # CURRENT_LIMIT

	# PWM_AB
	PWM_A         = ( 0x22, 0x000001FF,  0 ) # PWM_AB
	PWM_B         = ( 0x22, 0x01FF0000, 16 ) # PWM_AB
	PWM_AB        = ( 0x22, 0x000001FF,  0 ) # PWM_AB

	# CHOPCONF
	ENABLEDRV     = ( 0x6C, 0x00000001,  0 ) # CHOPCONF
	TBL           = ( 0x6C, 0x00018000, 15 ) # CHOPCONF
	DISS2G        = ( 0x6C, 0x40000000, 30 ) # CHOPCONF
	DISS2VS       = ( 0x6C, 0x80000000, 31 ) # CHOPCONF

	# DRV_STATUS
	OTPW          = ( 0x6F, 0x00000001,  0 ) # DRV_STATUS
	OT            = ( 0x6F, 0x00000002,  1 ) # DRV_STATUS
	S2GA          = ( 0x6F, 0x00000004,  2 ) # DRV_STATUS
	S2GB          = ( 0x6F, 0x00000008,  3 ) # DRV_STATUS
	S2VSA         = ( 0x6F, 0x00000010,  4 ) # DRV_STATUS
	S2VSB         = ( 0x6F, 0x00000020,  5 ) # DRV_STATUS
	OLA           = ( 0x6F, 0x00000040,  6 ) # DRV_STATUS
	OLB           = ( 0x6F, 0x00000080,  7 ) # DRV_STATUS
	T120          = ( 0x6F, 0x00000100,  8 ) # DRV_STATUS
	T150          = ( 0x6F, 0x00000200,  9 ) # DRV_STATUS

	# PWMCONF
	PWM_FREQ      = ( 0x70, 0x00030000, 16 ) # PWMCONF
	FREEWHEEL     = ( 0x70, 0x00300000, 20 ) # PWMCONF
