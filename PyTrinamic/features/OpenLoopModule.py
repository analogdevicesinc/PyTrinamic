'''
Created on 13.07.2021

@author: JH
'''

from PyTrinamic.features.Feature import FeatureProvider
from PyTrinamic.features.OpenLoop import OpenLoop

class OpenLoopModule(OpenLoop,FeatureProvider):
 
    class __GROUPING(OpenLoop,FeatureProvider):

        def set_open_loop_torque(self, torque):
            self.parent.set_axis_parameter(self.parent.APs.StartCurrent,torque)

        def get_open_loop_torque(self):
            return self.parent.get_axis_parameter(self.parent.APs.StartCurrent)
   
        open_loop_torque = property(get_open_loop_torque,set_open_loop_torque)
    
    def __init__(self):
            self.OpenLoop = self.__GROUPING(self)