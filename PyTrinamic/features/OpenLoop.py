'''
Created on 13.07.2021

@author: JH
'''

from PyTrinamic.features.Feature import Feature 

class OpenLoop(Feature):
 
    def set_open_loop_torque(self, torque):
        raise NotImplementedError()

    def get_open_loop_torque(self):
        raise NotImplementedError()

    def __str__(self):
            return "{} {}".format(
                "OpenLoop",
                {
                    "open_loop_torque": self.open_loop_torque,

                }
            )
    
    open_loop_torque = property(get_open_loop_torque,set_open_loop_torque)
