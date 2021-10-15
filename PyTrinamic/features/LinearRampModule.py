# Created on: 14.06.2021
# Author: LK

from PyTrinamic.features.Feature import Feature, FeatureProvider
from PyTrinamic.features.LinearRamp import LinearRamp

class LinearRampModule(LinearRamp, FeatureProvider):
    "LinearRamp feature implementation for modules"

    class __GROUPING(LinearRamp, FeatureProvider):

        # Grouping parent handling

        def __init__(self, parent):
            self.parent = parent
            
            self._hasMotorHaltedVelocity = False
            self._hasTargetReachedDistance = False
            self._hasTargetReachedVelocity = False

            if hasattr(parent.APs, "TargetReachedVelocity"):
                self._hasTargetReachedVelocity = True
            if hasattr(parent.APs, "TargetReachedDistance"):
                self._hasTargetReachedDistance = True
            if hasattr(parent.APs, "MotorHaltedVelocity"):
                self._hasMotorHaltedVelocity = True
            
        # Grouped feature functions

        def get_target_position(self):
            """
            Gets the target position of this axis.
            This value is stored as TargetPosition axis parameter.

            Returns: Target position for this axis.
            """
            return self.parent.get_axis_parameter(self.parent.APs.TargetPosition)

        def set_target_position(self, position):
            """
            Sets the target position of this axis.
            This value is stored as TargetPosition axis parameter.

            Parameters:
            position: Target position.
            """
            self.parent.set_axis_parameter(self.parent.APs.TargetPosition, position)

        def get_actual_position(self):
            """
            Gets the actual position of this axis.
            This value is stored as ActualPosition axis parameter.

            Returns: Actual position for this axis.
            """
            return self.parent.get_axis_parameter(self.parent.APs.ActualPosition)

        def set_actual_position(self, position):
            """
            Sets the actual position of this axis.
            This value is stored as ActualPosition axis parameter.

            Parameters:
            position: Actual position.
            """
            self.parent.set_axis_parameter(self.parent.APs.ActualPosition, position)

        def get_target_velocity(self):
            """
            Gets the target velocity of this axis.
            This value is stored as TargetVelocity axis parameter.

            Returns: Target velocity for this axis.
            """
            return self.parent.get_axis_parameter(self.parent.APs.TargetVelocity)

        def set_target_velocity(self, velocity):
            """
            Sets the target velocity of this axis.
            This value is stored as TargetVelocity axis parameter.

            Parameters:
            velocity: Target velocity.
            """
            self.parent.set_axis_parameter(self.parent.APs.TargetVelocity, velocity)

        def get_actual_velocity(self):
            """
            Gets the actual velocity of this axis.
            This value is stored as ActualVelocity axis parameter.

            Returns: Actual velocity for this axis.
            """
            return self.parent.get_axis_parameter(self.parent.APs.ActualVelocity)

        def get_max_velocity(self):
            """
            Gets the maximum positioning velocity of this axis.
            This value is stored as MaxVelocity axis parameter.

            Returns: Maximum positioning velocity for this axis.
            """
            return self.parent.get_axis_parameter(self.parent.APs.MaxVelocity)

        def set_max_velocity(self, velocity):
            """
            Sets the maximum positioning velocity of this axis.
            This value is stored as MaxVelocity axis parameter.

            Parameters:
            velocity: Maximum positioning velocity.
            """
            self.parent.set_axis_parameter(self.parent.APs.MaxVelocity, velocity)

        def get_max_acceleration(self):
            """
            Gets the maximum acceleration of this axis.
            This value is stored as MaxAcceleration axis parameter.

            Returns: Maximum acceleration for this axis.
            """
            return self.parent.get_axis_parameter(self.parent.APs.MaxAcceleration)

        def set_max_acceleration(self, acceleration):
            """
            Sets the maximum acceleration of this axis.
            This value is stored as MaxAcceleration axis parameter.

            Parameters:
            acceleration: Maximum acceleration.
            """
            self.parent.set_axis_parameter(self.parent.APs.MaxAcceleration, acceleration)
        
        def get_max_acceleration(self):
            """
            Gets the maximum acceleration of this axis.
            This value is stored as MaxAcceleration axis parameter.

            Returns: Maximum acceleration for this axis.
            """
            return self.parent.get_axis_parameter(self.parent.APs.MaxAcceleration)

        def set_max_acceleration(self, acceleration):
            """
            Sets the maximum acceleration of this axis.
            This value is stored as MaxAcceleration axis parameter.

            Parameters:
            acceleration: Maximum acceleration.
            """
            self.parent.set_axis_parameter(self.parent.APs.MaxAcceleration, acceleration)

        def set_ramp_enabled(self, enabled):
            """
            Sets if ramp is enabled for this axis.
            This value is stored as EnableRamp axis parameter.

            Parameters:
            enabled: ramp enable
            """
            self.parent.set_axis_parameter(self.parent.APs.EnableRamp, enabled)
        
        def get_ramp_enabled(self):
            """
            Gets if ramp is enabled for this axis.
            This value is stored as EnableRamp axis parameter.

            Returns: ramp enable
            """
            return self.parent.get_axis_parameter(self.parent.APs.EnableRamp)
        
        def set_motor_halted_velocity(self, velocity): 
            """
            Sets if motor halted velocity for this axis.
            This value is stored as MotorHaltedVelocity axis parameter.

            Parameters:
            velocity:  motor halted velocity
            """
            if self._hasMotorHaltedVelocity:
                self.parent.set_axis_parameter(self.parent.APs.MotorHaltedVelocity, velocity)
            else:
                return "Not supported"

             
        def get_motor_halted_velocity(self): 
            """
            Gets if motor halted velocity for this axis.
            This value is stored as MotorHaltedVelocity axis parameter.

            Returns: motor halted velocity
            """
            if self._hasMotorHaltedVelocity:
                return self.parent.get_axis_parameter(self.parent.APs.MotorHaltedVelocity)
            else:
                return "Not supported"

        def set_target_reached_distance(self, distance): 
            """
            Sets if target reached distance for this axis.
            This value is stored as TargetReachedDistance axis parameter.

            Parameters: 
            distance: target reached distance
            """
            if self._hasTargetReachedDistance:
                self.parent.set_axis_parameter(self.parent.APs.TargetReachedDistance, distance)
            else:
                return "Not supported"

             
        def get_target_reached_distance(self): 
            """
            Gets if target reached distance for this axis.
            This value is stored as TargetReachedDistance axis parameter.

            Returns: target reached distance
            """
            if self._hasTargetReachedDistance:
                return self.parent.get_axis_parameter(self.parent.APs.TargetReachedDistance)
            else:
                return "Not supported"

        def set_target_reached_velocity(self, velocity): 
            """
            Sets if target reached velocity for this axis.
            This value is stored as TargetReachedVelocity axis parameter.

            Parameters:
            velocity:  target reached velocity
            """
            if self._hasTargetReachedVelocity:
                self.parent.set_axis_parameter(self.parent.APs.TargetReachedVelocity, velocity)
            else:
                return "Not supported"

             
        def get_target_reached_velocity(self): 
            """
            Gets if target reached velocity for this axis.
            This value is stored as TargetReachedVelocity axis parameter.

            Returns: target reached velocity
            """
            if self._hasTargetReachedVelocity:
                return self.parent.get_axis_parameter(self.parent.APs.TargetReachedVelocity)
            else:
                return "Not supported"



        def __str__(self):
            return "{} {}".format(
                "LinearRamp",
                {
                    "target_position": self.target_position,
                    "actual_position": self.actual_position,
                    "target_velocity": self.target_velocity,
                    "actual_velocity": self.actual_velocity,
                    "max_velocity": self.max_velocity,
                    "max_acceleration": self.max_acceleration,
                    "enable" : self.enabled,
                    "target_reached_velocity" : self.target_reached_velocity,
                    "target_reached_distance" : self.target_reached_distance,
                    "motor_halted_velocity" : self.motor_halted_velocity,
                }
            )

        # Properties
        target_position = property(get_target_position, set_target_position)
        actual_position = property(get_actual_position, set_actual_position)
        target_velocity = property(get_target_velocity, set_target_velocity)
        actual_velocity = property(get_actual_velocity)
        max_velocity = property(get_max_velocity, set_max_velocity)
        max_acceleration = property(get_max_acceleration, set_max_acceleration)
        enabled         = property(get_ramp_enabled, set_ramp_enabled)
        motor_halted_velocity = property(get_motor_halted_velocity, set_motor_halted_velocity)
        target_reached_velocity = property(get_target_reached_velocity, set_target_reached_velocity)
        target_reached_distance = property(get_target_reached_distance, set_target_reached_distance)
    # Feature initialization and aggregation
    def __init__(self):
        self.LinearRamp = self.__GROUPING(self)

    # Motor-global functions

    def get_axis_parameter(self, parameter, signed=False):
        raise NotImplementedError()

    def set_axis_parameter(self, parameter, value):
        raise NotImplementedError()

    def get_target_position(self):
        """
        Gets the target position of this axis.
        This value is stored as TargetPosition axis parameter.

        Returns: Target position for this axis.
        """
        return self.get_axis_parameter(self.APs.TargetPosition)

    def set_target_position(self, position):
        """
        Sets the target position of this axis.
        This value is stored as TargetPosition axis parameter.

        Parameters:
        position: Target position.
        """
        self.set_axis_parameter(self.APs.TargetPosition, position)

    def get_actual_position(self):
        """
        Gets the actual position of this axis.
        This value is stored as ActualPosition axis parameter.

        Returns: Actual position for this axis.
        """
        return self.get_axis_parameter(self.APs.ActualPosition)

    def set_actual_position(self, position):
        """
        Sets the actual position of this axis.
        This value is stored as ActualPosition axis parameter.

        Parameters:
        position: Actual position.
        """
        self.set_axis_parameter(self.APs.ActualPosition, position)

    def get_target_velocity(self):
        """
        Gets the target velocity of this axis.
        This value is stored as TargetVelocity axis parameter.

        Returns: Target velocity for this axis.
        """
        return self.get_axis_parameter(self.APs.TargetVelocity)

    def set_target_velocity(self, velocity):
        """
        Sets the target velocity of this axis.
        This value is stored as TargetVelocity axis parameter.

        Parameters:
        velocity: Target velocity.
        """
        self.set_axis_parameter(self.APs.TargetVelocity, velocity)

    def get_actual_velocity(self):
        """
        Gets the actual velocity of this axis.
        This value is stored as ActualVelocity axis parameter.

        Returns: Actual velocity for this axis.
        """
        return self.get_axis_parameter(self.APs.ActualVelocity)

    def get_max_velocity(self):
        """
        Gets the maximum positioning velocity of this axis.
        This value is stored as MaxVelocity axis parameter.

        Returns: Maximum positioning velocity for this axis.
        """
        return self.get_axis_parameter(self.APs.MaxVelocity)

    def set_max_velocity(self, velocity):
        """
        Sets the maximum positioning velocity of this axis.
        This value is stored as MaxVelocity axis parameter.

        Parameters:
        velocity: Maximum positioning velocity.
        """
        self.set_axis_parameter(self.APs.MaxVelocity, velocity)

    def get_max_acceleration(self):
        """
        Gets the maximum acceleration of this axis.
        This value is stored as MaxAcceleration axis parameter.

        Returns: Maximum acceleration for this axis.
        """
        return self.get_axis_parameter(self.APs.MaxAcceleration)

    def set_max_acceleration(self, acceleration):
        """
        Sets the maximum acceleration of this axis.
        This value is stored as MaxAcceleration axis parameter.

        Parameters:
        acceleration: Maximum acceleration.
        """
        self.set_axis_parameter(self.APs.MaxAcceleration, acceleration)

    # Motor-global properties
    target_position = property(get_target_position, set_target_position)
    actual_position = property(get_actual_position, set_actual_position)
    target_velocity = property(get_target_velocity, set_target_velocity)
    actual_velocity = property(get_actual_velocity)
    max_velocity = property(get_max_velocity, set_max_velocity)
    max_acceleration = property(get_max_acceleration, set_max_acceleration)
