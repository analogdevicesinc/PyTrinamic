################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import enum
import inspect
import warnings

from typing import Optional, Union
from abc import ABC, abstractmethod


class TMCLModule(object):

    def __init__(self, connection, module_id=1, ap_index_bit_width=8):
        """
        Constructor for the module instance.

        Parameters:
        connection: TMCL connection interface object.
        module_id: Module ID to identify the module. This is used to differentiate
        between different modules on shared busses. Default is set to 1, different
        values have to be configured with the module first.
        """
        self.connection = connection
        self.module_id = module_id
        self.ap_index_bit_width = ap_index_bit_width
        self.name = ""
        self.desc = ""
        self.motors = []

    def list_features(self):
        """
        Lists all compatible feature classes for all axes of this module.

        Returns: Unified list of features of all axes.
        """
        features = list()
        for motor in self.motors:
            features.append(motor.list_features())
        return features

    def __str__(self):
        features = ""
        # for feature in self.list_features():
        #    features += str(feature) + ", "
        # features = features[1:]
        # features = features[:-3]
        return "{} {}".format(
                self.name,
                {
                    "module_id": self.module_id,
                    "features": features
                }
        )

    def set_axis_parameter(self, ap_type, axis, value):
        """
        Sets the axis parameter for the given axis of this module identified by type to the given value.

        Parameters:
        type: Axis parameter type. These can be retrieved from the APs class of the corresponding axis.
        axis: Axis index for the parameter to be set.
        value: Value to set the axis parameter to.
        """
        self.connection.set_axis_parameter(ap_type, axis, value, self.module_id, self.ap_index_bit_width)

    def get_axis_parameter(self, ap_type, axis, signed=False):
        """
        Gets the axis parameter for the given axis of this module identified by type.

        Parameters:
        type: Axis parameter type. These can be retrieved from the APs class of this axis.
        axis: Axis index for the parameter to get from.
        signed: Indicates whether the value should be interpreted as signed or not.
        By default, this is False, so the value will be interpreted as unsigned.

        Returns: Axis parameter value.
        """
        return self.connection.get_axis_parameter(ap_type, axis, self.module_id, signed, self.ap_index_bit_width)

    def set_global_parameter(self, gp_type, bank, value):
        """
        Sets the global parameter on this module identified by type to the given value.

        Parameters:
        type: Global parameter type. These can be retrieved from the GPs class of this module.
        bank: Bank number for the parameter to be set.
        value: Value to set the global parameter to.
        """
        self.connection.set_global_parameter(gp_type, bank, value, self.module_id)

    def get_global_parameter(self, gp_type, bank, signed=False):
        """
        Gets the global parameter on this module identified by type.

        Parameters:
        type: Global parameter type. These can be retrieved from the GPs class of this module.
        bank: Bank number for the parameter to be set.
        signed: Indicates whether the value should be interpreted as signed or not.
        By default, this is False, so the value will be interpreted as unsigned.

        Returns: Global parameter value.
        """
        return self.connection.get_global_parameter(gp_type, bank, self.module_id, signed)

    def get_analog_input(self, x):
        """
        Gets the analog input value identified by index x.

        Parameters:
        x: Analog input index.

        Returns: Analog input value.
        """
        return self.connection.get_analog_input(x, self.module_id)

    def get_digital_input(self, x):
        """
        Gets the digital input value identified by index x.

        Parameters:
        x: Digital input index.

        Returns: Digital input value.
        """
        return self.connection.get_digital_input(x, self.module_id)

    def get_digital_output(self, x):
        """
        Gets the digital output value identified by index x.

        Parameters:
        x: Digital output index.

        Returns: Digital output value.
        """
        return self.connection.get_digital_output(x, self.module_id)

    " write outputs "
    def set_digital_output(self, x):
        """
        Sets the digital output value identified by index x.

        Parameters:
        x: Digital output index.
        """
        return self.connection.set_digital_output(x, self.module_id)

    def clear_digital_output(self, x):
        """
        Clears the digital output identified by index x.

        Parameters:
        x: Digital output index.
        """
        return self.connection.clear_digital_output(x, self.module_id)


