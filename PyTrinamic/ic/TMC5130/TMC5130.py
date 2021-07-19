# Created on: 06.07.2021
# Author: LK

# General imports
from PyTrinamic.ic.TMC_IC import TMC_IC
from PyTrinamic.ic.TMC5130.TMC5130_Registers import TMC5130_Registers
from PyTrinamic.ic.TMC5130.TMC5130_Register_Variants import TMC5130_Register_Variants
from PyTrinamic.ic.TMC5130.TMC5130_Fields import TMC5130_Fields

# Feature imports
from PyTrinamic.features.MotorControlIC import MotorControlIC
from PyTrinamic.features.LinearRampIC import LinearRampIC
from PyTrinamic.features.CurrentIC import CurrentIC
from PyTrinamic.features.StallGuard2IC import StallGuard2IC

class TMC5130(TMC_IC):
    "TMC5130 IC implementation"
    # Constant registers, variants, fields
    REGISTERS = TMC5130_Registers
    VARIANTS = TMC5130_Register_Variants
    FIELDS = TMC5130_Fields

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
        self.MOTORS = [self.MOTOR_0(self, 0)]

    def write_axis_field(self, axis, field, value):
        """
        Writes the given value to the axis-dependend register field.
        On multi-axis ICs, this wraps the process of resolving the actual target
        register field to be used for the given axis, when multiple fields with
        same meaning for different axes are available.
        As this IC is single-axis, this function just wraps the write_register_field function.

        Parameters:
        axis: Axis index. As this IC is single-axis, this can be set to any value.
        field: Base register field for any axis.
        value: Value to write to the target register field for this axis.
        """
        del axis
        return self.write_register_field(field, value)

    def read_axis_field(self, axis, field):
        """
        Reads the value of the axis-dependend register field.
        On multi-axis ICs, this wraps the process of resolving the actual target
        register field to be used for the given axis, when multiple fields with
        same meaning for different axes are available.
        As this IC is single-axis, this function just wraps the read_register_field function.

        Parameters:
        axis: Axis index. As this IC is single-axis, this can be set to any value.
        field: Base register field for any axis.

        Returns: Value of the target register field for the given axis.
        """
        del axis
        return self.read_register_field(field)

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
        self.write_register(self.REGISTERS.AMAX, 1000)

        if value >= 0:
            self.write_register(self.REGISTERS.VMAX, value)
            self.write_register(self.REGISTERS.RAMPMODE, 1)
        else:
            self.write_register(self.REGISTERS.VMAX, -value)
            self.write_register(self.REGISTERS.RAMPMODE, 2)

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
        self.write_register(self.REGISTERS.RAMPMODE, 0)

        if velocity != 0:
            self.write_register(self.REGISTERS.VMAX, velocity)

        self.write_register(self.REGISTERS.XTARGET, position)

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
        position = self.read_register(self.REGISTERS.XACTUAL, signed=True)

        self.move_to(motor, position + distance, velocity)

        return position + distance

    class MOTOR_0(TMC_IC.Motor, LinearRampIC, CurrentIC, StallGuard2IC, MotorControlIC):
        "Motor class for the motor on axis 0."

        def __init__(self, ic, axis):
            TMC_IC.Motor.__init__(self, ic, axis)
            LinearRampIC.__init__(self)
            CurrentIC.__init__(self)
            StallGuard2IC.__init__(self)
