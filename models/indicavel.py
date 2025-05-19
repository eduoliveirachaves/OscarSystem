from abc import ABC, abstractmethod

class Indicavel(ABC):

    def __init__(self, nome: str, categorias: list):
        self._nome = nome
        self._categorias = categorias

    @abstractmethod
    def nome(self):
        pass

    @abstractmethod
    def categorias(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
