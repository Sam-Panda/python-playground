from autos.abs_auto import AbsAuto

class FordFiesta(AbsAuto):
    def start(self):
        print('Ford Fiesta ready to go!')
    def stop(self):
        print('Ford Fiesta shutting down.')

        