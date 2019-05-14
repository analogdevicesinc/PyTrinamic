#!/usr/bin/env python3
'''
Print out all available USB and Serial ports that are available for connecting.

Created on 29.04.2019

@author: LH
'''

import PyTrinamic

PyTrinamic.showInfo()

print("USB Ports:")
PyTrinamic.showAvailableComPorts(USB=True)

print("Serial Ports:")
PyTrinamic.showAvailableComPorts(Serial=True)
