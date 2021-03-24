'''
Created on 24.03.2021

@author: LK
'''

class tmcl_module(object):

    def __init__(self, connection, module_id):
        self.MOTORS = []
        self.connection = connection
        self.module_id = module_id
        self.name = ""
        self.desc = ""

    def __str__(self):
        return "{}\{module_id={}\}".format(self.name, self.module_id)

    def showModuleInfo(self):
        print(self)

    " multi axis parameter access "
    def setAxisParameter(self, type, axis, value):
        self.connection.setAxisParameter(type, axis, value, self.module_id)

    def axisParameter(self, type, axis, signed=False):
        return self.connection.axisParameter(type, axis, self.module_id, signed=signed)

    " global parameter access "
    def setGlobalParameter(self, type, bank, value):
        self.connection.setGlobalParameter(type, bank, value, self.module_id)

    def globalParameter(self, type, bank, signed=False):
        return self.connection.globalParameter(type, bank, self.module_id, signed=signed)

    " read inputs "
    def analogInput(self, x):
        return self.connection.analogInput(x, self.moduleID)

    def digitalInput(self, x):
        return self.connection.digitalInput(x, self.moduleID)

    def digitalOutput(self, x):
        return self.connection.digitalOutput(x, self.moduleID)

    " write outputs "
    def setDigitalOutput(self, x):
        return self.connection.setDigitalOutput(x, self.moduleID)

    def clearDigitalOutput(self, x):
        return self.connection.clearDigitalOutput(x, self.moduleID)
