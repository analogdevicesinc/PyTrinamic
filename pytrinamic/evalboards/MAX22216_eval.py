from pytrinamic.evalboards import TMCLEval
from pytrinamic.ic import MAX22216
from pytrinamic.helpers import TMC_helpers

class MAX22216_eval(TMCLEval):
    """
    This class represents a MAX22216 Evaluation board.
    """
    def __init__(self, connection, module_id=1):
        """
        Constructor for the MAX22216 evalboard instance.

        Parameters:
        connection: TMCL connection interface instance.
        module_id: Module ID to identify the evalboard module. This is used to differentiate
        between different modules on shared busses. Default is set to 1, different
        values have to be configured with the module first.
        """
        TMCLEval.__init__(self, connection, module_id)
        self.motors = [self._MotorTypeA(self, 0)]
        self.ics = [MAX22216(self)]

    # Use the driver controller functions for register access

    def write_register(self, register_address, value):
        return self._connection.write_mc(register_address, value, self._module_id)

    def read_register(self, register_address, signed=False):
        return self._connection.read_mc(register_address, self._module_id, signed)

    def write_register_field(self, field, value):
        return self.write_register(field[0], TMC_helpers.field_set(self.read_register(field[0]),
                                                                   field[1], field[2], value))

    def read_register_field(self, field):
        return TMC_helpers.field_get(self.read_register(field[0]), field[1], field[2])

    class _MotorTypeA(object):
        """
        Motor class for the generic motor.
        """
        def __init__(self, eval_board, axis):
            pass

        class AP:
            pass
