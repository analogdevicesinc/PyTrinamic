'''
Created on 24.10.2019

@author: JM
'''

class TMC5160_register:
    """
    Define all registers of the TMC5160.
    """
    GCONF             = 0x00
    GSTAT             = 0x01
    SLAVECONF         = 0x03
    IOIN_OUTPUT       = 0x04
    X_COMPARE         = 0x05
    OTP_PROG          = 0x06
    OTP_READ          = 0x07
    FACTORY_CONF      = 0x08
    SHORT_CONF        = 0x09
    DRV_CONF          = 0x0A
    GLOBAL_SCALER     = 0x0B
    OFFSET_READ       = 0x0C
    
    IHOLD_IRUN        = 0x10
    TPOWERDOWN        = 0x11
    TSTEP             = 0x12
    TPWMTHRS          = 0x13
    TCOOLTHRS         = 0x14
    THIGH             = 0x15
    
    RAMPMODE          = 0x20
    XACTUAL           = 0x21
    VACTUAL           = 0x22
    VSTART            = 0x23
    A1                = 0x24
    V1                = 0x25
    AMAX              = 0x26
    VMAX              = 0x27
    DMAX              = 0x28
    D1                = 0x2A
    VSTOP             = 0x2B
    TZEROWAIT         = 0x2C
    XTARGET           = 0x2D
    
    VDCMIN            = 0x33
    SW_MODE           = 0x34
    RAMP_STAT         = 0x35
    XLATCH            = 0x36
    ENCMODE           = 0x38
    X_ENC             = 0x39
    ENC_CONST         = 0x3A
    ENC_STATUS        = 0x3B
    ENC_LATCH         = 0x3C
    ENC_DEVIATION     = 0x3D
    
    MSLUT0            = 0x60
    MSLUT1            = 0x61
    MSLUT2            = 0x62
    MSLUT3            = 0x63
    MSLUT4            = 0x64
    MSLUT5            = 0x65
    MSLUT6            = 0x66
    MSLUT7            = 0x67
    MSLUTSEL          = 0x68
    MSLUTSTART        = 0x69
    MSCNT             = 0x6A
    MSCURACT          = 0x6B

    CHOPCONF          = 0x6C
    COOLCONF          = 0x6D
    DCCTRL            = 0x6E
    DRVSTATUS         = 0x6F

    PWMCONF           = 0x70
    PWM_SCALE         = 0x71
    PWM_AUTO          = 0x72
    LOST_STEPS        = 0x73

    list = [
    GCONF             ,
    GSTAT             ,
    SLAVECONF         ,
    IOIN_OUTPUT       ,
    X_COMPARE         ,
    OTP_PROG          ,
    OTP_READ          ,
    FACTORY_CONF      ,
    SHORT_CONF        ,
    DRV_CONF          ,
    GLOBAL_SCALER     ,
    OFFSET_READ       ,
    
    IHOLD_IRUN        ,
    TPOWERDOWN        ,
    TSTEP             ,
    TPWMTHRS          ,
    TCOOLTHRS         ,
    THIGH             ,
    
    RAMPMODE          ,
    XACTUAL           ,
    VACTUAL           ,
    VSTART            ,
    A1                ,
    V1                ,
    AMAX              ,
    VMAX              ,
    DMAX              ,
    D1                ,
    VSTOP             ,
    TZEROWAIT         ,
    XTARGET           ,
    
    VDCMIN            ,
    SW_MODE           ,
    RAMP_STAT         ,
    XLATCH            ,
    ENCMODE           ,
    X_ENC             ,
    ENC_CONST         ,
    ENC_STATUS        ,
    ENC_LATCH         ,
    ENC_DEVIATION     ,
    
    MSLUT0            ,
    MSLUT1            ,
    MSLUT2            ,
    MSLUT3            ,
    MSLUT4            ,
    MSLUT5            ,
    MSLUT6            ,
    MSLUT7            ,
    MSLUTSEL          ,
    MSLUTSTART        ,
    MSCNT             ,
    MSCURACT          ,

    CHOPCONF          ,
    COOLCONF          ,
    DCCTRL            ,
    DRVSTATUS         ,

    PWMCONF           ,
    PWM_SCALE         ,
    PWM_AUTO          ,
    LOST_STEPS        ,
    ]
