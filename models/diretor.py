from typing import List

from models.categoria import Categoria
from models.indicavel import Indicavel
from models.profissional import Profissional


class Diretor(Profissional, Indicavel):
    def __init__(self, id_counter, nome, data_nascimento):
        super().__init__(nome, data_nascimento)
        self.__id = id_counter
        self.__tipo = "Diretor(a)"

    @property
    def nome(self):
        return self._nome

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @property
    def id(self):
        return self.__id

    @property
    def tipo(self):
        return self.__tipo

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento

    def __str__(self):
        return f"ID: [{self.__id}] - {self._nome} - {self._data_nascimento} - {self.__tipo}"
