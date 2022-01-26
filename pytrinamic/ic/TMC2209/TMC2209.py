from pytrinamic.ic.TMC2209.TMC2209_register import TMC2209_register
from pytrinamic.ic.TMC2209.TMC2209_fields import TMC2209_fields


class TMC2209:
    """
    The TMC2209 is an ultra-silent motor driver IC for two phase stepper motors. TMC2209 pinning is compatible to a
    number of legacy drivers as well as to the TMC2208. Supply voltage is 4,75 - 29V.
    """
    def __init__(self):
        self.registers = TMC2209_register
        self.fields = TMC2209_fields
