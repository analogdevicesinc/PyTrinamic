'''
Created on 17.10.2019

@author: JM
'''

class TMC2208_register:
    """
    Define all registers of the TMC2208.
    """
    GCONF         = 0x00
    GSTAT         = 0x01
    IFCNT         = 0x02
    SLAVECONF     = 0x03
    OTP_PROG      = 0x04
    OTP_READ      = 0x05
    IOIN          = 0x06
    FACTORY_CONF  = 0x07
    IHOLD_IRUN    = 0x10
    TPOWERDOWN    = 0x11
    TSTEP         = 0x12
    TPWMTHRS      = 0x13
    VACTUAL       = 0x22
    MSCNT         = 0x6A
    MSCURACT      = 0x6B
    CHOPCONF      = 0x6C
    DRV_STATUS    = 0x6F
    PWMCONF       = 0x70
    PWM_SCALE     = 0x71
    PWM_AUTO      = 0x72
