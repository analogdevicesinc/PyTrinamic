'''
Created on 13.07.2021

@author: JH
'''

from PyTrinamic.features.Feature import Feature

class PID(Feature):
 
    " torque/flux controller "
    def get_torque_p_parameter(self):
        raise NotImplementedError()
    def set_torque_p_parameter(self, pValue):
        raise NotImplementedError()

    def get_torque_i_parameter(self):
        raise NotImplementedError()
    def set_torque_i_parameter(self, iValue):
        raise NotImplementedError()

        
    " velocity controller "
    def get_velocity_p_parameter(self):
        raise NotImplementedError()
    def set_velocity_p_parameter(self, pValue):
        raise NotImplementedError()

    def get_velocity_i_parameter(self):
        raise NotImplementedError()
    def set_velocity_i_parameter(self, iValue):
        raise NotImplementedError()

    def set_velocity_sensor(self, sensor):
        raise NotADirectoryError()
    def get_velocity_sensor(self):
        raise NotImplementedError()

    " position controller "
    def get_position_p_parameter(self):
        raise NotImplementedError()
    def set_position_p_parameter(self, pValue):
        raise NotImplementedError()

    def set_position_sensor(self, sensor):
        raise NotADirectoryError()
    def get_position_sensor(self):
        raise NotImplementedError()

    def __str__(self):
        return "{} {}".format(
            "PID",
            {
                "torque_p": self.torque_p,
                "torque_i": self.torque_i,

                "velocity_p": self.velocity_p,
                "velocity_i": self.velocity_i,
                "velocity_sensor": self.velocity_sensor,
                
                "position_p": self.position_p,
                "position_sensor": self.position_sensor,


            }
        )

    torque_p = property(get_torque_p_parameter,set_torque_p_parameter)
    torque_i = property(get_torque_i_parameter,set_torque_i_parameter)
    velocity_p = property(get_velocity_p_parameter,set_velocity_p_parameter)
    velocity_i = property(get_velocity_i_parameter,set_velocity_i_parameter)
    velocity_sensor = property(get_velocity_sensor,set_velocity_sensor)
    position_p = property(get_position_p_parameter,set_position_p_parameter)
    position_sensor = property(get_position_sensor,set_position_sensor)
