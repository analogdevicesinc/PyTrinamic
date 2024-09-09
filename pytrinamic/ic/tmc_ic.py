################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
from __future__ import annotations      #start at python 3.7
import typing
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
        segments = name.split(".")

        if len(segments) == 0:
            raise ValueError("Invalid name")

        if segments[0] != self._NAME:
            raise ValueError("Invalid name: RegisterGroup name doesn't match")

        if len(segments) == 1:
            return self

        #We have for some register lists of the register. It iterates throug them and looks for a match and return the match.
        if segments[1].find("[") != -1:
            found = False
            register = None
            for key in self.__dir__():
                if found: break
                obj = getattr(self, key)
                if isinstance(obj, list):
                    if all([isinstance(x, Register) for x in obj]):
                        i =0
                        for key in obj:
                            if obj[i].get_name() == segments[0]+"."+segments[1]:
                                register =obj[i]
                                found = True
                                break
                            i +=1

        else:
            # We have at least two segments -> search for the register
            register = getattr(self, segments[1], None)

        if not register :
            raise ValueError(f"Invalid name: Register {segments[1]} not found in {self._NAME}")

        if len(segments) == 2:
            return register

        # We have at least three segments -> search for field in register
        field = getattr(register, segments[2])
        if not field:
            raise ValueError(f"Invalid name '{name}': Field {segments[2]} not found in register {register.get_name()}")

        return field

    def get_registers(self) -> list:
        """
        Returns a list of all the Register members of this AddressBlock object
        """
        regs = []
        for key in self.__dir__():

            obj = getattr(self, key)
            if isinstance(obj, Register):
                regs.append(obj)
            if isinstance(obj, list):
                if all([isinstance(x, Register) for x in obj]):
                    regs += obj
        regs.sort(key=lambda x: x._ADDRESS)

        return regs


class Field:
    """
    This class implements an instance of a field, that contains mask and shift data for a given register.
    It also contains convenience functions to handle all the bit operations.

    Fields should be instantiated as class-wide attributes for a given register.
    The address is contained only as data used by the RegisterAccess class.

    name: Field name as "PERIPHERAL.REGISTER.FIELD".
    address: Address of the register that contains this field.
    mask: Field mask, does not need to be shifted by shift to get the actual mask.
    shift: Shift ammount for the field data.
    signed: If the field is signed or not.
    """

    def __init__(self, name, parent, access, mask, shift, *, signed=False):
        self.name = name
        self.parent = parent
        self.access = access
        self.mask = mask
        self.shift = shift
        self.signed = signed

    def is_in_bounds(self, value: typing.Union[int, bool]) -> bool:
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
    def __init__(self, name, parent, access, address, signed=False) -> None:
        self.name = name
        self.parent = parent
        self.access = access
        self.address = address
        self.signed = signed
        
    def find(self, name: str) -> Field:
        field = getattr(self, name)
        if not field or not isinstance(field, Field):
            raise ValueError(f"Register {self.get_name()} does not have a field named {name}")

        return field
