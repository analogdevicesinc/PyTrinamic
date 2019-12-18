'''
Created on 07.11.2019

@author: JM
'''

class TMC2660_register:
    """
    Define all registers of the TMC2660.
    """
    DRVSTATUS___MSTEP  = 0x00
    DRVSTATUS___SG     = 0x01
    DRVSTATUS___SG_SE  = 0x02
    DRVCTRL            = 0x08
    CHOPCONF           = 0x0C
    SMARTEN            = 0x0D
    SGCSCONF           = 0x0E
    DRVCONF            = 0x0F
