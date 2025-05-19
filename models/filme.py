from typing import List

from models.categoria import Categoria
from models.diretor import Diretor
from models.indicavel import Indicavel


class Filme(Indicavel):
    # genero? custo? bilheteria? duracao? elenco?
    def __init__(self, id_counter: int, nome: str, ano_lancamento: int, diretor: Diretor):
        super().__init__(nome, [])
        self.__id = id_counter
        self.__diretor = diretor
        self.__ano_lancamento = ano_lancamento
        self.__elenco = []

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self._nome

    @property
    def diretor(self):
        return self.__diretor

    @property
    def ano_lancamento(self):
        return self.__ano_lancamento

    @property
    def categorias(self):
        return self._categorias

    # quando faz sentido alterar algo como nome, diretor, ano de lancamento?
    # parecem dados imutaveis que nao precisam de setter definido
    # ta aqui de qualquer jeito!

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @diretor.setter
    def diretor(self, diretor):
        self.__diretor = diretor

    @ano_lancamento.setter
    def ano_lancamento(self, ano_lancamento):
        self.__ano_lancamento = ano_lancamento

    def add_categoria_concorrendo(self, categoria: Categoria):
        self._categorias.append(categoria)

    def __str__(self):
        return f"[{self.__id}] {self._nome} - {self.__ano_lancamento} - By {self.__diretor.nome}"
