from pytrinamic2.ic.TMC5062.TMC5062_register import TMC5062_register
from pytrinamic2.ic.TMC5062.TMC5062_fields import TMC5062_fields, TMC5062_fields_m1, TMC5062_fields_m2


class TMC5062:
    """
    The TMC5062 is a high performance motion controller and driver for up two stepper motors.
    Supply voltage is 4,75-20V.
    """
    def __init__(self):
        self.registers = TMC5062_register
        self.fields = TMC5062_fields
        self.fields = TMC5062_fields_m1
        self.fields = TMC5062_fields_m2
