'''
Created on 14.10.2019

@author: JM
'''

class TMC2130_register:
    """
    Define all registers of the TMC2130.
    """
    GCONF       = 0x00
    GSTAT       = 0x01
    INP_OUT     = 0x04

    IHOLD_IRUN  = 0x10
    TPOWERDOWN  = 0x11
    TSTEP       = 0x12
    TPWMTHRS    = 0x13
    TCOOLTHRS   = 0x14
    THIGH       = 0x15

    XDIRECT     = 0x2D

    VDCMIN      = 0x33

    MSLUT0      = 0x60
    MSLUT1      = 0x61
    MSLUT2      = 0x62
    MSLUT3      = 0x63
    MSLUT4      = 0x64
    MSLUT5      = 0x65
    MSLUT6      = 0x66
    MSLUT7      = 0x67
    MSLUTSEL    = 0x68
    MSLUTSTART  = 0x69
    MSCNT       = 0x6A
    MSCURACT    = 0x6B

    CHOPCONF    = 0x6C
    COOLCONF    = 0x6D
    DCCTRL      = 0x6E
    DRVSTATUS   = 0x6F

    PWMCONF     = 0x70
    PWMSTATUS   = 0x71
    ENCM_CTRL   = 0x72
    LOST_STEPS  = 0x73

    list = [
        GCONF       ,
        GSTAT       ,
        INP_OUT     ,
        IHOLD_IRUN  ,
        TPOWERDOWN  ,
        TSTEP       ,
        TPWMTHRS    ,
        TCOOLTHRS   ,
        THIGH       ,
        VDCMIN      ,
        MSLUT0      ,
        MSLUT1      ,
        MSLUT2      ,
        MSLUT3      ,
        MSLUT4      ,
        MSLUT5      ,
        MSLUT6      ,
        MSLUT7      ,
        MSLUTSEL    ,
        MSLUTSTART  ,
        MSCNT       ,
        MSCURACT    ,
        CHOPCONF    ,
        COOLCONF    ,
        DCCTRL      ,
        DRVSTATUS   ,
        PWMCONF     ,
        PWMSTATUS   ,
        ENCM_CTRL   ,
        LOST_STEPS  ,
    ]
