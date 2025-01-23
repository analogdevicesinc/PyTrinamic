################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

class BitField:

    @staticmethod
    def field_get(data, mask, shift):
        return (data & mask) >> shift

    @staticmethod
    def field_set(data, mask, shift, value):
        return (data & (~mask)) | ((value << shift) & mask)


def to_signed_32(x):
    """Convert any unsigned integer to a 32 bit signed integer."""
    m = x & 0xffffffff
    return (m ^ 0x80000000) - 0x80000000


def to_signed_16(x):
    """Convert any unsigned integer to a 16 bit signed integer."""
    m = x & 0x0000ffff
    return (m ^ 0x00008000) - 0x00008000
