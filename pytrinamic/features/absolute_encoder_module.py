from ..features.absolute_encoder import AbsoluteEncoder


class AbsoluteEncoderModule(AbsoluteEncoder):
        
    def __init__(self, module, axis, aps):
        super().__init__(module, axis)
        self._aps = aps
        self._hasAbsoluteEncoderType = False
        self._hasAbsoluteEncoderResolution = False

        if hasattr(self._aps, "AbsoluteEncoderType"):
            self._hasAbsoluteEncoderType = True
        if hasattr(self._aps, "AbsoluteEncoderSteps"):
            self._hasAbsoluteEncoderResolution = True

    def set_type(self, encoder_type):
        """
        Set absolut encoder type that is used for this axis.
        This value is stored as AbsoluteEncoderType axis parameter.

        Parameters:
        encoder_type: Absolute encoder type
        """
        if self._hasAbsoluteEncoderType:
            self._parent.set_axis_parameter(self._aps.AbsoluteEncoderType, self._axis, encoder_type)

    def get_type(self):
        """
        Gets absolut encoder type that is used for this axis.
        This value is stored in the  AbsoluteEncoderType axis parameter.

        Returns: Absolute encoder type
        """
        if self._hasAbsoluteEncoderType:
            return self._parent.get_axis_parameter(self._aps.AbsoluteEncoderType, self._axis)
        else:
            return None

    def set_resolution(self, resolution):
        """
        Resolution is typically constant depending on the selected absolute encoder type.
        """
        pass

    def get_resolution(self):
        if self._hasAbsoluteEncoderResolution:
            return self._parent.get_axis_parameter(self._aps.AbsoluteEncoderSteps, self._axis)
        else:
            return None

    def set_init_mode(self, init_mode):
        """
        Sets absolute encoder init mode that is used for this axis.
        This value is stored as AbsoluteEncoderInitMode axis parameter.

        Parameters:
        init_mode: absolute encoder init mode
        """
        self._parent.set_axis_parameter(self._aps.AbsoluteEncoderInitMode, self._axis, init_mode)

    def get_init_mode(self):
        """
        Gets absolute encoder init that is used for this axis.
        This value is stored in the  AbsoluteEncoderInit axis parameter.

        Returns: absolute encoder init
        """
        return self._parent.get_axis_parameter(self._aps.AbsoluteEncoderInitMode, self._axis)

    def set_direction(self, direction):
        """
        Sets absolute encoder direction that is used for this axis.
        This value is stored as AbsoluteEncoderDirection axis parameter.

        Parameters:
        dir:  absolute encoder direction
        """
        self._parent.set_axis_parameter(self._aps.AbsoluteEncoderDirection, self._axis, direction)

    def get_direction(self):
        """
        Gets  absolute encoder direction that is used for this axis.
        This value is stored in the  AbsoluteEncoderDirection axis parameter.

        Returns:  absolute encoder direction
        """
        return self._parent.get_axis_parameter(self._aps.AbsoluteEncoderDirection, self._axis)

    def set_offset(self, offset):
        """
        Sets absolute encoder offset that is used for this axis.
        This value is stored as AbsoluteEncoderOffset axis parameter.

        Parameters:
        offset: absolute encoder offset
        """
        self._parent.set_axis_parameter(self._aps.AbsoluteEncoderOffset, self._axis, offset)

    def get_offset(self):
        """
        Gets absolute encoder offset that is used for this axis.
        This value is stored in the  AbsoluteEncoderOffset axis parameter.

        Returns: absolute encoder offset
        """
        return self._parent.get_axis_parameter(self._aps.AbsoluteEncoderOffset, self._axis)

    # Properties
    type = property(get_type, set_type)
    resolution = property(get_resolution, set_resolution)
    init_mode = property(get_init_mode, set_init_mode)
    direction = property(get_direction, set_direction)
    offset = property(get_offset, set_offset)

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
