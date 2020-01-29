'''
Created on 29.01.2020

@author: JM
'''

class TMC5031_register:
    """
    Define all registers of the TMC5031.

    Each register is defined either as an integer or as a tuple of integers.
    Each integer represents a register address. Tuples of addresses are used to
    represent a register that exists multiple times for multiple motors.
    """
    GCONF          = 0x00
    GSTAT          = 0x01
    SLAVECONF      = 0x03
    INPUT          = 0x04
    X_COMPARE      = 0x05
    RAMPMODE       = ( 0x20, 0x40)
    XACTUAL        = ( 0x21, 0x41)
    VACTUAL        = ( 0x22, 0x42)
    VSTART         = ( 0x23, 0x43)
    A1             = ( 0x24, 0x44) # ATM , no motor validation possible
    V1             = ( 0x25, 0x45)
    AMAX           = ( 0x26, 0x46)
    VMAX           = ( 0x27, 0x47)
    DMAX           = ( 0x28, 0x48)
    D1             = ( 0x2A, 0x4A)
    VSTOP          = ( 0x2B, 0x4B)
    TZEROWAIT      = ( 0x2C, 0x4C)
    XTARGET        = ( 0x2D, 0x4D)
    RAMPMODE_M2    = 0x40
    XACTUAL_M2     = 0x41
    VACTUAL_M2     = 0x42
    VSTART_M2      = 0x43
    A1_M2          = 0x44
    V1_M2          = 0x45
    AMAX_M2        = 0x46
    VMAX_M2        = 0x47
    DMAX_M2        = 0x48
    D1_M2          = 0x4A
    VSTOP_M2       = 0x4B
    TZEROWAIT_M2   = 0x4C
    XTARGET_M2     = 0x4D
    IHOLD_IRUN_M1  = 0x30
    VCOOLTHRS_M1   = 0x31
    VHIGH_M1       = 0x32
    SW_MODE_M1     = 0x34
    RAMP_STAT_M1   = 0x35
    XLATCH_M1      = 0x36
    IHOLD_IRUN_M2  = 0x50
    VCOOLTHRS_M2   = 0x51
    VHIGH_M2       = 0x52
    SW_MODE_M2     = 0x54
    RAMP_STAT_M2   = 0x55
    XLATCH_M2      = 0x56
    MSLUT___M1     = 0x60
    MSLUTSEL_M1    = 0x68
    MSLUTSTART_M1  = 0x69
    MSCNT_M1       = 0x6A
    MSCURACT_M1    = 0x6B
    CHOPCONF_M1    = 0x6C
    COOLCONF_M1    = 0x6D
    DRV_STATUS_M1  = 0x6F
    MSLUT___M2     = 0x70
    MSLUTSEL_M2    = 0x78
    MSLUTSTART_M2  = 0x79
    MSCNT_M2       = 0x7A
    MSCURACT_M2    = 0x7B
    CHOPCONF_M2    = 0x7C
    COOLCONF_M2    = 0x7D
    DRV_STATUS_M2  = 0x7F
