'''
Created on 14.06.2020

@author:JH
'''
from PyTrinamic.features.Feature import Feature

class ABNEncoder(Feature):
        
    def set_resolution(self, steps):
        raise NotImplementedError()
                                             
    def get_resolution(self):
        raise NotImplementedError()

    def set_direction(self, direction):
        raise NotImplementedError()

    def get_direction(self):
        raise NotImplementedError()

    def set_init_mode(self, mode):
        raise NotImplementedError()

    def get_init_mode(self):
       raise NotImplementedError()

    def clear_once_on_n_channel(self):
        raise NotImplementedError()
    
    def __str__(self):
            return "{} {}".format(
                "ABNEncoder",
                {
                    "resolution": self.resolution,
                    "direction": self.direction,
                    "init_mode": self.init_mode
                }
            )
    
    resolution = property(get_resolution,set_resolution)
    direction  = property(get_direction,set_direction)
    init_mode  = property(get_init_mode,set_init_mode)