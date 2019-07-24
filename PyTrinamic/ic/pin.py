class PinState(object):
    @staticmethod
    def from_string(str):
        if(str == "PIN_STATE_LOW"):
            return PinStateLow()
        elif(str == "PIN_STATE_HIGH"):
            return PinStateHigh()
        elif(str == "PIN_STATE_FLOATING"):
            return PinStateFloating()
        else:
            raise ValueError(f"Unknown pin state string \"{str}\"")
    def __str__(self):
        raise NotImplementedError()

class PinStateLow(PinState):
    def __str__(self):
        return "PIN_STATE_LOW"

class PinStateHigh(PinState):
    def __str__(self):
        return "PIN_STATE_HIGH"

class PinStateFloating(PinState):
    def __str__(self):
        return "PIN_STATE_FLOATING"

class Pin(object):
    def __init__(self, pin_state=PinStateFloating()):
        self.__pin_state = pin_state
    def set_pin_state(self, pin_state):
        self.__pin_state = pin_state
    def get_pin_state(self):
        return self.__pin_state
