'''
Created 01.10.2020

@author: ED
'''

from abc import ABC

class commutation_selection_ap_feature(ABC):
 
    def __init__(self, parent):
        self._motorInterface = parent
            
    def setMode(self, mode):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.CommutationMode, mode)

    def mode(self):
        return self._motorInterface.axisParameter(self._motorInterface.AP.CommutationMode)

    def showConfiguration(self):
        print("Commutation selection:")
        print("\tMode: " + str(self.mode()))
