################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
from __future__ import annotations      #start at python 3.7
from typing import Union
from enum import IntEnum

class TMCIc(object):

    def __init__(self, name, info):
        self.__name = name
        self.__info = info

    def get_name(self):
        return self.__name

    def get_info(self):
        return self.__info


class Access(IntEnum):
    R   = 0x01 # read
    W   = 0x02 # write
    RW  = 0x03 # read/write
    D   = 0x13 # read/write, separate functions/values for reading or writing
    RC  = 0x21 # read, flag register (read to clear)
    RWC = 0x23 # read, flag register (write 1 to clear)

    def is_writable(self) -> bool:
        return (self & type(self).W) != 0


class RegisterGroup:
    """
    This base class represents an RegisterGroup, containing a list of registers.
    The registers are added in a derived class as object attributes.
    It also contains convenience functions.
    """
    def __init__(self, name) -> None:
        self.name = name

    def find(self, name: str):
        for register in self.registers():
            if register.name == name:
                return register

    def registers(self) -> list:
        """Returns a list of all the Register attributes."""
        registers = []
        for key in self.__dir__():
            obj = getattr(self, key)
            if isinstance(obj, Register):
                registers.append(obj)
        registers.sort(key=lambda x: x.address)

        return registers


class Field:
    """
    This class implements an instance of a field, that contains mask and shift data for a given register.
    It also contains convenience functions to handle all the bit operations.

    Fields should be instantiated as class-wide attributes for a given register.
    The address is contained only as data used by the RegisterAccess class.

    name: The name of this field.
    parent: The register that contains this field.
    access: The type of access of this field.
    mask: The binary mask without shift of this field.
    shift: The position of the field inside the register.
    signed: If the field is signed or not.
    """

    def __init__(self, name, parent, access, mask, shift, *, signed=False):
        self.name = name
        self.parent = parent
        self.access = access
        self.mask = mask
        self.shift = shift
        self.signed = signed

    def get(self, register_value: int) -> int:
        """Get the field value of a register value.
        
        This comes in handy if you want to read a register just once, and then extract multiple field values.
        """
        if self.signed:
            base_mask = self.mask >> self.shift
            sign_mask = base_mask & (~base_mask >> 1)
            return (register_value ^ sign_mask) - sign_mask
        else:
            return (register_value & self.mask) >> self.shift
    
    def set(self, register_value: int, new_field_value) -> int:
        """Change the field value of a register value.

        This comes in handy if you want to change multiple field values of a register in one write operation.
        """
        return (register_value & ~self.mask) | (new_field_value << self.shift)

    def is_in_bounds(self, value: Union[int, bool]) -> bool:
        """Check if the value is within the bounds of the field."""
        base_mask = self.mask >> self.shift
        if self.signed:
            return -base_mask//2 <= value <= base_mask//2
        else:
            return 0 <= value <= base_mask


class Register:
    """
    Abstract base class for register defined in map folders.

    The main purpose is to give these classes an easy way to set the value of a field for use with the bulk write functionality of the reg module.
    """
    def __init__(self, name, parent, access, address, signed=False, width=32) -> None:
        self.name = name
        self.parent = parent
        self.access = access
        self.address = address
        self.signed = signed
        self.width = width

    def is_in_bounds(self, value: int) -> bool:
        if self.signed:
            return -2**(self.width - 1) <= value <= 2**(self.width - 1) - 1
        else:
            return 0 <= value <= 2**self.width - 1

    def fields(self) -> list:
        """
        Returns a list of all the Field attributes.
        """
        fields = []
        for key in self.__dir__():
            obj = getattr(self, key)
            if isinstance(obj, Field):
                fields.append(obj)
        fields.sort(key=lambda x: x.shift)

        return fields


class Choice:
    def __init__(self, value, parent) -> None:
        self.value = value
        self.parent = parent