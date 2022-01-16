from PyTrinamic.ic.TMC6100.TMC6100_register import TMC6100_register
from PyTrinamic.ic.TMC6100.TMC6100_fields import TMC6100_fields


class TMC6100:
    """
    The TMC6100 is a high-power gate-driver for PMSM servo or BLDC motors. Supply voltage: 8 - 60V
    """
    def __init__(self):
        self.registers = TMC6100_register
        self.fields = TMC6100_fields
        self.MOTORS = 1
