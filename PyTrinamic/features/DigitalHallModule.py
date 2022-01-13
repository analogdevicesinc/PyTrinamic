from PyTrinamic.features.Feature import FeatureProvider
from PyTrinamic.features.DigitalHall import DigitalHall


class DigitalHallModule(DigitalHall, FeatureProvider):
    
    class __GROUPING(DigitalHall, FeatureProvider):
        def __init__(self, parent):
            self.parent = parent

            self._hasHallSensorDirection = False
            self._hasHallSensorPolarity = False
            self._hasHallSensorOffset = False
            self._hasHallSensorInterpolation = False

            if hasattr(parent.APs, "HallSensorDirection"):
                self._hasHallSensorDirection = True
            if hasattr(parent.APs, "HallSensorPolarity"):
                self._hasHallSensorPolarity = True
            if hasattr(parent.APs, "HallSensorOffset"):
                self._hasHallSensorOffset = True
            if hasattr(parent.APs, "HallSensorInterpolation"):
                self._hasHallSensorInterpolation = True

        def set_direction(self, direction):
            if self._hasHallSensorDirection:
                self.parent.set_axis_parameter(self.parent.APs.HallSensorDirection, direction)

        def get_direction(self):
            if self._hasHallSensorDirection:
                return self.parent.get_axis_parameter(self.parent.APs.HallSensorDirection)
            else:
                return None

        def set_polarity(self, invert):
            if self._hasHallSensorPolarity:
                self.parent.set_axis_parameter(self.parent.APs.HallSensorPolarity, invert)

        def get_polarity(self):
            if self._hasHallSensorPolarity:
                return self.parent.get_axis_parameter(self.parent.APs.HallSensorPolarity)
            else:
                return None

        def set_offset(self, offset):
            if self._hasHallSensorOffset:
                self.parent.set_axis_parameter(self.parent.APs.HallSensorOffset, offset)
            
        def get_offset(self):
            if self._hasHallSensorOffset:
                return self.parent.get_axis_parameter(self.parent.APs.HallSensorOffset)
            else:
                return None

        def set_interpolation(self, enable_interpolation):
            if self._hasHallSensorInterpolation:
                self.parent.set_axis_parameter(self.parent.APs.HallSensorInterpolation, enable_interpolation)
            
        def get_interpolation(self):
            if self._hasHallSensorInterpolation:
                return self.parent.get_axis_parameter(self.parent.APs.HallSensorInterpolation)
            else:
                return None

        def __str__(self):
            values = "DigitalHall {"
            if self._hasHallSensorDirection:
                values += "'direction':" + str(self.direction) + ", "

            if self._hasHallSensorPolarity:
                values += "'polarity':" + str(self.polarity) + ", "

            if self._hasHallSensorOffset:
                values += "'offset':" + str(self.offset) + ", "

            if self._hasHallSensorInterpolation:
                values += "'interpolation':" + str(self.interpolation) + ", "

            values = values[:-2]
            values += "}"
            return values

        direction = property(get_direction, set_direction)
        polarity = property(get_polarity, set_polarity)
        offset = property(get_offset, set_offset)
        interpolation = property(get_interpolation, set_interpolation)

    # Feature initialization
    def __init__(self):
        self.DigitalHall = self.__GROUPING(self)
