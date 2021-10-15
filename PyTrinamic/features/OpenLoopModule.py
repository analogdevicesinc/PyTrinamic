'''
Created on 13.07.2021

@author: JH
'''

from PyTrinamic.features.Feature import FeatureProvider
from PyTrinamic.features.OpenLoop import OpenLoop

class OpenLoopModule(OpenLoop,FeatureProvider):
 
    class __GROUPING(OpenLoop,FeatureProvider):
        def __init__(self, parent):
                    self.parent = parent

        def set_open_loop_torque(self, current):
            """
            Sets if open loop torque that is used for this axis.
            This value is stored as OpenLoopCurrent axis parameter.

            Parameters:
            current: Open Loop Current
            """
            self.parent.set_axis_parameter(self.parent.APs.OpenLoopCurrent,current)

        def get_open_loop_torque(self):
            """
            Gets open loop torque that is used for this axis.
            This value is stored as OpenLoopCurrent axis parameter.

            
            returns: Open loop current
            """
            return self.parent.get_axis_parameter(self.parent.APs.OpenLoopCurrent)
   
        open_loop_torque = property(get_open_loop_torque,set_open_loop_torque)
    
    def __init__(self):
            self.OpenLoop = self.__GROUPING(self)