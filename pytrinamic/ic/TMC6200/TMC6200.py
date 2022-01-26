from pytrinamic.ic.TMC6200.TMC6200_register import TMC6200_register
from pytrinamic.ic.TMC6200.TMC6200_fields import TMC6200_fields


class TMC6200:
    """
    The TMC6200 is a high-power gate-driver for PMSM servo or BLDC motors. Supply voltage: 8 - 60V
    """
    def __init__(self):
        self.registers = TMC6200_register
        self.fields = TMC6200_fields
        self.MOTORS = 1
