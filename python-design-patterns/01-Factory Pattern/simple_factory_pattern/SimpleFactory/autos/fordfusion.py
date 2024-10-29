from autos.abstract_auto import AbstractAuto

class FordFusion(AbstractAuto):
    def start(self):
        print('Ford Fusion running smoothly.')

    def stop(self):
        print('Ford Fusion shutting down.')