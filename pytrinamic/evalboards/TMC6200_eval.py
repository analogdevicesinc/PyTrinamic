from pytrinamic.ic import TMC6200
from pytrinamic.helpers import TMC_helpers


class TMC6200_eval(TMC6200):
    """
    Use TMC6100-EVAL with Landungsbrücke/Startrampe at DRV spi channel to access the TMC6100.
    """
    def __init__(self, connection, module_id=1):
        self.connection = connection
        TMC6200.__init__(self)

    # use Landungsbrücke/Startrampe with DRV channel for register access

    def write_register(self, register_address, value):
        return self.connection.write_drv(register_address, value)

    def read_register(self, register_address):
        return self.connection.read_drv(register_address)

    def write_register_field(self, field, value):
        return self.write_register(field[0], TMC_helpers.field_set(self.read_register(field[0]),
                                   field[1], field[2], value))

    def read_register_field(self, field):
        return TMC_helpers.field_get(self.read_register(field[0]), field[1], field[2])
