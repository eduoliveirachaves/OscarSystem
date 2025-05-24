from abc import ABC, abstractmethod



class Indicavel(ABC):
    @abstractmethod
    def nome(self):
        pass

    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def categorias(self):
        pass

    @abstractmethod
    def add_categoria(self, categoria):
        pass

    @abstractmethod
    def remove_categoria(self, categoria):
        pass


    @abstractmethod
    def __str__(self):
        pass
