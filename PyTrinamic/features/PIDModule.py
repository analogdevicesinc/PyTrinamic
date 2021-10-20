'''
Created on 13.07.2021

@author: JH
'''

from PyTrinamic.features.Feature import FeatureProvider
from PyTrinamic.features.PID import PID

class PIDModule(PID,FeatureProvider):
    
    class __GROUPING(PID,FeatureProvider):      
        def __init__(self, parent):
            self.parent = parent

        def get_torque_p_parameter(self):
            return self.parent.get_axis_parameter(self.parent.APs.TorqueP)

        def set_torque_p_parameter(self, pValue):
            self.parent.set_axis_parameter(self.parent.APs.TorqueP,pValue)

        def get_torque_i_parameter(self):
            return self.parent.get_axis_parameter(self.parent.APs.TorqueI)
    
        def set_torque_i_parameter(self, iValue):
            self.parent.set_axis_parameter(self.parent.APs.TorqueI,iValue)

            
        " velocity controller "
        def get_velocity_p_parameter(self):
            return self.parent.get_axis_parameter(self.parent.APs.VelocityP)
    
        def set_velocity_p_parameter(self, pValue):
            self.parent.set_axis_parameter(self.parent.APs.VelocityP,pValue)

        def get_velocity_i_parameter(self):
            return self.parent.get_axis_parameter(self.parent.APs.VelocityI)

        def set_velocity_i_parameter(self, iValue):
            self.parent.set_axis_parameter(self.parent.APs.VelocityI,iValue)
        

        " position controller "
        def get_position_p_parameter(self):
            return self.parent.get_axis_parameter(self.parent.APs.PositionP)

        def set_position_p_parameter(self, pValue):
            self.parent.set_axis_parameter(self.parent.APs.PositionP,pValue)

       

        torque_p = property(get_torque_p_parameter,set_torque_p_parameter)
        torque_i = property(get_torque_i_parameter,set_torque_i_parameter)
        velocity_p = property(get_velocity_p_parameter,set_velocity_p_parameter)
        velocity_i = property(get_velocity_i_parameter,set_velocity_i_parameter)
        position_p = property(get_position_p_parameter,set_position_p_parameter)
        
    def __init__(self):
        self.PID = self.__GROUPING(self)