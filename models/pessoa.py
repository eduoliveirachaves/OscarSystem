from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome):
        self.nome = nome

    @property
    @abstractmethod
    def nome(self):
        pass

    @nome.setter
    @abstractmethod
    def nome(self, nome):
        pass