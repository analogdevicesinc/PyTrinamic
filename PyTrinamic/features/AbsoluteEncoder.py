from PyTrinamic.features.Feature import Feature


class AbsoluteEncoder(Feature):
        
    def set_type(self, encoder_type):
        """
        Set absolut encoder type that is used for this axis.
        This value is stored as AbsoluteEncoderType axis parameter.

        Parameters:
        type: Absolute encoder type
        """
        raise NotImplementedError()

    def get_type(self):
        """
        Gets absolut encoder type that is used for this axis.
        This value is stored in the  AbsoluteEncoderType axis parameter.

        Returns: Absolute encoder type
        """
        raise NotImplementedError()

    def set_resolution(self, resolution):
        raise NotImplementedError()

    def get_resolution(self):
        raise NotImplementedError()

    def set_init_mode(self, init_mode):
        """
        Sets absolute encoder init mode that is used for this axis.
        This value is stored as AbsoluteEncoderInit axis parameter.

        Parameters:
        init_mode: absolute encoder init mode
        """
        raise NotImplementedError()

    def get_init_mode(self):
        """
        Gets absolute encoder init mode that is used for this axis.
        This value is stored in the  AbsoluteEncoderInit axis parameter.

        Returns: absolute encoder init mode
        """
        raise NotImplementedError()

    def set_direction(self, direction):
        """
        Sets absolute encoder direction that is used for this axis.
        This value is stored as AbsoluteEncoderDirection axis parameter.

        Parameters:
        dir:  absolute encoder direction 
        """
        raise NotImplementedError()

    def get_direction(self):
        """
        Gets  absolute encoder direction that is used for this axis.
        This value is stored in the  AbsoluteEncoderDirection axis parameter.

        Returns:  absolute encoder direction 
        """
        raise NotImplementedError()

    def set_offset(self, offset):
        """
        Sets absolute encoder offset that is used for this axis.
        This value is stored as AbsoluteEncoderOffset axis parameter.

        Parameters:
        offset: absolute encoder offset
        """
        raise NotImplementedError()

    def get_offset(self):
        """
        Gets absolute encoder offset that is used for this axis.
        This value is stored in the  AbsoluteEncoderOffset axis parameter.

        Returns: absolute encoder offset
        """
        raise NotImplementedError()

    def __str__(self):
        values = "AbsoluteEncoder {"
        if self._hasAbsoluteEncoderType:
            values += "'type': " + str(self.type) + ", "
        if self._hasAbsoluteEncoderResolution:
            values += "'resolution': " + str(self.resolution) + ", "
        values += "'direction': " + str(self.direction) + ", "
        values += "'offset': " + str(self.offset) + ", "
        values += "'init_mode': " + str(self.init_mode)
        values += "}"
        return values

    type = property(get_type, set_type)
    resolution = property(get_resolution, set_resolution)
    init_mode = property(get_init_mode, set_init_mode)
    direction = property(get_direction, set_direction)
    offset = property(get_offset, set_offset)
