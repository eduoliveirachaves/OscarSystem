from abc import ABC, abstractmethod


class Profissional(ABC):

    def __init__(self, nome: str, data: str):
        self._nome = nome
        self._data_nascimento = data

    @abstractmethod
    def nome(self):
        return self._nome

    @abstractmethod
    def data_nascimento(self):
        return self._data_nascimento

    @abstractmethod
    def __str__(self):
        pass

