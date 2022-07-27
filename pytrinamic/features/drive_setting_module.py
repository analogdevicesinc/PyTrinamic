from ..features.drive_setting import DriveSetting


class DriveSettingModule(DriveSetting):

    def __init__(self, module, axis, aps):
        super().__init__(module, axis)
        self._aps = aps
        self._hasCommutationMode = False
        self._hasMotorType = False
        self._hasMotorPolePairs = False
        self._hasMotorPoles = False
        self._hasOpenLoopCurrent = False
        self._hasMaxCurrent = False
        self._hasVelocitySensorSelection = False
        self._hasPositionSensorSelection = False
        self._hasMotorHaltedVelocity = False
        self._hasTargetReachedDistance = False
        self._hasTargetReachedVelocity = False
        self._hasMicrostepResolution = False
        self._hasReferenceSwitchTolerance = False
        self._hasStandbyCurrent = False
        self._hasBoostCurrent = False

        if hasattr(self._aps, "CommutationMode"):
            self._hasCommutationMode = True
        if hasattr(self._aps, "MotorType"):
            self._hasMotorType = True
        if hasattr(self._aps, "MotorPolePairs"):
            self._hasMotorPolePairs = True
        if hasattr(self._aps, "MotorPoles"):
            self._hasMotorPoles = True
        if hasattr(self._aps, "OpenLoopCurrent"):
            self._hasOpenLoopCurrent = True
        if hasattr(self._aps, "MaxCurrent"):
            self._hasMaxCurrent = True
        if hasattr(self._aps, "VelocitySensorSelection"):
            self._hasVelocitySensorSelection = True
        if hasattr(self._aps, "PositionSensorSelection"):
            self._hasPositionSensorSelection = True
        if hasattr(self._aps, "TargetReachedVelocity"):
            self._hasTargetReachedVelocity = True
        if hasattr(self._aps, "TargetReachedDistance"):
            self._hasTargetReachedDistance = True
        if hasattr(self._aps, "MotorHaltedVelocity"):
            self._hasMotorHaltedVelocity = True
        if hasattr(self._aps, "MicrostepResolution"):
            self._hasMicrostepResolution = True
        if hasattr(self._aps, "ReferenceSwitchTolerance"):
            self._hasReferenceSwitchTolerance = True
        if hasattr(self._aps, "StandbyCurrent"):
            self._hasStandbyCurrent = True
        if hasattr(self._aps, "BoostCurrent"):
            self._hasBoostCurrent = True

    def set_commutation_mode(self, mode):
        """
        Sets commutation mode that is used for this axis.
        This value is stored as CommutationMode axis parameter.

        Parameters:
        mode: commutation mode
        """
        if self._hasCommutationMode:
            self._parent.set_axis_parameter(self._aps.CommutationMode, self._axis, mode)

    def get_commutation_mode(self):
        """
        Gets commutation mode that is used for this axis.
        This value is stored in the  CommutationMode axis parameter.

        Returns: commutation mode
        """
        if self._hasCommutationMode:
            return self._parent.get_axis_parameter(self._aps.CommutationMode, self._axis)
        else:
            return None

    def set_motor_type(self, motor_type):
        """
        Sets motor type that is used for this axis.
        This value is stored as MotorType axis parameter.

        Parameters:
        type: motor type
        """
        if self._hasMotorType:
            self._parent.set_axis_parameter(self._aps.MotorType, self._axis, motor_type)

    def get_motor_type(self):
        """
        Gets motor type that is used for this axis.
        This value is stored in the  MotorType axis parameter.

        Returns: motor type
        """
        if self._hasMotorType:
            return self._parent.get_axis_parameter(self._aps.MotorType, self._axis)
        else:
            return None

    def set_pole_pairs(self, number):
        """
        Sets pole pairs that is used for this axis.
        This value is stored as MotorPolePairs axis parameter.

        Parameters:
        number:  pole pairs
        """
        if self._hasMotorPolePairs:
            self._parent.set_axis_parameter(self._aps.MotorPolePairs, self._axis, number)

    def get_pole_pairs(self):
        """
        Gets pole pairs that is used for this axis.
        This value is stored in the MotorPolePairs axis parameter.

        Returns: pole pairs
        """
        if self._hasMotorPolePairs:
            return self._parent.get_axis_parameter(self._aps.MotorPolePairs, self._axis)
        else:
            return None

    def set_poles(self, number):
        """
        Sets motor poles that are used for this axis.
        This value is stored as MotorPoles axis parameter.

        Parameters:
        number: poles
        """
        if self._hasMotorPoles:
            self._parent.set_axis_parameter(self._aps.MotorPoles, self._axis, number)

    def get_poles(self):
        """
        Gets motor poles that are used for this axis.
        This value is stored in the MotorPoles axis parameter.

        Returns: poles
        """
        if self._hasMotorPoles:
            return self._parent.get_axis_parameter(self._aps.MotorPoles, self._axis)
        else:
            return None

    def set_open_loop_current(self, current):
        """
        Sets  open loop current that is used for this axis.
        This value is stored as OpenLoopCurrent axis parameter.

        Parameters:
        current: open loop current
        """
        if self._hasOpenLoopCurrent:
            self._parent.set_axis_parameter(self._aps.OpenLoopCurrent, self._axis, current)

    def get_open_loop_current(self):
        """
        Gets open loop current that is used for this axis.
        This value is stored in the  OpenLoopCurrent axis parameter.

        Returns: open loop current
        """
        if self._hasOpenLoopCurrent:
            return self._parent.get_axis_parameter(self._aps.OpenLoopCurrent, self._axis)
        else:
            return None

    def set_max_current(self, current):
        """
        Sets maximum current that is used for this axis.
        This value is stored as MaxCurrent axis parameter.

        Parameters:
        current: maximum current
        """
        if self._hasMaxCurrent:
            self._parent.set_axis_parameter(self._aps.MaxCurrent, self._axis, current)

    def get_max_current(self):
        """
        Gets maximum current that is used for this axis.
        This value is stored in the  MaxCurrent axis parameter.

        Returns: maximum current
        """
        if self._hasMaxCurrent:
            return self._parent.get_axis_parameter(self._aps.MaxCurrent, self._axis)
        else:
            return None

    def set_standby_current(self, current):
        """
        Sets standby current that is used for this axis.
        This value is stored as StandbyCurrent axis parameter.

        Parameters:
        current: standby current
        """
        if self._hasStandbyCurrent:
            self._parent.set_axis_parameter(self._aps.StandbyCurrent, self._axis, current)

    def get_standby_current(self):
        """
        Gets standby current that is used for this axis.
        This value is stored in the StandbyCurrent axis parameter.

        Returns: standby current
        """
        if self._hasMaxCurrent:
            return self._parent.get_axis_parameter(self._aps.StandbyCurrent, self._axis)
        else:
            return None

    def set_boost_current(self, current):
        """
        Sets boost current that is used for this axis.
        This value is stored as BoostCurrent axis parameter.

        Parameters:
        current: boost current
        """
        if self._hasBoostCurrent:
            self._parent.set_axis_parameter(self._aps.BoostCurrent, self._axis, current)

    def get_boost_current(self):
        """
        Gets boost current that is used for this axis.
        This value is stored in the BoostCurrent axis parameter.

        Returns: boost current
        """
        if self._hasBoostCurrent:
            return self._parent.get_axis_parameter(self._aps.BoostCurrent, self._axis)
        else:
            return None

    def set_position_sensor(self, sensor):
        """
        Sets position sensor velocity for this axis.
        This value is stored as PositionSensorSelection axis parameter.

        Parameters:
        sensor: position sensor
        """
        if self._hasPositionSensorSelection:
            self._parent.set_axis_parameter(self._aps.PositionSensorSelection, self._axis, sensor)

    def get_position_sensor(self):
        """
        Gets position sensor for this axis.
        This value is stored as PositionSensorSelection axis parameter.

        Returns: position sensor
        """
        if self._hasPositionSensorSelection:
            return self._parent.get_axis_parameter(self._aps.PositionSensorSelection, self._axis)
        else:
            return None

    def set_velocity_sensor(self, sensor):
        """
        Sets velocity sensor velocity for this axis.
        This value is stored as VelocitySensorSelection axis parameter.

        Parameters:
        sensor: velocity sensor
        """
        if self._hasVelocitySensorSelection:
            self._parent.set_axis_parameter(self._aps.VelocitySensorSelection, self._axis, sensor)

    def get_velocity_sensor(self):
        """
        Gets velocity sensor for this axis.
        This value is stored as VelocitySensorSelection axis parameter.

        Returns: velocity sensor
        """
        if self._hasVelocitySensorSelection:
            return self._parent.get_axis_parameter(self._aps.VelocitySensorSelection, self._axis)
        else:
            return None

    def set_motor_halted_velocity(self, velocity):
        """
        Sets motor halted velocity for this axis.
        This value is stored as MotorHaltedVelocity axis parameter.

        Parameters:
        velocity:  motor halted velocity
        """
        if self._hasMotorHaltedVelocity:
            self._parent.set_axis_parameter(self._aps.MotorHaltedVelocity, self._axis, velocity)

    def get_motor_halted_velocity(self):
        """
        Gets motor halted velocity for this axis.
        This value is stored as MotorHaltedVelocity axis parameter.

        Returns: motor halted velocity
        """
        if self._hasMotorHaltedVelocity:
            return self._parent.get_axis_parameter(self._aps.MotorHaltedVelocity, self._axis)
        else:
            return None

    def set_target_reached_distance(self, distance):
        """
        Sets target reached distance for this axis.
        This value is stored as TargetReachedDistance axis parameter.

        Parameters:
        distance: target reached distance
        """
        if self._hasTargetReachedDistance:
            self._parent.set_axis_parameter(self._aps.TargetReachedDistance, self._axis, distance)

    def get_target_reached_distance(self):
        """
        Gets target reached distance for this axis.
        This value is stored as TargetReachedDistance axis parameter.

        Returns: target reached distance
        """
        if self._hasTargetReachedDistance:
            return self._parent.get_axis_parameter(self._aps.TargetReachedDistance, self._axis)
        else:
            return None

    def set_target_reached_velocity(self, velocity):
        """
        Sets target reached velocity for this axis.
        This value is stored as TargetReachedVelocity axis parameter.

        Parameters:
        velocity:  target reached velocity
        """
        if self._hasTargetReachedVelocity:
            self._parent.set_axis_parameter(self._aps.TargetReachedVelocity, self._axis, velocity)

    def get_target_reached_velocity(self):
        """
        Gets target reached velocity for this axis.
        This value is stored as TargetReachedVelocity axis parameter.

        Returns: target reached velocity
        """
        if self._hasTargetReachedVelocity:
            return self._parent.get_axis_parameter(self._aps.TargetReachedVelocity, self._axis)
        else:
            return None

    def set_microstep_resolution(self, resolution):
        """
        Sets microstep resolution for this axis.
        This value is stored as MicrostepResolution axis parameter.

        Parameters:
        resolution: microstep resolution
        """
        if self._hasMicrostepResolution:
            self._parent.set_axis_parameter(self._aps.MicrostepResolution, self._axis, resolution)

    def get_microstep_resolution(self):
        """
        Gets microstep resolution for this axis.
        This value is stored as MicrostepResolution axis parameter.

        Returns: microstep resolution
        """
        if self._hasMicrostepResolution:
            return self._parent.get_axis_parameter(self._aps.MicrostepResolution, self._axis)
        else:
            return None

    def set_reference_switch_tolerance(self, tolerance):
        """
        Sets reference switch tolerance for this axis.
        This value is stored as ReferenceSwitchTolerance axis parameter.

        Parameters:
        tolerance: reference switch tolerance
        """
        if self._hasReferenceSwitchTolerance:
            self._parent.set_axis_parameter(self._aps.ReferenceSwitchTolerance, self._axis, tolerance)

    def get_reference_switch_tolerance(self):
        """
        Gets reference switch tolerance for this axis.
        This value is stored as TargetReachedVelocity axis parameter.

        Returns: reference switch tolerance
        """
        if self._hasReferenceSwitchTolerance:
            return self._parent.get_axis_parameter(self._aps.ReferenceSwitchTolerance, self._axis)
        else:
            return None

    # Properties
    commutation_mode = property(get_commutation_mode, set_commutation_mode)
    motor_type = property(get_motor_type, set_motor_type)
    pole_pairs = property(get_pole_pairs, set_pole_pairs)
    poles = property(get_poles, set_poles)
    open_loop_current = property(get_open_loop_current, set_open_loop_current)
    max_current = property(get_max_current, set_max_current)
    standby_current = property(get_standby_current, set_standby_current)
    boost_current = property(get_boost_current, set_boost_current)
    position_sensor = property(get_position_sensor, set_position_sensor)
    velocity_sensor = property(get_velocity_sensor, set_velocity_sensor)
    motor_halted_velocity = property(get_motor_halted_velocity, set_motor_halted_velocity)
    target_reached_distance = property(get_target_reached_distance, set_target_reached_distance)
    target_reached_velocity = property(get_target_reached_velocity, set_target_reached_velocity)
    microstep_resolution = property(get_microstep_resolution, set_microstep_resolution)
    reference_switch_tolerance = property(get_reference_switch_tolerance, set_reference_switch_tolerance)

    def __str__(self):
        values = "DriveSettings {"
        if self._hasCommutationMode:
            values += "'commutation_mode': " + str(self.commutation_mode) + ", "

        if self._hasMotorType:
            values += "'motor_type': " + str(self.motor_type) + ", "

        if self._hasMotorPolePairs:
            values += "'pole_pairs': " + str(self.pole_pairs) + ", "

        if self._hasMotorPoles:
            values += "'poles': " + str(self.poles) + ", "

        if self._hasOpenLoopCurrent:
            values += "'open_loop_current': " + str(self.open_loop_current) + ", "

        if self._hasMaxCurrent:
            values += "'max_current': " + str(self.max_current)+", "

        if self._hasStandbyCurrent:
            values += "'standby_current': " + str(self.standby_current) + ", "

        if self._hasBoostCurrent:
            values += "'boost_current': " + str(self.boost_current) + ", "

        if self._hasPositionSensorSelection:
            values += "'position_sensor': " + str(self.position_sensor) + ", "

        if self._hasVelocitySensorSelection:
            values += "'velocity_sensor': " + str(self.velocity_sensor) + ", "

        if self._hasTargetReachedVelocity:
            values += "'target_reached_velocity': " + str(self.target_reached_velocity) + ", "

        if self._hasTargetReachedDistance:
            values += "'target_reached_distance': " + str(self.target_reached_distance) + ", "

        if self._hasMotorHaltedVelocity:
            values += "'motor_halted_velocity': " + str(self.motor_halted_velocity) + ", "

        if self._hasMicrostepResolution:
            values += "'microstep_resolution': " + str(self.microstep_resolution) + ", "

        if self._hasReferenceSwitchTolerance:
            values += "'reference_switch_tolerance': " + str(self.reference_switch_tolerance) + ", "

        values = values[:-2]
        values += "}"
        return values
