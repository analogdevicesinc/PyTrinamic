'''
Created on 22.02.2019

@author: ed
'''
import abc

class connection_interface(abc.ABC):

    @abc.abstractmethod
    def printInfo(self):
        pass
