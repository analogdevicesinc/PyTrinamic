from PyTrinamic.features.Feature import Feature


class DriveSetting(Feature):

    def set_commutation_mode(self, mode):
        """
        Sets commutation mode current that is used for this axis.
        This value is stored as CommutationMode axis parameter.

        Parameters:
        mode: commutation mode
        """
        raise NotImplemented()

    def get_commutation_mode(self):
        """
        Gets commutation mode current that is used for this axis.
        This value is stored in the  CommutationMode axis parameter.

        Returns: commutation mode
        """
        raise NotImplemented()

    def set_motor_type(self, type):
        raise NotImplemented

    def get_motor_type(self):
        raise NotImplemented
    
    def set_pole_pairs(self, pairs):
        raise NotImplemented

    def get_pole_pairs(self):
        raise NotImplemented

    def set_poles(self, poles):
        raise NotImplemented

    def get_poles(self):
        raise NotImplemented

    def set_open_loop_current(self, current):
        """
        Sets  open loop current that is used for this axis.
        This value is stored as OpenLoopCurrent axis parameter.

        Parameters:
        current: open loop current
        """
        raise NotImplemented

    def get_open_loop_current(self):
        """
        Gets open loop current that is used for this axis.
        This value is stored in the  OpenLoopCurrent axis parameter.

        Returns: open loop current
        """
        raise NotImplemented
    
    def get_max_current(self):
        """
        Gets motor maximum current that is used for this axis.
        This value is stored in the  MaxCurrent axis parameter.

        Returns: maximum current
        """
        raise NotImplementedError()

    def set_max_current(self, current):
        """
        Sets motor maximum current that is used for this axis.
        This value is stored as MaxCurrent axis parameter.

        Parameters:
        current: maximum current
        """
        raise NotImplementedError()
    
    def set_position_sensor(self, sensor):
        """
        Sets if position sensor velocity for this axis.
        This value is stored as PositionSensorSelection axis parameter.

        Parameters: 
        sensor: position sensor 
        """
        raise NotADirectoryError()

    def get_position_sensor(self):
        """
        Gets position sensor for this axis.
        This value is stored as PositionSensorSelection axis parameter.

        Returns: position sensor
        """
        raise NotImplementedError()

    def set_velocity_sensor(self, sensor):
        """
        Sets if velocity sensor velocity for this axis.
        This value is stored as VelocitySensorSelection axis parameter.

        Parameters: 
        sensor: velocity sensor 
        """
        raise NotADirectoryError()

    def get_velocity_sensor(self):
        """
        Gets velocity sensor for this axis.
        This value is stored as VelocitySensorSelection axis parameter.

        Returns: velocity sensor
        """
        raise NotImplementedError()

    def set_motor_halted_velocity(self, velocity): 
        """
        Sets motor halted velocity for this axis.
        This value is stored as MotorHaltedVelocity axis parameter.

        Parameters:
        velocity:  motor halted velocity
        """
        raise NotImplementedError()
    
    def get_motor_halted_velocity(self): 
        """
        Gets motor halted velocity for this axis.
        This value is stored as MotorHaltedVelocity axis parameter.

        Returns: motor halted velocity
        """
        raise NotImplementedError()

    def set_target_reached_distance(self, distance): 
        """
        Sets target reached distance for this axis.
        This value is stored as TargetReachedDistance axis parameter.

        Parameters: 
        distance: target reached distance
        """
        raise NotImplementedError()
            
    def get_target_reached_distance(self): 
        """
        Gets target reached distance for this axis.
        This value is stored as TargetReachedDistance axis parameter.

        Returns: target reached distance
        """
        raise NotImplementedError()

    def set_target_reached_velocity(self, velocity): 
        """
        Sets target reached velocity for this axis.
        This value is stored as TargetReachedVelocity axis parameter.

        Parameters:
        velocity:  target reached velocity
        """
        raise NotImplementedError()

    def get_target_reached_velocity(self):
        """
        Gets target reached velocity for this axis.
        This value is stored as TargetReachedVelocity axis parameter.

        Returns: target reached velocity
        """
        raise NotImplementedError()

    def __str__(self):
        return "{} {}".format(
                "DriveSettings",
                {
                    "commutation_mode": self.commutation_mode,
                    "motor_type": self.motor_type,
                    "pole_pairs": self.pole_pairs,
                    "open_loop_current": self.open_loop_current,
                    "max_current": self.max_current,
                    "velocity_sensor": self.velocity_sensor,
                    "position_sensor": self.position_sensor,
                    "target_reached_velocity": self.target_reached_velocity,
                    "target_reached_distance": self.target_reached_distance,
                    "motor_halted_velocity": self.motor_halted_velocity
                }
            )
    
    commutation_mode = property(get_commutation_mode, set_commutation_mode)
    motor_type = property(get_motor_type, set_motor_type)
    pole_pairs = property(get_pole_pairs, set_pole_pairs)
    open_loop_current = property(get_open_loop_current, set_open_loop_current)
    max_current = property(get_max_current, set_max_current)
    velocity_sensor = property(get_velocity_sensor, set_velocity_sensor)
    position_sensor = property(get_position_sensor, set_position_sensor)
    motor_halted_velocity = property(get_motor_halted_velocity, set_motor_halted_velocity)
    target_reached_velocity = property(get_target_reached_velocity, set_target_reached_velocity)
    target_reached_distance = property(get_target_reached_distance, set_target_reached_distance)
