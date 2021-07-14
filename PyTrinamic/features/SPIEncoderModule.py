'''
Created on 13.07.2021

@author: JH
'''

from PyTrinamic.features.Feature import FeatureProvider
from PyTrinamic.features.SPIEncoder import SPIEncoder

class SPIEncoderModule(SPIEncoder,FeatureProvider):
        
    class __GROUPING(SPIEncoder,FeatureProvider):     
        def __init__(self, parent):
            self.parent = parent
                
        def set_resolution(self, steps):
            self.parent.set_axis_parameter(self.parent.APs.EncoderSteps,steps)
                                                
        def get_resolution(self):
            return self.parent.get_axis_parameter(self.parent.APs.EncoderSteps)

        def set_direction(self, direction):
            self.parent.set_axis_parameter(self.parent.APs.EncoderDirection,direction)

        def get_direction(self):
            return self.parent.get_axis_parameter(self.parent.APs.EncoderDirection)

        def set_init_mode(self, mode):
            self.parent.set_axis_parameter(self.parent.APs.EncoderInitMode,mode)

        def get_init_mode(self):
            return self.parent.get_axis_parameter(self.parent.APs.EncoderInitMode)

        def clear_once_on_n_channel(self):
            self.parent.set_axis_parameter(self.parent.APs.ClearOnce,1)
            self.parent.set_axis_parameter(self.parent.APs.ClearOnNull,1)

        resolution = property(get_resolution,set_resolution)
        direction = property(get_direction,set_direction)
        init_mode = property(get_init_mode,set_init_mode)
    
    def __init__(self):
        self.SPIEncoder = self.__GROUPING(self)