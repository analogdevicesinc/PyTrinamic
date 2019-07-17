from openhtf.util import validators
from openhtf.util.validators import Equals

class ValuesEqualDict(Equals):
    def __call__(self, values):
        for key, value in values.items():
            if(self._expected.get(key)):
                if(self._expected[key] != value):
                    return False
        return True

validators.register(ValuesEqualDict)
