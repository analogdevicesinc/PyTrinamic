from ..features.motor_control import MotorControl
from ..helpers import TMC_helpers


class MotorControlIc(MotorControl):

    def __init__(self, eval_board, ic, axis):
        super().__init__(eval_board, axis)
        self._ic = ic

    def move_to(self, position, velocity=None):
        """
        Moves the motor to the given target position.

        Parameters:
        position: Target position to move the motor to. Units are IC specific.
        velocity: Maximum position velocity to position the motor. Units are IC specific.
        If no velocity is given, the previously configured maximum positioning velocity (VMAX register)
        will be used.

        Returns: None
        """
        self.write_axis_field(self._ic.FIELD.RAMPMODE, 0)

        if velocity and velocity != 0:
            self.write_axis_field(self._ic.FIELD.VMAX, velocity)

        self.write_axis_field(self._ic.FIELD.XTARGET, position)

    def move_by(self, distance, velocity=None):
        """
        Moves the motor by the given distance.

        Parameters:
        distance: Position difference to move the motor by. Units are IC specific.
        velocity: Maximum position velocity to position the motor. Units are IC specific.
        If no velocity is given, the previously configured maximum positioning velocity (VMAX register)
        will be used.

        Returns: None
        """
        self.move_to(self.actual_position + distance, velocity)

    def rotate(self, velocity):
        """
        Rotates the motor with the given velocity.

        Parameters:
        velocity: Target velocity to rotate the motor with. Units are IC specific.

        Returns: None
        """
        # self.write_axis_field(self._ic.FIELD.AMAX, 1000)

        if velocity >= 0:
            self.write_axis_field(self._ic.FIELD.VMAX, velocity)
            self.write_axis_field(self._ic.FIELD.RAMPMODE, 1)
        else:
            self.write_axis_field(self._ic.FIELD.VMAX, -velocity)
            self.write_axis_field(self._ic.FIELD.RAMPMODE, 2)

    def stop(self):
        """
        Stops the motor.

        Parameters:

        Returns: None
        """
        self.rotate(0)

    def set_target_position(self, position):
        """
        Sets the target position of this axis.
        This value is stored in the XTARGET field of the IC.

        Parameters:
        position: Target position.
        """
        self.move_to(position)

    def get_target_position(self):
        """
        Gets the target position of this axis.
        This value is stored in the XTARGET field of the IC.

        Returns: Target position for this axis.
        """
        return self.read_axis_field(self._ic.FIELD.XTARGET, True)

    def set_actual_position(self, position):
        """
        Sets the actual position of this axis.
        This value is stored in the XACTUAL field of the IC.

        Parameters:
        position: Actual position.
        """
        self.write_axis_field(self._ic.FIELD.XACTUAL, position)

    def get_actual_position(self):
        """
        Gets the actual position of this axis.
        This value is stored in the XACTUAL field of the IC.

        Returns: Actual position for this axis.
        """
        return self.read_axis_field(self._ic.FIELD.XACTUAL, True)

    def set_target_velocity(self, velocity):
        """
        Sets the target velocity of this axis.
        This value is stored in the VMAX field of the IC.

        Parameters:
        velocity: Target velocity.
        """
        self.rotate(velocity)

    def get_target_velocity(self):
        """
        Gets the target velocity of this axis.
        This value is stored in the VMAX field of the IC.

        Returns: Target velocity for this axis.
        """
        return self.read_axis_field(self._ic.FIELD.VMAX, True)

    def get_actual_velocity(self):
        """
        Gets the actual velocity of this axis.
        This value is stored in the VACTUAL field of the IC.

        Returns: Actual velocity for this axis.
        """
        return self.read_axis_field(self._ic.FIELD.VACTUAL, True)

    # ic specific functions

    def write_axis_field(self, field, value):
        """
        Writes the given value to the axis-dependent register field.
        On multi-axis ICs, this wraps the process of resolving the actual target
        register field to be used for the given axis, when multiple fields with
        same meaning for different axes are available.

        Parameters:
        field: Base register field for any axis.
        value: Value to write to the target register field for this axis.
        """
        return self._parent.write_register_field(field[self._axis] if type(field) == list else field, value)

    def read_axis_field(self, field, signed=False):
        """
        Reads the value of the axis-dependent register field.
        On multi-axis ICs, this wraps the process of resolving the actual target
        register field to be used for the given axis, when multiple fields with
        same meaning for different axes are available.

        Parameters:
        field: Base register field for any axis.

        Returns: Value of the target register field for the given axis.
        """
        value = self._parent.read_register_field(field[self._axis] if type(field) == list else field)
        return TMC_helpers.to_signed_32(value) if signed else value

    # Properties
    target_position = property(get_target_position, set_target_position)
    actual_position = property(get_actual_position, set_actual_position)
    target_velocity = property(get_target_velocity, set_target_velocity)
    actual_velocity = property(get_actual_velocity)

    def __str__(self):
        return "{} {}".format(
            "MotorControl",
            {
                "motor": self._axis,
                "target_position": self.target_position,
                "actual_position": self.actual_position,
                "target_velocity": self.target_velocity,
                "actual_velocity": self.actual_velocity
            }
        )
