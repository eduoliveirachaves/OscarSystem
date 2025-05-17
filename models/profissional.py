from abc import ABC, abstractmethod


class Profissional(ABC):
    __id_counter = 1

    def __init__(self, nome: str, data: str):
        self._id = Profissional.__id_counter
        Profissional.__id_counter += 1
        self._nome = nome
        self._data_nascimento = data

    @property
    @abstractmethod
    def nome(self):
        pass

    @nome.setter
    @abstractmethod
    def nome(self, nome):
        pass

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento

