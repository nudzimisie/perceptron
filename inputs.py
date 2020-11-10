from abc import ABC, abstractmethod
from utils import PolymorphicClass


class InputPrototype(ABC):
    def __init__(self, data):
        self.value = data

    @property
    def value(self):
        return float(self._value)

    @value.setter
    @abstractmethod
    def value(self, data):
        self._value = data

@PolymorphicClass
class Input(InputPrototype):

    @InputPrototype.value.setter
    def value(self, data):
        self._value = data

class InputFromInt(InputPrototype):
    
    @InputPrototype.value.setter
    def value(self, data):
        self._value = data

class InputFromFloat(InputPrototype):
    
    @InputPrototype.value.setter
    def value(self, data):
        self._value = data

class InputFromBool(InputPrototype):
    
    @InputPrototype.value.setter
    def value(self, data):
        self._value = data