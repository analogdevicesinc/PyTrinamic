'''
Created on 13.07.2021

@author: JH
'''

from PyTrinamic.features.Feature import FeatureProvider
from PyTrinamic.features.DigitalHall import DigitalHall

class DigitalHallModule(DigitalHall,FeatureProvider):
        
    class __GROUPING(DigitalHall,FeatureProvider):      
        def get_hall_invert(self):
            return self.parent.get_axis_parameter(self.parent.APs.HallSensorInvert)

        def set_hall_invert(self, invert):
            self.parent.set_axis_parameter(self.parent.APs.HallSensorInvert,invert)

        hall = property(get_hall_invert,set_hall_invert)

    def __init__(self):
        self.DigitalHall = self.__GROUPING(self)