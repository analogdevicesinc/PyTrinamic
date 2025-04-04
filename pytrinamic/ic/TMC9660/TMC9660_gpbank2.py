################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from pytrinamic.modules import ParameterGroup, Parameter


class GpBank2(ParameterGroup):

    def __init__(self):
        super().__init__("GpBank2", ParameterGroup.Category.GLOBAL, 2)
        self.USER_VARIABLE_0   =  _USER_VARIABLE_0( self,  0,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.USER_VARIABLE_1   =  _USER_VARIABLE_1( self,  1,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.USER_VARIABLE_2   =  _USER_VARIABLE_2( self,  2,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.USER_VARIABLE_3   =  _USER_VARIABLE_3( self,  3,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.USER_VARIABLE_4   =  _USER_VARIABLE_4( self,  4,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.USER_VARIABLE_5   =  _USER_VARIABLE_5( self,  5,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.USER_VARIABLE_6   =  _USER_VARIABLE_6( self,  6,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.USER_VARIABLE_7   =  _USER_VARIABLE_7( self,  7,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.USER_VARIABLE_8   =  _USER_VARIABLE_8( self,  8,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.USER_VARIABLE_9   =  _USER_VARIABLE_9( self,  9,   Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.USER_VARIABLE_10  =  _USER_VARIABLE_10(self,  10,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.USER_VARIABLE_11  =  _USER_VARIABLE_11(self,  11,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.USER_VARIABLE_12  =  _USER_VARIABLE_12(self,  12,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.USER_VARIABLE_13  =  _USER_VARIABLE_13(self,  13,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.USER_VARIABLE_14  =  _USER_VARIABLE_14(self,  14,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)
        self.USER_VARIABLE_15  =  _USER_VARIABLE_15(self,  15,  Parameter.Access.RWE,  Parameter.Datatype.SIGNED)


class _USER_VARIABLE_0(Parameter):

    def __init__(self, parent, index, access, datatype):
        super().__init__(parent, "USER_VARIABLE_0", index, access, datatype)


class _USER_VARIABLE_1(Parameter):

    def __init__(self, parent, index, access, datatype):
        super().__init__(parent, "USER_VARIABLE_1", index, access, datatype)


class _USER_VARIABLE_2(Parameter):

    def __init__(self, parent, index, access, datatype):
        super().__init__(parent, "USER_VARIABLE_2", index, access, datatype)


class _USER_VARIABLE_3(Parameter):

    def __init__(self, parent, index, access, datatype):
        super().__init__(parent, "USER_VARIABLE_3", index, access, datatype)


class _USER_VARIABLE_4(Parameter):

    def __init__(self, parent, index, access, datatype):
        super().__init__(parent, "USER_VARIABLE_4", index, access, datatype)


class _USER_VARIABLE_5(Parameter):

    def __init__(self, parent, index, access, datatype):
        super().__init__(parent, "USER_VARIABLE_5", index, access, datatype)


class _USER_VARIABLE_6(Parameter):

    def __init__(self, parent, index, access, datatype):
        super().__init__(parent, "USER_VARIABLE_6", index, access, datatype)


class _USER_VARIABLE_7(Parameter):

    def __init__(self, parent, index, access, datatype):
        super().__init__(parent, "USER_VARIABLE_7", index, access, datatype)


class _USER_VARIABLE_8(Parameter):

    def __init__(self, parent, index, access, datatype):
        super().__init__(parent, "USER_VARIABLE_8", index, access, datatype)


class _USER_VARIABLE_9(Parameter):

    def __init__(self, parent, index, access, datatype):
        super().__init__(parent, "USER_VARIABLE_9", index, access, datatype)


class _USER_VARIABLE_10(Parameter):

    def __init__(self, parent, index, access, datatype):
        super().__init__(parent, "USER_VARIABLE_10", index, access, datatype)


class _USER_VARIABLE_11(Parameter):

    def __init__(self, parent, index, access, datatype):
        super().__init__(parent, "USER_VARIABLE_11", index, access, datatype)


class _USER_VARIABLE_12(Parameter):

    def __init__(self, parent, index, access, datatype):
        super().__init__(parent, "USER_VARIABLE_12", index, access, datatype)


class _USER_VARIABLE_13(Parameter):

    def __init__(self, parent, index, access, datatype):
        super().__init__(parent, "USER_VARIABLE_13", index, access, datatype)


class _USER_VARIABLE_14(Parameter):

    def __init__(self, parent, index, access, datatype):
        super().__init__(parent, "USER_VARIABLE_14", index, access, datatype)


class _USER_VARIABLE_15(Parameter):

    def __init__(self, parent, index, access, datatype):
        super().__init__(parent, "USER_VARIABLE_15", index, access, datatype)
