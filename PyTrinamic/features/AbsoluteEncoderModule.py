from PyTrinamic.features.Feature import FeatureProvider
from PyTrinamic.features.AbsoluteEncoder import AbsoluteEncoder


class AbsoluteEncoderModule(AbsoluteEncoder, FeatureProvider):
        
    class __GROUPING(AbsoluteEncoder, FeatureProvider):
        def __init__(self, parent):
            self.parent = parent

            self._hasAbsoluteEncoderType = False
            self._hasAbsoluteEncoderResolution = False

            if hasattr(parent.AP, "AbsoluteEncoderType"):
                self._hasAbsoluteEncoderType = True
            if hasattr(parent.AP, "AbsoluteEncoderSteps"):
                self._hasAbsoluteEncoderResolution = True

        def set_type(self, encoder_type):
            """
            Set absolut encoder type that is used for this axis.
            This value is stored as AbsoluteEncoderType axis parameter.

            Parameters:
            type: Absolute encoder type
            """
            if self._hasAbsoluteEncoderType:
                self.parent.set_axis_parameter(self.parent.AP.AbsoluteEncoderType, type)

        def get_type(self):
            """
            Gets absolut encoder type that is used for this axis.
            This value is stored in the  AbsoluteEncoderType axis parameter.

            Returns: Absolute encoder type
            """
            if self._hasAbsoluteEncoderType:
                return self.parent.get_axis_parameter(self.parent.AP.AbsoluteEncoderType)
            else:
                return None

        def set_resolution(self, resolution):
            """
            Resolution is typically constant depending on the selected absolute encoder type.
            """
            raise NotImplementedError()

        def get_resolution(self):
            if self._hasAbsoluteEncoderResolution:
                return self.parent.get_axis_parameter(self.parent.AP.AbsoluteEncoderSteps)
            else:
                return None

        def set_init_mode(self, init_mode):
            """
            Sets absolute encoder init mode that is used for this axis.
            This value is stored as AbsoluteEncoderInitMode axis parameter.

            Parameters:
            init_mode: absolute encoder init mode
            """
            self.parent.set_axis_parameter(self.parent.AP.AbsoluteEncoderInitMode, init_mode)

        def get_init_mode(self):
            """
            Gets absolute encoder init that is used for this axis.
            This value is stored in the  AbsoluteEncoderInit axis parameter.

            Returns: absolute encoder init
            """
            return self.parent.get_axis_parameter(self.parent.AP.AbsoluteEncoderInitMode)

        def set_direction(self, direction):
            """
            Sets absolute encoder direction that is used for this axis.
            This value is stored as AbsoluteEncoderDirection axis parameter.

            Parameters:
            dir:  absolute encoder direction 
            """
            self.parent.set_axis_parameter(self.parent.AP.AbsoluteEncoderDirection, direction)

        def get_direction(self):
            """
            Gets  absolute encoder direction that is used for this axis.
            This value is stored in the  AbsoluteEncoderDirection axis parameter.

            Returns:  absolute encoder direction 
            """
            return self.parent.get_axis_parameter(self.parent.AP.AbsoluteEncoderDirection)

        def set_offset(self, offset):
            """
            Sets absolute encoder offset that is used for this axis.
            This value is stored as AbsoluteEncoderOffset axis parameter.

            Parameters:
            offset: absolute encoder offset
            """
            self.parent.set_axis_parameter(self.parent.AP.AbsoluteEncoderOffset, offset)

        def get_offset(self):
            """
            Gets absolute encoder offset that is used for this axis.
            This value is stored in the  AbsoluteEncoderOffset axis parameter.

            Returns: absolute encoder offset
            """
            return self.parent.get_axis_parameter(self.parent.AP.AbsoluteEncoderOffset)

        type = property(get_type, set_type)
        resolution = property(get_resolution, set_resolution)
        init_mode = property(get_init_mode, set_init_mode)
        direction = property(get_direction, set_direction)
        offset = property(get_offset, set_offset)
    
    # Feature initialization
    def __init__(self):
        self.AbsoluteEncoder = self.__GROUPING(self)
