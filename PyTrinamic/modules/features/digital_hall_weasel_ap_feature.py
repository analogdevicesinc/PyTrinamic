'''
Created on 29.09.2020

@author: ED
'''

from abc import ABC

class digital_hall_weasel_ap_feature(ABC):
 
    def __init__(self, parent):
        self._motorInterface = parent

    def setDirection(self, direction):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.HallSensorDirection, direction)

    def direction(self):
        return self._motorInterface.axisParameter(self._motorInterface.AP.HallSensorDirection)

    def setPolarity(self, invert):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.HallSensorPolarity, invert)

    def polarity(self):
        return self._motorInterface.axisParameter(self._motorInterface.AP.HallSensorPolarity)

    def setOffset(self, offset):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.HallSensorOffset, offset)
        
    def offset(self):
        return  self._motorInterface.axisParameter(self._motorInterface.AP.HallSensorOffset)

    def setInterpolation(self, enableInterpolation):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.HallSensorInterpolation, enableInterpolation)
        
    def interpolation(self):
        return self._motorInterface.axisParameter(self._motorInterface.AP.HallSensorInterpolation)
        
    def showConfiguration(self):
        print("Digital hall configuration:")
        print("\tDirection: " + str(self.direction()))
        print("\tPolarity:  " + str(self.polarity()))
        print("\tOffset:    " + str(self.offset()))
        print("\tInterpolation: " + ("disabled" if (self.interpolation()==0) else "enabled"))
