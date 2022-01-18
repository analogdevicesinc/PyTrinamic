from PyTrinamic.features.feature import Feature


class SRamp(Feature):
    "SRamp feature implementation"

    def get_ramp_type(self):
        """
        Gets if Ramp that is used for this axis.
        This value is stored in the  RampType axis parameter.

        Returns: ramp type 
        """
        raise NotImplementedError()

    def set_ramp_type(self, ramp_type):
        """
        Sets if Ramp that is used for this axis.
        This value is stored as RampType axis parameter.

        Parameters:
        ramp_type: ramp type value 
        """
        raise NotImplementedError()

    def get_bow_1(self):
        """
        Gets the bow 1 value for the S-Ramp of this axis.
        This value is stored as Bow1 axis parameter.

        Returns: Bow 1 value 
        """
        raise NotImplementedError()

    def set_bow_1(self, pps):
        """
        Sets the bow 1 value for the S-Ramp of this axis.
        This value is stored as Bow1 axis parameter.

        Parameters:
        pps: Bow 1 value
        """
        raise NotImplementedError()

    def get_bow_2(self):
        """
        Gets the bow 1 value for the S-Ramp of this axis.
        This value is stored as Bow1 axis parameter.

        Returns: Bow 1 value 
        """
        raise NotImplementedError()

    def set_bow_2(self, pps):
        """
        Sets the bow 2 value for the S-Ramp of this axis.
        This value is stored as Bow2 axis parameter.

        Parameters:
        pps: Bow 2 value
        """
        raise NotImplementedError()

    def get_bow_3(self):
        """
        Gets the bow 3 value for the S-Ramp of this axis.
        This value is stored as Bow3 axis parameter.

        Returns: Bow 3 value 
        """
        raise NotImplementedError()

    def set_bow_3(self, pps):
        """
        Sets the bow 3 value for the S-Ramp of this axis.
        This value is stored as Bow3 axis parameter.

        Parameters:
        pps: Bow 3 value
        """
        raise NotImplementedError()

    def get_bow_4(self):
        """
        Gets the bow 4 value for the S-Ramp of this axis.
        This value is stored as Bow4 axis parameter.

        Returns: Bow 4 value 
        """
        raise NotImplementedError()

    def set_bow_4(self, pps):
        """
        Sets the bow 4 value for the S-Ramp of this axis.
        This value is stored as Bow4 axis parameter.
 
        Parameters:
        pps: Bow 4 value
        """
        raise NotImplementedError()

    def __str__(self):
        return "{} {}".format(
            "S-Ramp:",
            {
                "Use S-Ramp": self.ramp_type,
                "Bow_1": self.bow_1,
                "Bow_2": self.bow_2,
                "Bow_3": self.bow_3,
                "Bow_4": self.bow_4,
            }
        )

    # Properties
    ramp_type = property(get_ramp_type, set_ramp_type)
    bow_1 = property(get_bow_1, set_bow_1)
    bow_2 = property(get_bow_2, set_bow_2)
    bow_3 = property(get_bow_3, set_bow_3)
    bow_4 = property(get_bow_4, set_bow_4)
