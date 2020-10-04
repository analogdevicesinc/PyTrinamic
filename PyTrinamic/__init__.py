'''
Created on 30.12.2018

@author: ED
'''

name = "PyTrinamic"
desc = "TRINAMIC's Python Technology Access Package"

def showInfo():
    print(name + " - " + desc)
    
" motor types "
class MotorTypes():
    DC              = 0
    BLDC            = 1
    DC_BLDC         = 2
    STEPPER         = 3
    DC_BLDC_STEPPER = 4