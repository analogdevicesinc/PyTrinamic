'''
Created on 23.10.2019

@author: JM
'''

class TMC2160_register:
    """
    Define all registers of the TMC2160.
    """
    GCONF         = 0x00
    GSTAT         = 0x01
    INP_OUT       = 0x04
    X_COMPARE     = 0x05
    OTP_PROG      = 0x06
    OTP_READ      = 0x07
    FACTORY_CONF  = 0x08
    SHORT_CONF    = 0x09
    
    DRV_CONF      = 0x0A
    GLOBAL_SCALER = 0x0B
    OFFSET_READ   = 0x0C
    
    IHOLD_IRUN    = 0x10
    TPOWERDOWN    = 0x11
    TSTEP         = 0x12
    TPWMTHRS      = 0x13
    TCOOLTHRS     = 0x14
    THIGH         = 0x15
    
    XDIRECT       = 0x2D
    
    VDCMIN        = 0x33
    
    MSLUT0        = 0x60
    MSLUT1        = 0x61
    MSLUT2        = 0x62
    MSLUT3        = 0x63
    MSLUT4        = 0x64
    MSLUT5        = 0x65
    MSLUT6        = 0x66
    MSLUT7        = 0x67
    MSLUTSEL      = 0x68
    MSLUTSTART    = 0x69
    MSCNT         = 0x6A
    MSCURACT      = 0x6B
    
    CHOPCONF      = 0x6C
    COOLCONF      = 0x6D
    DCCTRL        = 0x6E
    DRVSTATUS     = 0x6F
    
    PWMCONF       = 0x70
    PWM_SCALE    = 0x71
    PWM_AUTO      = 0x72
    LOST_STEPS    = 0x73
    
    list = [
    GCONF         ,
    GSTAT         ,
    INP_OUT       ,
    X_COMPARE     ,
    OTP_PROG      ,
    OTP_READ      ,
    FACTORY_CONF  ,
    SHORT_CONF    ,
    
    DRV_CONF      ,
    GLOBAL_SCALER ,
    OFFSET_READ   ,
    
    IHOLD_IRUN    ,
    TPOWERDOWN    ,
    TSTEP         ,
    TPWMTHRS      ,
    TCOOLTHRS     ,
    THIGH         ,
    
    XDIRECT       ,
    
    VDCMIN        ,
    
    MSLUT0        ,
    MSLUT1        ,
    MSLUT2        ,
    MSLUT3        ,
    MSLUT4        ,
    MSLUT5        ,
    MSLUT6        ,
    MSLUT7        ,
    MSLUTSEL      ,
    MSLUTSTART    ,
    MSCNT         ,
    MSCURACT      ,
    
    CHOPCONF      ,
    COOLCONF      ,
    DCCTRL        ,
    DRVSTATUS     ,
    
    PWMCONF       ,
    PWM_SCALE    ,
    PWM_AUTO      ,
    LOST_STEPS    ,
    ]
