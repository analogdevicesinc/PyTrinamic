'''
Created on 13.07.2021

@author: JH
'''

from PyTrinamic.features.Feature import Feature

class BLDCMotor(Feature):
 
    def get_type(self):
        """
        Gets motor type that is used for this axis.
        This value is stored in the  MotorType axis parameter.

        Returns: motor type
        """
        raise NotImplementedError()
    def set_type(self, type):
        """
        Sets motor type that is used for this axis.
        This value is stored as MotorType axis parameter.

        Parameters:
        type: motor type
        """
        raise NotImplementedError()

    def get_pole_pairs(self):
        """
        Gets motor pole pairs that is used for this axis.
        This value is stored in the  MotorPolePairs axis parameter.

        Returns: pole pairs
        """
        raise NotImplementedError()
    def set_pole_pairs(self, polePairs):
        """
        Sets motor pole pairs that is used for this axis.
        This value is stored as MotorPolePairs axis parameter.

        Parameters:
        polePairs: pole pairs
        """
        raise NotImplementedError()

    def get_max_torque(self):
        """
        Gets motor maximum torque that is used for this axis.
        This value is stored in the  MaxCurrent axis parameter.

        Returns: motor type
        """
        raise NotImplementedError()
    def set_max_torque(self, torque):
        """
        Sets motor maximum torque that is used for this axis.
        This value is stored as MaxCurrent axis parameter.

        Parameters:
        torque: maximum torque
        """
        raise NotImplementedError()

    def __str__(self):
        return "{} {}".format(
            "Motor configuration",
            {
                "type": self.type,
                "pole_pairs": self.pole_pairs,
                "max_torque": self.max_torque,
            }
        )

    type = property(get_type,set_type)
    pole_pairs = property(get_pole_pairs,set_pole_pairs)
    max_torque = property(get_max_torque,set_max_torque)
    
            