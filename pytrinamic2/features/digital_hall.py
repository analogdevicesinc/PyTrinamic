from abc import ABC


class DigitalHall(ABC):
 
    def set_direction(self, direction):
        raise NotImplementedError

    def get_direction(self):
        raise NotImplementedError

    def set_polarity(self, polarity):
        raise NotImplementedError

    def get_polarity(self):
        raise NotImplementedError

    def set_offset(self, offset):
        raise NotImplementedError
        
    def get_offset(self):
        raise NotImplementedError

    def set_interpolation(self, enable_interpolation):
        raise NotImplementedError
        
    def get_interpolation(self):
        raise NotImplementedError
