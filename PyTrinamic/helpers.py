'''
Created on 09.01.2019

@author: LK
'''

class TMC_helpers(object):
    
    def field_get(self, data, mask, shift):
        return (data & mask) >> shift
    
    def field_set(self, data, mask, shift, value):
        return (data & (~mask)) | ((value << shift) & mask)
    
    def toSigned32(self, x):
        m = x & 0xffffffff
        return (m ^ 0x80000000) - 0x80000000
