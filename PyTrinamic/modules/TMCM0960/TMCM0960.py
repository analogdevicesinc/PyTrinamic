'''
Created on 12.09.2020

@author: LK
'''

class TMCM0960(object):

    def __init__(self, connection, moduleID=1):
        self.connection = connection
        self.MODULE_ID  = moduleID

        self.MOTORS = 0
        self.__default_motor = 0

    def showChipInfo(self):
        print("The TMCM-Python is the MicroPython TMCL Master/Slave interface.")

    # Global parameter access
    def get_global_parameter(self, gpType, bank):
        return self.connection.globalParameter(gpType, bank)

    def set_global_parameter(self, gpType, bank, value):
        self.connection.setGlobalParameter(gpType, bank, value)

    class APs:
        linear_homing_margin = 0
        linear_homing_hyst = 1
        linear_homing_status = 2
        linear_bound_low_step = 3
        linear_bound_low_actual = 4
        linear_bound_high_step = 5
        linear_bound_high_actual = 6
        linear_position_step = 7
        linear_position_absolute = 8
        linear_position_relative = 9
        linear_position_step_actual = 10
        linear_position_absolute_actual = 11
        linear_position_relative_actual = 12
        linear_velocity_actual = 13
        linear_velocity_position = 14
        linear_velocity_homing = 15
        linear_acceleration_position = 16
        linear_acceleration_homing = 17
        linear_length = 18

    class ENUMs:
        # Version formats
        VERSION_FORMAT_ASCII = 0
        VERSION_FORMAT_BINARY = 1
        VERSION_FORMAT_BUILD = 5
        # Python subscript methods
        SUBSCRIPT_METHOD_EXECUTE = 0
        SUBSCRIPT_METHOD_APPEND = 1
        SUBSCRIPT_METHOD_CLEAR = 2
        # Linear distance methods
        LINEAR_DISTANCE_INIT = 0
        LINEAR_DISTANCE_HOMING_START = 1
        LINEAR_DISTANCE_POSITION_STEP = 2
        LINEAR_DISTANCE_POSITION_ABSOLUTE = 3
        LINEAR_DISTANCE_POSITION_RELATIVE = 4

        HOMING_STATUS_IDLE = 0
        HOMING_STATUS_INIT = 1
        HOMING_STATUS_FIRST = 2
        HOMING_STATUS_SECOND = 3
        HOMING_STATUS_DONE = 4

    class GPs:
        controlHost = 0
        controlModule = 1
        loggingEnabled = 2
