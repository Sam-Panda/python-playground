import abc

class AbstractFactory(abc.ABC):

    @abc.abstractmethod
    def create_auto(self):
        pass