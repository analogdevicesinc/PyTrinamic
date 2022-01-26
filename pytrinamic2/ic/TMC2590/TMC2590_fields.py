'''
Created on 07.02.2020

@author: JM
'''

class TMC2590_fields(object):
    """
    Define all register bitfields of the TMC2590.

    Each field is defined as a tuple consisting of ( Address, Mask, Shift ).

    The name of the register is written as a comment behind each tuple. This is
    intended for IDE users viewing the definition of a field by hovering over
    it. This allows the user to see the corresponding register name of a field
    without opening this file and searching for the definition.
    """

    # DRVSTATUS / MSTEP
    MSTEP                  = ( 0x00, 0x000FFC00, 10 ) # DRVSTATUS / MSTEP
    STST                   = ( 0x00, 0x00000080,  7 ) # DRVSTATUS / MSTEP
    OLB                    = ( 0x00, 0x00000040,  6 ) # DRVSTATUS / MSTEP
    OLA                    = ( 0x00, 0x00000020,  5 ) # DRVSTATUS / MSTEP
    S2GB                   = ( 0x00, 0x00000010,  4 ) # DRVSTATUS / MSTEP
    S2GA                   = ( 0x00, 0x00000008,  3 ) # DRVSTATUS / MSTEP
    OTPW                   = ( 0x00, 0x00000004,  2 ) # DRVSTATUS / MSTEP
    OT                     = ( 0x00, 0x00000002,  1 ) # DRVSTATUS / MSTEP
    SG                     = ( 0x00, 0x00000001,  0 ) # DRVSTATUS / MSTEP

    # DRVSTATUS / SG_SE
    SE                     = ( 0x02, 0x00007C00, 10 ) # DRVSTATUS / SG_SE

    # DRVCTRL
    REGISTER_ADDRESS_BITS  = ( 0x08, 0x00C00000, 18 ) # DRVCTRL
    INTPOL                 = ( 0x08, 0x00000200,  9 ) # DRVCTRL
    DEDGE                  = ( 0x08, 0x00000100,  8 ) # DRVCTRL
    MRES                   = ( 0x08, 0x0000000F,  0 ) # DRVCTRL
    PHA                    = ( 0x08, 0x00020000, 17 ) # DRVCTRL
    CA                     = ( 0x08, 0x0001FE00,  9 ) # DRVCTRL
    PHB                    = ( 0x08, 0x00000100,  8 ) # DRVCTRL
    CB                     = ( 0x08, 0x000000FF,  0 ) # DRVCTRL

    # CHOPCONF
    TBL                    = ( 0x0C, 0x00018000, 15 ) # CHOPCONF
    CHM                    = ( 0x0C, 0x00004000, 14 ) # CHOPCONF
    RNDTF                  = ( 0x0C, 0x00002000, 13 ) # CHOPCONF
    HDEC                   = ( 0x0C, 0x00001800, 11 ) # CHOPCONF
    HEND                   = ( 0x0C, 0x00000780,  7 ) # CHOPCONF
    HSTRT                  = ( 0x0C, 0x00000070,  4 ) # CHOPCONF
    HDEC1                  = ( 0x0C, 0x00002000, 12 ) # CHOPCONF
    HDEC0                  = ( 0x0C, 0x00001000, 11 ) # CHOPCONF
    TOFF                   = ( 0x0C, 0x0000000F,  0 ) # CHOPCONF

    # SMARTEN
    SEIMIN                 = ( 0x0D, 0x00008000, 15 ) # SMARTEN
    SEDN                   = ( 0x0D, 0x00006000, 13 ) # SMARTEN
    SEUP                   = ( 0x0D, 0x00000060,  5 ) # SMARTEN
    SEMAX                  = ( 0x0D, 0x00000F00,  8 ) # SMARTEN
    SEMIN                  = ( 0x0D, 0x0000000F,  0 ) # SMARTEN

    # SGCSCONF
    SFILT                  = ( 0x0E, 0x00010000, 16 ) # SGCSCONF
    SGT                    = ( 0x0E, 0x00007F00,  8 ) # SGCSCONF
    CS                     = ( 0x0E, 0x0000001F,  0 ) # SGCSCONF

    # DRVCONF
    TST                    = ( 0x0F, 0x00010000, 16 ) # DRVCONF
    SLPH                   = ( 0x0F, 0x0000C000, 14 ) # DRVCONF
    SLPL                   = ( 0x0F, 0x00003000, 12 ) # DRVCONF
    DISS2G                 = ( 0x0F, 0x00000400, 10 ) # DRVCONF
    TS2G                   = ( 0x0F, 0x00000300,  8 ) # DRVCONF
    SDOFF                  = ( 0x0F, 0x00000080,  7 ) # DRVCONF
    VSENSE                 = ( 0x0F, 0x00000040,  6 ) # DRVCONF
    RDSEL                  = ( 0x0F, 0x00000030,  4 ) # DRVCONF
