################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
from __future__ import annotations      #start at python 3.7
from typing import Optional, Union
from enum import IntFlag
from abc import ABC, abstractmethod


class TMCIc(object):

    def __init__(self, name, info):
        self.__name = name
        self.__info = info

    def get_name(self):
        return self.__name

    def get_info(self):
        return self.__info


class RegisterApiDevice(ABC):

    def read(self, read_target: Union[Register, Field]) -> int:
        """Generic read function to read a register or a field within a register

        :param read_target: This is the main differentiating argument:
            - If read_target is a Register object, we do a register read.
            - If read_target is a Field object, we do a field read.
        """
        if isinstance(read_target, Field):
            # Our target variable is a Field, we do field read in that case
            register_address = read_target.parent.address
            register_block = read_target.parent.block
            register_content = self.read_register(register_address, register_block)
            return read_target.get(register_content)  # Mask and shift is done in the Field.get function

        elif isinstance(read_target, Register):
            # Our target has the attributes of a register, we do register read in that case
            signed = bool(read_target.signed)
            register_address = read_target.address
            register_block = read_target.block
            return self.read_register(register_address, register_block, signed=signed)

        else:
            # Our target is neither a Register nor a Field.
            raise ValueError(
                f"Argument read_target {read_target} does not appear to be either a Register, or a Field."
            )

    def write(self, write_target: Union[Register, Field, Choice], value: Optional[Union[int, bool]] = None, *, omit_bounds_check=False, omit_permission_checks=False) -> int:
        """Generic write function, to write a register or a field within a register

        :param write_target: This is the main differentiating argument:
            - If write_target is a Choice object, we do a field write.
            - If write_target is a Field object, we do a field write.
            - If write_target is a Register object, we do a register write.
        """
        if isinstance(write_target, Choice) and (value == None):
            # Our target variable is a Choice, we do a choice write in that case
            return self.write(write_target.parent, write_target.value)
        if isinstance(write_target, Field) and isinstance(value, int):
            # Our target variable is a Field, we do field read in that case

            if not omit_permission_checks:
                if not write_target.access.is_writable():
                    raise PermissionError(f"Field {write_target.name} has no write permission!!")

            if not omit_bounds_check:
                if not write_target.is_in_bounds(value):
                    raise ValueError(f"Input value {value} is not in the allowed value range!")

            if write_target.access == Access.RWC:
                register_content_new = (value << write_target.shift) & write_target.mask
                self.write_register(write_target.parent.address, write_target.parent.bloc, register_content_new)
                return register_content_new

            register_address = write_target.parent.address
            register_block = write_target.parent.block
            register_content_old = self.read_register(register_address, register_block)
            register_content_new = write_target.set(register_content_old, value)  # Mask and shift is done in the Field.set function
            self.write_register(register_address, register_block, register_content_new)
            return register_content_new

        elif isinstance(write_target, Register) and isinstance(value, int):
            # Our target has the attributes of a register, we do register write in that case

            if not omit_permission_checks:
                if not write_target.access.is_writable():
                    raise PermissionError(f"Register {write_target.name} has no write permission!!")

            if not omit_bounds_check:
                if not write_target.is_in_bounds(value):
                    raise ValueError(f"Input value {value} is not in the allowed value range!")

            register_address = write_target.address
            register_block = write_target.block
            return self.write_register(register_address, register_block, value)

        else:
            # Our target is neither a Register nor a Field, nor Choice.
            raise ValueError(
                f"Argument write_target {write_target} does not appear to be either a Register, Field or Choice, or the value is invalid."
            )

    @abstractmethod
    def read_register(self, register_address: int, block: int, signed: bool = False):
        raise NotImplementedError

    @abstractmethod
    def write_register(self, register_address: int, block: int, value: int):
        raise NotImplementedError


class Access(IntFlag):
    R   = 0x01 # read
    W   = 0x02 # write
    RW  = 0x03 # read/write
    D   = 0x13 # read/write, separate functions/values for reading or writing
    RC  = 0x21 # read, flag register (read to clear)
    RWC = 0x23 # read, flag register (write 1 to clear)

    def is_writable(self) -> bool:
        return Access.W in self


class RegisterGroup:
    """
    This base class represents an RegisterGroup, containing a list of registers.
    The registers are added in a derived class as object attributes.
    It also contains convenience functions.
    """
    def __init__(self, name, block) -> None:
        self.name = name
        self.block = block

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
        value = (register_value & self.mask) >> self.shift
        if self.signed:
            base_mask = self.mask >> self.shift
            sign_mask = base_mask & (~base_mask >> 1)
            value = (value ^ sign_mask) - sign_mask
        return value
    
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
    def __init__(self, name, parent, access, address, block, signed=False, width=32) -> None:
        self.name = name
        self.parent = parent
        self.access = access
        self.address = address
        self.block = block
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