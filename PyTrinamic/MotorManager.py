'''
Created on 09.01.2019

@author: LK
'''

class MotorManager(object):

    @staticmethod
    def motor(axis, handler, features):

        class Motor(*features):
            def __init__(self, axis, handler):
                self.axis = axis
                self.handler = handler

        return Motor(axis, handler)

    @staticmethod
    def motors(*modules):
        return [motor for module in modules for motor in module.MOTORS]
