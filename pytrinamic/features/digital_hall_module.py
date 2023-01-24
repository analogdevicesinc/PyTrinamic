from ..features.digital_hall import DigitalHall


class DigitalHallModule(DigitalHall):
    
    def __init__(self, module, axis, aps):
        super().__init__(module, axis)
        self._aps = aps
        self._hasHallSensorDirection = False
        self._hasHallSensorPolarity = False
        self._hasHallSensorSectorOffset = False
        self._hasHallSensorOffset = False
        self._hasHallSensorInterpolation = False

        if hasattr(self._aps, "HallSensorDirection"):
            self._hasHallSensorDirection = True
        if hasattr(self._aps, "HallSensorPolarity"):
            self._hasHallSensorPolarity = True
        if hasattr(self._aps, "HallSensorSectorOffset"):
            self._hasHallSensorSectorOffset = True
        if hasattr(self._aps, "HallSensorOffset"):
            self._hasHallSensorOffset = True
        if hasattr(self._aps, "HallSensorInterpolation"):
            self._hasHallSensorInterpolation = True

    def set_direction(self, direction):
        if self._hasHallSensorDirection:
            self._parent.set_axis_parameter(self._aps.HallSensorDirection, self._axis, direction)

    def get_direction(self):
        if self._hasHallSensorDirection:
            return self._parent.get_axis_parameter(self._aps.HallSensorDirection, self._axis)
        else:
            return None

    def set_polarity(self, invert):
        if self._hasHallSensorPolarity:
            self._parent.set_axis_parameter(self._aps.HallSensorPolarity, self._axis, invert)

    def get_polarity(self):
        if self._hasHallSensorPolarity:
            return self._parent.get_axis_parameter(self._aps.HallSensorPolarity, self._axis)
        else:
            return None

    def set_sector_offset(self, sector_offset):
        if self._hasHallSensorSectorOffset:
            self._parent.set_axis_parameter(self._aps.HallSensorSectorOffset, self._axis, sector_offset)

    def get_sector_offset(self):
        if self._hasHallSensorSectorOffset:
            return self._parent.get_axis_parameter(self._aps.HallSensorSectorOffset, self._axis)
        else:
            return None

    def set_offset(self, offset):
        if self._hasHallSensorOffset:
            self._parent.set_axis_parameter(self._aps.HallSensorOffset, self._axis, offset)

    def get_offset(self):
        if self._hasHallSensorOffset:
            return self._parent.get_axis_parameter(self._aps.HallSensorOffset, self._axis)
        else:
            return None

    def set_interpolation(self, enable_interpolation):
        if self._hasHallSensorInterpolation:
            self._parent.set_axis_parameter(self._aps.HallSensorInterpolation, self._axis, enable_interpolation)

    def get_interpolation(self):
        if self._hasHallSensorInterpolation:
            return self._parent.get_axis_parameter(self._aps.HallSensorInterpolation, self._axis)
        else:
            return None

    # Properties
    direction = property(get_direction, set_direction)
    polarity = property(get_polarity, set_polarity)
    sector_offset = property(get_sector_offset, set_sector_offset)
    offset = property(get_offset, set_offset)
    interpolation = property(get_interpolation, set_interpolation)

    def __str__(self):
        values = "DigitalHall {"
        if self._hasHallSensorDirection:
            values += "'direction':" + str(self.direction) + ", "

        if self._hasHallSensorPolarity:
            values += "'polarity':" + str(self.polarity) + ", "

        if self._hasHallSensorSectorOffset:
            values += "'sector_offset':" + str(self.sector_offset) + ", "

        if self._hasHallSensorOffset:
            values += "'offset':" + str(self.offset) + ", "

        if self._hasHallSensorInterpolation:
            values += "'interpolation':" + str(self.interpolation) + ", "

        values = values[:-2]
        values += "}"
        return values
