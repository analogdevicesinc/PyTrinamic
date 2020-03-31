'''
Created on 30.03.2020

@author: JM
'''

class TMC7300_register(object):
    
    GCONF          = 0x00
    GSTAT          = 0x01
    IFCNT          = 0x02
    SLAVECONF      = 0x03
    IOIN           = 0x06
    CURRENT_LIMIT  = 0x10
    PWM_AB         = 0x22
    CHOPCONF       = 0x6C
    DRV_STATUS     = 0x6F
    PWMCONF        = 0x70
