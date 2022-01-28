class TMCIc(object):

    def __init__(self):
        self._name = "Unknown"
        self._info = "..."

    def get_name(self):
        return self._name

    def get_info(self):
        return self._info

#    @abc.abstractmethod
#    def writeRegister(self, registerAddress, value):
#        pass

#    @abc.abstractmethod
#    def readRegister(self, registerAddress):
#        pass

#    @abc.abstractmethod
#    def writeRegisterField(self, registerAddress, value, mask, shift):
#        pass

#    @abc.abstractmethod
#    def readRegisterField(self, registerAddress, mask, shift):
#        pass
