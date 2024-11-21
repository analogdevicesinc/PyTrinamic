################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from pytrinamic.modules import Parameter


class Bank0:

    def __init__(self):
        self.SERIAL_ADDRESS                           =  _SERIAL_ADDRESS(                           1,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.SERIAL_HOST_ADDRESS                      =  _SERIAL_HOST_ADDRESS(                      2,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.HEARTBEAT_MONITORING_CONFIG              =  _HEARTBEAT_MONITORING_CONFIG(              3,   Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.HEARTBEAT_MONITORING_TIMEOUT             =  _HEARTBEAT_MONITORING_TIMEOUT(             4,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.IO_DIRECTION_MASK                        =  _IO_DIRECTION_MASK(                        5,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.IO_INPUT_PULLUP_PULLDOWN_ENABLE_MASK     =  _IO_INPUT_PULLUP_PULLDOWN_ENABLE_MASK(     6,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.IO_INPUT_PULLUP_PULLDOWN_DIRECTION_MASK  =  _IO_INPUT_PULLUP_PULLDOWN_DIRECTION_MASK(  7,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.WAKE_PIN_CONTROL_ENABLE                  =  _WAKE_PIN_CONTROL_ENABLE(                  10,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.GO_TO_TIMEOUT_POWER_DOWN_STATE           =  _GO_TO_TIMEOUT_POWER_DOWN_STATE(           11,  Parameter.Access.W,    Parameter.Datatype.ENUM)
        self.STIMULUS_FSM_STATE                       =  _STIMULUS_FSM_STATE(                       25,  Parameter.Access.RW,   Parameter.Datatype.ENUM)
        self.STIMULUS_FREQUENCY_DIVISOR               =  _STIMULUS_FREQUENCY_DIVISOR(               26,  Parameter.Access.RW,   Parameter.Datatype.UNSIGNED)
        self.STIMULUS_CHANNEL_0_TARGET_ADDRESS        =  _STIMULUS_CHANNEL_0_TARGET_ADDRESS(        27,  Parameter.Access.RW,   Parameter.Datatype.UNSIGNED)
        self.STIMULUS_CHANNEL_1_TARGET_ADDRESS        =  _STIMULUS_CHANNEL_1_TARGET_ADDRESS(        28,  Parameter.Access.RW,   Parameter.Datatype.UNSIGNED)
        self.STIMULUS_CHANNEL_0_SCALING_FACTOR        =  _STIMULUS_CHANNEL_0_SCALING_FACTOR(        29,  Parameter.Access.RW,   Parameter.Datatype.UNSIGNED)
        self.STIMULUS_CHANNEL_1_SCALING_FACTOR        =  _STIMULUS_CHANNEL_1_SCALING_FACTOR(        30,  Parameter.Access.RW,   Parameter.Datatype.UNSIGNED)
        self.AUTO_START_ENABLE                        =  _AUTO_START_ENABLE(                        77,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.CLEAR_USER_VARIABLES                     =  _CLEAR_USER_VARIABLES(                     85,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)


class _SERIAL_ADDRESS(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SERIAL_ADDRESS", index, access, datatype)

        self.choice = None


class _SERIAL_HOST_ADDRESS(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SERIAL_HOST_ADDRESS", index, access, datatype)

        self.choice = None


class _HEARTBEAT_MONITORING_CONFIG(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = 0
            self.TMCL_UART_INTERFACE = 1
            self.SPI_INTERFACE = 2
            self.TMCL_UART_AND_SPI_INTERFACE = 3

    def __init__(self, index, access, datatype):
        super().__init__("HEARTBEAT_MONITORING_CONFIG", index, access, datatype)

        self.choice = self._Choices()


class _HEARTBEAT_MONITORING_TIMEOUT(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("HEARTBEAT_MONITORING_TIMEOUT", index, access, datatype)

        self.choice = None


class _IO_DIRECTION_MASK(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("IO_DIRECTION_MASK", index, access, datatype)

        self.choice = None


class _IO_INPUT_PULLUP_PULLDOWN_ENABLE_MASK(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("IO_INPUT_PULLUP_PULLDOWN_ENABLE_MASK", index, access, datatype)

        self.choice = None


class _IO_INPUT_PULLUP_PULLDOWN_DIRECTION_MASK(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("IO_INPUT_PULLUP_PULLDOWN_DIRECTION_MASK", index, access, datatype)

        self.choice = None


class _WAKE_PIN_CONTROL_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("WAKE_PIN_CONTROL_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _GO_TO_TIMEOUT_POWER_DOWN_STATE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.T_250_MILLISEC = 0
            self.T_500_MILLISEC = 1
            self.T_1_SEC = 2
            self.T_2_SEC = 3
            self.T_4_SEC = 4
            self.T_8_SEC = 5
            self.T_16_SEC = 6
            self.T_32_SEC = 7

    def __init__(self, index, access, datatype):
        super().__init__("GO_TO_TIMEOUT_POWER_DOWN_STATE", index, access, datatype)

        self.choice = self._Choices()


class _STIMULUS_FSM_STATE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.IDLE = 0
            self.INITIALIZING = 1
            self.RUNNING = 2
            self.DONE = 3

    def __init__(self, index, access, datatype):
        super().__init__("STIMULUS_FSM_STATE", index, access, datatype)

        self.choice = self._Choices()


class _STIMULUS_FREQUENCY_DIVISOR(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("STIMULUS_FREQUENCY_DIVISOR", index, access, datatype)

        self.choice = None


class _STIMULUS_CHANNEL_0_TARGET_ADDRESS(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("STIMULUS_CHANNEL_0_TARGET_ADDRESS", index, access, datatype)

        self.choice = None


class _STIMULUS_CHANNEL_1_TARGET_ADDRESS(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("STIMULUS_CHANNEL_1_TARGET_ADDRESS", index, access, datatype)

        self.choice = None


class _STIMULUS_CHANNEL_0_SCALING_FACTOR(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("STIMULUS_CHANNEL_0_SCALING_FACTOR", index, access, datatype)

        self.choice = None


class _STIMULUS_CHANNEL_1_SCALING_FACTOR(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("STIMULUS_CHANNEL_1_SCALING_FACTOR", index, access, datatype)

        self.choice = None


class _AUTO_START_ENABLE(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.DISABLED = False
            self.ENABLED = True

    def __init__(self, index, access, datatype):
        super().__init__("AUTO_START_ENABLE", index, access, datatype)

        self.choice = self._Choices()


class _CLEAR_USER_VARIABLES(Parameter):

    class _Choices:
        def __init__(self) -> None:
            self.TRY_LOAD_FROM_STORAGE = False
            self.CLEAR = True

    def __init__(self, index, access, datatype):
        super().__init__("CLEAR_USER_VARIABLES", index, access, datatype)

        self.choice = self._Choices()

