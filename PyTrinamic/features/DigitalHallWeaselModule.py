'''
Created on 13.07.2021

@author: JH
'''

from PyTrinamic.features.Feature import FeatureProvider
from PyTrinamic.features.DigitalHallWeasel import DigitalHallWeasel

class DigitalHallWeaselModule(DigitalHallWeasel,FeatureProvider):
    
    class __GROUPING(DigitalHallWeasel,FeatureProvider):
        def __init__(self, parent):
            self.parent = parent

        def set_direction(self, direction):
            self.parent.set_axis_parameter(self.parent.APs.HallSensorDirection,direction)

        def get_direction(self):
            return self.parent.get_axis_parameter(self.parent.APs.HallSensorDirection)

        def set_polarity(self, invert):
            self.parent.set_axis_parameter(self.parent.APs.HallSensorDirection,invert)

        def get_polarity(self):
            return self.parent.get_axis_parameter(self.parent.APs.HallSensorPolarity)

        def set_offset(self, offset):
            self.parent.set_axis_parameter(self.parent.APs.HallSensorOffset,offset)
            
        def get_offset(self):
            return self.parent.get_axis_parameter(self.parent.APs.HallSensorOffset)

        def set_interpolation(self, enableInterpolation):
            self.parent.set_axis_parameter(self.parent.APs.HallSensorInterpolation,enableInterpolation)
            
        def get_interpolation(self):
            return self.parent.get_axis_parameter(self.parent.APs.HallSensorInterpolation)
            
        direction = property(get_direction,set_direction)
        polarity  = property(get_polarity,set_polarity)
        offset  = property(get_offset,set_offset)
        interpolation = property(get_interpolation,set_interpolation)
    
    # Feature initialization
    def __init__(self):
        self.DigitalHallWeasel = self.__GROUPING(self)