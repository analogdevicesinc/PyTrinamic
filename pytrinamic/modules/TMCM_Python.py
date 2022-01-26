
class TMCM_Python(object):
    """
    The TMCM-Python is the MicroPython TMCL Master/Slave interface.
    """
    def __init__(self, connection, module_id=1):
        self.connection = connection
        self.MODULE_ID = module_id
        self.MOTORS = 0
        self.__default_motor = 0

    # Global parameter access
    def get_global_parameter(self, gp_type, bank):
        return self.connection.get_global_parameter(gp_type, bank)

    def set_global_parameter(self, gp_type, bank, value):
        self.connection.set_global_parameter(gp_type, bank, value)

    class AP:
        pass

    class ENUM:
        # Version formats
        VERSION_FORMAT_ASCII = 0
        VERSION_FORMAT_BINARY = 1
        VERSION_FORMAT_BUILD = 5
        # Python subscript methods
        SUBSCRIPT_METHOD_EXECUTE = 0
        SUBSCRIPT_METHOD_APPEND = 1
        SUBSCRIPT_METHOD_CLEAR = 2

    class GP:
        controlHost = 0
        controlModule = 1
        loggingEnabled = 2
