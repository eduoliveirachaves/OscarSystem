from models.diretor import Diretor
from models.indicavel import Indicavel


class Filme(Indicavel):

    # genero? custo? bilheteria? duracao? elenco?
    def __init__(self, id_counter: int, nome: str, ano_lancamento: int, diretor: Diretor):
        self.__nome = nome
        self.__id = id_counter
        self.__diretor = diretor
        self.__ano_lancamento = ano_lancamento
        self.__tipo = "Filme"

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def diretor(self):
        return self.__diretor

    @property
    def ano_lancamento(self):
        return self.__ano_lancamento

    @property
    def tipo(self):
        return self.__tipo

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @diretor.setter
    def diretor(self, diretor):
        self.__diretor = diretor

    @ano_lancamento.setter
    def ano_lancamento(self, ano_lancamento):
        self.__ano_lancamento = ano_lancamento

    def __str__(self):
        return f"[{self.__id}] {self.__nome} - {self.__ano_lancamento} - By {self.__diretor.nome}"
