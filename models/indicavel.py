from abc import ABC, abstractmethod



class Indicavel(ABC):
    @abstractmethod
    def nome(self):
        pass

    @abstractmethod
    def tipo(self):
        pass


    @abstractmethod
    def __str__(self):
        pass
