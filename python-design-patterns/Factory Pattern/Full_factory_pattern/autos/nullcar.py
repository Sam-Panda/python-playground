from autos.abstract_auto import AbstractAuto

class NullCar(AbstractAuto):

    def start(self):
        print('Unknown car "%s".' % self.name)

    def stop(self):
        pass
