class TMCIc(object):

    def __init__(self, name, info):
        self.__name = name
        self.__info = info

    def get_name(self):
        return self.__name

    def get_info(self):
        return self.__info

    # Only used for direct UART access without EvalSystem

    # def write_register(self, register_address, value):
    #    raise NotImplementedError()

    # def read_register(self, register_address, signed=False):
    #    raise NotImplementedError()

    # def write_register_field(self, field, value):
    #    raise NotImplementedError()

    # def read_register_field(self, field):
    #    raise NotImplementedError()
