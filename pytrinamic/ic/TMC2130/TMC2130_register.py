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
    IOIN        = 0x04
    IHOLD_IRUN  = 0x10
    TPOWERDOWN  = 0x11
    TSTEP       = 0x12
    TPWMTHRS    = 0x13
    TCOOLTHRS   = 0x14
    THIGH       = 0x15
    XDIRECT     = 0x2D
    VDCMIN      = 0x33
    MSLUT__     = 0x60
    MSLUTSEL    = 0x68
    MSLUTSTART  = 0x69
    MSCNT       = 0x6A
    MSCURACT    = 0x6B
    CHOPCONF    = 0x6C
    COOLCONF    = 0x6D
    DCCTRL      = 0x6E
    DRV_STATUS  = 0x6F
    PWMCONF     = 0x70
    PWM_SCALE   = 0x71
    ENCM_CTRL   = 0x72
    LOST_STEPS  = 0x73
