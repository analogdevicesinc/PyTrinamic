'''
Created on 13.07.2021

@author: JH
'''

from PyTrinamic.features.Feature import Feature 

class OpenLoop(Feature):
 
    def set_torque(self, torque):
        """
        Sets if open loop torque that is used for this axis.
        This value is stored as OpenLoopCurrent axis parameter.

        Parameters:
        current: Open Loop Current
        """
        raise NotImplementedError()

    def get_torque(self):
        """
        Gets open loop torque that is used for this axis.
        This value is stored as OpenLoopCurrent axis parameter.

        
        returns: Open loop current
        """
        raise NotImplementedError()

    def __str__(self):
            return "{} {}".format(
                "OpenLoop",
                {
                    "open_loop_torque": self.torque,
                }
            )
    
    torque = property(get_torque,set_torque)
