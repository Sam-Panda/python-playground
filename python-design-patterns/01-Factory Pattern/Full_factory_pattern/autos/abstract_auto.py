import abc
# Abstract Class for the Automobile classes. 
# The above two methods are abstract methods, which means 
# that the child/ concrete classes must implement these methods.
class AbstractAuto(abc.ABC):
    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name