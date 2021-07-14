'''
Created on 13.07.2021

@author: JH
'''

from PyTrinamic.features.Feature import FeatureProvider
from PyTrinamic.features.CommutationSelection import CommutationSelection

class CommutationSelectionModule(CommutationSelection,FeatureProvider):

    class __GROUPING(CommutationSelection,FeatureProvider):
        def __init__(self, parent):
            self.parent = parent
            
        def set_mode(self, mode):
            self.parent.set_axis_parameter(self.parent.APs.CommutationMode,mode)

        def get_mode(self):
            return self.parent.get_axis_parameter(self.parent.APs.CommutationMode)
    
        mode = property(get_mode,set_mode)

    # Feature initialization
    def __init__(self):
        self.CommutationSelection = self.__GROUPING(self)