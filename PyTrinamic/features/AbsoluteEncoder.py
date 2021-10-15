'''
Created on 13.07.2021

@author: JH
'''

from PyTrinamic.features.Feature import Feature

class AbsoluteEncoder(Feature):
        
    def set_type(self, type):
        """
        Set absolut encoder type that is used for this axis.
        This value is stored as AbsoluteEncoderType axis parameter.

        Parameters:
        type: Absolute encoder type
        """
        raise NotImplementedError()
    def get_type(self):
        """
        Gets absolut encoder type that is used for this axis.
        This value is stored in the  AbsoluteEncoderType axis parameter.

        Returns: Absolute encoder type
        """
        raise NotImplementedError()

    def set_init(self, init):
        """
        Sets absolute encoder init that is used for this axis.
        This value is stored as AbsoluteEncoderInit axis parameter.

        Parameters:
        inti: absolute encoder init
        """
        raise NotImplementedError()
    def get_init(self):
        """
        Gets absolute encoder init that is used for this axis.
        This value is stored in the  AbsoluteEncoderInit axis parameter.

        Returns: absolute encoder init
        """
        raise NotImplementedError()

    def set_direction(self, dir):
        """
        Sets absolute encoder direction that is used for this axis.
        This value is stored as AbsoluteEncoderDirection axis parameter.

        Parameters:
        dir:  absolute encoder direction 
        """
        raise NotImplementedError()
    def get_direction(self):
        """
        Gets  absolute encoder direction that is used for this axis.
        This value is stored in the  AbsoluteEncoderDirection axis parameter.

        Returns:  absolute encoder direction 
        """
        raise NotImplementedError()

    def set_offset(self, offset):
        """
        Sets absolute encoder offset that is used for this axis.
        This value is stored as AbsoluteEncoderOffset axis parameter.

        Parameters:
        offset: bsolute encoder offset
        """
        raise NotImplementedError()
    def get_offset(self):
        """
        Gets absolute encoder offset that is used for this axis.
        This value is stored in the  AbsoluteEncoderOffset axis parameter.

        Returns: bsolute encoder offset
        """
        raise NotImplementedError()


    def __str__(self):
            return "{} {}".format(
                "SPIEncoder",
                {
                    "type":self.type,
                    "direction": self.direction,
                    "offset":self.offset,
                    "init_mode": self.init_mode,
                }
            )

    type       = property(get_type,set_type)
    init_mode = property(get_init,set_init)
    direction = property(get_direction,set_direction)
    offset = property(get_offset,set_offset)
    