class ParameterGroup:
    class Category(enum.IntEnum):
        AXIS = enum.auto()
        GLOBAL = enum.auto()

    def __init__(self, name, category, block) -> None:
        self.name = name
        self.category = category
        self.block = block


class Parameter:

    class Access(enum.IntEnum):
        R   = 0x01
        W   = 0x02
        RW  = 0x03
        RWE = 0x07
        
    class Datatype(enum.IntEnum):
        BOOLEAN = enum.auto()
        UNSIGNED = enum.auto()
        SIGNED = enum.auto()
        ENUM = enum.auto()
        FIELD = enum.auto()

    class Choice:
        def __init__(self, parent: "Parameter"):
            self.parent = parent

        def options(self):
            return [member for name, member in inspect.getmembers(self) if isinstance(member, Parameter.Option)]

        def get(self, parameter_value):
            """Extracts the choice value from a parameter value."""
            try:
                return next(option for option in self.options() if option.value == parameter_value)
            except StopIteration:
                raise IndexError(f"Unknown value {parameter_value} for choice parameter {self.parent.name}!")

    class Option:
        def __init__(self, parent: "Parameter", value: int, name: str):
            self.parent = parent
            self.value = value
            self.name = name

    class Field:
        def __init__(self, parent: "Parameter", name: str, mask: int, shift: int):
            self.parent = parent
            self.name = name
            self.mask = mask
            self.shift = shift

        def get(self, parameter_value: int):
            """Extracts the field value from a parameter value."""
            return (parameter_value & self.mask) >> self.shift
        
        def set(self, parameter_value: int, new_field_value: int):
            """Sets the field value in a parameter value."""
            return (parameter_value & ~self.mask) | ((new_field_value << self.shift) & self.mask)

    def __init__(self, parent: ParameterGroup, name: str, index: int, access: "Parameter.Access", datatype: "Parameter.Datatype"):
        self.parent = parent
        self.name = name
        self.index = index
        self.access = access
        self.datatype = datatype

    def __int__(self):
        return self.index
    
    @property
    def block(self):
        return self.parent.block
    
    @property
    def category(self):
        return self.parent.category
    

class ParameterApiDevice(ABC):

    def get_parameter(self, get_target: Union[Parameter]):
        if isinstance(get_target, Parameter):
            parameter = get_target
        else:
            raise ValueError("get_target must be a Parameter!")
        signed = True if parameter.datatype == Parameter.Datatype.SIGNED else False
        if parameter.category == ParameterGroup.Category.AXIS:
            value = self._get_axis_parameter(
                parameter.index,
                signed=signed,
            )
        elif parameter.category == ParameterGroup.Category.GLOBAL:
            value = self._get_global_parameter(
                parameter.index,
                parameter.block,
                signed=signed,
            )
        else:
            raise ValueError("Unsupported parameter type.")
        return value

    def set_parameter(self, set_target: Union[Parameter, Parameter.Option], value: Optional[Union[int, bool]] = None):
        if isinstance(set_target, Parameter):
            parameter = set_target
            if value is None:
                raise ValueError("Value must be provided when setting a parameter.")
        elif isinstance(set_target, Parameter.Option):
            parameter =  set_target.parent
            if value is not None:
                warnings.warn("Value is ignored when setting a choice parameter.")
            value = set_target.value
        else:
            raise ValueError("set_target must be a Parameter or Parameter.Option object.")
        if parameter.category == ParameterGroup.Category.AXIS:
            return self._set_axis_parameter(
                parameter.index,
                value,
            )
        elif parameter.category == ParameterGroup.Category.GLOBAL:
            return self._set_global_parameter(
                parameter.index,
                bank=parameter.block,
                value=value,
            )
        else:
            raise ValueError("Unsupported parameter type.")
    
    @abstractmethod
    def _get_axis_parameter(self, index: int, signed: bool):
        raise NotImplementedError

    @abstractmethod
    def _set_axis_parameter(self, index: int, value: int):
        raise NotImplementedError
    
    @abstractmethod
    def _get_global_parameter(self, index: int, bank: int, signed: bool):
        raise NotImplementedError

    @abstractmethod
    def _set_global_parameter(self, index: int, bank: int, value: int):
        raise NotImplementedError
