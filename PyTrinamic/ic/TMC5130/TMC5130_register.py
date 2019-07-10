'''
Created on 09.01.2019

@author: LK
'''

class TMC5130_register:
    """
    Define all registers of the TMC5130.

    Each register is defined either as an integer or as a tuple of integers.
    Each integer represents a register address. Tuples of addresses are used to
    represent a register that exists multiple times for multiple motors.
    """
    GCONF       = 0x00
    GSTAT       = 0x01
    IFCNT       = 0x02
    SLAVECONF   = 0x03
    INP_OUT     = 0x04
    X_COMPARE   = 0x05

    IHOLD_IRUN  = 0x10
    TPOWERDOWN  = 0x11
    TSTEP       = 0x12
    TPWMTHRS    = 0x13
    TCOOLTHRS   = 0x14
    THIGH       = 0x15

    RAMPMODE    = 0x20
    XACTUAL     = 0x21
    VACTUAL     = 0x22
    VSTART      = 0x23
    A1          = 0x24
    V1          = 0x25
    AMAX        = 0x26
    VMAX        = 0x27
    DMAX        = 0x28
    D1          = 0x2A
    VSTOP       = 0x2B
    TZEROWAIT   = 0x2C
    XTARGET     = 0x2D

    VDCMIN      = 0x33
    SWMODE      = 0x34
    RAMPSTAT    = 0x35
    XLATCH      = 0x36
    ENCMODE     = 0x38
    XENC        = 0x39
    ENC_CONST   = 0x3A
    ENC_STATUS  = 0x3B
    ENC_LATCH   = 0x3C

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
        IFCNT       ,
        SLAVECONF   ,
        INP_OUT     ,
        X_COMPARE   ,
        IHOLD_IRUN  ,
        TPOWERDOWN  ,
        TSTEP       ,
        TPWMTHRS    ,
        TCOOLTHRS   ,
        THIGH       ,
        RAMPMODE    ,
        XACTUAL     ,
        VACTUAL     ,
        VSTART      ,
        A1          ,
        V1          ,
        AMAX        ,
        VMAX        ,
        DMAX        ,
        D1          ,
        VSTOP       ,
        TZEROWAIT   ,
        XTARGET     ,
        VDCMIN      ,
        SWMODE      ,
        RAMPSTAT    ,
        XLATCH      ,
        ENCMODE     ,
        XENC        ,
        ENC_CONST   ,
        ENC_STATUS  ,
        ENC_LATCH   ,
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
