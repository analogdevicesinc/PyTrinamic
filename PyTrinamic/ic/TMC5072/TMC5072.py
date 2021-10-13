# Created on: 12.10.2021
# Author: LK

# General imports
from PyTrinamic.ic.TMC_IC import TMC_IC
from PyTrinamic.ic.TMC5072.TMC5072_Registers import TMC5072_Registers
from PyTrinamic.ic.TMC5072.TMC5072_Register_Variants import TMC5072_Register_Variants
from PyTrinamic.ic.TMC5072.TMC5072_Fields import TMC5072_Fields

# Feature imports
from PyTrinamic.features.MotorControlIC import MotorControlIC
from PyTrinamic.features.LinearRampIC import LinearRampIC
from PyTrinamic.features.CurrentIC import CurrentIC
from PyTrinamic.features.StallGuard2IC import StallGuard2IC

class TMC5072(TMC_IC):
    "TMC5130 IC implementation"
    # Constant registers, variants, fields
    REGISTERS = TMC5072_Registers
    VARIANTS = TMC5072_Register_Variants
    FIELDS = TMC5072_Fields

    def __init__(self, handler, channel):
        """
        Constructor for the TMC_IC instance.

        Parameters:
        handler: Handler object for register access operations.
        This object is expected to implement write_register and read_register functions
        to read/write registers via platform-specific communication.
        channel: Channel identifier for this IC. This will be handed to the
        write_register and read_register functions of the handler to differentiate
        between multiple ICs.
        """
        super().__init__(handler, channel)
        self.MOTORS = [ self.MOTOR(self, 0), self.MOTOR(self, 1) ]

    def write_axis_field(self, axis, field, value):
        """
        Writes the given value to the axis-dependend register field.
        On multi-axis ICs, this wraps the process of resolving the actual target
        register field to be used for the given axis, when multiple fields with
        same meaning for different axes are available.

        Parameters:
        axis: Axis index.
        field: Base register field for any axis.
        value: Value to write to the target register field for this axis.
        """
        return self.write_register_field(field[axis] if type(field) == list else field, value)

    def read_axis_field(self, axis, field):
        """
        Reads the value of the axis-dependend register field.
        On multi-axis ICs, this wraps the process of resolving the actual target
        register field to be used for the given axis, when multiple fields with
        same meaning for different axes are available.

        Parameters:
        axis: Axis index.
        field: Base register field for any axis.

        Returns: Value of the target register field for the given axis.
        """
        return self.read_register_field(field[axis] if type(field) == list else field)

    def showChipInfo(self):
        print("TMC5130 chip info: The TMC5130/A is a high-performance stepper motor controller and driver IC with serial communication interfaces. Voltage supply: 4,75 - 46V")

    # Motion Control functions
    def rotate(self, axis, value):
        """
        Rotates the motor on the given axis with the given velocity.

        Parameters:
        axis: Axis index.
        velocity: Target velocity to rotate the motor with. Units are IC specific.

        Returns: None
        """
        self.write_axis_field(axis, self.FIELDS.AMAX, 1000)

        if value >= 0:
            self.write_axis_field(axis, self.FIELDS.VMAX, value)
            self.write_axis_field(axis, self.FIELDS.RAMPMODE, 1)
        else:
            self.write_axis_field(axis, self.FIELDS.VMAX, -value)
            self.write_axis_field(axis, self.FIELDS.RAMPMODE, 2)

    def stop(self, axis):
        """
        Stops the motor on the given axis.

        Parameters:
        axis: Axis index.

        Returns: None
        """
        self.rotate(axis, 0)

    def move_to(self, axis, position, velocity):
        """
        Moves the motor on the given axis to the given target position.

        Parameters:
        axis: Axis index.
        position: Target position to move the motor to. Units are IC specific.
        velocity: Maximum position velocity to position the motor. Units are IC specific.
        If no velocity is given, the previously configured maximum positioning velocity (VMAX register)
        will be used.

        Returns: None
        """
        self.write_axis_field(axis, self.FIELDS.RAMPMODE, 0)

        if velocity != 0:
            self.write_axis_field(axis, self.FIELDS.VMAX, velocity)

        self.write_axis_field(axis, self.FIELDS.XTARGET, position)

    def move_by(self, axis, distance, velocity):
        """
        Moves the motor on the given axis by the given distance.

        Parameters:
        axis: Axis index.
        distance: Position difference to move the motor by. Units are IC specific.
        velocity: Maximum position velocity to position the motor. Units are IC specific.
        If no velocity is given, the previously configured maximum positioning velocity (VMAX register)
        will be used.

        Returns: None
        """
        position = self.read_axis_field(axis, self.FIELDS.XACTUAL)

        self.move_to(motor, position + distance, velocity)

        return position + distance

    class MOTOR(TMC_IC.Motor, LinearRampIC, CurrentIC, StallGuard2IC, MotorControlIC):
        "Motor class for the generic motor."

        def __init__(self, ic, axis):
            TMC_IC.Motor.__init__(self, ic, axis)
            LinearRampIC.__init__(self)
            CurrentIC.__init__(self)
            StallGuard2IC.__init__(self)
