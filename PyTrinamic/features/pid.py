from PyTrinamic.features.Feature import Feature


class PID(Feature):
 
    # torque/flux controller

    def set_torque_p_parameter(self, p_value):
        raise NotImplementedError()

    def get_torque_p_parameter(self):
        raise NotImplementedError()

    def set_torque_i_parameter(self, i_value):
        raise NotImplementedError()

    def get_torque_i_parameter(self):
        raise NotImplementedError()

    # velocity controller "

    def set_velocity_p_parameter(self, p_value):
        raise NotImplementedError()

    def get_velocity_p_parameter(self):
        raise NotImplementedError()

    def set_velocity_i_parameter(self, i_value):
        raise NotImplementedError()

    def get_velocity_i_parameter(self):
        raise NotImplementedError()

    # position controller

    def set_position_p_parameter(self, p_value):
        raise NotImplementedError()

    def get_position_p_parameter(self):
        raise NotImplementedError()
