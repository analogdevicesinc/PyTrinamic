from PyTrinamic.features.Feature import FeatureProvider
from PyTrinamic.features.PID import PID


class PIDModule(PID, FeatureProvider):
    
    class __GROUPING(PID, FeatureProvider):
        def __init__(self, parent):
            self.parent = parent

        # torque/flux controller
        def get_torque_p_parameter(self):
            return self.parent.get_axis_parameter(self.parent.APs.TorqueP)

        def set_torque_p_parameter(self, p_value):
            self.parent.set_axis_parameter(self.parent.APs.TorqueP, p_value)

        def get_torque_i_parameter(self):
            return self.parent.get_axis_parameter(self.parent.APs.TorqueI)
    
        def set_torque_i_parameter(self, i_value):
            self.parent.set_axis_parameter(self.parent.APs.TorqueI, i_value)

        # velocity controller
        def get_velocity_p_parameter(self):
            return self.parent.get_axis_parameter(self.parent.APs.VelocityP)
    
        def set_velocity_p_parameter(self, p_value):
            self.parent.set_axis_parameter(self.parent.APs.VelocityP, p_value)

        def get_velocity_i_parameter(self):
            return self.parent.get_axis_parameter(self.parent.APs.VelocityI)

        def set_velocity_i_parameter(self, i_value):
            self.parent.set_axis_parameter(self.parent.APs.VelocityI, i_value)
        
        # position controller
        def get_position_p_parameter(self):
            return self.parent.get_axis_parameter(self.parent.APs.PositionP)

        def set_position_p_parameter(self, p_value):
            self.parent.set_axis_parameter(self.parent.APs.PositionP, p_value)

        torque_p = property(get_torque_p_parameter, set_torque_p_parameter)
        torque_i = property(get_torque_i_parameter, set_torque_i_parameter)
        velocity_p = property(get_velocity_p_parameter, set_velocity_p_parameter)
        velocity_i = property(get_velocity_i_parameter, set_velocity_i_parameter)
        position_p = property(get_position_p_parameter, set_position_p_parameter)

    def __init__(self):
        self.PID = self.__GROUPING(self)
