'''
Created on 14.10.2019

@author: JM
'''

from PyTrinamic.ic.TMC2130.TMC2130 import TMC2130

class TMC2130_eval(TMC2130):
    """
    This class represents a TMC2130 Evaluation board.

    Communication is done over the TMCL commands writeMC and readMC. An
    implementation without TMCL may still use this class if these two functions
    are provided properly. See __init__ for details on the function
    requirements.
    """
    
    def __init__(self, connection, moduleID=1):
        """
        Parameters:
            connection:
                Type: class
                A class that provides the neccessary functions for communicating
                with a TMC2130. The required functions are
                    connection.writeMC(registerAddress, value, moduleID)
                    connection.readMC(registerAddress, moduleID, signed)
                for writing/reading to registers of the TMC2130.
            moduleID:
                Type: int, optional, default value: 1
                The TMCL module ID of the TMC2130. This ID is used as a
                parameter for the writeMC and readMC functions.
        """
        TMC2130.__init__(self, moduleID)

        self.__connection = connection
        self._MODULE_ID = moduleID
        
        self.APs = _APs

    # Use the motion controller functions for register access
    def writeRegister(self, registerAddress, value, moduleID=None):
        # If the moduleID argument is omitted, use the stored module ID
        if not moduleID:
            moduleID = self._MODULE_ID

        return self.__connection.writeMC(registerAddress, value, moduleID)

    def readRegister(self, registerAddress, moduleID=None, signed=False):
        # If the moduleID argument is omitted, use the stored module ID
        if not moduleID:
            moduleID = self._MODULE_ID

        return self.__connection.readMC(registerAddress, moduleID, signed)

    # Axis parameter access
    def getAxisParameter(self, apType, axis):
        if not(0 <= axis < self.MOTORS):
            raise ValueError("Axis index out of range")
        
        if not apType in self.APs._list:
            raise ValueError("Invalid axis parameter")

        return self.__connection.axisParameter(apType, axis)

    def setAxisParameter(self, apType, axis, value):
        if not(0 <= axis < self.MOTORS):
            raise ValueError("Axis index out of range")

        if not apType in self.APs._list:
            raise ValueError("Invalid axis parameter")

        self.__connection.setAxisParameter(apType, axis, value)

    # Motion Control functions
    def rotate(self, motor, value):
        if not(0 <= motor < self.MOTORS):
            raise ValueError

        self.__connection.rotate(motor, value, moduleID=self._MODULE_ID)
    
    def stop(self, motor):
        self.__connection.stop(motor, moduleID=self._MODULE_ID)
    
    
    def moveTo(self, motor, position, velocity):
        # Set maximum positioning velocity
        self.setAxisParameter(self.APs.MAXIMUM_SPEED, motor, velocity)
        
        self.__connection.move(0, motor, position, moduleID=self._MODULE_ID)

