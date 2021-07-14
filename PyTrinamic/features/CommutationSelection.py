'''
Created on 13.07.2021

@author: JH
'''

from PyTrinamic.features.Feature import Feature

class CommutationSelection(Feature):

    def set_mode(self, mode):
        raise NotImplementedError()

    def get_mode(self):
        raise NotImplementedError()

    def __str__(self):
            return "{} {}".format(
                "Commutation",
                {
                    "mode": self.mode,

                }
            )
    
    mode = property(get_mode,set_mode)
