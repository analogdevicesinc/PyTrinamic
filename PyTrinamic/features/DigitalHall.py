'''
Created on 13.07.2021

@author: JH
'''


from PyTrinamic.features.Feature import Feature


class DigitalHall(Feature):
 
    def set_direction(self, direction):
        raise NotImplementedError()

    def get_direction(self):
        raise NotImplementedError()

    def set_polarity(self, invert):
        raise NotImplementedError()

    def get_polarity(self):
        raise NotImplementedError()

    def set_offset(self, offset):
        raise NotImplementedError()
        
    def get_offset(self):
        raise NotImplementedError()

    def set_interpolation(self, enable_interpolation):
        raise NotImplementedError()
        
    def get_interpolation(self):
        raise NotImplementedError()
        
    def __str__(self):
            return "{} {}".format(
                "DigitalHall",
                {
                    "direction": self.direction,
                    "polarity": self.polarity,
                    "offset": self.offset,
                    "interpolation": self.interpolation
                }
            )
    
    direction = property(get_direction, set_direction)
    polarity = property(get_polarity, set_polarity)
    offset = property(get_offset, set_offset)
    interpolation = property(get_interpolation, set_interpolation)
