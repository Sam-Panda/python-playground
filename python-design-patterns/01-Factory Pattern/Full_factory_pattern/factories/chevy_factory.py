from .abstract_factories import AbstractFactory
from autos.chevyvolt import ChevyVolt

class ChevyFactory(AbstractFactory):
    def create_auto(self):
        self.chevy = ChevyVolt()
        self.chevy.name = 'Chevy Volt'
        return self.chevy
        


