from autos.abs_auto import AbsAuto

class FordMustang(AbsAuto):
    def start(self):
        print('Ford Mustang roaring!')
    def stop(self):
        print('Ford Mustang shutting down.')
        