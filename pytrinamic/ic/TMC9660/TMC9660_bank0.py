################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from pytrinamic.modules import Parameter


class Bank0:

    def __init__(self):
        self.SERIAL_ADDRESS                           =  _SERIAL_ADDRESS(                         1,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.SERIAL_HOST_ADDRESS                      =  _SERIAL_HOST_ADDRESS(                    2,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.HEARTBEAT_MONITORING_CONFIG              =  _HEARTBEAT_MONITORING_CONFIG(            3,   Parameter.Access.RWE,  Parameter.Datatype.ENUM)
        self.HEARTBEAT_MONITORING_TIMEOUT             =  _HEARTBEAT_MONITORING_TIMEOUT(           4,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.IO_DIRECTION_MASK                        =  _IO_DIRECTION_MASK(                      5,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.IO_INPUT_PULLUP_PULLDOWN_ENABLE_MASK     =  _IO_INPUT_PULLUP_PULLDOWN_ENABLE_MASK(   6,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.IO_INPUT_PULLUP_PULLDOWN_DIRECTION_MASK  =  _IO_INPUT_PULLUP_PULLDOWN_DIRECTION_MASK(7,   Parameter.Access.RWE,  Parameter.Datatype.UNSIGNED)
        self.WAKE_PIN_CONTROL_ENABLE                  =  _WAKE_PIN_CONTROL_ENABLE(                10,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.GO_TO_TIMEOUT_POWER_DOWN_STATE           =  _GO_TO_TIMEOUT_POWER_DOWN_STATE(         11,  Parameter.Access.W,    Parameter.Datatype.ENUM)
        self.STIMULUS_FSM_STATE                       =  _STIMULUS_FSM_STATE(                     25,  Parameter.Access.RW,   Parameter.Datatype.ENUM)
        self.STIMULUS_FREQUENCY_DIVISOR               =  _STIMULUS_FREQUENCY_DIVISOR(             26,  Parameter.Access.RW,   Parameter.Datatype.UNSIGNED)
        self.STIMULUS_CHANNEL_0_TARGET_ADDRESS        =  _STIMULUS_CHANNEL_0_TARGET_ADDRESS(      27,  Parameter.Access.RW,   Parameter.Datatype.UNSIGNED)
        self.STIMULUS_CHANNEL_1_TARGET_ADDRESS        =  _STIMULUS_CHANNEL_1_TARGET_ADDRESS(      28,  Parameter.Access.RW,   Parameter.Datatype.UNSIGNED)
        self.STIMULUS_CHANNEL_0_SCALING_FACTOR        =  _STIMULUS_CHANNEL_0_SCALING_FACTOR(      29,  Parameter.Access.RW,   Parameter.Datatype.UNSIGNED)
        self.STIMULUS_CHANNEL_1_SCALING_FACTOR        =  _STIMULUS_CHANNEL_1_SCALING_FACTOR(      30,  Parameter.Access.RW,   Parameter.Datatype.UNSIGNED)
        self.AUTO_START_ENABLE                        =  _AUTO_START_ENABLE(                      77,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)
        self.CLEAR_USER_VARIABLES                     =  _CLEAR_USER_VARIABLES(                   85,  Parameter.Access.RWE,  Parameter.Datatype.BOOLEAN)


class _SERIAL_ADDRESS(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SERIAL_ADDRESS", index, access, datatype)


class _SERIAL_HOST_ADDRESS(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("SERIAL_HOST_ADDRESS", index, access, datatype)


class _HEARTBEAT_MONITORING_CONFIG(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.DISABLED = Parameter.Option(parent, 0, "DISABLED")
            self.TMCL_UART_INTERFACE = Parameter.Option(parent, 1, "TMCL_UART_INTERFACE")
            self.SPI_INTERFACE = Parameter.Option(parent, 2, "SPI_INTERFACE")
            self.TMCL_UART_AND_SPI_INTERFACE = Parameter.Option(parent, 3, "TMCL_UART_AND_SPI_INTERFACE")

    def __init__(self, index, access, datatype):
        super().__init__("HEARTBEAT_MONITORING_CONFIG", index, access, datatype)

        self.choice = self._Choice(self)


class _HEARTBEAT_MONITORING_TIMEOUT(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("HEARTBEAT_MONITORING_TIMEOUT", index, access, datatype)


class _IO_DIRECTION_MASK(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("IO_DIRECTION_MASK", index, access, datatype)


class _IO_INPUT_PULLUP_PULLDOWN_ENABLE_MASK(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("IO_INPUT_PULLUP_PULLDOWN_ENABLE_MASK", index, access, datatype)


class _IO_INPUT_PULLUP_PULLDOWN_DIRECTION_MASK(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("IO_INPUT_PULLUP_PULLDOWN_DIRECTION_MASK", index, access, datatype)


class _WAKE_PIN_CONTROL_ENABLE(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.DISABLED = Parameter.Option(parent, False, "DISABLED")
            self.ENABLED = Parameter.Option(parent, True, "ENABLED")

    def __init__(self, index, access, datatype):
        super().__init__("WAKE_PIN_CONTROL_ENABLE", index, access, datatype)

        self.choice = self._Choice(self)


class _GO_TO_TIMEOUT_POWER_DOWN_STATE(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.T_250_MILLISEC = Parameter.Option(parent, 0, "T_250_MILLISEC")
            self.T_500_MILLISEC = Parameter.Option(parent, 1, "T_500_MILLISEC")
            self.T_1_SEC = Parameter.Option(parent, 2, "T_1_SEC")
            self.T_2_SEC = Parameter.Option(parent, 3, "T_2_SEC")
            self.T_4_SEC = Parameter.Option(parent, 4, "T_4_SEC")
            self.T_8_SEC = Parameter.Option(parent, 5, "T_8_SEC")
            self.T_16_SEC = Parameter.Option(parent, 6, "T_16_SEC")
            self.T_32_SEC = Parameter.Option(parent, 7, "T_32_SEC")

    def __init__(self, index, access, datatype):
        super().__init__("GO_TO_TIMEOUT_POWER_DOWN_STATE", index, access, datatype)

        self.choice = self._Choice(self)


class _STIMULUS_FSM_STATE(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.IDLE = Parameter.Option(parent, 0, "IDLE")
            self.INITIALIZING = Parameter.Option(parent, 1, "INITIALIZING")
            self.RUNNING = Parameter.Option(parent, 2, "RUNNING")
            self.DONE = Parameter.Option(parent, 3, "DONE")

    def __init__(self, index, access, datatype):
        super().__init__("STIMULUS_FSM_STATE", index, access, datatype)

        self.choice = self._Choice(self)


class _STIMULUS_FREQUENCY_DIVISOR(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("STIMULUS_FREQUENCY_DIVISOR", index, access, datatype)


class _STIMULUS_CHANNEL_0_TARGET_ADDRESS(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("STIMULUS_CHANNEL_0_TARGET_ADDRESS", index, access, datatype)


class _STIMULUS_CHANNEL_1_TARGET_ADDRESS(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("STIMULUS_CHANNEL_1_TARGET_ADDRESS", index, access, datatype)


class _STIMULUS_CHANNEL_0_SCALING_FACTOR(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("STIMULUS_CHANNEL_0_SCALING_FACTOR", index, access, datatype)


class _STIMULUS_CHANNEL_1_SCALING_FACTOR(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("STIMULUS_CHANNEL_1_SCALING_FACTOR", index, access, datatype)


class _AUTO_START_ENABLE(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.DISABLED = Parameter.Option(parent, False, "DISABLED")
            self.ENABLED = Parameter.Option(parent, True, "ENABLED")

    def __init__(self, index, access, datatype):
        super().__init__("AUTO_START_ENABLE", index, access, datatype)

        self.choice = self._Choice(self)


class _CLEAR_USER_VARIABLES(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.TRY_LOAD_FROM_STORAGE = Parameter.Option(parent, False, "TRY_LOAD_FROM_STORAGE")
            self.CLEAR = Parameter.Option(parent, True, "CLEAR")

    def __init__(self, index, access, datatype):
        super().__init__("CLEAR_USER_VARIABLES", index, access, datatype)

        self.choice = self._Choice(self)
