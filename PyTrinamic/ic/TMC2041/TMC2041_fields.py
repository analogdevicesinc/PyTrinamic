'''
Created on 24.10.2019

@author: JM
'''

class TMC2041_fields(object):
	"""
	Define all register bitfields of the TMC2041.

	Each field is defined as a tuple consisting of ( Address, Mask, Shift ).

	The name of the register is written as a comment behind each tuple. This is
	intended for IDE users viewing the definition of a field by hovering over
	it. This allows the user to see the corresponding register name of a field
	without opening this file and searching for the definition.
	"""
	# GCONF
	TEST_MODE  = ( 0x00, 0x00000080,  7 )
	SHAFT1     = ( 0x00, 0x00000100,  8 )
	SHAFT2     = ( 0x00, 0x00000200,  9 )
	LOCK_GCONF = ( 0x00, 0x00000400, 10 )
	
	# GSTAT
	RESET      = ( 0x01, 0x00000001,  0 )
	DRV_ERR1   = ( 0x01, 0x00000002,  1 )
	DRV_ERR2   = ( 0x01, 0x00000004,  2 )
	UV_CP      = ( 0x01, 0x00000008,  3 )
	
	# IFCNT
	IFCNT      = ( 0x02, 0x000000FF,  0 )
	
	# TEST_SEL
	TEST_SEL   = ( 0x03, 0x0000000F,  0 )
	
	# INPUT
	DRV_ENN    = ( 0x04, 0x00000080,  7 )
	VERSION    = ( 0x04, 0xFF000000, 24 )
	
	# IHOLD_IRUN_M1
	IHOLD      = ( 0x30, 0x0000001F,  0 )
	IRUN       = ( 0x30, 0x00001F00,  8 )
	IHOLDDELAY = ( 0x30, 0x000F0000, 16 )
	
	# MSCNT_M1
	MSCNT      = ( 0x6A, 0x000003FF,  0 )
	
	# MSCURACT_M1
	CUR_A      = ( 0x6B, 0x000001FF,  0 )
	CUR_B      = ( 0x6B, 0x01FF0000, 16 )
	
	# CHOPCONF_M1
	TOFF       = ( 0x6C, 0x0000000F,  0 )
	TFD_2__0_  = ( 0x6C, 0x00000070,  4 )
	OFFSET     = ( 0x6C, 0x00000780,  7 )
	TFD__      = ( 0x6C, 0x00000800, 11 )
	DISFDCC    = ( 0x6C, 0x00001000, 12 )
	RNDTF      = ( 0x6C, 0x00002000, 13 )
	CHM        = ( 0x6C, 0x00004000, 14 )
	TBL        = ( 0x6C, 0x00018000, 15 )
	VSENSE     = ( 0x6C, 0x00020000, 17 )
	VHIGHFS    = ( 0x6C, 0x00040000, 18 )
	VHIGHCHM   = ( 0x6C, 0x00080000, 19 )
	SYNC       = ( 0x6C, 0x00F00000, 20 )
	MRES       = ( 0x6C, 0x0F000000, 24 )
	INTPOL16   = ( 0x6C, 0x10000000, 28 )
	DEDGE      = ( 0x6C, 0x20000000, 29 )
	DISS2G     = ( 0x6C, 0x40000000, 30 )
	HSTRT      = ( 0x6C, 0x00000070,  4 )
	HEND       = ( 0x6C, 0x00000780,  7 )
	
	# COOLCONF_M1
	SEMIN      = ( 0x6D, 0x0000000F,  0 )
	SEUP       = ( 0x6D, 0x00000060,  5 )
	SEMAX      = ( 0x6D, 0x00000F00,  8 )
	SEDN       = ( 0x6D, 0x00006000, 13 )
	SEIMIN     = ( 0x6D, 0x00008000, 15 )
	SGT        = ( 0x6D, 0x007F0000, 16 )
	SFILT      = ( 0x6D, 0x01000000, 24 )
	
	# DRV_STATUS_M1
	SG_RESULT  = ( 0x6F, 0x000003FF,  0 )
	FSACTIVE   = ( 0x6F, 0x00008000, 15 )
	CS_ACTUAL  = ( 0x6F, 0x001F0000, 16 )
	STALLGUARD = ( 0x6F, 0x01000000, 24 )
	OT         = ( 0x6F, 0x02000000, 25 )
	OTPW       = ( 0x6F, 0x04000000, 26 )
	S2GA       = ( 0x6F, 0x08000000, 27 )
	S2GB       = ( 0x6F, 0x10000000, 28 )
	OLA        = ( 0x6F, 0x20000000, 29 )
	OLB        = ( 0x6F, 0x40000000, 30 )
	STST       = ( 0x6F, 0x80000000, 31 )