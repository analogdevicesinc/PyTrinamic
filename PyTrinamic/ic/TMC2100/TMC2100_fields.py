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
	GCONF  = ( 0x00, 0xFFFFFFFF,  0 ) # GCONF