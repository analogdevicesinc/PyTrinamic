'''
Created on 01.01.2019

@author: ED
'''

class TMCM_0010_OPC(object):
    
    " brake chopper parameter "
    AP_SupplyVoltage            = 0
    AP_Enable                   = 1
    AP_VoltageLimit             = 2
    AP_Hysteresis               = 3
    AP_LowerVoltageLimit        = 4
    AP_Active                   = 5
    
    " diagnostic parameter "
    AP_MainLoopsPerSecond       = 200
    AP_UsbLoopsPerSecond        = 201

    def __init__(self, connection):
        self.connection = connection

    def showConfiguration(self):
        print("Brake chopper configuration:")
        print("\tenabled:       " + str(self.connection.axisParameter(self.AP_Enable, 0)))
        print("\tvoltage limit: " + str(self.connection.axisParameter(self.AP_VoltageLimit, 0) / 10) + "V")
        print("\thysteresis:    " + str(self.connection.axisParameter(self.AP_Hysteresis, 0) / 10) + "V")
