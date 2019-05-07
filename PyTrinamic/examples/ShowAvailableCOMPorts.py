'''
Created on 29.04.2019

@author: LH
'''

import PyTrinamic

PyTrinamic.showInfo()

print("USB Ports:")
PyTrinamic.showAvailableComPorts(USB=True)

print("Serial Ports:")
PyTrinamic.showAvailableComPorts(Serial=True)