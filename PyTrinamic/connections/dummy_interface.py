'''
Created on 27.05.2019

@author: LH
'''

from PyTrinamic.connections.tmcl_interface import tmcl_interface

class dummy_interface(tmcl_interface):

    def __init__(self, hostID=2, moduleID=1 , debug=True):
        tmcl_interface.__init__(self, hostID, moduleID, debug)

    def _send(self, hostID, moduleID, data):
        pass

    def _recv(self, hostID, moduleID):
        del hostID, moduleID

        return bytearray(9)

interface = dummy_interface()

interface.getVersionString()
interface.sendBoot()
