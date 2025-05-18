from typing import List

from models.categoria import Categoria
from models.diretor import Diretor


class Filme:
    # genero? custo? bilheteria? duracao? elenco?
    def __init__(self, titulo: str, ano_lancamento: int, diretor: Diretor):
        self.__titulo = titulo
        self.__diretor = diretor
        self.__ano_lancamento = ano_lancamento
        self.__categorias_concorrendo: List[Categoria] = []
        self.__elenco = []

    @property
    def titulo(self):
        return self.__titulo

    @property
    def diretor(self):
        return self.__diretor

    @property
    def ano_lancamento(self):
        return self.__ano_lancamento
    @property
    def categorias_concorrendo(self):
        return self.__categorias_concorrendo

    # quando faz sentido alterar algo como titulo, diretor, ano de lancamento?
    # parecem dados imutaveis que nao precisam de setter definido
    # ta aqui de qualquer jeito!

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @diretor.setter
    def diretor(self, diretor):
        self.__diretor = diretor

    @ano_lancamento.setter
    def ano_lancamento(self, ano_lancamento):
        self.__ano_lancamento = ano_lancamento

    def add_categoria_concorrendo(self, categoria: Categoria):
        self.__categorias_concorrendo.append(categoria)



    def __str__(self):
        return f"{self.titulo} - {self.ano_lancamento} - By {self.diretor}"

