import abc

class AbsFactory(abc.ABC):
    @staticmethod
    def create_economy():
        pass
    
    @staticmethod
    def create_sport():
        pass

    @staticmethod
    def create_luxury():
        pass
