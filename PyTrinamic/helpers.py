'''
Created on 09.01.2019

@author: LK
'''

class TMC_helpers(object):

    @staticmethod
    def field_get(data, mask, shift):
        return (data & mask) >> shift

    @staticmethod
    def field_set(data, mask, shift, value):
        return (data & (~mask)) | ((value << shift) & mask)

    @staticmethod
    def toSigned32(x):
        m = x & 0xffffffff
        return (m ^ 0x80000000) - 0x80000000
