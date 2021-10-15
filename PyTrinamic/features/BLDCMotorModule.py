'''
Created on 13.07.2021

@author: JH
'''

from PyTrinamic.features.Feature import FeatureProvider
from PyTrinamic.features.BLDCMotor import BLDCMotor

class BLDCMotorModule(BLDCMotor,FeatureProvider):
        
    class __GROUPING(BLDCMotor,FeatureProvider):     
        def __init__(self, parent):
            self.parent = parent
                

        def get_type(self):
            """
            Gets motor type that is used for this axis.
            This value is stored in the  MotorType axis parameter.

            Returns: motor type
            """
            return self.parent.get_axis_parameter(self.parent.APs.MotorType)
        def set_type(self, type):
            """
            Sets motor type that is used for this axis.
            This value is stored as MotorType axis parameter.

            Parameters:
            type: motor type
            """
            self.parent.set_axis_parameter(self.parent.APs.MotorType,type)

        def get_pole_pairs(self):
            """
            Gets motor pole pairs that is used for this axis.
            This value is stored in the  MotorPolePairs axis parameter.

            Returns: pole pairs
            """
            return self.parent.get_axis_parameter(self.parent.APs.MotorPolePairs)
        def set_pole_pairs(self, polePairs):
            """
            Sets motor pole pairs that is used for this axis.
            This value is stored as MotorPolePairs axis parameter.

            Parameters:
            polePairs: pole pairs
            """
            self.parent.set_axis_parameter(self.parent.APs.MotorPolePairs,polePairs)

        def get_max_torque(self):
            """
            Gets motor maximum torque that is used for this axis.
            This value is stored in the  MaxCurrent axis parameter.

            Returns: motor type
            """
            return self.parent.get_axis_parameter(self.parent.APs.MaxCurrent)
        def set_max_torque(self, torque):
            """
            Sets motor maximum torque that is used for this axis.
            This value is stored as MaxCurrent axis parameter.

            Parameters:
            torque: maximum torque
            """
            self.parent.set_axis_parameter(self.parent.APs.MaxCurrent,torque)


        type = property(get_type,set_type)
        pole_pairs = property(get_pole_pairs,set_pole_pairs)
        max_torque = property(get_max_torque,set_max_torque)
    
    
    def __init__(self):
        self.BLDCMotor = self.__GROUPING(self)