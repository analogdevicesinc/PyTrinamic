'''
Created on 01.10.2020

@author: ED
'''

from abc import ABC

class open_loop_ap_feature(ABC):
 
    def __init__(self, parent):
        self._motorInterface = parent

    def setOpenLoopTorque(self, torque):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.StartCurrent, torque)

    def openLoopTorque(self):
        return self._motorInterface.axisParameter(self._motorInterface.AP.StartCurrent)

    def showConfiguration(self):
        print("Open loop configuration:")
        print("\tOpen loop torque: " + str(self.openLoopTorque()))
