'''
Created on 18.03.2020

@author: LK
'''

class TMC_EvalShield(object):

    """
    Arguments:
        connection:
            Type: connection interface
            The connection interface used for this module.
        shield:
            Type: class
            The EvalShield class used for every axis on this module.
            For every axis connected, an instance of this class will be created,
            which can be used later.
    """
    def __init__(self, connection, shield, moduleID=1):
        self.GPs = _GPs

        self.shields = []

        while(not(connection.globalParameter(self.GPs.attachedAxes, 0, moduleID))):
            pass
        attachedAxes = connection.globalParameter(self.GPs.attachedAxes, 0, moduleID)
        for i in range(attachedAxes):
            self.shields.append(shield(connection, i, moduleID))

class _GPs():
    attachedAxes = 6
