# lets import the abstract class and inherit it in the ChevyVolt class
from autos.abstract_auto import AbstractAuto

class ChevyVolt(AbstractAuto):
    def start(self):
        print('Chevrolet Volt running with shocking power!')

    def stop(self):
        print('Chevrolet Volt shutting down.')