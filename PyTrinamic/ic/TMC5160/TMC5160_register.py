'''
Created on 24.10.2019

@author: JM
'''

class TMC5160_register:
    """
    Define all registers of the TMC5160.
    """

    GCONF          = 0x00
    GSTAT          = 0x01
    IFCNT          = 0x02
    SLAVECONF      = 0x03
    IOIN___OUTPUT  = 0x04
    X_COMPARE      = 0x05
    OTP_PROG       = 0x06
    OTP_READ       = 0x07
    FACTORY_CONF   = 0x08
    SHORT_CONF     = 0x09
    DRV_CONF       = 0x0A
    GLOBAL_SCALER  = 0x0B
    OFFSET_READ    = 0x0C
    IHOLD_IRUN     = 0x10
    TPOWERDOWN     = 0x11
    TSTEP          = 0x12
    TPWMTHRS       = 0x13
    TCOOLTHRS      = 0x14
    THIGH          = 0x15
    RAMPMODE       = 0x20
    XACTUAL        = 0x21
    VACTUAL        = 0x22
    VSTART         = 0x23
    A1             = 0x24
    V1             = 0x25
    AMAX           = 0x26
    VMAX           = 0x27
    DMAX           = 0x28
    D1             = 0x2A
    VSTOP          = 0x2B
    TZEROWAIT      = 0x2C
    XTARGET        = 0x2D
    VDCMIN         = 0x33
    SW_MODE        = 0x34
    RAMP_STAT      = 0x35
    XLATCH         = 0x36
    ENCMODE        = 0x38
    X_ENC          = 0x39
    ENC_CONST      = 0x3A
    ENC_STATUS     = 0x3B
    ENC_LATCH      = 0x3C
    ENC_DEVIATION  = 0x3D
    MSLUT__        = 0x60
    MSLUTSEL       = 0x68
    MSLUTSTART     = 0x69
    MSCNT          = 0x6A
    MSCURACT       = 0x6B
    CHOPCONF       = 0x6C
    COOLCONF       = 0x6D
    DCCTRL         = 0x6E
    DRV_STATUS     = 0x6F
    PWMCONF        = 0x70
    PWM_SCALE      = 0x71
    PWM_AUTO       = 0x72
    LOST_STEPS     = 0x73

    dict = {
        "GCONF": GCONF,
        "GSTAT": GSTAT,
        "IFCNT": IFCNT,
        "SLAVECONF": SLAVECONF,
        "IOIN___OUTPUT": IOIN___OUTPUT,
        "X_COMPARE": X_COMPARE,
        "OTP_PROG": OTP_PROG,
        "OTP_READ": OTP_READ,
        "FACTORY_CONF": FACTORY_CONF,
        "SHORT_CONF": SHORT_CONF,
        "DRV_CONF": DRV_CONF,
        "GLOBAL_SCALER": GLOBAL_SCALER,
        "OFFSET_READ": OFFSET_READ,
        "IHOLD_IRUN": IHOLD_IRUN,
        "TPOWERDOWN": TPOWERDOWN,
        "TSTEP": TSTEP,
        "TPWMTHRS": TPWMTHRS,
        "TCOOLTHRS": TCOOLTHRS,
        "THIGH": THIGH,
        "RAMPMODE": RAMPMODE,
        "XACTUAL": XACTUAL,
        "VACTUAL": VACTUAL,
        "VSTART": VSTART,
        "A1": A1,
        "V1": V1,
        "AMAX": AMAX,
        "VMAX": VMAX,
        "DMAX": DMAX,
        "D1": D1,
        "VSTOP": VSTOP,
        "TZEROWAIT": TZEROWAIT,
        "XTARGET": XTARGET,
        "VDCMIN": VDCMIN,
        "SW_MODE": SW_MODE,
        "RAMP_STAT": RAMP_STAT,
        "XLATCH": XLATCH,
        "ENCMODE": ENCMODE,
        "X_ENC": X_ENC,
        "ENC_CONST": ENC_CONST,
        "ENC_STATUS": ENC_STATUS,
        "ENC_LATCH": ENC_LATCH,
        "ENC_DEVIATION": ENC_DEVIATION,
        "MSLUT__": MSLUT__,
        "MSLUTSEL": MSLUTSEL,
        "MSLUTSTART": MSLUTSTART,
        "MSCNT": MSCNT,
        "MSCURACT": MSCURACT,
        "CHOPCONF": CHOPCONF,
        "COOLCONF": COOLCONF,
        "DCCTRL": DCCTRL,
        "DRV_STATUS": DRV_STATUS,
        "PWMCONF": PWMCONF,
        "PWM_SCALE": PWM_SCALE,
        "PWM_AUTO": PWM_AUTO,
        "LOST_STEPS": LOST_STEPS,
    }
