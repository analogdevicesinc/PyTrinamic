'''
Created on 13.07.2021

@author: JH
'''

from PyTrinamic.features.Feature import FeatureProvider
from PyTrinamic.features.AbsoluteEncoder import AbsoluteEncoder

class AbsoluteEncoderModule(AbsoluteEncoder,FeatureProvider):
        
    class __GROUPING(AbsoluteEncoder,FeatureProvider):     
        def __init__(self, parent):
            self.parent = parent
                

        def set_type(self, type):
            """
            Set absolut encoder type that is used for this axis.
            This value is stored as AbsoluteEncoderType axis parameter.

            Parameters:
            type: Absolute encoder type
            """
            self.parent.set_axis_parameter(self.parent.APs.AbsoluteEncoderType,type)
        def get_type(self):
            """
            Gets absolut encoder type that is used for this axis.
            This value is stored in the  AbsoluteEncoderType axis parameter.

            Returns: Absolute encoder type
            """
            return self.parent.get_axis_parameter(self.parent.APs.AbsoluteEncoderType)

        def set_init(self, init):
            """
            Sets absolute encoder init that is used for this axis.
            This value is stored as AbsoluteEncoderInit axis parameter.

            Parameters:
            inti: absolute encoder init
            """
            self.parent.set_axis_parameter(self.parent.APs.AbsoluteEncoderInit,init)
        def get_init(self):
            """
            Gets absolute encoder init that is used for this axis.
            This value is stored in the  AbsoluteEncoderInit axis parameter.

            Returns: absolute encoder init
            """
            return self.parent.get_axis_parameter(self.parent.APs.AbsoluteEncoderInit)

        def set_direction(self, dir):
            """
            Sets absolute encoder direction that is used for this axis.
            This value is stored as AbsoluteEncoderDirection axis parameter.

            Parameters:
            dir:  absolute encoder direction 
            """
            self.parent.set_axis_parameter(self.parent.APs.AbsoluteEncoderDirection,dir)
        def get_direction(self):
            """
            Gets  absolute encoder direction that is used for this axis.
            This value is stored in the  AbsoluteEncoderDirection axis parameter.

            Returns:  absolute encoder direction 
            """
            return self.parent.get_axis_parameter(self.parent.APs.AbsoluteEncoderDirection)

        def set_offset(self, offset):
            """
            Sets absolute encoder offset that is used for this axis.
            This value is stored as AbsoluteEncoderOffset axis parameter.

            Parameters:
            offset: bsolute encoder offset
            """
            self.parent.set_axis_parameter(self.parent.APs.AbsoluteEncoderOffset,offset)
        def get_offset(self):
            """
            Gets absolute encoder offset that is used for this axis.
            This value is stored in the  AbsoluteEncoderOffset axis parameter.

            Returns: bsolute encoder offset
            """
            return self.parent.get_axis_parameter(self.parent.APs.AbsoluteEncoderOffset)

        type       = property(get_type,set_type)
        init_mode = property(get_init,set_init)
        direction = property(get_direction,set_direction)
        offset = property(get_offset,set_offset)
    
    
    def __init__(self):
        self.AbsoluteEncoder = self.__GROUPING(self)