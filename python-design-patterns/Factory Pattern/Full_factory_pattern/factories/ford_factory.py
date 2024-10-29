from .abstract_factories import AbstractFactory
from autos.fordfusion import FordFusion

class FordFactory(AbstractFactory):
    def create_auto(self):
        self.ford = FordFusion()
        self.ford.name = 'Ford Fusion'
        return self.ford