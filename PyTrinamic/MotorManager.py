'''
Created on 09.01.2019

@author: LK
'''

class MotorManager(object):

    @staticmethod
    def motor(axis, handlers, features, handler=None):

        class Motor(*features):
            def __init__(self, axis, handlers, handler=None):
                self.axis = axis
                self.handlers = handlers
                self.handler = handler if handler else handlers[0]

        return Motor(axis, handlers, handler)

    @staticmethod
    def motors(*modules):
        return [motor for module in modules for motor in module.MOTORS]
