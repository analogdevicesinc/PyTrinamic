'''
Created on 13.07.2021

@author: JH
'''

from PyTrinamic.features.Feature import Feature

class DigitalHall(Feature):
        
    def get_hall_invert(self):
        raise NotImplementedError()

    def set_hall_invert(self, invert):
        raise NotImplementedError()

    def __str__(self):
            return "{} {}".format(
                "Hall",
                {
                    "hall": self.hall,
                    "direction": self.direction,
                    "init_mode": self.init_mode
                }
            )
    
    hall = property(get_hall_invert,set_hall_invert)

