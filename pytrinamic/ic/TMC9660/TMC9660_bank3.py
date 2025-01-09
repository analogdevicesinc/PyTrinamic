################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from pytrinamic.modules import Parameter


class Bank3:

    def __init__(self):
        self.TIMER_0_PERIOD                 =  _TIMER_0_PERIOD(               0,   Parameter.Access.RW,  Parameter.Datatype.UNSIGNED)
        self.TIMER_1_PERIOD                 =  _TIMER_1_PERIOD(               1,   Parameter.Access.RW,  Parameter.Datatype.UNSIGNED)
        self.TIMER_2_PERIOD                 =  _TIMER_2_PERIOD(               2,   Parameter.Access.RW,  Parameter.Datatype.UNSIGNED)
        self.STOP_LEFT_TRIGGER_TRANSITION   =  _STOP_LEFT_TRIGGER_TRANSITION( 10,  Parameter.Access.RW,  Parameter.Datatype.ENUM)
        self.STOP_RIGHT_TRIGGER_TRANSITION  =  _STOP_RIGHT_TRIGGER_TRANSITION(11,  Parameter.Access.RW,  Parameter.Datatype.ENUM)
        self.HOME_RIGHT_TRIGGER_TRANSITION  =  _HOME_RIGHT_TRIGGER_TRANSITION(12,  Parameter.Access.RW,  Parameter.Datatype.ENUM)
        self.INPUT_0_TRIGGER_TRANSITION     =  _INPUT_0_TRIGGER_TRANSITION(   13,  Parameter.Access.RW,  Parameter.Datatype.ENUM)
        self.INPUT_1_TRIGGER_TRANSITION     =  _INPUT_1_TRIGGER_TRANSITION(   14,  Parameter.Access.RW,  Parameter.Datatype.ENUM)
        self.INPUT_2_TRIGGER_TRANSITION     =  _INPUT_2_TRIGGER_TRANSITION(   15,  Parameter.Access.RW,  Parameter.Datatype.ENUM)
        self.INPUT_3_TRIGGER_TRANSITION     =  _INPUT_3_TRIGGER_TRANSITION(   16,  Parameter.Access.RW,  Parameter.Datatype.ENUM)
        self.INPUT_4_TRIGGER_TRANSITION     =  _INPUT_4_TRIGGER_TRANSITION(   17,  Parameter.Access.RW,  Parameter.Datatype.ENUM)
        self.INPUT_5_TRIGGER_TRANSITION     =  _INPUT_5_TRIGGER_TRANSITION(   18,  Parameter.Access.RW,  Parameter.Datatype.ENUM)
        self.INPUT_6_TRIGGER_TRANSITION     =  _INPUT_6_TRIGGER_TRANSITION(   19,  Parameter.Access.RW,  Parameter.Datatype.ENUM)
        self.INPUT_7_TRIGGER_TRANSITION     =  _INPUT_7_TRIGGER_TRANSITION(   20,  Parameter.Access.RW,  Parameter.Datatype.ENUM)
        self.INPUT_8_TRIGGER_TRANSITION     =  _INPUT_8_TRIGGER_TRANSITION(   21,  Parameter.Access.RW,  Parameter.Datatype.ENUM)
        self.INPUT_9_TRIGGER_TRANSITION     =  _INPUT_9_TRIGGER_TRANSITION(   22,  Parameter.Access.RW,  Parameter.Datatype.ENUM)
        self.INPUT_10_TRIGGER_TRANSITION    =  _INPUT_10_TRIGGER_TRANSITION(  23,  Parameter.Access.RW,  Parameter.Datatype.ENUM)
        self.INPUT_11_TRIGGER_TRANSITION    =  _INPUT_11_TRIGGER_TRANSITION(  24,  Parameter.Access.RW,  Parameter.Datatype.ENUM)
        self.INPUT_12_TRIGGER_TRANSITION    =  _INPUT_12_TRIGGER_TRANSITION(  25,  Parameter.Access.RW,  Parameter.Datatype.ENUM)
        self.INPUT_13_TRIGGER_TRANSITION    =  _INPUT_13_TRIGGER_TRANSITION(  26,  Parameter.Access.RW,  Parameter.Datatype.ENUM)
        self.INPUT_14_TRIGGER_TRANSITION    =  _INPUT_14_TRIGGER_TRANSITION(  27,  Parameter.Access.RW,  Parameter.Datatype.ENUM)
        self.INPUT_15_TRIGGER_TRANSITION    =  _INPUT_15_TRIGGER_TRANSITION(  28,  Parameter.Access.RW,  Parameter.Datatype.ENUM)
        self.INPUT_16_TRIGGER_TRANSITION    =  _INPUT_16_TRIGGER_TRANSITION(  29,  Parameter.Access.RW,  Parameter.Datatype.ENUM)
        self.INPUT_17_TRIGGER_TRANSITION    =  _INPUT_17_TRIGGER_TRANSITION(  30,  Parameter.Access.RW,  Parameter.Datatype.ENUM)
        self.INPUT_18_TRIGGER_TRANSITION    =  _INPUT_18_TRIGGER_TRANSITION(  31,  Parameter.Access.RW,  Parameter.Datatype.ENUM)


class _TIMER_0_PERIOD(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("TIMER_0_PERIOD", index, access, datatype)


class _TIMER_1_PERIOD(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("TIMER_1_PERIOD", index, access, datatype)


class _TIMER_2_PERIOD(Parameter):

    def __init__(self, index, access, datatype):
        super().__init__("TIMER_2_PERIOD", index, access, datatype)


class _STOP_LEFT_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("STOP_LEFT_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)


class _STOP_RIGHT_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("STOP_RIGHT_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)


class _HOME_RIGHT_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("HOME_RIGHT_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)


class _INPUT_0_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("INPUT_0_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)


class _INPUT_1_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("INPUT_1_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)


class _INPUT_2_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("INPUT_2_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)


class _INPUT_3_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("INPUT_3_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)


class _INPUT_4_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("INPUT_4_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)


class _INPUT_5_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("INPUT_5_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)


class _INPUT_6_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("INPUT_6_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)


class _INPUT_7_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("INPUT_7_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)


class _INPUT_8_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("INPUT_8_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)


class _INPUT_9_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("INPUT_9_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)


class _INPUT_10_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("INPUT_10_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)


class _INPUT_11_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("INPUT_11_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)


class _INPUT_12_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("INPUT_12_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)


class _INPUT_13_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("INPUT_13_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)


class _INPUT_14_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("INPUT_14_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)


class _INPUT_15_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("INPUT_15_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)


class _INPUT_16_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("INPUT_16_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)


class _INPUT_17_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("INPUT_17_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)


class _INPUT_18_TRIGGER_TRANSITION(Parameter):

    class _Choice(Parameter.Choice):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.OFF = Parameter.Option(parent, 0, "OFF")
            self.RISING = Parameter.Option(parent, 1, "RISING")
            self.FALLING = Parameter.Option(parent, 2, "FALLING")
            self.BOTH = Parameter.Option(parent, 3, "BOTH")

    def __init__(self, index, access, datatype):
        super().__init__("INPUT_18_TRIGGER_TRANSITION", index, access, datatype)

        self.choice = self._Choice(self)
