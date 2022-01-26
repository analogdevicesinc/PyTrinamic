class TMC5062_register:
    """
    Define all registers of the TMC5062.

    Each register is defined either as an integer or as a tuple of integers.
    Each integer represents a register address. Tuples of addresses are used to
    represent a register that exists multiple times for multiple motors.
    """
    GCONF           = 0x00
    GSTAT           = 0x01
    SLAVECONF       = 0x03
    INPUT_OUTPUT    = 0x04
    X_COMPARE       = 0x05
    RAMPMODE        = (0x20, 0x40)
    XACTUAL         = (0x21, 0x41)
    VACTUAL         = (0x22, 0x42)
    VSTART          = (0x23, 0x43)
    A1              = (0x24, 0x44)
    V1              = (0x25, 0x45)
    AMAX            = (0x26, 0x46)
    VMAX            = (0x27, 0x47)
    DMAX            = (0x28, 0x48)
    D1              = (0x2A, 0x4A)
    VSTOP           = (0x2B, 0x4B)
    TZEROWAIT       = (0x2C, 0x4C)
    XTARGET         = (0x2D, 0x4D)
    IHOLD_IRUN      = (0x30, 0x50)
    VCOOLTHRS       = (0x31, 0x51)
    VHIGH           = (0x32, 0x52)
    VDCMIN          = (0x33, 0x53)
    SW_MODE         = (0x34, 0x54)
    RAMP_STAT       = (0x35, 0x55)
    XLATCH          = (0x36, 0x56)
    ENCMODE         = (0x38, 0x58)

    X_ENC           = (0x39, 0x59)
    ENC_CONST       = (0x3A, 0x5A)
    ENC_STATUS      = (0x3B, 0x5B)
    ENC_LATCH       = (0x3C, 0x5C)

    MSLUT0          = (0x60, 0x70)
    MSLUT1          = (0x61, 0x71)
    MSLUT2          = (0x62, 0x72)
    MSLUT3          = (0x63, 0x73)
    MSLUT4          = (0x64, 0x74)
    MSLUT5          = (0x65, 0x75)
    MSLUT6          = (0x66, 0x76)
    MSLUT7          = (0x67, 0x77)
    MSLUTSEL        = (0x68, 0x78)
    MSLUTSTART      = (0x69, 0x79)
    MSCNT           = (0x6A, 0x7A)
    MSCURACT        = (0x6B, 0x7B)
    CHOPCONF        = (0x6C, 0x7C)
    COOLCONF        = (0x6D, 0x7D)
    DRV_STATUS      = (0x6F, 0x7F)