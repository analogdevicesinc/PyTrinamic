from abc import ABC, abstractmethod


class AbsoluteEncoder(ABC):

    def __init__(self, parent, axis):
        self._parent = parent
        self._axis = axis

    @abstractmethod
    def set_type(self, encoder_type):
        """
        Set absolut encoder type that is used for this axis.
        This value is stored as AbsoluteEncoderType axis parameter.

        Parameters:
        type: Absolute encoder type
        """
        raise NotImplementedError

    @abstractmethod
    def get_type(self):
        """
        Gets absolut encoder type that is used for this axis.
        This value is stored in the  AbsoluteEncoderType axis parameter.

        Returns: Absolute encoder type
        """
        raise NotImplementedError

    @abstractmethod
    def set_resolution(self, resolution):
        raise NotImplementedError

    @abstractmethod
    def get_resolution(self):
        raise NotImplementedError

    @abstractmethod
    def set_init_mode(self, init_mode):
        """
        Sets absolute encoder init mode that is used for this axis.
        This value is stored as AbsoluteEncoderInit axis parameter.

        Parameters:
        init_mode: absolute encoder init mode
        """
        raise NotImplementedError

    @abstractmethod
    def get_init_mode(self):
        """
        Gets absolute encoder init mode that is used for this axis.
        This value is stored in the  AbsoluteEncoderInit axis parameter.

        Returns: absolute encoder init mode
        """
        raise NotImplementedError

    @abstractmethod
    def set_direction(self, direction):
        """
        Sets absolute encoder direction that is used for this axis.
        This value is stored as AbsoluteEncoderDirection axis parameter.

        Parameters:
        dir:  absolute encoder direction 
        """
        raise NotImplementedError

    @abstractmethod
    def get_direction(self):
        """
        Gets  absolute encoder direction that is used for this axis.
        This value is stored in the  AbsoluteEncoderDirection axis parameter.

        Returns:  absolute encoder direction 
        """
        raise NotImplementedError

    @abstractmethod
    def set_offset(self, offset):
        """
        Sets absolute encoder offset that is used for this axis.
        This value is stored as AbsoluteEncoderOffset axis parameter.

        Parameters:
        offset: absolute encoder offset
        """
        raise NotImplementedError

    @abstractmethod
    def get_offset(self):
        """
        Gets absolute encoder offset that is used for this axis.
        This value is stored in the  AbsoluteEncoderOffset axis parameter.

        Returns: absolute encoder offset
        """
        raise NotImplementedError
