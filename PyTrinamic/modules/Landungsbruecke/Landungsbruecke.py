'''
Created on 24.07.2019

@author: LK
'''

class _GPs():
    VitalSignsErrorMask  = 1
    DriversEnable        = 2
    DebugMode            = 3
    BoardAssignment      = 4
    HWID                 = 5
    PinState             = 6

class Landungsbruecke():
    def __init__(self, connection):
        self.GPs   = _GPs
        self.__connection = connection
