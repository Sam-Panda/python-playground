from .abstract_factories import AbstractFactory
from autos.nullcar import NullCar

class NullFactory(AbstractFactory):

    def create_auto(self):
        self.nullcar = nullcar = NullCar()
        nullcar.name = 'Unknown'
        return nullcar
