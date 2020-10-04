'''
Created on 29.09.2020

@author: ED
'''

from abc import ABC

class digital_hall_ap_feature(ABC):
 
    def __init__(self, parent):
        self._motorInterface = parent
        
    def hallInvert(self):
        return self._motorInterface.axisParameter(self._motorInterface.AP.HallSensorInvert)

    def setHallInvert(self, invert):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.HallSensorInvert, invert)

    def showConfiguration(self):
        print("Digital hall configuration:")
        print("\tHall invert: " + str(self.hallInvert()))
