from PyTrinamic.features.abn_encoder import ABNEncoder


class ABNEncoderModule(ABNEncoder):
    
    def __init__(self, module, axis, aps):
        self._module = module
        self._axis = axis
        self._aps = aps

    def set_resolution(self, steps):
        self._module.set_axis_parameter(self._aps.EncoderSteps, self._axis, steps)
                                                
    def get_resolution(self):
        return self._module.get_axis_parameter(self._aps.EncoderSteps, self._axis,)

    def set_direction(self, direction):
        self._module.set_axis_parameter(self._aps.EncoderDirection, self._axis, direction)

    def get_direction(self):
        return self._module.get_axis_parameter(self._aps.EncoderDirection, self._axis,)

    def set_init_mode(self, mode):
        self._module.set_axis_parameter(self._aps.EncoderInitMode, self._axis, mode)

    def get_init_mode(self):
        return self._module.get_axis_parameter(self._aps.EncoderInitMode, self._axis,)

    def clear_once_on_n_channel(self):
        self._module.set_axis_parameter(self._aps.ClearOnce, self._axis, 1)
        self._module.set_axis_parameter(self._aps.ClearOnNull, self._axis, 1)

    def __str__(self):
        return "{} {}".format(
            "ABNEncoder",
            {
                "resolution": self.resolution,
                "direction": self.direction,
                "init_mode": self.init_mode
            }
        )

    resolution = property(get_resolution, set_resolution)
    direction = property(get_direction, set_direction)
    init_mode = property(get_init_mode, set_init_mode)