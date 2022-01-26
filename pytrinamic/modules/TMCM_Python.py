'''
Created on 12.09.2020

@author: LK
'''

class TMCM_Python(object):

    def __init__(self, connection, moduleID=1):
        self.connection = connection
        self.MODULE_ID  = moduleID

        self.MOTORS = 0
        self.__default_motor = 0

    def showChipInfo(self):
        print("The TMCM-Python is the MicroPython TMCL Master/Slave interface.")

    # Global parameter access
    def get_global_parameter(self, gpType, bank):
        return self.connection.get_global_parameter(gpType, bank)

    def set_global_parameter(self, gpType, bank, value):
        self.connection.set_global_parameter(gpType, bank, value)

    class APs:
        pass

    class ENUMs:
        # Version formats
        VERSION_FORMAT_ASCII = 0
        VERSION_FORMAT_BINARY = 1
        VERSION_FORMAT_BUILD = 5
        # Python subscript methods
        SUBSCRIPT_METHOD_EXECUTE = 0
        SUBSCRIPT_METHOD_APPEND = 1
        SUBSCRIPT_METHOD_CLEAR = 2

    class GPs:
        controlHost = 0
        controlModule = 1
        loggingEnabled = 2
