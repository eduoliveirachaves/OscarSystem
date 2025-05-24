from typing import List

from models.categoria import Categoria
from models.indicavel import Indicavel
from models.profissional import Profissional


class Ator(Profissional, Indicavel):
    def __init__(self, id_counter, nome, nacionalidade, data_nascimento: str):
        super().__init__(nome, data_nascimento)
        self.__id = id_counter
        self.__nacionalidade = nacionalidade
        self.__categorias: List[Categoria] = []
        self.__tipo = "Ator/Atriz"

    @property
    def id(self):
        return self.__id

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @property
    def nacionalidade(self):
        return self.__nacionalidade

    @property
    def nome(self):
        return self._nome

    @property
    def tipo(self):
        return self.__tipo

    @property
    def categorias(self):
        return self.__categorias

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento

    @nacionalidade.setter
    def nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def add_categoria(self, categoria):
        self.__categorias.append(categoria)

    def remove_categoria(self, categoria):
        self.__categorias.remove(categoria)

    def __str__(self):
        return (f"ID: [{self.__id}] - {self._nome} - {self._data_nascimento} - "
                f"{self.__nacionalidade} - {self.__tipo}")
