from abc import ABC, abstractmethod


class DriveSetting(ABC):

    def __init__(self, parent, axis):
        self._parent = parent
        self._axis = axis

    @abstractmethod
    def set_commutation_mode(self, mode):
        """
        Sets commutation mode current that is used for this axis.
        This value is stored as CommutationMode axis parameter.

        Parameters:
        mode: commutation mode
        """
        raise NotImplementedError

    @abstractmethod
    def get_commutation_mode(self):
        """
        Gets commutation mode current that is used for this axis.
        This value is stored in the  CommutationMode axis parameter.

        Returns: commutation mode
        """
        raise NotImplementedError

    @abstractmethod
    def set_motor_type(self, motor_type):
        raise NotImplementedError

    @abstractmethod
    def get_motor_type(self):
        raise NotImplementedError

    @abstractmethod
    def set_pole_pairs(self, pairs):
        raise NotImplementedError

    @abstractmethod
    def get_pole_pairs(self):
        raise NotImplementedError

    @abstractmethod
    def set_poles(self, poles):
        raise NotImplementedError

    @abstractmethod
    def get_poles(self):
        raise NotImplementedError

    @abstractmethod
    def set_open_loop_current(self, current):
        """
        Sets  open loop current that is used for this axis.
        This value is stored as OpenLoopCurrent axis parameter.

        Parameters:
        current: open loop current
        """
        raise NotImplementedError

    @abstractmethod
    def get_open_loop_current(self):
        """
        Gets open loop current that is used for this axis.
        This value is stored in the  OpenLoopCurrent axis parameter.

        Returns: open loop current
        """
        raise NotImplementedError

    @abstractmethod
    def set_max_current(self, current):
        """
        Sets motor maximum current that is used for this axis.
        This value is stored as MaxCurrent axis parameter.

        Parameters:
        current: maximum current
        """
        raise NotImplementedError

    @abstractmethod
    def get_max_current(self):
        """
        Gets motor maximum current that is used for this axis.
        This value is stored in the  MaxCurrent axis parameter.

        Returns: maximum current
        """
        raise NotImplementedError

    @abstractmethod
    def set_standby_current(self, current):
        raise NotImplementedError

    @abstractmethod
    def get_standby_current(self):
        raise NotImplementedError

    @abstractmethod
    def set_boost_current(self, current):
        raise NotImplementedError

    @abstractmethod
    def get_boost_current(self):
        raise NotImplementedError

    @abstractmethod
    def set_position_sensor(self, sensor):
        """
        Sets if position sensor velocity for this axis.
        This value is stored as PositionSensorSelection axis parameter.

        Parameters: 
        sensor: position sensor 
        """
        raise NotImplementedError

    @abstractmethod
    def get_position_sensor(self):
        """
        Gets position sensor for this axis.
        This value is stored as PositionSensorSelection axis parameter.

        Returns: position sensor
        """
        raise NotImplementedError

    @abstractmethod
    def set_velocity_sensor(self, sensor):
        """
        Sets if velocity sensor velocity for this axis.
        This value is stored as VelocitySensorSelection axis parameter.

        Parameters: 
        sensor: velocity sensor 
        """
        raise NotImplementedError

    @abstractmethod
    def get_velocity_sensor(self):
        """
        Gets velocity sensor for this axis.
        This value is stored as VelocitySensorSelection axis parameter.

        Returns: velocity sensor
        """
        raise NotImplementedError

    @abstractmethod
    def set_motor_halted_velocity(self, velocity): 
        """
        Sets motor halted velocity for this axis.
        This value is stored as MotorHaltedVelocity axis parameter.

        Parameters:
        velocity:  motor halted velocity
        """
        raise NotImplementedError

    @abstractmethod
    def get_motor_halted_velocity(self): 
        """
        Gets motor halted velocity for this axis.
        This value is stored as MotorHaltedVelocity axis parameter.

        Returns: motor halted velocity
        """
        raise NotImplementedError

    @abstractmethod
    def set_target_reached_distance(self, distance): 
        """
        Sets target reached distance for this axis.
        This value is stored as TargetReachedDistance axis parameter.

        Parameters: 
        distance: target reached distance
        """
        raise NotImplementedError

    @abstractmethod
    def get_target_reached_distance(self): 
        """
        Gets target reached distance for this axis.
        This value is stored as TargetReachedDistance axis parameter.

        Returns: target reached distance
        """
        raise NotImplementedError

    @abstractmethod
    def set_target_reached_velocity(self, velocity): 
        """
        Sets target reached velocity for this axis.
        This value is stored as TargetReachedVelocity axis parameter.

        Parameters:
        velocity:  target reached velocity
        """
        raise NotImplementedError

    @abstractmethod
    def get_target_reached_velocity(self):
        """
        Gets target reached velocity for this axis.
        This value is stored as TargetReachedVelocity axis parameter.

        Returns: target reached velocity
        """
        raise NotImplementedError

    @abstractmethod
    def set_microstep_resolution(self, resolution):
        raise NotImplementedError

    @abstractmethod
    def get_microstep_resolution(self):
        raise NotImplementedError

    @abstractmethod
    def set_reference_switch_tolerance(self, tolerance):
        raise NotImplementedError

    @abstractmethod
    def get_reference_switch_tolerance(self):
        raise NotImplementedError
