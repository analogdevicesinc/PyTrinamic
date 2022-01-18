from PyTrinamic.features.feature import FeatureProvider
from PyTrinamic.features.pid import PID


class PIDModule:

    def __init__(self):
        self.PID = self.__GROUPING(self)

    class __GROUPING(PID, FeatureProvider):

        def __init__(self, motor):
            self._motor = motor

        # torque/flux controller

        def set_torque_p_parameter(self, p_value):
            self._motor.set_axis_parameter(self._motor.AP.TorqueP, p_value)

        def get_torque_p_parameter(self):
            return self._motor.get_axis_parameter(self._motor.AP.TorqueP)

        def set_torque_i_parameter(self, i_value):
            self._motor.set_axis_parameter(self._motor.AP.TorqueI, i_value)

        def get_torque_i_parameter(self):
            return self._motor.get_axis_parameter(self._motor.AP.TorqueI)

        # velocity controller

        def set_velocity_p_parameter(self, p_value):
            self._motor.set_axis_parameter(self._motor.AP.VelocityP, p_value)

        def get_velocity_p_parameter(self):
            return self._motor.get_axis_parameter(self._motor.AP.VelocityP)

        def set_velocity_i_parameter(self, i_value):
            self._motor.set_axis_parameter(self._motor.AP.VelocityI, i_value)

        def get_velocity_i_parameter(self):
            return self._motor.get_axis_parameter(self._motor.AP.VelocityI)

        # position controller

        def set_position_p_parameter(self, p_value):
            self._motor.set_axis_parameter(self._motor.AP.PositionP, p_value)

        def get_position_p_parameter(self):
            return self._motor.get_axis_parameter(self._motor.AP.PositionP)

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