class _APs():
    TARGET_POSITION                           =  0
    ACTUAL_POSITION                           =  1
    TARGET_SPEED                              =  2
    ACTUAL_SPEED                              =  3
    MAXIMUM_SPEED                             =  4
    MAXIMUM_ACCELERATION                      =  5
    MAXIMUM_CURRENT                           =  6
    STANDBY_CURRENT                           =  7
    POSITION_REACHED_FLAG                     =  8
    SPEED_THRESHHOLD_FOR_HIGHSPEED_MODE       = 23
    MINIMUM_SPEED_FOR_SWITCHING_TO_DCSTEP     = 24
    HIGH_SPEED_FULLSTEP_MODE                  = 26
    HIGH_SPEED_CHOPPER_MODE                   = 27
    INTERNAL_RSENSE                           = 28
    MEASURED_SPEED                            = 29
    STEP_DIR_SOURCE                           = 50
    STEP_DIR_FREQUENCY                        = 51
    MICROSTEP_RESOLUTION                      = 140
    CHOPPER_BLANK_TIME                        = 162
    CONSTANT_TOFF_MODE                        = 163
    DISABLE_FAST_DECAY_COMPARATOR             = 164
    CHOPPER_HYSTERESIS_END_FAST_DECAY_TIME    = 165
    CHOPPER_HYSTERESIS_START_SINE_WAVE_OFFSET = 166
    CHOPPER_OFF_TIME                          = 167
    SMART_ENERGY_CURRENT_MINIMUM              = 168
    SMART_ENERGY_CURRENT_DOWN_STEP            = 169
    SMART_ENERGY_HYSTERESIS                   = 170
    SMART_ENERGY_CURRENT_UP_STEP              = 171
    SMART_ENERGY_HYSTERESIS_START             = 172
    STALL_GUARD2_FILTER_ENABLE                = 173
    STALL_GUARD2_THRESHOLD                    = 174
    VSENSE                                    = 179
    SMART_ENERGY_ACTUAL_CURRENT               = 180
    SMART_ENERGY_STALL_VELOCITY               = 181
    SMART_ENERGY_THRESHOLD_SPEED              = 182
    RANDOM_TOFF_MODE                          = 184
    CHOPPER_SYNCHRONIZATION                   = 185
    PWM_TRESHOLD_SPEED                        = 186
    PWM_GRADIENT                              = 187
    PWM_AMPLITUDE                             = 188
    PWM_FREQUENCY                             = 191
    PWM_AUTOSCALE                             = 192
    FREEWHEELING_MODE                         = 204
    LOAD_VALUE                                = 206
    
    _list = (
        TARGET_POSITION                           ,
        ACTUAL_POSITION                           ,
        TARGET_SPEED                              ,
        ACTUAL_SPEED                              ,
        MAXIMUM_SPEED                             ,
        MAXIMUM_ACCELERATION                      ,
        MAXIMUM_CURRENT                           ,
        STANDBY_CURRENT                           ,
        POSITION_REACHED_FLAG                     ,
        SPEED_THRESHHOLD_FOR_HIGHSPEED_MODE       ,
        MINIMUM_SPEED_FOR_SWITCHING_TO_DCSTEP     ,
        HIGH_SPEED_FULLSTEP_MODE                  ,
        HIGH_SPEED_CHOPPER_MODE                   ,
        INTERNAL_RSENSE                           ,
        MEASURED_SPEED                            ,
        STEP_DIR_SOURCE                           ,
        STEP_DIR_FREQUENCY                        ,
        MICROSTEP_RESOLUTION                      ,
        CHOPPER_BLANK_TIME                        ,
        CONSTANT_TOFF_MODE                        ,
        DISABLE_FAST_DECAY_COMPARATOR             ,
        CHOPPER_HYSTERESIS_END_FAST_DECAY_TIME    ,
        CHOPPER_HYSTERESIS_START_SINE_WAVE_OFFSET ,
        CHOPPER_OFF_TIME                          ,
        SMART_ENERGY_CURRENT_MINIMUM              ,
        SMART_ENERGY_CURRENT_DOWN_STEP            ,
        SMART_ENERGY_HYSTERESIS                   ,
        SMART_ENERGY_CURRENT_UP_STEP              ,
        SMART_ENERGY_HYSTERESIS_START             ,
        STALL_GUARD2_FILTER_ENABLE                ,
        STALL_GUARD2_THRESHOLD                    ,
        VSENSE                                    ,
        SMART_ENERGY_ACTUAL_CURRENT               ,
        SMART_ENERGY_STALL_VELOCITY               ,
        SMART_ENERGY_THRESHOLD_SPEED              ,
        RANDOM_TOFF_MODE                          ,
        CHOPPER_SYNCHRONIZATION                   ,
        PWM_TRESHOLD_SPEED                        ,
        PWM_GRADIENT                              ,
        PWM_AMPLITUDE                             ,
        PWM_FREQUENCY                             ,
        PWM_AUTOSCALE                             ,
        FREEWHEELING_MODE                         ,
        LOAD_VALUE                                ,
        )