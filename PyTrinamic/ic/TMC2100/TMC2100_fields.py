'''
Created on 15.10.2019

@author: JM
'''

class TMC2100_fields(object):
	"""
	Define all register bitfields of the TMC2100.

	Each field is defined as a tuple consisting of ( Address, Mask, Shift ).

	The name of the register is written as a comment behind each tuple. This is
	intended for IDE users viewing the definition of a field by hovering over
	it. This allows the user to see the corresponding register name of a field
	without opening this file and searching for the definition.
	"""
	# GCONF
	I_SCALE_ANALOG          = ( 0x00, 0x00000001,  0 ) # GCONF
	INTERNAL_RSENSE         = ( 0x00, 0x00000002,  1 ) # GCONF
	EN_PWM_MODE             = ( 0x00, 0x00000004,  2 ) # GCONF
	ENC_COMMUTATION         = ( 0x00, 0x00000008,  3 ) # GCONF
	SHAFT                   = ( 0x00, 0x00000010,  4 ) # GCONF
	DIAG0_ERROR             = ( 0x00, 0x00000020,  5 ) # GCONF
	DIAG0_OTPW              = ( 0x00, 0x00000040,  6 ) # GCONF
	DIAG0_STALL             = ( 0x00, 0x00000080,  7 ) # GCONF
	DIAG1_STALL             = ( 0x00, 0x00000100,  8 ) # GCONF
	DIAG1_INDEX             = ( 0x00, 0x00000200,  9 ) # GCONF
	DIAG1_ONSTATE           = ( 0x00, 0x00000400, 10 ) # GCONF
	DIAG1_STEPS_SKIPPED     = ( 0x00, 0x00000800, 11 ) # GCONF
	DIAG0_INT_PUSHPULL      = ( 0x00, 0x00001000, 12 ) # GCONF
	DIAG1_POSCOMP_PUSHPULL  = ( 0x00, 0x00002000, 13 ) # GCONF
	SMALL_HYSTERESIS        = ( 0x00, 0x00004000, 14 ) # GCONF
	STOP_ENABLE             = ( 0x00, 0x00008000, 15 ) # GCONF
	DIRECT_MODE             = ( 0x00, 0x00010000, 16 ) # GCONF
	TEST_MODE               = ( 0x00, 0x00020000, 17 ) # GCONF