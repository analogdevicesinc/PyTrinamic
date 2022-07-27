from ..features.pid import PID


class PIDModule(PID):

    def __init__(self, module, axis, aps):
        super().__init__(module, axis)
        self._aps = aps

    # torque/flux controller

    def set_torque_p_parameter(self, p_value):
        self._parent.set_axis_parameter(self._aps.TorqueP, self._axis, p_value)

    def get_torque_p_parameter(self):
        return self._parent.get_axis_parameter(self._aps.TorqueP, self._axis)

    def set_torque_i_parameter(self, i_value):
        self._parent.set_axis_parameter(self._aps.TorqueI, self._axis, i_value)

    def get_torque_i_parameter(self):
        return self._parent.get_axis_parameter(self._aps.TorqueI, self._axis)

    # velocity controller

    def set_velocity_p_parameter(self, p_value):
        self._parent.set_axis_parameter(self._aps.VelocityP, self._axis, p_value)

    def get_velocity_p_parameter(self):
        return self._parent.get_axis_parameter(self._aps.VelocityP, self._axis)

    def set_velocity_i_parameter(self, i_value):
        self._parent.set_axis_parameter(self._aps.VelocityI, self._axis, i_value)

    def get_velocity_i_parameter(self):
        return self._parent.get_axis_parameter(self._aps.VelocityI, self._axis)

    # position controller

    def set_position_p_parameter(self, p_value):
        self._parent.set_axis_parameter(self._aps.PositionP, self._axis, p_value)

    def get_position_p_parameter(self):
        return self._parent.get_axis_parameter(self._aps.PositionP, self._axis)

    # properties
    torque_p = property(get_torque_p_parameter, set_torque_p_parameter)
    torque_i = property(get_torque_i_parameter, set_torque_i_parameter)
    velocity_p = property(get_velocity_p_parameter, set_velocity_p_parameter)
    velocity_i = property(get_velocity_i_parameter, set_velocity_i_parameter)
    position_p = property(get_position_p_parameter, set_position_p_parameter)

    def __str__(self):
        return "{} {}".format(
            "PID",
            {
                "torque_p": self.torque_p,
                "torque_i": self.torque_i,
                "velocity_p": self.velocity_p,
                "velocity_i": self.velocity_i,
                "position_p": self.position_p,
            }
        )
