'''
Created on 27.03.2020

@author: JM
'''

class TMC2300_register(object):
    
    GCONF       = 0x00
    GSTAT       = 0x01
    IFCNT       = 0x02
    SLAVECONF   = 0x03
    IOIN        = 0x06
    IHOLD_IRUN  = 0x10
    TPOWERDOWN  = 0x11
    TSTEP       = 0x12
    TCOOLTHRS   = 0x14
    VACTUAL     = 0x22
    SGTHRS      = 0x40
    SG_VALUE    = 0x41
    COOLCONF    = 0x42
    MSCNT       = 0x6A
    MSCURACT    = 0x6B
    CHOPCONF    = 0x6C
    DRV_STATUS  = 0x6F
    PWMCONF     = 0x70
    PWM_SCALE   = 0x71
    PWM_AUTO    = 0x72